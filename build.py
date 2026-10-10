# Bygger getbusted.online: engelsk på /, svensk på /se/ og dansk på /dk/ (/sv/ og /da/ sender videre). Norsk ligger på getbusted.no.
# Hver språkblokk gir forside, hjelpeside og juridiske sider (vilkår, personvern, cookies, kjøp). Juridisk tekst står i LEGAL, oversatt fra getbusted.no/_kilde/juridisk.py.
# Kjør: python3 build.py
import html, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent / '_kilde'))
from heltekort import hero_card_html  # heltekortet i hero (kortliste og tekster: _kilde/heltekort.py)
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
FIRMA, ORGNR, ADDR = 'Snikkerbua Holding AS', '927 118 300', 'Voldgata 27, 2000 Lillestrøm'

# Ingen priser og ingen lanseringspris på en/sv/da (utenlandske priser er ikke vedtatt). Norske priser står bare på getbusted.no.
PRICE_TXT = {
  'en': 'The price you see in the store when you buy is the one that applies. Price changes do not affect what you have already bought.',
  'sv': 'Priset som visas i butiken när du köper är det som gäller. Prisändringar påverkar inte det du redan har köpt.',
  'da': 'Den pris, du ser i butikken, når du køber, er den, der gælder. Prisændringer påvirker ikke det, du allerede har købt.',
}
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
  featK='More than just cards', featH='Things only a phone can do',
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
         ('reise', 'cover_reise_en.jpg', 'Travel', 'Budget airlines and flings', True),
         ('student', 'cover_student.jpg', 'Student', "Freshers' and house parties", True),
         ('utdrikning', 'cover_utdrikning_en.jpg', 'Stag & Hen', 'For the one getting married', True),
         ('fotball', 'cover_fotball_en.jpg', 'Football', 'Match day and fantasy drama', True),
         ('sport', 'cover_sport.jpg', 'Sport', 'Run clubs and padel losers', True)],
  specialsK='Seasonal specials', specialsH='Only in English',
  specials=[('friendsgiving', 'cover_friendsgiving.jpg', 'Friendsgiving', 'Potluck and turkey disasters', True),
            ('paddys', 'cover_paddys.jpg', "St. Paddy's", 'Green, the craic and the Irish exit', True)],
  soon='Coming soon', months=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
  prices=[('Free', '50 cards from Original every night. No sign-up.'),
          ('One pack', 'Per theme pack, or the Get Fu**ed level across every pack. One-time purchase.'),
          ('Night Pack', 'One pack of your choice + the Get Fu**ed level, for less than buying them separately.'),
          ('Busted+', 'The whole app: every pack, including future ones, the Get Fu**ed level and unlimited Original. Pay once, no subscription.')],
  respK='Play smart', respH='Made for a good night, not a bad morning',
  resp=[('Max 6', 'Whatever the level, a card never asks for more than 6 sips.'),
        ('Water breaks', 'They come more often the thirstier you say you are.'),
        ('Alcohol-free', 'The same game with points instead of sips. Everyone can join.'),
        ('Skip', 'You can always skip a card. Always.')],
  faqK='Questions', faqH='FAQ',
  faq=[('Is it free?', 'Yes. You get 50 cards from Original for free every night. Theme packs are one-time purchases, the Night Pack gets you one pack plus the Get Fu**ed level, and Busted+ unlocks the whole app with one payment. No subscription.'),
       ('Do we have to drink?', 'No. Turn on alcohol-free mode and every sip becomes a point. And skipping is always allowed.'),
       ('How many can play?', 'From 2 to 30. Big groups get more cards that apply to everyone at once.'),
       ('Can we play in teams?', 'Yes. Pick duos or two teams, Red vs Blue, when you set up the game. The app keeps the score.'),
       ('Which languages?', 'English, Swedish, Danish and Norwegian, each with its own cards and menus. Pick the language on the start screen.'),
       ('When is it out?', 'Soon on iPhone and Android. Follow @getbusted.uk on Instagram and TikTok to hear first.')],
  help='Help', privacy='Privacy', contact='Contact', foot='Adults 18+',
  terms='Terms of use', cookies='Cookies', buy='Purchases & refunds', skip='Skip to content', orgno='Org. no.', country='Norway',
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
  path='/se/', lang='sv', hero='sv', title='Get Busted - partyspelet som tar över kvällen',
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
  featK='Mer än bara kort', featH='Sånt bara en app kan',
  feats=[('Skrivet för Sverige', 'Swish, BankID, mello, Bajen och Gnaget, kräftor och Små grodorna. Nya aktuella kort varje månad, utan uppdatering.'),
         ('Twistar', 'Vissa kort vänder sig efter att de lästs upp. Det du trodde var säkert, är det inte.'),
         ('Rapid', 'Fem fingrar upp. Påståenden i rad. Först ute förlorar.'),
         ('Hemliga uppdrag', 'Telefonen går till en spelare, som får ett uppdrag som bara hen känner till.'),
         ('Låtkort', 'Sätt på låten och följ regeln. Ett tryck öppnar den i Spotify.'),
         ('Lagspel', 'Spela i fasta duos eller Röd mot Blå. Lagdueller längs vägen, och appen håller koll på ställningen.'),
         ('Odds', '«Vad är oddsen att du ...?» Båda räknar ner och säger ett tal samtidigt.'),
         ('Stor text', 'Större bokstäver som är lätta att läsa högt, även i ett mörkt rum. Byt med Aa mitt i spelet.'),
         ('Kvällen i siffror', 'Efter spelet: kvällens mest avslöjade, antal kort och Rapid-rundor. Klart att dela.')],
  packsK='Paket', packsH='Ett för varje tillfälle',
  packsLead='Varje paket har egna svenska kort, skrivna i Sverige för svenskar. Testa 5 kort från valfritt paket gratis innan du köper.',
  packs=[('original', 'cover_original.jpg', 'Original', '50 gratis kort varje kväll', None),
         ('halloween', 'cover_halloween.jpg', 'Halloween', 'Maskerad och skräckfilm', None),
         ('jul', 'cover_jul.jpg', 'Jul', 'Julbord och Kalle Anka', None),
         ('nach', 'cover_nach_sv.jpg', 'Efterfest', 'När klockan är tre', None),
         ('hytta', 'cover_hytta_sv.jpg', 'Stugan', 'Bastu och noll täckning', None),
         ('reise', 'cover_reise_sv.jpg', 'Resa', 'Charter och Finlandsbåten', True),
         ('student', 'cover_student.jpg', 'Student', 'Nollning och sittningar', True),
         ('utdrikning', 'cover_utdrikning_sv.jpg', 'Svensexa & möhippa', 'För den som ska gifta sig', True),
         ('fotball', 'cover_fotball_sv.jpg', 'Fotboll', 'Allsvenskan och derby', True),
         ('sport', 'cover_sport.jpg', 'Sport', 'Padel och Vasaloppet', True)],
  specialsK='Bara i Sverige', specialsH='Paket för svenska högtider',
  specials=[('mello', 'cover_mello.jpg', 'Mello', 'Sex lördagar och en final', True),
            ('midsommar', 'cover_midsommar.jpg', 'Midsommar', 'Sill, jordgubbar och regn', True),
            ('kraftskiva', 'cover_kraftskiva.jpg', 'Kräftskiva', 'Pappershattar och allsång', True)],
  soon='Kommer snart', months=['jan', 'feb', 'mars', 'april', 'maj', 'juni', 'juli', 'aug', 'sep', 'okt', 'nov', 'dec'],
  prices=[('Gratis', '50 kort från Original varje kväll. Ingen registrering.'),
          ('Ett paket', 'Per temapaket, eller Get Fu**ed-nivån i alla paket. Engångsköp.'),
          ('Kvällspaket', 'Ett paket du väljer + Get Fu**ed-nivån, till lägre pris än var för sig.'),
          ('Busted+', 'Hela appen: alla paket, även de som kommer, Get Fu**ed-nivån och obegränsat Original. Betala en gång, ingen prenumeration.')],
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
  terms='Användarvillkor', cookies='Cookies', buy='Köpvillkor och ångerrätt', skip='Hoppa till innehållet', orgno='Org.nr', country='Norge',
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
  path='/dk/', lang='da', hero='sv', title='Get Busted - festspillet, der tager over aftenen',
  desc='Get Busted er festspillet til spilleaftenen, efterfesten og sommerhuset. 1.000+ kort fra start, med eller uden alkohol. For voksne 18+.',
  og='Én oplæser, 1.000+ kort fra start og ingen kedelige pauser. Til iPhone og Android.',
  nav=[('#how', 'Sådan virker det'), ('#packs', 'Pakker'), ('#faq', 'Spørgsmål')], download='Hent',
  h1='Festspillet der styrer aftenen',
  lead='Én person holder telefonen og læser højt. Resten kigger på hinanden, ikke på en skærm. 1.000+ kort fra start, Rapid-runder, hemmelige missioner og sangkort.',
  soonTo='Snart i', note='For voksne 18+. Kan altid spilles uden alkohol.',
  heroAlt='Get Busted i brug: et kort på en mobilskærm',
  howK='Sådan virker det', howH='Klar på 20 sekunder',
  steps=[('Skriv spillerne ind', '2 til 30 spillere. Navnene kommer direkte på kortene, så ingen kan gemme sig.'),
         ('Vælg niveau', 'Mild, Fræk eller Get Fu**ed. Og hvor tørstige I er, fra smagsprøve til rigtig tørstig.'),
         ('Læs højt og spil', 'Oplæseren læser kortene. Terningen, twistene og Rapid-runderne dukker op af sig selv.')],
  featK='Mere end bare kort', featH='Det kan kun en app',
  feats=[('Nye kort hver måned', 'Fodbold, julefrokost, flykaos og alt det, folk snakker om. De dukker op i appen af sig selv, uden opdatering.'),
         ('Twist', 'Nogle kort vender, når de er læst op. Det, du troede, var sikkert, er det ikke.'),
         ('Rapid', 'Fem fingre op. Påstande i træk. Første der er ude, taber.'),
         ('Hemmelige missioner', 'Telefonen går til én spiller, der får en hemmelig mission, som kun vedkommende kender.'),
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
         ('reise', 'cover_reise_da.jpg', 'Rejse', 'Charter og billigfly', True),
         ('student', 'cover_student.jpg', 'Student', 'Rusture og fredagsbar', True),
         ('utdrikning', 'cover_utdrikning_da.jpg', 'Polterabend', 'For den, der skal giftes', True),
         ('fotball', 'cover_fotball_da.jpg', 'Fodbold', 'Kampdag og derby', True),
         ('sport', 'cover_sport.jpg', 'Sport', 'Padel og løbeklubber', True)],
  specialsK='', specialsH='', specials=[],
  soon='Kommer snart', months=['jan.', 'feb.', 'marts', 'april', 'maj', 'juni', 'juli', 'aug.', 'sep.', 'okt.', 'nov.', 'dec.'],
  prices=[('Gratis', '50 kort fra Original hver aften. Ingen tilmelding.'),
          ('Én pakke', 'Per temapakke, eller Get Fu**ed-niveauet i alle pakker. Engangskøb.'),
          ('Aftenpakke', 'Én pakke du vælger + Get Fu**ed-niveauet, til en lavere pris end hver for sig.'),
          ('Busted+', 'Hele appen: alle pakker, også dem der kommer, Get Fu**ed-niveauet og ubegrænset Original. Betal én gang, intet abonnement.')],
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
  terms='Brugsvilkår', cookies='Cookies', buy='Køb og refusion', skip='Gå til indholdet', orgno='Org.nr.', country='Norge',
  helpTitle='Hjælp - Get Busted', helpDesc='Svar om Get Busted: sådan spiller I, gendan køb, indløs kode, alkoholfri tilstand og mere.',
  helpK='Hjælp', helpH='Spørgsmål og svar',
  helpQA=[('Hvordan spiller man?', 'Skriv navnene ind (2 til 30 spillere), og vælg pakker, niveau og hvor tørstige I er. Én person er oplæser: vedkommende holder telefonen og læser alle kortene højt. Swipe eller tryk for næste kort, og tryk i venstre kant af kortet for at gå tilbage. I kan skifte oplæser og tilføje eller fjerne spillere når som helst ved at trykke på navnet øverst.'),
          ('Hvordan gendanner jeg mine køb?', 'Åbn Pakker i appen, og tryk på Gendan køb under «Har du købt før?». Brug den samme Apple-konto eller Google-konto, som du købte med. Du behøver ikke en konto hos os.'),
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
    'sv': 'Ett kort från appen: På tre - peka på den som skulle åka ut först i Paradise Hotel. Den med flest pekningar får 2 poäng.',
    'da': 'Et kort fra appen: På tre - peg på den, der ville blive stemt ud først på Paradise Hotel. Den, flest peger på, får 2 point.',
}

# Eksempelkort på forsiden (fra appens cards.json på test-bygg, okt 2026). Bare kort uten alkoholord og uten straff.
# Navnene er oppdiktet og brukes ikke andre steder.
SAMPLES = {
 'en': dict(k='A taste', h=('Cards from ', 'the app'), lead='A few picks from the packs out at launch. The names get swapped for your crew.',
  cards=[('original', 'Original', 'On three, point at the one who', 'would get scammed by a deepfake of their own mum'),
         ('jul', 'Christmas', 'On three, point at the one who', 'will lose Whamageddon first this year'),
         ('hytta', 'The Cabin', 'On three, point at the one who', 'sends the Splitwise request before the car is even unpacked'),
         ('halloween', 'Halloween', 'On three, point at the one who', 'would say “I’m not scared, I’m just cold” to get an arm round them'),
         ('nach', 'Afterparty', 'On three, point at the one who', 'texts “home safe x” first and gets home last'),
         ('original', 'Original', 'On three, point at the one who', 'nods along to crypto talk without understanding a single word'),
         ('original', 'Original', 'Truth', 'Rory: what’s the longest situationship you’ve been in, and how did it end?'),
         ('original', 'Original', 'Secret mission', 'Get someone to ask you “what’s wrong with you?” before the next dice roll.')]),
 'sv': dict(k='Smakprov', h=('Kort från ', 'appen'), lead='Ett litet urval ur paketen som finns från start. Namnen byts mot ert gäng.',
  cards=[('jul', 'Jul', 'På tre - peka på den som', 'somnar först i soffan under Kalle Anka'),
         ('original', 'Original', 'På tre - peka på den som', 'beställer för två på Max klockan tre och äter upp allt själv'),
         ('hytta', 'Stugan', 'På tre - peka på den som', 'frågar efter wifi-lösenordet i en stuga utan rinnande vatten'),
         ('halloween', 'Halloween', 'På tre - peka på den som', 'tycker att halloween är amerikanskt trams men är mest utklädd ändå'),
         ('nach', 'Efterfest', 'På tre - peka på den som', 'har de mest kaotiska DM:en efter klockan tre'),
         ('jul', 'Jul', 'På tre - peka på den som', 'säger ”vi borde ses i mellandagarna” och aldrig hör av sig'),
         ('original', 'Original', 'Sanning', 'Signe: vilken Mellolåt kan du hela texten till?'),
         ('original', 'Original', 'Hemligt uppdrag', 'Få gänget att börja prata bostadspriser före nästa tärningsslag.')]),
 'da': dict(k='Smagsprøver', h=('Kort fra ', 'appen'), lead='Et lille udvalg fra pakkerne, der er klar fra start. Navnene bliver skiftet ud med jeres.',
  cards=[('original', 'Original', 'På tre - peg på den, der', 'regner fællesspisningen ud på MobilePay ned til 50 øre'),
         ('jul', 'Jul', 'På tre - peg på den, der', 'græder til Fra alle os til alle jer'),
         ('hytta', 'Sommerhuset', 'På tre - peg på den, der', 'ikke kan tænde op i brændeovnen, men nægter at få hjælp'),
         ('halloween', 'Halloween', 'På tre - peg på den, der', 'ville græde i et gyserhus på Bakken'),
         ('nach', 'Efterfest', 'På tre - peg på den, der', 'ville tænde loftslyset for at smide os alle ud'),
         ('original', 'Original', 'På tre - peg på den, der', 'råber mest ad folk på cykelstien'),
         ('original', 'Original', 'Sandhed', 'Asger: hvem i rummet ville du ringe til, hvis du stod på Roskilde uden telt, penge og telefon?'),
         ('original', 'Original', 'Hemmelig mission', 'Få to andre til at diskutere cykelhjelm, før næste terningslag.')]),
}

def samples_html(L):
    sm = SAMPLES[L]
    cards = ''.join(f"<figure class='sample' style='--c:{COLORS[pk]}'><figcaption>{E(pn)}</figcaption><p class='sample-head'>{E(hd)}</p><blockquote>{E(tx)}</blockquote></figure>" for pk, pn, hd, tx in sm['cards'])
    return f"""<section id="cards">
  <div class="wrap">
    <p class="kicker">{E(sm['k'])}</p>
    <h2>{E(sm['h'][0])}<em>{E(sm['h'][1])}</em></h2>
    <p class="lead">{E(sm['lead'])}</p>
    <div class="samples">{cards}</div>
    {lp_links(L)}
  </div>
</section>"""

# Strukturert data (schema.org) for Google og AI-søk: organisasjon, appen og FAQ-en som står på siden.
import json as _json
def jsonld(t):
    L = t['lang']; url = full(HOME[L])
    org = {'@type': 'Organization', '@id': 'https://getbusted.no/#org', 'name': 'Get Busted', 'url': 'https://getbusted.no/',
           'logo': 'https://getbusted.no/img/logo.png', 'email': MAIL,
           'parentOrganization': {'@type': 'Organization', 'name': 'Snikkerbua Holding AS', 'identifier': '927 118 300'},
           'sameAs': ['https://www.instagram.com/getbusted.no/', 'https://www.tiktok.com/@getbusted.no', 'https://www.facebook.com/getbusted.no']}
    app = {'@type': 'MobileApplication', '@id': url + '#app', 'name': 'Get Busted', 'url': url, 'inLanguage': L,
           'description': t['desc'], 'applicationCategory': 'GameApplication', 'applicationSubCategory': 'Party game',
           'operatingSystem': 'iOS, Android', 'contentRating': '18+', 'publisher': {'@id': 'https://getbusted.no/#org'},
           'image': f'{SITE}/img/og_{L}.jpg',
           'offers': {'@type': 'Offer', 'price': '0', 'priceCurrency': 'NOK', 'description': t['prices'][0][1]}}
    faq = {'@type': 'FAQPage', '@id': url + '#faq', 'inLanguage': L,
           'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': re.sub('<[^>]+>', '', a)}} for q, a in t['faq']]}
    data = {'@context': 'https://schema.org', '@graph': [org, app, faq]}
    return '<script type="application/ld+json">' + _json.dumps(data, ensure_ascii=False).replace('</', '<\\/') + '</script>'

# Lanseringsbryteren i season.js bytter tekst på disse (se STORE og LAUNCH der).
FAQ_ATTR = ' data-launch="faq"'
GROUP_ATTR = ' data-launch="group"'
ICONS = ['✨', '🔄', '⚡', '🤫', '🎵', '⚔️', '🎯', '🔠', '📊']
SHOTS = ['3_lag', '4_vri', '5_rapid', '6_odds', '7_stortekst', '8_halloween']
UPDATE = {
 'en': dict(
  desc='Get Busted is the party card game for game nights, house parties, stag and hen dos and cabin weekends. 1,000+ cards in English at launch, team play, Rapid rounds and secret missions. Adults 18+.',
  og='One reader, 1,000+ cards at launch and zero boring breaks. For iPhone and Android.',
  h1=('The party game that ', 'runs the night', ''),
  lead='One reader holds the phone. Everyone else looks at each other, not at a screen. 1,000+ cards at launch about the internet, the news and your group chat, plus team play, Rapid rounds and secret missions.',
  soonTo='Coming soon to', note='For adults 18+. Alcohol-free mode is always included.', download='Coming soon',
  steps=[('Add your crew', '2 to 30 players. Names go straight onto the cards, so nobody gets to hide.'),
         ('Pick packs and level', 'Mild, Cheeky or Get Fu**ed. Play solo, in fixed duos or Red vs Blue.'),
         ('Read out loud and play', 'The reader reads the cards. The dice, the twists and the Rapid rounds show up on their own.')],
  stats=[('1,000+', 'cards in English at launch'), ('5', 'packs at launch, more this autumn'), ('2-30', 'players'), ('Free', 'to get started')],
  shots=['Team play', 'Twists', 'Rapid', 'Odds', 'Big text', 'Halloween'],
  calK='1-24 December · free', calH=('Advent calendar ', 'in the app'), calLead='A new door every day until Christmas. What you open gets mixed into every game until the end of December.',
  calList=['17 new cards: office parties, Christmas stress, home for Christmas and family', 'December rules that last all night', 'New dice sides and a Christmas quiz'],
  groups=['At launch', 'Autumn and winter', 'Only in English'], cards='cards', freeCards='50 free cards every night',
  priceK='Buying', priceH=('Pay once. ', 'No subscription.'), plusTag='',
  resp=[('Alcohol-free', 'The same game with points. Everyone can join.'), ('Breaks', 'Water breaks and breathers turn up along the way.'),
        ('Skip', 'You can always skip a card. Always.'), ('18+', 'Made for adults. Your crew picks the level.')],
  respH='Made for a good night',
  faq0=('Can everyone join?', 'Yes. In alcohol-free mode everything becomes points, and you can always skip a card.'),
  faqWhen=('When is it out?', 'Coming soon to iPhone and Android, with Norway first. Follow @getbusted.uk on Instagram and TikTok to hear first.'),
  faqCal=('What is the advent calendar?', 'A new door every day from 1 to 24 December, free for everyone. The cards, rules and dice sides you open get mixed into every game until the end of December.'),
  foot='Adults 18+'),
 'sv': dict(
  desc='Get Busted är partyspelet för förfesten, efterfesten och stughelgen. 1 000+ kort från start, skrivna för Sverige och inte översatta. Lagspel, Rapid och hemliga uppdrag. För vuxna 18+.',
  og='En läsare, 1 000+ kort från start och noll tråkiga pauser. För iPhone och Android.',
  h1=('Partyspelet som ', 'tar över', ' kvällen'),
  lead='En person håller i telefonen och läser högt. Resten tittar på varandra, inte på en skärm. 1 000+ kort från start, skrivna för Sverige, inte översatta, plus lagspel, Rapid och hemliga uppdrag.',
  soonTo='Snart i', note='För vuxna 18+. Alkoholfritt läge finns alltid med.', download='Kommer snart',
  steps=[('Skriv in gänget', '2 till 30 spelare. Namnen hamnar direkt på korten, så ingen kan gömma sig.'),
         ('Välj paket och nivå', 'Mild, Fräck eller Get Fu**ed. Spela var för sig, i fasta duos eller Röd mot Blå.'),
         ('Läs högt och kör', 'Läsaren läser korten. Tärningen, twistarna och Rapid-rundorna dyker upp av sig själva.')],
  stats=[('1 000+', 'kort på svenska från start'), ('5', 'paket från start, fler i höst'), ('2-30', 'spelare'), ('Gratis', 'att komma igång')],
  shots=['Lagspel', 'Twist', 'Rapid', 'Odds', 'Stor text', 'Halloween'],
  calK='1-24 december · gratis', calH=('Julkalender ', 'i appen'), calLead='Ny lucka varje dag fram till jul. Det ni öppnar blandas in i alla spel december ut.',
  calList=['17 nya kort: julbord, julstress, hem till jul och familjen', 'Decemberregler som gäller hela kvällen', 'Nya sidor på tärningen och ett julquiz'],
  groups=['Från start', 'Hösten och vintern', 'Bara i Sverige'], cards='kort', freeCards='50 gratis kort varje kväll',
  priceK='Köp', priceH=('Betala en gång. ', 'Ingen prenumeration.'), plusTag='',
  resp=[('Alkoholfritt', 'Samma spel med poäng. Alla kan vara med.'), ('Pauser', 'Vattenpauser och andningspauser dyker upp längs vägen.'),
        ('Stå över', 'Du får alltid stå över ett kort. Alltid.'), ('18+', 'Gjort för vuxna. Gänget väljer nivån.')],
  respH='Gjort för en bra kväll',
  faq0=('Kan alla vara med?', 'Ja. I alkoholfritt läge blir allt poäng, och det är alltid okej att stå över ett kort.'),
  faqWhen=('När kommer den?', 'Snart till iPhone och Android, med Norge först. Följ @getbusted.se på Instagram och TikTok så får du veta först.'),
  faqCal=('Vad är julkalendern?', 'En ny lucka varje dag 1-24 december, gratis för alla. Korten, reglerna och tärningssidorna ni öppnar blandas in i alla spel december ut.'),
  foot='För vuxna 18+'),
 'da': dict(
  desc='Get Busted er festspillet til forfesten, efterfesten og sommerhusturen. 1.000+ kort skrevet på dansk fra start, holdspil, Rapid og hemmelige missioner. For voksne 18+.',
  og='Én oplæser, 1.000+ kort fra start og ingen kedelige pauser. Til iPhone og Android.',
  h1=('Festspillet, der ', 'tager over', ' aftenen'),
  lead='Én person holder telefonen og læser højt. Resten kigger på hinanden, ikke på en skærm. 1.000+ kort skrevet på dansk fra start, holdspil, Rapid-runder og hemmelige missioner.',
  soonTo='Snart i', note='For voksne 18+. Alkoholfri tilstand er altid med.', download='Kommer snart',
  steps=[('Skriv spillerne ind', '2 til 30 spillere. Navnene kommer direkte på kortene, så ingen kan gemme sig.'),
         ('Vælg pakker og niveau', 'Mild, Fræk eller Get Fu**ed. Spil hver for sig, i faste par eller Rød mod Blå.'),
         ('Læs højt og spil', 'Oplæseren læser kortene. Terningen, twistene og Rapid-runderne dukker op af sig selv.')],
  stats=[('1.000+', 'kort på dansk fra start'), ('5', 'pakker fra start, flere i efteråret'), ('2-30', 'spillere'), ('Gratis', 'at komme i gang')],
  shots=['Holdspil', 'Twist', 'Rapid', 'Odds', 'Stor tekst', 'Halloween'],
  calK='1.-24. december · gratis', calH=('Julekalender ', 'i appen'), calLead='Ny låge hver dag til jul. Det, I åbner, blandes ind i alle spil december ud.',
  calList=['17 nye kort: julefrokost, julestress, hjem til jul og familien', 'Decemberregler, der gælder hele aftenen', 'Nye sider på terningen og en julequiz'],
  groups=['Fra start', 'Efteråret og vinteren', ''], cards='kort', freeCards='50 gratis kort hver aften',
  packsLead='Fem pakker er klar fra start, og flere kommer hen over efteråret. Prøv 5 kort fra en hvilken som helst pakke gratis, før du køber.',
  priceK='Køb', priceH=('Betal én gang. ', 'Intet abonnement.'), plusTag='',
  resp=[('Alkoholfri', 'Samme spil med point. Alle kan være med.'), ('Pauser', 'Vandpauser og pustepauser dukker op undervejs.'),
        ('Spring over', 'Du må altid springe et kort over. Altid.'), ('18+', 'Lavet til voksne. I vælger selv niveauet.')],
  respH='Lavet til en god aften',
  faq0=('Kan alle være med?', 'Ja. I alkoholfri tilstand bliver alt til point, og du må altid springe et kort over.'),
  faqWhen=('Hvornår kommer den?', 'Snart til iPhone og Android, med Norge først.'),
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
LEGAL['en'] = dict(updated='Last updated: 7 October 2026', updated_terms='Last updated: 8 October 2026', updated_purchases='Last updated: 8 October 2026')

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

# Terms of use (separate from the purchase terms on /purchases/). Mirrors getbusted.no/vilkar/ (Bruksvilkår).
# SPRÅK USIKKERT: natural UK legal-plain English, not checked by a native lawyer. JURIDISK USIKKERT: governing law and complaint bodies for UK/EU readers (Roma I), see getbusted.no/_kilde/juridisk.py.
LEGAL['en']['terms'] = ('Terms of use', 'Terms of use for the Get Busted app and the websites getbusted.online and getbusted.no.', 'Terms of use', f"""
<p>These terms apply when you use the Get Busted app and the websites getbusted.online and getbusted.no. By downloading or using the app, you accept the terms. The purchase terms, including the right to cancel, refunds and faulty purchases, are on their own page: <a href="{BUY['en']}">Purchases, cancellation and refunds</a>. The terms do not limit the rights you have as a consumer under the law.</p>

<h2>1. Who we are</h2>
<p>Get Busted is provided by {FIRMA}, org. no. {ORGNR}, {ADDR}, Norway. Email: {M}.</p>

<h2>2. Adults 18+ only</h2>
<p>Get Busted is a party game for adults. You must be at least 18 years old to use the app. The game can be played with or without alcohol, and alcohol-free mode (points instead of sips) is always available.</p>

<h2>3. Play responsibly</h2>
<ul>
  <li>Everyone decides for themselves. You can always skip a card, without explaining why.</li>
  <li>Nobody should be pressured into drinking, doing challenges or answering questions they do not want to.</li>
  <li>Play alcohol-free if anyone is pregnant, taking medication that does not mix with alcohol, driving or for any other reason should not drink.</li>
  <li>Follow the law and the rules of the place you are in. Do not take part in challenges that could harm yourself, others or things around you.</li>
  <li>Only share photos, recordings or summaries of other people if they have given their consent.</li>
</ul>
<p>You are responsible for how you and your group use the game. The cards are meant as humour and can feel crude or provocative, especially on the Get Fu**ed level. Choose a level and packs that suit your group.</p>

<h2>4. Licence to use the app</h2>
<p>The app is free to download. You get a personal, non-transferable right to use the app and the content you have access to on the devices linked to the same Apple ID or Google account. You may not sell the right or pass it on to anyone else. Your use is also subject to Apple's or Google's terms for the app.</p>

<h2>5. Content and rights</h2>
<p>The Get Busted name, the logo, the cards, the texts, the covers and the rest of the content belong to {FIRMA}. You may share single cards and summaries from the app using the share feature. You may not copy the cards, resell the content, make your own versions of the game or use the content commercially without our written consent.</p>

<h2>6. Changes to the app</h2>
<p>We keep developing the app and may add, change or remove cards, features and design. We do not remove content you have paid for unless it is necessary. That could be, for example, a card that turns out to be offensive or unlawful. In that case we replace it with equivalent content. Updates may be needed for the app to keep working.</p>

<h2>7. Availability and liability</h2>
<p>We do our best to make the app work, but we cannot promise that it will always be free of errors or available. The app may be unavailable during maintenance or if problems occur at Apple, Google or other providers. Some features, for example sharing and links to other services, need an internet connection.</p>
<p>We are not liable for damage or loss caused by how the game is used, for example someone drinking too much or a challenge going wrong. This does not apply if the damage is caused by our gross negligence or intent, or if the law does not allow such a limitation of liability.</p>

<h2>8. Links to other services</h2>
<p>The app and the websites may link to Spotify, Instagram, TikTok, Facebook, the App Store and Google Play. These services have their own terms, and we are not responsible for them.</p>

<h2>9. Governing law and disputes</h2>
<p>Norwegian law applies to these terms. If you live in the UK or in another country in the EU/EEA, you still keep the mandatory consumer protection that applies under the law of the country where you live. If you are unhappy, please contact us first. If we cannot find a solution, you can contact the consumer advice service or the consumer authorities in your country, or take the matter to court. The same applies to complaints about purchases.</p>

<h2>10. Changes to these terms</h2>
<p>We may change these terms, for example when the app gets new features or the law changes. The current version is always here, with the date at the top. We will tell you about significant changes that are to your disadvantage in the app or on the website before they apply.</p>
""")

# Purchase terms. Mirrors getbusted.no/kjop/. No "14 days" refund promise and no "48 hours" (the cancellation right is explained as the legal rule only).
# JURIDISK USIKKERT: Do Apple's and Google's purchase dialogs meet the UK/EU rules on express consent and acknowledgement (Consumer Contracts Regulations 2013 reg 37)? Who is the seller?
# JURIDISK USIKKERT: "for as long as we offer the app" for Busted+; launch price notice; time limits for faulty digital content.
LEGAL['en']['purchases'] = ('Purchases, cancellation and refunds', 'How purchases in Get Busted work: the right to cancel, refunds and faulty purchases.', 'Purchases', f"""
<p>This page covers purchases in the Get Busted app. The seller is {FIRMA}, org. no. {ORGNR}, {ADDR}, Norway, {M}. You must be at least 18 years old to buy in the app. The rules for using the app are in <a href="{TERMS['en']}">Terms of use</a>.</p>

<h2>In short</h2>
<ul>
  <li>All purchases are one-time purchases through the App Store or Google Play. There are no subscriptions and no automatic payments.</li>
  <li>The payment goes through Apple or Google, who also handle refund requests under their own rules.</li>
  <li>If something you have bought does not work as it should, we fix it. If we cannot, you are entitled to a price reduction or to your money back.</li>
  <li>Because the content is delivered straight away, you lose the right to cancel once you have given your consent in the store's payment dialog. Read more under Right to cancel.</li>
</ul>

<h2>What you buy</h2>
<p>The app is free to download and gives you 50 free cards from Original every night. You can buy theme packs, the Get Fu**ed level, the Night Pack (a pack of your choice plus the Get Fu**ed level) and Busted+ (all packs). The price is shown in the store before you confirm the purchase, and includes VAT. Prices can vary between countries. You enter into the purchase when you confirm it in the store. The content unlocks as soon as the purchase is confirmed, and the app saves your purchase so you can play without an internet connection. What you may use the content for is set out under Content and rights in <a href="{TERMS['en']}">Terms of use</a>.</p>

<h2>Busted+ and packs still to come</h2>
<p>Busted+ gives you access to all packs in the app, including new card packs and levels that {FIRMA} itself releases in the Get Busted app, for as long as we offer the app. You do not pay extra for new packs that are part of the app's normal range of packs. This does not include:</p>
<ul>
  <li>a separate app or another game</li>
  <li>content made with or sold by a third party, if it is clearly marked as not included in Busted+</li>
  <li>limited-time content that we have expressly announced is an extra</li>
</ul>
<p>It is up to us to decide how many packs are released, and when. Busted+ is a one-time purchase with no subscription. There are no automatic renewals.</p>
<p>Packs with a later release date are shown as "Coming soon" and cannot be bought individually until they are released. Busted+ unlocks them automatically on the release date. If a pack is delayed, it unlocks when it arrives.</p>

<h2>Price</h2>
<p>{PRICE_TXT['en']}</p>

<h2>Right to cancel</h2>
<p>Purchases in the app are digital content that is delivered straight away once the purchase is confirmed. When you buy, you expressly consent to delivery starting immediately and acknowledge that you lose your right to cancel. So you have no right to cancel purchases in the app (in the UK: regulation 37 of the Consumer Contracts (Information, Cancellation and Additional Charges) Regulations 2013; in the EU/EEA: the consumer rules in your country). Your right to a refund from Apple or Google is described below, and your rights if something is faulty are not affected.</p>

<h2>Refunds from Apple and Google</h2>
<p>Apple and Google take the payment and handle refunds under their own rules. The rules can change, so always check the current rules with the store:</p>
<ul>
  <li><b>iPhone:</b> <a href="https://support.apple.com/118223">Apple's information on refunds</a>. You request a refund at <a href="https://reportaproblem.apple.com/">reportaproblem.apple.com</a> with the Apple ID you bought with.</li>
  <li><b>Android:</b> <a href="https://support.google.com/googleplay/answer/15574897">Google's information on refunds in Google Play</a>.</li>
</ul>
<p>If you bought something by mistake, you can write to {M} and send the receipt or order number from Apple or Google. We will help as far as we can, but the refund is made through Apple or Google.</p>

<h2>Faulty purchases</h2>
<p>Content you have bought should work as described. If it is faulty, for example a pack does not unlock or cannot be restored, you have rights under the Consumer Rights Act 2015 if you live in the UK, or under the consumer rules in your country if you live in the EU/EEA. First try "Restore purchases" in the app, with the same Apple ID or Google account you bought with. If that does not help, write to {M} within a reasonable time after you discover the problem and describe it, ideally with the receipt, your phone and the app version. We will fix the problem as quickly as we can, for example with an update, which you may need to install. If we cannot fix it within a reasonable time, you are entitled to a price reduction or to cancel the purchase and get your money back. This does not limit your rights as a consumer under the law.</p>

<h2>Questions and complaints</h2>
<p>Write to {M}. Who you can complain to if we cannot agree is set out under Governing law and disputes in <a href="{TERMS['en']}">Terms of use</a>. How we handle personal data is explained in the <a href="{PRIV['en']}">privacy policy</a>.</p>
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
LEGAL['sv'] = dict(updated='Senast uppdaterad: 7 oktober 2026', updated_terms='Senast uppdaterad: 8 oktober 2026', updated_purchases='Senast uppdaterad: 8 oktober 2026')

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

# Användarvillkor (skilda från köpvillkoren på /se/kop/). Motsvarar getbusted.no/vilkar/ (Bruksvilkår).
# SPRÅK USIKKERT: naturligt juridiskt-enkelt svenskt språk, ej granskat av svensk jurist. JURIDISK USIKKERT: tillämplig lag och tvistlösning för svenska konsumenter (Rom I, ARN).
LEGAL['sv']['terms'] = ('Användarvillkor', 'Användarvillkor för appen Get Busted och webbplatserna getbusted.online och getbusted.no.', 'Användarvillkor', f"""
<p>Dessa villkor gäller när du använder appen Get Busted och webbplatserna getbusted.online och getbusted.no. Genom att ladda ner eller använda appen godtar du villkoren. Köpvillkoren, med ångerrätt, återbetalning och fel vid köp, finns på en egen sida: <a href="{BUY['sv']}">Köpvillkor och ångerrätt</a>. Villkoren begränsar inte de rättigheter du har som konsument enligt lag.</p>

<h2>1. Vilka vi är</h2>
<p>Get Busted tillhandahålls av {FIRMA}, org.nr {ORGNR}, {ADDR}, Norge. E-post: {M}.</p>

<h2>2. Endast för vuxna (18+)</h2>
<p>Get Busted är ett festspel för vuxna. Du måste vara minst 18 år för att använda appen. Spelet kan spelas med eller utan alkohol, och alkoholfritt läge (poäng i stället för klunkar) finns alltid.</p>

<h2>3. Spela ansvarsfullt</h2>
<ul>
  <li>Alla bestämmer själva. Det är alltid okej att stå över ett kort, utan att förklara varför.</li>
  <li>Ingen ska pressas att dricka, göra utmaningar eller svara på frågor de inte vill.</li>
  <li>Spela alkoholfritt om någon är gravid, tar mediciner som inte tål alkohol, ska köra bil eller av andra skäl inte bör dricka.</li>
  <li>Följ lagen och reglerna där ni är. Gör inga utmaningar som kan skada dig själv, andra eller saker runt er.</li>
  <li>Dela bara bilder, inspelningar eller sammanfattningar av andra om de har gett sitt samtycke.</li>
</ul>
<p>Du ansvarar själv för hur du och gänget använder spelet. Korten är tänkta som humor och kan upplevas som grova eller provocerande, särskilt på nivån Get Fu**ed. Välj nivå och paket som passar gänget.</p>

<h2>4. Licens att använda appen</h2>
<p>Appen är gratis att ladda ner. Du får en personlig, icke-överlåtbar rätt att använda appen och det innehåll du har tillgång till på de enheter som är kopplade till samma Apple-ID eller Google-konto. Du får inte sälja eller överlåta rätten till någon annan. Användningen följer också Apples eller Googles villkor för appen.</p>

<h2>5. Innehåll och rättigheter</h2>
<p>Namnet Get Busted, logotypen, korten, texterna, omslagen och resten av innehållet tillhör {FIRMA}. Du får dela enstaka kort och sammanfattningar från appen med delningsfunktionen. Du får inte kopiera korten, sälja innehållet vidare, göra egna versioner av spelet eller använda innehållet kommersiellt utan vårt skriftliga samtycke.</p>

<h2>6. Ändringar i appen</h2>
<p>Vi utvecklar appen vidare och kan lägga till, ändra eller ta bort kort, funktioner och design. Vi tar inte bort innehåll som du har betalat för, om det inte är nödvändigt. Det kan till exempel gälla ett kort som visar sig vara kränkande eller olagligt. Då ersätter vi det med likvärdigt innehåll. Uppdateringar kan behövas för att appen ska fungera.</p>

<h2>7. Tillgänglighet och ansvar</h2>
<p>Vi gör vårt bästa för att appen ska fungera, men kan inte lova att den alltid är felfri eller tillgänglig. Appen kan vara otillgänglig vid underhåll eller om det uppstår fel hos Apple, Google eller andra leverantörer. Vissa funktioner kräver internetanslutning.</p>
<p>Vi ansvarar inte för skada eller förlust som beror på hur spelet används, till exempel att någon dricker för mycket eller att en utmaning går fel. Detta gäller inte om skadan beror på grov oaktsamhet eller uppsåt från vår sida, eller om en sådan ansvarsbegränsning inte är tillåten enligt lag.</p>

<h2>8. Länkar till andra tjänster</h2>
<p>Appen och webbplatserna kan länka till Spotify, Instagram, TikTok, Facebook, App Store och Google Play. Dessa tjänster har egna villkor, och vi ansvarar inte för dem.</p>

<h2>9. Tillämplig lag och tvister</h2>
<p>Norsk lag gäller för dessa villkor. Bor du i Sverige eller ett annat land i EU/EES behåller du ändå det tvingande konsumentskydd som finns i lagen där du bor. Kontakta oss först om du är missnöjd. Hittar vi ingen lösning kan du som konsument i Sverige få kostnadsfri och oberoende rådgivning av <a href="https://www.konsumentverket.se/">Hallå konsument</a> och be <a href="https://www.arn.se/">Allmänna reklamationsnämnden (ARN)</a> pröva tvisten. Du kan också vända dig till domstol. Detsamma gäller klagomål på köp.</p>

<h2>10. Ändringar i villkoren</h2>
<p>Vi kan ändra villkoren, till exempel när appen får nya funktioner eller lagen ändras. Den gällande versionen finns alltid här, med datum högst upp. Väsentliga ändringar till din nackdel meddelar vi i appen eller på webbplatsen innan de börjar gälla.</p>
""")

# Köpvillkor. Motsvarar getbusted.no/kjop/. Inget löfte om 14 dagar och inget om 48 timmar (ångerrätten förklaras bara som lagens huvudregel).
# JURIDISK USIKKERT: Uppfyller Apples och Googles köpdialog kraven på uttryckligt samtycke och bekräftelse enligt svensk lag? Vem är säljare?
# JURIDISK USIKKERT: «så länge vi erbjuder appen» för Busted+, lanseringspris, reklamationstider för digitalt innehåll. Lagreferensen (2022:260) i den gamla texten är borttagen eftersom den inte är verifierad.
LEGAL['sv']['purchases'] = ('Köpvillkor och ångerrätt', 'Så fungerar köp i Get Busted: ångerrätt, återbetalning och fel vid köp.', 'Köp', f"""
<p>Den här sidan gäller köp i appen Get Busted. Säljare är {FIRMA}, org.nr {ORGNR}, {ADDR}, Norge, {M}. Du måste vara minst 18 år för att köpa i appen. Regler för användning av appen finns i <a href="{TERMS['sv']}">Användarvillkor</a>.</p>

<h2>Kort sagt</h2>
<ul>
  <li>Alla köp är engångsköp via App Store eller Google Play. Det finns ingen prenumeration och inga automatiska betalningar.</li>
  <li>Betalningen går via Apple eller Google, som också hanterar återbetalningar enligt sina egna regler.</li>
  <li>Fungerar inte något du har köpt som det ska åtgärdar vi felet. Lyckas vi inte har du rätt till prisavdrag eller att få pengarna tillbaka. Eftersom innehållet levereras direkt har du ingen ångerrätt när du har samtyckt till det.</li>
</ul>

<h2>Vad du köper</h2>
<p>Appen är gratis att ladda ner och ger dig 50 kort ur Original varje kväll, utan kostnad. Du kan köpa temapaket, Get Fu**ed-nivån, Kvällspaketet (ett valfritt paket plus Get Fu**ed-nivån) och Busted+ (alla paket). Priset står i butiken innan du bekräftar köpet och inkluderar moms. Priset kan variera mellan länder. Köpet genomförs när du bekräftar det i butiken. Innehållet låses upp direkt när köpet är bekräftat, och appen sparar ditt köp så att du kan spela utan internetanslutning. Vad du får använda innehållet till framgår under Innehåll och rättigheter i <a href="{TERMS['sv']}">Användarvillkor</a>.</p>

<h2>Busted+ och paket som kommer</h2>
<p>Busted+ ger tillgång till alla paket i appen, även nya kortpaket och nya nivåer som {FIRMA} själv släpper i Get Busted-appen, så länge vi erbjuder appen. Du betalar inget extra för nya paket som ingår i appens vanliga paketutbud. Det gäller inte:</p>
<ul>
  <li>en egen, separat app eller ett annat spel</li>
  <li>innehåll som tagits fram tillsammans med eller säljs av en tredje part, om det tydligt anges att det inte ingår i Busted+</li>
  <li>tidsbegränsat innehåll som vi uttryckligen har meddelat är extra</li>
</ul>
<p>Det är vi som bestämmer hur många paket som släpps och när. Busted+ är ett engångsköp utan prenumeration. Det sker inga automatiska förnyelser.</p>
<p>Paket med senare släppdatum visas som «Kommer snart» och kan inte köpas separat förrän de är släppta. Busted+ låser upp dem automatiskt på släppdatumet. Blir ett paket försenat låses det upp när det kommer.</p>

<h2>Pris</h2>
<p>{PRICE_TXT['sv']}</p>

<h2>Ångerrätt</h2>
<p>Köp i appen avser digitalt innehåll som levereras direkt när köpet är bekräftat. När du köper samtycker du uttryckligen till att leveransen påbörjas direkt och bekräftar att du då förlorar din ångerrätt. Därför har du ingen ångerrätt för köp i appen (lagen (2005:59) om distansavtal och avtal utanför affärslokaler). Rätten till återbetalning hos Apple eller Google beskrivs nedan, och dina rättigheter vid fel påverkas inte.</p>

<h2>Återbetalning hos Apple och Google</h2>
<p>Apple och Google tar emot betalningen och hanterar återbetalning enligt sina egna regler. Reglerna kan ändras, så kontrollera alltid gällande regler hos butiken:</p>
<ul>
  <li><b>iPhone:</b> <a href="https://support.apple.com/sv-se/118223">Apples information om återbetalning</a>. Du begär återbetalning på <a href="https://reportaproblem.apple.com/">reportaproblem.apple.com</a> med det Apple-ID du köpte med.</li>
  <li><b>Android:</b> <a href="https://support.google.com/googleplay/answer/15574897?hl=sv">Googles information om återbetalning på Google Play</a>.</li>
</ul>
<p>Har du köpt något av misstag kan du skriva till {M} och skicka kvittot eller ordernumret från Apple eller Google. Vi hjälper dig så långt vi kan, men återbetalningen sker via Apple eller Google.</p>

<h2>Fel vid köp</h2>
<p>Innehåll du har köpt ska fungera som det är beskrivet. Är det fel, till exempel att ett paket inte låses upp eller inte kan återställas, har du rättigheter enligt konsumentköplagen, som även gäller digitalt innehåll och digitala tjänster. Prova först «Återställ köp» i appen, med samma Apple-ID eller Google-konto som du köpte med. Fungerar det inte, skriv till {M} inom skälig tid efter att du upptäckt felet och beskriv felet, gärna med kvitto, telefon och appversion. Vi åtgärdar felet så snabbt vi kan, till exempel med en uppdatering som du kan behöva installera. Klarar vi inte att åtgärda felet inom skälig tid har du rätt till prisavdrag eller att häva köpet och få pengarna tillbaka. Detta begränsar inte de rättigheter du har som konsument enligt lag.</p>

<h2>Frågor och klagomål</h2>
<p>Skriv till {M}. Vem du kan vända dig till om vi inte blir överens står under Tillämplig lag och tvister i <a href="{TERMS['sv']}">Användarvillkor</a>. Hur vi behandlar personuppgifter står i <a href="{PRIV['sv']}">integritetspolicyn</a>.</p>
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
LEGAL['da'] = dict(updated='Sidst opdateret: 7. oktober 2026', updated_terms='Sidst opdateret: 8. oktober 2026', updated_purchases='Sidst opdateret: 8. oktober 2026')

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

# Brugsvilkår (adskilt fra købsvilkårene på /dk/koeb/). Svarer til getbusted.no/vilkar/ (Bruksvilkår).
# SPRÅK USIKKERT: naturligt, enkelt juridisk dansk, ikke gennemgået af dansk jurist. JURIDISK USIKKERT: lovvalg og klageinstans for danske forbrugere (Rom I, Nævnenes Hus).
LEGAL['da']['terms'] = ('Brugsvilkår', 'Brugsvilkår for appen Get Busted og hjemmesiderne getbusted.online og getbusted.no.', 'Brugsvilkår', f"""
<p>Disse vilkår gælder, når du bruger appen Get Busted og hjemmesiderne getbusted.online og getbusted.no. Når du henter eller bruger appen, accepterer du vilkårene. Købsvilkårene, med fortrydelsesret, refusion og fejl ved køb, står på en separat side: <a href="{BUY['da']}">Køb, fortrydelsesret og refusion</a>. Vilkårene begrænser ikke de rettigheder, du har som forbruger efter loven.</p>

<h2>1. Hvem vi er</h2>
<p>Get Busted udbydes af {FIRMA}, org.nr. {ORGNR}, {ADDR}, Norge. E-mail: {M}.</p>

<h2>2. Kun for voksne (18+)</h2>
<p>Get Busted er et festspil for voksne. Du skal være mindst 18 år for at bruge appen. Spillet kan spilles med eller uden alkohol, og alkoholfri tilstand (point i stedet for slurke) er altid tilgængelig.</p>

<h2>3. Spil ansvarligt</h2>
<ul>
  <li>Alle bestemmer selv. Det er altid i orden at springe et kort over, uden at forklare hvorfor.</li>
  <li>Ingen skal presses til at drikke, lave udfordringer eller svare på spørgsmål, de ikke vil.</li>
  <li>Spil alkoholfrit, hvis nogen er gravide, tager medicin, der ikke kan kombineres med alkohol, skal køre eller af andre grunde ikke bør drikke.</li>
  <li>Følg loven og stedets regler. Gennemfør ikke udfordringer, der kan skade dig selv, andre eller ting omkring jer.</li>
  <li>Del kun billeder, optagelser eller oversigter, hvor andre optræder, hvis de har sagt ja.</li>
</ul>
<p>Du er selv ansvarlig for, hvordan du og dit selskab bruger spillet. Kortene er ment som humor og kan opleves som frække, især på niveauet Get Fu**ed. Vælg niveau og pakker, der passer til jeres selskab.</p>

<h2>4. Licens til at bruge appen</h2>
<p>Appen er gratis at hente. Du får en personlig ret til at bruge appen og det indhold, du har adgang til, på de enheder, der er knyttet til samme Apple-konto eller Google-konto. Retten kan ikke sælges eller overdrages til andre. Din brug er også underlagt Apples eller Googles vilkår for appen.</p>

<h2>5. Indhold og rettigheder</h2>
<p>Navnet Get Busted, logoet, kortene, teksterne, forsiderne og resten af indholdet tilhører {FIRMA}. Du må dele enkelte kort og opsummeringer fra appen med delingsfunktionen. Du må ikke kopiere kortene, sælge indholdet videre, udarbejde egne udgaver af spillet eller bruge indholdet erhvervsmæssigt uden vores skriftlige samtykke.</p>

<h2>6. Ændringer i appen</h2>
<p>Vi udvikler appen videre og kan tilføje, ændre eller fjerne kort, funktioner og design. Vi fjerner ikke indhold, du har betalt for, medmindre det er nødvendigt, for eksempel fordi et kort viser sig at være krænkende eller ulovligt. I så fald erstatter vi det med tilsvarende indhold. Opdateringer kan være nødvendige, for at appen fortsat kan fungere.</p>

<h2>7. Tilgængelighed og ansvar</h2>
<p>Vi gør, hvad vi kan, for at appen fungerer, men kan ikke love, at den altid er fejlfri eller tilgængelig. Appen kan være utilgængelig ved vedligeholdelse eller fejl hos Apple, Google eller andre leverandører, og nogle funktioner, for eksempel deling og links til andre tjenester, kræver internetforbindelse.</p>
<p>Vi er ikke ansvarlige for skade eller tab, der skyldes, hvordan spillet bliver brugt, for eksempel at nogen drikker for meget eller laver udfordringer, der går galt. Det gælder ikke, hvis skaden skyldes grov uagtsomhed eller forsæt fra vores side, eller hvis loven ikke tillader en ansvarsbegrænsning.</p>

<h2>8. Links til andre tjenester</h2>
<p>Appen og hjemmesiderne kan linke til Spotify, Instagram, TikTok, Facebook, App Store og Google Play. Disse tjenester har egne vilkår, og vi er ikke ansvarlige for dem.</p>

<h2>9. Lovvalg og tvister</h2>
<p>Norsk lov gælder. Bor du i Danmark eller et andet land i EU/EØS, beholder du den ufravigelige forbrugerbeskyttelse, som loven i dit bopælsland giver dig. Kontakt os først, hvis du er utilfreds. Finder vi ikke en løsning, kan du som forbruger i Danmark klage til Forbrugerklagenævnet via <a href="https://naevneneshus.dk/">Nævnenes Hus</a> eller indbringe sagen for domstolene. Du kan få generel vejledning om dine rettigheder på <a href="https://www.forbrug.dk/">Forbrug.dk</a>. Det gælder også klager over køb.</p>

<h2>10. Ændringer i vilkårene</h2>
<p>Vi kan ændre vilkårene, for eksempel når appen får nye funktioner, eller loven ændres. Den gældende version står altid her, med dato øverst. Væsentlige ændringer til ulempe for dig giver vi besked om i appen eller på hjemmesiden, før de gælder.</p>
""")

# Købsvilkår. Svarer til getbusted.no/kjop/. Intet løfte om 14 dage og intet om 48 timer (fortrydelsesretten forklares kun som lovens hovedregel).
# JURIDISK USIKKERT: Opfylder Apples og Googles købsdialog kravene om udtrykkeligt samtykke og bekræftelse efter dansk ret (forbrugeraftaleloven)? Hvem er sælger?
# JURIDISK USIKKERT: «så længe vi tilbyder appen» for Busted+, lanceringspris, reklamationsfrister for digitalt indhold.
LEGAL['da']['purchases'] = ('Køb, fortrydelsesret og refusion', 'Sådan fungerer køb i Get Busted: fortrydelsesret, refusion og fejl ved køb.', 'Køb', f"""
<p>Denne side gælder køb i appen Get Busted. Sælger er {FIRMA}, org.nr. {ORGNR}, {ADDR}, Norge, {M}. Du skal være mindst 18 år. Regler for brug af appen står i <a href="{TERMS['da']}">Brugsvilkår</a>.</p>

<h2>Kort fortalt</h2>
<ul>
  <li>Alle køb er engangskøb gennem App Store eller Google Play. Der er intet abonnement og ingen automatiske betalinger.</li>
  <li>Betalingen går gennem Apple eller Google, som også behandler anmodninger om refusion efter deres egne regler.</li>
  <li>Virker noget, du har købt, ikke, retter vi fejlen. Kan vi ikke det, har du krav på forholdsmæssigt afslag i prisen eller på at hæve købet og få pengene tilbage.</li>
  <li>Da indholdet leveres med det samme, mister du fortrydelsesretten, når du har givet samtykke i butikkens betalingsdialog. Læs mere under Fortrydelsesret.</li>
</ul>

<h2>Hvad du køber</h2>
<p>Appen er gratis at hente og giver 50 gratis kort fra Original hver aften. Du kan købe temapakker, Get Fu**ed-niveauet, Aftenpakken (en pakke plus niveauet Get Fu**ed) og Busted+ (alle pakker). Prisen står i butikken, før du bekræfter købet, og er inklusive moms. Prisen kan variere mellem lande. Du indgår købet, når du bekræfter det i butikken. Indholdet låses op, så snart købet er bekræftet, og appen husker købet, så du kan spille uden internetforbindelse. Hvad du må bruge indholdet til, står under Indhold og rettigheder i <a href="{TERMS['da']}">Brugsvilkår</a>.</p>

<h2>Busted+ og pakker, der kommer</h2>
<p>Busted+ giver adgang til alle pakker i appen, også nye kortpakker og nye niveauer, som {FIRMA} selv udgiver i Get Busted-appen, så længe vi tilbyder appen. Du betaler ikke ekstra for nye pakker, der er en del af appens almindelige pakkeudvalg. Det gælder ikke:</p>
<ul>
  <li>en separat app eller et andet spil</li>
  <li>indhold lavet sammen med eller solgt af en tredjepart, hvis det tydeligt er markeret, at det ikke er med i Busted+</li>
  <li>tidsbegrænset indhold, som vi udtrykkeligt har meddelt er ekstra</li>
</ul>
<p>Det er os, der beslutter, hvor mange pakker der udgives, og hvornår. Busted+ er et engangskøb uden abonnement. Der sker ingen automatiske betalinger.</p>
<p>Pakker med senere udgivelsesdato vises som «Kommer snart» og kan ikke købes enkeltvis, før de er udgivet. Busted+ låser dem op automatisk på udgivelsesdatoen. Bliver en pakke forsinket, låses den op, når den kommer.</p>

<h2>Pris</h2>
<p>{PRICE_TXT['da']}</p>

<h2>Fortrydelsesret</h2>
<p>Efter forbrugeraftaleloven har du som forbruger normalt 14 dages fortrydelsesret, når du handler på afstand (fjernsalg). Køber du digitalt indhold, som leveres med det samme, bortfalder fortrydelsesretten, når leveringen er begyndt. Det forudsætter, at du først udtrykkeligt har samtykket til, at leveringen begynder, og har bekræftet, at du dermed mister din fortrydelsesret (forbrugeraftaleloven).</p>

<h2>Refusion hos Apple og Google</h2>
<p>Apple og Google modtager betalingen og behandler refusion efter deres egne regler. Reglerne kan ændres, så tjek altid de gældende regler hos butikken:</p>
<ul>
  <li><b>iPhone:</b> <a href="https://support.apple.com/da-dk/118223">Apples side om refusion</a>. Du beder om refusion på <a href="https://reportaproblem.apple.com/">reportaproblem.apple.com</a> med den Apple-konto, du købte med.</li>
  <li><b>Android:</b> <a href="https://support.google.com/googleplay/answer/15574897?hl=da">Googles side om refusion i Google Play</a>.</li>
</ul>
<p>Har du købt noget ved en fejl, kan du skrive til {M} og sende kvitteringen eller ordrenummeret fra Apple eller Google. Vi hjælper dig så langt, vi kan, men tilbagebetalingen sker via Apple eller Google.</p>

<h2>Fejl ved køb</h2>
<p>Indhold, du har købt, skal virke, som det er beskrevet. Er der fejl, for eksempel at en pakke ikke låses op eller ikke kan gendannes, har du de rettigheder, som dansk forbrugerlovgivning giver dig. Prøv først «Gendan køb» i appen, med samme Apple-konto eller Google-konto, som du købte med. Virker det ikke, så skriv til {M} uden unødigt ophold og beskriv fejlen, gerne med kvittering, telefon og appversion. Vi retter fejlen så hurtigt, vi kan, for eksempel med en opdatering, som du muligvis skal installere. Kan vi ikke det inden for rimelig tid, har du krav på forholdsmæssigt afslag i prisen eller på at hæve købet og få pengene tilbage. Det begrænser ikke de rettigheder, du har som forbruger efter loven.</p>

<h2>Spørgsmål og klager</h2>
<p>Skriv til {M}. Bliver vi ikke enige, kan du som forbruger klage til Forbrugerklagenævnet via <a href="https://naevneneshus.dk/">Nævnenes Hus</a>. Se Lovvalg og tvister i <a href="{TERMS['da']}">Brugsvilkår</a>. Hvordan vi behandler personoplysninger, står i <a href="{PRIV['da']}">privatlivspolitikken</a>.</p>
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

def label(rel, t):
    # Utenlandske sider viser ingen datoer: bare «Kommer snart» / «Coming soon»
    return t['soon']

def packs(lst, t):
    out = []
    for slug, img, name, sub, rel in lst:
        soon = f"<i class='soon'>{E(label(rel, t))}</i>" if rel else ''
        dr = ''
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
<script src="/vaer.js" defer></script>
<script>
// Språkvalg huskes; «Kommer»-merket forsvinner på slippdagen.
document.querySelectorAll('.langs a').forEach(function (a) {{ a.addEventListener('click', function () {{ try {{ localStorage.setItem('gb-lang', a.dataset.lang); }} catch (e) {{}} }}); }});
var now = Date.now();
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
    xmas_html = f'''<section class="xmas" data-until="2026-12-31">
  <div class="wrap">
    <div>
      <p class="kicker">{E(u['calK'])}</p>
      <h2>{E(u['calH'][0])}<em>{E(u['calH'][1])}</em></h2>
      <p class="lead">{E(u['calLead'])}</p>
      <ul>{cal}</ul>
    </div>
    <div class="doors" aria-hidden="true">{doors}</div>
  </div>
</section>''' if CAL else ''
    prices = ''.join(f"<div class='price'><h3>{E(h)}</h3><p>{E(p)}</p></div>" for h, p in t['prices'][:3])
    ph, pp = t['prices'][3]
    tag = f"<span class='tag'>{E(u['plusTag'])}</span>" if u['plusTag'] else ''
    plus = f"<div class='price plus'><div><h3>{E(ph)}</h3></div><div><p>{E(pp)}</p>{tag}</div></div>"
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
      {hero_card_html(L)}
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

{samples_html(L)}

{xmas_html}

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
    return shell(t, HOME, t['title'], t['desc'], body, redirect=True).replace('</head>', jsonld(t) + '\n</head>', 1)

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
  <p class="meta">{E(LEGAL[t['lang']].get('updated_' + key, LEGAL[t['lang']]['updated']))}</p>
  {html_body.strip()}
</article>"""
    return shell(t, alt, f'{title} - Get Busted', desc, body)

def write(path, text):
    f = ROOT / path.lstrip('/') / 'index.html'
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(text, encoding='utf-8')

# ---------- Landingssider per anledning (okt 2026) ----------
# Samme oppskrift som getbusted.no/julebord/ osv.: eksempelkort fra appen (ingen alkoholord), grunner, tips og FAQ med schema.
LP_ALT = {
 'xmas':  {'en': '/christmas-party/', 'sv': '/se/julbord/', 'da': '/dk/julefrokost/', 'no': 'https://getbusted.no/julebord/'},
 'cabin': {'en': '/cabin-weekend/', 'sv': '/se/stugan/', 'da': '/dk/sommerhus/', 'no': 'https://getbusted.no/hyttetur/'},
 'wed':   {'en': '/stag-and-hen/', 'sv': '/se/svensexa-mohippa/', 'da': '/dk/polterabend/', 'no': 'https://getbusted.no/utdrikningslag/'},
}
LP_COLOR = {'xmas': '#E0473E', 'cabin': '#C7864A', 'wed': '#E94B8A'}
LP_COVER = {'xmas': {'en': 'cover_jul_en.jpg', 'sv': 'cover_jul.jpg', 'da': 'cover_jul.jpg'},
            'cabin': {'en': 'cover_hytta_en.jpg', 'sv': 'cover_hytta_sv.jpg', 'da': 'cover_hytta_da.jpg'},
            'wed': {'en': 'cover_utdrikning_en.jpg', 'sv': 'cover_utdrikning_sv.jpg', 'da': 'cover_utdrikning_da.jpg'}}
PK = {'en': 'On three, point at the one who', 'sv': 'På tre - peka på den som', 'da': 'På tre - peg på den, der'}
TR = {'en': 'Truth', 'sv': 'Sanning', 'da': 'Sandhed'}
LPT = {
 'en': dict(cardsK='A taste', cardsH='Cards from the pack', cardsLead='A few picks. The names get swapped for your crew.', whyK='Why Get Busted', whyH='Made for the night', tipsH='Get the most out of it', faqK='Questions', faqH='FAQ', more='More occasions:', note='For adults 18+. Alcohol-free mode is always included.', home='More about Get Busted', out='At launch', soon='Coming soon'),
 'sv': dict(cardsK='Smakprov', cardsH='Kort från paketet', cardsLead='Ett litet urval. Namnen byts mot ert gäng.', whyK='Varför Get Busted', whyH='Gjort för kvällen', tipsH='Så får ni ut mest av det', faqK='Frågor', faqH='Vanliga frågor', more='Fler tillfällen:', note='För vuxna 18+. Alkoholfritt läge finns alltid med.', home='Mer om Get Busted', out='Med från start', soon='Kommer snart'),
 'da': dict(cardsK='Smagsprøver', cardsH='Kort fra pakken', cardsLead='Et lille udvalg. Navnene bliver skiftet ud med jeres.', whyK='Hvorfor Get Busted', whyH='Lavet til aftenen', tipsH='Sådan får I mest ud af det', faqK='Spørgsmål', faqH='Ofte stillede spørgsmål', more='Flere anledninger:', note='For voksne 18+. Alkoholfri tilstand er altid med.', home='Mere om Get Busted', out='Med fra start', soon='Kommer snart'),
}
LANDINGS = {
 'en': {
  'xmas': dict(pack='Christmas', live=True, menu='Christmas party', title='Party game for the office Christmas party - Get Busted',
    desc='A party game for the Christmas party and the festive season: cards about Secret Santa, the family and the HR email. Get Busted, for adults 18+, one phone, 2-30 players.',
    h1=('Party game for the ', 'Christmas party'), lead='Office party, friends’ Christmas or a night in with the family you chose. The Christmas pack turns it into the night everyone talks about in January.',
    why=[('Cards you recognise', 'Secret Santa disasters, the HR email and the Hinge date you brought home. Written in English for English-speaking crews, not translated.'), ('Works for big tables', '2 to 30 players. Big groups get cards for everyone at once, and team play turns departments into Red vs Blue.'), ('Everyone can join', 'Alcohol-free mode turns everything into points, and any card can be skipped.')],
    cards=[(PK['en'], 'will buy every single present on Christmas Eve'), (PK['en'], 'will still be in pyjamas eating leftovers for dinner on the 29th'), (PK['en'], 'would cancel their New Year’s plans at 9pm'), (PK['en'], 'will set their Hinge location to their hometown the second they get off the train'), (PK['en'], 'will end up as the reason for HR’s email after this year’s Christmas party'), (PK['en'], 'would bring a Hinge date home for Christmas to stop the questions'), (TR['en'], 'Niamh: what’s the worst Secret Santa present you’ve ever given?'), (TR['en'], 'Hamish: what does your family think you do for a living, and how wrong are they?')],
    tips=['Pick Christmas and Original, on Mild or Cheeky if the boss is at the table.', 'Turn on teams and let the departments play Red vs Blue.', 'Swap the reader every few rounds so nobody reads all night.'],
    faq=[('Does it work for an office party?', 'Yes. Pick Mild or Cheeky and the cards stay on the right side of HR. Get Fu**ed is for your mates.'), ('How many can play?', 'From 2 to 30. Big tables get more cards that apply to everyone at once.'), ('What does the Christmas pack cost?', 'It is a one-time purchase. Try 5 cards for free first, and Original has 50 free cards every night.')]),
  'cabin': dict(pack='The Cabin', live=True, menu='Cabin weekend', title='Party game for a cabin weekend - Get Busted',
    desc='A party game for the cabin weekend or the group Airbnb: cards about the double room, the board games and the Splitwise request. Get Busted, adults 18+, works offline.',
    h1=('Party game for the ', 'cabin weekend'), lead='Zero signal, a hot tub and a whole night ahead. Get Busted turns the group trip into the one you talk about all year.',
    why=[('Written for group trips', 'The Cabin pack is about the double room, the board game cheat, the BBQ hero and the friend who never pays their share.'), ('No signal? No problem', 'The cards live in the app, so it works offline once the app and packs are downloaded.'), ('One phone is enough', 'One reader holds the phone. Everyone else looks at each other, not at a screen.')],
    cards=[(PK['en'], 'brings ten board games nobody asked for'), (PK['en'], 'says they’re going offline and posts five stories'), (PK['en'], 'claims the double room without asking anyone'), (PK['en'], 'would cheat at Catan and deny it to the grave'), (PK['en'], 'takes over the BBQ and then burns everything'), (PK['en'], 'would get the whole group banned from Airbnb'), (TR['en'], 'Freya: who in this room still owes you money from a trip, and how much?'), (TR['en'], 'Callum: what’s the pettiest thing you’ve ever argued about on a group trip?')],
    tips=['Download the app and packs before you leave, so everything works offline.', 'Pick The Cabin and Original. Save Get Fu**ed for after midnight.', 'Play in duos and keep the teams all weekend.'],
    faq=[('Does it work offline?', 'Yes, the cards live in the app. Download the app and the packs you want before you go.'), ('How many can play?', 'From 2 to 30, and you can add or remove players along the way.'), ('What does The Cabin pack cost?', 'It is a one-time purchase. Try 5 cards for free first.')]),
  'wed': dict(pack='Stag & Hen', live=False, menu='Stag and hen dos', title='Stag and hen do games - Get Busted',
    desc='Games for the stag or hen do: cards about the rings, the speech and the save the date. Get Busted, a party game for adults 18+ on one phone. Stag & Hen pack coming soon.',
    h1=('Games for the ', 'stag and hen do'), lead='One of you is getting married. The rest of you are making sure the weekend is remembered. The Stag & Hen pack is made for exactly that.',
    why=[('All about the one getting married', 'Cards about the rings, the speech, the guest list and the save the date sent too early.'), ('Just one phone', 'One reader, one card at a time. No props, no prep.'), ('Every level', 'Mild for the in-laws, Cheeky for the group and Get Fu**ed when the star of the show can take it.')],
    cards=[(PK['en'], 'would lose the rings on the way to the ceremony'), (PK['en'], 'will send a “save the date” before they have an actual date'), (PK['en'], 'will announce their engagement on Instagram before telling their parents'), (PK['en'], 'has the most embarrassing Love Island audition tape ready to go'), (PK['en'], 'will still be paying off this weekend in six months'), (PK['en'], 'will be the one who drops out of the next stag or hen do last minute'), (TR['en'], 'Orla: what’s the worst stag or hen do you’ve ever been on, and what went wrong?'), (TR['en'], 'Theo: how much are you honestly going to spend on the wedding gift?')],
    tips=['Make the one getting married the reader for the first round.', 'Mix Stag & Hen with Original for variety.', 'Use secret missions: the phone goes to one player, who gets a mission only they know about.'],
    faq=[('When is the Stag & Hen pack out?', 'Later this autumn. Until then you can play Original, Christmas, Afterparty, The Cabin and Halloween.'), ('Does it work for both stag and hen dos?', 'Yes. The cards are about the wedding and the one getting married.'), ('What does it cost?', 'The pack is a one-time purchase, or get Busted+ for everything.')]),
 },
 'sv': {
  'xmas': dict(pack='Jul', live=True, menu='Julbord', title='Partyspel till julbordet - Get Busted',
    desc='Partyspel till julbordet och julfesten: kort om släkten, julklapparna och Kalle Anka. Get Busted, för vuxna 18+, en telefon, 2-30 spelare.',
    h1=('Partyspel till ', 'julbordet'), lead='Julfest med jobbet, julbord med gänget eller mellandagarna i hemstan. Jul-paketet gör kvällen till den alla pratar om i januari.',
    why=[('Kort ni känner igen', 'Gävlebocken, Mall of Scandinavia på annandagen och julklappen du låtsas älska. Skrivet i Sverige, inte översatt.'), ('Funkar för stora bord', '2 till 30 spelare. Stora gäng får kort som gäller alla samtidigt, och med lagspel kan avdelningarna köra Röd mot Blå.'), ('Alla kan vara med', 'Alkoholfritt läge gör allt till poäng, och man får alltid stå över ett kort.')],
    cards=[(PK['sv'], 'har redan en julfestflört utsedd innan förrätten'), (PK['sv'], 'fortfarande tror att Gävlebocken klarar sig i år'), (PK['sv'], 'börjar prata dialekt igen så fort hen kliver av tåget i hemstan'), (PK['sv'], 'står först i kön utanför Mall of Scandinavia på annandagen'), (PK['sv'], 'skickar ”gott nytt år” till ett ex en minut efter tolvslaget'), (PK['sv'], 'säger ”vi borde ses i mellandagarna” och aldrig hör av sig'), (TR['sv'], 'Valdemar: vad är det pinsammaste du gjort på en julfest med jobbet?'), (TR['sv'], 'Edla: vilken julklapp från släkten har du ljugit och sagt att du älskar?')],
    tips=['Välj Jul och Original, och Mild eller Fräck om chefen sitter vid bordet.', 'Slå på lag och låt avdelningarna köra Röd mot Blå.', 'Byt läsare då och då, så slipper en person läsa hela kvällen.'],
    faq=[('Funkar det på en julfest med jobbet?', 'Ja. Välj Mild eller Fräck, så håller sig korten på rätt sida. Get Fu**ed är för kompisgänget.'), ('Hur många kan spela?', 'Från 2 till 30. Stora bord får fler kort som gäller alla samtidigt.'), ('Vad kostar Jul-paketet?', 'Ett engångsköp. Testa 5 kort gratis först, och Original har 50 gratis kort varje kväll.')]),
  'cabin': dict(pack='Stugan', live=True, menu='Stugan', title='Partyspel till stughelgen - Get Busted',
    desc='Partyspel till stughelgen: kort om bastun, Fjällrävenjackan och wifi-lösenordet. Get Busted, för vuxna 18+, funkar utan täckning.',
    h1=('Partyspel till ', 'stughelgen'), lead='Ingen täckning, en bastu och en hel kväll framför er. Get Busted gör stughelgen till den ni pratar om hela året.',
    why=[('Skrivet för svenska stugor', 'Stugan-paketet handlar om bastun, städdagen, landstället och den som frågar efter wifi i en stuga utan rinnande vatten.'), ('Ingen täckning? Inga problem', 'Korten finns i appen, så det funkar offline när appen och paketen är nedladdade.'), ('En telefon räcker', 'En läsare håller i telefonen. Resten tittar på varandra, inte på en skärm.')],
    cards=[(PK['sv'], 'säger att de ska vara offline hela helgen och lägger upp tre stories första kvällen'), (PK['sv'], 'kallar sin sommarstuga för ”landstället”'), (PK['sv'], 'skulle dö först om vi blev insnöade i Vemdalen'), (PK['sv'], 'har en Fjällrävenjacka för en månadshyra och aldrig går längre än till bilen'), (PK['sv'], 'alltid försvinner på städdagen innan man åker'), (PK['sv'], 'somnar först, mitt i ett parti Monopol'), (TR['sv'], 'Ebbe: vem i rummet skulle du minst vilja dela stuga med?'), (TR['sv'], 'Ingrid: vem ringer du först om täckningen kommer tillbaka klockan tre i natt?')],
    tips=['Ladda ner appen och paketen innan ni åker, så funkar allt utan täckning.', 'Välj Stugan och Original. Spara Get Fu**ed till efter midnatt.', 'Spela i duos och behåll lagen hela helgen.'],
    faq=[('Funkar det utan internet?', 'Ja, korten finns i appen. Ladda ner appen och paketen innan ni åker.'), ('Hur många kan spela?', 'Från 2 till 30, och ni kan lägga till eller ta bort spelare under kvällen.'), ('Vad kostar Stugan-paketet?', 'Ett engångsköp. Testa 5 kort gratis först.')]),
  'wed': dict(pack='Svensexa & möhippa', live=False, menu='Svensexa och möhippa', title='Lekar till svensexa och möhippa - Get Busted',
    desc='Lekar till svensexan och möhippan: kort om ringen, talet och gruppchatten. Get Busted, partyspel för vuxna 18+ på en telefon. Paketet kommer i höst.',
    h1=('Lekar till ', 'svensexan och möhippan'), lead='En av er ska gifta sig, resten ska se till att dagen blir ihågkommen. Svensexa & möhippa-paketet är gjort för just det.',
    why=[('Handlar om den som ska gifta sig', 'Kort om ringen, talet, gruppchatten och hur paret egentligen träffades.'), ('Bara en telefon', 'En läsare, ett kort i taget. Inga rekvisita, inga förberedelser.'), ('Alla nivåer', 'Mild för svärfamiljen, Fräck för gänget och Get Fu**ed när huvudpersonen klarar det.')],
    cards=[(PK['sv'], 'hade flyttat sitt eget bröllop om det krockade med Melodifestivalen'), (PK['sv'], 'gråter redan när musiken börjar på vigseln'), (PK['sv'], 'klagar mest på budgeten i gruppchatten'), (PK['sv'], 'skulle ge bort ett presentkort på Gekås i bröllopspresent'), (PK['sv'], 'har flest pinsamma bilder på den som ska gifta sig'), (PK['sv'], 'sjunger högst när ABBA kommer på'), (TR['sv'], 'Tyra: vad tyckte du om förlovningsringen, helt ärligt?'), (TR['sv'], 'Gösta: vad är det pinsammaste du vet om hur paret träffades?')],
    tips=['Låt huvudpersonen vara läsare första rundan.', 'Blanda Svensexa & möhippa med Original.', 'Kör hemliga uppdrag: telefonen går till en spelare som får ett uppdrag bara hen vet om.'],
    faq=[('När kommer paketet?', 'I höst. Tills dess kan ni spela Original, Jul, Efterfest, Stugan och Halloween.'), ('Funkar det för både svensexa och möhippa?', 'Ja. Korten handlar om bröllopet och den som ska gifta sig.'), ('Vad kostar det?', 'Paketet är ett engångsköp, eller ta Busted+ för allt.')]),
 },
 'da': {
  'xmas': dict(pack='Jul', live=True, menu='Julefrokost', title='Festspil til julefrokosten - Get Busted',
    desc='Festspil til julefrokosten: kort om kransekagen, pakkelegen og kollegaen dagen efter. Get Busted, for voksne 18+, én telefon, 2-30 spillere.',
    h1=('Festspil til ', 'julefrokosten'), lead='Firmajulefrokost, vennejulefrokost eller mellem jul og nytår i hjembyen. Jul-pakken gør aftenen til den, alle snakker om i januar.',
    why=[('Kort I kender', 'Kransekagen kl. 3, Whamageddon og julefrokostcrushet, der stadig ikke ved det. Skrevet på dansk, ikke oversat.'), ('Virker til store borde', '2 til 30 spillere. Store grupper får kort, der gælder alle på én gang, og med holdspil kan afdelingerne spille Rød mod Blå.'), ('Alle kan være med', 'Alkoholfri tilstand gør alt til point, og man må altid springe et kort over.')],
    cards=[(PK['da'], 'står alene tilbage med kransekagen kl. 3'), (PK['da'], 'ender med at holde tale til familiejulefrokosten'), (PK['da'], 'har et julefrokostcrush, der stadig ikke ved det'), (PK['da'], 'taber Whamageddon først i år'), (PK['da'], 'lyver bedst om, hvor de var natten efter julefrokosten'), (PK['da'], 'skriver «glædelig jul» til en eks'), (TR['da'], 'Thyge: hvad er den værste gave, du har fået, og hvem gav den?'), (TR['da'], 'Aksel: hvad er det mest akavede, du har sagt til en kollega dagen efter julefrokosten?')],
    tips=['Vælg Jul og Original, og Mild eller Fræk, hvis chefen sidder med ved bordet.', 'Slå hold til, og lad afdelingerne spille Rød mod Blå.', 'Skift oplæser undervejs, så ingen skal læse hele aftenen.'],
    faq=[('Virker det til en firmajulefrokost?', 'Ja. Vælg Mild eller Fræk, så holder kortene sig på den rigtige side. Get Fu**ed er til vennerne.'), ('Hvor mange kan spille?', 'Fra 2 til 30. Store borde får flere kort, der gælder alle på én gang.'), ('Hvad koster Jul-pakken?', 'Det er et engangskøb. Prøv 5 kort gratis først, og Original har 50 gratis kort hver aften.')]),
  'cabin': dict(pack='Sommerhuset', live=True, menu='Sommerhus', title='Festspil til sommerhusturen - Get Busted',
    desc='Festspil til sommerhusturen: kort om Bezzerwizzer, dansktop kl. 10 og gryden, der skal stå i blød. Get Busted, for voksne 18+, virker uden dækning.',
    h1=('Festspil til ', 'sommerhusturen'), lead='Ingen dækning, en sauna og en hel aften foran jer. Get Busted gør sommerhusturen til den, I snakker om hele året.',
    why=[('Skrevet til danske sommerhuse', 'Sommerhuset-pakken handler om brætspil, varmt vand, slik i kufferten og den, der aldrig betaler sin andel.'), ('Ingen dækning? Intet problem', 'Kortene ligger i appen, så det virker offline, når appen og pakkerne er hentet.'), ('Én telefon er nok', 'Én oplæser holder telefonen. Resten kigger på hinanden, ikke på en skærm.')],
    cards=[(PK['da'], 'snyder i Bezzerwizzer'), (PK['da'], 'sætter dansktop på kl. 10 om morgenen'), (PK['da'], 'siger «den skal lige stå i blød» og aldrig kommer tilbage til gryden'), (PK['da'], 'har pakket mere slik end tøj'), (PK['da'], 'bruger alt det varme vand første morgen'), (PK['da'], 'aldrig betaler sin andel af sommerhuset til tiden'), (TR['da'], 'Frida: hvilken sommerhusferie var den værste, og hvis skyld var det?'), (TR['da'], 'Villum: hvad har du aldrig fortalt nogen her om den sidste sommerhustur?')],
    tips=['Hent appen og pakkerne, før I kører, så virker alt uden dækning.', 'Vælg Sommerhuset og Original. Gem Get Fu**ed til efter midnat.', 'Spil i par, og behold holdene hele weekenden.'],
    faq=[('Virker det uden internet?', 'Ja, kortene ligger i appen. Hent appen og pakkerne, før I tager af sted.'), ('Hvor mange kan spille?', 'Fra 2 til 30, og I kan tilføje eller fjerne spillere undervejs.'), ('Hvad koster Sommerhuset-pakken?', 'Det er et engangskøb. Prøv 5 kort gratis først.')]),
  'wed': dict(pack='Polterabend', live=False, menu='Polterabend', title='Lege til polterabend - Get Busted',
    desc='Lege til polterabenden: kort om vielsen, talen og polterbussen. Get Busted, festspil for voksne 18+ på én telefon. Polterabend-pakken kommer i efteråret.',
    h1=('Lege til ', 'polterabenden'), lead='En af jer skal giftes, resten skal sørge for, at dagen bliver husket. Polterabend-pakken er lavet til netop det.',
    why=[('Handler om den, der skal giftes', 'Kort om vielsen, talen, bryllupssangen og polterabendopgaverne.'), ('Kun én telefon', 'Én oplæser, ét kort ad gangen. Ingen rekvisitter, ingen forberedelse.'), ('Alle niveauer', 'Mild til svigerfamilien, Fræk til vennerne og Get Fu**ed, når hovedpersonen kan tåle det.')],
    cards=[(PK['da'], 'græder først til vielsen'), (PK['da'], 'bliver den næste, der skal giftes'), (PK['da'], 'ville holde sin polterabend i Lalandia'), (PK['da'], 'falder i søvn i polterbussen før frokost'), (PK['da'], 'har allerede valgt sin bryllupssang uden at have en kæreste'), (PK['da'], 'kræver omkørsel efter at være kørt af banen til go-kart'), (TR['da'], 'Ellen: hvad er det pinligste, du har sagt i en tale?'), (TR['da'], 'Bastian: hvilken polterabendopgave ville du aldrig lave, selv for 1.000 kr.?')],
    tips=['Lad hovedpersonen være oplæser i første runde.', 'Bland Polterabend med Original.', 'Brug hemmelige missioner: telefonen går til én spiller, der får en mission, kun vedkommende kender.'],
    faq=[('Hvornår kommer Polterabend-pakken?', 'I efteråret. Indtil da kan I spille Original, Jul, Efterfest, Sommerhuset og Halloween.'), ('Virker det til både polterabend for mænd og kvinder?', 'Ja. Kortene handler om brylluppet og den, der skal giftes.'), ('Hvad koster det?', 'Pakken er et engangskøb, eller tag Busted+ for det hele.')]),
 },
}

def landing(t, key):
    L = t['lang']; d = LANDINGS[L][key]; x = LPT[L]; col = LP_COLOR[key]
    cards = ''.join(f"<figure class='sample' style='--c:{col}'><figcaption>{E(d['pack'])}</figcaption><p class='sample-head'>{E(h)}</p><blockquote>{E(c)}</blockquote></figure>" for h, c in d['cards'])
    why = ''.join(f"<div class='feature'><h3>{E(h)}</h3><p>{E(c)}</p></div>" for h, c in d['why'])
    tips = ''.join(f'<li>{E(c)}</li>' for c in d['tips'])
    faq = ''.join(f'<details><summary>{E(q)}</summary><p>{E(a)}</p></details>' for q, a in d['faq'])
    more = ' · '.join(f'<a href="{LP_ALT[k][L]}">{E(LANDINGS[L][k]["menu"])}</a>' for k in LP_ALT if k != key)
    url = full(LP_ALT[key][L])
    ld = {'@context': 'https://schema.org', '@graph': [
        {'@type': 'WebPage', '@id': url, 'url': url, 'name': d['title'], 'description': d['desc'], 'inLanguage': L, 'isPartOf': {'@type': 'WebSite', 'url': full(HOME[L]), 'name': 'Get Busted'}},
        {'@type': 'BreadcrumbList', 'itemListElement': [{'@type': 'ListItem', 'position': 1, 'name': 'Get Busted', 'item': full(HOME[L])}, {'@type': 'ListItem', 'position': 2, 'name': d['menu'], 'item': url}]},
        {'@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in d['faq']]}]}
    body = f"""<section class="hero lp">
  <div class="wrap">
    <div>
      <p class="kicker">{E(d['pack'])} · {E(x['out'] if d['live'] else x['soon'])}</p>
      <h1>{E(d['h1'][0])}<em>{E(d['h1'][1])}</em></h1>
      <p class="lead">{E(d['lead'])}</p>
      <p class="note">{E(x['note'])} <a href="{HOME[L]}">{E(x['home'])}</a>.</p>
    </div>
    <div class="stage lp-stage" aria-hidden="true"><img class="cover" src="/img/{LP_COVER[key][L]}" alt="" style="--c:{col}" width="360" height="503"></div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <p class="kicker">{E(x['cardsK'])}</p>
    <h2>{E(x['cardsH'])}</h2>
    <p class="lead">{E(x['cardsLead'])}</p>
    <div class="samples">{cards}</div>
  </div>
</section>

<section>
  <div class="wrap">
    <p class="kicker">{E(x['whyK'])}</p>
    <h2>{E(x['whyH'])}</h2>
    <div class="features three">{why}</div>
    <div class="lp-tips"><h3>{E(x['tipsH'])}</h3><ul>{tips}</ul></div>
  </div>
</section>

<section class="alt">
  <div class="wrap" style="max-width:820px">
    <p class="kicker">{E(x['faqK'])}</p>
    <h2>{E(x['faqH'])}</h2>
    {faq}
    <p class="lp-more">{E(x['more'])} {more}</p>
  </div>
</section>"""
    page = shell(t, LP_ALT[key], d['title'], d['desc'], body)
    return page.replace('</head>', '<script type="application/ld+json">' + _json.dumps(ld, ensure_ascii=False).replace('</', '<\\/') + '</script>\n</head>', 1)

def lp_links(L):
    x = LPT[L]
    return '<p class="lp-more">' + E(x['more']) + ' ' + ' · '.join(f'<a href="{LP_ALT[k][L]}">{E(LANDINGS[L][k]["menu"])}</a>' for k in LP_ALT) + '</p>'

for lang in LANGS:
    t = T[lang]
    write(HOME[lang], home(t))
    write(HELP[lang], help_page(t))
    for _k in LP_ALT:
        write(LP_ALT[_k][lang], landing(t, _k))
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
.samples{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:18px;margin-top:28px}
.sample{margin:0;background:linear-gradient(180deg,var(--card),var(--card2));border:1px solid var(--line);border-top:4px solid var(--c);border-radius:var(--radius);padding:20px 20px 22px;display:flex;flex-direction:column;gap:8px;box-shadow:0 18px 40px -22px color-mix(in srgb,var(--c) 60%,transparent)}
.sample figcaption{font-weight:800;font-size:13px;letter-spacing:2px;text-transform:uppercase;color:var(--c)}
.sample .sample-head{font-weight:800;font-style:italic;color:var(--muted);font-size:16px}
.sample blockquote{margin:0;font-weight:800;font-size:21px;line-height:1.3;color:var(--fg)}
.lp-more{margin-top:22px;color:var(--muted)}
.hero.lp .wrap{grid-template-columns:1.3fr .7fr}
.lp-stage{height:auto;min-height:0;display:flex;justify-content:center}
.lp-stage .cover{position:relative;top:0;width:240px;height:auto;transform:rotate(3deg)}
.features.three{grid-template-columns:repeat(3,1fr)}
.lp-tips{margin-top:28px;background:var(--card2);border:1px solid var(--line);border-radius:var(--radius);padding:22px 26px}
.lp-tips h3{font-size:22px;margin-bottom:6px}.lp-tips li{color:var(--muted)}
@media (max-width:900px){.hero.lp .wrap{grid-template-columns:1fr}.features.three{grid-template-columns:1fr}.lp-stage .cover{width:180px}}
@media (max-width:900px){.pricing.three{grid-template-columns:1fr}}
@media (max-width:760px){.nav nav .langs{display:inline-flex;margin:0 4px}.nav nav .langs a{display:inline-block}.nav nav a.cta{display:none}.nav .brand{white-space:nowrap;font-size:19px}.nav .brand img{width:34px;height:34px}.langs a{padding:4px 6px}}
""", encoding='utf-8')
(ROOT / 'CNAME').write_text('getbusted.online\n')
# Gamle adresser sender videre: /da/ til /dk/ og /sv/ til /se/
for _old, _new in (('/da/', '/dk/'), ('/da/hjaelp/', '/dk/hjaelp/'), ('/da/privatliv/', '/dk/privatliv/'),
                   ('/sv/', '/se/'), ('/sv/hjalp/', '/se/hjalp/'), ('/sv/integritet/', '/se/integritet/')):
    write(_old, f"<!doctype html><meta charset='utf-8'><title>Get Busted</title><link rel='canonical' href='{SITE}{_new}'><meta http-equiv='refresh' content='0;url={_new}'><a href='{_new}'>Get Busted</a>\n")
AI_BOTS = ['GPTBot', 'OAI-SearchBot', 'ChatGPT-User', 'ClaudeBot', 'Claude-SearchBot', 'Claude-User', 'PerplexityBot', 'Perplexity-User', 'Google-Extended', 'Applebot-Extended', 'Bingbot', 'DuckAssistBot', 'meta-externalagent', 'CCBot']
ROBOTS = 'User-agent: *\nAllow: /\n\n' + ''.join(f'User-agent: {b}\nAllow: /\n\n' for b in AI_BOTS) + 'Sitemap: https://getbusted.online/sitemap.xml\n'
LLMS = """# Get Busted

> Get Busted is a party card game app for adults (18+) on iPhone and Android, made in Norway. One person holds the phone and reads the cards out loud; everyone else plays together. 2 to 30 players. Separate card decks written for English, Swedish, Danish and Norwegian speakers (not translations).

Key facts:
- Levels: Mild, Cheeky and Get Fu**ed (the most adult level).
- Theme packs: Original, Halloween, Christmas, Afterparty, The Cabin at launch; Travel, Student, Stag & Hen, Football and Sport later. Sweden-only packs: Mello, Midsommar, Kräftskiva. English-only: Friendsgiving, St. Paddy's.
- Modes and features: team play (duos or Red vs Blue), Rapid rounds, secret missions, twists, odds cards, song cards, big text, "the night in numbers" summary, alcohol-free mode with points.
- Pricing: free to start (50 Original cards every night). Theme packs and the Get Fu**ed level are one-time purchases. Busted+ unlocks everything with one payment. No subscription, no ads.
- Responsible play: a card never asks for more than 6 sips, water breaks, alcohol-free mode, any card can be skipped.
- Publisher: Snikkerbua Holding AS (Norway, org. no. 927 118 300), Voldgata 27, 2000 Lillestrøm. Contact: kontakt@getbusted.no

## Pages
- [English](https://getbusted.online/): overview, packs, prices, FAQ
- [Svenska](https://getbusted.online/se/): partyspel för vuxna, svenska kort
- [Dansk](https://getbusted.online/dk/): festspil for voksne, danske kort
- [Norsk](https://getbusted.no/): festspill for voksne, norske kort
- [Help](https://getbusted.online/help/)
- [Purchases & refunds](https://getbusted.online/purchases/)
- [Privacy](https://getbusted.online/privacy/)
"""

(ROOT / 'robots.txt').write_text(ROBOTS)
(ROOT / 'llms.txt').write_text(LLMS, encoding='utf-8')


# Sitemap med hreflang mellom språkene. Norsk hjelpeside finnes ikke, så hjelpesidene lenker bare en/sv/da.
def sm_entry(loc, alt, langs):
    links = ''.join(f'\n  <xhtml:link rel="alternate" hreflang="{l}" href="{full(alt[l])}"/>' for l in langs)
    return f'<url>\n  <loc>{full(loc)}</loc>{links}\n  <xhtml:link rel="alternate" hreflang="x-default" href="{full(alt["en"])}"/>\n</url>'
entries = []
for alt, langs in ((HOME, LANGS + ['no']), (HELP, LANGS), (LP_ALT['xmas'], LANGS + ['no']), (LP_ALT['cabin'], LANGS + ['no']), (LP_ALT['wed'], LANGS + ['no']), (PRIV, LANGS + ['no']), (TERMS, LANGS + ['no']), (COOK, LANGS + ['no']), (BUY, LANGS + ['no'])):
    for l in LANGS:
        entries.append(sm_entry(alt[l], alt, langs))
(ROOT / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + '\n'.join(entries) + '\n</urlset>\n', encoding='utf-8')
(ROOT / '404.html').write_text("<!doctype html><meta charset='utf-8'><title>Get Busted</title><meta http-equiv='refresh' content='0;url=/'><a href='/'>Get Busted</a>\n")
print('ok')
