# Seitenplan klhe.de (v1, Entwurf zur Freigabe)

Stand 15.10.2026 · Etappe 1, letzter Schritt vor der Gestaltung · Grundlage: `klhe-entscheidungen-und-offene-punkte.md` (A1–A25), `klhe-inhalte-rohmaterial.md`

---

## 1. Leitlinien

1. **Erst der Verlag, dann die Personen.** Programm, Reihen, Vertriebswege und Presse anderer Autor:innen stehen vorn. Chris und Jens erscheinen als Verleger auf „Verlag“.
2. **80/20.** Wenige Seitentypen. Alles, was Bücher betrifft, kommt aus einer Datentabelle. Keine Formulare, keine Cookies, kein JavaScript nötig.
3. **Nur belegte Fakten** (A12). Keine Preise, keine Konditionen.
4. **Bestehende Pfade bleiben, wo es geht:** `/buecher/`, `/verlag/`, `/kontakt/`, `/impressum/`, `/datenschutz/`.

## 2. Navigation

- **Kopf:** Logo · Bücher · Für Autor:innen · Verlag · Kontakt
- **Fuß:** Kategorien · Reihen · Bonusmaterial · Buchhandel und Presse · Impressum · Datenschutz · Börsenverein · Social (F8) · „KLHE ist der Verlag hinter BuchBuddy“ · Amazon-Partner-Hinweis

## 3. Seiten

### 3.1 Startseite `/`

| # | Abschnitt | Inhalt | Quelle |
|---|---|---|---|
| 1 | Einstieg | „Unabhängiger Verlag seit 2011“, Claim „Bücher, die bewegen.“ (bisheriger Claim), ein Satz zum Programm; Bild: Cover aktueller Titel, kein Porträt | Bestand |
| 2 | Faktenleiste | seit 2011 · 500.000+ verkaufte Bücher · lieferbar über Libri, Zeitfracht und Umbreit · Börsenverein (keine Titelanzahl, A40) | A12, Rohmaterial |
| 3 | Neu und empfohlen | 6–8 Titel groß, bevorzugt von anderen Autor:innen (Auswahl durch Chris) | Datentabelle |
| 4 | Programm | 6 Kategorie-Kacheln (ohne Anzahl) | Datentabelle |
| 5 | Reihen | 5 Reihen-Karten mit Cover-Fächer | Datentabelle |
| 6 | Presse | Logo-Leiste plus 3 Belege (Medium, Ausgabe, Titel), z. B. Psychologie Heute zu Mutmacherinnen, Tagesspiegel zu Kleine Redner, Focus Money zur Faulbär-Strategie | Presse-Belege |
| 7 | Im Buchhandel | Händler-Logos plus „und in jeder Buchhandlung vor Ort per ISBN“ | A2 |
| 8 | Für Autor:innen | Kurz: Was ein Verlag leistet, Link auf `/autoren/` | Rohmaterial |
| 9 | Verlag | 2–3 Sätze Geschichte, kleines Foto, Link auf `/verlag/` | Rohmaterial |

### 3.2 Programm `/buecher/`

- Kurzer Einstieg, Sprungmarken zu den 6 Kategorien.
- Neuerscheinungen groß.
- Je Kategorie ein Cover-Raster: Titel, Autor:in, Badges (Hörbuch · im Buchhandel · auch übersetzt). Reihen erscheinen als **eine** Karte.
- Backlist am Ende als kompakte Liste mit Amazon-Link: Visualisierung, Ziele finden, Autosuggestion, Meditation für Anfänger, Lateinamerikanisches Spanisch, Vermögensfalle Eigenheim? (Chris kann weitere zuordnen).

### 3.3 Buchseite `/buecher/<titel>/` (rund 50, generiert)

- Cover, Titel, Untertitel, Autor:in, Kategorie, ggf. Reihe und Band
- Klappentext, 80–150 Wörter (A11)
- Badges: Softcover / Hardcover / E-Book, Hörbuch, im Buchhandel bestellbar (ISBN), übersetzt
- Button „Bei Amazon ansehen“ (Partner-Link)
- ISBN; Leseprobe als PDF, wo vorhanden (heute 9 Finanztitel); Presse zum Buch, wo vorhanden
- „Mehr aus dieser Reihe/Kategorie“
- Strukturierte Daten (schema.org/Book) für Google

**Warum eigene Seiten trotz 80/20:** Sie entstehen automatisch aus der Tabelle, der einzige Aufwand ist der Klappentext, den die Übersicht ohnehin braucht. Und für BuchBuddy ist „So sieht Dein Buch bei uns aus“ mit eigenem Link das stärkste Vorzeigestück im Verkaufsgespräch.

### 3.4 Reihenseite `/reihen/<reihe>/` (5)

| Reihe | Titel | Einzelseiten? |
|---|---|---|
| Finanzreihe Chris & Jens | 9 | ja, Reihenseite ist Übersicht |
| Mitmachbücher | 3 | ja |
| Mutmachbücher vor Arztterminen | 14 | nein, alles auf der Reihenseite, je Titel Amazon-Link; Hinweis „von Hand illustriert“ und dezent auf praxis-kinderbuch.de |
| Kuschelige Momente | 5 | nein |
| Unnützes Wissen | 3 | nein |

### 3.5 Für Autorinnen und Autoren `/autoren/`

1. Einstieg: Bei einem Verlag erscheinen, mit allem, was dazugehört.
2. Was ein Verlag leistet, im Vergleich zu Self-Publishing: VLB-Listung; Verträge mit Libri, Zeitfracht und Umbreit, also bestellbar in jeder Buchhandlung; Verlagsauslieferung mit Bestellungen, Versand, Rechnung, Remissionen; Mitglied im Börsenverein.
3. So arbeiten wir: Programmentscheidung; Partnerschaft (eigene Reichweite oder Marketing-Investition); kein Druckkostenzuschussverlag.
4. Beispielrechnung „Wohin der Buchpreis geht“ als einfache Grafik, ausdrücklich als branchenübliche Größenordnung.
5. „Wir nehmen keine unverlangten Manuskripte an.“ Weg zum Verlag: BuchBuddy (Button), ohne Kosten.
6. Beispiele: Cover von Titeln anderer Autor:innen.

### 3.6 Verlag `/verlag/` (Pfad bleibt)

- Geschichte als kurze Zeitleiste: Studium · Mexiko 2010/11 · Gründung 2011 mit 300 vorgedruckten Exemplaren · Finanzreihe · Buch-Software · BuchBuddy · heute (ohne Titelanzahl)
- „Warum wir so arbeiten“: kurz und positiv (B6)
- Verleger: Chris und Jens mit Foto
- Presse: alle belegten Artikel als Liste
- Verlagsangaben: GbR, Adresse, Börsenverein, Vertrieb

### 3.7 Kontakt `/kontakt/` (Pfad bleibt)

E-Mail info@klhe.de (Telefon offen, F3), Adresse. Vier kurze Blöcke: Leser:innen · Buchhandel (Barsortimente oder direkt zu Händlerkonditionen, Versand und Rechnung über die Verlagsauslieferung) · Presse (Rezensionsexemplare per Mail) · Autor:innen (→ `/autoren/`).

### 3.8 Bonusmaterial `/bonus/`

- Einstieg „Bonusmaterial zu Deinem Buch oder Hörbuch“, ohne Anmeldung.
- Abschnitte je Titel bzw. Paket mit direkten Download-Links; Sprachabschnitte English · Español · Italiano · Français.
- Im Fuß verlinkt, nicht im Hauptmenü, nicht in der Google-Suche (`noindex`).
- Alle 42 alten Bonus-Adressen leiten per 301 auf ihren Abschnitt (siehe URL-Inventar).

### 3.9 Impressum, Datenschutz, 404

- Impressum nach BuchBuddy-Vorbild, Rechtsgrundlagen aktualisiert (DDG statt TMG, MStV statt RStV), richtige USt-IdNr. (F2).
- Datenschutz: eine Seite für Hosting, Cloudflare, Server-Logs, E-Mail-Kontakt, Amazon-Partnerlinks, ggf. Videos per Klick. Kein Newsletter, kein Formular, kein Tracking.
- 404-Seite mit Link zu Bücher und Bonusmaterial.

## 4. Datentabelle `data/buecher.csv`

| Spalte | Beispiel | Hinweis |
|---|---|---|
| slug | `nine-to-five-muss-nicht-sein` | für die Adresse |
| titel, untertitel | | |
| autorin | Christopher M. Klein | mehrere mit „;“ |
| kategorie | Ratgeber | eine der 6 |
| reihe, band | Finanzreihe Chris & Jens, 5 | leer, wenn keine |
| seite | eigen / reihe / backlist | steuert die Darstellung |
| isbn | 978-3-947061-84-6 | Hauptausgabe |
| amazon_url | | wird mit Partner-Tag ergänzt |
| buchhandel | ja / nein | „nein“ = nur Amazon (Liste im Entscheidungsdokument, Abschnitt A) |
| formate | SC;HC;EB | Badges |
| hoerbuch, uebersetzt | ja / nein | nur Hinweis |
| neu, empfohlen | ja / nein | Startseite und Programm |
| klappentext | | 80–150 Wörter |
| leseprobe, trailer | Dateiname / URL | optional |
| presse | IDs aus `presse.csv` | optional |

Dazu `data/presse.csv` (Medium, Ausgabe, Titel, Beleg-Datei, Logo) und `data/bonus.csv` (Abschnitt, Dateien, alte Adressen).

## 5. Was wegfällt

Shop mit Warenkorb, Kasse, Konto, AGB, Widerruf, Versand, Zahlung, Bewertungen · Team- und Personenseiten · Newsletter-Anmeldungen und GetResponse · Kontaktformular, reCAPTCHA, Cookie-Banner · Imprint-Logos (finance, helper, kids …) · Trailer auf der Startseite (Verlagstrailer offen, F10) · Archiv-, Kategorie- und Schlagwortseiten.

## 6. Weiterleitungen (Konzept)

| Alt | Neu |
|---|---|
| `/project/<buch>/`, `/product/<buch>/` | passende Buchseite bzw. Reihenseite |
| Düsseldorf Guide, Finanz-Kochbuch, Finanzkochbuch light, E.S.E.L. | `/buecher/` |
| `/project/<person>/` | Buchseite der Person; Chris, Jens → `/verlag/`; Übersetzer, Lektorat, Sprecher → `/verlag/` |
| 42 Bonus-, Newsletter-, Hörbuchseiten | `/bonus/#<abschnitt>` |
| Golf-/Tennis-Kopien unter `/allgemein/` | `/reihen/unnuetzes-wissen/` |
| `/team/` | `/verlag/` |
| `/datenschutzerklaerung/`, `/impressum-2/` | `/datenschutz/`, `/impressum/` |
| Shop-Seiten (9), `/product-category/…` | `/buecher/` |
| `/manuskript-einsenden/` | `/autoren/` |
| `/under-construction/` | `/` |
| 93 Archivseiten | `/buecher/` |
| 35 Bonus-Dateien unter `/wp-content/uploads/…` | `/bonus/dateien/<datei>` |
| alles andere (`/wp-admin/`, `/wp-login.php`, Spam-Adressen aus dem Hack) | 404 bzw. 410, keine Weiterleitung |

Abfrage-Parameter wie `?fbclid=` werden ignoriert. Die vollständige Zuordnung pro Adresse entsteht beim Bauen aus dem URL-Inventar.

## 7. Umfang

Rund 60 erzeugte Seiten: Startseite, Programm, ca. 50 Buchseiten, 5 Reihenseiten, Autor:innen, Verlag, Kontakt, Bonus, Impressum, Datenschutz, 404.

## 8. Nächste Etappen

1. **Freigabe dieses Seitenplans** (insbesondere 3.3 Buchseiten und 3.8 Bonus).
2. **Etappe 2 – Gestaltung:** klickbare Vorschau von Startseite, Programm, einer Buchseite und der Autorenseite mit echten Covern. Parallel: Entwurf der Datentabelle und der Klappentexte.
3. **Etappe 3 – Bauen:** Plan-Datei `PLAN-klhe-relaunch.md` für /umsetzen, Generator nach BuchBuddy-Vorbild.
4. **Etappe 4 – Livegang durch Jens:** Weiterleitungen, Sitemap, Search Console, WordPress vollständig löschen, Zugangsdaten erneuern.
