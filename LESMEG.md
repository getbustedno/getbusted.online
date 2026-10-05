# getbusted.online

Internasjonal nettside for Get Busted: engelsk på /, svensk på /sv/ og dansk på /da/. Norsk ligger på getbusted.no.
Språkvalg øverst (EN / SV / DA / NO). Første besøk fra en svensk eller dansk telefon sendes til /sv/ eller /da/, og valgt språk huskes.

Hjelp og personvern per språk (lenket i footeren, brukes som support- og personvern-URL i butikkene):
- engelsk: /help/ og /privacy/
- svensk: /sv/hjalp/ og /sv/integritet/
- dansk: /da/hjaelp/ og /da/privatliv/

Personvernsidene er oversatt fra store/personvern.html. Datoen står som plassholder («[date at launch]» osv.) i build.py og må fylles inn ved lansering, samme dag som på getbusted.no.

Bygg: `python3 build.py` (all tekst står i build.py, én blokk per språk). Bildene ligger i img/.

## Oppsett (én gang)
1. Kjøp domenet getbusted.online hvis det ikke er gjort.
2. GitHub Desktop: File → Add local repository → denne mappa → Publish repository (navn: getbusted.online, offentlig).
3. GitHub → repoet → Settings → Pages: Source «Deploy from a branch», branch main, mappe / (root). Custom domain: getbusted.online. Huk av Enforce HTTPS når sertifikatet er klart.
4. DNS hos domeneleverandøren:
   - A-poster for @: 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153
   - CNAME for www: <github-brukernavn>.github.io
5. Bytt lenka i bio på @getbusted.uk til getbusted.online og på @getbusted.se til getbusted.online/sv/.
