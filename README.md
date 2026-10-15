# klhe.de

Statische Website des Verlags KLHE (GbR C. Klein & J. Helbig). Ersetzt die alte WordPress-Installation.
Gestaltung: v5 „Transparentpapier“, freigegeben am 15.10.2026.

## Bauen

```bash
pip install -r requirements.txt     # einmalig (nur Jinja2)
python3 build.py --check            # baut nach public/ und prüft alle internen Links
python3 tools/test_weiterleitungen.py   # prüft die Weiterleitungen in public/.htaccess
```

Lokal ansehen: `python3 -m http.server 8000 --directory public`, dann http://localhost:8000

## Was wo liegt

| Pfad | Inhalt |
|---|---|
| `data/buecher.csv` | alle Titel: eine Zeile pro Buch (Titel, Autor:in, Kategorie, Reihe, ISBN, Amazon-ASIN, Klappentext …). Lässt sich in Excel oder Numbers bearbeiten, als CSV (UTF-8) speichern. |
| `data/kategorien.json`, `data/reihen.json` | die sechs Kategorien und fünf Reihen mit ihren Texten |
| `data/presse.json` | Presseausschnitte (Bild unter `static/img/presse/`) |
| `data/bonus.json` | Bonusmaterial: Abschnitte, Dateien, alte Adressen |
| `data/redirects.csv` | alte WordPress-Adressen → neue Adressen (301) oder 410 |
| `templates/` | Seitenvorlagen (Jinja2) |
| `static/` | CSS, Schrift (selbst gehostet), Bilder, Favicons, Bonusdateien |
| `public/` | fertige Website, wird bei jedem Bauen neu erzeugt (nicht im Repo) |
| `docs/` | Seitenplan, Entscheidungen und offene Punkte, URL-Inventar |

### Spalten in `buecher.csv`

- `seite`: `eigen` = eigene Buchseite unter `/buecher/<slug>/`, `reihe` = nur auf der Reihenseite, `backlist` = nur als Zeile „Weitere Ratgeber“
- `amazon`: ASIN oder ISBN-10; der Partner-Tag `jcbooks04-21` wird automatisch angehängt
- `buchhandel`: `ja` = Hinweis „Im Buchhandel“ und „mit der ISBN bestellen“, `nein` = nur Amazon
- `hoerbuch`, `uebersetzt`, `neu`: `ja` oder leer
- `empfohlen`: Zahl 1–6 = Reihenfolge unter „Neu und empfohlen“ auf der Startseite
- `cover`: Dateiname ohne Endung in `static/img/cover/` (leer = Platzhalter „Cover folgt“)
- `presse`: IDs aus `presse.json`, mehrere mit `;`

Neues Buch: Zeile ergänzen, Cover als `static/img/cover/<slug>.webp` ablegen (einheitlich: lange Kante 720 px), bauen.

## Bonusmaterial

Die Dateien liegen noch auf der alten Website. Einmalig holen (auf einem Rechner mit Internet, solange klhe.de noch läuft):

```bash
python3 tools/bonus_holen.py
python3 build.py --check
```

Solange eine Datei fehlt, zeigt die Bonusseite bei diesem Eintrag „folgt“.

## Livegang (Jens)

1. `python3 tools/bonus_holen.py` und `python3 build.py --check` ausführen.
2. Inhalt von `public/` (inklusive `.htaccess`) in das Web-Verzeichnis von klhe.de laden. Die `.htaccess` braucht Apache mit `mod_rewrite` (und optional `mod_headers`). Für Cloudflare Pages oder Netlify liegt dieselbe Liste als `public/_redirects` bei.
3. HTTPS prüfen, dann in der `.htaccess` die drei auskommentierten Zeilen für `https://www.klhe.de` aktivieren (Quelle: `build.py`, Funktion `write_redirects`).
4. Stichproben: `/project/nine-to-five/` → Buchseite, `/finance/bonus-download/` → `/bonus/#finanz`, `/wp-login.php` → 410.
5. Sitemap `https://www.klhe.de/sitemap.xml` in der Search Console einreichen.
6. WordPress samt Datenbank vollständig löschen, alle alten Zugänge ändern.

## Datenschutz

Keine Cookies, kein Tracking, keine externen Schriften oder Skripte. Einziges JavaScript: öffnet auf der Bonusseite den Abschnitt aus der Adresse (`/bonus/#english`).
