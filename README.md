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

Die 31 Bonusdateien (PDF, ZIP, PNG) liegen noch auf dem alten Server unter `wp-content/uploads/…`. Niemand muss sie suchen oder verlinken: Das Skript sucht sie heraus, benennt sie um und legt sie nach `static/bonus/dateien/`. Beim nächsten Bauen sind sie auf `/bonus/` verlinkt, und die alten Download-Links aus Büchern und Hörbüchern leiten automatisch auf die neuen Dateien.

**Weg A, aus dem FTP-Server:** den Ordner `wp-content/uploads` per FTP komplett auf den Rechner ziehen, dann

```bash
python3 tools/bonus_holen.py --ordner ~/Downloads/uploads
```

**Weg B, von der laufenden alten Website** (solange klhe.de noch online ist):

```bash
python3 tools/bonus_holen.py
```

Das Skript meldet am Ende „31 von 31“ oder listet, was fehlt. Übernommen werden nur die 31 bekannten Dateien, nichts sonst aus WordPress. Fehlt eine Datei, steht auf der Bonusseite bei diesem Eintrag „folgt“.

## Livegang (Jens)

Die Weiterleitungen muss niemand anfassen: Sie stecken komplett in der Datei `public/.htaccess`, die einfach mit hochgeladen wird. Wer danach einen alten Link aufruft (aus einem Buch, von Google, Instagram oder einem Hörbuch), landet automatisch auf der passenden neuen Seite.

1. **Repo holen:** `git clone https://github.com/JCBOOKS/klhe-website.git` und `pip install -r requirements.txt`
2. **Bonusdateien holen** (siehe oben, Weg A oder B).
3. **Bauen und prüfen:** `python3 build.py --check` und `python3 tools/test_weiterleitungen.py`. Beide müssen ohne Fehler durchlaufen.
4. **Hosting:** klhe.de liegt bei IONOS (Webhosting, Apache) und läuft über Cloudflare. So steht es auch im Datenschutz. Bei IONOS im Kundenbereich prüfen, dass der Vertrag zur Auftragsverarbeitung (AVV) abgeschlossen ist.
5. **Sichern:** WordPress-Ordner und Datenbank komplett sichern (nicht im Web-Verzeichnis ablegen).
6. **Austauschen:** Alles aus dem Web-Verzeichnis von klhe.de entfernen und den **Inhalt** von `public/` hochladen. Wichtig: `.htaccess` ist eine versteckte Datei; im FTP-Programm versteckte Dateien einblenden und prüfen, dass sie oben liegt.
7. **Testen:**
   - `https://www.klhe.de/` zeigt die neue Startseite
   - `https://www.klhe.de/project/nine-to-five/` landet auf der Buchseite „Nine to five muss nicht sein!“
   - `https://www.klhe.de/finance/bonus-download/` landet auf `/bonus/` beim Abschnitt Finanzreihe, ein Download dort funktioniert
   - `https://www.klhe.de/wp-login.php` antwortet mit „Gone“ (410)
   - eine erfundene Adresse zeigt die Fehlerseite von KLHE
8. **HTTPS und www:** Das am besten in Cloudflare regeln, nicht in der `.htaccess`: SSL-Modus „Full (strict)“ (oder „Full“), „Always Use HTTPS“ an und eine Weiterleitungsregel `klhe.de/*` → `https://www.klhe.de/$1`. Den Schalter `https_www_erzwingen` in `build.py` dann auf `False` lassen. Achtung: Steht Cloudflare auf „Flexible“ und der Schalter auf `True`, entsteht eine Endlosschleife. Nach jedem Hochladen in Cloudflare den Cache leeren („Purge Everything“).
9. **Google:** In der Search Console `https://www.klhe.de/sitemap.xml` einreichen.
10. **Aufräumen:** WordPress-Datenbank und alte Zugänge (FTP, Datenbank, WordPress-Nutzer) löschen bzw. Passwörter ändern.

Für Cloudflare Pages oder Netlify statt Apache liegt dieselbe Weiterleitungsliste als `public/_redirects` bei.

## Datenschutz

Keine Cookies, kein Tracking, keine externen Schriften oder Skripte. Einziges JavaScript: öffnet auf der Bonusseite den Abschnitt aus der Adresse (`/bonus/#english`).
