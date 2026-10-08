# Påminnelser

## Før Sverige-lanseringen: personvernsidene er ikke oppdatert

Personvernsidene /privacy/, /se/integritet/ og /dk/privatliv/ er ikke oppdatert til ny personvernerklæring ennå (de er bevisst ikke med på branchen kun-juridisk). Legg dem på listen og oppdater dem (LEGAL[...]['privacy'] i `build.py`, etter getbusted.no/personvern/) før Sverige-lanseringen. Når du gjør det: bytt «over 18» til «minst 18 år» / «mindst 18 år» / «at least 18 years old», og sjekk at ingen dato eller pris dukker opp.

Merk: `python3 build.py` endrer fotlenken («Terms of use», «Användarvillkor», «Brugsvilkår») på disse tre sidene. Det er ikke committet på kun-juridisk. Kjør `git checkout -- privacy se/integritet dk/privatliv` etter hvert bygg, til de oppdateres.

## Ingen priser og ingen datoer på en/sv/da

Vedtatt (okt 2026): sidene på getbusted.online har ingen priser, ingen lanseringspris og ingen lanseringsdato. Bare Norge lanseres 30. oktober (getbusted.no). Utenlandske priser og datoer er ikke vedtatt.
- `season.js`: `LAUNCH = null`. Lanseringsbryteren (butikkmerker blir lenker, «Ute nu») er av. Sett en dato først når den er vedtatt for landet. `?launch=1` i adressen fungerer fortsatt som test.
- Før lansering i et land: bestem pris, dato og tekst, og legg dem inn i `build.py` (PRICE_TXT, UPDATE) sammen.
- Pakkeflisene på forsiden viser fortsatt «Kommer 5. nov» osv. (pakkedatoer). Sjekk at de stemmer for hvert land før Sverige/Danmark/UK åpner.

## Kortantall

Sidene sier «1 000+ kort» (sv: «1 000+», da: «1.000+», en: «1,000+») og «5 pakker fra start». Tallene i `COUNTS` i `build.py` er per pakke. Oppdater ved hvert pakkeslipp.

## Fjernet i denne runden (kun-juridisk, oktober 2026)

- Dato «30. oktober» på sv, da og en: nav-knapp, hero-merke, meta/og, FAQ, pakkegruppe og `season.js` (erstattet med «Snart» / «Kommer snart» / «Från start»).
- Løftet om prisavdrag hvis en Busted+-pakke ikke kommer (alle språk). Lovfestede rettigheter ved feil står igjen.
- Alle priser og lanseringspriser (Busted+-tag, «0 kr», «Lanseringspris»). `LAUNCH_PRICE_ACTIVE`-vakten er fjernet fra `build.py`.
- All omtale av fysisk kortstokk/kortspill/fysiske produkter (også «kortlek»/«deck»).
- «flokken»/«Skriv flokken ind» på dansk (erstattet med «Skriv spillerne ind», «I vælger selv niveauet», «dit selskab»).

## Ikke verifisert

Fra redaktør sv og da. Ingen av punktene står som forbehold på sidene. Sjekk med jurist/morsmålsleser før lansering i hvert land.

Generelt:
- Hele teksten bør leses av svensk og dansk morsmålsleser (helst med juridisk bakgrunn). Engelsk er skrevet i enkelt juridisk engelsk uten redaktør.
- Org.nr 927 118 300 og adressen Voldgata 27 mot Brønnøysundregistrene.
- At Apples og Googles kjøpsdialog faktisk innhenter uttrykkelig samtykke og bekreftelse på at angreretten bortfaller (viktigste åpne punkt, sv og da; tilsvarende for UK: Consumer Contracts Regulations reg. 37). Sammendraget på dansk sier «når du har givet samtykke i butikkens betalingsdialog». Hvis dialogen ikke gjør dette, må appen vise egen tekst/avkrysning før kjøp.
- Om Snikkerbua Holding AS er «sælger/säljare» overfor forbrukere i app-kjøp, eller om Apple/Google er det.
- «Så länge vi erbjuder appen» for Busted+ mot svensk/dansk/britisk markedsføringsrett (Forbrugerombudsmanden fører tilsyn i Danmark).
- Om «ersätter med likvärdigt innehåll» (§6) og ansvarsbegrensningen (§7) holder mot konsumentregler i hvert land.
- At niveauet fortsatt heter «Get Fu**ed» i appen (merkenavnet er Get Busted), og at «valfritt paket» stemmer for Kvällspaketet/Aftenpakken.

Sverige (/se/villkor/, /se/kop/):
- Lovnavn og -nummer: lagen (2005:59) om distansavtal och avtal utanför affärslokaler; konsumentköplagen (2022:260, nummer står ikke på siden) - IKKE VERIFISERT
- Reklamasjonsfrist («inom skälig tid») og «häva köpet» - IKKE VERIFISERT
- Hallå konsument (lenket til konsumentverket.se), Allmänna reklamationsnämnden (ARN, arn.se), Konsumentverket - IKKE VERIFISERT. Om ARN tar saker mot en norsk næringsdrivende, og om Europeiske forbrukersenter (ECC Sverige) er riktigere for grenseoverskridende saker - IKKE VERIFISERT
- Om EU-ODR-plattformen er avviklet (derfor ikke nevnt) - IKKE VERIFISERT
- Lenkene til Apple (support.apple.com/sv-se/118223) og Google (support.google.com/googleplay/answer/15574897?hl=sv) - IKKE VERIFISERT, test at de virker
- Integritetsskyddsmyndigheten (IMY, imy.se, i /se/integritet/) - IKKE VERIFISERT

Danmark (/dk/vilkaar/, /dk/koeb/):
- Forbrugerklagenævnet via Nævnenes Hus (naevneneshus.dk): om det tar klager mot norsk virksomhet uten dansk filial, og om Forbrugereuropa (ECC Danmark) skal nevnes - IKKE VERIFISERT
- Forbrug.dk (forbrug.dk, lagt inn som generell veiledning) - IKKE VERIFISERT
- Forbrugerombudsmanden og Forbrugerstyrelsen: ikke nevnt, bevisst (tilsyn, ikke klageinstans) - IKKE VERIFISERT
- Begreper og lov: forbrugeraftaleloven, «fjernsalg», «forholdsmæssigt afslag», «hæve købet» - IKKE VERIFISERT
- «Apple-konto» i stedet for «Apple-id»: sjekk mot dagens danske iOS-tekst og support.apple.com/da-dk - IKKE VERIFISERT
- Lenkene til Apple (support.apple.com/da-dk/118223) og Google (...answer/15574897?hl=da) - IKKE VERIFISERT, test at de virker
- Datatilsynet Danmark (datatilsynet.dk, i /dk/privatliv/) - IKKE VERIFISERT
- Kombinasjonen «norsk lov gælder» og dansk forbrukerlov i «Fejl ved køb» - IKKE VERIFISERT; be juristen vurdere om Brugsvilkår §9 bør si det eksplisitt
- Om «Hvad du køber»: Kort fortalt-sammendraget er tilstrekkelig opplysning om bortfall av fortrydelsesret - IKKE VERIFISERT
- Redaktør-da brukte «som ikke leveres på et fysisk medie» i fortrydelsesret; det er utelatt fordi all omtale av fysiske produkter er fjernet. Be juristen vurdere om lovens formulering må inn.

Norge, UK og EU (personvern og vilkår):
- Datatilsynet Norge (datatilsynet.no/en/) - IKKE VERIFISERT
- Information Commissioner's Office, ICO (ico.org.uk) - IKKE VERIFISERT
- Forbrukerorganer og personvernmyndighet i EU-land generelt (ingen navn eller lenker) - IKKE VERIFISERT
- Consumer Rights Act 2015 og Consumer Contracts (Information, Cancellation and Additional Charges) Regulations 2013 reg. 37 (UK-henvisninger i /purchases/) - lovhenvisning IKKE VERIFISERT

## Julekalender på en/sv/da

Kalenderseksjonen og FAQ-punktet er fjernet fra en/sv/da (CAL = False i build.py, seksjonen genereres ikke). Når kalenderen skal vises i utlandet, sett CAL = True og bygg på nytt. Husk å gjøre det før 1. desember og bare etter Emils ja.
