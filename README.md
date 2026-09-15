# Akupunktøren.com – moderne statisk site

Dette repo indeholder den officielle hjemmeside for Akupunktur Charlotte Kuszon: ren, håndskrevet HTML/CSS/JS uden nogen afhængighed af WordPress, Elementor eller andre plugins. Ingen build-proces — det er almindelige statiske filer, der kan hostes hvor som helst (GitHub Pages, Netlify, Vercel, et almindeligt webhotel osv.).

## Struktur

- `index.html` — forsiden
- Én mappe pr. underside, f.eks. `akupunktur/`, `priser/`, `kontakt/` osv. — alle indeholder en `index.html`
- `assets/css/style.css` — al styling (ingen andre CSS-filer)
- `assets/fonts/` — selv-hostet Inter-skrifttype
- `assets/images/` — alle billeder sitet bruger
- `_generate.py` + `_gen_*.py` — Python-scripts brugt til at generere undersidernes HTML ud fra fælles header/footer-skabeloner. De er ikke en del af selve hjemmesiden (ingen side linker til dem), men er nyttigt værktøj, hvis en side skal opdateres eller en ny side skal tilføjes i samme stil. Kør fx `python3 _gen_priser.py` for at genskabe `priser/index.html` efter en ændring i scriptet.

## Design

- Farver: oliven-grøn (`#7a8033`), gul/amber (`#f4b637`), mørk (`#222222`) — samme branding som hidtil.
- Ikoner er inline SVG (Feather Icons, MIT-licens) — ingen ikon-font-afhængighed.
- Billeder bruger native `loading="lazy"` — intet JavaScript-bibliotek til lazy-loading.
- Header er gennemsigtig og ligger ovenpå hero-billedet på hver side; bliver til en almindelig hvid bjælke på mobil, når menuen er åben.

## Sådan ses siden lokalt

```bash
python3 -m http.server 8000
```

Åbn derefter `http://localhost:8000/`.

## Kontaktformular (Formspree)

Kontaktformularen på `/kontakt/` sender direkte til Formspree — ingen backend nødvendig:

- Endpoint: `https://formspree.io/f/xwlkgnke`
- Felter: Navn, Tlf. nr. (valgfrit), Email, Besked.
- Indsendelse sker via JavaScript (`fetch`) uden sidereload. Ved succes sendes brugeren videre til `/tak-for-din-henvendelse/`. Ved fejl vises en fejlbesked med telefonnummer som alternativ.
- Et skjult honeypot-felt (`_gotcha`) beskytter mod simpel spam.

Formspree-kontoen skal selv konfigureres til at sende notifikationer til ckuszon@akupunktoeren.com under formularens indstillinger på formspree.io. Formspree kræver typisk, at den første rigtige indsendelse bekræftes via email, før formularen er fuldt aktiveret.

## Sider uden originalt indhold

Tre sider (`ydelse/`, `referencer/`, `reference/`, `galleri/`) havde intet reelt indhold i den oprindelige WordPress-side (kun tomme skabeloner eller generisk demotekst). De er erstattet med korte, ærlige sider i stedet for opfundet indhold:

- `galleri/` viser to rigtige billeder, der allerede bruges andre steder på sitet.
- `referencer/` fremhæver faktuelle points (siden 1998, RAB-godkendt, uddannelse) i stedet for patientudtalelser, da der ikke findes nogen offentliggjorte.
- `ydelse/` og `reference/` er korte sider, der linker videre til de rigtige sider (behandlinger, priser, referencer).

## Næste skridt

- Sæt rigtig hosting op (Netlify/Vercel/GitHub Pages) og peg domænet `akupunktoeren.com` dertil.
- Test kontaktformularen efter deployment.
