#!/usr/bin/env python3
"""Lädt die Bonusdateien einmalig von der alten Website und legt sie unter static/bonus/dateien/ ab.

Auf einem Rechner mit normalem Internetzugang ausführen, solange die alte Website noch erreichbar ist:
    python3 tools/bonus_holen.py
Danach neu bauen: python3 build.py
Es werden nur Dateien aus data/bonus.json geholt (Whitelist: pdf, zip, png), sonst nichts von WordPress.
"""
import json
import sys
from pathlib import Path
from urllib.parse import quote
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent.parent
ALT = 'https://www.klhe.de'
ZIEL = ROOT / 'static' / 'bonus' / 'dateien'
ERLAUBT = ('.pdf', '.zip', '.png')


def main():
    ZIEL.mkdir(parents=True, exist_ok=True)
    data = json.loads((ROOT / 'data' / 'bonus.json').read_text(encoding='utf-8'))
    jobs = {}
    for s in data:
        for g in s['gruppen']:
            for it in g['items']:
                if it.get('alt') and it.get('datei'):
                    jobs[it['datei']] = it['alt']
    ok = fehler = 0
    for datei, alt in sorted(jobs.items()):
        if not datei.lower().endswith(ERLAUBT):
            print('übersprungen (Dateityp):', datei)
            continue
        ziel = ZIEL / datei
        if ziel.exists() and ziel.stat().st_size > 0:
            print('schon da:', datei)
            ok += 1
            continue
        url = ALT + quote(alt)
        try:
            with urlopen(Request(url, headers={'User-Agent': 'KLHE-Umzug/1.0'}), timeout=60) as r:
                inhalt = r.read()
            ziel.write_bytes(inhalt)
            print(f'geholt: {datei} ({len(inhalt) // 1024} KB)')
            ok += 1
        except Exception as e:  # noqa: BLE001
            print(f'FEHLER: {datei} ← {url}: {e}')
            fehler += 1
    print(f'\n{ok} Dateien vorhanden, {fehler} Fehler.')
    sys.exit(1 if fehler else 0)


if __name__ == '__main__':
    main()
