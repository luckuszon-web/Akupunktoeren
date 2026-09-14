import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _generate import page

body = '''  <section class="section">
    <div class="container article">
      <h2>Helhedsorienteret behandling med akupunktur</h2>
      <p>Akupunkturen bygger på en holistisk menneskeopfattelse, hvilket vil sige, at det er hele mennesket, der behandles, ikke blot symptomet. Derfor er det vigtigt for akupunktøren at få så meget information af patienten som muligt for at stille den mest optimale akupunkturdiagnose.</p>
      <p>Patienten stilles derfor en lang række spørgsmål vedrørende den helbredsmæssige tilstand. Desuden kan akupunktøren anvende en række diagnoseværktøjer, såsom pulsdiagnose, tungediagnose, irisanalyse m.v., som alle har til formål at klarlægge/bekræfte kroppens ubalancer.</p>
      <p>Vi har stor erfaring med akupunktur som smertelindring og ved spændinger forskellige steder i kroppen. Allergier for dyr og pollen, luftvejsproblemer, astma, eksem, høfeber og tinnitus er alle gener og lidelser, som vi har gode erfaringer med at behandle ved hjælp af akupunktur. Faktisk har vi så gode resultater med at bruge akupunktur på høfeber-patienter, at langt de fleste får det bedre eller slipper helt af med høfeber.</p>
      <p>Derudover kan mange øjenlidelser og problemer med led og gigt behandles med akupunktur, hvor der i langt de fleste tilfælde ville kunne mærkes en markant forbedring.</p>

      <h3>Akupunktur kan i det hele taget have en lindrende effekt på en lang række smerter og lidelser, blandt andet</h3>
      <p><strong>Smerter og spændinger i:</strong></p>
      <ul class="plain-list">
        <li>Hoved</li><li>Nakke</li><li>Skulder</li><li>Ryg</li><li>Hofte</li><li>Knæ</li>
        <li>Akillessene</li><li>Hælespore</li><li>Kæbe</li><li>Psykiske ubalancer</li>
        <li>Balanceforstyrrelser</li><li>Koncentrationsbesvær</li><li>Neurologiske forstyrrelser</li>
        <li>Sanseapparatslidelser</li><li>Indlæringsvanskeligheder</li>
      </ul>

      <h3>Andre lidelser med gode resultater – øjenlidelser f.eks.:</h3>
      <ul class="plain-list">
        <li>Grøn stær</li><li>Øjen-forkalkninger</li><li>Kikkertsyn</li><li>Aldersbetinget langsyn</li>
        <li>Leddegigt</li><li>Slidgigt</li><li>Fibromyalgi</li>
      </ul>

      <h3>Andre ting:</h3>
      <ul class="plain-list">
        <li>Tinnitus</li><li>Idrætsskader</li><li>Høfeber</li><li>Lungeproblemer</li><li>Psoriasis / eksem</li>
      </ul>

      <h2>Sådan foregår en behandling</h2>
      <p>Når diagnosen er fastlagt, påbegyndes selve behandlingsforløbet, som kan variere meget alt efter lidelsens/ubalancens omfang. Selve behandlingen med nåle tager typisk 20-30 minutter. Behandlingsreaktionen kan f.eks. være alt fra ekstrem afslappelse til kløe/summen/prikken flere steder i kroppen.</p>
      <p>Efter behandlingen bliver nogle patienter trætte, og andre oplever forøget energi og livsmod. Under hele behandlingsforløbet er det vigtigt at indtage rigeligt med væske, så kroppen får hjælp til at udskille affaldsstoffer.</p>
      <p>Har du spørgsmål til behandlingsforløbet, giver jeg med glæde en nærmere forklaring.</p>

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
    "akupunktur",
    "Akupunktur",
    "Helhedsorienteret akupunkturbehandling hos Akupunktur Charlotte Kuszon i Rungsted – smertelindring, allergi, høfeber og meget mere.",
    "akupunktur",
    "Akupunktur Charlotte Kuszon",
    "Akupunktur",
    body,
)
