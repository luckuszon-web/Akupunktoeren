import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _generate import page, SITE_URL

# Each entry: (slug, title, description, date_iso "YYYY-MM-DD", date_display "8. oktober 2026", excerpt, body_html)
# Add a new post by appending a tuple here, then run `python3 _gen_blog.py`
# and add the new slug to SLUGS in _gen_sitemap.py.
BLOG_POSTS = [
]


def article_schema(title, description, date_iso, slug):
    url = f"{SITE_URL}/blog/{slug}/"
    return f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "{title}",
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


def generate_post(slug, title, description, date_iso, date_display, body_html):
    body = f'''  <section class="section">
    <div class="container article">
{body_html}
      <p><a href="../" style="color:var(--color-accent)">&larr; Tilbage til bloggen</a></p>
    </div>
  </section>
'''
    page(
        f"blog/{slug}",
        title,
        description,
        "blog",
        date_display,
        title,
        body,
        og_type="article",
        extra_head=article_schema(title, description, date_iso, slug),
    )


for slug, title, description, date_iso, date_display, excerpt, body_html in BLOG_POSTS:
    generate_post(slug, title, description, date_iso, date_display, body_html)


# ---------------------------------------------------------------- blog index
if BLOG_POSTS:
    posts_sorted = sorted(BLOG_POSTS, key=lambda p: p[3], reverse=True)
    cards = "\n".join(
        f'''        <div class="blog-card">
          <p class="blog-card-date">{date_display}</p>
          <h3><a href="{slug}/">{title}</a></h3>
          <p>{excerpt}</p>
          <a class="eyebrow-link" href="{slug}/">Læs mere &rarr;</a>
        </div>'''
        for slug, title, description, date_iso, date_display, excerpt, body_html in posts_sorted
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
