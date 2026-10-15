#!/usr/bin/env python3
"""KLHE Website: statischer Generator.

    python3 build.py           baut die Website nach public/
    python3 build.py --check   baut und prüft zusätzlich alle internen Links

Quellen: data/*.csv und data/*.json (Inhalte), templates/ (Seiten), static/ (CSS, Schrift, Bilder, Bonusdateien).
"""
import csv
import html
import json
import re
import shutil
import sys
from datetime import date
from pathlib import Path
from urllib.parse import quote, urlsplit

from jinja2 import Environment, FileSystemLoader, StrictUndefined

ROOT = Path(__file__).resolve().parent
DATA, TPL, STATIC, OUT = ROOT / 'data', ROOT / 'templates', ROOT / 'static', ROOT / 'public'

SITE = {
    'url': 'https://www.klhe.de',          # Hauptadresse (mit www wie bisher)
    'name': 'KLHE',
    'claim': 'Bücher, die bewegen.',
    'mail': 'info@klhe.de',
    'tel': '0211 53804066',
    'tel_link': '+4921153804066',
    'firma': 'GbR C. Klein & J. Helbig',
    'strasse': 'Hortensienstraße 26',
    'ort': '40474 Düsseldorf',
    'ust': 'DE320046102',
    'amazon_tag': 'jcbooks04-21',
    'instagram': 'https://www.instagram.com/klhe_verlag/',
    'facebook': 'https://www.facebook.com/KLHE.Verlag/',
    'buchbuddy': 'https://buchbuddy.de/',
    'jahr': date.today().year,
    'stand': '15. Oktober 2026',
}

# Startseite: drei bewegte Cover-Spalten (Gestaltung v5)
WALL = [
    ['bei-gegenwind-loslaufen', 'mein-besuch-beim-kinderarzt', 'die-faulbaer-strategie-zur-million', 'kuschelige-momente-4', 'einmal-himmel-und-zurueck-zu-mir', 'golf-unnuetzes-wissen', 'psychedelika'],
    ['mein-besuch-beim-tierarzt', 'finde-dein-warum-und-lebe', 'kuschelige-momente-2', 'kleine-redner-grosse-worte', 'mutmacherinnen', 'affe-loki-und-die-reise-zur-schatzinsel', 'nuernberg-guide'],
    ['elfe-filia-regelt-das', 'tennis-unnuetzes-wissen', 'mein-besuch-beim-augenarzt', 'mit-blockchain-zum-krypto-investor', 'kuschelige-momente-5', 'die-verlorenen-jahre', 'das-witzige-sport-mitmachbuch'],
]
# Reihenfolge der Reihen-Karten im Programm je Kategorie
SERIES_IN_CAT = {'ratgeber': ['finanzreihe'], 'kinderbuecher': ['mutmachbuecher', 'mitmachbuecher'], 'ausmalbuecher': ['kuschelige-momente'], 'geschenkbuecher': ['unnuetzes-wissen']}
FINANZ_PRESSE = ['focus-money-2018', 'jolie', 'eve-2020', 'bank-und-umwelt-2018', 'rhein-main-magazin-2020']
START_PRESSE = ['focus-money-2018', 'tagesspiegel-2025', 'prisma-2022', 'tina-2023', 'eve-2020', 'chance-2020']
TAGCLS = {'ratgeber': 'flieder', 'lebensgeschichten': 'apricot', 'kinderbuecher': 'mint', 'ausmalbuecher': 'rose', 'geschenkbuecher': 'pistazie', 'reisen': 'apricot'}
KAT_EINZAHL = {'ratgeber': 'Ratgeber', 'lebensgeschichten': 'Lebensgeschichte', 'kinderbuecher': 'Kinderbuch', 'ausmalbuecher': 'Ausmalbuch', 'geschenkbuecher': 'Geschenkbuch', 'reisen': 'Reisen'}

warnings = []


def warn(msg):
    warnings.append(msg)


# ---------------------------------------------------------------- Daten
def ja(v):
    return (v or '').strip().lower() in ('ja', 'x', '1', 'true')


def names(s):
    parts = [p.strip() for p in (s or '').split(';') if p.strip()]
    if len(parts) <= 1:
        return ''.join(parts)
    return ', '.join(parts[:-1]) + ' und ' + parts[-1]


def amazon(asin):
    asin = (asin or '').strip()
    return f'https://www.amazon.de/dp/{asin}?tag={SITE["amazon_tag"]}' if asin else ''


def load():
    kats = json.loads((DATA / 'kategorien.json').read_text(encoding='utf-8'))
    reihen = json.loads((DATA / 'reihen.json').read_text(encoding='utf-8'))
    presse = json.loads((DATA / 'presse.json').read_text(encoding='utf-8'))
    bonus = json.loads((DATA / 'bonus.json').read_text(encoding='utf-8'))
    kat_by = {k['id']: k for k in kats}
    reihe_by = {r['id']: r for r in reihen}
    presse_by = {p['id']: p for p in presse}
    books = []
    with open(DATA / 'buecher.csv', encoding='utf-8', newline='') as f:
        for i, r in enumerate(csv.DictReader(f)):
            b = {k: (v or '').strip() for k, v in r.items()}
            b['pos'] = i
            if b['kategorie'] not in kat_by:
                raise SystemExit(f'buecher.csv: unbekannte Kategorie „{b["kategorie"]}“ bei {b["slug"]}')
            if b['reihe'] and b['reihe'] not in reihe_by:
                raise SystemExit(f'buecher.csv: unbekannte Reihe „{b["reihe"]}“ bei {b["slug"]}')
            b['kat'] = kat_by[b['kategorie']]
            b['tint'] = b['kat']['tint']
            b['kat_einzahl'] = KAT_EINZAHL[b['kategorie']]
            b['reihe_obj'] = reihe_by.get(b['reihe'])
            b['autoren'] = names(b['autorin'])
            b['autoren_liste'] = [p.strip() for p in b['autorin'].split(';') if p.strip()]
            b['amazon_url'] = amazon(b['amazon'])
            b['im_buchhandel'] = ja(b['buchhandel'])
            b['hat_hoerbuch'] = ja(b['hoerbuch'])
            b['ist_uebersetzt'] = ja(b['uebersetzt'])
            b['ist_neu'] = ja(b['neu'])
            b['formate_liste'] = [x.strip() for x in b['formate'].split(';') if x.strip()]
            b['voller_titel'] = b['titel'] + (f': {b["untertitel"]}' if b['seite'] == 'reihe' and b['reihe'] == 'kuschelige-momente' else '')
            img = STATIC / 'img' / 'cover' / f'{b["cover"]}.webp' if b['cover'] else None
            if img and not img.exists():
                warn(f'Cover fehlt: {img.relative_to(ROOT)}')
                img = None
            b['img'] = f'/img/cover/{b["cover"]}.webp' if img else ''
            if b['seite'] == 'eigen':
                b['url'] = f'/buecher/{b["slug"]}/'
            elif b['seite'] == 'reihe':
                b['url'] = f'/reihen/{b["reihe"]}/#{b["slug"]}'
            else:
                b['url'] = b['amazon_url']
            b['extern'] = b['seite'] == 'backlist'
            b['badges'] = (['Im Buchhandel'] if b['im_buchhandel'] else []) + (['Hörbuch'] if b['hat_hoerbuch'] else [])
            b['presse_liste'] = [presse_by[p] for p in b['presse'].split(';') if p.strip() in presse_by]
            for p in b['presse'].split(';'):
                if p.strip() and p.strip() not in presse_by:
                    warn(f'{b["slug"]}: Presse-ID „{p}“ nicht in presse.json')
            if b['seite'] in ('eigen', 'reihe') and not b['amazon_url']:
                warn(f'{b["slug"]}: kein Amazon-Link')
            books.append(b)
    slug_by = {b['slug']: b for b in books}
    if len(slug_by) != len(books):
        raise SystemExit('buecher.csv: doppelter slug')
    for r in reihen:
        r['buecher'] = sorted([b for b in books if b['reihe'] == r['id']], key=lambda b: (int(b['band']) if b['band'].isdigit() else 99, b['pos']))
        r['url'] = f'/reihen/{r["id"]}/'
        r['fach_imgs'] = [slug_by[s]['img'] for s in r['fach'] if slug_by.get(s) and slug_by[s]['img']]
    for k in kats:
        k['url'] = f'/buecher/#{k["id"]}'
        k['start_imgs'] = [slug_by[s]['img'] for s in k['start'] if slug_by.get(s) and slug_by[s]['img']]
    return dict(kats=kats, kat_by=kat_by, reihen=reihen, reihe_by=reihe_by, presse=presse, presse_by=presse_by, bonus=bonus, books=books, slug_by=slug_by)


# ---------------------------------------------------------------- Seiten
def page_meta(title, desc, path, **kw):
    d = {'title': title, 'desc': desc, 'path': path, 'canonical': SITE['url'] + path, 'noindex': False, 'og_image': SITE['url'] + '/img/foto/chris-jens-buehne.webp', 'nav': '', 'jsonld': None}
    d.update(kw)
    return d


def short(text, n=155):
    text = re.sub(r'\s+', ' ', text or '').strip()
    if len(text) <= n:
        return text
    cut = text[:n].rsplit(' ', 1)[0].rstrip(',;:')
    return cut + ' …'


def book_jsonld(b):
    d = {'@context': 'https://schema.org', '@type': 'Book', 'name': b['titel'], 'inLanguage': 'de',
         'publisher': {'@type': 'Organization', 'name': 'KLHE', 'url': SITE['url'] + '/'},
         'url': SITE['url'] + b['url']}
    if b['untertitel']:
        d['alternativeHeadline'] = b['untertitel']
    if b['autoren_liste']:
        d['author'] = [{'@type': 'Person', 'name': re.sub(r'\s*\(Hrsg\.\)', '', a)} for a in b['autoren_liste']]
    if b['isbn']:
        d['isbn'] = b['isbn']
    if b['seiten'].isdigit():
        d['numberOfPages'] = int(b['seiten'])
    if b['img']:
        d['image'] = SITE['url'] + b['img']
    if b['klappentext']:
        d['description'] = b['klappentext']
    return json.dumps(d, ensure_ascii=False)


def org_jsonld():
    return json.dumps({'@context': 'https://schema.org', '@type': 'Organization', 'name': 'KLHE', 'legalName': SITE['firma'], 'url': SITE['url'] + '/',
                       'logo': SITE['url'] + '/img/logo/klhe-schwarz.png', 'email': SITE['mail'], 'telephone': SITE['tel'], 'foundingDate': '2011',
                       'address': {'@type': 'PostalAddress', 'streetAddress': SITE['strasse'], 'postalCode': '40474', 'addressLocality': 'Düsseldorf', 'addressCountry': 'DE'},
                       'sameAs': [SITE['instagram'], SITE['facebook']]}, ensure_ascii=False)


def build():
    d = load()
    books, slug_by, reihe_by = d['books'], d['slug_by'], d['reihe_by']
    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(STATIC, OUT, ignore=shutil.ignore_patterns('.gitkeep', '.DS_Store'))

    env = Environment(loader=FileSystemLoader(TPL), autoescape=True, undefined=StrictUndefined, trim_blocks=True, lstrip_blocks=True)
    env.globals.update(site=SITE, reihen=d['reihen'], kats=d['kats'])
    env.filters['urlq'] = lambda s: quote(s)
    pages = []

    def render(tpl, path, meta, **ctx):
        target = OUT / path.lstrip('/') / 'index.html' if path.endswith('/') else OUT / path.lstrip('/')
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(env.get_template(tpl).render(meta=meta, **ctx), encoding='utf-8')
        pages.append((path, meta))

    def pick(slugs):
        return [slug_by[s] for s in slugs if s in slug_by]

    # Startseite
    wall = [[slug_by[s]['img'] for s in col if slug_by.get(s) and slug_by[s]['img']] for col in WALL]
    picks = sorted([b for b in books if b['empfohlen']], key=lambda b: int(b['empfohlen']) if b['empfohlen'].isdigit() else 99)
    render('index.html', '/', page_meta('KLHE · Bücher, die bewegen.', 'KLHE ist ein unabhängiger Verlag aus Düsseldorf, seit 2011: Ratgeber, Lebensgeschichten, Kinder- und Ausmalbücher, bestellbar im Buchhandel.', '/', jsonld=org_jsonld()),
           wall=wall, picks=picks, start_reihen=[r for r in d['reihen'] if r.get('start')], mitmach=reihe_by['mitmachbuecher'],
           clips=[d['presse_by'][p] for p in START_PRESSE])

    # Programm
    sections = []
    for k in d['kats']:
        series = [reihe_by[r] for r in SERIES_IN_CAT.get(k['id'], [])]
        items = [b for b in books if b['kategorie'] == k['id'] and b['seite'] == 'eigen' and not b['reihe']]
        backlist = [b for b in books if b['kategorie'] == k['id'] and b['seite'] == 'backlist']
        sections.append({'k': k, 'series': series, 'titel': items, 'backlist': backlist})
    render('buecher.html', '/buecher/', page_meta('Unsere Bücher · KLHE', 'Alle Bücher von KLHE: Ratgeber, Lebensgeschichten, Kinder-, Ausmal- und Geschenkbücher. Die meisten sind in jeder Buchhandlung bestellbar.', '/buecher/', nav='buecher'),
           sections=sections)

    # Buchseiten
    for b in books:
        if b['seite'] != 'eigen':
            continue
        if b['reihe']:
            more = [x for x in b['reihe_obj']['buecher'] if x['slug'] != b['slug']]
            more_title, more_link = f'Mehr aus der Reihe „{b["reihe_obj"]["kurzname"]}“', b['reihe_obj']['url']
        else:
            more = [x for x in books if x['kategorie'] == b['kategorie'] and x['slug'] != b['slug'] and x['seite'] in ('eigen', 'reihe') and x['img']]
            more_title, more_link = f'Mehr {b["kat"]["name"]}', b['kat']['url']
        # gleichmäßig verteilt statt immer die ersten
        if len(more) > 6:
            start = b['pos'] % len(more)
            more = (more[start:] + more[:start])[:6]
        img_abs = SITE['url'] + b['img'] if b['img'] else SITE['url'] + '/img/foto/chris-jens-buehne.webp'
        title = f'{b["titel"]}' + (f' von {b["autoren"]}' if b['autoren'] else '') + ' · KLHE'
        render('buch.html', b['url'], page_meta(title, short(b['klappentext']) or b['untertitel'], b['url'], nav='buecher', og_image=img_abs, jsonld=book_jsonld(b)),
               b=b, more=more, more_title=more_title, more_link=more_link)

    # Reihen
    others = lambda rid: [r for r in d['reihen'] if r['id'] != rid]
    for r in d['reihen']:
        tpl = {'finanzreihe': 'reihe-finanzreihe.html', 'mutmachbuecher': 'reihe-mutmachbuecher.html', 'kuschelige-momente': 'reihe-kuschelige-momente.html'}.get(r['id'], 'reihe.html')
        extra = {}
        if r['id'] == 'finanzreihe':
            extra['clips'] = [d['presse_by'][p] for p in FINANZ_PRESSE]
        if r['id'] == 'mutmachbuecher':
            extra['kids'] = pick(['das-witzige-sport-mitmachbuch', 'das-tierische-mitmachbuch', 'die-wuselbande-sucht-das-gaehnen', 'mama-wer-wohnt-eigentlich-auf-dem-bauernhof', 'affe-loki-und-die-reise-zur-schatzinsel', 'das-total-verrueckte-suchbuch'])
        desc = r['text'] if 'intro' not in r else short(r['intro'])
        render(tpl, r['url'], page_meta(f'{r["name"]} · KLHE', desc, r['url'], nav='reihen'), r=r, others=others(r['id']), **extra)

    # Verlag, Autor:innen, Kontakt
    render('verlag.html', '/verlag/', page_meta('Der Verlag · KLHE', 'KLHE ist ein unabhängiger Verlag aus Düsseldorf, gegründet 2011 von Christopher Klein und Jens Helbig. Die Geschichte des Verlags.', '/verlag/', nav='verlag'),
           heute=pick(['bei-gegenwind-loslaufen', 'einmal-himmel-und-zurueck-zu-mir', 'mein-besuch-beim-kinderarzt', 'elfe-filia-regelt-das']))
    render('autoren.html', '/autoren/', page_meta('Für Autorinnen und Autoren · KLHE', 'Bei einem Verlag erscheinen: ISBN, Eintrag im VLB, Barsortimente Libri, Zeitfracht und Umbreit und eine eigene Verlagsauslieferung.', '/autoren/', nav='autoren'),
           shelf=pick(['bei-gegenwind-loslaufen', 'einmal-himmel-und-zurueck-zu-mir', 'kleine-redner-grosse-worte', 'elfe-filia-regelt-das', 'ausgeschieden', 'englische-grammatik-1']))
    render('kontakt.html', '/kontakt/', page_meta('Kontakt · KLHE', 'So erreichst Du KLHE: per E-Mail an info@klhe.de oder telefonisch. Für Leserinnen und Leser, Buchhandel, Presse und Autorinnen und Autoren.', '/kontakt/', nav='kontakt'))

    # Bonus
    missing = set()
    for s in d['bonus']:
        n_files = n_links = 0
        for g in s['gruppen']:
            for it in g['items']:
                if it.get('url'):
                    it['href'], it['go'] = it['url'], 'Öffnen'
                    n_links += 1
                elif it['datei']:
                    exists = (STATIC / 'bonus' / 'dateien' / it['datei']).exists()
                    it['href'] = f'/bonus/dateien/{it["datei"]}' if exists else ''
                    it['go'] = 'Herunterladen' if exists else ''
                    if exists:
                        n_files += 1
                    else:
                        missing.add(it['datei'])
                else:
                    it['href'], it['go'] = '', ''
        lang = s.get('lang', 'de')
        word = {'de': ('Download', 'Downloads'), 'en': ('download', 'downloads'), 'es': ('descarga', 'descargas'), 'it': ('download', 'download'), 'fr': ('téléchargement', 'téléchargements')}[lang]
        parts = []
        if n_files:
            parts.append(f'{n_files} {word[0] if n_files == 1 else word[1]}')
        if n_links:
            parts.append(f'{n_links} Link' if n_links == 1 else f'{n_links} Links')
        s['count'] = ', '.join(parts) or 'folgt'
    if missing:
        warn(f'{len(missing)} Bonusdateien fehlen noch in static/bonus/dateien/ und erscheinen als „folgt“. Holen mit: python3 tools/bonus_holen.py')
    render('bonus.html', '/bonus/', page_meta('Bonusmaterial · KLHE', 'Zusatzmaterial zu Büchern und Hörbüchern von KLHE, ohne Anmeldung zum Herunterladen.', '/bonus/', noindex=True), bonus=d['bonus'])

    # Recht
    render('impressum.html', '/impressum/', page_meta('Impressum · KLHE', 'Impressum von KLHE, GbR C. Klein & J. Helbig, Düsseldorf.', '/impressum/'))
    render('datenschutz.html', '/datenschutz/', page_meta('Datenschutz · KLHE', 'Datenschutzerklärung von KLHE: keine Cookies, kein Tracking.', '/datenschutz/'))
    render('404.html', '/404.html', page_meta('Seite nicht gefunden · KLHE', 'Diese Seite gibt es nicht (mehr).', '/404.html', noindex=True),
           picks=pick(['kleine-redner-grosse-worte', 'bei-gegenwind-loslaufen', 'psychedelika', 'die-faulbaer-strategie-zur-million', 'elfe-filia-regelt-das', 'mein-besuch-beim-tierarzt']))

    write_sitemap(pages)
    (OUT / 'robots.txt').write_text(f'User-agent: *\nAllow: /\nDisallow: /bonus/dateien/\n\nSitemap: {SITE["url"]}/sitemap.xml\n', encoding='utf-8')
    write_redirects()
    return pages


def write_sitemap(pages):
    today = date.today().isoformat()
    urls = [p for p, m in pages if not m['noindex'] and p.endswith('/')]
    body = '\n'.join(f'  <url><loc>{html.escape(SITE["url"] + p)}</loc><lastmod>{today}</lastmod></url>' for p in sorted(urls))
    (OUT / 'sitemap.xml').write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{body}\n</urlset>\n', encoding='utf-8')


# ---------------------------------------------------------------- Weiterleitungen
GONE_PATTERNS = [
    r'^wp-admin(/.*)?$', r'^wp-includes(/.*)?$', r'^wp-json(/.*)?$', r'^wp-content/(.*)$',
    r'^(wp-login|wp-cron|wp-config|wp-signup|wp-trackback|xmlrpc)\.php$', r'^(readme\.html|license\.txt)$',
    r'^(.*/)?feed/?$', r'^comments/feed/?$',
]
ARCHIVE_PATTERNS = [r'^(category|project_category|project_tag|product-category|type|author|tag|page)/.*$']


def apache_pattern(path):
    p = path.lstrip('/')
    slash = p.endswith('/')
    p = p.rstrip('/')
    esc = re.sub(r'([.^$*+?()\[\]{}|\\])', r'\\\1', p).replace(' ', '\\ ')
    return '^' + esc + ('/?$' if slash else '$')


def write_redirects():
    rows = list(csv.DictReader(open(DATA / 'redirects.csv', encoding='utf-8', newline='')))
    ht = [
        '# KLHE · erzeugt von build.py, nicht von Hand ändern (Quelle: data/redirects.csv)',
        'ErrorDocument 404 /404.html',
        'ErrorDocument 410 /404.html',
        'Options -Indexes',
        'AddDefaultCharset utf-8',
        'AddType font/woff .woff',
        'AddType image/webp .webp',
        '',
        '<IfModule mod_headers.c>',
        '  Header always set X-Content-Type-Options "nosniff"',
        '  Header always set Referrer-Policy "strict-origin-when-cross-origin"',
        '  Header always set X-Frame-Options "SAMEORIGIN"',
        '  <FilesMatch "\\.(css|woff|webp|png|jpg|svg|ico)$">',
        '    Header set Cache-Control "public, max-age=2592000"',
        '  </FilesMatch>',
        '</IfModule>',
        '',
        'RewriteEngine On',
        '',
        '# Hauptadresse erzwingen (erst aktivieren, wenn HTTPS und www eingerichtet sind)',
        '# RewriteCond %{HTTPS} off [OR]',
        '# RewriteCond %{HTTP_HOST} !^www\\.klhe\\.de$ [NC]',
        '# RewriteRule ^(.*)$ https://www.klhe.de/$1 [R=301,L]',
        '',
        '# 1. Alte Adressen einzeln (301, Abfrage-Parameter wie ?fbclid werden verworfen)',
    ]
    nl = ['# KLHE · erzeugt von build.py (Format für Cloudflare Pages / Netlify)']
    for r in rows:
        pat = apache_pattern(r['alt'])
        if r['code'] == '410':
            ht.append(f'RewriteRule "{pat}" - [G,L]')
        else:
            ht.append(f'RewriteRule "{pat}" "{r["neu"]}" [R=301,L,NE,QSD]')
            alt = quote(r['alt'], safe='/-_.~')
            nl.append(f'{alt} {r["neu"]} 301')
            if r['alt'].endswith('/'):
                nl.append(f'{alt.rstrip("/")} {r["neu"]} 301')
    ht += ['', '# 2. Archivseiten von WordPress (Kategorien, Schlagwörter, Autoren)']
    ht += [f'RewriteRule "{p}" "/buecher/" [R=301,L,QSD]' for p in ARCHIVE_PATTERNS]
    ht += ['', '# 3. WordPress-Reste und Adressen aus dem Hack: dauerhaft weg (410)']
    ht += [f'RewriteRule "{p}" - [G,L]' for p in GONE_PATTERNS]
    for p in ['/category/*', '/project_category/*', '/project_tag/*', '/product-category/*', '/type/*', '/author/*']:
        nl.append(f'{p} /buecher/ 301')
    (OUT / '.htaccess').write_text('\n'.join(ht) + '\n', encoding='utf-8')
    (OUT / '_redirects').write_text('\n'.join(nl) + '\n', encoding='utf-8')
    # Prüfen: Ziele existieren
    for r in rows:
        if r['code'] == '410':
            continue
        target = urlsplit(r['neu']).path
        if target.startswith('/bonus/dateien/'):
            continue  # fehlende Bonusdateien meldet schon der Bonus-Abschnitt
        if not exists(target):
            warn(f'Weiterleitung zeigt ins Leere: {r["alt"]} → {r["neu"]}')


# ---------------------------------------------------------------- Prüfung
def exists(path):
    if not path.startswith('/'):
        return True
    p = OUT / path.lstrip('/')
    if path.endswith('/'):
        return (p / 'index.html').exists()
    return p.exists() or (p / 'index.html').exists()


def check_links():
    bad = []
    ids_cache = {}
    for f in OUT.rglob('*.html'):
        text = f.read_text(encoding='utf-8')
        for m in re.finditer(r'(?:href|src)="([^"]+)"', text):
            u = html.unescape(m.group(1))
            if u.startswith(('http://', 'https://', 'mailto:', 'tel:', 'data:')):
                continue
            parts = urlsplit(u)
            if not parts.path:  # nur #anker auf derselben Seite
                target_file, frag = f, parts.fragment
            else:
                if not exists(parts.path):
                    bad.append(f'{f.relative_to(OUT)}: {u}')
                    continue
                target_file = (OUT / parts.path.lstrip('/') / 'index.html') if parts.path.endswith('/') else OUT / parts.path.lstrip('/')
                frag = parts.fragment
            if frag and target_file.suffix == '.html':
                if target_file not in ids_cache:
                    ids_cache[target_file] = set(re.findall(r'\sid="([^"]+)"', target_file.read_text(encoding='utf-8')))
                if frag not in ids_cache[target_file]:
                    bad.append(f'{f.relative_to(OUT)}: Anker fehlt {u}')
    return bad


if __name__ == '__main__':
    pages = build()
    print(f'{len(pages)} Seiten nach {OUT.relative_to(ROOT)}/ geschrieben.')
    for w in warnings:
        print('Hinweis:', w)
    if '--check' in sys.argv:
        bad = check_links()
        if bad:
            print(f'{len(bad)} defekte Links:')
            for b in bad:
                print('  ', b)
            sys.exit(1)
        print('Linkprüfung: alle internen Links und Anker in Ordnung.')
