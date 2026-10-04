# Bygger getbusted.online: engelsk på / og svensk på /sv/. Norsk ligger på getbusted.no.
# Kjør: python3 build.py
import html, json, pathlib
E = html.escape
ROOT = pathlib.Path(__file__).parent

T = {
 'en': dict(
  path='/', lang='en', title='Get Busted - the party game that runs the night',
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
          ('Busted+', 'The whole app: every pack, including future ones, the Get Fu**ed level and unlimited Original. Pay once, no subscription.')],
  respK='Play smart', respH='Made for a good night, not a bad morning',
  resp=[('Max 6', 'Whatever the level, a card never asks for more than 6 sips.'),
        ('Water breaks', 'They come more often the thirstier you say you are.'),
        ('Alcohol-free', 'The same game with points instead of sips. Everyone can join.'),
        ('Skip', 'You can always skip a card. Always.')],
  faqK='Questions', faqH='FAQ',
  faq=[('Is it free?', 'Yes. You get 50 cards from the Original deck for free every night. Theme packs are one-time purchases, and Busted+ unlocks the whole app with one payment. No subscription.'),
       ('Do we have to drink?', 'No. Turn on alcohol-free mode and every sip becomes a point. And skipping is always allowed.'),
       ('How many can play?', 'From 2 to 30. Big groups get more cards that apply to everyone at once.'),
       ('Which languages?', 'English, Swedish and Norwegian, each with its own cards and menus. Pick the language on the start screen.'),
       ('When is it out?', 'Soon on iPhone and Android. Follow @getbusted.uk on Instagram and TikTok to hear first.')],
  privacy='Privacy', contact='Contact', foot='Adults 18+ · Drink responsibly',
 ),
 'sv': dict(
  path='/sv/', lang='sv', title='Get Busted - festspelet som styr kvällen',
  desc='Get Busted är kortspelet för förfesten, efterfesten och stugan. 2 500+ kort skrivna för Sverige, inte översatta. För vuxna 18+.',
  og='En läsare, 2 500+ kort och noll tråkiga pauser. För iPhone och Android.',
  nav=[('#how', 'Så funkar det'), ('#packs', 'Paket'), ('#faq', 'Frågor')], download='Ladda ner',
  h1='Festspelet som styr kvällen',
  lead='En person håller i telefonen och läser högt. Resten tittar på varandra, inte på en skärm. 2 500+ kort skrivna för Sverige: Systemet som stänger 15, Kalle Anka klockan tre, 08:or och norrlänningar.',
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
          ('Busted+', 'Hela appen: alla paket, även de som kommer, Get Fu**ed-nivån och obegränsat Original. Betala en gång, ingen prenumeration.')],
  respK='Spela smart', respH='Gjort för en bra kväll, inte en dålig morgon',
  resp=[('Max 6', 'Oavsett nivå ber ett kort aldrig om mer än 6 klunkar.'),
        ('Vattenpauser', 'De kommer oftare ju törstigare ni säger att ni är.'),
        ('Alkoholfritt', 'Samma spel med poäng i stället för klunkar. Alla kan vara med.'),
        ('Stå över', 'Du får alltid stå över ett kort. Alltid.')],
  faqK='Frågor', faqH='Vanliga frågor',
  faq=[('Är det gratis?', 'Ja. Du får 50 kort från Original gratis varje kväll. Temapaketen är engångsköp, och Busted+ låser upp hela appen med en betalning. Ingen prenumeration.'),
       ('Måste vi dricka?', 'Nej. Slå på alkoholfritt läge så blir varje klunk ett poäng. Och det är alltid okej att stå över.'),
       ('Hur många kan spela?', 'Från 2 till 30. Stora gäng får fler kort som gäller alla samtidigt.'),
       ('Vilka språk?', 'Svenska, engelska och norska, med egna kort och menyer. Välj språk på startsidan.'),
       ('När kommer den?', 'Snart till iPhone och Android. Följ @getbusted.se på Instagram och TikTok så får du veta först.')],
  privacy='Integritet', contact='Kontakt', foot='För vuxna 18+ · Drick ansvarsfullt',
 ),
}

def label(d, t):
    y, m, dd = d.split('-')
    return f"{t['soon']} {int(dd)} {t['months'][int(m)-1]}" if t['lang'] == 'sv' else f"{t['soon']} {t['months'][int(m)-1]} {int(dd)}"

def packs(lst, t):
    out = []
    for slug, img, name, sub, rel in lst:
        soon = f"<i class='soon'>{E(label(rel, t))}</i>" if rel else ''
        dr = f" data-release='{rel}'" if rel else ''
        out.append(f"<div class='pack' data-pack='{slug}'{dr}><img src='/img/{img}' alt='' loading='lazy'><b>{E(name)}</b><span>{E(sub)}</span>{soon}</div>")
    return "\n      ".join(out)

CUR = ' aria-current="page"'

def langbar(t):
    items = [('/', 'EN', 'en'), ('/sv/', 'SV', 'sv'), ('https://getbusted.no/', 'NO', 'no')]
    return "<span class='langs'>" + ''.join(
        f"<a href='{h}' data-lang='{l}'{CUR if l == t['lang'] else ''}>{n}</a>" for h, n, l in items) + "</span>"

def page(t):
    url = 'https://getbusted.online' + t['path']
    steps = ''.join(f"<div class='step'><div class='n'>{i}</div><h3>{E(h)}</h3><p>{E(p)}</p></div>" for i, (h, p) in enumerate(t['steps'], 1))
    feats = ''.join(f"<div class='feature'><h3>{E(h)}</h3><p>{E(p)}</p></div>" for h, p in t['feats'])
    prices = ''.join(f"<div class='price'><div class='amt'>{E(h)}</div><p>{E(p)}</p></div>" for h, p in t['prices'])
    resp = ''.join(f"<div><b>{E(h)}</b><p>{E(p)}</p></div>" for h, p in t['resp'])
    faq = ''.join(f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q, a in t['faq'])
    nav = ''.join(f"<a href='{h}'>{E(n)}</a>" for h, n in t['nav'])
    redirect = '' if t['lang'] != 'en' else """<script>
// Første besøk fra en svensk telefon: send til /sv/. Valgt språk huskes.
try { var c = localStorage.getItem('gb-lang');
  if (!c && /^sv\\b/i.test(navigator.language || '')) location.replace('/sv/'); } catch (e) {}
</script>"""
    return f"""<!doctype html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(t['title'])}</title>
<meta name="description" content="{E(t['desc'])}">
<meta property="og:title" content="{E(t['title'])}">
<meta property="og:description" content="{E(t['og'])}">
<meta property="og:image" content="https://getbusted.online/img/og.jpg">
<meta property="og:url" content="{url}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en" href="https://getbusted.online/">
<link rel="alternate" hreflang="sv" href="https://getbusted.online/sv/">
<link rel="alternate" hreflang="no" href="https://getbusted.no/">
<link rel="alternate" hreflang="x-default" href="https://getbusted.online/">
<meta name="theme-color" content="#2B2B2B">
<link rel="icon" href="/img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Semi+Condensed:ital,wght@0,500;0,700;0,800;1,800;1,900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css">
<link rel="stylesheet" href="/online.css">
{redirect}
</head>
<body>
<header class="nav">
  <div class="wrap">
    <a class="brand" href="{t['path']}"><img src="/img/logo.png" alt="">Get Busted</a>
    <nav>
      {nav}
      {langbar(t)}
      <a class="cta" href="#download">{E(t['download'])}</a>
    </nav>
  </div>
</header>

<main>
<section class="hero">
  <div class="wrap">
    <div>
      <img class="logo" src="/img/logo.png" alt="Get Busted">
      <h1>{E(t['h1'])}</h1>
      <p class="lead">{E(t['lead'])}</p>
      <div class="badges" id="download">
        <span class="badge"><small>{E(t['soonTo'])}</small><b>App Store</b></span>
        <span class="badge"><small>{E(t['soonTo'])}</small><b>Google Play</b></span>
      </div>
      <p class="note">{E(t['note'])}</p>
    </div>
    <div class="phone"><picture><source srcset="/img/hero_{t['lang']}.webp" type="image/webp"><img src="/img/hero_{t['lang']}.png" alt="{E(t['heroAlt'])}" width="470" height="960"></picture></div>
  </div>
</section>

<section id="how" class="alt">
  <div class="wrap">
    <p class="kicker">{E(t['howK'])}</p>
    <h2>{E(t['howH'])}</h2>
    <div class="steps">{steps}</div>
  </div>
</section>

<section>
  <div class="wrap">
    <p class="kicker">{E(t['featK'])}</p>
    <h2>{E(t['featH'])}</h2>
    <div class="features">{feats}</div>
  </div>
</section>

<section id="packs" class="alt">
  <div class="wrap">
    <p class="kicker">{E(t['packsK'])}</p>
    <h2>{E(t['packsH'])}</h2>
    <p class="lead">{E(t['packsLead'])}</p>
    <div class="packs">
      {packs(t['packs'], t)}
    </div>
    <p class="kicker" style="margin-top:48px">{E(t['specialsK'])}</p>
    <h2>{E(t['specialsH'])}</h2>
    <div class="packs">
      {packs(t['specials'], t)}
    </div>
    <div class="pricing">{prices}</div>
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
</section>
</main>

<footer>
  <div class="wrap">
    <div><a href="https://getbusted.no/personvern/#en">{E(t['privacy'])}</a><a href="mailto:kontakt@getbusted.no">{E(t['contact'])}</a>{langbar(t)}</div>
    <div>© 2026 Get Busted · Snikkerbua Holding AS, org.nr. 927 118 300 · {E(t['foot'])}</div>
  </div>
</footer>
<script>
// Språkvalg huskes; «Kommer»-merket forsvinner på slippdagen.
document.querySelectorAll('.langs a').forEach(function (a) {{ a.addEventListener('click', function () {{ try {{ localStorage.setItem('gb-lang', a.dataset.lang); }} catch (e) {{}} }}); }});
var now = Date.now();
document.querySelectorAll('[data-release]').forEach(function (p) {{ if (now >= new Date(p.dataset.release + 'T00:00:00+01:00').getTime()) {{ var s = p.querySelector('.soon'); if (s) s.remove(); }} }});
</script>
</body>
</html>
"""

(ROOT / 'index.html').write_text(page(T['en']), encoding='utf-8')
(ROOT / 'sv' / 'index.html').write_text(page(T['sv']), encoding='utf-8')
(ROOT / 'online.css').write_text(""".langs{display:inline-flex;gap:6px;margin:0 6px}
.langs a{padding:4px 8px;border:1px solid #555;border-radius:8px;font-weight:800;font-size:13px;letter-spacing:1px;opacity:.75}
.langs a[aria-current]{border-color:#B7D147;color:#B7D147;opacity:1}
footer .langs{margin-left:12px}
@media (max-width:640px){.nav nav .langs a{display:inline-block;margin-left:0}.nav nav .langs{margin:0 4px}.nav nav a.cta{display:none}.nav .brand{white-space:nowrap}}
""", encoding='utf-8')
(ROOT / 'CNAME').write_text('getbusted.online\n')
(ROOT / 'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: https://getbusted.online/sitemap.xml\n')
(ROOT / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n<url><loc>https://getbusted.online/</loc></url>\n<url><loc>https://getbusted.online/sv/</loc></url>\n</urlset>\n')
(ROOT / '404.html').write_text("<!doctype html><meta charset='utf-8'><title>Get Busted</title><meta http-equiv='refresh' content='0;url=/'><a href='/'>Get Busted</a>\n")
print('ok')
