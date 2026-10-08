import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _generate import page, SITE_URL

# Each entry: (slug, seo_title, h1_title, description, date_iso "YYYY-MM-DD",
# date_display "8. oktober 2026", excerpt, body_html)
# - seo_title: goes in <title>/og:title (site name is appended automatically)
# - h1_title: the on-page heading and blog-card heading
# Add a new post by appending a tuple here, then run `python3 _gen_blog.py`
# and add the new slug to SLUGS in _gen_sitemap.py.
BLOG_POSTS = [
    (
        "hvad-koster-akupunktur",
        "Hvad koster akupunktur? Priser og tilskud",
        "Hvad koster akupunktur, og kan du få tilskud?",
        "Se hvad akupunktur koster i Rungsted/Hørsholm, hvad første behandling indeholder, og hvordan du søger tilskud hos din sundhedsforsikring.",
        "2026-10-08",
        "8. oktober 2026",
        "Se hvad akupunktur koster i Rungsted/Hørsholm, hvad første behandling indeholder, og hvordan du søger tilskud hos din sundhedsforsikring.",
        '''      <p>En akupunkturbehandling hos mig i Rungsted/Hørsholm koster 700 kr. første gang og 600 kr. de efterfølgende gange. Her kan du se, hvad prisen dækker, og hvordan du undersøger, om din sundhedsforsikring giver tilskud.</p>

      <h3>Priser på akupunktur</h3>
      <ul class="price-list">
        <li><span class="price-name">Første akupunkturbehandling</span><span class="price-fill"></span><span class="price-amount">700 kr.</span></li>
        <li><span class="price-name">Efterfølgende akupunkturbehandling</span><span class="price-fill"></span><span class="price-amount">600 kr.</span></li>
      </ul>
      <p>Du kan se priserne på alle mine behandlinger på <a href="../../priser/">prissiden</a>.</p>

      <h3>Det får du med i første behandling</h3>
      <p>Første behandling er mere end selve nålene. Jeg begynder altid med at danne mig et samlet billede af dig og din krop, og derfor er disse to undersøgelser inkluderet i prisen:</p>
      <ul class="plain-list">
        <li>Iris aflæsning</li>
        <li>Posturologiundersøgelse</li>
      </ul>
      <p>Det koster heller ikke ekstra, hvis jeg undervejs vurderer, at cupping eller laser er det rette for dig. Jeg laver en individuel vurdering hver gang og vælger behandlingen ud fra den.</p>

      <h3>Hvor mange behandlinger skal du regne med?</h3>
      <p>Det afhænger af, hvad du kommer med, og hvor længe du har haft det. Ved første besøg taler vi om, hvad du kan forvente, så du kender det sandsynlige forløb og den samlede pris, før du beslutter dig.</p>

      <h3>Kan du få tilskud til akupunktur?</h3>
      <p>Ja, mange kan. Flere sundhedsforsikringer giver tilskud til akupunktur, blandt andet Sygeforsikringen "danmark", når behandlingen udføres af en RAB-registreret akupunktør.</p>
      <p>Jeg er RAB-registreret gennem Danske Akupunktører, så mine behandlinger opfylder det krav. Sådan gør du:</p>
      <ol class="article-steps">
        <li>Kontakt din sundhedsforsikring, og spørg, om din ordning dækker akupunktur.</li>
        <li>Spørg, hvor meget de dækker pr. behandling, og om der er et loft pr. år.</li>
        <li>Bestil tid hos mig, og gem din kvittering til forsikringen.</li>
      </ol>
      <p>Du skal selv henvende dig til forsikringen. Beløb og vilkår er forskellige fra ordning til ordning, så det er dem, der kan give dig det præcise svar.</p>

      <h3>Bestil tid i Rungsted/Hørsholm</h3>
      <p>Klinikken ligger på Pennehave 9 i Rungsted Kyst, tæt på Rungsted Station, og bus 375 og 381 kører lige til døren.</p>
      <p>Ring eller skriv på 31 60 88 80, eller send en mail til <a href="mailto:ckuszon@akupunktoeren.com">ckuszon@akupunktoeren.com</a>. Du er også velkommen til at ringe først for en uforpligtende samtale om, hvorvidt <a href="../../akupunktur/">akupunktur</a> er noget for dig.</p>
''',
    ),
]


def article_schema(headline, description, date_iso, slug):
    url = f"{SITE_URL}/blog/{slug}/"
    return f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "{headline}",
  "description": "{description}",
  "datePublished": "{date_iso}",
  "dateModified": "{date_iso}",
  "author": {{
    "@type": "Person",
    "name": "Charlotte Kuszon"
  }},
  "publisher": {{
    "@type": "Organization",
    "name": "Akupunktur Charlotte Kuszon",
    "logo": {{
      "@type": "ImageObject",
      "url": "{SITE_URL}/assets/images/logo.png"
    }}
  }},
  "mainEntityOfPage": {{
    "@type": "WebPage",
    "@id": "{url}"
  }}
}}
</script>'''


def generate_post(slug, seo_title, h1_title, description, date_iso, date_display, body_html):
    body = f'''  <section class="section">
    <div class="container article">
{body_html}
      <p><a href="../" style="color:var(--color-accent)">&larr; Tilbage til bloggen</a></p>
    </div>
  </section>
'''
    page(
        f"blog/{slug}",
        seo_title,
        description,
        "blog",
        date_display,
        h1_title,
        body,
        og_type="article",
        extra_head=article_schema(h1_title, description, date_iso, slug),
        prefix="../../",
    )


for slug, seo_title, h1_title, description, date_iso, date_display, excerpt, body_html in BLOG_POSTS:
    generate_post(slug, seo_title, h1_title, description, date_iso, date_display, body_html)


# ---------------------------------------------------------------- blog index
if BLOG_POSTS:
    posts_sorted = sorted(BLOG_POSTS, key=lambda p: p[4], reverse=True)
    cards = "\n".join(
        f'''        <div class="blog-card">
          <p class="blog-card-date">{date_display}</p>
          <h3><a href="{slug}/">{h1_title}</a></h3>
          <p>{excerpt}</p>
          <a class="eyebrow-link" href="{slug}/">Læs mere &rarr;</a>
        </div>'''
        for slug, seo_title, h1_title, description, date_iso, date_display, excerpt, body_html in posts_sorted
    )
    blog_index_body = f'''  <section class="section">
    <div class="container">
      <div class="blog-list">
{cards}
      </div>
    </div>
  </section>
'''
else:
    blog_index_body = '''  <section class="section">
    <div class="container" style="max-width:640px; text-align:center;">
      <p>Det første blogindlæg er på vej. Kom snart tilbage for gode råd om akupunktur, posturologi og holistisk behandling.</p>
    </div>
  </section>
'''

page(
    "blog",
    "Blog",
    "Artikler om akupunktur, posturologi og holistisk behandling fra Akupunktur Charlotte Kuszon i Rungsted/Hørsholm.",
    "blog",
    "Akupunktur Charlotte Kuszon",
    "Blog",
    blog_index_body,
)
