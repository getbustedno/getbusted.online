# Bygger getbusted.online: engelsk på /, svensk på /se/ og dansk på /dk/ (/sv/ og /da/ sender videre). Norsk ligger på getbusted.no.
# Hver språkblokk gir forside, hjelpeside og juridiske sider (vilkår, personvern, cookies, kjøp). Juridisk tekst står i LEGAL, oversatt fra getbusted.no/_kilde/juridisk.py.
# Kjør: python3 build.py
import html, pathlib, re
E = html.escape
ROOT = pathlib.Path(__file__).parent
SITE = 'https://getbusted.online'
MAIL = 'kontakt@getbusted.no'

# Adresser per språk. 'no' ligger på getbusted.no.
HOME = {'en': '/', 'sv': '/se/', 'da': '/dk/', 'no': 'https://getbusted.no/'}
HELP = {'en': '/help/', 'sv': '/se/hjalp/', 'da': '/dk/hjaelp/', 'no': 'https://getbusted.no/hjelp/'}
PRIV = {'en': '/privacy/', 'sv': '/se/integritet/', 'da': '/dk/privatliv/', 'no': 'https://getbusted.no/personvern/'}
TERMS = {'en': '/terms/', 'sv': '/se/villkor/', 'da': '/dk/vilkaar/', 'no': 'https://getbusted.no/vilkar/'}
COOK = {'en': '/cookies/', 'sv': '/se/cookies/', 'da': '/dk/cookies/', 'no': 'https://getbusted.no/informasjonskapsler/'}
BUY = {'en': '/purchases/', 'sv': '/se/kop/', 'da': '/dk/koeb/', 'no': 'https://getbusted.no/kjop/'}
FIRMA, ORGNR, ADDR = 'Snikkerbua Holding AS', '927 118 300', 'Floraveien 22B, 2007 Kjeller'
LANGS = ['en', 'sv', 'da']

T = {
 'en': dict(
  path='/', lang='en', hero='en', title='Get Busted - the party game that runs the night',
  desc='Get Busted is the party card game for game nights, house parties and cabin weekends. 1,000+ cards in English at launch, about the internet, the news and your group chat. Adults 18+.',
  og='One reader, 1,000+ cards at launch and zero boring breaks. For iPhone and Android.',
  nav=[('#how', 'How it works'), ('#packs', 'Packs'), ('#faq', 'FAQ')], download='Download',
  h1='The party game that runs the night',
  lead='One reader holds the phone. Everyone else looks at each other, not at a screen. 1,000+ cards in English at launch, about the internet, the news and your group chat, plus Rapid rounds, secret missions and song cards.',
  soonTo='Coming soon to', note='For adults 18+. Can always be played without alcohol.',
  heroAlt='Get Busted in use: a card on the screen of a phone',
  howK='How it works', howH='Ready in 20 seconds',
  steps=[('Add your crew', '2 to 30 players. Names go straight onto the cards, so nobody gets to hide.'),
         ('Pick your level', 'Mild, Cheeky or Get Fu**ed. And how thirsty you are, from sipping to very thirsty.'),
         ('Read out loud and play', 'The reader reads the cards. The dice, the twists and the Rapid rounds show up on their own.')],
  featK='More than a deck of cards', featH="Things a normal deck can't do",
  feats=[('Written for now', 'AI everything, viral moments, dating apps, budget airlines and the shows you binged. New topical cards every month, no update needed.'),
         ('Twists', "Some cards flip after they're read out. What you thought was safe, isn't."),
         ('Rapid', 'Five fingers up. Statements back to back. First one out loses.'),
         ('Secret missions', 'The phone goes to one player, who gets a mission only they know about.'),
         ('Song cards', 'Put on the song and follow the rule. One tap opens it in Spotify.'),
         ('Team play', 'Play in fixed duos or Red vs Blue. Team duels along the way, and the app keeps the score.'),
         ('Odds', '"What are the odds you ...?" You both count down and say a number at the same time.'),
         ('Big text', 'Larger letters that are easy to read out loud, even in a dark room. Switch with Aa mid-game.'),
         ('The night in numbers', 'After the game: the most busted player, cards played and Rapid rounds. Ready to share.')],
  packsK='Packs', packsH='One for every occasion',
  packsLead='Every pack has its own English cards, written for English-speaking crews, not translated. Try 5 cards from any pack for free before you buy.',
  packs=[('original', 'cover_original.jpg', 'Original', '50 free cards every night', None),
         ('halloween', 'cover_halloween.jpg', 'Halloween', 'Costumes and A24 horror', None),
         ('jul', 'cover_jul_en.jpg', 'Christmas', 'Office parties and NYE', None),
         ('nach', 'cover_nach_en.jpg', 'Afterparty', "When it's 3 a.m.", None),
         ('hytta', 'cover_hytta_en.jpg', 'The Cabin', 'Hot tubs and zero signal', None),
         ('reise', 'cover_reise_en.jpg', 'Travel', 'Budget airlines and flings', '2026-11-05'),
         ('student', 'cover_student.jpg', 'Student', "Freshers' and house parties", '2026-11-12'),
         ('utdrikning', 'cover_utdrikning_en.jpg', 'Stag & Hen', 'For the one getting married', '2026-11-19'),
         ('fotball', 'cover_fotball_en.jpg', 'Football', 'Match day and fantasy drama', '2026-11-21'),
         ('sport', 'cover_sport.jpg', 'Sport', 'Run clubs and padel losers', '2026-12-03')],
  specialsK='Seasonal specials', specialsH='Only in English',
  specials=[('friendsgiving', 'cover_friendsgiving.jpg', 'Friendsgiving', 'Potluck and turkey disasters', '2026-11-12'),
            ('paddys', 'cover_paddys.jpg', "St. Paddy's", 'Green, the craic and the Irish exit', '2027-03-03')],
  soon='Coming', months=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
  prices=[('Free', '50 cards from Original every night. No sign-up.'),
          ('One pack', 'Per theme pack, or the Get Fu**ed level across every pack. One-time purchase.'),
          ('Night Pack', 'One pack of your choice + the Get Fu**ed level, for less than buying them separately.'),
          ('Busted+', 'The whole app: every pack, including future ones, the Get Fu**ed level and unlimited Original. Pay once, no subscription. Launch price until the end of December.')],
  respK='Play smart', respH='Made for a good night, not a bad morning',
  resp=[('Max 6', 'Whatever the level, a card never asks for more than 6 sips.'),
        ('Water breaks', 'They come more often the thirstier you say you are.'),
        ('Alcohol-free', 'The same game with points instead of sips. Everyone can join.'),
        ('Skip', 'You can always skip a card. Always.')],
  faqK='Questions', faqH='FAQ',
  faq=[('Is it free?', 'Yes. You get 50 cards from the Original deck for free every night. Theme packs are one-time purchases, the Night Pack gets you one pack plus the Get Fu**ed level, and Busted+ unlocks the whole app with one payment. No subscription.'),
       ('Do we have to drink?', 'No. Turn on alcohol-free mode and every sip becomes a point. And skipping is always allowed.'),
       ('How many can play?', 'From 2 to 30. Big groups get more cards that apply to everyone at once.'),
       ('Can we play in teams?', 'Yes. Pick duos or two teams, Red vs Blue, when you set up the game. The app keeps the score.'),
       ('Which languages?', 'English, Swedish, Danish and Norwegian, each with its own cards and menus. Pick the language on the start screen.'),
       ('When is it out?', 'Soon on iPhone and Android. Follow @getbusted.uk on Instagram and TikTok to hear first.')],
  help='Help', privacy='Privacy', contact='Contact', foot='Adults 18+',
  terms='Terms', cookies='Cookies', buy='Purchases & refunds', skip='Skip to content', orgno='Org. no.', country='Norway',
  helpTitle='Help - Get Busted', helpDesc='Answers about Get Busted: how to play, restoring purchases, redeeming codes, alcohol-free mode and more.',
  helpK='Help', helpH='Questions and answers',
  helpQA=[('How do you play?', 'Enter the names (2 to 30 players), pick packs, level and how thirsty you are. One person is the reader: they hold the phone and read every card out loud. Swipe or tap for the next card, and tap the left edge of the card to go back. You can change the reader, and add or remove players, at any time by tapping the name at the top.'),
          ('How do I restore my purchases?', 'Open Packs in the app and tap Restore purchases under "Bought before?". Use the same Apple ID or Google account you bought with. You do not need an account with us.'),
          ('How do I redeem a code?', 'Open Packs and tap Redeem code. On iPhone, Apple opens a window where you enter the code. On Android, Google Play opens so you can redeem it there.'),
          ('How does alcohol-free mode work?', 'Choose Alcohol-free when you set up the game. It is the same game, but sips become points, and whoever has the most points loses. Everyone can play together, with or without a drink.'),
          ('Is the text hard to read?', 'Choose Large text when you set up the game, or tap Aa during the game to switch.'),
          ('Why 18+?', 'Get Busted is a party game for adults. The app asks you to confirm that you are 18 or older the first time you open it. If you are under 18, you cannot use the app.'),
          ('Can I skip a card?', 'Yes, always. Just go to the next card. Nobody has to do anything they do not want to.'),
          ('Something else?', f'Email <a href="mailto:{MAIL}">{MAIL}</a>. For purchases, include the purchase date or the receipt from Apple or Google.')],
 ),
 'sv': dict(
  path='/se/', lang='sv', hero='sv', title='Get Busted - festspelet som styr kvällen',
  desc='Get Busted är kortspelet för spelkvällen, efterfesten och stugan. 1 000+ kort från start, skrivna för Sverige, inte översatta. För vuxna 18+.',
  og='En läsare, 1 000+ kort från start och noll tråkiga pauser. För iPhone och Android.',
  nav=[('#how', 'Så funkar det'), ('#packs', 'Paket'), ('#faq', 'Frågor')], download='Ladda ner',
  h1='Festspelet som styr kvällen',
  lead='En person håller i telefonen och läser högt. Resten tittar på varandra, inte på en skärm. 1 000+ kort från start, skrivna för Sverige: Kalle Anka klockan tre, 08:or och norrlänningar.',
  soonTo='Snart i', note='För vuxna 18+. Går alltid att spela utan alkohol.',
  heroAlt='Get Busted i användning: ett kort på en mobilskärm',
  howK='Så funkar det', howH='Klart på 20 sekunder',
  steps=[('Skriv in gänget', '2 till 30 spelare. Namnen hamnar direkt på korten, så ingen kan gömma sig.'),
         ('Välj nivå', 'Mild, Fräck eller Get Fu**ed. Och hur törstiga ni är, från lagom till riktigt törstig.'),
         ('Läs högt och kör', 'Läsaren läser korten. Tärningen, twistarna och Rapid-rundorna dyker upp av sig själva.')],
  featK='Mer än en kortlek', featH='Sånt en vanlig kortlek inte kan',
  feats=[('Skrivet för Sverige', 'Swish, BankID, mello, Bajen och Gnaget, kräftor och Små grodorna. Nya aktuella kort varje månad, utan uppdatering.'),
         ('Twistar', 'Vissa kort vänder sig efter att de lästs upp. Det du trodde var säkert, är det inte.'),
         ('Rapid', 'Fem fingrar upp. Påståenden i rad. Först ute förlorar.'),
         ('Hemliga uppdrag', 'Telefonen går till en spelare som får ett uppdrag bara hen vet om.'),
         ('Låtkort', 'Sätt på låten och följ regeln. Ett tryck öppnar den i Spotify.'),
         ('Lagspel', 'Spela i fasta duos eller Röd mot Blå. Lagdueller längs vägen, och appen håller koll på ställningen.'),
         ('Odds', '«Vad är oddsen att du ...?» Båda räknar ner och säger ett tal samtidigt.'),
         ('Stor text', 'Större bokstäver som är lätta att läsa högt, även i ett mörkt rum. Byt med Aa mitt i spelet.'),
         ('Kvällen i siffror', 'Efter spelet: den mest påkomna, antal kort och Rapid-rundor. Redo att dela.')],
  packsK='Paket', packsH='Ett för varje tillfälle',
  packsLead='Varje paket har egna svenska kort, skrivna i Sverige för svenskar. Testa 5 kort från valfritt paket gratis innan du köper.',
  packs=[('original', 'cover_original.jpg', 'Original', '50 gratis kort varje kväll', None),
         ('halloween', 'cover_halloween.jpg', 'Halloween', 'Maskerad och skräckfilm', None),
         ('jul', 'cover_jul.jpg', 'Jul', 'Julbord och Kalle Anka', None),
         ('nach', 'cover_nach_sv.jpg', 'Efterfest', 'När klockan är tre', None),
         ('hytta', 'cover_hytta_sv.jpg', 'Stugan', 'Bastu och noll täckning', None),
         ('reise', 'cover_reise_sv.jpg', 'Resa', 'Charter och Finlandsbåten', '2026-11-05'),
         ('student', 'cover_student.jpg', 'Student', 'Nollning och sittningar', '2026-11-12'),
         ('utdrikning', 'cover_utdrikning_sv.jpg', 'Svensexa & möhippa', 'För den som ska gifta sig', '2026-11-19'),
         ('fotball', 'cover_fotball_sv.jpg', 'Fotboll', 'Allsvenskan och derby', '2026-11-21'),
         ('sport', 'cover_sport.jpg', 'Sport', 'Padel och Vasaloppet', '2026-12-03')],
  specialsK='Bara i Sverige', specialsH='Paket för svenska högtider',
  specials=[('mello', 'cover_mello.jpg', 'Mello', 'Sex lördagar och en final', '2027-01-29'),
            ('midsommar', 'cover_midsommar.jpg', 'Midsommar', 'Sill, jordgubbar och regn', '2027-06-04'),
            ('kraftskiva', 'cover_kraftskiva.jpg', 'Kräftskiva', 'Pappershattar och allsång', '2027-07-30')],
  soon='Kommer', months=['jan', 'feb', 'mars', 'april', 'maj', 'juni', 'juli', 'aug', 'sep', 'okt', 'nov', 'dec'],
  prices=[('Gratis', '50 kort från Original varje kväll. Ingen registrering.'),
          ('Ett paket', 'Per temapaket, eller Get Fu**ed-nivån i alla paket. Engångsköp.'),
          ('Kvällspaket', 'Ett paket du väljer + Get Fu**ed-nivån, till lägre pris än var för sig.'),
          ('Busted+', 'Hela appen: alla paket, även de som kommer, Get Fu**ed-nivån och obegränsat Original. Betala en gång, ingen prenumeration. Lanseringspris året ut, till och med december.')],
  respK='Spela smart', respH='Gjort för en bra kväll, inte en dålig morgon',
  resp=[('Max 6', 'Oavsett nivå ber ett kort aldrig om mer än 6 klunkar.'),
        ('Vattenpauser', 'De kommer oftare ju törstigare ni säger att ni är.'),
        ('Alkoholfritt', 'Samma spel med poäng i stället för klunkar. Alla kan vara med.'),
        ('Stå över', 'Du får alltid stå över ett kort. Alltid.')],
  faqK='Frågor', faqH='Vanliga frågor',
  faq=[('Är det gratis?', 'Ja. Du får 50 kort från Original gratis varje kväll. Temapaketen är engångsköp, Kvällspaketet ger dig ett paket plus Get Fu**ed-nivån, och Busted+ låser upp hela appen med en betalning. Ingen prenumeration.'),
       ('Måste vi dricka?', 'Nej. Slå på alkoholfritt läge så blir varje klunk ett poäng. Och det är alltid okej att stå över.'),
       ('Hur många kan spela?', 'Från 2 till 30. Stora gäng får fler kort som gäller alla samtidigt.'),
       ('Kan vi spela i lag?', 'Ja. Välj duos eller två lag, Röd mot Blå, när ni ställer in spelet. Appen håller koll på ställningen.'),
       ('Vilka språk?', 'Svenska, engelska, danska och norska, med egna kort och menyer. Välj språk på startsidan.'),
       ('När kommer den?', 'Snart till iPhone och Android. Följ @getbusted.se på Instagram och TikTok så får du veta först.')],
  help='Hjälp', privacy='Integritet', contact='Kontakt', foot='För vuxna 18+',
  terms='Villkor', cookies='Cookies', buy='Köp och återbetalning', skip='Hoppa till innehållet', orgno='Org.nr', country='Norge',
  helpTitle='Hjälp - Get Busted', helpDesc='Svar om Get Busted: hur man spelar, återställa köp, lösa in kod, alkoholfritt läge och mer.',
  helpK='Hjälp', helpH='Frågor och svar',
  helpQA=[('Hur spelar man?', 'Skriv in namnen (2 till 30 spelare), välj paket, nivå och hur törstiga ni är. En person är läsare: hen håller i telefonen och läser upp alla kort. Svep eller tryck för nästa kort, och tryck på vänstra kanten av kortet för att gå tillbaka. Läsaren kan bytas, och spelare kan läggas till eller tas bort, när som helst genom att trycka på namnet högst upp.'),
          ('Hur återställer jag mina köp?', 'Öppna Paket i appen och tryck på Återställ köp under «Har du köpt tidigare?». Använd samma Apple-ID eller Google-konto som du köpte med. Du behöver inget konto hos oss.'),
          ('Hur löser jag in en kod?', 'Öppna Paket och tryck på Lös in kod. På iPhone öppnar Apple ett fönster där du skriver in koden. På Android öppnas Google Play så att du kan lösa in den där.'),
          ('Hur funkar alkoholfritt läge?', 'Välj Alkoholfritt när ni ställer in spelet. Det är samma spel, men klunkar blir poäng, och den med flest poäng förlorar. Alla kan spela tillsammans, med eller utan något i glaset.'),
          ('Är texten svår att läsa?', 'Välj Stor text när ni ställer in spelet, eller tryck på Aa under spelet för att byta.'),
          ('Varför 18+?', 'Get Busted är ett festspel för vuxna. Appen ber dig bekräfta att du är 18 år eller äldre första gången du öppnar den. Är du under 18 kan du inte använda appen.'),
          ('Kan jag stå över ett kort?', 'Ja, alltid. Gå bara vidare till nästa kort. Ingen behöver göra något hen inte vill.'),
          ('Något annat?', f'Mejla <a href="mailto:{MAIL}">{MAIL}</a>. Gäller det ett köp, skicka med köpdatum eller kvittot från Apple eller Google.')],
 ),
 'da': dict(
  path='/dk/', lang='da', hero='sv', title='Get Busted - festspillet der styrer aftenen',
  desc='Get Busted er festspillet til spilleaftenen, efterfesten og sommerhuset. 1.000+ kort fra start, med eller uden alkohol. For voksne 18+.',
  og='Én oplæser, 1.000+ kort fra start og ingen kedelige pauser. Til iPhone og Android.',
  nav=[('#how', 'Sådan virker det'), ('#packs', 'Pakker'), ('#faq', 'Spørgsmål')], download='Hent',
  h1='Festspillet der styrer aftenen',
  lead='Én person holder telefonen og læser højt. Resten kigger på hinanden, ikke på en skærm. 1.000+ kort fra start, Rapid-runder, hemmelige missioner og sangkort.',
  soonTo='Snart i', note='For voksne 18+. Kan altid spilles uden alkohol.',
  heroAlt='Get Busted i brug: et kort på en mobilskærm',
  howK='Sådan virker det', howH='Klar på 20 sekunder',
  steps=[('Skriv flokken ind', '2 til 30 spillere. Navnene kommer direkte på kortene, så ingen kan gemme sig.'),
         ('Vælg niveau', 'Mild, Fræk eller Get Fu**ed. Og hvor tørstige I er, fra smagsprøve til rigtig tørstig.'),
         ('Læs højt og spil', 'Oplæseren læser kortene. Terningen, twistene og Rapid-runderne dukker op af sig selv.')],
  featK='Mere end et spil kort', featH='Det kan et almindeligt spil kort ikke',
  feats=[('Nye kort hver måned', 'Fodbold, julefrokost, flykaos og alt det, folk snakker om. De dukker op i appen af sig selv, uden opdatering.'),
         ('Twist', 'Nogle kort vender sig, efter de er læst op. Det, du troede var sikkert, er det ikke.'),
         ('Rapid', 'Fem fingre op. Påstande i træk. Første der er ude, taber.'),
         ('Hemmelige missioner', 'Telefonen går til én spiller, som får en mission, kun vedkommende kender til.'),
         ('Sangkort', 'Sæt sangen på og følg reglen. Ét tryk åbner den i Spotify.'),
         ('Holdspil', 'Spil i faste duoer eller Rød mod Blå. Holddueller undervejs, og appen holder styr på stillingen.'),
         ('Odds', '«Hvad er oddsene for, at du ...?» I tæller begge ned og siger et tal på samme tid.'),
         ('Stor tekst', 'Større bogstaver, der er nemme at læse højt, også i et mørkt rum. Skift med Aa midt i spillet.'),
         ('Aftenen i tal', 'Efter spillet: aftenens mest busted, antal kort og Rapid-runder. Klar til at dele.')],
  packsK='Pakker', packsH='En til enhver anledning',
  packsLead='Fem pakker er klar fra start, og flere kommer hen over efteråret. Prøv 5 kort fra en hvilken som helst pakke gratis, før du køber.',
  packs=[('original', 'cover_original.jpg', 'Original', '50 gratis kort hver aften', None),
         ('halloween', 'cover_halloween.jpg', 'Halloween', 'Udklædning og gyserfilm', None),
         ('jul', 'cover_jul.jpg', 'Jul', 'Julefrokost og nytår', None),
         ('nach', 'cover_nach_da.jpg', 'Efterfest', 'Når klokken er tre', None),
         ('hytta', 'cover_hytta_da.jpg', 'Sommerhuset', 'Vildmarksbad og ingen dækning', None),
         ('reise', 'cover_reise_da.jpg', 'Rejse', 'Charter og billigfly', '2026-11-05'),
         ('student', 'cover_student.jpg', 'Student', 'Rusture og fredagsbar', '2026-11-12'),
         ('utdrikning', 'cover_utdrikning_da.jpg', 'Polterabend', 'For den, der skal giftes', '2026-11-19'),
         ('fotball', 'cover_fotball_da.jpg', 'Fodbold', 'Kampdag og derby', '2026-11-21'),
         ('sport', 'cover_sport.jpg', 'Sport', 'Padel og løbeklubber', '2026-12-03')],
  specialsK='', specialsH='', specials=[],
  soon='Kommer', months=['jan.', 'feb.', 'marts', 'april', 'maj', 'juni', 'juli', 'aug.', 'sep.', 'okt.', 'nov.', 'dec.'],
  prices=[('Gratis', '50 kort fra Original hver aften. Ingen tilmelding.'),
          ('Én pakke', 'Per temapakke, eller Get Fu**ed-niveauet i alle pakker. Engangskøb.'),
          ('Aftenpakke', 'Én pakke du vælger + Get Fu**ed-niveauet, til en lavere pris end hver for sig.'),
          ('Busted+', 'Hele appen: alle pakker, også dem der kommer, Get Fu**ed-niveauet og ubegrænset Original. Betal én gang, intet abonnement. Lanceringspris året ud, til og med december.')],
  respK='Spil smart', respH='Lavet til en god aften, ikke en dårlig morgen',
  resp=[('Max 6', 'Uanset niveau beder et kort aldrig om mere end 6 slurke.'),
        ('Vandpauser', 'De kommer oftere, jo tørstigere I siger, I er.'),
        ('Alkoholfri', 'Samme spil med point i stedet for slurke. Alle kan være med.'),
        ('Spring over', 'Du må altid springe et kort over. Altid.')],
  faqK='Spørgsmål', faqH='Ofte stillede spørgsmål',
  faq=[('Er det gratis?', 'Ja. Du får 50 kort fra Original gratis hver aften. Temapakkerne er engangskøb, Aftenpakken giver dig én pakke plus Get Fu**ed-niveauet, og Busted+ låser hele appen op med én betaling. Intet abonnement.'),
       ('Skal vi drikke?', 'Nej. Slå alkoholfri tilstand til, så bliver hver slurk til et point. Og det er altid i orden at springe over.'),
       ('Hvor mange kan spille?', 'Fra 2 til 30. Store grupper får flere kort, der gælder alle på én gang.'),
       ('Kan vi spille på hold?', 'Ja. Vælg duoer eller to hold, Rød mod Blå, når I sætter spillet op. Appen holder styr på stillingen.'),
       ('Hvilke sprog?', 'Dansk, svensk, engelsk og norsk, med egne kort og menuer. Vælg sprog på startskærmen.'),
       ('Hvornår kommer den?', 'Snart til iPhone og Android.')],
  help='Hjælp', privacy='Privatliv', contact='Kontakt', foot='For voksne 18+',
  terms='Vilkår', cookies='Cookies', buy='Køb og refusion', skip='Spring til indholdet', orgno='Org.nr.', country='Norge',
  helpTitle='Hjælp - Get Busted', helpDesc='Svar om Get Busted: sådan spiller I, gendan køb, indløs kode, alkoholfri tilstand og mere.',
  helpK='Hjælp', helpH='Spørgsmål og svar',
  helpQA=[('Hvordan spiller man?', 'Skriv navnene ind (2 til 30 spillere), og vælg pakker, niveau og hvor tørstige I er. Én person er oplæser: vedkommende holder telefonen og læser alle kortene højt. Swipe eller tryk for næste kort, og tryk i venstre kant af kortet for at gå tilbage. I kan skifte oplæser og tilføje eller fjerne spillere når som helst ved at trykke på navnet øverst.'),
          ('Hvordan gendanner jeg mine køb?', 'Åbn Pakker i appen, og tryk på Gendan køb under «Har du købt før?». Brug det samme Apple-id eller Google-konto, som du købte med. Du behøver ikke en konto hos os.'),
          ('Hvordan indløser jeg en kode?', 'Åbn Pakker, og tryk på Indløs kode. På iPhone åbner Apple et vindue, hvor du skriver koden. På Android åbner Google Play, så du kan indløse den der.'),
          ('Hvordan virker alkoholfri tilstand?', 'Vælg Alkoholfri, når I sætter spillet op. Det er samme spil, men slurke bliver til point, og den med flest point taber. Alle kan spille sammen, med eller uden noget i glasset.'),
          ('Er teksten svær at læse?', 'Vælg Stor tekst, når I sætter spillet op, eller tryk på Aa under spillet for at skifte.'),
          ('Hvorfor 18+?', 'Get Busted er et festspil for voksne. Appen beder dig bekræfte, at du er 18 år eller ældre, første gang du åbner den. Er du under 18, kan du ikke bruge appen.'),
          ('Kan jeg springe et kort over?', 'Ja, altid. Gå bare videre til næste kort. Ingen skal gøre noget, de ikke har lyst til.'),
          ('Noget andet?', f'Skriv til <a href="mailto:{MAIL}">{MAIL}</a>. Gælder det et køb, så send købsdato eller kvitteringen fra Apple eller Google med.')],
 ),
}


# ---------- Grafisk løft (okt 2026): samme stil som getbusted.no, ingen alkohol i markedsføringen ----------
COLORS = {'original': '#B7D147', 'halloween': '#FF8A1F', 'jul': '#E0473E', 'nach': '#8E7CFF', 'hytta': '#C7864A', 'reise': '#3FB8C4',
          'student': '#5B8DEF', 'utdrikning': '#E94B8A', 'fotball': '#3DAE5E', 'sport': '#F26B3A', 'friendsgiving': '#E0892E',
          'paddys': '#2FA84F', 'mello': '#E24AC9', 'midsommar': '#F2C94C', 'kraftskiva': '#E2543B'}
# Antall kort per pakke og språk (fra appens cards.json, okt 2026)
COUNTS = {
 'en': {'original': 345, 'halloween': 152, 'jul': 182, 'reise': 190, 'fotball': 179, 'sport': 179, 'student': 182, 'utdrikning': 185, 'hytta': 177, 'nach': 177, 'friendsgiving': 175, 'paddys': 170},
 'sv': {'original': 380, 'halloween': 168, 'jul': 194, 'reise': 225, 'fotball': 217, 'sport': 217, 'student': 210, 'utdrikning': 212, 'hytta': 175, 'nach': 166, 'mello': 174, 'midsommar': 173, 'kraftskiva': 175},
 'da': {'original': 308, 'halloween': 163, 'jul': 194, 'nach': 177, 'hytta': 173, 'reise': 178, 'student': 180, 'utdrikning': 178, 'fotball': 182, 'sport': 182},
}
# Julekalenderen kommer i en appoppdatering etter 10. november. Sett CAL = True når den er ute.
CAL = False
# Alt-tekst til kortet øverst (samme tekst som står på bildet)
SHOTS_LABEL = {'en': 'Screenshots from the app', 'sv': 'Skärmbilder från appen', 'da': 'Skærmbilleder fra appen'}
HERO_ALT = {
    'en': 'A card from the app: On three, point at the one who would get banished first on The Traitors. Whoever gets the most fingers gets 2 points.',
    'sv': 'Ett kort från appen: På tre - peka på den som skulle åka ut först i Paradise Hotel. Flest pekningar får 2 poäng.',
    'da': 'Et kort fra appen: På tre - peg på den, der ville blive stemt ud først på Paradise Hotel. Den, flest peger på, får 2 point.',
}
# Lanseringsbryteren i season.js bytter tekst på disse (se STORE og LAUNCH der).
FAQ_ATTR = ' data-launch="faq"'
GROUP_ATTR = ' data-launch="group"'
ICONS = ['✨', '🔄', '⚡', '🤫', '🎵', '⚔️', '🎯', '🔠', '📊']
SHOTS = ['3_lag', '4_vri', '5_rapid', '6_odds', '7_stortekst', '8_halloween']
UPDATE = {
 'en': dict(
  desc='Get Busted is the party card game for game nights, house parties and cabin weekends. 1,000+ cards in English at launch, team play, Rapid rounds and secret missions. Adults 18+.',
  og='One reader, 1,000+ cards at launch and zero boring breaks. For iPhone and Android.',
  h1=('The party game that ', 'runs the night', ''),
  lead='One reader holds the phone. Everyone else looks at each other, not at a screen. 1,000+ cards at launch about the internet, the news and your group chat, plus team play, Rapid rounds and secret missions.',
  soonTo='30 October on', note='For adults 18+. Alcohol-free mode is always included.', download='30 October',
  steps=[('Add your crew', '2 to 30 players. Names go straight onto the cards, so nobody gets to hide.'),
         ('Pick packs and level', 'Mild, Cheeky or Get Fu**ed. Play solo, in fixed duos or Red vs Blue.'),
         ('Read out loud and play', 'The reader reads the cards. The dice, the twists and the Rapid rounds show up on their own.')],
  stats=[('1,000+', 'cards in English at launch'), ('5', 'packs at launch, more this autumn'), ('2-30', 'players'), ('Free', 'to get started')],
  shots=['Team play', 'Twists', 'Rapid', 'Odds', 'Big text', 'Halloween'],
  calK='1-24 December · free', calH=('Advent calendar ', 'in the app'), calLead='A new door every day until Christmas. What you open gets mixed into every game until the end of December.',
  calList=['17 new cards: office parties, Christmas stress, home for Christmas and family', 'December rules that last all night', 'New dice sides and a Christmas quiz'],
  groups=['Out on 30 October', 'Autumn and winter', 'Only in English'], cards='cards', freeCards='50 free cards every night',
  priceK='Prices', priceH=('Pay once. ', 'No subscription.'), plusTag='Launch price until the end of December',
  resp=[('Alcohol-free', 'The same game with points. Everyone can join.'), ('Breaks', 'Water breaks and breathers turn up along the way.'),
        ('Skip', 'You can always skip a card. Always.'), ('18+', 'Made for adults. Your crew picks the level.')],
  respH='Made for a good night',
  faq0=('Can everyone join?', 'Yes. In alcohol-free mode everything becomes points, and you can always skip a card.'),
  faqWhen=('When is it out?', '30 October on iPhone and Android. Follow @getbusted.uk on Instagram and TikTok to hear first.'),
  faqCal=('What is the advent calendar?', 'A new door every day from 1 to 24 December, free for everyone. The cards, rules and dice sides you open get mixed into every game until the end of December.'),
  foot='Adults 18+'),
 'sv': dict(
  desc='Get Busted är festspelet för spelkvällen, festen och stugan. 1 000+ kort från start, skrivna för Sverige, lagspel, Rapid och hemliga uppdrag. För vuxna 18+.',
  og='En läsare, 1 000+ kort från start och noll tråkiga pauser. För iPhone och Android.',
  h1=('Festspelet som ', 'tar över', ' kvällen'),
  lead='En person håller i telefonen och läser högt. Resten tittar på varandra, inte på en skärm. 1 000+ kort från start, skrivna för Sverige, inte översatta, plus lagspel, Rapid och hemliga uppdrag.',
  soonTo='30 oktober i', note='För vuxna 18+. Alkoholfritt läge finns alltid med.', download='30 oktober',
  steps=[('Skriv in gänget', '2 till 30 spelare. Namnen hamnar direkt på korten, så ingen kan gömma sig.'),
         ('Välj paket och nivå', 'Mild, Fräck eller Get Fu**ed. Spela var för sig, i fasta duos eller Röd mot Blå.'),
         ('Läs högt och kör', 'Läsaren läser korten. Tärningen, twistarna och Rapid-rundorna dyker upp av sig själva.')],
  stats=[('1 000+', 'kort på svenska från start'), ('5', 'paket från start, fler i höst'), ('2-30', 'spelare'), ('0 kr', 'för att komma igång')],
  shots=['Lagspel', 'Twist', 'Rapid', 'Odds', 'Stor text', 'Halloween'],
  calK='1-24 december · gratis', calH=('Julkalender ', 'i appen'), calLead='Ny lucka varje dag fram till jul. Det ni öppnar blandas in i alla spel december ut.',
  calList=['17 nya kort: julbord, julstress, hem till jul och familjen', 'Decemberregler som gäller hela kvällen', 'Nya sidor på tärningen och ett julquiz'],
  groups=['Ute 30 oktober', 'Hösten och vintern', 'Bara i Sverige'], cards='kort', freeCards='50 gratis kort varje kväll',
  priceK='Priser', priceH=('Betala en gång. ', 'Ingen prenumeration.'), plusTag='Lanseringspris december ut',
  resp=[('Alkoholfritt', 'Samma spel med poäng. Alla kan vara med.'), ('Pauser', 'Vattenpauser och andningspauser dyker upp längs vägen.'),
        ('Stå över', 'Du får alltid stå över ett kort. Alltid.'), ('18+', 'Gjort för vuxna. Gänget väljer nivån.')],
  respH='Gjort för en bra kväll',
  faq0=('Kan alla vara med?', 'Ja. I alkoholfritt läge blir allt poäng, och det är alltid okej att stå över ett kort.'),
  faqWhen=('När kommer den?', '30 oktober till iPhone och Android. Följ @getbusted.se på Instagram och TikTok så får du veta först.'),
  faqCal=('Vad är julkalendern?', 'En ny lucka varje dag 1-24 december, gratis för alla. Korten, reglerna och tärningssidorna ni öppnar blandas in i alla spel december ut.'),
  foot='För vuxna 18+'),
 'da': dict(
  desc='Get Busted er festspillet til spilleaftenen, festen og sommerhuset. 1.000+ danske kort fra start, holdspil, Rapid og hemmelige missioner. For voksne 18+.',
  og='Én oplæser, 1.000+ kort fra start og ingen kedelige pauser. Til iPhone og Android.',
  h1=('Festspillet der ', 'tager over', ' aftenen'),
  lead='Én person holder telefonen og læser højt. Resten kigger på hinanden, ikke på en skærm. 1.000+ kort skrevet på dansk fra start, holdspil, Rapid-runder og hemmelige missioner.',
  soonTo='30. oktober i', note='For voksne 18+. Alkoholfri tilstand er altid med.', download='30. oktober',
  steps=[('Skriv flokken ind', '2 til 30 spillere. Navnene kommer direkte på kortene, så ingen kan gemme sig.'),
         ('Vælg pakker og niveau', 'Mild, Fræk eller Get Fu**ed. Spil hver for sig, i faste par eller Rød mod Blå.'),
         ('Læs højt og spil', 'Oplæseren læser kortene. Terningen, twistene og Rapid-runderne dukker op af sig selv.')],
  stats=[('1.000+', 'kort på dansk fra start'), ('5', 'pakker fra start, flere i efteråret'), ('2-30', 'spillere'), ('0 kr', 'for at komme i gang')],
  shots=['Holdspil', 'Twist', 'Rapid', 'Odds', 'Stor tekst', 'Halloween'],
  calK='1.-24. december · gratis', calH=('Julekalender ', 'i appen'), calLead='Ny låge hver dag til jul. Det, I åbner, blandes ind i alle spil december ud.',
  calList=['17 nye kort: julefrokost, julestress, hjem til jul og familien', 'Decemberregler, der gælder hele aftenen', 'Nye sider på terningen og en julequiz'],
  groups=['Ude 30. oktober', 'Efteråret og vinteren', ''], cards='kort', freeCards='50 gratis kort hver aften',
  packsLead='Fem pakker er klar fra start, og flere kommer hen over efteråret. Prøv 5 kort fra en hvilken som helst pakke gratis, før du køber.',
  priceK='Priser', priceH=('Betal én gang. ', 'Intet abonnement.'), plusTag='Lanceringspris december ud',
  resp=[('Alkoholfri', 'Samme spil med point. Alle kan være med.'), ('Pauser', 'Vandpauser og pustepauser dukker op undervejs.'),
        ('Spring over', 'Du må altid springe et kort over. Altid.'), ('18+', 'Lavet til voksne. Flokken vælger niveauet.')],
  respH='Lavet til en god aften',
  faq0=('Kan alle være med?', 'Ja. I alkoholfri tilstand bliver alt til point, og du må altid springe et kort over.'),
  faqWhen=('Hvornår kommer den?', '30. oktober til iPhone og Android.'),
  faqCal=('Hvad er julekalenderen?', 'En ny låge hver dag 1.-24. december, gratis for alle. Kortene, reglerne og terningsiderne I åbner, blandes ind i alle spil december ud.'),
  foot='For voksne 18+'),
}
for _l, _u in UPDATE.items():
    _t = T[_l]
    for _k in ('desc', 'og', 'lead', 'soonTo', 'note', 'download', 'steps', 'resp', 'respH', 'foot', 'packsLead'):
        if _k in _u: _t[_k] = _u[_k]
    # Ingen drikkespørsmål i FAQ: erstatt «må vi drikke?», og oppdater lanseringsdato, legg til julekalender
    _t['faq'] = [_u['faq0'] if i == 1 else (_u['faqWhen'] if i == len(_t['faq']) - 1 else qa) for i, qa in enumerate(_t['faq'])] + ([_u['faqCal']] if CAL else [])
    _t['u'] = _u

# ---------- Juridiske sider (okt 2026) ----------
# Oversatt og tilpasset fra getbusted.no/_kilde/juridisk.py (norsk er kilden). Samme fakta og løfter på alle språk.
# Forskjell: getbusted.online har ingen statistikk og ingen samtykkeboks, bare språkvalget i localStorage (gb-lang).
M = f'<a href="mailto:{MAIL}">{MAIL}</a>'

def tbl(caption, heads, rows):
    """Tabell som blir kort på mobil: hver celle får kolonnenavnet i data-l."""
    th = ''.join(f'<th scope="col">{h}</th>' for h in heads)
    tr = ''.join('<tr>' + ''.join(f'<td data-l="{h}">{c}</td>' for h, c in zip(heads, r)) + '</tr>' for r in rows)
    return f'<table class="tbl"><caption class="sr">{caption}</caption><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>'

LEGAL = {}

# ===== English (UK-oriented, also EU readers) =====
LEGAL['en'] = dict(updated='Last updated: 7 October 2026')

LEGAL['en']['privacy'] = ('Privacy policy', 'How Get Busted handles personal data in the app and on the websites: no accounts, no ads, no analytics.', 'Privacy', f"""
<h2>In short</h2>
<ul>
  <li>The app has no user accounts, no ads and no analytics tools.</li>
  <li>The names you enter and your settings are stored only on your phone.</li>
  <li>Purchases go through Apple or Google. We use RevenueCat to keep track of which packs you own, with a random ID and no name.</li>
  <li>This website, getbusted.online, has no visitor statistics and no cookies. It only remembers the language you chose.</li>
</ul>

<h2>Who is responsible</h2>
<p>{FIRMA}, org. no. {ORGNR}, {ADDR}, Norway, is the controller for the Get Busted app and the websites getbusted.online and getbusted.no. Contact: {M}.</p>

<h2>The app</h2>
<h3>What is stored on your phone</h3>
<ul>
  <li>Player names, chosen packs, level, language and other settings, so you do not have to enter them again.</li>
  <li>A game in progress, so you can pick up where you left off.</li>
  <li>That you have confirmed you are over 18, and whether you have turned on notifications.</li>
</ul>
<p>This is not sent to us or anyone else, and it is deleted when you delete the app. Please do not use full names or sensitive information about other people as player names: first names or nicknames are enough.</p>

<h3>Purchases</h3>
<p>Purchases are made in the App Store or Google Play. Apple and Google process the payment and are responsible for the information they hold about you. We never receive your name, your email address or your payment details.</p>
<p>To know which packs you own, and so you can restore purchases on a new phone, we use RevenueCat (RevenueCat, Inc., USA) as our processor. RevenueCat receives a random app user ID created by the app, the receipt for the purchase from Apple or Google (which product, when, and the transaction ID) and technical information sent with the request, including IP address, platform and app version. RevenueCat stores data in the USA, and the transfer is based on the EU Standard Contractual Clauses (SCCs). The legal basis is that this is necessary to deliver what you have bought (GDPR Art. 6(1)(b)). The information is kept for as long as you may need to restore your purchases, or until you ask us to delete it.</p>

<h3>New cards from the internet</h3>
<p>The app fetches a file with current cards from getbusted.no. No information about you is sent, but as with any visit to a website, the server (GitHub, see below) sees your phone's IP address.</p>

<h3>Notifications, sharing and ratings</h3>
<ul>
  <li>Notifications are scheduled on your phone. There is no notification server, and you can turn them off in the app or in your phone's settings.</li>
  <li>When you share a card or a summary, the app uses your phone's own share menu. We do not see what you share or with whom.</li>
  <li>The app may ask Apple or Google to show a dialog for rating the app in the store. We do not find out what you answer.</li>
  <li>Song cards may have a button that opens Spotify. Spotify's own terms and privacy policy then apply.</li>
</ul>

<h2>The websites</h2>
<h3>Hosting</h3>
<p>The websites are hosted on GitHub Pages (GitHub, Inc., USA). GitHub logs visitors' IP addresses for security reasons. GitHub is certified under the EU-US Data Privacy Framework. The legal basis is our legitimate interest in delivering the website securely (Art. 6(1)(f)).</p>
<h3>No statistics on getbusted.online</h3>
<p>getbusted.online has no visitor statistics, no analytics tools and no cookies. It only remembers the language you chose, in your browser's local storage, and that is never sent to us. Read more on the <a href="{COOK['en']}">cookies page</a>. The Norwegian site getbusted.no counts visits with Metricool, but only if you say yes to statistics there.</p>
<h3>Fonts and links</h3>
<p>The fonts are on our own server, so nothing is sent to Google or anyone else when the page loads. Links to other services, such as the App Store, Google Play, Instagram or TikTok, only take you there when you tap them.</p>

<h2>Emailing us</h2>
<p>If you write to us, we use your email address and what you write to reply to you and follow up the matter. The legal basis is our legitimate interest in answering enquiries (Art. 6(1)(f)). The email is deleted when the matter is closed, unless we need to keep it, for example in the case of a complaint.</p>

<h2>Age limit</h2>
<p>Get Busted is made for adults over 18. We do not knowingly process information about anyone under 18.</p>

<h2>Your rights</h2>
<p>You have the right to access the information we hold about you, and to have it corrected or deleted. You can also ask us to restrict processing, object to processing based on legitimate interest, receive information you have given us (data portability) and withdraw consent. Write to {M}. We reply within one month.</p>
<p>Since we do not have your name linked to purchases, we need the receipt or order number from Apple or Google to find the right information at RevenueCat.</p>
<p>If you think we process personal data in breach of the rules, you can complain to the Norwegian Data Protection Authority, <a href="https://www.datatilsynet.no/en/">Datatilsynet</a>. If you live in the UK, you can also complain to the <a href="https://ico.org.uk/">Information Commissioner's Office (ICO)</a>, and if you live in the EU, to the data protection authority in your country. We would appreciate it if you contact us first.</p>

<h2>Changes</h2>
<p>If we change how the app or the websites process personal data, we will update this page and the date at the top. If there are significant changes to something you have consented to, we will ask you again.</p>
""")

LEGAL['en']['terms'] = ('Terms of use', 'Terms for the Get Busted app and the websites getbusted.online and getbusted.no.', 'Terms', f"""
<p>These terms apply to the Get Busted app and the websites getbusted.online and getbusted.no. By downloading or using the app, you accept the terms. The terms do not limit the rights you have as a consumer under the law.</p>

<h2>1. Who we are</h2>
<p>Get Busted is provided by {FIRMA}, org. no. {ORGNR}, {ADDR}, Norway. Email: {M}.</p>

<h2>2. Adults 18+ only</h2>
<p>Get Busted is a party game for adults. You must be over 18 to use the app. The game can be played with or without alcohol, and alcohol-free mode (points instead of sips) is always available.</p>

<h2>3. Play responsibly</h2>
<ul>
  <li>Everyone decides for themselves. You can always skip a card, without explaining why.</li>
  <li>Nobody should be pressured into drinking, doing challenges or answering questions they do not want to.</li>
  <li>Play alcohol-free if anyone is pregnant, taking medication that does not mix with alcohol, driving or for any other reason should not drink.</li>
  <li>Follow the law and the rules of the place you are in. Do not do challenges that could harm yourself, others or things around you.</li>
  <li>Only share photos, recordings or summaries of other people if they have said yes.</li>
</ul>
<p>You are responsible for how you and your group use the game. The cards are meant as humour and may feel cheeky, especially on the Get Fu**ed level. Choose a level and packs that suit your group.</p>

<h2>4. Free content and purchases</h2>
<p>The app is free to download and gives you 50 cards from Original for free every night. Theme packs, the Get Fu**ed level, the Night Pack and Busted+ are one-time purchases. There are no subscriptions. The price is shown in the store before you buy, and includes VAT.</p>
<ul>
  <li>Purchases are made in the App Store or Google Play and are also subject to Apple's or Google's terms.</li>
  <li>A purchase gives you a personal right to use the content in the app on the devices linked to the same Apple ID or Google account. The content cannot be resold.</li>
  <li>Busted+ gives access to all packs in the app, including packs that come later, for as long as we offer the app.</li>
  <li>Packs with a later release date are shown as "Coming" and can be bought from the release date. Busted+ unlocks them automatically on the day.</li>
  <li>Purchases can be restored on a new phone with "Restore purchases" in the app.</li>
</ul>
<p>For the right to cancel, refunds and faulty purchases, see <a href="{BUY['en']}">Purchases, cancellation and refunds</a>.</p>

<h2>5. Changes to the app</h2>
<p>We keep developing the app and may add, change or remove cards, features and design. We do not remove content you have paid for unless it is necessary, for example because a card turns out to be offensive or unlawful. In that case we replace it with similar content. Updates may be needed for the app to work.</p>

<h2>6. Rights</h2>
<p>The Get Busted name, the logo, the cards, the texts, the covers and the rest of the content belong to {FIRMA}. You may share single cards and summaries from the app using the share feature. You may not copy the decks, resell the content, make your own versions of the game or use the content commercially without our written consent.</p>

<h2>7. Availability and liability</h2>
<p>We do our best to make the app work, but we cannot promise that it will always be free of errors or available. If something you have bought is faulty, you have the rights described on <a href="{BUY['en']}">Purchases, cancellation and refunds</a>.</p>
<p>We are not liable for damage or loss caused by how the game is used, for example someone drinking too much or a challenge going wrong. This does not apply if the damage is caused by our gross negligence or intent, or where the law does not allow liability to be excluded.</p>

<h2>8. Links to other services</h2>
<p>The app and the websites may link to Spotify, Instagram, TikTok, Facebook, the App Store and Google Play. These services have their own terms, and we are not responsible for them.</p>

<h2>9. Changes to these terms</h2>
<p>We may change these terms, for example when the app gets new features or the law changes. The current version is always here, with the date at the top. We will tell you about significant changes that are to your disadvantage in the app or on the website before they apply.</p>

<h2>10. Governing law and disputes</h2>
<p>Norwegian law applies. If you live in the UK or in another country in the EU/EEA, you keep the mandatory consumer protection you have under the law of the country where you live. If you are unhappy, please contact us first. If we cannot find a solution, you can contact the consumer authorities or the consumer advice service in your country, or take the matter to the courts.</p>
""")

LEGAL['en']['purchases'] = ('Purchases, cancellation and refunds', 'How purchases in Get Busted work: the right to cancel, refunds and faulty purchases.', 'Purchases', f"""
<h2>In short</h2>
<ul>
  <li>All purchases are one-time purchases through the App Store or Google Play. No subscriptions.</li>
  <li>You ask Apple or Google for a refund. On iPhone, Apple gives you 14 days to cancel.</li>
  <li>If something you have bought does not work, we fix it. If we cannot, you are entitled to a price reduction or your money back.</li>
</ul>

<h2>What you buy</h2>
<p>Theme packs, the Get Fu**ed level, the Night Pack (one pack and the Get Fu**ed level) and Busted+ (all packs, including those still to come). The price is shown in the store before you confirm the purchase. The content unlocks as soon as the purchase is confirmed.</p>

<h2>Cancellation and refunds</h2>
<p>Purchases are made in the App Store or Google Play. Apple and Google take the payment and handle refunds, under their own rules:</p>
<ul>
  <li><b>iPhone:</b> Apple gives you 14 days to cancel from when you receive the receipt, without giving a reason. Go to <a href="https://reportaproblem.apple.com/">reportaproblem.apple.com</a>, sign in with your Apple ID, choose the purchase and request a refund.</li>
  <li><b>Android:</b> For the first 48 hours after the purchase, you can request a refund directly in Google Play under <a href="https://play.google.com/store/account/orderhistory">Order history</a>. After that, write to us and we can refund the purchase through Google Play.</li>
</ul>
<p>For digital content that is delivered straight away, the statutory right to cancel does not apply once the download has started with your express consent and you have acknowledged that you lose the right to cancel (in the UK: regulation 37 of the Consumer Contracts (Information, Cancellation and Additional Charges) Regulations 2013; in the EU: the consumer rules in your country). If you bought something by mistake, we will still refund it if you write to us within 14 days. Send the receipt or order number to {M}.</p>

<h2>Faulty purchases</h2>
<p>Content you have bought should work as described. If it is faulty, for example a pack does not unlock or cannot be restored, you have rights under the Consumer Rights Act 2015 if you live in the UK, or under the consumer rules in your country if you live in the EU/EEA. First try "Restore purchases" in the app. If that does not help, write to {M}. We will fix the problem as quickly as we can. If we cannot do so within a reasonable time, you are entitled to a price reduction or your money back.</p>

<h2>Packs not released yet</h2>
<p>Packs with a later release date are shown as "Coming" and cannot be bought individually until they are released. Busted+ gives you access to them automatically on the release date. If a pack is delayed, it unlocks when it arrives. If you have bought Busted+ and an announced pack is not released, you can contact us for a fair price reduction.</p>

<h2>Prices and launch price</h2>
<p>Busted+ has a launch price until 31 December 2026, and a higher price from 1 January 2027. The price you see in the store when you buy is the one that applies. Price changes do not affect what you have already bought.</p>

<h2>Questions and complaints</h2>
<p>Write to {M}. If we cannot agree, you can contact the consumer authorities or the consumer advice service in the country where you live. {FIRMA}, org. no. {ORGNR}, {ADDR}, Norway.</p>
""")

_tbl = tbl('Storage in the browser on getbusted.online', ['Name', 'What and why', 'How long', 'Consent'], [
  ['<code>gb-lang</code>', "Remembers the language you picked in the language menu (EN, SE, DK or NO), so the site shows the right language next time. Stored in the browser's local storage (localStorage), not sent to anyone.", 'Until you clear browser data or pick another language', 'No, strictly necessary'],
])
LEGAL['en']['cookies'] = ('Cookies and local storage', 'What getbusted.online stores in your browser: no cookies, no statistics, only your language choice.', 'Cookies', f"""
<h2>In short</h2>
<p>getbusted.online uses no cookies and no statistics. Your browser only stores the language you chose. That is why there is no consent box on this site.</p>

<h2>What is stored in your browser</h2>
{_tbl}
<p>Storage that is strictly necessary to give you something you have asked for, here the language you chose, does not require consent.</p>

<h2>No statistics</h2>
<p>getbusted.online has no visitor statistics, no analytics tools and no ads. Nothing is loaded that tracks what you do on the site.</p>

<h2>Deleting what is stored</h2>
<p>You can delete the stored language choice by clearing site data for getbusted.online in your browser settings. Next time you open the front page, the site picks the language from your browser's language settings again.</p>

<h2>No other third parties</h2>
<p>The fonts are on our own server, and there are no embedded videos, maps, ads or social media buttons that load content from others. The site is hosted on GitHub Pages, which logs IP addresses for security, see the <a href="{PRIV['en']}">privacy policy</a>.</p>

<h2>getbusted.no</h2>
<p>The Norwegian site getbusted.no also uses no cookies. It counts visits with Metricool (Metricool Software S.L., Spain), but only if you tap "Accept" in the box about statistics there. You can change your choice at any time on <a href="{COOK['no']}">getbusted.no</a>.</p>

<h2>More about privacy</h2>
<p>Read the <a href="{PRIV['en']}">privacy policy</a> to see how we handle personal data in the app and on the websites. Questions: {M}.</p>
""")

# ===== Svenska =====
LEGAL['sv'] = dict(updated='Senast uppdaterad: 7 oktober 2026')

LEGAL['sv']['privacy'] = ('Integritetspolicy', 'Så hanterar Get Busted personuppgifter i appen och på webbplatserna: inga konton, ingen reklam, ingen analys.', 'Integritet', f"""
<h2>Kort sagt</h2>
<ul>
  <li>Appen har inga användarkonton, ingen reklam och inga analysverktyg.</li>
  <li>Namnen ni skriver in och era inställningar sparas bara på telefonen.</li>
  <li>Köp går via Apple eller Google. Vi använder RevenueCat för att hålla koll på vilka paket du äger, med ett slumpmässigt ID utan namn.</li>
  <li>Den här webbplatsen, getbusted.online, har ingen besöksstatistik och inga cookies. Den kommer bara ihåg språket du har valt.</li>
</ul>

<h2>Vem är ansvarig</h2>
<p>{FIRMA}, org.nr {ORGNR}, {ADDR}, Norge, är personuppgiftsansvarig för appen Get Busted och webbplatserna getbusted.online och getbusted.no. Kontakt: {M}.</p>

<h2>Appen</h2>
<h3>Det som sparas på din telefon</h3>
<ul>
  <li>Spelarnamn, valda paket, nivå, språk och andra inställningar, så att ni slipper skriva in dem igen.</li>
  <li>Ett pågående spel, så att ni kan fortsätta där ni slutade.</li>
  <li>Att du har bekräftat att du är över 18 år, och om du har slagit på notiser.</li>
</ul>
<p>Detta skickas inte till oss eller någon annan, och det raderas när du raderar appen. Använd inte fullständiga namn eller känsliga uppgifter om andra som spelarnamn: förnamn eller smeknamn räcker.</p>

<h3>Köp</h3>
<p>Köp görs i App Store eller Google Play. Apple och Google hanterar betalningen och är själva ansvariga för de uppgifter de har om dig. Vi får aldrig ditt namn, din e-postadress eller dina betalningsuppgifter.</p>
<p>För att veta vilka paket du äger, och för att du ska kunna återställa köp på en ny telefon, använder vi RevenueCat (RevenueCat, Inc., USA) som personuppgiftsbiträde. RevenueCat tar emot ett slumpmässigt app-användar-ID som appen skapar, kvittot för köpet från Apple eller Google (vilken produkt, när och transaktions-ID) och teknisk information som följer med förfrågan, bland annat IP-adress, plattform och appversion. RevenueCat lagrar data i USA, och överföringen bygger på EU:s standardavtalsklausuler (SCC). Den rättsliga grunden är att det är nödvändigt för att leverera det du har köpt (dataskyddsförordningen artikel 6.1 b). Uppgifterna sparas så länge du kan behöva återställa dina köp, eller tills du ber oss radera dem.</p>

<h3>Nya kort från nätet</h3>
<p>Appen hämtar en fil med aktuella kort från getbusted.no. Inga uppgifter om dig skickas, men som vid alla besök på en webbplats ser servern (GitHub, se nedan) telefonens IP-adress.</p>

<h3>Notiser, delning och betyg</h3>
<ul>
  <li>Notiser planeras på telefonen. Det finns ingen notisserver, och du kan stänga av dem i appen eller i telefonens inställningar.</li>
  <li>När du delar ett kort eller en sammanfattning använder appen telefonens egen delningsmeny. Vi ser inte vad du delar eller med vem.</li>
  <li>Appen kan be Apple eller Google att visa en ruta för betyg i butiken. Vi får inte veta vad du svarar.</li>
  <li>Låtkort kan ha en knapp som öppnar Spotify. Då gäller Spotifys egna villkor och integritetspolicy.</li>
</ul>

<h2>Webbplatserna</h2>
<h3>Drift</h3>
<p>Webbplatserna ligger hos GitHub Pages (GitHub, Inc., USA). GitHub registrerar besökarnas IP-adresser av säkerhetsskäl. GitHub är certifierat enligt EU-US Data Privacy Framework. Den rättsliga grunden är vårt berättigade intresse av att leverera webbplatsen på ett säkert sätt (artikel 6.1 f).</p>
<h3>Ingen statistik på getbusted.online</h3>
<p>getbusted.online har ingen besöksstatistik, inga analysverktyg och inga cookies. Den kommer bara ihåg språket du har valt, i webbläsarens lokala lagring, och det skickas aldrig till oss. Läs mer på sidan om <a href="{COOK['sv']}">cookies</a>. Den norska webbplatsen getbusted.no räknar besök med Metricool, men bara om du säger ja till statistik där.</p>
<h3>Typsnitt och länkar</h3>
<p>Typsnitten ligger på vår egen server, så ingenting skickas till Google eller andra när sidan laddas. Länkar till andra tjänster, till exempel App Store, Google Play, Instagram eller TikTok, tar dig dit först när du trycker på dem.</p>

<h2>Mejl till oss</h2>
<p>Om du skriver till oss använder vi din e-postadress och det du skriver för att svara dig och följa upp ärendet. Den rättsliga grunden är vårt berättigade intresse av att svara på frågor (artikel 6.1 f). Mejlet raderas när ärendet är avslutat, om vi inte måste spara det, till exempel vid ett klagomål.</p>

<h2>Åldersgräns</h2>
<p>Get Busted är gjort för vuxna över 18 år. Vi behandlar inte medvetet uppgifter om personer under 18 år.</p>

<h2>Dina rättigheter</h2>
<p>Du har rätt att få tillgång till de uppgifter vi har om dig och att få dem rättade eller raderade. Du kan också begära begränsad behandling, invända mot behandling som bygger på berättigat intresse, få ut uppgifter du har gett oss (dataportabilitet) och återkalla samtycke. Skriv till {M}. Vi svarar inom en månad.</p>
<p>Eftersom vi inte har ditt namn kopplat till köp behöver vi kvittot eller ordernumret från Apple eller Google för att hitta rätt uppgifter hos RevenueCat.</p>
<p>Om du anser att vi behandlar personuppgifter i strid med reglerna kan du klaga till den norska dataskyddsmyndigheten, <a href="https://www.datatilsynet.no/en/">Datatilsynet</a>, eller till <a href="https://www.imy.se/">Integritetsskyddsmyndigheten (IMY)</a> i Sverige. Vi uppskattar om du kontaktar oss först.</p>

<h2>Ändringar</h2>
<p>Om vi ändrar hur appen eller webbplatserna behandlar personuppgifter uppdaterar vi den här sidan och datumet högst upp. Vid väsentliga ändringar av något du har samtyckt till frågar vi dig igen.</p>
""")

LEGAL['sv']['terms'] = ('Användarvillkor', 'Villkor för appen Get Busted och webbplatserna getbusted.online och getbusted.no.', 'Villkor', f"""
<p>Dessa villkor gäller för appen Get Busted och webbplatserna getbusted.online och getbusted.no. Genom att ladda ner eller använda appen godkänner du villkoren. Villkoren begränsar inte de rättigheter du har som konsument enligt lag.</p>

<h2>1. Vilka vi är</h2>
<p>Get Busted tillhandahålls av {FIRMA}, org.nr {ORGNR}, {ADDR}, Norge. E-post: {M}.</p>

<h2>2. För vuxna över 18 år</h2>
<p>Get Busted är ett festspel för vuxna. Du måste vara över 18 år för att använda appen. Spelet kan spelas med eller utan alkohol, och alkoholfritt läge (poäng i stället för klunkar) finns alltid.</p>

<h2>3. Spela ansvarsfullt</h2>
<ul>
  <li>Alla bestämmer själva. Det är alltid okej att stå över ett kort, utan att förklara varför.</li>
  <li>Ingen ska pressas att dricka, göra utmaningar eller svara på frågor de inte vill.</li>
  <li>Spela alkoholfritt om någon är gravid, tar mediciner som inte tål alkohol, ska köra eller av andra skäl inte bör dricka.</li>
  <li>Följ lagen och reglerna där ni är. Gör inga utmaningar som kan skada dig själv, andra eller saker runt er.</li>
  <li>Dela bara bilder, inspelningar eller sammanfattningar av andra om de har sagt ja.</li>
</ul>
<p>Du ansvarar själv för hur du och gänget använder spelet. Korten är menade som humor och kan upplevas som fräcka, särskilt på nivån Get Fu**ed. Välj nivå och paket som passar gänget.</p>

<h2>4. Gratis innehåll och köp</h2>
<p>Appen är gratis att ladda ner och ger 50 kort från Original gratis varje kväll. Temapaket, Get Fu**ed-nivån, Kvällspaketet och Busted+ är engångsköp. Det finns ingen prenumeration. Priset står i butiken innan du köper och inkluderar moms.</p>
<ul>
  <li>Köp görs i App Store eller Google Play och följer också Apples eller Googles villkor.</li>
  <li>Ett köp ger dig en personlig rätt att använda innehållet i appen på de enheter som är kopplade till samma Apple-ID eller Google-konto. Innehållet får inte säljas vidare.</li>
  <li>Busted+ ger tillgång till alla paket i appen, även paket som kommer senare, så länge vi erbjuder appen.</li>
  <li>Paket med senare släppdatum visas som «Kommer» och kan köpas från släppdatumet. Busted+ låser upp dem automatiskt på dagen.</li>
  <li>Köp kan återställas på en ny telefon med «Återställ köp» i appen.</li>
</ul>
<p>Om ångerrätt, återbetalning och fel vid köp: se <a href="{BUY['sv']}">Köp, ångerrätt och återbetalning</a>.</p>

<h2>5. Ändringar i appen</h2>
<p>Vi utvecklar appen vidare och kan lägga till, ändra eller ta bort kort, funktioner och design. Vi tar inte bort innehåll du har betalat för, om det inte är nödvändigt, till exempel för att ett kort visar sig vara kränkande eller olagligt. Då ersätter vi det med motsvarande innehåll. Uppdateringar kan behövas för att appen ska fungera.</p>

<h2>6. Rättigheter</h2>
<p>Namnet Get Busted, logotypen, korten, texterna, omslagen och resten av innehållet tillhör {FIRMA}. Du får dela enstaka kort och sammanfattningar från appen med delningsfunktionen. Du får inte kopiera kortlekarna, sälja innehållet vidare, göra egna versioner av spelet eller använda innehållet kommersiellt utan vårt skriftliga samtycke.</p>

<h2>7. Tillgänglighet och ansvar</h2>
<p>Vi gör vårt bästa för att appen ska fungera, men kan inte lova att den alltid är felfri eller tillgänglig. Om något du har köpt är felaktigt har du de rättigheter som står på <a href="{BUY['sv']}">Köp, ångerrätt och återbetalning</a>.</p>
<p>Vi ansvarar inte för skada eller förlust som beror på hur spelet används, till exempel att någon dricker för mycket eller att en utmaning går fel. Detta gäller inte om skadan beror på grov oaktsamhet eller uppsåt från vår sida, eller om ansvarsfriskrivning inte är tillåten enligt lag.</p>

<h2>8. Länkar till andra tjänster</h2>
<p>Appen och webbplatserna kan länka till Spotify, Instagram, TikTok, Facebook, App Store och Google Play. Dessa tjänster har egna villkor, och vi ansvarar inte för dem.</p>

<h2>9. Ändringar i villkoren</h2>
<p>Vi kan ändra villkoren, till exempel när appen får nya funktioner eller lagen ändras. Den gällande versionen finns alltid här, med datum högst upp. Väsentliga ändringar till din nackdel meddelar vi i appen eller på webbplatsen innan de börjar gälla.</p>

<h2>10. Tillämplig lag och tvister</h2>
<p>Norsk lag gäller. Bor du i Sverige eller ett annat land i EU/EES, behåller du det tvingande konsumentskydd du har enligt lagen där du bor. Kontakta oss först om du är missnöjd. Hittar vi ingen lösning kan du som konsument i Sverige vända dig till <a href="https://www.konsumentverket.se/">Konsumentverket</a> och <a href="https://www.arn.se/">Allmänna reklamationsnämnden (ARN)</a>, eller ta saken till domstol.</p>
""")

LEGAL['sv']['purchases'] = ('Köp, ångerrätt och återbetalning', 'Så fungerar köp i Get Busted: ångerrätt, återbetalning och fel vid köp.', 'Köp', f"""
<h2>Kort sagt</h2>
<ul>
  <li>Alla köp är engångsköp via App Store eller Google Play. Ingen prenumeration.</li>
  <li>Återbetalning begär du hos Apple eller Google. På iPhone har du 14 dagars ångerrätt hos Apple.</li>
  <li>Fungerar inte något du har köpt rättar vi felet. Lyckas vi inte har du rätt till prisavdrag eller pengarna tillbaka.</li>
</ul>

<h2>Vad du köper</h2>
<p>Temapaket, Get Fu**ed-nivån, Kvällspaketet (ett paket och Get Fu**ed-nivån) och Busted+ (alla paket, även de som kommer). Priset står i butiken innan du bekräftar köpet. Innehållet låses upp direkt när köpet är bekräftat.</p>

<h2>Ångerrätt och återbetalning</h2>
<p>Köpen görs i App Store eller Google Play. Apple och Google tar emot betalningen och sköter återbetalningen, enligt sina egna regler:</p>
<ul>
  <li><b>iPhone:</b> Apple ger 14 dagars ångerrätt från att du fick kvittot, utan att du behöver ange skäl. Gå till <a href="https://reportaproblem.apple.com/">reportaproblem.apple.com</a>, logga in med ditt Apple-ID, välj köpet och begär återbetalning.</li>
  <li><b>Android:</b> De första 48 timmarna efter köpet kan du begära återbetalning direkt i Google Play under <a href="https://play.google.com/store/account/orderhistory">Beställningshistorik</a>. Efter det kan du skriva till oss, så kan vi återbetala köpet via Google Play.</li>
</ul>
<p>För digitalt innehåll som levereras direkt gäller inte den lagstadgade ångerrätten när leveransen har påbörjats med ditt uttryckliga samtycke och du har bekräftat att ångerrätten då går förlorad (lagen om distansavtal och avtal utanför affärslokaler). Har du köpt något av misstag återbetalar vi det ändå om du skriver till oss inom 14 dagar. Skicka kvittot eller ordernumret till {M}.</p>

<h2>Fel vid köp</h2>
<p>Innehåll du har köpt ska fungera som det är beskrivet. Är det fel, till exempel att ett paket inte låses upp eller inte kan återställas, har du rättigheter enligt lagen (2022:260) om tillhandahållande av digitalt innehåll och digitala tjänster. Prova först «Återställ köp» i appen. Fungerar det inte, skriv till {M}. Vi rättar felet så snabbt vi kan. Klarar vi det inte inom rimlig tid har du rätt till prisavdrag eller att få pengarna tillbaka.</p>

<h2>Paket som inte är släppta än</h2>
<p>Paket med senare släppdatum visas som «Kommer» och kan inte köpas separat förrän de är släppta. Busted+ ger tillgång till dem automatiskt på släppdatumet. Blir ett paket försenat låses det upp när det kommer. Har du köpt Busted+ och ett utlovat paket inte släpps kan du kontakta oss för ett skäligt prisavdrag.</p>

<h2>Priser och lanseringspris</h2>
<p>Busted+ har ett lanseringspris till och med 31 december 2026 och ett högre pris från 1 januari 2027. Det pris du ser i butiken när du köper är det som gäller. Prisändringar påverkar inte det du redan har köpt.</p>

<h2>Frågor och klagomål</h2>
<p>Skriv till {M}. Kommer vi inte överens kan du vända dig till <a href="https://www.konsumentverket.se/">Konsumentverket</a> och <a href="https://www.arn.se/">Allmänna reklamationsnämnden (ARN)</a>. {FIRMA}, org.nr {ORGNR}, {ADDR}, Norge.</p>
""")

_tbl = tbl('Lagring i webbläsaren på getbusted.online', ['Namn', 'Vad och varför', 'Hur länge', 'Samtycke'], [
  ['<code>gb-lang</code>', 'Kommer ihåg språket du valde i språkmenyn (EN, SE, DK eller NO), så att webbplatsen visar rätt språk nästa gång. Sparas i webbläsarens lokala lagring (localStorage), skickas inte till någon.', 'Tills du rensar webbläsardata eller väljer ett annat språk', 'Nej, nödvändig'],
])
LEGAL['sv']['cookies'] = ('Cookies och lokal lagring', 'Vad getbusted.online sparar i din webbläsare: inga cookies, ingen statistik, bara ditt språkval.', 'Cookies', f"""
<h2>Kort sagt</h2>
<p>getbusted.online använder inga cookies och ingen statistik. Webbläsaren sparar bara språket du har valt. Därför finns det ingen samtyckesruta på den här webbplatsen.</p>

<h2>Det som sparas i din webbläsare</h2>
{_tbl}
<p>Lagring som är nödvändig för att ge dig något du har bett om, här språket du valt, kräver inget samtycke.</p>

<h2>Ingen statistik</h2>
<p>getbusted.online har ingen besöksstatistik, inga analysverktyg och ingen reklam. Ingenting laddas som följer vad du gör på webbplatsen.</p>

<h2>Radera det som sparas</h2>
<p>Du kan radera det sparade språkvalet genom att rensa webbplatsdata för getbusted.online i webbläsarens inställningar. Nästa gång du öppnar startsidan väljer webbplatsen språk utifrån webbläsarens språkinställningar igen.</p>

<h2>Inga andra tredje parter</h2>
<p>Typsnitten ligger på vår egen server, och det finns inga inbäddade videor, kartor, reklam eller knappar för sociala medier som laddar innehåll från andra. Webbplatsen ligger hos GitHub Pages, som registrerar IP-adresser av säkerhetsskäl, se <a href="{PRIV['sv']}">integritetspolicyn</a>.</p>

<h2>getbusted.no</h2>
<p>Den norska webbplatsen getbusted.no använder inte heller några cookies. Den räknar besök med Metricool (Metricool Software S.L., Spanien), men bara om du trycker «Godta» i rutan om statistik där. Du kan ändra ditt val när som helst på <a href="{COOK['no']}">getbusted.no</a>.</p>

<h2>Mer om integritet</h2>
<p>Läs <a href="{PRIV['sv']}">integritetspolicyn</a> för att se hur vi behandlar personuppgifter i appen och på webbplatserna. Frågor: {M}.</p>
""")

# ===== Dansk =====
LEGAL['da'] = dict(updated='Sidst opdateret: 7. oktober 2026')

LEGAL['da']['privacy'] = ('Privatlivspolitik', 'Sådan behandler Get Busted personoplysninger i appen og på hjemmesiderne: ingen konti, ingen reklamer, ingen analyse.', 'Privatliv', f"""
<h2>Kort fortalt</h2>
<ul>
  <li>Appen har ingen brugerkonti, ingen reklamer og ingen analyseværktøjer.</li>
  <li>De navne, I skriver ind, og jeres indstillinger gemmes kun på telefonen.</li>
  <li>Køb foregår gennem Apple eller Google. Vi bruger RevenueCat til at holde styr på, hvilke pakker du ejer, med et tilfældigt id uden navn.</li>
  <li>Denne hjemmeside, getbusted.online, har ingen besøgsstatistik og ingen cookies. Den husker kun det sprog, du har valgt.</li>
</ul>

<h2>Hvem er ansvarlig</h2>
<p>{FIRMA}, org.nr. {ORGNR}, {ADDR}, Norge, er dataansvarlig for appen Get Busted og hjemmesiderne getbusted.online og getbusted.no. Kontakt: {M}.</p>

<h2>Appen</h2>
<h3>Det, der gemmes på din telefon</h3>
<ul>
  <li>Spillernavne, valgte pakker, niveau, sprog og andre indstillinger, så I slipper for at skrive dem ind igen.</li>
  <li>Et igangværende spil, så I kan fortsætte, hvor I slap.</li>
  <li>At du har bekræftet, at du er over 18 år, og om du har slået notifikationer til.</li>
</ul>
<p>Det sendes ikke til os eller andre, og det slettes, når du sletter appen. Brug ikke fulde navne eller følsomme oplysninger om andre som spillernavne: fornavne eller kælenavne er nok.</p>

<h3>Køb</h3>
<p>Køb foregår i App Store eller Google Play. Apple og Google behandler betalingen og er selv ansvarlige for de oplysninger, de har om dig. Vi får aldrig dit navn, din e-mailadresse eller dine betalingsoplysninger.</p>
<p>For at vide, hvilke pakker du ejer, og for at du kan gendanne køb på en ny telefon, bruger vi RevenueCat (RevenueCat, Inc., USA) som databehandler. RevenueCat modtager et tilfældigt app-bruger-id, som appen laver, kvitteringen for købet fra Apple eller Google (hvilket produkt, hvornår og transaktions-id) og teknisk information, der følger med forespørgslen, blandt andet IP-adresse, platform og appversion. RevenueCat opbevarer data i USA, og overførslen bygger på EU's standardkontraktbestemmelser (SCC). Behandlingsgrundlaget er, at det er nødvendigt for at levere det, du har købt (databeskyttelsesforordningen artikel 6, stk. 1, litra b). Oplysningerne opbevares, så længe du kan få brug for at gendanne dine køb, eller indtil du beder os slette dem.</p>

<h3>Nye kort fra nettet</h3>
<p>Appen henter en fil med aktuelle kort fra getbusted.no. Der sendes ingen oplysninger om dig, men som ved alle besøg på en hjemmeside ser serveren (GitHub, se nedenfor) telefonens IP-adresse.</p>

<h3>Notifikationer, deling og bedømmelser</h3>
<ul>
  <li>Notifikationer planlægges på telefonen. Der er ingen notifikationsserver, og du kan slå dem fra i appen eller i telefonens indstillinger.</li>
  <li>Når du deler et kort eller en opsummering, bruger appen telefonens egen delingsmenu. Vi ser ikke, hvad du deler, eller med hvem.</li>
  <li>Appen kan bede Apple eller Google om at vise en dialog til bedømmelse i butikken. Vi får ikke at vide, hvad du svarer.</li>
  <li>Sangkort kan have en knap, der åbner Spotify. Så gælder Spotifys egne vilkår og privatlivspolitik.</li>
</ul>

<h2>Hjemmesiderne</h2>
<h3>Drift</h3>
<p>Hjemmesiderne ligger hos GitHub Pages (GitHub, Inc., USA). GitHub registrerer de besøgendes IP-adresser af sikkerhedshensyn. GitHub er certificeret under EU-US Data Privacy Framework. Behandlingsgrundlaget er vores legitime interesse i at levere hjemmesiden sikkert (artikel 6, stk. 1, litra f).</p>
<h3>Ingen statistik på getbusted.online</h3>
<p>getbusted.online har ingen besøgsstatistik, ingen analyseværktøjer og ingen cookies. Den husker kun det sprog, du har valgt, i browserens lokale lager, og det sendes aldrig til os. Læs mere på siden om <a href="{COOK['da']}">cookies</a>. Den norske hjemmeside getbusted.no tæller besøg med Metricool, men kun hvis du siger ja til statistik dér.</p>
<h3>Skrifttyper og links</h3>
<p>Skrifttyperne ligger på vores egen server, så intet sendes til Google eller andre, når siden indlæses. Links til andre tjenester, for eksempel App Store, Google Play, Instagram eller TikTok, sender dig først derhen, når du trykker på dem.</p>

<h2>E-mail til os</h2>
<p>Skriver du til os, bruger vi din e-mailadresse og det, du skriver, til at svare dig og følge op på sagen. Behandlingsgrundlaget er vores legitime interesse i at svare på henvendelser (artikel 6, stk. 1, litra f). E-mailen slettes, når sagen er afsluttet, medmindre vi skal gemme den, for eksempel ved en klage.</p>

<h2>Aldersgrænse</h2>
<p>Get Busted er lavet til voksne over 18 år. Vi behandler ikke bevidst oplysninger om personer under 18 år.</p>

<h2>Dine rettigheder</h2>
<p>Du har ret til indsigt i de oplysninger, vi har om dig, og til at få dem berigtiget eller slettet. Du kan også bede om begrænset behandling, gøre indsigelse mod behandling, der bygger på legitim interesse, få udleveret oplysninger, du har givet os (dataportabilitet), og trække samtykke tilbage. Skriv til {M}. Vi svarer inden for en måned.</p>
<p>Da vi ikke har dit navn knyttet til køb, skal vi bruge kvitteringen eller ordrenummeret fra Apple eller Google for at finde de rigtige oplysninger hos RevenueCat.</p>
<p>Mener du, at vi behandler personoplysninger i strid med reglerne, kan du klage til den norske tilsynsmyndighed, <a href="https://www.datatilsynet.no/en/">Datatilsynet</a>, eller til <a href="https://www.datatilsynet.dk/">Datatilsynet</a> i Danmark. Vi sætter pris på, hvis du kontakter os først.</p>

<h2>Ændringer</h2>
<p>Hvis vi ændrer, hvordan appen eller hjemmesiderne behandler personoplysninger, opdaterer vi denne side og datoen øverst. Ved væsentlige ændringer i noget, du har givet samtykke til, spørger vi dig igen.</p>
""")

LEGAL['da']['terms'] = ('Vilkår for brug', 'Vilkår for appen Get Busted og hjemmesiderne getbusted.online og getbusted.no.', 'Vilkår', f"""
<p>Disse vilkår gælder for appen Get Busted og hjemmesiderne getbusted.online og getbusted.no. Når du henter eller bruger appen, accepterer du vilkårene. Vilkårene begrænser ikke de rettigheder, du har som forbruger efter loven.</p>

<h2>1. Hvem vi er</h2>
<p>Get Busted leveres af {FIRMA}, org.nr. {ORGNR}, {ADDR}, Norge. E-mail: {M}.</p>

<h2>2. For voksne over 18 år</h2>
<p>Get Busted er et festspil for voksne. Du skal være over 18 år for at bruge appen. Spillet kan spilles med eller uden alkohol, og alkoholfri tilstand (point i stedet for slurke) er altid tilgængelig.</p>

<h2>3. Spil ansvarligt</h2>
<ul>
  <li>Alle bestemmer selv. Det er altid i orden at springe et kort over, uden at forklare hvorfor.</li>
  <li>Ingen skal presses til at drikke, lave udfordringer eller svare på spørgsmål, de ikke vil.</li>
  <li>Spil alkoholfrit, hvis nogen er gravide, tager medicin, der ikke tåler alkohol, skal køre eller af andre grunde ikke bør drikke.</li>
  <li>Følg loven og stedets regler. Lav ingen udfordringer, der kan skade dig selv, andre eller ting omkring jer.</li>
  <li>Del kun billeder, optagelser eller opsummeringer af andre, hvis de har sagt ja.</li>
</ul>
<p>Du er selv ansvarlig for, hvordan du og flokken bruger spillet. Kortene er ment som humor og kan opleves som frække, især på niveauet Get Fu**ed. Vælg niveau og pakker, der passer til flokken.</p>

<h2>4. Gratis indhold og køb</h2>
<p>Appen er gratis at hente og giver 50 kort fra Original gratis hver aften. Temapakker, Get Fu**ed-niveauet, Aftenpakken og Busted+ er engangskøb. Der er intet abonnement. Prisen står i butikken, før du køber, og er inklusive moms.</p>
<ul>
  <li>Køb foregår i App Store eller Google Play og følger også Apples eller Googles vilkår.</li>
  <li>Et køb giver dig en personlig ret til at bruge indholdet i appen på de enheder, der er knyttet til samme Apple-id eller Google-konto. Indholdet må ikke sælges videre.</li>
  <li>Busted+ giver adgang til alle pakker i appen, også pakker der kommer senere, så længe vi tilbyder appen.</li>
  <li>Pakker med senere udgivelsesdato vises som «Kommer» og kan købes fra udgivelsesdatoen. Busted+ låser dem op automatisk på dagen.</li>
  <li>Køb kan gendannes på en ny telefon med «Gendan køb» i appen.</li>
</ul>
<p>Om fortrydelsesret, refusion og fejl ved køb: se <a href="{BUY['da']}">Køb, fortrydelsesret og refusion</a>.</p>

<h2>5. Ændringer i appen</h2>
<p>Vi udvikler appen videre og kan tilføje, ændre eller fjerne kort, funktioner og design. Vi fjerner ikke indhold, du har betalt for, medmindre det er nødvendigt, for eksempel fordi et kort viser sig at være krænkende eller ulovligt. Så erstatter vi det med tilsvarende indhold. Opdateringer kan være nødvendige, for at appen virker.</p>

<h2>6. Rettigheder</h2>
<p>Navnet Get Busted, logoet, kortene, teksterne, forsiderne og resten af indholdet tilhører {FIRMA}. Du må dele enkelte kort og opsummeringer fra appen med delingsfunktionen. Du må ikke kopiere kortspillene, sælge indholdet videre, lave egne udgaver af spillet eller bruge indholdet kommercielt uden vores skriftlige samtykke.</p>

<h2>7. Tilgængelighed og ansvar</h2>
<p>Vi gør vores bedste for, at appen virker, men kan ikke love, at den altid er fejlfri eller tilgængelig. Er der fejl ved noget, du har købt, har du de rettigheder, der står på <a href="{BUY['da']}">Køb, fortrydelsesret og refusion</a>.</p>
<p>Vi er ikke ansvarlige for skade eller tab, der skyldes, hvordan spillet bliver brugt, for eksempel at nogen drikker for meget eller laver udfordringer, der går galt. Det gælder ikke, hvis skaden skyldes grov uagtsomhed eller forsæt fra vores side, eller hvis ansvarsfraskrivelse ikke er tilladt efter loven.</p>

<h2>8. Links til andre tjenester</h2>
<p>Appen og hjemmesiderne kan linke til Spotify, Instagram, TikTok, Facebook, App Store og Google Play. Disse tjenester har egne vilkår, og vi er ikke ansvarlige for dem.</p>

<h2>9. Ændringer i vilkårene</h2>
<p>Vi kan ændre vilkårene, for eksempel når appen får nye funktioner, eller loven ændres. Den gældende version står altid her, med dato øverst. Væsentlige ændringer til ulempe for dig giver vi besked om i appen eller på hjemmesiden, før de gælder.</p>

<h2>10. Lovvalg og tvister</h2>
<p>Norsk lov gælder. Bor du i Danmark eller et andet land i EU/EØS, beholder du den ufravigelige forbrugerbeskyttelse, du har efter loven, hvor du bor. Kontakt os først, hvis du er utilfreds. Finder vi ikke en løsning, kan du som forbruger i Danmark klage til <a href="https://naevneneshus.dk/">Nævnenes Hus</a> (Forbrugerklagenævnet), eller indbringe sagen for domstolene.</p>
""")

LEGAL['da']['purchases'] = ('Køb, fortrydelsesret og refusion', 'Sådan fungerer køb i Get Busted: fortrydelsesret, refusion og fejl ved køb.', 'Køb', f"""
<h2>Kort fortalt</h2>
<ul>
  <li>Alle køb er engangskøb gennem App Store eller Google Play. Intet abonnement.</li>
  <li>Refusion søger du om hos Apple eller Google. På iPhone har du 14 dages fortrydelsesret hos Apple.</li>
  <li>Virker noget, du har købt, ikke, retter vi fejlen. Kan vi ikke det, har du krav på afslag i prisen eller pengene tilbage.</li>
</ul>

<h2>Hvad du køber</h2>
<p>Temapakker, Get Fu**ed-niveauet, Aftenpakken (én pakke og Get Fu**ed-niveauet) og Busted+ (alle pakker, også dem der kommer). Prisen står i butikken, før du bekræfter købet. Indholdet låses op, så snart købet er bekræftet.</p>

<h2>Fortrydelsesret og refusion</h2>
<p>Købene foregår i App Store eller Google Play. Apple og Google modtager betalingen og står for tilbagebetaling efter deres egne regler:</p>
<ul>
  <li><b>iPhone:</b> Apple giver 14 dages fortrydelsesret fra du fik kvitteringen, uden at du skal give en grund. Gå til <a href="https://reportaproblem.apple.com/">reportaproblem.apple.com</a>, log ind med dit Apple-id, vælg købet og bed om refusion.</li>
  <li><b>Android:</b> De første 48 timer efter købet kan du bede om refusion direkte i Google Play under <a href="https://play.google.com/store/account/orderhistory">Ordrehistorik</a>. Derefter kan du skrive til os, så kan vi refundere købet gennem Google Play.</li>
</ul>
<p>For digitalt indhold, der leveres med det samme, gælder den lovbestemte fortrydelsesret ikke, når leveringen er begyndt med dit udtrykkelige samtykke, og du har bekræftet, at fortrydelsesretten dermed bortfalder (forbrugeraftaleloven). Har du købt noget ved en fejl, refunderer vi det alligevel, hvis du skriver til os inden for 14 dage. Send kvitteringen eller ordrenummeret til {M}.</p>

<h2>Fejl ved køb</h2>
<p>Indhold, du har købt, skal virke, som det er beskrevet. Er der fejl, for eksempel at en pakke ikke låses op eller ikke kan gendannes, har du rettigheder efter de danske forbrugerregler. Prøv først «Gendan køb» i appen. Virker det ikke, så skriv til {M}. Vi retter fejlen så hurtigt, vi kan. Kan vi ikke det inden for rimelig tid, har du krav på afslag i prisen eller at få pengene tilbage.</p>

<h2>Pakker, der ikke er udgivet endnu</h2>
<p>Pakker med senere udgivelsesdato vises som «Kommer» og kan ikke købes enkeltvis, før de er udgivet. Busted+ giver adgang til dem automatisk på udgivelsesdatoen. Bliver en pakke forsinket, låses den op, når den kommer. Har du købt Busted+, og en annonceret pakke ikke bliver udgivet, kan du kontakte os for et passende afslag i prisen.</p>

<h2>Priser og lanceringspris</h2>
<p>Busted+ har en lanceringspris til og med 31. december 2026 og en højere pris fra 1. januar 2027. Den pris, du ser i butikken, når du køber, er den, der gælder. Prisændringer påvirker ikke det, du allerede har købt.</p>

<h2>Spørgsmål og klager</h2>
<p>Skriv til {M}. Bliver vi ikke enige, kan du klage til <a href="https://naevneneshus.dk/">Nævnenes Hus</a> (Forbrugerklagenævnet). {FIRMA}, org.nr. {ORGNR}, {ADDR}, Norge.</p>
""")

_tbl = tbl('Lagring i browseren på getbusted.online', ['Navn', 'Hvad og hvorfor', 'Hvor længe', 'Samtykke'], [
  ['<code>gb-lang</code>', 'Husker det sprog, du valgte i sprogmenuen (EN, SE, DK eller NO), så hjemmesiden viser det rigtige sprog næste gang. Gemmes i browserens lokale lager (localStorage) og sendes ikke til nogen.', 'Indtil du sletter browserdata eller vælger et andet sprog', 'Nej, nødvendig'],
])
LEGAL['da']['cookies'] = ('Cookies og lokal lagring', 'Hvad getbusted.online gemmer i din browser: ingen cookies, ingen statistik, kun dit sprogvalg.', 'Cookies', f"""
<h2>Kort fortalt</h2>
<p>getbusted.online bruger ingen cookies og ingen statistik. Browseren gemmer kun det sprog, du har valgt. Derfor er der ingen samtykkeboks på denne hjemmeside.</p>

<h2>Det, der gemmes i din browser</h2>
{_tbl}
<p>Lagring, der er nødvendig for at give dig noget, du har bedt om, her det sprog du har valgt, kræver ikke samtykke.</p>

<h2>Ingen statistik</h2>
<p>getbusted.online har ingen besøgsstatistik, ingen analyseværktøjer og ingen reklamer. Der indlæses intet, som følger, hvad du gør på hjemmesiden.</p>

<h2>Slet det, der er gemt</h2>
<p>Du kan slette det gemte sprogvalg ved at rydde webstedsdata for getbusted.online i browserens indstillinger. Næste gang du åbner forsiden, vælger hjemmesiden sprog ud fra browserens sprogindstillinger igen.</p>

<h2>Ingen andre tredjeparter</h2>
<p>Skrifttyperne ligger på vores egen server, og der er ingen indlejrede videoer, kort, reklamer eller knapper til sociale medier, som henter indhold fra andre. Hjemmesiden ligger hos GitHub Pages, som registrerer IP-adresser af sikkerhedshensyn, se <a href="{PRIV['da']}">privatlivspolitikken</a>.</p>

<h2>getbusted.no</h2>
<p>Den norske hjemmeside getbusted.no bruger heller ingen cookies. Den tæller besøg med Metricool (Metricool Software S.L., Spanien), men kun hvis du trykker «Godta» i boksen om statistik dér. Du kan ændre dit valg når som helst på <a href="{COOK['no']}">getbusted.no</a>.</p>

<h2>Mere om privatliv</h2>
<p>Læs <a href="{PRIV['da']}">privatlivspolitikken</a> for at se, hvordan vi behandler personoplysninger i appen og på hjemmesiderne. Spørgsmål: {M}.</p>
""")

LEGAL_KEYS = (('terms', TERMS), ('privacy', PRIV), ('cookies', COOK), ('purchases', BUY))

def label(d, t):
    y, m, dd = d.split('-')
    mon = t['months'][int(m)-1]
    if t['lang'] == 'sv':
        return f"{t['soon']} {int(dd)} {mon}"
    if t['lang'] == 'da':
        return f"{t['soon']} {int(dd)}. {mon}"
    return f"{t['soon']} {mon} {int(dd)}"

def packs(lst, t):
    out = []
    for slug, img, name, sub, rel in lst:
        soon = f"<i class='soon'>{E(label(rel, t))}</i>" if rel else ''
        dr = f" data-release='{rel}'" if rel else ''
        n = COUNTS[t['lang']].get(slug, 0)
        cnt = t['u']['freeCards'] if slug == 'original' else f"{n} {t['u']['cards']}"
        sub = '' if slug == 'original' and sub == t['u']['freeCards'] else sub
        web = img.rsplit('.', 1)[0] + '.webp'
        out.append(f"<div class='pack' data-pack='{slug}'{dr} style='--c:{COLORS.get(slug, '#B7D147')}'><picture><source srcset='/img/{web}' type='image/webp'>"
                   f"<img src='/img/{img}' alt='' width='360' height='503' loading='lazy'></picture><b>{E(name)}</b>"
                   + (f"<span>{E(sub)}</span>" if sub else '') + f"<small>{E(cnt)}</small>{soon}</div>")
    return "\n      ".join(out)

CUR = ' aria-current="page"'

def langbar(t, alt):
    items = [('EN', 'en'), ('SE', 'sv'), ('DK', 'da'), ('NO', 'no')]
    return "<span class='langs'>" + ''.join(
        f"<a href='{alt[l]}' data-lang='{l}'{CUR if l == t['lang'] else ''}>{n}</a>" for n, l in items) + "</span>"

def full(p):
    return p if p.startswith('http') else SITE + p

REDIRECT = """<script>
// Første besøk fra en svensk eller dansk telefon: send til /se/ eller /dk/. Valgt språk huskes.
try { var c = localStorage.getItem('gb-lang'), l = navigator.language || '';
  if (!c && /^sv\\b/i.test(l)) location.replace('/se/');
  else if (!c && /^da\\b/i.test(l)) location.replace('/dk/'); } catch (e) {}
</script>"""

def shell(t, alt, title, desc, body, hreflang_no=True, redirect=False):
    """Felles ramme: head, header og footer. alt = adressene til samme side på hvert språk."""
    url = full(alt[t['lang']])
    langs = LANGS + (['no'] if hreflang_no else [])
    hl = '\n'.join(f'<link rel="alternate" hreflang="{l}" href="{full(alt[l])}">' for l in langs)
    home = t['path']
    nav = ''.join(f"<a href='{home if not redirect else ''}{h}'>{E(n)}</a>" for h, n in t['nav'])
    dl = '#download' if redirect else home + '#download'
    L = t['lang']
    return f"""<!doctype html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(t['og'] if redirect else desc)}">
<meta property="og:image" content="{SITE}/img/og_{t['lang']}.jpg">
<meta property="og:url" content="{url}">
<link rel="canonical" href="{url}">
{hl}
<link rel="alternate" hreflang="x-default" href="{full(alt['en'])}">
<meta name="theme-color" content="#191919">
<link rel="icon" href="/img/favicon.png">
<link rel="apple-touch-icon" href="/img/apple-touch-icon.png">
<link rel="preload" href="/fonts/bsc-900Black_Italic.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/style.css">
<link rel="stylesheet" href="/online.css">
{REDIRECT if redirect and t['lang'] == 'en' else ''}
</head>
<body>
<a class="skip" href="#innhold">{E(t['skip'])}</a>
<header class="nav">
  <div class="wrap">
    <a class="brand" href="{home}"><img src="/img/logo.png" alt="">Get Busted</a>
    <nav>
      {nav}
      {langbar(t, alt)}
      <a class="cta" href="{dl}" data-launch="cta">{E(t['download'])}</a>
    </nav>
  </div>
</header>

<main id="innhold">
{body}
</main>

<footer>
  <div class="wrap">
    <div class="footer-links"><a href="{TERMS[L]}">{E(t['terms'])}</a><a href="{PRIV[L]}">{E(t['privacy'])}</a><a href="{COOK[L]}">{E(t['cookies'])}</a><a href="{BUY[L]}">{E(t['buy'])}</a><a href="{HELP[L]}">{E(t['help'])}</a><a href="mailto:{MAIL}">{E(t['contact'])}</a>{langbar(t, alt)}</div>
    <div class="footer-firma">© 2026 {FIRMA} · {E(t['orgno'])} {ORGNR} · {ADDR}, {E(t['country'])} · {E(t['foot'])}</div>
  </div>
</footer>
<script src="/season.js" defer></script>
<script>
// Språkvalg huskes; «Kommer»-merket forsvinner på slippdagen.
document.querySelectorAll('.langs a').forEach(function (a) {{ a.addEventListener('click', function () {{ try {{ localStorage.setItem('gb-lang', a.dataset.lang); }} catch (e) {{}} }}); }});
var now = Date.now();
document.querySelectorAll('[data-release]').forEach(function (p) {{ if (now >= new Date(p.dataset.release + 'T00:00:00+01:00').getTime()) {{ var s = p.querySelector('.soon'); if (s) s.remove(); }} }});
document.querySelectorAll('[data-until]').forEach(function (el) {{ if (now >= new Date(el.dataset.until + 'T00:00:00+01:00').getTime() + 864e5) el.remove(); }});
</script>
</body>
</html>
"""

def home(t):
    u = t['u']; L = t['lang']
    steps = ''.join(f"<div class='step'><div class='n'>{i}</div><h3>{E(h)}</h3><p>{E(p)}</p></div>" for i, (h, p) in enumerate(t['steps'], 1))
    feats = ''.join(f"<div class='feature'><div class='ic' aria-hidden='true'>{ic}</div><h3>{E(h)}</h3><p>{E(p)}</p></div>" for ic, (h, p) in zip(ICONS, t['feats']))
    shots = ''.join(f"<figure><div class='phone'><picture><source srcset='/img/app_{L}_{f}.webp' type='image/webp'><img src='/img/app_{L}_{f}.jpg' alt='{E(c)}' width='600' height='1304' loading='lazy'></picture></div><figcaption>{E(c)}</figcaption></figure>" for f, c in zip(SHOTS, u['shots']))
    stats = ''.join(f"<div><b>{E(a)}</b><span>{E(b)}</span></div>" for a, b in u['stats'])
    resp = ''.join(f"<div><b>{E(h)}</b><p>{E(p)}</p></div>" for h, p in t['resp'])
    faq = ''.join(f"<details{FAQ_ATTR if (q, a) == u['faqWhen'] else ''}><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q, a in t['faq'])
    doors = ''.join(f"<i class='{'o' if d < 7 else ('t' if d == 7 else '')}'>{d}</i>" for d in range(1, 25))
    cal = ''.join(f"<li>{E(x)}</li>" for x in u['calList'])
    prices = ''.join(f"<div class='price'><h3>{E(h)}</h3><p>{E(p)}</p></div>" for h, p in t['prices'][:3])
    ph, pp = t['prices'][3]
    pp = re.sub(r'\s*[^.]*(aunch price|anseringspris|anceringspris)[^.]*\.', '', pp)
    plus = f"<div class='price plus'><div><h3>{E(ph)}</h3></div><div><p>{E(pp)}</p><span class='tag'>{E(u['plusTag'])}</span></div></div>"
    start = [x for x in t['packs'] if not x[4]]
    later = [x for x in t['packs'] if x[4]]
    groups = [(u['groups'][0], start), (u['groups'][1], later)] + ([(u['groups'][2], t['specials'])] if t['specials'] else [])
    packs_html = ''.join(f"<div class='group'><h3{GROUP_ATTR if i == 0 else ''}>{E(g)}</h3><div class='packs'>\n      {packs(lst, t)}\n    </div></div>" for i, (g, lst) in enumerate(groups))
    jul = 'cover_jul_en.jpg' if L == 'en' else 'cover_jul.jpg'
    h1a, h1b, h1c = u['h1']
    apple = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M16.4 12.6c0-2.6 2.1-3.8 2.2-3.9-1.2-1.8-3.1-2-3.7-2-1.6-.2-3.1.9-3.9.9-.8 0-2-.9-3.4-.9-1.7 0-3.3 1-4.2 2.6-1.8 3.1-.5 7.7 1.3 10.2.8 1.2 1.8 2.6 3.1 2.5 1.3-.1 1.7-.8 3.2-.8s1.9.8 3.2.8c1.3 0 2.2-1.2 3-2.4.9-1.4 1.3-2.7 1.3-2.8-.1 0-2.6-1-2.6-4.2zM13.9 5c.7-.8 1.1-1.9 1-3-1 0-2.1.6-2.8 1.4-.6.7-1.2 1.8-1 2.9 1 .1 2.1-.5 2.8-1.3z"/></svg>'
    play = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3.6 1.8c-.3.3-.4.7-.4 1.3v17.8c0 .6.1 1 .4 1.3l.1.1 10-10v-.2l-10-10.4zM17 15.6l-3.3-3.3v-.2L17 8.7l.1.1 3.9 2.2c1.1.6 1.1 1.7 0 2.3l-3.9 2.2-.1.1zm-.1.1L13.6 12 3.6 22c.4.4 1 .4 1.7.1l11.6-6.4M16.9 8.3 5.3 1.7c-.7-.4-1.3-.3-1.7.1l10 10 3.3-3.5z"/></svg>'
    body = f"""<section class="hero">
  <div class="wrap">
    <div>
      <img class="logo" src="/img/logo.png" alt="Get Busted" width="150" height="150">
      <a class="season-pill" href="#packs" hidden></a>
      <h1>{E(h1a)}<em>{E(h1b)}</em>{E(h1c)}</h1>
      <p class="lead">{E(t['lead'])}</p>
      <div class="badges" id="download">
        <span class="badge" data-store="ios">{apple}<span><small>{E(t['soonTo'])}</small><b>App Store</b></span></span>
        <span class="badge" data-store="play">{play}<span><small>{E(t['soonTo'])}</small><b>Google Play</b></span></span>
      </div>
      <p class="note">{E(t['note'])}</p>
    </div>
    <div class="stage" aria-hidden="true">
      <img class="cover l" src="/img/cover_halloween.jpg" alt="" style="--c:#FF8A1F" width="360" height="503">
      <img class="cover r" src="/img/{jul}" alt="" style="--c:#E0473E" width="360" height="503">
      <picture class="card"><source srcset="/img/card_hero_{L}.webp" type="image/webp"><img src="/img/card_hero_{L}.png" alt="{E(HERO_ALT[t['lang']])}" width="600" height="841"></picture>
    </div>
  </div>
</section>

<div class="wrap"><div class="stats">{stats}</div></div>

<section id="how">
  <div class="wrap">
    <p class="kicker">{E(t['howK'])}</p>
    <h2>{E(t['howH'])}</h2>
    <div class="steps">{steps}</div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <p class="kicker">{E(t['featK'])}</p>
    <h2>{E(t['featH'])}</h2>
    <div class="features">{feats}</div>
    <div class="shots" role="region" tabindex="0" aria-label="{E(SHOTS_LABEL[t['lang']])}">{shots}</div>
  </div>
</section>

<section class="xmas" data-until="2026-12-31"{'' if CAL else ' hidden'}>
  <div class="wrap">
    <div>
      <p class="kicker">{E(u['calK'])}</p>
      <h2>{E(u['calH'][0])}<em>{E(u['calH'][1])}</em></h2>
      <p class="lead">{E(u['calLead'])}</p>
      <ul>{cal}</ul>
    </div>
    <div class="doors" aria-hidden="true">{doors}</div>
  </div>
</section>

<section id="packs">
  <div class="wrap">
    <p class="kicker">{E(t['packsK'])}</p>
    <h2>{E(t['packsH'])}</h2>
    <p class="lead">{E(t['packsLead'])}</p>
    {packs_html}
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <p class="kicker">{E(u['priceK'])}</p>
    <h2>{E(u['priceH'][0])}<em>{E(u['priceH'][1])}</em></h2>
    <div class="pricing three">{prices}{plus}</div>
  </div>
</section>

<section>
  <div class="wrap">
    <p class="kicker">{E(t['respK'])}</p>
    <h2>{E(t['respH'])}</h2>
    <div class="resp">{resp}</div>
  </div>
</section>

<section id="faq" class="alt">
  <div class="wrap" style="max-width:820px">
    <p class="kicker">{E(t['faqK'])}</p>
    <h2>{E(t['faqH'])}</h2>
    {faq}
  </div>
</section>"""
    return shell(t, HOME, t['title'], t['desc'], body, redirect=True)

def help_page(t):
    # Svarene kan inneholde lenker (e-post), derfor ikke escapet.
    qa = '\n  '.join(f"<h2>{E(q)}</h2>\n  <p>{a}</p>" for q, a in t['helpQA'])
    body = f"""<article class="article">
  <p class="kicker">{E(t['helpK'])}</p>
  <h1>{E(t['helpH'])}</h1>
  {qa}
</article>"""
    return shell(t, HELP, t['helpTitle'], t['helpDesc'], body, hreflang_no=False)

def legal_page(t, key, alt):
    """Juridisk side (vilkår, personvern, cookies, kjøp) i samme artikkeloppsett som hjelpesiden."""
    title, desc, kicker, html_body = LEGAL[t['lang']][key]
    body = f"""<article class="article">
  <p class="kicker">{E(kicker)}</p>
  <h1>{E(title)}</h1>
  <p class="meta">{E(LEGAL[t['lang']]['updated'])}</p>
  {html_body.strip()}
</article>"""
    return shell(t, alt, f'{title} - Get Busted', desc, body)

def write(path, text):
    f = ROOT / path.lstrip('/') / 'index.html'
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(text, encoding='utf-8')

for lang in LANGS:
    t = T[lang]
    write(HOME[lang], home(t))
    write(HELP[lang], help_page(t))
    for key, alt in LEGAL_KEYS:
        write(alt[lang], legal_page(t, key, alt))

(ROOT / 'online.css').write_text(""".langs{display:inline-flex;gap:6px;margin:0 6px 0 16px}
.langs a{padding:4px 8px;border:1px solid #555;border-radius:8px;font-weight:800;font-size:13px;letter-spacing:1px;opacity:.75;margin-left:0!important}
.langs a[aria-current]{border-color:#B7D147;color:#B7D147;opacity:1}
footer .langs{margin-left:0}
.pricing.three{grid-template-columns:repeat(3,1fr)}
.price.plus h3{font-size:clamp(40px,5vw,64px);text-shadow:0 0 30px rgba(183,209,71,.4)}
.article h1{overflow-wrap:break-word}
/* Juridiske sider, hopp-lenke og bunntekst (samme regler som style.css på getbusted.no) */
:focus-visible{outline:3px solid var(--lime);outline-offset:3px;border-radius:6px}
.skip{position:absolute;left:12px;top:-60px;z-index:100;background:var(--lime);color:#1E1E1E;padding:10px 16px;border-radius:10px;font-weight:800;text-decoration:none}
.skip:focus{top:12px}
.sr{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;border:0}
.article h3{font-size:20px;margin:22px 0 6px;color:var(--fg)}
.article a{color:var(--lime)}
.article p+p,.article ul+p,.article p+ul,.article table+p{margin-top:10px}
.tbl{width:100%;border-collapse:collapse;margin:12px 0 8px;font-size:15px}
.tbl th,.tbl td{text-align:left;vertical-align:top;padding:10px 8px;border-bottom:1px solid var(--line);color:var(--muted)}
.tbl th,.tbl code{color:var(--fg)}
@media (max-width:640px){.tbl,.tbl tbody,.tbl tr,.tbl td{display:block;width:100%}.tbl thead{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}.tbl tr{border-bottom:1px solid var(--line);padding:8px 0}.tbl td{border:0;padding:4px 0}.tbl td::before{content:attr(data-l);display:block;color:var(--fg);font-weight:700}}
footer .footer-links a{margin-bottom:8px}
footer .footer-firma{color:var(--muted)}
@media (max-width:900px){.pricing.three{grid-template-columns:1fr}}
@media (max-width:760px){.nav nav .langs{display:inline-flex;margin:0 4px}.nav nav .langs a{display:inline-block}.nav nav a.cta{display:none}.nav .brand{white-space:nowrap;font-size:19px}.nav .brand img{width:34px;height:34px}.langs a{padding:4px 6px}}
""", encoding='utf-8')
(ROOT / 'CNAME').write_text('getbusted.online\n')
# Gamle adresser sender videre: /da/ til /dk/ og /sv/ til /se/
for _old, _new in (('/da/', '/dk/'), ('/da/hjaelp/', '/dk/hjaelp/'), ('/da/privatliv/', '/dk/privatliv/'),
                   ('/sv/', '/se/'), ('/sv/hjalp/', '/se/hjalp/'), ('/sv/integritet/', '/se/integritet/')):
    write(_old, f"<!doctype html><meta charset='utf-8'><title>Get Busted</title><link rel='canonical' href='{SITE}{_new}'><meta http-equiv='refresh' content='0;url={_new}'><a href='{_new}'>Get Busted</a>\n")
(ROOT / 'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: https://getbusted.online/sitemap.xml\n')

# Sitemap med hreflang mellom språkene. Norsk hjelpeside finnes ikke, så hjelpesidene lenker bare en/sv/da.
def sm_entry(loc, alt, langs):
    links = ''.join(f'\n  <xhtml:link rel="alternate" hreflang="{l}" href="{full(alt[l])}"/>' for l in langs)
    return f'<url>\n  <loc>{full(loc)}</loc>{links}\n  <xhtml:link rel="alternate" hreflang="x-default" href="{full(alt["en"])}"/>\n</url>'
entries = []
for alt, langs in ((HOME, LANGS + ['no']), (HELP, LANGS), (PRIV, LANGS + ['no']), (TERMS, LANGS + ['no']), (COOK, LANGS + ['no']), (BUY, LANGS + ['no'])):
    for l in LANGS:
        entries.append(sm_entry(alt[l], alt, langs))
(ROOT / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + '\n'.join(entries) + '\n</urlset>\n', encoding='utf-8')
(ROOT / '404.html').write_text("<!doctype html><meta charset='utf-8'><title>Get Busted</title><meta http-equiv='refresh' content='0;url=/'><a href='/'>Get Busted</a>\n")
print('ok')
