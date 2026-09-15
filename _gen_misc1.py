import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _generate import page, icon

# ------------------------------------------------------------ book-akupunktur
book_body = '''  <section class="section">
    <div class="container article">
      <h2>Akupunktur – det handler om balance</h2>
      <h3>Hvad er akupunktur?</h3>
      <p>Akupunktur virker på den energi, som findes i kroppen. Overalt på din krop er der punkter, som man påvirker med nåle, med varme eller tryk. Hvert enkelt punkt har en specifik virkning, og flere punkter kan kombineres for at opnå en særlig effekt.</p>
      <p>Akupunktøren er uddannet til at kende punkternes virkninger. Det kræver viden om menneskelegemet, dets organer og funktioner i samme omfang som for alle andre behandlere i sundhedssektoren. Klinikken benytter udelukkende sterile engangsnåle.</p>

      <h2>Hemmeligheden er i helheden</h2>
      <p>"Et par nåle, og smerten var væk" – sådan er der mange, som har oplevet akupunktur. Det er dejlig lindring her og nu, men den primære målsætning med akupunktur er at forebygge og fjerne årsagerne til sygdommene og lidelserne. Akupunktøren arbejder helhedsorienteret ud fra en opfattelse af balance mellem krop og sjæl, og den energi som holder sammen på det hele. Derfor inddrager akupunktørens diagnose alle forhold – ikke blot det, der umiddelbart har symptomet at gøre.</p>

      <h3>Tradition og forskning</h3>
      <p>Akupunktur er en del af traditionel kinesisk medicin, et system, som bygger på erfaringer gjort gennem tusinder af år. De grundlæggende antagelser om kroppens energi, om balance og ubalance, har vist deres blivende værdi og gyldighed, men akupunkturvidenskaben står ikke stille. Den udvikler sig hele tiden på baggrund af nye forsøg og iagttagelser og med inddragelse af moderne teknikker som f.eks. elakupunktur og laser til at påvirke akupunkturpunkterne. Også den vestlige forskning har bidraget væsentligt til at udvikle akupunkturens teori og praksis gennem forskning i neurologi og neurofysiologi.</p>
      <p>Akupunkturklinikken bruger såvel de traditionelle kinesiske som vestlige videnskabeligt udviklede akupunkturmetoder og følger løbende med i udviklingen af terapiformerne.</p>

      <h2>Bestil tid til akupunktur i Rungsted</h2>
      <p>Hvis du er interesseret i at bestille tid til akupunktur i Rungsted, eller vil høre mere om akupunktur som behandlingsform, så er du meget velkommen til at kontakte mig for en uforpligtende samtale.</p>
      <p>Har du yderligere spørgsmål, er du velkommen til at skrive en mail på <a href="mailto:ckuszon@akupunktoeren.com" style="color:var(--color-accent)">ckuszon@akupunktoeren.com</a> eller ringe til mig på telefon 31 60 88 80.</p>
      <div class="btn-row article-cta">
        <a class="btn btn-accent" href="../priser/">Se priser</a>
        <a class="btn btn-cta" href="../kontakt/">Kontakt mig i dag</a>
      </div>
    </div>
  </section>
'''
page(
    "book-akupunktur",
    "Book akupunktur",
    "Sådan foregår akupunktur hos Akupunktur Charlotte Kuszon i Rungsted – balance, helhed og en tradition der bygger på tusindvis af års erfaring.",
    "akupunktur",
    "Akupunktur Charlotte Kuszon",
    "Book akupunktur",
    book_body,
)

# ------------------------------------------------------------------- ydelse
ydelse_body = f'''  <section class="section">
    <div class="container status-page">
      <div class="status-icon">{icon("phone")}</div>
      <h2>Denne side er flyttet</h2>
      <p>Du kan finde mine behandlinger og priser via menuen, eller gå direkte til en af siderne herunder.</p>
      <div class="btn-row" style="justify-content:center;">
        <a class="btn btn-accent" href="../akupunktur/">Se behandlinger</a>
        <a class="btn btn-cta" href="../priser/">Se priser</a>
      </div>
    </div>
  </section>
'''
page(
    "ydelse",
    "Ydelser",
    "Se mine behandlinger og priser hos Akupunktur Charlotte Kuszon i Rungsted.",
    "priser",
    "Akupunktur Charlotte Kuszon",
    "Ydelser",
    ydelse_body,
    include_cta_band=False,
    noindex=True,
)

# ---------------------------------------------------------- tak-for-din-henv.
tak_body = f'''  <section class="section">
    <div class="container status-page">
      <div class="status-icon">{icon("check")}</div>
      <h2>Tak for din henvendelse</h2>
      <p>Jeg kontakter dig hurtigst muligt. Du kan også gå tilbage til forsiden, hvis du ønsker.</p>
      <p>Hvis du ønsker at bestille tid til en akupunkturbehandling, er du velkommen til at skrive en mail på <a href="mailto:ckuszon@akupunktoeren.com" style="color:var(--color-accent)">ckuszon@akupunktoeren.com</a> eller ringe til mig på telefon 31 60 88 80.</p>
      <p>Du er også meget velkommen til at kontakte mig for en uforpligtende samtale, hvis du vil høre mere om akupunktur som behandlingsform.</p>
      <div class="btn-row" style="justify-content:center;">
        <a class="btn btn-accent" href="../index.html">Til forsiden</a>
        <a class="btn btn-cta" href="tel:+4531608880">Ring 31 60 88 80</a>
      </div>
    </div>
  </section>
'''
page(
    "tak-for-din-henvendelse",
    "Tak for din henvendelse",
    "Tak for din henvendelse til Akupunktur Charlotte Kuszon. Jeg vender tilbage hurtigst muligt.",
    "",
    "Akupunktur Charlotte Kuszon",
    "Tak for din henvendelse",
    tak_body,
    include_cta_band=False,
    noindex=True,
)
