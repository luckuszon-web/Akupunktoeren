#!/usr/bin/env python3
"""Generator for the modern rebuild's subpages. Not shipped to production —
kept here only as the tool used to produce the static HTML files."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

SITE_URL = "https://akupunktoeren.com"

LOCAL_BUSINESS_SCHEMA = f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "MedicalClinic",
  "name": "Akupunktur Charlotte Kuszon",
  "image": "{SITE_URL}/assets/images/hero.jpg",
  "logo": "{SITE_URL}/assets/images/logo.png",
  "url": "{SITE_URL}/",
  "telephone": "+4531608880",
  "email": "ckuszon@akupunktoeren.com",
  "address": {{
    "@type": "PostalAddress",
    "streetAddress": "Pennehave 9",
    "postalCode": "2960",
    "addressLocality": "Rungsted Kyst",
    "addressCountry": "DK"
  }},
  "openingHoursSpecification": [
    {{
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Thursday"],
      "opens": "08:30",
      "closes": "17:45"
    }}
  ]
}}
</script>'''

ICONS = {
    "phone": '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>',
    "mail": '<path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/>',
    "map-pin": '<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>',
    "check": '<polyline points="20 6 9 17 4 12"/>',
    "chevron-down": '<polyline points="6 9 12 15 18 9"/>',
    "menu": '<line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/>',
    "close": '<line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>',
}

def icon(name, cls="icon", style=""):
    s = f' style="{style}"' if style else ""
    return f'<svg class="{cls}" viewBox="0 0 24 24"{s}>{ICONS[name]}</svg>'

NAV_ITEMS = [
    ("forside", "../index.html", "Forside"),
    ("akupunktoeren", "../akupunktoeren-baggrund-og-uddannelse/", "Akupunktøren"),
    ("priser", "../priser/", "Priser"),
]

BEHANDLINGER_COND = [
    ("smerter-og-spaendinger", "Smerter og spændinger"),
    ("hoved-og-nakke", "Hoved og nakke"),
    ("tinnitus", "Tinnitus"),
    ("hoefeber", "Høfeber"),
    ("idraets-skader", "Idrætsskader"),
    ("astma", "Astma"),
    ("ryg-og-bevaegeapparat", "Ryg og bevægeapparat"),
    ("hormonforstyrrelser", "Hormonforstyrrelser"),
]
BEHANDLINGER_OTHER = [
    ("posturologi", "Posturologi"),
    ("iris-analyse", "Iris analyse"),
    ("healing", "Healing"),
    ("fjernhealing", "Fjernhealing"),
    ("kursus-i-skovhealing-og-meditation", "Skovhealing og meditation"),
]
BEHANDLINGER_ALL = [s for s, _ in BEHANDLINGER_COND] + [s for s, _ in BEHANDLINGER_OTHER] + ["akupunktur"]


def header(current):
    def cur(slug):
        return " current" if slug == current else ""

    cond_items = "\n".join(
        f'                <li><a href="../{slug}/">{label}</a></li>'
        for slug, label in BEHANDLINGER_COND
    )
    other_items = "\n".join(
        f'                <li><a href="../{slug}/">{label}</a></li>'
        for slug, label in BEHANDLINGER_OTHER
    )
    behandlinger_class = "has-dropdown has-mega"
    if current in BEHANDLINGER_ALL:
        behandlinger_class += " current"

    return f'''<div class="header-overlay">
<div class="topbar">
  <div class="container">
    <a href="tel:+4531608880">
      {icon("phone")}
      31 60 88 80
    </a>
    <span class="topbar-address">
      {icon("map-pin")}
      Pennehave 9, 2960 Rungsted Kyst
    </span>
    <a href="mailto:ckuszon@akupunktoeren.com">
      {icon("mail")}
      ckuszon@akupunktoeren.com
    </a>
  </div>
</div>

<header class="site-header">
  <div class="container">
    <a class="logo" href="../index.html" aria-label="Akupunktur Charlotte Kuszon – forside">
      <img src="../assets/images/logo.png" alt="Akupunktur Charlotte Kuszon logo" width="64" height="64">
    </a>

    <button class="nav-toggle" id="navToggle" aria-expanded="false" aria-controls="siteNav" aria-label="Åbn menu">
      {icon("menu", cls="icon icon-menu", style="width:26px;height:26px")}
      {icon("close", cls="icon icon-close", style="width:26px;height:26px")}
    </button>

    <nav class="nav" id="siteNav">
      <ul class="nav-list">
        <li class="{'current' if current == 'forside' else ''}"><a href="../index.html">Forside</a></li>
        <li class="{behandlinger_class}">
          <a href="#">Behandlinger
            {icon("chevron-down", style="width:.7em;height:.7em")}
          </a>
          <div class="dropdown dropdown-mega">
            <div class="dropdown-col">
              <p class="dropdown-heading"><a href="../akupunktur/">Akupunktur for</a></p>
              <ul>
{cond_items}
              </ul>
            </div>
            <div class="dropdown-col">
              <p class="dropdown-heading">Andre behandlinger</p>
              <ul>
{other_items}
              </ul>
            </div>
          </div>
        </li>
        <li class="{'current' if current == 'akupunktoeren' else ''}"><a href="../akupunktoeren-baggrund-og-uddannelse/">Om Akupunktøren</a></li>
        <li class="{'current' if current == 'priser' else ''}"><a href="../priser/">Priser</a></li>
        <li class="has-dropdown">
          <a href="#">Apps
            {icon("chevron-down", style="width:.7em;height:.7em")}
          </a>
          <ul class="dropdown">
            <li><a href="https://myggeapp.dk/" target="_blank" rel="noopener">MyggeApp <span class="dropdown-note">Myggefri på én video</span></a></li>
            <li><a href="https://AllergiApp.dk/" target="_blank" rel="noopener">AllergiApp <span class="dropdown-note">Allergifri på én video</span></a></li>
          </ul>
        </li>
      </ul>
      <div class="nav-cta">
        <a class="btn btn-cta" href="../kontakt/">Kontakt</a>
      </div>
    </nav>
  </div>
</header>
</div>
'''


def footer(prefix="../"):
    return f'''<footer class="site-footer">
  <div class="container footer-grid">
    <div>
      <h4>Firmainformation</h4>
      <p>Akupunktur Charlotte Kuszon<br>Pennehave 9, 2960 Rungsted Kyst<br>CVR: 25513126</p>
    </div>
    <div>
      <h4>Kontakt os</h4>
      <ul>
        <li>
          {icon("phone")}
          <a href="tel:+4531608880">31 60 88 80</a>
        </li>
        <li>
          {icon("mail")}
          <a href="mailto:ckuszon@akupunktoeren.com">ckuszon@akupunktoeren.com</a>
        </li>
      </ul>
      <p>Kontakt mig for et tilbud.</p>
    </div>
    <div>
      <h4>Åbningstider</h4>
      <p>
        Mandag: 08:30 – 17:45<br>
        Tirsdag: 08:30 – 17:45<br>
        Onsdag: Efter særlig aftale<br>
        Torsdag: 08:30 – 17:45<br>
        Fredag: Efter særlig aftale<br>
        <strong>Telefontid</strong><br>
        Alle hverdage mellem 8 – 17
      </p>
    </div>
  </div>
  <div class="container footer-bottom">
    <p>&copy; 2026 Akupunktur Charlotte Kuszon</p>
    <a href="{prefix}privatlivspolitik/">Cookie- og privatlivspolitik</a>
  </div>
</footer>
'''

SCRIPT = '''<script>
(function () {
  var toggle = document.getElementById('navToggle');
  var nav = document.getElementById('siteNav');
  toggle.addEventListener('click', function () {
    var open = nav.classList.toggle('is-open');
    toggle.classList.toggle('is-open', open);
    toggle.setAttribute('aria-expanded', open);
    toggle.setAttribute('aria-label', open ? 'Luk menu' : 'Åbn menu');
  });
  document.querySelectorAll('.has-dropdown > a').forEach(function (link) {
    link.addEventListener('click', function (e) {
      if (window.innerWidth <= 960) {
        e.preventDefault();
        link.parentElement.classList.toggle('is-open');
      }
    });
  });
})();
</script>
'''

CTA_BAND = f'''  <section class="cta-band">
    <div class="container">
      <div>
        <h2>Kontakt</h2>
        <p>Bus linje 375 + 381 kører lige til døren.</p>
        <p>Jeg ligger ganske tæt på Rungsted station.</p>
        <ul class="check-list">
          <li>
            {icon("check")}
            Få svar på din henvendelse inden for 1-3 hverdage
          </li>
          <li>
            {icon("check")}
            Erfaren fagperson med mangeårig erfaring
          </li>
        </ul>
        <div class="btn-row">
          <a class="btn btn-cta" href="tel:+4531608880">+45 31 60 88 80</a>
          <a class="btn btn-outline" href="mailto:ckuszon@akupunktoeren.com">ckuszon@akupunktoeren.com</a>
        </div>
      </div>
      <div class="cta-card">
        <h3>Har du spørgsmål eller ønsker du et tilbud?</h3>
        <p>Kontakt mig allerede i dag for kompetent sparring og rådgivning ved din behandling.</p>
      </div>
    </div>
  </section>
'''


def page_banner(eyebrow, title, extra_contact=True):
    contact = ""
    if extra_contact:
        contact = f'''
        <div class="page-banner-contact">
          <a href="tel:+4531608880">{icon("phone")} 31 60 88 80</a>
          <a href="mailto:ckuszon@akupunktoeren.com">{icon("mail")} ckuszon@akupunktoeren.com</a>
        </div>'''
    return f'''  <section class="hero page-banner">
    <div class="container hero-content">
      <p class="hero-eyebrow">{eyebrow}</p>
      <h1>{title}</h1>{contact}
    </div>
  </section>
'''


def page(slug, title, description, current, banner_eyebrow, banner_title, body, include_cta_band=True, noindex=False):
    cta = CTA_BAND if include_cta_band else ""
    full_title = f"{title} | Akupunktur Charlotte Kuszon"
    canonical = f"{SITE_URL}/{slug}/"
    robots_tag = '<meta name="robots" content="noindex, follow">\n' if noindex else ""
    html = f'''<!DOCTYPE html>
<html lang="da">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{description}">
{robots_tag}<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:locale" content="da_DK">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE_URL}/assets/images/hero.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{full_title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{SITE_URL}/assets/images/hero.jpg">
<link rel="icon" href="../assets/images/favicon.png">
<link rel="stylesheet" href="../assets/css/style.css?v=13">
{LOCAL_BUSINESS_SCHEMA}
</head>
<body>
<a class="skip-link" href="#main">Spring til indhold</a>

{header(current)}
<main id="main">

{page_banner(banner_eyebrow, banner_title)}
{body}
{cta}
</main>

{footer()}
{SCRIPT}
</body>
</html>
'''
    out_dir = os.path.join(ROOT, slug)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", slug)
