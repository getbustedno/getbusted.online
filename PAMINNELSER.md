# Påminnelser

## 1. januar 2027: lanseringsprisen på Busted+ utløper

Kjøpssidene (/purchases/, /se/kop/, /dk/koeb/) sier at Busted+ har lanseringspris til og med 31. desember 2026 og høyere pris fra 1. januar 2027.

Gjør dette 1. januar 2027 (eller før):
1. Bekreft at prisen i App Store og Google Play er endret.
2. I `build.py`: sett `LAUNCH_PRICE_ACTIVE = False`. Sidene sier da bare at prisen i butikken gjelder.
3. Kjør `python3 build.py` og kontroller kjøpssidene på alle tre språk.
4. Gjør tilsvarende i getbusted.no (`_kilde/juridisk.py`, samme konstanter, der prisene 249 og 299 kr står).
5. Sjekk at forsiden, butikkoppføringene og SoMe ikke fortsatt nevner lanseringsprisen.

Bygget stopper med en feilmelding hvis det kjøres 1. januar 2027 eller senere mens `LAUNCH_PRICE_ACTIVE = True`. Konstanten `PRICE_CHANGE_DATE` står øverst i `build.py`.

## Før Sverige-lanseringen: personvernsidene er ikke oppdatert

Personvernsidene /privacy/, /se/integritet/ og /dk/privatliv/ er ikke oppdatert til ny personvernerklæring ennå (de er bevisst ikke med på branchen kun-juridisk). Legg dem på listen og oppdater dem (LEGAL[...]['privacy'] i `build.py`, etter getbusted.no/personvern/) før Sverige-lanseringen.

Merk: `python3 build.py` endrer fotlenken («Terms of use», «Användarvillkor», «Brugsvilkår») på disse tre sidene. Det er ikke committet på kun-juridisk, så sidene har fortsatt gammel fotlenketekst til de oppdateres.

## Ikke verifisert

Klageorganer og tilsyn som er nevnt i `build.py`, pluss de som vanligvis hører hjemme i Sverige og Danmark. Ingen er sjekket mot offisielle kilder (navn, om de gjelder for en app/nettbutikk fra Norge, og at lenkene virker). Sjekk før lansering i hvert land.

Sverige (nevnt i /se/villkor/ og /se/integritet/):
- Allmänna reklamationsnämnden (ARN, arn.se) - IKKE VERIFISERT
- Konsumentverket (konsumentverket.se) - IKKE VERIFISERT
- Integritetsskyddsmyndigheten (IMY, imy.se) - IKKE VERIFISERT

Danmark (nevnt i /dk/vilkaar/ og /dk/privatliv/):
- Nævnenes Hus / Forbrugerklagenævnet (naevneneshus.dk) - IKKE VERIFISERT
- Datatilsynet Danmark (datatilsynet.dk) - IKKE VERIFISERT
- Forbrugerombudsmanden og Forbrugerstyrelsen: ikke nevnt ennå, vurder om de skal med - IKKE VERIFISERT

Norge, UK og EU (nevnt i personvern og vilkår):
- Datatilsynet Norge (datatilsynet.no/en/) - IKKE VERIFISERT
- Information Commissioner's Office, ICO (ico.org.uk) - IKKE VERIFISERT
- Forbrukerorganer og personvernmyndighet i EU-land generelt (ingen navn eller lenker) - IKKE VERIFISERT
- Consumer Rights Act 2015 (UK-henvisning i /purchases/) - lovhenvisning IKKE VERIFISERT
