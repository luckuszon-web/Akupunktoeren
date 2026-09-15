#!/usr/bin/env python3
"""Generates sitemap.xml. Not shipped as a build step — run manually
(`python3 _gen_sitemap.py`) whenever a page is added, removed, or its
noindex status changes. Excludes pages marked noindex in their own
_gen_*.py page() call (thin/utility pages: ydelse, reference,
tak-for-din-henvendelse)."""
import os
from _generate import SITE_URL, ROOT

# Keep in sync with the noindex=True pages in _gen_misc1.py / _gen_misc2.py.
SLUGS = [
    "",  # homepage
    "akupunktoeren-baggrund-og-uddannelse",
    "akupunktur",
    "astma",
    "book-akupunktur",
    "fjernhealing",
    "galleri",
    "healing",
    "hoefeber",
    "hormonforstyrrelser",
    "hoved-og-nakke",
    "idraets-skader",
    "iris-analyse",
    "kontakt",
    "kursus-i-skovhealing-og-meditation",
    "posturologi",
    "priser",
    "referencer",
    "ryg-og-bevaegeapparat",
    "smerter-og-spaendinger",
    "tinnitus",
]

urls = "\n".join(
    f"  <url><loc>{SITE_URL}/{slug}/</loc></url>" if slug else f"  <url><loc>{SITE_URL}/</loc></url>"
    for slug in SLUGS
)

xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>
'''

with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write(xml)
print(f"wrote sitemap.xml with {len(SLUGS)} URLs")
