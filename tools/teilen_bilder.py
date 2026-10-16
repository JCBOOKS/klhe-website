#!/usr/bin/env python3
"""Erzeugt die Vorschaubilder für geteilte Links (WhatsApp, Facebook, LinkedIn, Messenger).

Für jede eigene Buchseite entsteht static/img/teilen/<slug>.jpg (1200 x 630 Pixel):
das Cover auf der Pastellfarbe der Kategorie, dahinter ein zweites Blatt, unten rechts das KLHE-Logo.
Dazu kommt static/img/teilen/klhe.jpg als Vorschaubild für alle anderen Seiten.
build.py nimmt das Buchbild als og:image, wenn es existiert, sonst klhe.jpg.

Nur nötig, wenn ein Buch oder ein Cover dazukommt oder sich ändert (braucht Pillow):
    pip install pillow
    python3 tools/teilen_bilder.py            # nur fehlende Bilder
    python3 tools/teilen_bilder.py --alle     # alle neu
"""
import argparse
import csv
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
COVER = ROOT / 'static' / 'img' / 'cover'
ZIEL = ROOT / 'static' / 'img' / 'teilen'
LOGO = ROOT / 'static' / 'img' / 'logo' / 'klhe-schwarz.png'
W, H = 1200, 630
# Pastelltöne deckend (wie im Stylesheet auf Weiß)
FARBE = {'flieder': (232, 228, 249), 'rose': (252, 229, 236), 'mint': (225, 244, 238), 'apricot': (253, 233, 220), 'pistazie': (238, 244, 223)}
ZWEITE = {'flieder': 'apricot', 'rose': 'flieder', 'mint': 'flieder', 'apricot': 'flieder', 'pistazie': 'mint'}


def blatt(groesse, farbe, winkel):
    """Abgerundete Fläche, leicht gedreht (wie die Transparentpapier-Blätter der Website)."""
    w, h = groesse
    im = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    ImageDraw.Draw(im).rounded_rectangle((0, 0, w - 1, h - 1), radius=46, fill=farbe + (255,))
    return im.rotate(winkel, resample=Image.BICUBIC, expand=True)


def bild(slug, cover_datei, tint):
    grund = FARBE.get(tint, FARBE['flieder'])
    im = Image.new('RGB', (W, H), (252, 251, 250))
    leinwand = im.convert('RGBA')
    # zwei Blätter
    b1 = blatt((760, 560), grund, -4)
    leinwand.alpha_composite(b1, ((W - b1.width) // 2 - 60, (H - b1.height) // 2 + 6))
    b2 = blatt((520, 470), FARBE[ZWEITE.get(tint, 'flieder')], 5)
    leinwand.alpha_composite(b2, ((W - b2.width) // 2 + 210, (H - b2.height) // 2 - 10))
    # Cover mit Schatten
    c = Image.open(cover_datei).convert('RGBA')
    ch = 500
    cw = round(c.width * ch / c.height)
    if cw > 620:  # sehr breite Cover (z. B. quadratische Kinderbücher)
        cw = 620
        ch = round(c.height * cw / c.width)
    c = c.resize((cw, ch), Image.LANCZOS)
    x, y = (W - cw) // 2, (H - ch) // 2
    schatten = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(schatten).rounded_rectangle((x + 6, y + 22, x + cw + 6, y + ch + 22), radius=8, fill=(34, 35, 42, 95))
    leinwand.alpha_composite(schatten.filter(ImageFilter.GaussianBlur(18)))
    leinwand.alpha_composite(c, (x, y))
    # Logo unten rechts
    logo = Image.open(LOGO).convert('RGBA')
    lh = 30
    logo = logo.resize((round(logo.width * lh / logo.height), lh), Image.LANCZOS)
    leinwand.alpha_composite(logo, (W - logo.width - 44, H - lh - 36))
    ZIEL.mkdir(parents=True, exist_ok=True)
    leinwand.convert('RGB').save(ZIEL / f'{slug}.jpg', quality=84, optimize=True, progressive=True)


def standardbild():
    """Vorschaubild für alle anderen Seiten: drei Cover aufgefächert, KLHE-Logo."""
    im = Image.new('RGBA', (W, H), (252, 251, 250, 255))
    for b, x, y in ((blatt((700, 520), FARBE['flieder'], -5), 120, 40), (blatt((560, 470), FARBE['apricot'], 4), 520, 70)):
        im.alpha_composite(b, (x, y))
    # links, rechts, dann die Mitte obenauf
    for slug, winkel, mitte_x, hoehe in (('bei-gegenwind-loslaufen', -9, 370, 360), ('mein-besuch-beim-kinderarzt', 9, 830, 330), ('die-faulbaer-strategie-zur-million', 0, 600, 430)):
        c = Image.open(COVER / f'{slug}.webp').convert('RGBA')
        ch = hoehe
        cw = round(c.width * ch / c.height)
        c = c.resize((cw, ch), Image.LANCZOS)
        rahmen = Image.new('RGBA', (cw + 80, ch + 80), (0, 0, 0, 0))
        ImageDraw.Draw(rahmen).rounded_rectangle((46, 62, cw + 40, ch + 60), radius=8, fill=(34, 35, 42, 90))
        rahmen = rahmen.filter(ImageFilter.GaussianBlur(16))
        rahmen.alpha_composite(c, (40, 40))
        rahmen = rahmen.rotate(-winkel, resample=Image.BICUBIC, expand=True)
        im.alpha_composite(rahmen, (mitte_x - rahmen.width // 2, (H - rahmen.height) // 2 + 8))
    logo = Image.open(LOGO).convert('RGBA')
    logo = logo.resize((round(logo.width * 30 / logo.height), 30), Image.LANCZOS)
    im.alpha_composite(logo, (W - logo.width - 44, H - 30 - 36))
    ZIEL.mkdir(parents=True, exist_ok=True)
    im.convert('RGB').save(ZIEL / 'klhe.jpg', quality=84, optimize=True, progressive=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--alle', action='store_true', help='alle Bilder neu erzeugen')
    args = ap.parse_args()
    kats = {k['id']: k['tint'] for k in json.loads((ROOT / 'data' / 'kategorien.json').read_text(encoding='utf-8'))}
    neu = 0
    with open(ROOT / 'data' / 'buecher.csv', encoding='utf-8', newline='') as f:
        for r in csv.DictReader(f):
            if r['seite'] != 'eigen' or not r['cover']:
                continue
            quelle = COVER / f'{r["cover"]}.webp'
            ziel = ZIEL / f'{r["slug"]}.jpg'
            if not quelle.exists() or (ziel.exists() and not args.alle and ziel.stat().st_mtime >= quelle.stat().st_mtime):
                continue
            bild(r['slug'], quelle, kats.get(r['kategorie'], 'flieder'))
            neu += 1
    if args.alle or not (ZIEL / 'klhe.jpg').exists():
        standardbild()
        neu += 1
    print(f'{neu} Vorschaubilder erzeugt in static/img/teilen/')


if __name__ == '__main__':
    main()
