# Bestandsaufnahme klhe.de

Stand 15.10.2026 · Etappe 1 von 4 (Bestandsaufnahme → Gestaltung → Bauen → Livegang) · Quellen: Live-Seite www.klhe.de (abgerufen 15.10.2026), `Liste Bücher.xlsx`, Anhänge im Projekt. Alle Zahlen unten sind gezählt, nicht geschätzt. Wo etwas nicht prüfbar war, steht es dabei.

Zugehörige Dokumente: `klhe-url-inventar.md` (alle 286 Adressen) · `klhe-entscheidungen-und-offene-punkte.md` (Entscheidungen, Fragen, To-dos)

---

## Kurzfassung

1. **Mehr Seiten als gedacht.** Die WordPress-Sitemap (`/wp-sitemap.xml`, eine `sitemap_index.xml` gibt es nicht) listet **286 Adressen**.
2. **Es gibt schon eine Seite pro Buch.** 57 Buchseiten unter `/project/…` plus 54 Shop-Produktseiten unter `/product/…` (weitgehend Dubletten). Das Briefing („keine eigenen Seiten pro Buch“) stimmt nicht.
3. **Der Shop läuft technisch noch.** WooCommerce, 54 Produkte, nur Kauf auf Rechnung, Abwicklung über die **Runge Verlagsauslieferung**. AGB, Widerruf, Versand, Zahlung zuletzt 2022 geändert, Versandseite ist leer. Bestellzahlen liegen nicht vor.
4. **Größtes Migrationsrisiko: 44 Bonus-, Download- und Hörbuchseiten.** Die Texte sprechen Käufer direkt an („Danke für den Kauf …“, „wie versprochen“). Diese Adressen stehen sehr wahrscheinlich in Büchern und Hörbüchern und müssen exakt weiterlaufen.
5. **Titel:** Liste 77, Website 57. 23 Listentitel fehlen online, 3 Website-Titel fehlen in der Liste (Düsseldorf Guide, Das große Fürth Wimmelbuch, Mikroabenteuer in Franken).
6. **Datenqualität:** 3 Amazon-Links in der Liste zeigen auf eine andere ISBN, 4 auf B0-ASINs, Bandnummern bei „Kuschelige Momente“ widersprechen sich, auf der Website mehrere falsch verknüpfte Autoren- und Kauf-Links.
7. **Rechtstexte veraltet:** Impressum nach TMG/RStV, zwei fast gleiche Datenschutzerklärungen, eingebunden sind Google reCAPTCHA, ein Cookie-Banner (hu-manity) und Cloudflare Insights.
8. **Cover:** Die Zip enthält 13 Screenshots mit je ca. 3 3D-Mockups (ca. 37 Titel, je ~500 px breit). Für Buchseiten zu klein und nicht flach. Die Original-Cover liegen vermutlich in `/wp-content/uploads/` bzw. in Euren Satzdaten.

---

## 1. Technik und eingebundene Dienste (live)

| Bereich | Befund |
|---|---|
| System | WordPress mit Divi/Elegant-Themes-Portfolio („project“), WooCommerce, WordPress-Core-Sitemap |
| Vor der Seite | Cloudflare (E-Mail-Verschleierung, Insights-Beacon) |
| Einwilligung | Cookie-Banner von hu-manity.co (Cookie Notice) |
| Formulare | Kontaktformular mit Rechenaufgabe; Google reCAPTCHA wird geladen |
| Newsletter | „KLHE-letter“; Anmeldeseiten verweisen im Datenschutztext auf **GetResponse** |
| Amazon | Links teils mit Partner-Tag `jcbooks04-21`, teils amzn.to-Kurzlinks, teils Suchergebnis-Links mit Tracking |
| Videos | 4 Trailer als MP4 (`/wp-content/uploads/2023/04/…`: helper, kids, finance, Verlag); einzelne YouTube-/Vimeo-Einbettungen auf Buchseiten |
| Social | Facebook `KLHE.Verlag`, Instagram `klhe_verlag`, Amazon-Autorenlink (amzn.to) |

## 2. Navigation und Seitentypen

**Hauptmenü:** Home · Bücher · Team · Über uns (`/verlag/`) · Manuskript (→ buchbuddy.de) · Kontakt · Shop · Warenkorb
**Footer:** GbR-Adresse, © 2024, Börsenverein-Logo, `info@klhe.de`, Facebook, Amazon, Instagram, Impressum, „Datenschutzbestimmungen“

| Seitentyp | Anzahl | Was drauf ist |
|---|---|---|
| Startseite | 1 | Zitate (Belsky, Yoda, Huxley), 4 Trailer, „Geschichten, die inspirieren“, Kontaktformular |
| Bücher-Übersicht `/buecher/` | 1 | 57 Titel, Filter Alle · Finance · Helper · Kids · Coloring · Learn · Travel, Newsletter-Kasten |
| Buchseiten `/project/…` | 57 | Cover, Text, Autorbox, „Erhältlich bei“ (Amazon, Thalia, Hugendubel, Fairbuch, Buch7), Preise je Format; Textlänge von 10 bis ~500 Wörtern |
| Personenseiten `/project/…` | 18 | 13 Autor:innen, 1 Übersetzer, 1 Lektorat, 3 Sprecher:innen; keine verlinkt ihre Bücher |
| Shop-Produkte `/product/…` | 54 | Preis, Warenkorb-Button (bei 8 Seiten fehlt er), 0 Bewertungen |
| Beiträge (Bonus/Newsletter/Hörbuch) | 44 | siehe Abschnitt 5 |
| Statische Seiten | 19 | Über uns, Team, Kontakt, Shop-Seiten, Rechtstexte, Altlasten (`/impressum-2/`, `/under-construction/`, `/manuskript-einsenden/`) |
| Archive (Kategorien, Tags, Autoren) | 93 | automatisch erzeugte Listen, kein eigener Inhalt |
| **Summe** | **286** | |

**Verteilung der 57 Titel auf die heutigen Filter:** Finance 9 · Helper 21 · Kids 11 (+ „Kleine Redner“ doppelt) · Learn 9 · Coloring 4 · Travel 3.
Hinweis zum Briefing: Die Trailer liegen auf der Startseite, nicht in der Bücher-Übersicht, und es gibt sechs Filter statt vier Gruppen.

**Über uns (`/verlag/`):** Gründung 2011 durch Christopher Klein und Jens Helbig; Imprints KLHE finance, helper, travel, learn, kids, coloring; Gründer-Bios mit Bestseller-Aussagen (z. B. „Der Hamster verlässt das Rad“ 2018 auf Platz 2 im Kindle-Store); Pressestimmen 2013–2022 (u. a. Focus-Money 05/2018, Bank & Umwelt 11/2018, BUNTE 05/2019, Geld-Magazin Österreich 2015).
**Team (`/team/`):** nur Namen und Rollen, keine Texte.
**Kontakt (`/kontakt/`):** Name, E-Mail, Nachricht, Rechenaufgabe; „Antwort innerhalb von 24 Stunden“; Abschnitt für Buchhändler (individuelle Konditionen über das Formular, sonst über die Barsortimente). Keine Telefonnummer.

## 3. Bücher

Vollständige Titeltabelle mit Abgleich: Anhang A.

**Abgleich Liste ↔ Website**

| | Anzahl | Titel |
|---|---|---|
| In Liste und auf Website | 54 | |
| Nur in der Liste | 23 | 14 × Mutmachbücher Arztbesuch (2 davon noch nicht online), Kuschelige Momente Band 3 (Hygge) und 5 (Herbst), Unnützes Wissen Wilder Westen, Visualisierung mit der Kraft der Gedanken, Ziele finden …, Autosuggestion …, Meditation für Anfänger, Lateinamerikanisches Spanisch lernen, Vermögensfalle Eigenheim? (nur im Shop) |
| Nur auf der Website | 3 | Der Düsseldorf Guide, Das große Fürth Wimmelbuch, Mikroabenteuer in Franken (Cover liegt in der Zip) |
| Nur im Shop | 3 + 1 | Das große Finanz-Kochbuch (978-3-947061-58-7), Das Finanzkochbuch light (978-3-947061-94-5), Die E-S-E-L-Strategie (978-3-947061-69-3), dazu Vermögensfalle Eigenheim? |

**Aus der Liste (Hinweis an Runge):** Entfernen bzw. vernichten: E.S.E.L.-Strategie, ROMI-Methode, Inside Modern Family, alle fremdsprachigen Ausgaben. Diese Titel kommen nicht auf die Website.

**Formate, Hörbücher, Übersetzungen (soweit live erkennbar)**
- Formate auf Buchseiten: Softcover, Hardcover, E-Book; Hardcover u. a. bei Nine to five, Einmal Himmel, Akupressur 1+2, Zeitzeugen, Chinesisch kochen, Englische Grammatik 1+2, Suchbuch, Ein etwas anderes Ausmalbuch, Mutmacherinnen.
- Hörbuch-Begleitseiten gibt es zu: Nine to five, Mit Blockchain, Ökoethinvesting, Faulbär-Strategie (auch FR), Einmal Dividende, Tag auf Tag, Akupressur, Michael Jordan, Psychedelika. Die vollständige Hörbuchliste fehlt noch.
- Übersetzungen: Französisch belegt für Nine to five, Mit Blockchain, Ökoethinvesting, Faulbär-Strategie („Millionnaire avec la stratégie du paresseux“). Bonus- und Newsletterseiten gibt es auf Englisch, Spanisch, Italienisch und Französisch für Helper- und Kids-Titel. Welche Titel genau übersetzt sind, ist offen.

**Datenfehler (zum Korrigieren vor dem Bauen)**
- Liste, Amazon-Link passt nicht zur ISBN: Ziele finden (→ 3981579488), Glücklich denken (→ 3985380252), Chinesisch kochen (→ 3985381437, das ist laut Website die Taschenbuch-Ausgabe).
- Liste, Link auf B0-ASIN statt ISBN: Michael Jordan, Zeitzeugen 1 und 2, All the things … Möglicherweise Amazon-only-/KDP-Ausgaben, bitte bestätigen.
- Kuschelige Momente: Website führt „Sommer & Ferien“ als Band 3, die Liste als Band 4 (Band 3 = Hygge Café). Die Sommer-Seite verlinkt zusätzlich die Band-2-ASIN.
- Titel: Liste „Mama, wer wohnt eigentlich **am** Meer?“, Website „**im** Meer?“.
- Mutmacherinnen: Liste Softcover 978-3-98538-026-8, Shop/Flyer Hardcover 978-3-98538-008-4. Beide Ausgaben führen?
- Website: „Finde dein WARUM“ verlinkt Autor auf Kim Frieten und Amazon auf „Chinesisch kochen“; Akupressur-Autorin uneinheitlich (Jingling Song / Ai Huihui / Yihong Wu); Tarot: Autor Matthias Groß, Personenseite heißt „matthias-nordmeyer“ (Sprecher?); Shop-„Artikelnummern“ bei 6 neueren Titeln sind keine gültigen ISBNs.

## 4. Shop

- 54 Produkte, Preise zwischen 10,80 € und 27,00 €, Standard 14,80 €. Bei 8 Produkten fehlt der Warenkorb-Button.
- Zahlungsart: nur Rechnung. Die Rechnung kommt als PDF von der Runge Verlagsauslieferung, Zahlung binnen 14 Tagen.
- Versandarten-Seite: leer. AGB & Widerrufsbelehrung der C. Klein & J. Helbig GbR (Stand 2022). Eigene Seite „Echtheit von Bewertungen“, aber keine einzige Bewertung.
- Shop-Rechtsseiten sind im Footer nicht verlinkt.
- **Nicht ermittelbar:** Bestellungen pro Monat/Jahr, ob B2B-Mengen (Praxen, Schulen, Buchhandel) darüber laufen.

## 5. Bonus-, Download- und Hörbuchseiten (44 Beiträge)

| Bereich | Seiten | Inhalt |
|---|---|---|
| Finance | `/finance/bonus/` (Newsletter-Anmeldung), `/finance/bonus-download/`, `/finanzas/descargar-bonus-gratis/` (ES), `/finance/eigenheim/`, `/finance/finanzkochbuchlight/`, 7 × `/finance/audible/…` | ZIP-Pakete (E-Books, Excel-Tools, Vergleichsreports), PDF-Zusatzmaterial für Hörbuchkäufer, Rezensionsbitte |
| Helper | `/helper/bonus-2/`, `/helper/helper-download/`, Newsletter/Bonus EN, ES, IT, FR, `/helper/mutmacherinnen/`, `/helper/gegenwind-bonus/`, `/helper/akupressur-audio/`, `/helper/audible-akupressur/`, `/helper/klhe-grammatik-en-bonus/`, `/helper/lebedeinwarum/` | E-Book-Pakete, Grafiken, Bonus zum Buch |
| Psychology | `/psychology/bonusmaterial/` (ROMI-Grafiken), `/psychology/anmelden/` | Downloads, Newsletter |
| Kids | `/kids/geschenk/`, `/kids/regalo/`, `/kids/present/`, `/kids/kids-bonus-download/` (+ `-en`, `-es`) | Gratis-PDFs (Sport-Mitmachbuch, Mama Meer), Grafiken, Checkliste, Memory |
| Sonstiges | `/allgemein/presseverteiler-klhe/`, `/allgemein/michael-jordan-audio/`, `/allgemein/psychedelika-audio/`, `/allgemein/planer-selbstfuersorge/`, `/sprache/newsletter-englische-grammatik/` | Audio-Zusatzmaterial, Presseverteiler, Planer |
| Versehentliche Kopien | `/allgemein/golf-…/`, `/allgemein/tennis-…/` | Kopie der Buchseite („… Kopieren“) |

**Befunde**
- Downloads sind direkte Dateien unter `/wp-content/uploads/<Jahr>/<Monat>/…` (2019–2023). Bleiben diese Pfade im neuen Repo gleich, laufen die Links ohne Weiterleitung weiter. Dateinamen mit Umlauten, Leerzeichen, Kommas und dem Tippfehler „Bouns“ müssen exakt übernommen werden.
- **Fehler live:** `/helper/akupressur-audio/` liefert als Download die Blockchain-PDF.
- `/finance/audible/paresseux/` (FR) verweist für den Newsletter auf financepreneur.fr.
- Rund 30 dieser Seiten ließen sich wegen Drosselung nicht automatisch vollständig lesen. Für die Umsetzung brauchen wir einen WordPress-Export plus Kopie von `/wp-content/uploads/` (To-do für Jens).

## 6. Rechtliches

- **Impressum (`/impressum/`):** Christopher Klein & Jens Helbig GbR, KLHE Verlag, Hortensienstr. 26, 40474 Düsseldorf; Gesellschafter Jens Helbig und Christopher Klein; E-Mail; USt-IdNr. vorhanden; „Angaben gemäß § 5 TMG“ und „§ 55 Abs. 2 RStV“ sind veraltete Rechtsgrundlagen; keine Telefonnummer.
- **Datenschutz:** zwei fast gleiche Seiten (`/datenschutz/` und `/datenschutzerklaerung/`, je ~20.000 Zeichen), erwähnen u. a. Facebook, GetResponse, YouTube. Der Footer verlinkt die eine, das Kontaktformular die andere.
- **Altlasten:** `/impressum-2/`, `/under-construction/`, AGB/Widerruf nur für den Shop.
- **Vorlage BuchBuddy (live):** Buuk Publishing GmbH & Co. KG, gleiche Adresse, Telefon im Footer, Seiten Impressum, Datenschutzerklärung, AGB, Cookie-Einstellungen.

## 7. Material im Projekt

| Material | Befund |
|---|---|
| `klhe-projekt-briefing.md` | Grundlage; zwei Punkte korrigiert (Sitemap-Name, Buchseiten existieren) |
| `Liste Bücher.xlsx` | 77 Titel mit ISBN, Titel, Amazon-Link, einzelnen Kommentaren. Es fehlen Untertitel, Autor, Formate, Seiten, Klappentext, Hörbuch, Übersetzungen, „nur Amazon“ |
| `Buchcover.zip` | 13 Screenshots mit 3D-Mockups (~37 Titel), keine flachen Cover, keine ISBN-Dateinamen |
| `Leseproben Finance-Titel.zip` | 9 PDF-Leseproben = genau die 9 Titel der Finanzreihe |
| `skills-planen-umsetzen.zip` | Eure Arbeitsweise: /planen → `PLAN-<thema>.md` → /umsetzen in neuer Session |
| Logos | `KLHE_Logo_Schwarz.png`, `KLHE_Logo_Weiß.png` (1987 × 455 px), **kein SVG** |
| Print | Flyer A5 lang (3 Ansichten), Programmflyer DIN lang, Finanzbücher-Broschüre: Schwarz-Weiß, kräftige Grotesk, grauer Schwung, Imprint-Schriftzüge (finance, helper, kids, travel, psychology) |
| Fotos | 19 Bilder von Chris und Jens (Porträts, Vorträge, 2 sehr alte Interviewfotos) |

**Presse-Belege im Projekt** (Zuordnung zu Titeln; ✓ = wird bereits auf buchbuddy.de genutzt)

| Medium | Ausgabe | Titel / Person | BB |
|---|---|---|---|
| Focus Money | 05/2018 | Die Faulbär-Strategie zur Million | ✓ |
| Bank und Umwelt | 2018/19 | Ökoethinvesting | ✓ |
| Eve | 01/2020 | Ökoethinvesting | ✓ |
| Chance | 03/2020 | Glück – der ultimative Ratgeber | ✓ |
| Rhein Main Magazin | 09/2020 | Geld sparen und clever reich werden | ✓ |
| Psychologie Heute | 10/2022 | Mutmacherinnen | |
| Prisma | 11/2022 | Katrin Lange, Bei Gegenwind loslaufen | ✓ |
| tina | Nr. 50, 06.12.2023 | Katrin Lange | ✓ |
| Niederrhein Nachrichten | ohne Datum | Katrin Lange | ✓ |
| Rhein Main Magazin | 03/2025 | Englische Grammatik 1 + 2 | |
| Rhein Main Magazin | 08/2025 | Becoming Dad, Kleine Redner große Worte | |
| Tagesspiegel | 01.09.2025 | Kleine Redner, große Worte | |
| Rhein Main Magazin | 02/2026 | GOLF, Suchbuch, Monsterparade, Wuselbande | |
| Fürther Nachrichten, Landsberger Zeitung | ohne Datum | Elfe Filia regelt das | |
| Zeitungsartikel (Quelle offen) | | Ausgeschieden; Die verlorenen Jahre; Finde dein Warum | |
| Mutmacherinnen-Presse + Bestseller-Bild | | Mutmacherinnen | |
| Jolie (Foto) | | Chris als Experte | ✓ |

Auf buchbuddy.de zusätzlich genannt, Beleg nicht im Projekt: WDR „Hier und heute“ 27.10.2023 (Celine Stüker), RTL.de, Cashkurs, Frankfurter Buchmesse, Content Shift Accelerator 2021, future!publish. Auf klhe.de genannt, Beleg fehlt: BUNTE 05/2019, Geld-Magazin Österreich 2015.

## 8. Folgen für Weiterleitungen (Entwurf, Details nach den Entscheidungen)

| Alte Adressen | Anzahl | Vorschlag |
|---|---|---|
| Bonus-, Download-, Hörbuchseiten | 42 | **gleiche Adresse behalten** (statische Seite am selben Pfad) |
| `/wp-content/uploads/…` Download-Dateien | ? | **gleiche Adresse behalten** (Dateien 1:1 ins Repo) |
| Golf/Tennis-Kopien unter `/allgemein/` | 2 | 301 → neue Buchseite |
| Buchseiten `/project/…` | 57 | 301 → neue Buchseite |
| Shop-Produkte `/product/…` | 54 | 301 → neue Buchseite (Finanz-Kochbuch, E.S.E.L. → Bücher-Übersicht) |
| Personenseiten | 18 | 301 → Buchseite der Person bzw. Bücher-Übersicht |
| Archive | 93 | 301 → Bücher-Übersicht bzw. neue Kategorie |
| `/verlag/`, `/team/` | 2 | 301 → Über uns |
| `/datenschutzerklaerung/`, `/impressum-2/` | 2 | 301 → neue Datenschutz- bzw. Impressumsseite |
| Shop-Seiten (Warenkorb, Kasse, Konto, AGB, Widerruf, Versand, Zahlung, Bewertungen) | 9 | 301 → Bücher-Übersicht, falls der Shop entfällt |
| `/under-construction/`, `/manuskript-einsenden/` | 2 | 301 → Startseite bzw. Autorenseite |

Abfrage-Parameter (`?fbclid=…`) werden ignoriert.

---

## Anhang A: Titeltabelle (77 Titel aus der Liste)

„Kategorie-Vorschlag“ und „Reihe“ sind ein erster Vorschlag von Claude zur Diskussion, nicht entschieden. „heute auf klhe.de“ nennt den heutigen Filter.

| # | Titel (laut Liste) | ISBN | Amazon-Link | heute auf klhe.de | Kategorie-Vorschlag | Reihe |
|---|---|---|---|---|---|---|
| 1 | Visualisierung mit der Kraft der Gedanken | 978-3-947061-09-9 | ok | nein | Ratgeber |  |
| 2 | Glück - der ultimative Ratgeber | 978-3-947061-23-5 | ok | ja (Helper) | Ratgeber |  |
| 3 | Ziele finden, setzen und erreichen | 978-3-947061-25-9 | ⚠ zeigt auf 3981579488, ISBN erwartet 3947061250 | nein | Ratgeber |  |
| 4 | Autosuggestion mit der Kraft der Gedanken | 978-3-947061-27-3 | ok | nein | Ratgeber |  |
| 5 | Meditation für Anfänger | 978-3-947061-28-0 | ok | nein | Ratgeber |  |
| 6 | Wer gibt, wird reicher!: Eine radikale Anleitung für Selbst- und Weltverbesserer | 978-3-947061-34-1 | ok | ja (Helper) | Ratgeber |  |
| 7 | Hermetik - hermetische Gesetze | 978-3-947061-54-9 | ok | ja (Helper) | Ratgeber |  |
| 8 | Tag auf Tag im Hamsterrad | 978-3-947061-80-8 | ok | ja (Finance) | Ratgeber | Finanzreihe Chris & Jens |
| 9 | Der Hamster verlässt das Rad | 978-3-947061-81-5 | ok | ja (Finance) | Ratgeber | Finanzreihe Chris & Jens |
| 10 | Geld sparen und clever reich werden | 978-3-947061-82-2 | ok | ja (Finance) | Ratgeber | Finanzreihe Chris & Jens |
| 11 | Mein Geldbaum | 978-3-947061-48-8 | ok | ja (Finance) | Ratgeber | Finanzreihe Chris & Jens |
| 12 | Nine to five muss nicht sein! | 978-3-947061-84-6 | ok | ja (Finance) | Ratgeber | Finanzreihe Chris & Jens |
| 13 | Einmal Dividende bitte! | 978-3-947061-85-3 | ok | ja (Finance) | Ratgeber | Finanzreihe Chris & Jens |
| 14 | Die Faulbär Strategie zur Million | 978-3-947061-86-0 | ok | ja (Finance) | Ratgeber | Finanzreihe Chris & Jens |
| 15 | Mit Blockchain zum Krypto-Investor | 978-3-947061-87-7 | ok | ja (Finance) | Ratgeber | Finanzreihe Chris & Jens |
| 16 | Ökoethinvesting | 978-3-947061-88-4 | ok | ja (Finance) | Ratgeber | Finanzreihe Chris & Jens |
| 17 | Erfolgshacks | 978-3-947061-91-4 | ok | ja (Helper) | Ratgeber |  |
| 18 | Dr. Raabes Formulierungshelfer | 978-3-98538-009-1 | ok | ja (Learn) | Ratgeber |  |
| 19 | Glücklich denken - glücklich leben! | 978-3-947061-90-7 | ⚠ zeigt auf 3985380252, ISBN erwartet 3947061900 | ja (Helper) | Ratgeber |  |
| 20 | Mutmacherinnen SC | 978-3-98538-026-8 | ok | ja (Helper) | Ratgeber |  |
| 21 | Bei Gegenwind loslaufen - Mein Leben zwischen Brustkrebs und Corona-Pandemie | 978-3-98538-058-9 | ok | ja (Helper) | Lebensgeschichten |  |
| 22 | Lateinamerikanisches Spanisch lernen | 978-3-98538-061-9 | ok | nein | Ratgeber |  |
| 23 | Vermögensfalle Eigenheim? | 978-3-947061-95-2 | ok | nur im Shop | Ratgeber | Finanzreihe? |
| 24 | Das witzige Sport Mitmachbuch | 978-3-98538-077-0 | ok | ja (Kids) | Kinderbücher | Mitmachbücher |
| 25 | Affe Loki und die Reise zur Schatzinsel | 978-3-98538-078-7 | ok | ja (Kids) | Kinderbücher |  |
| 26 | Mama, wer wohnt eigentlich am Meer? | 978-3-98538-076-3 | ok | ja (Kids) | Kinderbücher | Mama, wer wohnt …? |
| 27 | Das tierische Mitmachbuch | 978-3-98538-080-0 | ok | ja (Kids) | Kinderbücher | Mitmachbücher |
| 28 | Einmal Himmel und zurück zu mir | 978-3-98538-081-7 | ok | ja (Helper) | Lebensgeschichten |  |
| 29 | Der erste Tag im Tierkinderhort | 978-3-98538-106-7 | ok | ja (Kids) | Kinderbücher |  |
| 30 | Akupressur bei psychischen Beschwerden | 978-3-98538-109-8 | ok | ja (Helper) | Ratgeber | Akupressur |
| 31 | Akupressur bei körperlichen Beschwerden | 978-3-98538-110-4 | ok | ja (Helper) | Ratgeber | Akupressur |
| 32 | Michael Air Jordan - der GOAT | 978-3-98538-123-4 | ASIN B0CGTTTMX1 (prüfen: E-Book/KDP?) | ja (Learn) | Geschenkbücher? |  |
| 33 | Zeitzeugen Teil 1, 42 verlorene | 978-3-98538-130-2 | ASIN B0CJXGRXF4 (prüfen: E-Book/KDP?) | ja (Learn) | Lebensgeschichten | Zeitzeugen |
| 34 | Zeitzeugen Teil 2, 51 verlorene | 978-3-98538-131-9 | ASIN B0CJXHRB3N (prüfen: E-Book/KDP?) | ja (Learn) | Lebensgeschichten | Zeitzeugen |
| 35 | Becoming Dad | 978-3-98538-138-8 | ok | ja (Helper) | Ratgeber |  |
| 36 | Psychedelika - Reisen an die Grenzen des Bewusstseins | 978-3-98538-142-5 | ok | ja (Helper) | Ratgeber |  |
| 37 | Chinesisch kochen mit Elsie Ai | 978-3-98538-145-6 | ⚠ zeigt auf 3985381437, ISBN erwartet 3985381453 | ja (Helper) | Ratgeber |  |
| 38 | Die verlorenen Jahre | 978-3-98538-150-0 | ok | ja (Learn) | Lebensgeschichten |  |
| 39 | All the things I never talked about | 978-3-98538-154-8 | ASIN B0DBM4DJ1T (prüfen: E-Book/KDP?) | ja (Helper) | Lebensgeschichten |  |
| 40 | Englische Grammatik Teil 1 | 978-3-98538-161-6 | ok | ja (Learn) | Ratgeber | Englische Grammatik |
| 41 | Tarot Karten Set SehlenReise | 978-3-98538-165-4 | ok | ja (Helper) | Geschenkbücher |  |
| 42 | Ausgeschieden | 978-3-98538-166-1 | ok | ja (Helper) | Lebensgeschichten |  |
| 43 | Englische Grammatik Teil 2 | 978-3-98538-167-8 | ok | ja (Learn) | Ratgeber | Englische Grammatik |
| 44 | Finde Dein WARUM und lebe! | 978-3-98538-171-5 | ok | ja (Helper) | Ratgeber |  |
| 45 | Nürnberg Guide mit Hotspots! | 978-3-98538-173-9 | ok | ja (Travel) | Reisen |  |
| 46 | Kuschelige Momente Herbst & bunter Wald Ausmalbuch (Band 5) | 978-3985382156 | ok | nein | Ausmalbücher | Kuschelige Momente |
| 47 | Kuschelige Momente Sommer & Ferien Ausmalbuch (Band 4) | 978-3985381999 | ok | ja (Coloring, als Band 3) | Ausmalbücher | Kuschelige Momente |
| 48 | Kuschelige Momente Hygge Café & Bäckerei Ausmalbuch (Band 3) | 978-3985382101 | ok | nein | Ausmalbücher | Kuschelige Momente |
| 49 | Kuschelige Momente Blumen & Frühling (Band 2) | 978-3-98538-198-2 | ok | ja (Coloring) | Ausmalbücher | Kuschelige Momente |
| 50 | Kuschelige Momente ruhige Motive (Band 1) | 978-3-98538-195-1 | ok | ja (Coloring) | Ausmalbücher | Kuschelige Momente |
| 51 | Kleine Redner, große Worte | 978-3-98538-176-0 | ok | ja (Helper + Kids) | Kinderbücher |  |
| 52 | Buchmarketing Blueprint | 978-3-98538-177-7 | ok | ja (Helper) | Ratgeber |  |
| 53 | Elfe Filia regelt das | 978-3-98538-181-4 | ok | ja (Kids) | Kinderbücher |  |
| 54 | GOLF - unnützes Wissen für Tee, Tresen und das 19. Loch | 978-3-98538-193-7 | ok | ja (Learn) | Geschenkbücher | Unnützes Wissen |
| 55 | Weniger ist auch gut genug | 978-3-98538-196-8 | ok | ja (Helper) | Ratgeber |  |
| 56 | Tennis - unnützes Wissen für Tennisspieler | 978-3985381944 | ok | ja (Learn) | Geschenkbücher | Unnützes Wissen |
| 57 | Unnützes Wissen Wilder Westen | 978-3985382163 | ok | nein | Geschenkbücher | Unnützes Wissen |
| 58 | Mein Besuch beim Zahnarzt | 978-3-98538-200-2 | ok | nein | Kinderbücher | Mutmachbücher Arztbesuch |
| 59 | Mein Besuch beim Tierarzt | 978-3-98538-201-9 | ok | nein | Kinderbücher | Mutmachbücher Arztbesuch |
| 60 | Mein Besuch beim HNO | 978-3-98538-202-6 | ok | nein | Kinderbücher | Mutmachbücher Arztbesuch |
| 61 | Mein Besuch beim Kinderarzt | 978-3-98538-203-3 | ok | nein | Kinderbücher | Mutmachbücher Arztbesuch |
| 62 | Mein Besuch bei der Logopädie | 978-3-98538-204-0 | ok | nein | Kinderbücher | Mutmachbücher Arztbesuch |
| 63 | Mein Besuch bei der Kieferorthopädie | 978-3-98538-205-7 | ok | nein | Kinderbücher | Mutmachbücher Arztbesuch |
| 64 | Mein Besuch beim Hausarzt | 978-3-98538-206-4 | ok | nein | Kinderbücher | Mutmachbücher Arztbesuch |
| 65 | Mein Besuch bei der Ergotherapie | 978-3-98538-207-1 | ok | nein | Kinderbücher | Mutmachbücher Arztbesuch |
| 66 | Mein Besuch beim Augenarzt | 978-3-98538-208-8 | ok | nein | Kinderbücher | Mutmachbücher Arztbesuch |
| 67 | Meine erste Impfung | 978-3-98538-209-5 | ok | nein | Kinderbücher | Mutmachbücher Arztbesuch |
| 68 | Mein erster Krankenhaus Aufenthalt | 978-3-98538-211-8 | ok | nein | Kinderbücher | Mutmachbücher Arztbesuch |
| 69 | Das erste Mal Blut abnehmen | 978-3-98538-212-5 | fehlt (noch nicht online) | nein | Kinderbücher | Mutmachbücher Arztbesuch |
| 70 | Das erste Mal Allergie | 978-3-98538-213-2 | fehlt (noch nicht online) | nein | Kinderbücher | Mutmachbücher Arztbesuch |
| 71 | Mein Buch tut weh | 978-3-98538-214-9 | ok | nein | Kinderbücher | Mutmachbücher Arztbesuch? |
| 72 | Das total verrückte Suchbuch | 978-3-98538-191-3 | ok | ja (Kids) | Kinderbücher |  |
| 73 | Die große Monsterparade: Das verschwundene Signalhorn | 978-3-98538-186-9 | ok | ja (Kids) | Kinderbücher |  |
| 74 | Ein etwas anderes Ausmalbuch: Dein kreativer Weg aus Stress, Angst und Überforderung bei Autismus, ADHS und Hochsensibilität | 978-3-98538-185-2 | ok | ja (Coloring) | Ausmalbücher |  |
| 75 | Selbstfürsorge Planer: Kleine Schritte, große Veränderungen | 978-3-98538-174-6 | ok | ja (Helper) | Ratgeber |  |
| 76 | Mama, wer wohnt eigentlich auf dem Bauernhof? | 978-3-98538-079-4 | ok | ja (Kids) | Kinderbücher | Mama, wer wohnt …? |
| 77 | Die Wuselbande sucht das Gähnen: Ein chaotisch-lustiges Mitmachbuch zum Pusten, Schütteln und Gute Nacht sagen | 978-3985381838 | ok | ja (Kids) | Kinderbücher | Mitmachbücher |

Dazu (nicht in der Liste, aber auf der Website): Der Düsseldorf Guide (Travel), Das große Fürth Wimmelbuch (Kids), Mikroabenteuer in Franken (Travel).
