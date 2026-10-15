# Plan: Relaunch klhe.de als statische Website

Stand: 15.10.2026 · Status: gebaut, wartet auf Livegang (T1, T9, T14)

## Ziel
klhe.de zieht von der gehackten WordPress-Installation auf eine statische Website um, gebaut mit einem kleinen Python-Generator wie bei buchbuddy.de. Gestaltung nach der freigegebenen Vorschau v5 „Transparentpapier“. Schneller Umzug hat Vorrang, Feinschliff (Bücherliste, Texte) folgt nach dem Livegang.

## Abnahmekriterium
`python3 build.py` erzeugt `public/` ohne Fehler; alle internen Links in `public/` zeigen auf vorhandene Dateien (Prüfung `python3 build.py --check`); jede alte Adresse aus `docs/klhe-url-inventar.md` hat eine Regel in `public/.htaccess`.

## Kontext
- Entscheidungen und offene Punkte: `docs/klhe-entscheidungen-und-offene-punkte.md` (A1–A56).
- Seitenplan: `docs/klhe-seitenplan.md`. Alte Adressen: `docs/klhe-url-inventar.md`.
- Gestaltung: v5-Entwürfe im Projektordner unter `entwurf/seiten-v5/` (Canvas „KLHE Website“).
- Keine Cookies, kein Tracking, keine externen Schriften (Instrument Sans liegt unter `static/fonts/`).
- Kauf-Links nur zu Amazon mit Partner-Tag `jcbooks04-21` (A1, A24).

## Entscheidungen
- Datenquelle `data/buecher.csv` (eine Zeile pro Titel); Reihen, Presse, Bonus als JSON in `data/`.
- Eigene Buchseite für Titel mit `seite=eigen`; Mutmachbücher, Kuschelige Momente und Unnützes Wissen nur auf ihrer Reihenseite; ältere Ratgeber als Liste (`seite=backlist`).
- Weiterleitungen als `.htaccess` (Apache) und zusätzlich `_redirects` (Cloudflare Pages/Netlify-Format), damit der Hosting-Weg offen bleibt.

## Nicht Teil dieses Plans
- Bonus-Dateien selbst (T1, Jens kopiert sie nach `static/bonus/`).
- Löschen von WordPress und Search-Console-Bereinigung (T10, T11).

## Handgriffe
- [x] H1: Gerüst, Schrift, Bilder · Dateien: `static/` · fertig, wenn: alle Cover unter `static/img/cover/<slug>.webp` liegen
- [x] H2: Datentabelle mit gekürzten Klappentexten · `data/buecher.csv` · fertig, wenn: 77 Titel, jeder mit Kategorie und Darstellung
- [x] H3: Vorlagen und Stylesheet nach v5 · `templates/`, `static/css/klhe.css`
- [x] H4: Generator · `build.py` · fertig, wenn: Build läuft fehlerfrei
- [x] H5: Rechtstexte · Impressum, Datenschutz
- [x] H6: Weiterleitungen · `data/redirects.csv` → `.htaccess`, `_redirects`
- [x] H7: Prüfung · Linkcheck, Sichtprüfung aller Seitentypen

## Offene Fragen
- F32 bis F38 in `docs/klhe-entscheidungen-und-offene-punkte.md`, Abschnitt C8 (Hosting, MStV, www, ISBN-Abweichungen, Auflage, Bandnummern)

## Protokoll
- 15.10.2026: Plan erstellt, Repo `jcbooks/klhe-website` angelegt (leer).
- 15.10.2026: H1–H7 erledigt. 69 Cover vereinheitlicht, 77 Titel mit Klappentexten, Vorlagen nach v5, Rechtstexte, 222 Weiterleitungen. `python3 build.py --check` und `python3 tools/test_weiterleitungen.py` laufen ohne Fehler. Offen: Bonusdateien holen (T1), GitHub-Zugriff (T9), Livegang (T14).
