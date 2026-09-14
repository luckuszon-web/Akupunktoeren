import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _generate import page, icon

# ------------------------------------------------------------------- galleri
galleri_body = '''  <section class="section">
    <div class="container">
      <h2 style="text-align:center; margin-bottom:0.4em;">Indblik i klinikken</h2>
      <p style="text-align:center; max-width:640px; margin:0 auto 2.5rem;">Et par glimt fra Akupunkturklinik Charlotte Kuszon og de naturskønne omgivelser i Rungsted.</p>
      <div class="gallery-grid">
        <a href="../assets/images/hero.jpg" target="_blank" rel="noopener"><img src="../assets/images/hero.jpg" alt="Naturen omkring klinikken i Rungsted" loading="lazy"></a>
        <a href="../assets/images/traditions.png" target="_blank" rel="noopener"><img src="../assets/images/traditions.png" alt="Gåtur i skoven som en del af den holistiske behandling" loading="lazy"></a>
      </div>
    </div>
  </section>
'''
page("galleri", "Galleri", "Billeder fra Akupunkturklinik Charlotte Kuszon i Rungsted.", "", "Akupunktur Charlotte Kuszon", "Galleri", galleri_body)


# ---------------------------------------------------------------- referencer
referencer_body = f'''  <section class="section">
    <div class="container article" style="max-width:820px;">
      <h2>Hvorfor vælge Akupunktur Charlotte Kuszon?</h2>
      <p>Vi har endnu ikke offentliggjort skriftlige patientudtalelser her på siden, men her er, hvorfor patienter i Rungsted og omegn vælger klinikken:</p>
      <div class="stat-grid" style="grid-template-columns:repeat(3,1fr); margin-bottom:2.5rem;">
        <div class="stat-card">
          <div class="feature-icon">{icon("check")}</div>
          <h3>Siden 1998</h3>
          <p>Mangeårig erfaring med akupunktur og holistisk behandling.</p>
        </div>
        <div class="stat-card">
          <div class="feature-icon">{icon("check")}</div>
          <h3>RAB-godkendt</h3>
          <p>Registreret og godkendt via Danske Akupunktører.</p>
        </div>
        <div class="stat-card">
          <div class="feature-icon">{icon("check")}</div>
          <h3>Bred uddannelse</h3>
          <p>Løbende efteruddannelse gennem mere end 30 år.</p>
        </div>
      </div>
      <p>Har du selv haft en god oplevelse hos os, hører vi meget gerne fra dig – ring eller skriv, så kan din historie komme med her.</p>
      <div class="btn-row">
        <a class="btn btn-accent" href="../akupunktoeren-baggrund-og-uddannelse/">Læs mere om Charlotte</a>
        <a class="btn btn-cta" href="../kontakt/">Kontakt os</a>
      </div>
    </div>
  </section>
'''
page("referencer", "Referencer", "Hvorfor patienter vælger Akupunktur Charlotte Kuszon i Rungsted.", "", "Akupunktur Charlotte Kuszon", "Referencer", referencer_body)


# ------------------------------------------------------------------ reference
reference_body = '''  <section class="section">
    <div class="container status-page">
      <h2>Se vores referencer</h2>
      <p>Denne side er flyttet – find vores referencer og baggrund via linkene herunder.</p>
      <div class="btn-row" style="justify-content:center;">
        <a class="btn btn-accent" href="../referencer/">Referencer</a>
        <a class="btn btn-cta" href="../kontakt/">Kontakt os</a>
      </div>
    </div>
  </section>
'''
page("reference", "Reference", "Referencer og baggrund for Akupunktur Charlotte Kuszon i Rungsted.", "", "Akupunktur Charlotte Kuszon", "Reference", reference_body, include_cta_band=False)
