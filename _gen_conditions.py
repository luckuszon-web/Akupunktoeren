import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _generate import page

CTA_BUTTONS = '''
    <div class="btn-row article-cta">
      <a class="btn btn-accent" href="../priser/">Se priser</a>
      <a class="btn btn-cta" href="../kontakt/">Kontakt mig i dag</a>
    </div>'''

BOOK_TEXT = '''
    <h2>Bestil tid til akupunktur i Rungsted/Hørsholm</h2>
    <p>Hvis du er interesseret i at bestille tid til akupunktur i Rungsted/Hørsholm, eller vil høre mere om akupunktur som behandlingsform, så er du meget velkommen til at kontakte mig for en uforpligtende samtale.</p>
    <p>Har du yderligere spørgsmål, er du velkommen til at skrive en mail på <a href="mailto:ckuszon@akupunktoeren.com" style="color:var(--color-accent)">ckuszon@akupunktoeren.com</a> eller ringe til mig på telefon 31 60 88 80.</p>''' + CTA_BUTTONS


def article(slug, title, description, eyebrow, intro_html, extra_html=""):
    body = f'''  <section class="section">
    <div class="container article">
      <h2>{eyebrow}</h2>
{intro_html}
{extra_html}
{BOOK_TEXT}
    </div>
  </section>
'''
    page(slug, title, description, slug, "Akupunktur Charlotte Kuszon", title, body)


article(
    "smerter-og-spaendinger",
    "Smerter og spændinger",
    "Effektiv behandling af smerter og spændinger med akupunktur hos Akupunktur Charlotte Kuszon i Rungsted/Hørsholm.",
    "Fjernelse af smerter og spændinger med akupunktur",
    '''    <p>Smerter og spændinger i hele eller dele af kroppen kan være en stor gene i hverdagen og for nogle decideret invaliderende.</p>
    <p>Det kan være alt fra en forkert arbejdsstilling til posturologisk skævhed eller forkert brug af kroppen ved sportsudøvelse, der kan være årsag til smerterne.</p>
    <p>På Akupunkturklinik Charlotte Kuszon har jeg erfaring med behandling af en lang række smerter og spændinger, hvor jeg har set rigtig gode resultater ved brug af akupunktur.</p>
    <p>I langt de fleste tilfælde kan akupunktur helt eller delvist fjerne smerter og spændinger og dermed forbedre patientens tilstand væsentligt.</p>
    <p>Sammen med dig finder jeg årsagen til dine smerter og får tilrettelagt et behandlingsforløb, hvor jeg retter op på problemet. <a href="../posturologi/" style="color:var(--color-accent)">Læs mere om posturologi her.</a></p>''',
)

article(
    "hoved-og-nakke",
    "Hoved og nakke",
    "Behandling af hovedpine, migræne og nakkesmerter med akupunktur hos Akupunktur Charlotte Kuszon i Rungsted/Hørsholm.",
    "Læs mere om hoved og nakke",
    '''    <p>Hovedpine, migræne, piskesmæld, nakkesmerter og -spændinger er et problem i større eller mindre grad for mange mennesker.</p>
    <p>Akupunktur kan allerede efter få behandlinger afhjælpe de værst forekommende smerter. Ved migræne bliver mange patienter helt smertefri på trods af, at det ikke er lykkedes dem med konventionel behandling og medicin.</p>
    <p>Efter en grundig snak med dig om problemet tilrettelægger jeg et behandlingsforløb, som er skræddersyet efter dine behov. <a href="../posturologi/" style="color:var(--color-accent)">Læs mere om posturologi her.</a></p>''',
)

article(
    "tinnitus",
    "Tinnitus",
    "Akupunkturbehandling af tinnitus hos Akupunktur Charlotte Kuszon i Rungsted/Hørsholm.",
    "Tinnitus og akupunkturbehandling",
    '''    <p>Tinnitus er en ørelidelse, der kan være invaliderende i større eller mindre omfang. Nogle patienter bemærker det stort set ikke i hverdagen, mens andre ikke kan fungere optimalt på grund af tinnitus.</p>
    <p>Jeg har rigtig gode erfaringer med at behandle tinnitus ved hjælp af akupunktur og på den måde enten få den generende lyd helt væk eller i hvert fald forbedre tilstanden væsentligt.</p>
    <h3>Behandling af forskellige typer tinnitus</h3>
    <p>Jeg udfører forskellige behandlinger alt efter, hvilken type tinnitus der er tale om. Nogle tinnituspatienter oplever en susen for ørerne, mens andre generes af en konstant hyletone. Inden behandlingen går i gang, kortlægger jeg sammen med dig typen af tinnitus, så vi sikrer den rette behandling.</p>''',
)

article(
    "hoefeber",
    "Høfeber",
    "Effektiv akupunkturbehandling mod høfeber og allergi hos Akupunktur Charlotte Kuszon i Rungsted/Hørsholm.",
    "Læs mere om høfeber",
    '''    <p>Høfeber, allergi over for dyr og allergi i forbindelse med luftveje generelt kan for nogle være en meget ubehagelig lidelse, hvor selv konventionel behandling og medicin ikke er nok til at holde symptomerne nede.</p>
    <p>Akupunktur er utrolig effektivt mod høfeber og allergi generelt. Faktisk så effektiv, at langt de fleste høfeberpatienter, jeg behandler med akupunktur, får det bedre eller slipper helt af med høfeberen.</p>
    <h3>Rigtig gode resultater ved behandling af høfeber</h3>
    <p>Ved hjælp af akupunktur kan jeg styrke kroppens immunforsvar og derved minimere medicinforbrug, snue, kløende og røde øjne i forbindelse med høfeber. Erfaringen er, at man meget hurtigt mærker resultater ved akupunkturbehandlinger mod høfeber.</p>
    <p>Høfeberen kan behandles, selvom allergien er startet, men jeg anbefaler, at du starter behandlingsforløbet lige inden "allergisæsonen" går i gang.</p>''',
)

article(
    "idraets-skader",
    "Idrætsskader",
    "Hurtig og effektiv akupunkturbehandling af idrætsskader hos Akupunktur Charlotte Kuszon i Rungsted/Hørsholm.",
    "Forkort skadeperioden med akupunktur",
    '''    <p>Idrætsskader som eksempelvis forstuvninger, fibersprængninger eller ondt i fødderne kan meget hurtigt udbedres med akupunktur. Den bedste effekt opnås, når du kommer samme dag eller dagen efter, skaden er sket.</p>
    <p>Det vil sige, at jo nyere skaden er, jo nemmere er den at behandle, så den efter kun ganske få dage ofte er helt væk. En forstuvning kan som hovedregel være væk efter tre dage, hvis den behandles med akupunktur med det samme.</p>
    <p>Hvis en skade behandles med akupunktur en uge efter, den er opstået, kan skadesperioden som hovedregel halveres.</p>
    <p>Er der gået længere tid, fra en skade er opstået, til den behandles, vil den dog stadig kunne behandles med akupunktur og give resultater.</p>''',
)

article(
    "astma",
    "Astma",
    "Akupunkturbehandling af astma, lungeproblemer og bronkitis hos Akupunktur Charlotte Kuszon i Rungsted/Hørsholm.",
    "Læs mere om astma",
    '''    <p>Lungeproblemer, astma og bronkitis er alle lidelser, der har betydning for vejrtrækningen og som oftest behandles med konventionel medicin. Ofte har astmapatienter også allergi.</p>
    <p>På Akupunkturklinik Charlotte Kuszon har jeg stor erfaring med behandling af astma, lungeproblemer, allergi og bronkitis, hvor akupunktur har en gavnlig effekt og er med til at forbedre lungefunktionen.</p>
    <h3>Gode resultater</h3>
    <p>I nogle tilfælde kan patienter næsten undvære astmamedicinen eller bliver mindre afhængige af den. Det er individuelt, hvor mange behandlinger, det kræver, før der opnås en ændring.</p>
    <p>Jeg har rigtig gode erfaringer med behandling af vejrtrækningslidelser, og langt de fleste oplever øget livskvalitet efter et behandlingsforløb.</p>''',
)

article(
    "ryg-og-bevaegeapparat",
    "Ryg og bevægeapparat",
    "Akupunkturbehandling af smerter i ryg og bevægeapparat hos Akupunktur Charlotte Kuszon i Rungsted/Hørsholm.",
    "Læs mere om ryg og bevægeapparat",
    '''    <p>En af de lidelser, jeg har allerbedst erfaringer med at behandle ved hjælp af akupunktur, er smerter i ryg og bevægeapparat. Akupunkturen kan rette op på kroppens skævheder og dermed lindre smerten. Ofte oplever jeg, at patienter, der har været plaget af smerter i mange år, ender med at blive smertefri.</p>
    <p>I det hele taget kan stort set alle former for smerter og spændinger i bevægeapparatet behandles og smertelindres væsentligt med akupunktur. Det er altid individuelt, hvor mange behandlinger der er behov for.</p>''',
    '''    <h3>Nogle af de lidelser, akupunkturen kan behandle i ryg og bevægelsesapparat, er:</h3>
    <ul class="plain-list">
      <li>Tennisalbue</li>
      <li>Musearm</li>
      <li>Skulderskader</li>
      <li>Lænde-/iskiassmerter</li>
      <li>Gigtsmerter</li>
      <li>Hofte</li>
      <li>Knæ</li>
      <li>Ledsmerter</li>
      <li>Skader forårsaget af ulykker</li>
    </ul>''',
)

article(
    "hormonforstyrrelser",
    "Hormonforstyrrelser",
    "Holistisk akupunkturbehandling af hormonforstyrrelser hos Akupunktur Charlotte Kuszon i Rungsted/Hørsholm.",
    "Læs mere om hormonforstyrrelser",
    '''    <p>Hormonel ubalance kan give fertilitetsproblemer, herunder tab af barn og dårlig sædkvalitet, og kan desuden være årsag til eksempelvis uregelmæssig menstruation, PCO og problemer i overgangsalderen.</p>
    <p>På Akupunkturklinik Charlotte Kuszon har jeg stor erfaring inden for behandling af hormonforstyrrelser med akupunktur. Jeg kan hjælpe dig med at finde tilbage til en harmonisk balance i kroppen, så du igen kan fungere normalt.</p>
    <h3>Holistisk opfattelse</h3>
    <p>Jeg lægger vægt på en god dialog med mine patienter gennem hele behandlingsforløbet.</p>
    <p>Min holistiske anskuelse af kroppen betyder, at jeg ser på problemer i sammenhæng og gør meget ud af at finde frem til den egentlige årsag. Derved kan jeg behandle problemet bedst muligt.</p>''',
)
