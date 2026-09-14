# Akupunktøren.com – statisk kopi

Dette repo indeholder en statisk HTML/CSS/JS-kopi af [akupunktoeren.com](https://akupunktoeren.com/), hentet direkte fra det nuværende WordPress-site som forberedelse til flytning til ny hosting.

## Hvad er med

Alle sider fra sitemap er hentet, inkl. billeder, CSS og JS:

- Forside (`index.html`)
- `akupunktur/` + de 8 underemner (`smerter-og-spaendinger`, `hoved-og-nakke`, `tinnitus`, `hoefeber`, `idraets-skader`, `astma`, `ryg-og-bevaegeapparat`, `hormonforstyrrelser`)
- `posturologi/`, `iris-analyse/`, `healing/`, `fjernhealing/`, `kursus-i-skovhealing-og-meditation/`
- `akupunktoeren-baggrund-og-uddannelse/`, `priser/`, `kontakt/`
- `ydelse/`, `referencer/`, `reference/`, `galleri/`, `tak-for-din-henvendelse/`, `book-akupunktur/`
- Alle assets under `wp-content/` og `wp-includes/`

Interne links mellem siderne er tjekket og peger korrekt på de lokale filer (ingen døde links).

## Uafhængig af det originale site

Alle billeder, CSS og JS-filer (inkl. lazy-loadede billeder, cookie-samtykke-script og andre "deferred" scripts) er hentet ned lokalt og alle links er omskrevet fra `https://akupunktoeren.com/...` til relative stier. Sitet loader altså **ikke** længere nogen ressourcer fra det oprindelige WordPress-site — det kan køre fuldstændig uafhængigt, også efter det gamle site lukkes ned. Rene analytics-/telemetri-scripts (WP Statistics) og døde metadata-links (RSS-feed, oEmbed, WP REST-discovery, RSD/xmlrpc) er fjernet helt, da de udelukkende pegede tilbage på den gamle WordPress-backend.

## Sådan ses siden lokalt

```bash
python3 -m http.server 8000
```

Åbn derefter `http://localhost:8000/`.

## Vigtige begrænsninger (ingen WordPress-backend)

Da dette er en **statisk** kopi uden WordPress bagved, virker følgende ting fra det oprindelige site stadig **ikke** automatisk, fordi de kræver en server bagved:

1. **Booking-knapper** der linker videre til eksterne booking-/kalendersystemer virker fortsat, hvis de peger på en ekstern tjeneste – men eventuelle indlejrede WordPress-widgets med serverkald vil ikke virke.
2. **WP REST API-referencer** (`wp-json/...` i nogle scripts' konfiguration) er ikke fjernet, men bruges ikke ved almindeligt sidebesøg — kun hvis en specifik plugin-funktion aktivt kalder dem.

## Kontaktformular (Formspree)

Kontaktformularen på `/kontakt/` er lavet om fra Forminator (som krævede en AJAX-hentning fra WordPress for overhovedet at vise felterne) til en almindelig statisk HTML-formular, der sender direkte til Formspree:

- Endpoint: `https://formspree.io/f/xwlkgnke`
- Felter: Navn, Tlf. nr. (valgfrit), Email, Besked — samme felter som den oprindelige formular.
- Indsendelse sker via JavaScript (`fetch`) uden sidereload, og ved succes sendes brugeren videre til den eksisterende `/tak-for-din-henvendelse/`-side. Ved fejl vises en fejlbesked med telefonnummer som alternativ.
- Der er tilføjet et skjult "honeypot"-felt (`_gotcha`) som simpel spam-beskyttelse.

Formspree-kontoen skal selv konfigureres til at sende notifikationer til den rigtige emailadresse (ckuszon@akupunktoeren.com) under formularens indstillinger på formspree.io.

## Næste skridt

- Verificér SEO-metadata (canonical-tags peger stadig på `akupunktoeren.com`, hvilket er korrekt, så længe det nye site også ligger på samme domæne).
- Sæt op med rigtig hosting (f.eks. Netlify/Vercel/GitHub Pages) og peg domænet dertil.
- Test kontaktformularen efter deployment (Formspree kræver typisk at man bekræfter den første indsendelse via email, før formularen er "aktiveret").
