import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _generate import page

def price_item(name, price):
    return f'''      <li><span class="price-name">{name}</span><span class="price-fill"></span><span class="price-amount">{price}</span></li>'''

col1 = [
    ("Akupunkturbehandling", [("Første akupunktur behandling", "700 kr"), ("Efterfølgende akupunkturbehandling", "600 kr")]),
    ("Myggebehandling med akupunktur", [("Første Myggebehandling", "700 kr"), ("Efterfølgende Myggebehandling", "600 kr")]),
    ("Cupping", [("Første Cupping behandling", "700 kr"), ("Efterfølgende Cupping behandling", "600 kr")]),
    ("Zoneterapi baby med Kolik", [("Første Baby Zoneterapi behandling", "700 kr"), ("Efterfølgende behandling", "650 kr")]),
    ("Posturologi", [("Første Posturologi", "700 kr"), ("Efterfølgende Posturologi", "600 kr")]),
]
col2 = [
    ("Iris aflæsning", [("Iris aflæsning", "600 kr")]),
    ("TFT – Tankefeltterapi", [("TFT - Tankefeltterapi · 30 min - 120 min", "888 kr")]),
    ("Healing i klinik", [("Healing i klinik", "700 kr"), ("Efterfølgende healing session", "600 kr")]),
    ("Fjernhealing", [("Fjernhealing", "500 kr")]),
    ("Skovhealing og meditation", [("Skovhealing og meditation", "1000 kr")]),
]

def render_col(groups):
    out = []
    for heading, items in groups:
        out.append(f'    <div class="price-group">\n      <h3>{heading}</h3>\n      <ul class="price-list">')
        out.extend(price_item(n, p) for n, p in items)
        out.append('      </ul>\n    </div>')
    return "\n".join(out)

body = f'''  <section class="section">
    <div class="container">
      <h2 style="margin-bottom:2rem;">Se vores priser</h2>
      <div class="price-groups">
        <div>
{render_col(col1)}
        </div>
        <div>
{render_col(col2)}
          <div class="btn-row">
            <a class="btn btn-cta" href="../kontakt/">Kontakt os i dag</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section about-clinic">
    <div class="container article-grid">
      <div>
        <h2>Det koster ikke ekstra</h2>
        <p>Det koster ikke ekstra, når du booker din første tid til akupunkturbehandling. Akupunkturbehandlingen er nemlig altid inkluderet iris aflæsning samt posturologiundersøgelse.</p>
        <p>Det samme gælder, hvis du bestiller tid til iris aflæsning eller posturologibehandling. Det koster heller ikke ekstra, hvis jeg under din behandling vælger at bruge cupping, laser eller zoneterapi. Jeg laver altid en individuel vurdering og finder derefter den mest egnede behandlingsmetode til dig.</p>
        <h3>Tilskud til akupunktur</h3>
        <p>Vidste du, at du kan søge om tilskud til akupunktur i akupunkturklinikken, hvis du er medlem af en sundhedsforsikring? Det gælder fx også, hvis du er medlem af "danmark" Sygeforsikring, som giver tilskud til behandling udført af RAB-registrerede akupunktører. Du skal selv rette henvendelse til din sundhedsforsikring og høre, om du har mulighed for at få tilskud. Det kan du, fordi jeg er RAB-registreret og godkendt inden for akupunktur.</p>
      </div>
      <div>
        <h3>RAB Godkendt</h3>
        <p>"Registreret Alternativ Behandler, RAB". Jeg er RAB-registreret og godkendt. Når du som behandler er RAB-registreret, betyder det, at man er medlem af en organisation – hos mig Danske Akupunktører – der udelukkende består af registreringsansvarlige brancheforeninger, godkendte af Sundhedsstyrelsen.</p>
        <h3>Danske Akupunktører</h3>
        <p>Akupunktur har vundet stort indpas de seneste år, og ikke uden grund. Hvem bør du konsultere, når du ønsker at få foretaget en akupunkturbehandling? Naturligvis den med størst viden inden for sygdomsbehandling med akupunktur. Alle medlemmer af Danske Akupunktører har gennemgået flerårige uddannelser i akupunktur og har nøje kendskab til kroppens fysik og sygdomme på samme vilkår som det øvrige sundhedssystem.</p>
        <p>Charlotte Kuszon videreuddanner sig løbende og er en af Danmarks mest uddannede inden for akupunktur. Vælg en akupunktør, som er medlem af Danske Akupunktører, så du sikrer dig, at de faglige kvalifikationer er i orden.</p>
      </div>
    </div>
  </section>
'''

page(
    "priser",
    "Priser",
    "Se priser på akupunktur, posturologi, iris aflæsning, healing, fjernhealing og skovhealing hos Akupunktur Charlotte Kuszon.",
    "priser",
    "Akupunktur Charlotte Kuszon",
    "Priser",
    body,
)
