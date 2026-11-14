"""Tysk promoside (getbusted.online/de/): «kommt bald», søkbar og i sitemap (lagt inn i build.py), ikke i språkvelgeren før lansering.
Kortantall fra de-utvikling-grenen. Kjør: python3 _kilde/de_start.py
Pakkeinfo (trykk på pakke): pakkeinfo.json har en «de»-del laget fra de-utvikling (pakkeinfo.py ... de).
Kjøres pakkeinfo.py på nytt for sv da en, må de-delen legges inn igjen."""
import pathlib, html
E_ = html.escape
ROOT = pathlib.Path(__file__).resolve().parent.parent
PACKS = [('original', 'cover_original.jpg', '#B7D147', 'Original', 'Der Klassiker für jeden Abend', 219),
         ('jul', 'cover_jul_de.jpg', '#E0473E', 'Weihnachten & Silvester', 'Weihnachtsfeier, Heiligabend und Mitternacht', 152),
         ('utdrikning', 'cover_utdrikning_de.jpg', '#E94B8A', 'JGA', 'Für die Person, die heiratet', 114)]
tiles = ''.join(f"<div class='pack' data-pack='{k}' style='--c:{c}'><picture><source srcset='/img/{img[:-4]}.webp' type='image/webp'><img src='/img/{img}' alt='' width='360' height='503' loading='lazy'></picture><b>{E_(n)}</b><span>{E_(s)}</span><small>{cnt} Karten</small><i class='soon'>Kommt bald</i></div>" for k, img, c, n, s, cnt in PACKS)
steps = [('Crew eintragen', '2 bis 30 Leute. Die Namen landen direkt auf den Karten, also kann sich niemand verstecken.'),
         ('Level wählen', 'Mild, Frech oder Get Fu**ed. Die Level bauen aufeinander auf.'),
         ('Laut vorlesen und spielen', 'Eine Person liest vor. Würfel, Twists und Rapid-Runden kommen von selbst.')]
feats = [('Für jetzt geschrieben', 'Karten über Dating-Apps, Gruppenchats, Billigflieger und alles, worüber gerade geredet wird. Jeden Monat neue Karten, ohne Update.'),
         ('Twists', 'Manche Karten drehen sich um, nachdem sie vorgelesen wurden. Was sicher aussah, ist es nicht.'),
         ('Rapid', 'Fünf Finger hoch. Aussagen am laufenden Band. Wer zuerst raus ist, verliert.'),
         ('Geheime Missionen', 'Das Handy geht an eine Person, die eine Mission bekommt, von der nur sie weiß.'),
         ('Teamspiel', 'Feste Duos oder Rot gegen Blau. Die App zählt mit.'),
         ('Der Abend in Zahlen', 'Am Ende: wer am meisten busted wurde, wie viele Karten und Rapid-Runden. Zum Teilen.')]
ft = ''.join(f"<div class='feature'><h3>{E_(h)}</h3><p>{E_(p)}</p></div>" for h, p in feats)
faq = [('Wann kommt Get Busted nach Deutschland?', 'Die deutschen Karten werden gerade geschrieben und von Leuten aus Deutschland geprüft. Sobald die ersten Pakete fertig sind, kommt die App in den App Store und zu Google Play.'),
       ('Müssen wir trinken?', 'Nein. Im alkoholfreien Modus gibt es Punkte statt Schlucke, und jede Karte darf übersprungen werden.'),
       ('Wie viele können mitspielen?', '2 bis 30. Große Gruppen bekommen mehr Karten, die für alle gleichzeitig gelten.'),
       ('Gibt es ein Abo?', 'Nein. Alle Käufe sind Einmalkäufe. Jeden Abend gibt es 50 Karten kostenlos.')]
fq = ''.join(f'<details><summary>{E_(q)}</summary><p>{E_(a)}</p></details>' for q, a in faq)
st = ''.join(f"<div class='step'><div class='n'>{i}</div><h3>{E_(h)}</h3><p>{E_(p)}</p></div>" for i, (h, p) in enumerate(steps, 1))
page = f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Get Busted - das Partyspiel für jede Jahreszeit | Bald in Deutschland</title>
<link rel="canonical" href="https://getbusted.online/de/">
<meta property="og:title" content="Get Busted - das Partyspiel kommt bald nach Deutschland">
<meta property="og:description" content="Ein Handy, eine Person liest vor, alle spielen. Bald im App Store und bei Google Play. Ab 18.">
<meta property="og:image" content="https://getbusted.online/img/og_en.jpg">
<meta property="og:url" content="https://getbusted.online/de/">
<meta property="og:locale" content="de_DE">
<meta name="description" content="Get Busted, das Partyspiel für Spieleabend, Weihnachtsfeier und JGA, kommt bald nach Deutschland. Deutsche Karten, geschrieben in Deutschland. Bald im App Store und bei Google Play. Ab 18.">
<meta name="theme-color" content="#191919">
<link rel="icon" href="/img/favicon.png">
<link rel="preload" href="/fonts/bsc-900Black_Italic.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/style.css">
<link rel="stylesheet" href="/online.css">
<style>.flag-de{{display:inline-block;width:22px;height:13px;border-radius:3px;margin-right:9px;vertical-align:-1px;background:linear-gradient(#111 0 33.3%,#DD0000 33.3% 66.6%,#FFCE00 66.6%);box-shadow:0 0 0 1px rgba(255,255,255,.18),0 0 14px rgba(255,206,0,.35)}}</style>
</head>
<body>
<main id="innhold">
<section class="hero">
  <div class="wrap">
    <div>
      <img class="logo" src="/img/logo.png" alt="Get Busted" width="150" height="150">
      <p class="kicker"><span class="flag-de" aria-hidden="true"></span>Kommt bald nach Deutschland · Für Deutschland geschrieben</p>
      <h1>Das Partyspiel für <em>jede Jahreszeit</em></h1>
      <p class="lead">Eine Person hält das Handy und liest vor. Alle anderen schauen sich an, nicht auf einen Bildschirm. Ein Spiel für das ganze Jahr: von der Weihnachtsfeier bis zum JGA, mit Karten, die in Deutschland geschrieben werden, nicht übersetzt.</p>
      <div class="badges">
        <span class="badge"><span><small>Bald im</small><b>App Store</b></span></span>
        <span class="badge"><span><small>Bald bei</small><b>Google Play</b></span></span>
      </div>
      <p class="note">Für Erwachsene ab 18. Ohne Alkohol spielbar: Dann gibt es Punkte statt Schlucke.</p>
    </div>
    <div class="stage" aria-hidden="true">
      <img class="cover l" src="/img/cover_jul_de.jpg" alt="" style="--c:#E0473E" width="360" height="503">
      <img class="cover r" src="/img/cover_original.jpg" alt="" style="--c:#B7D147" width="360" height="503">
    </div>
  </div>
</section>

<section id="how">
  <div class="wrap">
    <p class="kicker">So geht's</p>
    <h2>Startklar in 20 Sekunden</h2>
    <div class="steps">{st}</div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <p class="kicker">Mehr als nur Karten</p>
    <h2>Was nur eine App kann</h2>
    <div class="features">{ft}</div>
  </div>
</section>

<section id="packs">
  <div class="wrap">
    <p class="kicker">Pakete</p>
    <h2>Eins für jeden Anlass, <em>das ganze Jahr</em></h2>
    <p class="lead">Die ersten deutschen Pakete kommen bald. Danach folgen Pakete für jede Jahreszeit.</p>
    <div class="group"><h3>Kommt bald</h3><div class="packs">
      {tiles}
    </div></div>
  </div>
</section>

<section id="faq" class="alt">
  <div class="wrap" style="max-width:820px">
    <p class="kicker">Fragen</p>
    <h2>Häufige Fragen</h2>
    {fq}
  </div>
</section>
</main>

<footer>
  <div class="wrap">
    <div class="footer-links"><a href="/privacy/">Datenschutz (EN)</a><a href="/terms/">Nutzungsbedingungen (EN)</a><a href="mailto:kontakt@getbusted.no">Kontakt</a></div>
    <div class="footer-firma">© 2026 Snikkerbua Holding AS · Org.-Nr. 927 118 300 · Voldgata 27, 2000 Lillestrøm, Norwegen · Ab 18</div>
  </div>
</footer>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"MobileApplication","name":"Get Busted","url":"https://getbusted.online/de/","inLanguage":"de","description":"Das Partyspiel für jede Jahreszeit. Kommt bald nach Deutschland.","applicationCategory":"GameApplication","operatingSystem":"iOS, Android","contentRating":"18+"}}</script>
<script src="/pakkeinfo.js" defer></script>
</body>
</html>
"""
(ROOT / 'de' / 'index.html').write_text(page, encoding='utf-8')
print('ok')
