# getbusted.online

Internasjonal nettside for Get Busted: engelsk på /, svensk på /sv/ og dansk på /dk/ (/da/ sender videre). Norsk ligger på getbusted.no.
Språkvalg øverst (EN / SE / DK / NO). Første besøk fra en svensk eller dansk telefon sendes til /se/ eller /dk/ (/sv/ sender videre til /se/), og valgt språk huskes.

Hjelp og juridiske sider per språk (lenket i footeren, hjelp og personvern brukes som support- og personvern-URL i butikkene):
- engelsk: /help/, /terms/, /privacy/, /cookies/, /purchases/
- svensk: /se/hjalp/, /se/villkor/, /se/integritet/, /se/cookies/, /se/kop/
- dansk: /dk/hjaelp/, /dk/vilkaar/, /dk/privatliv/, /dk/cookies/, /dk/koeb/

De juridiske sidene (LEGAL i build.py) er oversatt fra getbusted.no/_kilde/juridisk.py, som er kilden. Endres den norske teksten, må LEGAL og datoen («updated») oppdateres samme dag.

Bygg: `python3 build.py` (all tekst står i build.py, én blokk per språk). Bildene ligger i img/.

## Oppsett (én gang)
1. Kjøp domenet getbusted.online hvis det ikke er gjort.
2. GitHub Desktop: File → Add local repository → denne mappa → Publish repository (navn: getbusted.online, offentlig).
3. GitHub → repoet → Settings → Pages: Source «Deploy from a branch», branch main, mappe / (root). Custom domain: getbusted.online. Huk av Enforce HTTPS når sertifikatet er klart.
4. DNS hos domeneleverandøren:
   - A-poster for @: 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153
   - CNAME for www: <github-brukernavn>.github.io
5. Bytt lenka i bio på @getbusted.uk til getbusted.online og på @getbusted.se til getbusted.online/se/.
