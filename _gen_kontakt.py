import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _generate import page, icon

body = f'''  <section class="section">
    <div class="container article-grid">
      <div>
        <h2>Interesseret i at høre mere?</h2>
        <p>Har du brug for professionel behandling, eller er du i tvivl om, hvordan jeg bedst kan hjælpe dig, er du velkommen til at kontakte mig via formularen herunder.</p>

        <form id="kontakt-formspree-form" class="contact-form" action="https://formspree.io/f/xwlkgnke" method="POST">
          <div class="form-message success" id="kontakt-form-success" hidden>Tak for din henvendelse! Jeg vender tilbage hurtigst muligt.</div>
          <div class="form-message error" id="kontakt-form-error" hidden>Der opstod en fejl. Prøv igen, eller ring til mig på 31 60 88 80.</div>

          <div class="contact-form-row">
            <div>
              <label for="f-name">Navn</label>
              <input type="text" id="f-name" name="name" required autocomplete="name">
            </div>
            <div>
              <label for="f-phone">Tlf. nr.</label>
              <input type="tel" id="f-phone" name="phone" autocomplete="tel">
            </div>
          </div>
          <label for="f-email">Email</label>
          <input type="email" id="f-email" name="email" required autocomplete="email">
          <label for="f-message">Besked</label>
          <textarea id="f-message" name="message" required></textarea>
          <input class="honeypot-field" type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true">
          <button type="submit" class="btn btn-cta">Send besked</button>
        </form>

        <script>
        (function () {{
          var form = document.getElementById('kontakt-formspree-form');
          if (!form) return;
          var successMsg = document.getElementById('kontakt-form-success');
          var errorMsg = document.getElementById('kontakt-form-error');
          form.addEventListener('submit', function (e) {{
            e.preventDefault();
            successMsg.hidden = true;
            errorMsg.hidden = true;
            fetch(form.action, {{
              method: 'POST',
              body: new FormData(form),
              headers: {{ 'Accept': 'application/json' }}
            }}).then(function (response) {{
              if (response.ok) {{
                window.location.href = '../tak-for-din-henvendelse/';
              }} else {{
                errorMsg.hidden = false;
              }}
            }}).catch(function () {{
              errorMsg.hidden = false;
            }});
          }});
        }})();
        </script>
      </div>

      <div class="article-aside">
        <h3>Jeg glæder mig til at høre fra dig!</h3>
        <p style="font-size:0.95rem;">Tøv ikke med at kontakte mig, hvis du har spørgsmål om mine behandlinger, eller hvis du ønsker vejledning om, hvordan jeg kan hjælpe dig. Jeg besvarer henvendelser inden for 1–3 hverdage. Er din henvendelse akut, er du meget velkommen til at ringe til mig.</p>
        <ul class="check-list on-light">
          <li>{icon("check")} <span>Få svar på din henvendelse inden for 1-3 hverdage</span></li>
          <li>{icon("check")} <span>Erfaren fagperson med mangeårig erfaring</span></li>
        </ul>
        <div class="btn-row" style="margin-top:1rem;">
          <a class="btn btn-cta" href="tel:+4531608880">+45 31 60 88 80</a>
        </div>
      </div>
    </div>
  </section>
'''

page(
    "kontakt",
    "Kontakt",
    "Kontakt Akupunktur Charlotte Kuszon i Rungsted – book en tid eller stil et spørgsmål via formularen.",
    "kontakt",
    "Akupunktur Charlotte Kuszon",
    "Kontakt",
    body,
    include_cta_band=False,
)
