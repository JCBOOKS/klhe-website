#!/usr/bin/env python3
"""Prüft public/.htaccess ohne Apache: wendet die RewriteRules (wie Apache, erste Regel gewinnt) auf
alle alten Adressen aus data/redirects.csv und auf alle neuen Seiten an.
    python3 tools/test_weiterleitungen.py
"""
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
rules = []
for line in (ROOT / 'public' / '.htaccess').read_text(encoding='utf-8').splitlines():
    m = re.match(r'RewriteRule "(.+?)" (?:"(.+?)"|-) \[(.+)\]$', line)
    if m:
        pat = m.group(1).replace('\\ ', ' ')
        rules.append((re.compile(pat), m.group(2), m.group(3)))


def apply(path):
    p = path.lstrip('/')
    for rx, target, flags in rules:
        if rx.search(p):
            return ('410', None) if 'G' in flags else ('301', target)
    return ('200', None)


fehler = 0
for r in csv.DictReader(open(ROOT / 'data' / 'redirects.csv', encoding='utf-8')):
    for variante in {r['alt'], r['alt'].rstrip('/')} if r['alt'].endswith('/') else {r['alt']}:
        code, target = apply(variante)
        if code != r['code'] or (code == '301' and target != r['neu']):
            print('FALSCH:', variante, '→', code, target, '(erwartet', r['code'], r['neu'], ')')
            fehler += 1
neu = [('/' + str(f.relative_to(ROOT / 'public')).replace('index.html', '')) for f in (ROOT / 'public').rglob('index.html')]
for p in neu:
    code, target = apply(p)
    if code != '200':
        print('NEUE SEITE WIRD UMGELEITET:', p, code, target)
        fehler += 1
for p, erwartet in [('/wp-login.php', '410'), ('/wp-admin/', '410'), ('/wp-content/plugins/x.php', '410'), ('/feed/', '410'),
                    ('/category/finance/', '301'), ('/project_tag/aktien/', '301'), ('/author/jens/', '301'), ('/xmlrpc.php', '410')]:
    code, _ = apply(p)
    if code != erwartet:
        print('MUSTER FALSCH:', p, code, 'erwartet', erwartet)
        fehler += 1
print(f'{len(rules)} Regeln, {len(neu)} neue Seiten geprüft, {fehler} Fehler.')
sys.exit(1 if fehler else 0)
