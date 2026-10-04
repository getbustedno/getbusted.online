# getbusted.online

Internasjonal nettside for Get Busted: engelsk på / og svensk på /sv/. Norsk ligger på getbusted.no.
Språkvalg øverst (EN / SV / NO). Første besøk fra en svensk telefon sendes til /sv/, og valgt språk huskes.

Bygg: `python3 build.py` (all tekst står i build.py, én blokk per språk). Bildene ligger i img/.

## Oppsett (én gang)
1. Kjøp domenet getbusted.online hvis det ikke er gjort.
2. GitHub Desktop: File → Add local repository → denne mappa → Publish repository (navn: getbusted.online, offentlig).
3. GitHub → repoet → Settings → Pages: Source «Deploy from a branch», branch main, mappe / (root). Custom domain: getbusted.online. Huk av Enforce HTTPS når sertifikatet er klart.
4. DNS hos domeneleverandøren:
   - A-poster for @: 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153
   - CNAME for www: <github-brukernavn>.github.io
5. Bytt lenka i bio på @getbusted.uk til getbusted.online og på @getbusted.se til getbusted.online/sv/.
