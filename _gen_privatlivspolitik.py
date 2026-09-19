import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _generate import page

body = '''  <section class="section">
    <div class="container article">
      <h2>Dataansvarlig</h2>
      <p>Jeg er dataansvarlig for behandlingen af de personoplysninger, jeg indsamler via denne hjemmeside:</p>
      <p>Akupunktur Charlotte Kuszon<br>Pennehave 9, 2960 Rungsted Kyst<br>CVR: 25513126<br>Email: <a href="mailto:ckuszon@akupunktoeren.com" style="color:var(--color-accent)">ckuszon@akupunktoeren.com</a><br>Telefon: 31 60 88 80</p>

      <h2>Hvilke oplysninger indsamler jeg</h2>
      <p>Jeg indsamler kun de personoplysninger, du selv giver mig, når du bruger kontaktformularen på siden. Det drejer sig om:</p>
      <ul class="plain-list">
        <li>Navn</li>
        <li>Telefonnummer (hvis du vælger at oplyse det)</li>
        <li>Email-adresse</li>
        <li>Indholdet af din besked</li>
      </ul>
      <p>Jeg indsamler ikke oplysninger via cookies, sporing eller analyseværktøjer – se afsnittet om cookies herunder.</p>

      <h2>Formål og retsgrundlag</h2>
      <p>Oplysningerne bruges udelukkende til at besvare din henvendelse og eventuelt aftale eller gennemføre en behandling. Retsgrundlaget er dit samtykke ved at sende formularen (databeskyttelsesforordningens artikel 6, stk. 1, litra a) samt, hvis der indgås en behandlingsaftale, opfyldelse af aftalen (artikel 6, stk. 1, litra b).</p>

      <h2>Tredjeparter</h2>
      <p>Kontaktformularen leveres af tjenesten Formspree, som modtager og videresender din besked til min email. Formspree er en databehandler, der opbevarer oplysningerne på servere uden for EU/EØS. Du kan læse mere om Formsprees behandling af data på <a href="https://formspree.io/legal/privacy-policy" target="_blank" rel="noopener" style="color:var(--color-accent)">formspree.io</a>. Jeg deler ikke dine oplysninger med andre tredjeparter, og oplysningerne bruges ikke til markedsføring.</p>

      <h2>Opbevaring af oplysninger</h2>
      <p>Jeg opbevarer henvendelser og eventuelle patientoplysninger, så længe det er nødvendigt for at kunne besvare din henvendelse eller gennemføre din behandling, og i øvrigt så længe lovgivningen kræver det – f.eks. bogføringslovens krav om opbevaring af regnskabsbilag i 5 år.</p>

      <h2>Cookies</h2>
      <p>Denne hjemmeside sætter ikke selv cookies til statistik, analyse eller markedsføring. Der bruges ingen cookie-banner, fordi der ikke indsamles data på den måde.</p>
      <p>Formspree kan som databehandler af kontaktformularen sætte tekniske cookies, der er nødvendige for, at formularen kan fungere og beskytte mod spam. Min hostingudbyder kan desuden registrere tekniske oplysninger som IP-adresse i driftslogs, hvilket er normal praksis for at holde en hjemmeside sikker og kørende.</p>

      <h2>Dine rettigheder</h2>
      <p>Efter databeskyttelsesforordningen har du en række rettigheder i forhold til de oplysninger, jeg har om dig:</p>
      <ul class="plain-list">
        <li>Ret til at se dine oplysninger (indsigtsret)</li>
        <li>Ret til at få urigtige oplysninger rettet</li>
        <li>Ret til at få oplysninger slettet</li>
        <li>Ret til at få behandlingen af dine oplysninger begrænset</li>
        <li>Ret til at gøre indsigelse mod behandlingen</li>
        <li>Ret til dataportabilitet</li>
      </ul>
      <p>Hvis du ønsker at gøre brug af dine rettigheder, er du velkommen til at kontakte mig på <a href="mailto:ckuszon@akupunktoeren.com" style="color:var(--color-accent)">ckuszon@akupunktoeren.com</a> eller 31 60 88 80.</p>

      <h2>Klageadgang</h2>
      <p>Hvis du er utilfreds med, hvordan jeg behandler dine personoplysninger, er du velkommen til at kontakte mig først. Du har desuden altid ret til at klage til Datatilsynet:</p>
      <p>Datatilsynet<br>Carl Jacobsens Vej 35<br>2500 Valby<br><a href="https://www.datatilsynet.dk" target="_blank" rel="noopener" style="color:var(--color-accent)">datatilsynet.dk</a></p>

      <h2>Ændringer af denne politik</h2>
      <p>Jeg kan opdatere denne cookie- og privatlivspolitik, hvis der sker ændringer i, hvordan hjemmesiden eller kontaktformularen fungerer, eller hvis lovgivningen ændrer sig. Den seneste version er altid tilgængelig her på siden.</p>
    </div>
  </section>
'''

page(
    "privatlivspolitik",
    "Cookie- og privatlivspolitik",
    "Cookie- og privatlivspolitik for Akupunktur Charlotte Kuszon – hvilke oplysninger jeg indsamler via kontaktformularen, og hvordan de bruges og beskyttes.",
    "",
    "Akupunktur Charlotte Kuszon",
    "Cookie- og privatlivspolitik",
    body,
    include_cta_band=False,
)
