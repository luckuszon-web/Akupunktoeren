import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _generate import page

education = [
    ("1987 – 1988", "Helseskolen Søborg: Anatomi, fysiologi, patologi, alternativ sygdomslære, øreakupunktur og zoneterapi."),
    ("1989", "Brosbøll's helseskole: Helhedsterapi, akutryk, massage og kiropraktik."),
    ("1995", "AM-Massageskole: Massage, bindevævs- og sportsmassage."),
    ("1996 – 1997", "Scandinavian College of Acupuncture i Søborg: Traditionel kinesisk akupunktur 1 og 2."),
    ("1997", "Moxaskolen i Svendborg: Moxakursus."),
    ("1998", "Øjensygdomsterapi: Kursus hos J. Boel."),
    ("1998", "Auriculomedicin – École de Paul Nogier."),
    ("2000", "Nada – National Acupuncture Detoxification Association: Afvænning."),
    ("2000 – 2001", "Akupunktur Internationale Universitet Medicina Alternativa – John Boel."),
    ("2001", "Mikroterapi Akupunktur: hos J. Boel."),
    ("2002", "Avanceret øreakupunktur hos Prof. Dr. med. Michel Marignan (Marseilles, Frankrig) og Dr. med. Raphael Nogier (Lyon, Frankrig)."),
    ("1997 & 2002", "Studier i auriculoterapi og -medicin hos Rafael Nogier."),
    ("1999 & 2002", "Studier i posturologi hos Michael Migranon."),
    ("2006", "Qi-Mag Feng Shui Business, Hus & Have Konsulent hos Qi-Mag International Feng Shui og Geobiology Institute – Marianne P."),
    ("2010", "TFT Management – Triune Institute, LLC: Tankefeltterapi."),
    ("2011", "Traditionel Kinesisk Medicin – Materia Medica, den klassiske receptlære og den kinesiske interne medicin."),
    ("2016", "BBRS-kursus i akupunktur – teori og praktik efter BBRS: Hugo Nielsen Parallel Akupunktur – Specialdiagnostik & Behandling."),
    ("2017", "Acupunctureshop.com Grundkursus & Udvidet kursus i Astar Laser (8/18 W): medicinsk virkning, sikkerhedsforanstaltninger, bivirkninger, terapifunktioner, indstilling, vedligeholdelse og hudtest."),
    ("2019", "Dansk Akupunktører – kursus efterårsseminar."),
    ("2019", "Myo Fascial Decompression – Bay Area Sports Performance and Rehabilitation seminar."),
]

edu_items = "\n".join(
    f'        <li><span class="price-name"><strong>{year}</strong> — {desc}</span></li>'
    for year, desc in education
)

body = f'''  <section class="section">
    <div class="container article">
      <h2>Charlotte Kuszons baggrund</h2>
      <p>Charlotte Kuszon har praktiseret akupunktur og holistisk behandling siden 1998. Bag klinikken ligger mere end tre årtiers løbende efteruddannelse inden for traditionel kinesisk akupunktur, posturologi, øreakupunktur, zoneterapi og en lang række beslægtede behandlingsformer – se den fulde uddannelseshistorik nedenfor.</p>

      <h3>Uddannelse og kurser</h3>
      <ul class="price-list" style="margin-bottom:2rem;">
{edu_items}
      </ul>

      <h2>Links til Danske Akupunktører, gode venner og dygtige kollegaer</h2>
      <ul class="plain-list">
        <li>Akupunktør og hypnoterapeut Jens Waaben – København K</li>
        <li>Sexolog og parterapeut Nadja Kuszon – <a href="http://www.nadjakuszon.dk" target="_blank" rel="noopener" style="color:var(--color-accent)">nadjakuszon.dk</a> – Kbh. &amp; Hillerød</li>
        <li>Psykologisk rådgivning og alternativ behandling I/S – Frede Munkholm – Hovmosevej 3, 3400 Hillerød – Tlf. 48246880</li>
        <li>Tandlægerne Hørsholm – Camilla Trolle – <a href="http://www.hovedgade33.dk" target="_blank" rel="noopener" style="color:var(--color-accent)">hovedgade33.dk</a> – Hørsholm</li>
        <li>Psykoterapi, Den Intuitive &amp; TRE-Provider – Jeanne Fairy – <a href="http://www.jeannefairy.dk" target="_blank" rel="noopener" style="color:var(--color-accent)">jeannefairy.dk</a> &amp; <a href="http://www.hangonwords.dk" target="_blank" rel="noopener" style="color:var(--color-accent)">hangonwords.dk</a> – Virum</li>
        <li>Akupunktør Bo Stentofte – Køge – <a href="http://www.lyngens-akupunktur.dk" target="_blank" rel="noopener" style="color:var(--color-accent)">lyngens-akupunktur.dk</a></li>
      </ul>

      <h2>Bestil tid til akupunktur i Rungsted</h2>
      <p>Hvis du er interesseret i at bestille tid til akupunktur i Rungsted, eller vil høre mere om akupunktur som behandlingsform, så er du meget velkommen til at kontakte mig for en uforpligtende samtale.</p>
      <p>Har du yderligere spørgsmål, er du velkommen til at skrive en mail på <a href="mailto:ckuszon@akupunktoeren.com" style="color:var(--color-accent)">ckuszon@akupunktoeren.com</a> eller ringe til os på telefon 31 60 88 80.</p>
      <div class="btn-row article-cta">
        <a class="btn btn-accent" href="../priser/">Se priser</a>
        <a class="btn btn-cta" href="../kontakt/">Kontakt os i dag</a>
      </div>
    </div>
  </section>
'''

page(
    "akupunktoeren-baggrund-og-uddannelse",
    "Akupunktøren – baggrund og uddannelse",
    "Mød Charlotte Kuszon: baggrund, mangeårig erfaring og bred uddannelse inden for akupunktur, posturologi og holistisk behandling.",
    "akupunktoeren",
    "Akupunktur Charlotte Kuszon",
    "Akupunktøren – baggrund og uddannelse",
    body,
)
