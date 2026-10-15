#!/usr/bin/env python3
"""Holt die 31 Bonusdateien einmalig und legt sie umbenannt unter static/bonus/dateien/ ab.
Verknüpfen muss niemand etwas: build.py findet die Dateien dort und verlinkt sie auf /bonus/.

Zwei Wege, je nachdem, was einfacher ist:

  A) Aus dem FTP-Download (empfohlen, wenn die alte Seite schon abgeschaltet ist):
     Den Ordner wp-content/uploads per FTP komplett herunterladen (einfach den ganzen Ordner ziehen),
     dann:  python3 tools/bonus_holen.py --ordner /Pfad/zum/heruntergeladenen/uploads
     Das Skript sucht die 31 Dateien darin selbst heraus. Alles andere bleibt unberührt.

  B) Direkt von der alten Website, solange klhe.de noch läuft:
     python3 tools/bonus_holen.py

Danach neu bauen: python3 build.py --check
Es werden nur die Dateien aus data/bonus.json übernommen (nur pdf, zip, png), nichts sonst aus WordPress.
"""
import argparse
import json
import shutil
import sys
import unicodedata
from pathlib import Path
from urllib.parse import quote
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent.parent
ALT = 'https://www.klhe.de'
ZIEL = ROOT / 'static' / 'bonus' / 'dateien'
ERLAUBT = ('.pdf', '.zip', '.png')
PRAEFIX = '/wp-content/uploads/'


def nfc(s):
    return unicodedata.normalize('NFC', s)


def auftraege():
    data = json.loads((ROOT / 'data' / 'bonus.json').read_text(encoding='utf-8'))
    jobs = {}
    for s in data:
        for g in s['gruppen']:
            for it in g['items']:
                if it.get('alt') and it.get('datei'):
                    jobs[it['datei']] = it['alt']
    return jobs


def aus_ordner(ordner, jobs):
    """Sucht jede Datei im heruntergeladenen Ordner: erst über den Pfad (2019/03/…), sonst über den Dateinamen."""
    ordner = Path(ordner).expanduser()
    if not ordner.is_dir():
        sys.exit(f'Ordner nicht gefunden: {ordner}')
    nach_pfad, nach_name = {}, {}
    for f in ordner.rglob('*'):
        if f.is_file():
            rel = nfc(f.relative_to(ordner).as_posix())
            nach_pfad[rel] = f
            nach_name.setdefault(nfc(f.name), []).append(f)
    ok, fehlt = 0, []
    for datei, alt in sorted(jobs.items()):
        rel = nfc(alt[len(PRAEFIX):] if alt.startswith(PRAEFIX) else alt.lstrip('/'))
        treffer = None
        for key, f in nach_pfad.items():  # Pfad passt, egal ob der Ordner bei uploads/ oder höher beginnt
            if key == rel or key.endswith('/' + rel):
                treffer = f
                break
        if not treffer:
            kandidaten = nach_name.get(nfc(Path(rel).name), [])
            treffer = kandidaten[0] if len(kandidaten) == 1 else None
        if treffer:
            shutil.copyfile(treffer, ZIEL / datei)
            print(f'übernommen: {datei}  ←  {treffer.relative_to(ordner)}')
            ok += 1
        else:
            fehlt.append((datei, alt))
    return ok, fehlt


def aus_web(jobs):
    ok, fehlt = 0, []
    for datei, alt in sorted(jobs.items()):
        url = ALT + quote(alt)
        try:
            with urlopen(Request(url, headers={'User-Agent': 'KLHE-Umzug/1.0'}), timeout=60) as r:
                inhalt = r.read()
            (ZIEL / datei).write_bytes(inhalt)
            print(f'geholt: {datei} ({len(inhalt) // 1024} KB)')
            ok += 1
        except Exception as e:  # noqa: BLE001
            print(f'Fehler bei {datei}: {e}')
            fehlt.append((datei, alt))
    return ok, fehlt


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--ordner', help='heruntergeladener Ordner wp-content/uploads (oder ein Ordner darüber)')
    args = ap.parse_args()
    ZIEL.mkdir(parents=True, exist_ok=True)
    jobs = {d: a for d, a in auftraege().items() if d.lower().endswith(ERLAUBT)}
    ok, fehlt = aus_ordner(args.ordner, jobs) if args.ordner else aus_web(jobs)
    print(f'\n{ok} von {len(jobs)} Bonusdateien liegen jetzt in static/bonus/dateien/.')
    if fehlt:
        print('Nicht gefunden (alter Pfad unter wp-content/uploads):')
        for datei, alt in fehlt:
            print(f'  {alt}  →  {datei}')
    print('Jetzt neu bauen: python3 build.py --check')
    sys.exit(1 if fehlt else 0)


if __name__ == '__main__':
    main()
