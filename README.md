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

## Cookie- og privatlivspolitik

`/privatlivspolitik/` (genereret af `_gen_privatlivspolitik.py`) beskriver, hvilke oplysninger der indsamles via kontaktformularen, at Formspree er databehandler, og hvilke cookies der bruges. Der er et link til siden nederst i footeren på alle sider (`footer()` i `_generate.py`).

En cookie-boks (`cookie_banner()` i `_generate.py`, CSS-klasse `.cookie-banner`) vises nederst på skærmen ved første besøg, med en kort forklaring og to knapper: "Kun nødvendige" og "Accepter alle". Valget gemmes i `localStorage` (nøgle `cookie-consent`, værdi `accepted`/`rejected`), så boksen ikke vises igen i samme browser.

- **Nødvendige cookies** (Formsprees egne, til kontaktformularen/spam-beskyttelse) sættes altid — de kræver ikke samtykke efter cookiebekendtgørelsen.
- **Google Ads** (konverteringssporing, annonce-id `AW-1065423115`) indlæses *først*, når brugeren trykker "Accepter alle" — scriptet injiceres dynamisk via JS (`loadGoogleAds()` i `SCRIPT`-blokken i `_generate.py`) og ligger ikke som et statisk `<script src>` i `<head>`, netop for at undgå at sætte markedsføringscookies, før der er givet aktivt samtykke. Vælger brugeren "Kun nødvendige", indlæses Google Ads slet ikke.

Hvis der tilføjes flere ikke-nødvendige cookies/scripts (analytics, andre annoncenetværk osv.), skal de hægtes på samme `loadGoogleAds()`-mønster (kun indlæst efter accept) og beskrives i `/privatlivspolitik/`.

## SEO

- `robots.txt` og `sitemap.xml` ligger i rodmappen. Kør `python3 _gen_sitemap.py` for at genskabe sitemap.xml, hvis en side tilføjes/fjernes eller dens noindex-status ændres (listen over sider holdes manuelt i toppen af scriptet).
- Alle sider har unik `<title>`, meta-description, canonical-tag samt Open Graph- og Twitter-card-tags (deling på sociale medier).
- Strukturerede data (JSON-LD, `MedicalClinic`) er indsat på alle sider med navn, adresse, telefon og åbningstider.
- `ydelse/`, `reference/` og `tak-for-din-henvendelse/` har `<meta name="robots" content="noindex, follow">`, da de er tynde omdirigerings-/kvitteringssider uden selvstændigt indhold at rangere på.
- Alt ovenstående forudsætter, at sitet i sidste ende ligger på `https://akupunktoeren.com/` — hvis domænet ændres, skal `SITE_URL` i `_generate.py` samt URL'erne i `index.html`, `robots.txt` og `_gen_sitemap.py` opdateres tilsvarende.

## Sider uden originalt indhold

Tre sider (`ydelse/`, `referencer/`, `reference/`, `galleri/`) havde intet reelt indhold i den oprindelige WordPress-side (kun tomme skabeloner eller generisk demotekst). De er erstattet med korte, ærlige sider i stedet for opfundet indhold:

- `galleri/` viser to rigtige billeder, der allerede bruges andre steder på sitet.
- `referencer/` fremhæver faktuelle points (siden 1998, RAB-godkendt, uddannelse) i stedet for patientudtalelser, da der ikke findes nogen offentliggjorte.
- `ydelse/` og `reference/` er korte sider, der linker videre til de rigtige sider (behandlinger, priser, referencer).

## Næste skridt

- Sæt rigtig hosting op (Netlify/Vercel/GitHub Pages) og peg domænet `akupunktoeren.com` dertil.
- Test kontaktformularen efter deployment.
