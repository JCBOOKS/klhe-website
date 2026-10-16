# KLHE-Website: Entscheidungen, offene Fragen, To-dos

Stand 16.10.2026, ca. 10:30 Uhr (Etappe 3: Website gebaut, wartet auf Livegang) · Dieses Dokument ist die Übergabe zwischen Chats: Was hier nicht steht, gilt als nicht entschieden.

Grundlagen: `klhe-projekt-briefing.md` · `klhe-bestandsaufnahme.md` · `klhe-url-inventar.md` · `klhe-inhalte-rohmaterial.md` · `klhe-seitenplan.md`

---

## 0. Ziel der Website (Chris, 15.10.2026)

KLHE ist **Aushängeschild für BuchBuddy**: Autor:innen, die in einem Verlag veröffentlichen wollen, sollen von klhe.de beeindruckt sein. Kernargument: Über KLHE ist ein Buch im gesamten Buchhandel bestellbar (Barsortimentsverträge, Verlagsauslieferung). Die Seite muss als echter Verlag wirken, nicht als Privatprojekt von Chris und Jens. Nach dem Hack der WordPress-Seite: einfache, solide, statische Seite als **schnelle 80/20-Lösung**.

## A. Entschieden

**Inhalt und Programm**
- A1 Kauf-Links nur zu Amazon. Formate werden nicht einzeln verlinkt.
- A2 Buchhandel als Hinweis und Social Proof (Händler-Logos erlaubt). Nicht jeder Titel ist im Buchhandel: Hinweis nur bei gelisteten Titeln.
- A3 Übersetzungen nur als dezenter Hinweis, keine eigenen Seiten, keine Detailangaben.
- A4 Hörbücher als Hinweis: Audible und über 1.600 weitere Shops (Formulierung des Distributors).
- A5 Kategorien: **Ratgeber · Lebensgeschichten · Kinderbücher · Ausmalbücher · Geschenkbücher · Reisen** (Vorschlag B3 aus v1, von Chris bestätigt).
- A6 Reihen sichtbar: Mitmachbücher · Mutmachbücher vor Arztterminen · Unnützes Wissen · Finanzreihe Chris & Jens · Kuschelige Momente.
- A7 Neuere Titel groß, ältere Titel und Reihen zusammengefasst und kleiner.
- A8 Titel raus: Düsseldorf Guide (schlecht bewertet), Das große Finanz-Kochbuch, Finanzkochbuch light, E.S.E.L.-Strategie, ROMI-Methode, Inside Modern Family, fremdsprachige Ausgaben.
- A9 Titel rein: Das große Fürth Wimmelbuch, Mikroabenteuer in Franken; die vier alten Helper-Titel und Lateinamerikanisches Spanisch kompakt.
- A10 Keine Preise auf der Website.
- A11 Klappentexte: Claude kürzt und vereinheitlicht aus heutiger Website bzw. Amazon, Chris gibt frei.
- A12 Zahlen dürfen genannt werden: **seit 2011, über 50 Titel, 500.000+ verkaufte Bücher, Amazon-Bestseller**. Belege existieren intern, werden nicht gezeigt.
- A13 Mutmachbücher: dezenter Hinweis auf personalisierte Praxis-Ausgaben (praxis-kinderbuch.de).

**Verlag und Autor:innen**
- A14 KLHE sucht keine Autor:innen aktiv. „Keine unverlangten Manuskripte“ plus Verweis auf BuchBuddy. Keine Kosten auf klhe.de.
- A15 Programmentscheidung: KLHE entscheidet, was ins Programm passt. Autor:innen bringen Reichweite mit oder investieren ins Marketing. Kein Druckkostenzuschussverlag.
- A16 Begriffe wie Verlagsauslieferung, Barsortimente, VLB, Händlerkonditionen dürfen sichtbar sein (Kompetenzsignal).
- A17 Die Wahrnehmung als „Zuschussverlag“ nimmt Chris in Kauf.

**Abgeschaltet bzw. gestrichen**
- A18 Shop (WooCommerce) entfällt; heute rund eine Bestellung pro Quartal. AGB, Widerruf, Versand, Zahlung entfallen.
- A19 Team-Seite und alle Personenseiten entfallen. Autor:innen erscheinen bei ihrem Buch.
- A20 Newsletter und GetResponse werden abgeschaltet (rund 1.200 € pro Jahr ohne Gegenwert). Bonusmaterial wird ohne Anmeldung direkt herunterladbar.
- A21 Kein Kontaktformular. Kontakt per E-Mail an info@klhe.de.
- A22 Kein Tracking, keine Anzeigen. Ziel: keine Cookies, kein Banner.

**Technik und Recht**
- A23 Impressum und Datenschutz neu nach BuchBuddy-Vorbild, Anbieter GbR C. Klein & J. Helbig, Hortensienstraße 26, 40474 Düsseldorf.
- A24 Amazon-Partner-Tag bleibt (`jcbooks04-21`); dafür Pflichthinweis im Footer und Absatz im Datenschutz.
- A25 Bilder und Presse aus dem BuchBuddy-Relaunch dürfen mitgenutzt werden.

**Nachgetragen 15.10.2026, 12:48 (zweite Antwortrunde)**
- A26 **Seitenplan v1 freigegeben.** Eigene Seite pro Buch ist okay, solange sie kurz und übersichtlich bleibt.
- A27 **Bonusmaterial:** eine einzige Bonusseite, nach Kategorien geordnet, aufklappbar, ohne Eintragung. Alle alten Bonus-Adressen (aus Büchern und Hörbüchern) leiten dorthin. GetResponse wird gekündigt. Eigenes Material für Mutmacherinnen und Akupressur gibt es vermutlich, Psychedelika unklar: klärt Chris später, sobald die Vorschau steht.
- A28 **USt-IdNr.:** DE320046102 (identisch mit dem heutigen Impressum, war also korrekt).
- A29 **Telefon im Impressum:** Festnetznummer von BuchBuddy, 0211 53804066.
- A30 **Repo-Vorlage:** GitHub `BuchBuddy/buchbuddy-website`. Zugriff erst nach Verknüpfung eines GitHub-Kontos in claude.ai.
- A31 **Hörbuch-Distributor:** Feiyr.
- A32 **Facebook** (`facebook.com/KLHE.Verlag`) und **Instagram** (`instagram.com/klhe_verlag`) kommen in den Footer.
- A33 Gestaltung: Die Finanzreihe ist Ursprung des Verlags, aber älter; der Verlag hat sich weiterentwickelt. Das soll auch visuell sichtbar sein (Finanzreihe als eine Reihe unter mehreren, Chris und Jens als Verleger).

**Nachgetragen 15.10.2026, 14:17 (Feedback zur Vorschau v1)**
- A34 **Vorschau v1 abgelehnt:** zu nah am alten KLHE (Schwarz-Weiß), zu nüchtern. Gewünscht: neue Farben, modernes Layout, emotional und bildgetragen wie BuchBuddy, Reihen groß als Cover-Gruppen inszeniert.
- A35 **„Empfohlen“ bunt gemischt:** eigene Titel von Chris und Jens ausdrücklich erlaubt; Mischung in Farbe, Covergestaltung und Inhalt.
- A36 **ROMI fliegt komplett raus**, das Bonusmaterial ebenfalls.
- A37 **Titel von Christopher Klein, nicht im Buchhandel:** Mikroabenteuer in Franken, Die große Monsterparade, Das große Fürth Wimmelbuch (Kostenstruktur: nur über Amazon vorgedruckt). „Mein Bauch tut weh“ ebenfalls von Chris, Buchhandel noch offen.
- A38 **Projektordner** `~/Projekte/klhe-website` auf Chris’ Mac, Zugriff für Claude freigegeben. Material (fehlende Cover) legt Chris später dort ab.
- A39 **Zusatzmaterial „Kleine Redner, große Worte“:** laut Tagesspiegel (01.09.2025) auf sprechburg.de. Auf der Bonusseite als Link.

**Nachgetragen 15.10.2026, 14:54 (Feedback zur Vorschau v2)**
- A40 **Keine Titelanzahl nennen.** „50+ Titel“ wirkt für einen Verlag eher klein und damit kontraproduktiv. Gilt auch für Zählungen wie „20+ Autor:innen“ und Titelzahlen pro Kategorie. Ersetzt A12 teilweise: genannt werden nur noch „seit 2011“, „500.000+ verkaufte Bücher“, „Amazon-Bestseller“.
- A41 *(ersetzt durch A46)* **Weniger bunt:** v2 war zu bunt. Eine Markenfarbe (Indigo), ein Akzent (Koralle); alle anderen Flächen neutral, die Farbe kommt aus Covern und Illustrationen.
- A42 **Finanzreihe nicht auf dunklem Grund:** Die Cover gingen auf Dunkelblau unter. Jetzt heller Grund und flache Cover.
- A43 Die bewegte Bücherwand im Einstieg gefällt und bleibt.
- A44 Neue Cover und A+-Grafiken von Chris im Projekt (Kuschelige Momente 1–5, Zahnarzt, Suchbuch, Wuselbande, Fürth Wimmelbuch). Weitere Cover darf Claude aus vorhandenem Material ausschneiden (Programmflyer, Magazine).

**Nachgetragen 15.10.2026, 15:14 (Feedback zur Vorschau v3)**
- A45 **Leseproben entfallen.** Kein Leseproben-Bereich auf Reihen- oder Buchseiten.
- A46 **Kein Blau, komplett neuer Gestaltungsansatz.** Modern ist gut, Indigo passt nicht. Ersetzt A41 (Indigo/Koralle).
- A47 **Chris und Jens sichtbar machen:** Wo sind wir, wo ist unsere Kompetenz, wo unsere Geschichte? Gilt besonders für die Finanzreihe (dort war rechts nichts von Euch zu sehen).
- A48 **A+-Grafiken sind keine Cover**, sondern Zusatzmaterial für Amazon. Sie eignen sich als Einblicke auf eigenen Kinderbuch-Seiten, vor allem für Mutmachbücher und Kuschelige Momente.

**Nachgetragen 15.10.2026, 15:56 (Feedback zur Vorschau v4)**
- A49 **Claim bleibt „Bücher, die bewegen.“**
- A50 **Die Geschichte passt** („unsere Story super“), Texte der Verlagsseite gelten als freigegeben.
- A51 **Kein Gelb, keine Serifen.** v4 wirkte wie eine Zeitung; weil das Programm vor allem aus Ratgebern besteht, nur serifenlose Schrift. v3 war moderner.
- A52 **Reihenname: „Mutmachbücher vor dem Arztbesuch“.**
- A53 **Chris und Jens weniger präsent:** nicht im Einstieg der Startseite, sonst (weiter unten, Verlagsseite, Finanzreihe) passt es.
- A54 **Richtung Pastell:** leichte, eher transparente Pastellfarben wie bei BuchBuddy, ruhig statt unruhig. Daraus Vorschau v5.
- A55 Praxisbuch 1–7 liegen jetzt im Projektordner, alle Mutmach-Cover und A+-Grafiken sind verarbeitet.

**Nachgetragen 15.10.2026, 16:57**
- A56 **Gestaltung v5 „Transparentpapier“ freigegeben** („Richtung passt!“). Grundlage für Etappe 3. Programm, Buchseite und Bonusmaterial sind ebenfalls auf v5 umgestellt, damit liegen alle neun Seitentypen vor.

**Nachgetragen 15.10.2026, 17:07**
- A57 **Repo:** `jcbooks/klhe-website` (von Chris angelegt) ist das Repo der Website.
- A58 **Bücherliste als Entwurf ok**, Feinschliff nach dem Livegang. Schneller Umzug hat Vorrang.
- A59 **Klappentexte schreibt und kürzt Claude** ohne Einzelfreigabe (ersetzt in A11 „Chris gibt frei“).
- A60 **Cover:** Hauptsache einheitlich.

**Nachgetragen 15.10.2026, 18:54**
- A61 **Hosting:** klhe.de liegt bei IONOS und läuft über Cloudflare (Auskunft Jens). Datenschutz entsprechend angepasst (IONOS anonymisiert IP-Adressen in den Logfiles und löscht sie nach spätestens acht Wochen; Hinweis auf mögliches Sicherheits-Cookie von Cloudflare). HTTPS und www werden in Cloudflare geregelt, nicht in der `.htaccess`.
- A62 **Livegang:** Jens übernimmt, Termin noch offen.

**Nachgetragen 15.10.2026, 19:42**
- A63 **Kein Mitglied im Börsenverein** (mehr). Überall entfernt: Fuß, Impressum, Kontakt, Startseite, Für Autor:innen, Verlagsgeschichte.
- A64 **Reihenbild Kuschelige Momente** zeigt ein Cover (A+-Grafik „Blumen & Frühling“ mit Cover auf Rosa).
- A65 **Preisleiste „Wohin der Preis eines Buches geht“** zeigt jetzt auch die Verlagskosten: 10 € Handel, 2 € Auslieferung, 2 € Autor:in, 4–5 € Druck, Lektorat, Marketing, 1–2 € bleiben dem Verlag (hervorgehoben).
- A66 **Presse ausgebaut:** eigene Seite `/presse/` mit allen 21 Berichten aus den Projektdateien (neu: Psychologie Heute 06/2025 und 10/2022, Rhein Main Magazin 03/25, 08/25, 02/26, Niederrhein Nachrichten, Landsberger Zeitung, Wochenpost, drei Berichte ohne Mediennamen). „Presse“ in der Navigation führt dorthin, Buchseiten zeigen alle Berichte zum Buch.
- A67 **Cover nachgeliefert:** Michael Jordan und Der erste Tag im Tierkinderhort (F26 erledigt).

**Nachgetragen 15.10.2026, 20:14 (Presse und Belege)**
- A68 **Logos sind Pflicht:** WDR, RTL, Cashkurs und Jolie als echte Logos (grau, von buchbuddy.de übernommen) in der Leiste „Zu sehen, zu hören und zu lesen bei“ auf Start- und Presseseite. Zeitungen und Zeitschriften stehen dort als Namen; ihre Titelköpfe sind auf den Ausschnitten selbst zu sehen. Aus den Scans freigestellte Titelköpfe (Eve, Prisma, Bank & Umwelt, Niederrhein Nachrichten) waren nicht sauber genug und wurden nicht verwendet.
- A69 **Bestseller-Beleg kommt rein:** Bildschirmfoto von amazon.de, „Bestseller in Brust & Brustkrebs“, Mutmacherinnen auf Platz 1. Ausschnitt bis zur ersten Reihe, Plätze 2 und 3 (fremde Titel) aufgehellt, sonst unverändert. Steht auf `/presse/#bestseller`, auf der Startseite im Pressebereich und auf der Buchseite Mutmacherinnen; die Kennzahl „Bestseller bei Amazon“ verlinkt dorthin. Kein Datum genannt (F41). Ergänzend nach buchbuddy.de: Die Finanzreihe war Amazon-Bestseller und in den Amazon Top 100.
- A70 **Neue Beiträge (25 statt 21):** WDR „Hier und heute“, 27.10.2023, Celine Stüker zu Gast mit „Einmal Himmel und zurück zu mir“ (Beleg: buchbuddy.de und Sendungsseite bei fernsehserien.de); WDR 2 „Sonntagsfragen“ mit Gisela Steinhauer, Celine Stüker über die Reise ihres Lebens (Beleg: Bildschirmfoto mit Link zur ARD Audiothek; ohne Datum und ohne Link, F42); RTL.de, Online-Serie von Chris und Jens mit Spar- und Investmenttipps aus ihren Büchern; Cashkurs, Chris und Jens zu Gast (beide Wortlaut wie auf buchbuddy.de, ohne Datum). Jolie mit Logo, Text wie auf buchbuddy.de („Christopher Klein als Experte zitiert“). Focus Money: „Titelgeschichte, sechs Seiten“.
- A71 **Pressekarten neu:** Jede Karte zeigt den Ausschnitt auf einer Pastellfläche, mehrseitige Belege als aufgefächerter Stapel (Focus Money mit drei Seiten; Eve, Bank & Umwelt, Chance, Prisma, Rhein Main Magazin 09/2020 und tina mit zwei Seiten), davor die besprochenen Bücher als 3D-Mockup (höchstens drei). Fernsehen, Radio und Online ohne Ausschnitt: Logo und Sendungsname auf einer Karte. Die Presseseite trennt „Fernsehen, Radio und online“ von „Zeitungen und Zeitschriften“. Bei RTL.de, Cashkurs und Jolie zeigen die Mockups Bücher der Finanzreihe und verlinken auf die Reihe, nicht auf ein einzelnes Buch, weil nicht belegt ist, um welches Buch es ging.
- A72 **Startseite:** Pressebereich mit sechs Karten (WDR, Focus Money, RTL.de, Psychologie Heute, Tagesspiegel, tina) und dem Bestseller-Beleg. Finanzreihe: „Presse zur Reihe“ mit Focus Money, RTL.de, Cashkurs, Jolie, Eve, Bank & Umwelt, Rhein Main Magazin.
- A73 **Zweiter Bestseller-Beleg (15.10., 21:02):** „Nine to five muss nicht sein!“ auf Platz 1 der Amazon-Bestseller in Geldanlage & Vermögensaufbau, vor „Rich Dad Poor Dad“ und „Souverän investieren“ (Bildschirmfoto vom 18. Juli 2017, Datum aus der Taskleiste; Taskleiste und Seitenleiste abgeschnitten, Plätze 2 und 3 bewusst sichtbar). Dazu drei kleine Belege: Nr. 1 in Betriebswirtschaft, E-Commerce, Online-Marketing; Nr. 1 in Geldanlage & Vermögensaufbau (Kindle); Bestseller-Kennzeichnung. Hinweis „frühere Auflage (Kindle-Ausgabe)“ steht dabei. Zu sehen auf `/presse/#bestseller`, auf der Buchseite, auf der Finanzreihe und als Kurzform auf der Startseite (beide Belege nebeneinander). Kennzahl Startseite: „Bestseller bei Amazon, mehrfach auf Platz 1 ihrer Kategorie“.

**Nachgetragen 16.10.2026, 10:20**
- A74 **Pflichtexemplare an die Deutsche Nationalbibliothek** als Verlagsleistung genannt, neben ISBN/VLB, Barsortimenten und Verlagsauslieferung: eigene Karte unter „Was KLHE für Dein Buch leistet“ (`/autoren/`), Punkt in der Liste „Bei einem Verlag erscheinen“ auf der Startseite, Seitenbeschreibung von `/autoren/`. Text: DNB archiviert dauerhaft und verzeichnet in der Deutschen Nationalbibliografie. Landesbibliothek (NRW) bewusst nicht genannt, siehe F44.
- A75 **Fehler behoben:** Seit dem Umbau am 15.10. abends stand auf der Startseite ein überzähliges `</div>`. Dadurch lag alles ab „Unsere Verleger“ außerhalb des Seitenrahmens (Schrift fiel auf Times zurück). Repariert; `build.py --check` prüft jetzt zusätzlich, ob alle Seiten sauber verschachtelt sind.

**Nur über Amazon (KDP) erhältlich, Stand 15.10.2026** (Rest: im Buchhandel gelistet)
- Visualisierung mit der Kraft der Gedanken · Glück – der ultimative Ratgeber · Lateinamerikanisches Spanisch lernen · Mama, wer wohnt eigentlich auf dem Bauernhof? · Das total verrückte Suchbuch · Die große Monsterparade · Ein etwas anderes Ausmalbuch · Selbstfürsorge-Planer · Die Wuselbande sucht das Gähnen · Mikroabenteuer in Franken · Das große Fürth Wimmelbuch · Mein Bauch tut weh (offen)
- Geplant zu listen (bis dahin Amazon only): Kuschelige Momente (alle Bände), Tennis, Unnützes Wissen Wilder Westen, vermutlich alle Mutmachbücher. Umstellung später = eine Zelle in der Datentabelle.

## B. Vorschläge von Claude, warten auf Freigabe

- B1 **Seitenplan v1** (`klhe-seitenplan.md`), insbesondere:
- B2 **Buchseiten gestaffelt:** eigene Seite für aktuelle und wichtige Titel (~40), Reihenseiten für Mutmachbücher, Kuschelige Momente, Unnützes Wissen (je Reihe eine Seite statt Einzelseiten), ältere Titel nur als kompakte Liste. Alles aus einer Datentabelle generiert, kein Mehraufwand pro Seite.
- B3 **Bonusmaterial:** eine Seite `/bonus/` mit Abschnitten je Buch und Sprache, alle 42 alten Bonus-Adressen leiten per 301 auf den passenden Abschnitt. 35 Dateien, Liste im URL-Inventar.
- B4 **Startseite zeigt zuerst Bücher anderer Autor:innen** und deren Presse; Chris und Jens erscheinen als Verleger auf „Über uns“, die Finanzreihe als eine Reihe unter mehreren.
- B5 **Beispielrechnung „Was von einem Buch übrig bleibt“** auf der Autorenseite, als branchenübliche Größenordnung, nicht als Eure Vertragskonditionen.
- B6 **Haltung kurz und positiv** formulieren („Warum wir so arbeiten“), nicht als Abgesang auf die Branche.
- B7 Bisherige Pfade bleiben, wo es geht: `/buecher/`, `/verlag/`, `/kontakt/`, `/impressum/`, `/datenschutz/`.
- B8 Sicherheit nach dem Hack: kein WordPress-Code übernehmen, nur Inhalte und geprüfte Dateien (Whitelist pdf, zip, png, jpg, webp); WordPress samt Datenbank nach dem Livegang vollständig löschen; alle Zugangsdaten neu.

## C. Offene Fragen an Chris

- ~~F1 Buchseiten~~ → A26 · ~~F2 USt-IdNr.~~ → A28 · ~~F3 Telefon~~ → A29 · ~~F4 Repo~~ → A30 · ~~F7 Feiyr~~ → A31 · ~~F8 Social~~ → A32
- F5 **GetResponse vor der Kündigung:** Einige Inhalte gab es nur per Mail nach Anmeldung (z. B. Michael-Jordan-Hörbuchmaterial, Englisch-Newsletter). Vor der Kündigung aus den Autoresponder-Mails sichern. *(später, nach der Vorschau)*
- F6 **Bonus Mutmacherinnen, Akupressur, Psychedelika:** Die Seiten zeigen heute Blockchain-Material. Eigenes Material suchen. *(später, nach der Vorschau)*
- F9 Händlerkonditionen bei Direktbestellung: Reicht der Satz „Buchhandlungen bestellen über die Barsortimente oder direkt bei uns zu Händlerkonditionen“ ohne Prozentzahl?
- F10 Der Verlagstrailer (MP4 von 2023) auf „Über uns“ behalten oder weglassen?

## C2. Etappe 2: Gestaltungsvorschau v1 (15.10.2026)

Vorschau als Design-Canvas „KLHE Website“ (claude.ai), fünf Seiten: Startseite, Programm, Buchseite (Beispiel „Kleine Redner, große Worte“), Für Autor:innen, Bonusmaterial (aufklappbar).

- Richtung: Verlagsprogramm in Schwarz-Weiß wie Flyer und Programm; Cover tragen die Farbe; grauer Schwung aus dem Flyer als einziges Ornament; scharfe Kanten (bewusster Kontrast zu BuchBuddy); Schriften Archivo (breit, kräftig) und Spectral für Klappentexte, im Livebetrieb selbst gehostet.
- Cover: aus den Mockup-Screenshots ausgeschnitten (37 Titel), übrige als „Cover folgt“. Für den Livegang flache Original-Cover nötig (T2).
- Zahlen pro Kategorie sind Entwurf auf Basis der vorgeschlagenen Zuordnung.
- Bewusst nicht auf der Seite: „kein Druckkostenzuschussverlag“. Solange der Weg zu KLHE über ein bezahltes BuchBuddy-Paket führt, wäre der Satz angreifbar.

F11–F15 beantwortet → A34–A39.

## C3. Gestaltungsvorschau v2 (15.10.2026)

Gleicher Canvas „KLHE Website“, jetzt sechs Seiten: Startseite, Programm, Reihe (Beispiel Finanzreihe), Buchseite, Für Autor:innen, Bonusmaterial.

- **Farben:** Indigo als Marke, Koralle als Akzent; jede Reihe und jede Kategorie hat eine eigene Bühnenfarbe (Sonnengelb, Rosé, Mint, Himmelblau, Flieder).
- **Schrift:** Bricolage Grotesque (Überschriften), Figtree (Text), Newsreader kursiv für betonte Wörter. Alle frei lizenziert, im Livebetrieb selbst gehostet.
- **Bilder:** bewegte Bücherwand im Einstieg; Reihen als Cover-Fächer; Presse als echte Magazin-Titel (Focus Money, Prisma, Chance, Eve, Bank & Umwelt, Rhein Main Magazin); „Menschen hinter den Büchern“ mit Presseausschnitten (tina, Tagesspiegel, Mutmacherinnen, Ausgeschieden); Bühnenfoto und Focus-Money-Foto von Chris und Jens.
- **Gegen den Eindruck „Privatprojekt“:** Kennzahl „über 20 Autorinnen und Autoren“, Namensliste aller Autor:innen, Presse anderer Autor:innen vorn; Finanzreihe als eine von fünf Reihen.
- **Platzhalter:** Für Mutmachbücher, Kuschelige Momente, Unnützes Wissen, Mitmachbücher und einige Einzeltitel stehen farbige Platzhalter-Cover, markiert mit „Cover folgen“.

Offen zur Vorschau v2:
- F16 Trifft v2 die Richtung? Farben, Schrift, Bildsprache, Reihen-Inszenierung.
- F17 Fehlende Cover in den Projektordner legen (Liste: `material/README.md` im Ordner).
- F18 Rechte an Presseausschnitten und Fotos Dritter: dürfen Scans von Magazin-Titeln und Artikeln mit Fotos auf klhe.de gezeigt werden (bei BuchBuddy bereits so)? Autor:innen-Freigaben (T7).
- F19 „Mein Bauch tut weh“: Titel richtig (Liste: „Mein Buch tut weh“)? Gehört er zur Reihe Mutmachbücher?
- F20 Bühnenfoto: Bei welchem Anlass entstanden (für eine ehrliche Bildunterschrift)?

## C4. Gestaltungsvorschau v3 (15.10.2026)

- Ruhige Palette (A41): Indigo nur im Einstieg, im Autorenblock und im Fuß; Koralle für Haupt-Buttons und kleine Akzente; sonst Weiß und helles Grau.
- Kennzahlen-Leiste ohne Titelanzahl: seit 2011 · 500.000+ verkaufte Bücher · Buchhandel (Libri, Zeitfracht, Umbreit) · Börsenverein.
- Reihen: Finanzreihe als Fächer auf hellem Grund; Kuschelige Momente und Mutmachbücher als große Karten mit Illustration aus dem Buch; Unnützes Wissen und Mitmachbücher als kleine Karten (je nur ein Cover, markiert „weitere Cover folgen“).
- 17 Cover jetzt flach aus dem Programmflyer, dazu die neuen Cover aus Chris’ Lieferung.

Offen zur Vorschau v3:
- F21 Passt die Farbmenge jetzt?
- F22 Praxisbuch 1–7 sind für das Projekt zu groß: bitte in `~/Projekte/klhe-website/material/` legen.
- F16–F20 weiterhin offen (Rechte Presseausschnitte, „Mein Bauch tut weh“, Anlass Bühnenfoto).
- F23 Auf buchbuddy.de steht „KLHE eigener Verlag mit über 50 Titeln“. Nach A40 dort ebenfalls ändern?

## C5. Gestaltungsvorschau v4 „Schwarz auf Weiß, gelb markiert“ (15.10.2026)

Gleicher Canvas „KLHE Website“. Oben die fünf v4-Seiten, darunter v3 zum Vergleich.

- **Farbe:** warmes Papierweiß, Schwarz für Schrift und dunkle Flächen, genau eine Signalfarbe: Verlagsgelb (#FFD200) als Textmarker unter Schlüsselwörtern, für Sticker und das Buchhandels-Band. Kein Blau. Die Farbe kommt aus Covern, Illustrationen und Fotos.
- **Schrift:** Instrument Serif (Überschriften, Zahlen) und Hanken Grotesk (Text, Navigation). Beide frei lizenziert, im Livebetrieb selbst gehostet.
- **Ihr beide:** Startseite mit freigestelltem Foto von Chris und Jens auf Gelb, umgeben von Covern; Abschnitt „Die Verleger“ mit Einzelporträts und Werdegang; Zeitleiste 2007–heute; neue Seite **Verlag** mit der ganzen Geschichte (Studium, Mexiko, 300 vorgedruckte Bücher, Focus Money, BuchBuddy) und „Wofür wir stehen“. Finanzreihe mit dem Foto von Euch mit den Büchern, Focus-Money-Titel und Autorenkarten.
- **Kompetenz:** Kennzahlen (2011 · 500.000+ · 3 Barsortimente · Amazon-Bestseller), gelbes Band „Bestellbar in jeder Buchhandlung“ mit VLB, Barsortimenten und Verlagsauslieferung, Presse-Leiste.
- **Kinderbuch-Seiten aus A+-Grafiken:** Mutmachbücher (Zahnarzt-Illustrationen, Reihe mit 11 Titeln, Platzhalter für fehlende Cover, dezenter Praxis-Hinweis) und Kuschelige Momente (alle fünf Bände mit ihren A+-Bannern, Ausmalseiten).
- **Unnützes Wissen und Mitmachbücher** mit den neuen flachen Covern; Golf und Tennis mit A+-Grafiken.
- Leseproben entfernt (A45). Programm, Buchseite, Für Autor:innen und Bonus werden nach Freigabe der Richtung auf v4 umgestellt.

Offen zur Vorschau v4:
- ~~F24 v4~~ → A49–A54
- F25 **Fotos aus dem „Querdenken TV“-Interview (2016) nicht verwenden.** Im Bild stehen Banner wie „Impfkritik“, „Geopolitik“, „Freie Energie“. Für einen Verlag, der seriös wirken will, ein unnötiges Risiko. Bitte bestätigen, dass die beiden Fotos raus sind.
- F26 Cover „Der erste Tag im Tierkinderhort“: In der Datei steht mitten im Bild ein Text „vYC$QboOT (3)“ (vermutlich Ebenen- oder Dateiname). Bitte saubere Datei.
- F27 Kuschelige Momente: Autorin bzw. Illustratorin als „Jinyi Park“ nennen? Und „für jedes Alter“ als Einordnung (A+ sagt „für jeden geeignet“)?
- ~~F28 Reihenname~~ → A52
- ~~F29 Geschichte~~ → A50 (Haltungstexte bitte trotzdem kurz gegenlesen)
- F30 Fotos: Wer hat Studio- und Bühnenfotos gemacht, muss die Fotografin oder der Fotograf genannt werden? (F20 Anlass Bühnenfoto weiterhin offen.)
- F22 weiterhin: Praxisbuch 1–7 lassen sich im Projekt nicht öffnen, bitte in `~/Projekte/klhe-website/material/` legen. Ohne sie fehlen 10 Mutmach-Cover.

## C6. Gestaltungsvorschau v5 „Transparentpapier“ (15.10.2026)

Gleicher Canvas „KLHE Website“: oben sechs v5-Seiten (Start, Verlag, Finanzreihe, Mutmachbücher, Kuschelige Momente, Für Autor:innen), darunter v4 und v3 zum Vergleich.

- **Farbe:** fünf Pastelltöne wie Bögen Transparentpapier (Flieder, Rosé, Mint, Apricot, Pistazie). Sie sind leicht durchscheinend; wo sie sich überlappen, entsteht ein dritter Ton. Grundfarbe fast Weiß, Schrift Graphit, Fuß dunkel. Kein Gelb, kein Blau. Die Töne ordnen das Programm: Ratgeber Flieder, Lebensgeschichten Apricot, Kinderbücher Mint, Ausmalbücher Rosé, Geschenkbücher Pistazie.
- **Schrift:** Instrument Sans, eine Familie, Überschriften schmal und kräftig. Frei lizenziert, im Livebetrieb selbst gehostet.
- **Nähe zu BuchBuddy:** schwebende Navigationsleiste, Pastellflächen, runde Formen, kräftige Grotesk. Eigene Palette und Schrift, damit KLHE als eigener Verlag erkennbar bleibt.
- **Startseite:** Einstieg mit Claim und bewegter Cover-Wand auf Pastellbögen (keine Personen). Darunter Kennzahlen, Presse, sechs Programmbereiche, Neu und empfohlen, Reihen, der Weg ins Buchhandelsregal (VLB, Barsortiment, Auslieferung, Buchhandlung), Presse, weiter unten „Hinter KLHE stehen …“ und der Block für Autor:innen.
- **Mutmachbücher:** alle 12 Cover, dazu „Jedes Buch hat seine eigene Welt“ mit sechs „…hausen“-Welten aus den A+-Grafiken.
- **Für Autor:innen** jetzt ebenfalls in v5 (Leistungen, So arbeiten wir, Beispielrechnung als Pastell-Balken, Manuskripte über BuchBuddy).
- Nach der Freigabe (A56) ergänzt: Programm (sechs Bereiche mit Reihenkacheln und Liste älterer Ratgeber), Buchseite (Beispiel „Kleine Redner, große Worte“), Bonusmaterial (aufklappbar). Der Canvas zeigt alle neun v5-Seiten in einer Reihe, v4 und v3 als Archiv darunter.

Offen zur Vorschau v5:
- ~~F31 Richtung v5~~ → A56
- F19 „Mein Bauch tut weh“ ist in v5 als zwölfter Band der Mutmachbücher gezeigt (gleiches Design, liegt bei den Praxisbüchern). Bitte bestätigen.
- F25 weiterhin: Fotos aus dem „Querdenken TV“-Interview nicht verwenden – bitte bestätigen.
- F26 Tierkinderhort-Cover mit eingebranntem Text „vYC$QboOT (3)“ – saubere Datei.
- F27 Jinyi Park als Autorin von Kuschelige Momente nennen?
- F30 Fotograf:in der Studio- und Bühnenfotos nennen? Anlass Bühnenfoto (F20)?

## C7. Ausblick Etappe 3: Umsetzung

Was Etappe 3 braucht, bevor gebaut wird:
- **Repo-Zugang (T9):** Die Claude-GitHub-App braucht Zugriff auf das Repo in der Organisation BuchBuddy (oder ein neues Repo `klhe-website`). Ohne das baue ich im Projektordner auf dem Mac, Jens übernimmt.
- **Datentabelle (T5):** `buecher.csv` als Entwurf aus Liste, Website und Flyern; Chris prüft Kategorie, Buchhandel ja/nein, Hörbuch, Amazon-Link.
- **Klappentexte (T6):** gekürzt und vereinheitlicht, Chris gibt frei.
- **Flache Cover (T2/T13):** vor allem Kleine Redner, Tag auf Tag, Geld sparen, Mein Geldbaum und die älteren Ratgeber (heute aus Mockups ausgeschnitten).
- **Rechtstexte:** Impressum und Datenschutz nach BuchBuddy-Vorbild (A23, A24).
- Ablauf wie bei buchbuddy.de: Python-Generator, statische Seiten, 301-Weiterleitungen nach URL-Inventar, Livegang durch Jens.

## C8. Etappe 3: Website gebaut (15.10.2026)

Code im Repo `jcbooks/klhe-website` (Branch `main`), Kopie im Projektordner unter `~/Projekte/klhe-website/website/`. Anleitung in `README.md`, Arbeitsplan in `PLAN-klhe-relaunch.md`.

- **Generator:** `build.py` (Python + Jinja2) baut 64 Seiten nach `public/`: Start, Programm, 51 Buchseiten, 5 Reihenseiten, Verlag, Für Autor:innen, Kontakt, Bonusmaterial, Impressum, Datenschutz, 404. Dazu `sitemap.xml`, `robots.txt`, `.htaccess`. Linkprüfung: alle internen Links und Anker in Ordnung.
- **Daten:** alle 77 Titel in `data/buecher.csv` (51 mit eigener Seite, 20 nur auf Reihenseiten, 6 als „Weitere Ratgeber“). Liste von Chris ist maßgeblich für ISBN und Amazon-Link. Die drei falschen Amazon-Links sind korrigiert (ISBN-10), für Fürth und Mikroabenteuer ist der Link aus der ISBN erzeugt.
- **Klappentexte:** für alle Titel mit eigener Seite neu geschrieben und gekürzt (40 bis 90 Wörter), nur aus alter Website, Untertiteln und Liste. Keine Heilversprechen bei Akupressur, Psychedelika, Tarot.
- **Cover:** 69 Cover einheitlich aufbereitet (WebP, lange Kante 720 px, Mockup-Kanten und Schatten abgeschnitten, auf der Seite alle mit gleichem Schatten). Tierkinderhort und Michael Jordan mit Platzhalter „Cover folgt“.
- **Mutmachbücher:** 12 Titel einschließlich „Mein Bauch tut weh“ (F19). „Das erste Mal Blut abnehmen“ und „Das erste Mal Allergie“ sind noch nicht online und fehlen deshalb.
- **Weiterleitungen:** 222 alte Adressen einzeln (Buch-, Personen-, Shop-, Bonus- und Rechtsseiten, 31 Bonusdateien), Archivseiten per Muster nach `/buecher/`, WordPress-Reste und ROMI- bzw. Finanzkochbuch-Dateien mit 410. Abfrage-Parameter wie `?fbclid` werden verworfen. Geprüft mit `tools/test_weiterleitungen.py`.
- **Bonusmaterial:** 31 Dateien (ROMI und Finanzkochbuch light entfallen). Sie liegen noch auf dem alten Server; `tools/bonus_holen.py` holt sie einmalig. Bis dahin steht bei jedem Eintrag „folgt“.
- **Rechtstexte:** Impressum (§ 5 DDG, USt-IdNr., MStV, Börsenverein, Amazon-Partner, Verbraucherstreitbeilegung, Bildnachweise) und Datenschutz (Hosting, Cloudflare, keine Cookies, E-Mail, Amazon-Links, Rechte, LDI NRW) nach BuchBuddy-Vorbild.
- **Technik:** Schrift Instrument Sans selbst gehostet, kein externes Skript, keine Cookies. Neues Favicon (K auf Pastellbögen). Mobilansicht mit Menü-Knopf.

Offen aus Etappe 3 (vor dem Livegang klären):
- ~~F32 Hosting~~ → A61
- F33 **Verantwortlich nach § 18 Abs. 2 MStV:** eingetragen sind Chris und Jens gemeinsam. Oder nur eine Person?
- F34 **Hauptadresse:** gebaut für `https://www.klhe.de` (wie bisher). Oder ohne www?
- F35 **ISBN-Abweichungen** zwischen alter Website und Liste (Website zeigt die Liste): Der Hamster verlässt das Rad (alt 978-3966980555, Liste 978-3-947061-81-5), Mit Blockchain zum Krypto-Investor (alt 978-3966980562, Liste 978-3-947061-87-7), Nürnberg Guide (alt 978-3-98538-126-5, Liste 978-3-98538-173-9), Ein etwas anderes Ausmalbuch (alt 978-3985381845, Liste 978-3-98538-185-2), Mutmacherinnen (alt 978-3-98538-008-4, Liste 978-3-98538-026-8).
- F36 **Auflage „Tag auf Tag im Hamsterrad“:** alte Website „7. Auflage 2020, erstmals erschienen 2013“, Liste und Verlagsgeschichte „6. Auflage“, Gründung 2011 mit diesem Buch. Die Buchseite nennt vorerst keine Auflage.
- F37 **Kuschelige Momente:** Bandnummern nach der Liste (Hygge Band 3, Sommer Band 4; alte Website: Sommer Band 3). Band 1 heißt auf der Website „Kleine Auszeiten“ wie auf dem Cover, in der Liste „ruhige Motive“.
- F39 **Presse ohne Mediennamen:** Bei drei Berichten steht kein Zeitungsname auf dem Ausschnitt: „Das Leben auf der dunklen Seite der Rennbahn“ (14. Mai 2024, Ausgeschieden), „Die Schockstarre in Mut verwandeln“ (Kiel, 22. April 2022, Mutmacherinnen), „Brustkrebs: Betroffene schreiben Buch“ (Mutmacherinnen). Welche Zeitungen? Außerdem bestätigen: „Landsberger Zeitung“ (so im Dateinamen; heißt sie genau so?) und „Wochenpost Hohenlohe-Franken“ (aus Logo und E-Mail-Adresse auf der Seite abgeleitet).
- F40 **Weitere Presse:** WDR, WDR 2, RTL.de und Cashkurs sind jetzt drin (A70), Bestseller-Bildschirmfoto auch (A69). Weiter offen: Datum und Thema von RTL.de und Cashkurs; Artikel zu Ausgeschieden, Die verlorenen Jahre, Finde dein Warum (T8). Nicht aufgenommen: „Onkolotsin hilft mit eigener Erfahrung“ (Thema ist der Verein, nicht das Buch). Ganze Artikel werden nicht zum Lesen angeboten, nur Vorschaubilder (Rechte der Verlage).
- F41 **Bestseller-Datum:** Wann entstand das Amazon-Bildschirmfoto zu Mutmacherinnen? Mit Datum („Platz 1 im Mai 2022“ o. ä.) wirkt der Beleg noch stärker.
- F43 **Beleg für „Amazon Top 100“:** Die neuen Bildschirmfotos zeigen Platz 1 in Kategorien und Rang 383 bzw. 735 im Kindle-Shop insgesamt, also nicht die Top 100. Die Aussage „Finanzreihe in den Amazon Top 100“ (von buchbuddy.de) steht weiter als Satz ohne Bild. Auf der alten klhe.de stand: „Der Hamster verlässt das Rad“ 2018 auf Platz 2 im Kindle-Shop. Gibt es davon ein Bildschirmfoto? Das wäre der stärkste Beleg.
- F44 **Landes-Pflichtexemplar:** Neben der DNB verlangt NRW-Landesrecht ein Exemplar für die zuständige Landesbibliothek (nach dem Gesetz von 2013 für Verlage im Regierungsbezirk Düsseldorf die ULB Düsseldorf; das Gesetz wurde zum 1.1.2022 neu gefasst). Macht KLHE das? Dann ergänzen wir es.
- F42 **WDR 2 „Sonntagsfragen“:** Sendedatum? Ist die Folge in der ARD Audiothek noch abrufbar (von hier aus nicht prüfbar)? Dann setzen wir den Link. Außerdem: Gibt es saubere Logos (SVG/PNG) von Focus Money, Psychologie Heute, Tagesspiegel, Prisma usw.? Dann kommen sie in die Leiste.
- F38 Autor:innen der Mutmachbücher und des Tarot-Sets sind nicht genannt, weil unbekannt. Nennen?

## D. To-dos (Material)

| # | Was | Wer | Status |
|---|---|---|---|
| T1 | Die 31 Bonusdateien holen, ohne Suchen und Verlinken: Ordner `wp-content/uploads` per FTP herunterladen und `python3 tools/bonus_holen.py --ordner <Ordner>` ausführen (oder ohne `--ordner` direkt von der noch laufenden Seite). Das Skript sucht, benennt um und legt ab; neu bauen | Jens | offen, vor dem Livegang |
| T2 | Flache Cover in hoher Auflösung, Dateiname = ISBN (heute nur 3D-Mockups für ~37 Titel) | Chris | offen |
| T3 | Logo als SVG (oder Schriftname des Wortbilds) | Chris | offen |
| T4 | Korrekturen Bücherliste: 3 falsche Amazon-Links (Ziele finden, Glücklich denken, Chinesisch kochen), 4 B0-ASINs, Bandnummern Kuschelige Momente, „am/im Meer“, Mutmacherinnen SC/HC | Chris | offen |
| T5 | Datentabelle `buecher.csv` als Entwurf aus Liste, Website und Flyern | Claude | erledigt 15.10. (Feinschliff nach Livegang, A58) |
| T6 | Klappentexte kürzen und vereinheitlichen | Claude | erledigt 15.10. (A59) |
| T7 | Freigaben für Namen, Fotos, Zitate von Autor:innen | Chris | offen |
| T8 | Presse-Belege: WDR, RTL.de, Cashkurs erledigt (Logos und Angaben von buchbuddy.de, 15.10.). Offen: Daten zu RTL.de, Cashkurs, WDR 2 (F42), Bestseller-Datum (F41), Artikel zu Ausgeschieden, Die verlorenen Jahre, Finde dein Warum | Chris | teilweise |
| T9 | **Erledigt 15.10.:** Website liegt in `jcbooks/klhe-website`, Push funktioniert. Früher: Zugang BuchBuddy-Repo, Hosting und Deploy-Weg wie bei buchbuddy.de. Stand 15.10.: Mit dem verknüpften GitHub-Konto sind nur Repos von Buuk-Publishing und JCBOOKS sichtbar; für `BuchBuddy/buchbuddy-website` muss die Claude-GitHub-App in der Organisation BuchBuddy Zugriff auf das Repo bekommen | Chris/Jens | offen |
| T10 | Search Console prüfen: Hat der Hack Spam-Seiten in den Google-Index gebracht? Liste exportieren, die neue Seite antwortet darauf mit 410 | Jens | offen |
| T11 | Vor dem Löschen von WordPress: prüfen, ob Bestell- oder Kundendaten aufbewahrt werden müssen | Chris/Jens | offen |
| T12 | GetResponse: Inhalte sichern (F5), dann kündigen | Chris | offen |
| T15 | Bei IONOS prüfen, dass der Vertrag zur Auftragsverarbeitung abgeschlossen ist (der Datenschutz sagt das) | Jens | offen |
| T14 | Livegang nach `README.md`: Bonusdateien holen, bauen, `public/` hochladen, HTTPS und www prüfen, Stichproben der Weiterleitungen, Sitemap einreichen, WordPress löschen | Jens | offen |
| T13 | **Michael Jordan und Tierkinderhort erledigt (15.10.).** Fehlende Cover: saubere Tierkinderhort-Datei, Originale von Monsterparade und Ein etwas anderes Ausmalbuch, Michael Jordan; flach: Tag auf Tag, Geld sparen, Mein Geldbaum (Mutmachbücher erledigt) | Chris | offen |

## E. Protokoll

- 16.10.2026, ca. 10:30 Uhr: Pflichtexemplare DNB ergänzt (A74), Startseiten-Fehler behoben und Strukturprüfung eingebaut (A75). Frage F44 neu.
- 15.10.2026, ca. 21:10 Uhr: Coverwand auf der Startseite repariert (Lücken durch verzögert geladene Cover ohne feste Größe). Bestseller-Belege zu Nine to five eingebaut (A73), Frage F43 neu.
- 15.10.2026, ca. 21 Uhr: Presse-Feedback umgesetzt (A68–A72): Logos WDR, RTL, Cashkurs, Jolie; Bestseller-Beleg; vier neue Beiträge (25 statt 21); Pressekarten mit Seitenstapeln und 3D-Buch-Mockups auf Start, Presse, Buchseiten und Finanzreihe. Build, Linkprüfung und Weiterleitungstest ohne Fehler, Desktop und Mobil angesehen. Fragen F41, F42 neu.
- 15.10.2026, ca. 20 Uhr: Feedback umgesetzt (A63–A67): Börsenverein entfernt, Cover im Reihenbild Kuschelige Momente, Verlagskosten in der Preisleiste, Presseseite mit 21 Berichten, Cover Jordan und Tierkinderhort. Fragen F39, F40 offen.
- 15.10.2026, ca. 19 Uhr: Etappe 3 umgesetzt (C8, A57–A60). Website im Repo-Ordner gebaut und geprüft (64 Seiten, 222 Weiterleitungen, Linkprüfung ohne Fehler, Desktop- und Mobilansicht angesehen). Nach `jcbooks/klhe-website` gepusht (T9 erledigt). Fragen F32–F38 offen.
- 15.10.2026, ca. 18 Uhr: Richtung v5 freigegeben (A56). Programm, Buchseite und Bonusmaterial auf v5 umgestellt, Canvas neu geordnet (neun v5-Seiten, Archiv darunter). Ausblick Etappe 3 festgehalten (C7).
- 15.10.2026, ca. 17 Uhr: Feedback zu v4 (A49–A55). Alle Mutmach-Cover und zwölf A+-Grafiken aus Praxisbuch 1–7 verarbeitet. BuchBuddy-Gestaltung angesehen (Pastellflächen, runde Formen, kräftige Grotesk). Gestaltungsvorschau v5 „Transparentpapier“ mit sechs Seiten veröffentlicht. Frage F31 offen.
- 15.10.2026, ca. 16 Uhr: Feedback zu v3 (A45–A48). Neue Cover und A+-Grafiken verarbeitet (Golf, Tennis, Wilder Westen, Mitmachbücher, Bauernhof, Affe Loki, Einmal Himmel, Weniger ist auch gut genug, Mikroabenteuer Franken, Kuschelige Momente und Zahnarzt A+). Gestaltungsvorschau v4 mit neuem Ansatz veröffentlicht (Start, Verlag, Finanzreihe, Mutmachbücher, Kuschelige Momente). Fragen F24–F30 offen.
- 15.10.2026: Bestandsaufnahme erstellt (286 Adressen, 77 + 3 Titel, Shop, 44 Bonusseiten, Rechtstexte, Material).
- 15.10.2026, ca. 15 Uhr: Feedback zu v2 (A40–A44), neue Cover verarbeitet, Gestaltungsvorschau v3 veröffentlicht. Fragen F21–F23 offen.
- 15.10.2026, nachmittags: Feedback zu v1 (A34–A39). Projektordner `~/Projekte/klhe-website` angelegt. Gestaltungsvorschau v2 veröffentlicht (6 Seiten, neue Farben, Bilder, Reihen). Fragen F16–F20 offen.
- 15.10.2026: Gestaltungsvorschau v1 als Design-Canvas veröffentlicht (5 Seiten). Fragen F11–F15 offen.
- 15.10.2026, 12:48: Seitenplan freigegeben, Bonus-Lösung bestätigt, USt-IdNr., Telefon, Repo, Distributor, Social geklärt (A26–A33). Etappe 2 (Gestaltungsvorschau) gestartet; Repo-Zugriff wartet auf GitHub-Verknüpfung.
- 15.10.2026: Chris beantwortet die Fragen aus v1, formuliert das Ziel (Aushängeschild für BuchBuddy) und nennt den Hack als Anlass. Entscheidungen A1–A25 festgehalten. Seitenplan v1 erstellt. Bonus-Dateien vollständig erfasst (35 Dateien auf 42 Seiten).
