# Bygger getbusted.online: engelsk på /, svensk på /sv/ og dansk på /dk/ (/da/ sender videre). Norsk ligger på getbusted.no.
# Hver språkblokk gir forside, hjelpeside og personvernside.
# Kjør: python3 build.py
import html, pathlib, re
E = html.escape
ROOT = pathlib.Path(__file__).parent
SITE = 'https://getbusted.online'
MAIL = 'kontakt@getbusted.no'

# Adresser per språk. 'no' ligger på getbusted.no.
HOME = {'en': '/', 'sv': '/sv/', 'da': '/dk/', 'no': 'https://getbusted.no/'}
HELP = {'en': '/help/', 'sv': '/sv/hjalp/', 'da': '/dk/hjaelp/', 'no': 'https://getbusted.no/hjelp/'}
PRIV = {'en': '/privacy/', 'sv': '/sv/integritet/', 'da': '/dk/privatliv/', 'no': 'https://getbusted.no/personvern/'}
LANGS = ['en', 'sv', 'da']

T = {
 'en': dict(
  path='/', lang='en', hero='en', title='Get Busted - the party game that runs the night',
  desc='Get Busted is the party card game for pregames, afterparties and cabin weekends. 2,000+ cards in English about the internet, the news and your group chat. Adults 18+.',
  og='One reader, 2,000+ cards and zero boring breaks. For iPhone and Android.',
  nav=[('#how', 'How it works'), ('#packs', 'Packs'), ('#faq', 'FAQ')], download='Download',
  h1='The party game that runs the night',
  lead='One reader holds the phone. Everyone else looks at each other, not at a screen. 2,000+ cards in English about the internet, the news and your group chat, plus Rapid rounds, secret missions and song cards.',
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
  help='Help', privacy='Privacy', contact='Contact', foot='Adults 18+ · Drink responsibly',
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
  privTitle='Privacy policy - Get Busted', privDesc='How Get Busted handles data: no accounts, no ads, no tracking.',
  privK='Privacy',
  priv=dict(
   h1='Privacy policy for Get Busted', updated='Last updated: [date at launch]',
   sections=[
    ('In short', ['Get Busted has no user accounts, no ads and no tracking. The names you enter and your settings are stored only on the phone. The only thing that goes over the internet is purchases of packs, which are handled by Apple or Google.']),
    ('Who is responsible', [f'Snikkerbua Holding AS, org. no. 927 118 300, Floraveien 22B, 2007 Kjeller, Norway. Contact: <a href="mailto:{MAIL}">{MAIL}</a>.']),
    ('What is stored on your phone', [['Player names, chosen packs and settings, so you do not have to enter them again.',
                                       'A game in progress, so you can continue where you left off.',
                                       'That you have confirmed that you are over 18.'],
                                      'This is never sent to us or anyone else. It is deleted when you delete the app.']),
    ('Purchases', ['Purchases are made through the Apple App Store or Google Play, and they process the payment. We never receive card details or your name. To know which packs you own, we use the service RevenueCat, which receives a random, anonymous ID and the purchase history linked to it. RevenueCat is our data processor and may store data in the USA, based on the EU Standard Contractual Clauses. The legal basis is that it is necessary to deliver what you have bought (GDPR Art. 6(1)(b)).']),
    ('Links to other services', ["The song cards have a button that opens Spotify. Spotify's own terms and privacy policy then apply."]),
    ('Age limit', ['Get Busted is made for adults over 18.']),
    ('Your rights', ['You can ask for access to, correction of or deletion of information we have about you by contacting us. Since we have no name or contact details linked to purchases, you must provide the purchase date or the receipt from Apple or Google. You can also complain to the Norwegian Data Protection Authority, <a href="https://www.datatilsynet.no">Datatilsynet</a>.']),
    ('Changes', ['If we change how the app processes data, we will update this page and the date at the top.']),
   ]),
 ),
 'sv': dict(
  path='/sv/', lang='sv', hero='sv', title='Get Busted - festspelet som styr kvällen',
  desc='Get Busted är kortspelet för förfesten, efterfesten och stugan. 2 500+ kort skrivna för Sverige, inte översatta. För vuxna 18+.',
  og='En läsare, 2 500+ kort och noll tråkiga pauser. För iPhone och Android.',
  nav=[('#how', 'Så funkar det'), ('#packs', 'Paket'), ('#faq', 'Frågor')], download='Ladda ner',
  h1='Festspelet som styr kvällen',
  lead='En person håller i telefonen och läser högt. Resten tittar på varandra, inte på en skärm. 2 500+ kort skrivna för Sverige: Systemet som stänger 15, Kalle Anka klockan tre, 08:or och norrlänningar.',
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
            ('midsommar', 'cover_midsommar.jpg', 'Midsommar', 'Sill, nubbe och regn', '2027-06-04'),
            ('kraftskiva', 'cover_kraftskiva.jpg', 'Kräftskiva', 'Pappershattar och snapsvisor', '2027-07-30')],
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
  help='Hjälp', privacy='Integritet', contact='Kontakt', foot='För vuxna 18+ · Drick ansvarsfullt',
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
  privTitle='Integritetspolicy - Get Busted', privDesc='Så hanterar Get Busted data: inga konton, ingen reklam, ingen spårning.',
  privK='Integritet',
  priv=dict(
   h1='Integritetspolicy för Get Busted', updated='Senast uppdaterad: [datum vid lansering]',
   sections=[
    ('Kort sagt', ['Get Busted har inga användarkonton, ingen reklam och ingen spårning. Namnen ni skriver in och era inställningar sparas bara på telefonen. Det enda som går via internet är köp av paket, som hanteras av Apple eller Google.']),
    ('Vem är ansvarig', [f'Snikkerbua Holding AS, org.nr 927 118 300, Floraveien 22B, 2007 Kjeller, Norge. Kontakt: <a href="mailto:{MAIL}">{MAIL}</a>.']),
    ('Vad som sparas på din telefon', [['Spelarnamn, valda paket och inställningar, så att ni slipper skriva in dem igen.',
                                        'Ett pågående spel, så att ni kan fortsätta där ni slutade.',
                                        'Att du har bekräftat att du är över 18 år.'],
                                       'Detta skickas aldrig till oss eller någon annan. Det raderas när du raderar appen.']),
    ('Köp', ['Köp görs via Apple App Store eller Google Play, och det är de som hanterar betalningen. Vi får aldrig kortuppgifter eller ditt namn. För att veta vilka paket du äger använder vi tjänsten RevenueCat, som tar emot ett slumpmässigt, anonymt ID och den köphistorik som hör till det. RevenueCat är personuppgiftsbiträde åt oss och kan lagra data i USA, med EU:s standardavtalsklausuler som grund. Den rättsliga grunden är att det är nödvändigt för att leverera det du har köpt (GDPR art. 6.1 b).']),
    ('Länkar till andra tjänster', ['Låtkorten har en knapp som öppnar Spotify. Då gäller Spotifys egna villkor och integritetspolicy.']),
    ('Åldersgräns', ['Get Busted är gjort för vuxna över 18 år.']),
    ('Dina rättigheter', ['Du kan begära tillgång till, rättelse eller radering av uppgifter vi har om dig genom att kontakta oss. Eftersom vi inte har namn eller kontaktuppgifter kopplade till köp behöver du ange köpdatum eller kvittot från Apple eller Google. Du kan också klaga till den norska dataskyddsmyndigheten, <a href="https://www.datatilsynet.no">Datatilsynet</a>.']),
    ('Ändringar', ['Om vi ändrar hur appen behandlar data uppdaterar vi den här sidan och datumet högst upp.']),
   ]),
 ),
 'da': dict(
  path='/dk/', lang='da', hero='sv', title='Get Busted - festspillet der styrer aftenen',
  desc='Get Busted er festspillet til forfesten, efterfesten og sommerhuset. 1.000+ kort, med eller uden alkohol. For voksne 18+.',
  og='Én oplæser, 1.000+ kort og ingen kedelige pauser. Til iPhone og Android.',
  nav=[('#how', 'Sådan virker det'), ('#packs', 'Pakker'), ('#faq', 'Spørgsmål')], download='Hent',
  h1='Festspillet der styrer aftenen',
  lead='Én person holder telefonen og læser højt. Resten kigger på hinanden, ikke på en skærm. 1.000+ kort med «Drik hvis du har», Rapid-runder, hemmelige missioner og sangkort.',
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
  packsLead='Fire temapakker fra start og en ny pakke hver uge hen over efteråret. Prøv 5 kort fra en hvilken som helst pakke gratis, før du køber.',
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
  resp=[('Max 6', 'Uanset niveau beder et kort aldrig om mere end 6 tårer.'),
        ('Vandpauser', 'De kommer oftere, jo tørstigere I siger, I er.'),
        ('Alkoholfri', 'Samme spil med point i stedet for tårer. Alle kan være med.'),
        ('Spring over', 'Du må altid springe et kort over. Altid.')],
  faqK='Spørgsmål', faqH='Ofte stillede spørgsmål',
  faq=[('Er det gratis?', 'Ja. Du får 50 kort fra Original gratis hver aften. Temapakkerne er engangskøb, Aftenpakken giver dig én pakke plus Get Fu**ed-niveauet, og Busted+ låser hele appen op med én betaling. Intet abonnement.'),
       ('Skal vi drikke?', 'Nej. Slå alkoholfri tilstand til, så bliver hver tår til et point. Og det er altid i orden at springe over.'),
       ('Hvor mange kan spille?', 'Fra 2 til 30. Store grupper får flere kort, der gælder alle på én gang.'),
       ('Kan vi spille på hold?', 'Ja. Vælg duoer eller to hold, Rød mod Blå, når I sætter spillet op. Appen holder styr på stillingen.'),
       ('Hvilke sprog?', 'Dansk, svensk, engelsk og norsk, med egne kort og menuer. Vælg sprog på startskærmen.'),
       ('Hvornår kommer den?', 'Snart til iPhone og Android.')],
  help='Hjælp', privacy='Privatliv', contact='Kontakt', foot='For voksne 18+ · Drik med omtanke',
  helpTitle='Hjælp - Get Busted', helpDesc='Svar om Get Busted: sådan spiller I, gendan køb, indløs kode, alkoholfri tilstand og mere.',
  helpK='Hjælp', helpH='Spørgsmål og svar',
  helpQA=[('Hvordan spiller man?', 'Skriv navnene ind (2 til 30 spillere), og vælg pakker, niveau og hvor tørstige I er. Én person er oplæser: vedkommende holder telefonen og læser alle kortene højt. Swipe eller tryk for næste kort, og tryk i venstre kant af kortet for at gå tilbage. I kan skifte oplæser og tilføje eller fjerne spillere når som helst ved at trykke på navnet øverst.'),
          ('Hvordan gendanner jeg mine køb?', 'Åbn Pakker i appen, og tryk på Gendan køb under «Har du købt før?». Brug det samme Apple-id eller Google-konto, som du købte med. Du behøver ikke en konto hos os.'),
          ('Hvordan indløser jeg en kode?', 'Åbn Pakker, og tryk på Indløs kode. På iPhone åbner Apple et vindue, hvor du skriver koden. På Android åbner Google Play, så du kan indløse den der.'),
          ('Hvordan virker alkoholfri tilstand?', 'Vælg Alkoholfri, når I sætter spillet op. Det er samme spil, men tårer bliver til point, og den med flest point taber. Alle kan spille sammen, med eller uden noget i glasset.'),
          ('Er teksten svær at læse?', 'Vælg Stor tekst, når I sætter spillet op, eller tryk på Aa under spillet for at skifte.'),
          ('Hvorfor 18+?', 'Get Busted er et festspil for voksne. Appen beder dig bekræfte, at du er 18 år eller ældre, første gang du åbner den. Er du under 18, kan du ikke bruge appen.'),
          ('Kan jeg springe et kort over?', 'Ja, altid. Gå bare videre til næste kort. Ingen skal gøre noget, de ikke har lyst til.'),
          ('Noget andet?', f'Skriv til <a href="mailto:{MAIL}">{MAIL}</a>. Gælder det et køb, så send købsdato eller kvitteringen fra Apple eller Google med.')],
  privTitle='Privatlivspolitik - Get Busted', privDesc='Sådan håndterer Get Busted data: ingen konti, ingen reklamer, ingen sporing.',
  privK='Privatliv',
  priv=dict(
   h1='Privatlivspolitik for Get Busted', updated='Sidst opdateret: [dato ved lancering]',
   sections=[
    ('Kort fortalt', ['Get Busted har ingen brugerkonti, ingen reklamer og ingen sporing. De navne, I skriver ind, og jeres indstillinger gemmes kun på telefonen. Det eneste, der går via internettet, er køb af pakker, som håndteres af Apple eller Google.']),
    ('Hvem er ansvarlig', [f'Snikkerbua Holding AS, org.nr. 927 118 300, Floraveien 22B, 2007 Kjeller, Norge. Kontakt: <a href="mailto:{MAIL}">{MAIL}</a>.']),
    ('Hvad der gemmes på din telefon', [['Spillernavne, valgte pakker og indstillinger, så I slipper for at skrive dem ind igen.',
                                         'Et igangværende spil, så I kan fortsætte, hvor I slap.',
                                         'At du har bekræftet, at du er over 18 år.'],
                                        'Dette sendes aldrig til os eller andre. Det slettes, når du sletter appen.']),
    ('Køb', ['Køb foregår gennem Apple App Store eller Google Play, og det er dem, der behandler betalingen. Vi får aldrig kortoplysninger eller dit navn. For at vide, hvilke pakker du ejer, bruger vi tjenesten RevenueCat, som modtager et tilfældigt, anonymt id og den købshistorik, der er knyttet til det. RevenueCat er databehandler for os og kan opbevare data i USA med EU\'s standardkontraktbestemmelser som grundlag. Behandlingsgrundlaget er, at det er nødvendigt for at levere det, du har købt (GDPR art. 6, stk. 1, litra b).']),
    ('Links til andre tjenester', ['Sangkortene har en knap, der åbner Spotify. Så gælder Spotifys egne vilkår og privatlivspolitik.']),
    ('Aldersgrænse', ['Get Busted er lavet til voksne over 18 år.']),
    ('Dine rettigheder', ['Du kan bede om indsigt i, berigtigelse eller sletning af oplysninger, vi har om dig, ved at kontakte os. Da vi ikke har navn eller kontaktoplysninger knyttet til køb, skal du oplyse købsdato eller kvitteringen fra Apple eller Google. Du kan også klage til den norske tilsynsmyndighed, <a href="https://www.datatilsynet.no">Datatilsynet</a>.']),
    ('Ændringer', ['Hvis vi ændrer, hvordan appen behandler data, opdaterer vi denne side og datoen øverst.']),
   ]),
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
ICONS = ['✨', '🔄', '⚡', '🤫', '🎵', '⚔️', '🎯', '🔠', '📊']
SHOTS = ['3_lag', '4_vri', '5_rapid', '6_odds', '7_stortekst', '8_halloween']
UPDATE = {
 'en': dict(
  desc='Get Busted is the party card game for game nights, house parties and cabin weekends. 2,200+ cards written in English, team play, Rapid rounds and secret missions. Adults 18+.',
  og='One reader, 2,200+ cards and zero boring breaks. For iPhone and Android.',
  h1=('The party game that ', 'runs the night', ''),
  lead='One reader holds the phone. Everyone else looks at each other, not at a screen. 2,200+ cards about the internet, the news and your group chat, plus team play, Rapid rounds and secret missions.',
  soonTo='30 October on', note='For adults 18+. Alcohol-free mode is always included.', download='30 October',
  steps=[('Add your crew', '2 to 30 players. Names go straight onto the cards, so nobody gets to hide.'),
         ('Pick packs and level', 'Mild, Cheeky or Get Fu**ed. Play solo, in fixed duos or Red vs Blue.'),
         ('Read out loud and play', 'The reader reads the cards. The dice, the twists and the Rapid rounds show up on their own.')],
  stats=[('2,200+', 'cards in English'), ('12', 'packs'), ('2-30', 'players'), ('Free', 'to get started')],
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
  desc='Get Busted är festspelet för spelkvällen, festen och stugan. 2 600+ kort skrivna för Sverige, lagspel, Rapid och hemliga uppdrag. För vuxna 18+.',
  og='En läsare, 2 600+ kort och noll tråkiga pauser. För iPhone och Android.',
  h1=('Festspelet som ', 'tar över', ' kvällen'),
  lead='En person håller i telefonen och läser högt. Resten tittar på varandra, inte på en skärm. 2 600+ kort skrivna för Sverige, inte översatta, plus lagspel, Rapid och hemliga uppdrag.',
  soonTo='30 oktober i', note='För vuxna 18+. Alkoholfritt läge finns alltid med.', download='30 oktober',
  steps=[('Skriv in gänget', '2 till 30 spelare. Namnen hamnar direkt på korten, så ingen kan gömma sig.'),
         ('Välj paket och nivå', 'Mild, Fräck eller Get Fu**ed. Spela var för sig, i fasta duos eller Röd mot Blå.'),
         ('Läs högt och kör', 'Läsaren läser korten. Tärningen, twistarna och Rapid-rundorna dyker upp av sig själva.')],
  stats=[('2 600+', 'kort på svenska'), ('13', 'paket'), ('2-30', 'spelare'), ('0 kr', 'för att komma igång')],
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
  desc='Get Busted er festspillet til spilleaftenen, festen og sommerhuset. 1.900+ danske kort, holdspil, Rapid og hemmelige missioner. For voksne 18+.',
  og='Én oplæser, 1.900+ kort og ingen kedelige pauser. Til iPhone og Android.',
  h1=('Festspillet der ', 'tager over', ' aftenen'),
  lead='Én person holder telefonen og læser højt. Resten kigger på hinanden, ikke på en skærm. 1.900+ kort skrevet på dansk, holdspil, Rapid-runder og hemmelige missioner.',
  soonTo='30. oktober i', note='For voksne 18+. Alkoholfri tilstand er altid med.', download='30. oktober',
  steps=[('Skriv flokken ind', '2 til 30 spillere. Navnene kommer direkte på kortene, så ingen kan gemme sig.'),
         ('Vælg pakker og niveau', 'Mild, Fræk eller Get Fu**ed. Spil hver for sig, i faste par eller Rød mod Blå.'),
         ('Læs højt og spil', 'Oplæseren læser kortene. Terningen, twistene og Rapid-runderne dukker op af sig selv.')],
  stats=[('1.900+', 'kort på dansk'), ('10', 'pakker'), ('2-30', 'spillere'), ('0 kr', 'for at komme i gang')],
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
    items = [('EN', 'en'), ('SV', 'sv'), ('DK', 'da'), ('NO', 'no')]
    return "<span class='langs'>" + ''.join(
        f"<a href='{alt[l]}' data-lang='{l}'{CUR if l == t['lang'] else ''}>{n}</a>" for n, l in items) + "</span>"

def full(p):
    return p if p.startswith('http') else SITE + p

REDIRECT = """<script>
// Første besøk fra en svensk eller dansk telefon: send til /sv/ eller /dk/. Valgt språk huskes.
try { var c = localStorage.getItem('gb-lang'), l = navigator.language || '';
  if (!c && /^sv\\b/i.test(l)) location.replace('/sv/');
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
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Semi+Condensed:ital,wght@0,500;0,700;0,800;1,800;1,900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css">
<link rel="stylesheet" href="/online.css">
{REDIRECT if redirect and t['lang'] == 'en' else ''}
</head>
<body>
<header class="nav">
  <div class="wrap">
    <a class="brand" href="{home}"><img src="/img/logo.png" alt="">Get Busted</a>
    <nav>
      {nav}
      {langbar(t, alt)}
      <a class="cta" href="{dl}">{E(t['download'])}</a>
    </nav>
  </div>
</header>

<main>
{body}
</main>

<footer>
  <div class="wrap">
    <div><a href="{HELP[t['lang']]}">{E(t['help'])}</a><a href="{PRIV[t['lang']]}">{E(t['privacy'])}</a><a href="mailto:{MAIL}">{E(t['contact'])}</a>{langbar(t, alt)}</div>
    <div>© 2026 Get Busted · Snikkerbua Holding AS, org.nr. 927 118 300 · {E(t['foot'])}</div>
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
    faq = ''.join(f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q, a in t['faq'])
    doors = ''.join(f"<i class='{'o' if d < 7 else ('t' if d == 7 else '')}'>{d}</i>" for d in range(1, 25))
    cal = ''.join(f"<li>{E(x)}</li>" for x in u['calList'])
    prices = ''.join(f"<div class='price'><h3>{E(h)}</h3><p>{E(p)}</p></div>" for h, p in t['prices'][:3])
    ph, pp = t['prices'][3]
    pp = re.sub(r'\s*[^.]*(aunch price|anseringspris|anceringspris)[^.]*\.', '', pp)
    plus = f"<div class='price plus'><div><h3>{E(ph)}</h3></div><div><p>{E(pp)}</p><span class='tag'>{E(u['plusTag'])}</span></div></div>"
    start = [x for x in t['packs'] if not x[4]]
    later = [x for x in t['packs'] if x[4]]
    groups = [(u['groups'][0], start), (u['groups'][1], later)] + ([(u['groups'][2], t['specials'])] if t['specials'] else [])
    packs_html = ''.join(f"<div class='group'><h3>{E(g)}</h3><div class='packs'>\n      {packs(lst, t)}\n    </div></div>" for g, lst in groups)
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
        <span class="badge">{apple}<span><small>{E(t['soonTo'])}</small><b>App Store</b></span></span>
        <span class="badge">{play}<span><small>{E(t['soonTo'])}</small><b>Google Play</b></span></span>
      </div>
      <p class="note">{E(t['note'])}</p>
    </div>
    <div class="stage" aria-hidden="true">
      <img class="cover l" src="/img/cover_halloween.jpg" alt="" style="--c:#FF8A1F" width="360" height="503">
      <img class="cover r" src="/img/{jul}" alt="" style="--c:#E0473E" width="360" height="503">
      <picture class="card"><source srcset="/img/card_hero_{L}.webp" type="image/webp"><img src="/img/card_hero_{L}.png" alt="" width="600" height="841"></picture>
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
    <div class="shots">{shots}</div>
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

def privacy_page(t):
    p = t['priv']
    parts = []
    for h, items in p['sections']:
        parts.append(f"<h2>{E(h)}</h2>")
        for it in items:
            if isinstance(it, list):
                parts.append('<ul>' + ''.join(f'<li>{E(li)}</li>' for li in it) + '</ul>')
            else:
                parts.append(f'<p>{it}</p>')
    body = f"""<article class="article">
  <p class="kicker">{E(t['privK'])}</p>
  <h1>{E(p['h1'])}</h1>
  <p class="meta">{E(p['updated'])}</p>
  {''.join(parts)}
</article>"""
    return shell(t, PRIV, t['privTitle'], t['privDesc'], body)

def write(path, text):
    f = ROOT / path.lstrip('/') / 'index.html'
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(text, encoding='utf-8')

for lang in LANGS:
    t = T[lang]
    write(HOME[lang], home(t))
    write(HELP[lang], help_page(t))
    write(PRIV[lang], privacy_page(t))

(ROOT / 'online.css').write_text(""".langs{display:inline-flex;gap:6px;margin:0 6px 0 16px}
.langs a{padding:4px 8px;border:1px solid #555;border-radius:8px;font-weight:800;font-size:13px;letter-spacing:1px;opacity:.75;margin-left:0!important}
.langs a[aria-current]{border-color:#B7D147;color:#B7D147;opacity:1}
footer .langs{margin-left:0}
.pricing.three{grid-template-columns:repeat(3,1fr)}
.price.plus h3{font-size:clamp(40px,5vw,64px);text-shadow:0 0 30px rgba(183,209,71,.4)}
.article h1{overflow-wrap:break-word}
@media (max-width:900px){.pricing.three{grid-template-columns:1fr}}
@media (max-width:760px){.nav nav .langs{display:inline-flex;margin:0 4px}.nav nav .langs a{display:inline-block}.nav nav a.cta{display:none}.nav .brand{white-space:nowrap;font-size:19px}.nav .brand img{width:34px;height:34px}.langs a{padding:4px 6px}}
""", encoding='utf-8')
(ROOT / 'CNAME').write_text('getbusted.online\n')
# Gamle danske adresser (/da/) sender videre til /dk/
for _old, _new in (('/da/', '/dk/'), ('/da/hjaelp/', '/dk/hjaelp/'), ('/da/privatliv/', '/dk/privatliv/')):
    write(_old, f"<!doctype html><meta charset='utf-8'><title>Get Busted</title><link rel='canonical' href='{SITE}{_new}'><meta http-equiv='refresh' content='0;url={_new}'><a href='{_new}'>Get Busted</a>\n")
(ROOT / 'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: https://getbusted.online/sitemap.xml\n')

# Sitemap med hreflang mellom språkene. Norsk hjelpeside finnes ikke, så hjelpesidene lenker bare en/sv/da.
def sm_entry(loc, alt, langs):
    links = ''.join(f'\n  <xhtml:link rel="alternate" hreflang="{l}" href="{full(alt[l])}"/>' for l in langs)
    return f'<url>\n  <loc>{full(loc)}</loc>{links}\n  <xhtml:link rel="alternate" hreflang="x-default" href="{full(alt["en"])}"/>\n</url>'
entries = []
for alt, langs in ((HOME, LANGS + ['no']), (HELP, LANGS), (PRIV, LANGS + ['no'])):
    for l in LANGS:
        entries.append(sm_entry(alt[l], alt, langs))
(ROOT / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + '\n'.join(entries) + '\n</urlset>\n', encoding='utf-8')
(ROOT / '404.html').write_text("<!doctype html><meta charset='utf-8'><title>Get Busted</title><meta http-equiv='refresh' content='0;url=/'><a href='/'>Get Busted</a>\n")
print('ok')
