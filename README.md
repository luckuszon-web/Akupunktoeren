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

## Sådan ses siden lokalt

```bash
python3 -m http.server 8000
```

Åbn derefter `http://localhost:8000/`.

## Vigtige begrænsninger (ingen WordPress-backend)

Da dette er en **statisk** kopi uden WordPress bagved, virker følgende ting fra det oprindelige site **ikke** automatisk:

1. **Kontaktformularen** (`kontakt/index.html`) bruger Forminator-pluginnet, som sender data til WordPress' `admin-ajax.php`. Den skal erstattes med en statisk formular-løsning (f.eks. Formspree, Netlify Forms, eller en simpel serverless-funktion), før siden går i luften.
2. **Booking-knapper** der linker videre til eksterne booking-/kalendersystemer virker fortsat, hvis de peger på en ekstern tjeneste – men eventuelle indlejrede WordPress-widgets med serverkald vil ikke virke.
3. **Søgefunktion og evt. cache-plugins** (Elementor/Forminator/GeneratePress-cache-filer under `wp-content/cache/`) er kun de statiske output-filer – ikke den bagvedliggende funktionalitet.

## Næste skridt

- Vælg en løsning til kontaktformularen og opdater `kontakt/index.html` (og evt. `book-akupunktur/index.html`).
- Verificér SEO-metadata (canonical-tags peger stadig på `akupunktoeren.com`, hvilket er korrekt, så længe det nye site også ligger på samme domæne).
- Sæt op med rigtig hosting (f.eks. Netlify/Vercel/GitHub Pages) og peg domænet dertil.
