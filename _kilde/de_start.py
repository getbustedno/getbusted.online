"""Tysk startside (getbusted.online/de/). Ikke lansert: noindex, ikke i sitemap, ikke i språkvelgeren.
Kortantall fra de-utvikling-grenen. Kjør: python3 _kilde/de_start.py"""
import pathlib, html
E_ = html.escape
ROOT = pathlib.Path(__file__).resolve().parent.parent
PACKS = [('original', 'cover_original.jpg', '#B7D147', 'Original', 'Der Klassiker für jeden Abend', 219),
         ('jul', 'cover_jul_en.jpg', '#E0473E', 'Weihnachten & Silvester', 'Weihnachtsfeier, Heiligabend und Mitternacht', 152),
         ('utdrikning', 'cover_utdrikning_en.jpg', '#E94B8A', 'JGA', 'Für die Person, die heiratet', 114)]
tiles = ''.join(f"<div class='pack' data-pack='{k}' style='--c:{c}'><picture><img src='/img/{img}' alt='' width='360' height='503' loading='lazy'></picture><b>{E_(n)}</b><span>{E_(s)}</span><small>{cnt} Karten</small><i class='soon'>In Arbeit</i></div>" for k, img, c, n, s, cnt in PACKS)
steps = [('Crew eintragen', '2 bis 30 Leute. Die Namen landen direkt auf den Karten, also kann sich niemand verstecken.'),
         ('Level wählen', 'Mild, Frech oder Get Fu**ed. Die Level bauen aufeinander auf.'),
         ('Laut vorlesen und spielen', 'Eine Person liest vor. Würfel, Twists und Rapid-Runden kommen von selbst.')]
st = ''.join(f"<div class='step'><div class='n'>{i}</div><h3>{E_(h)}</h3><p>{E_(p)}</p></div>" for i, (h, p) in enumerate(steps, 1))
page = f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Get Busted - das Partyspiel für jede Jahreszeit</title>
<meta name="robots" content="noindex">
<meta name="description" content="Get Busted ist das Partyspiel für das ganze Jahr. Bald auf Deutsch, mit Karten, die in Deutschland geschrieben wurden. Für Erwachsene ab 18.">
<meta name="theme-color" content="#191919">
<link rel="icon" href="/img/favicon.png">
<link rel="preload" href="/fonts/bsc-900Black_Italic.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/style.css">
<link rel="stylesheet" href="/online.css">
</head>
<body>
<main id="innhold">
<section class="hero">
  <div class="wrap">
    <div>
      <img class="logo" src="/img/logo.png" alt="Get Busted" width="150" height="150">
      <p class="kicker">Bald auf Deutsch</p>
      <h1>Das Partyspiel für <em>jede Jahreszeit</em></h1>
      <p class="lead">Eine Person hält das Handy und liest vor. Alle anderen schauen sich an, nicht auf einen Bildschirm. Ein Spiel für das ganze Jahr: von der Weihnachtsfeier bis zum JGA, mit Karten, die in Deutschland geschrieben werden, nicht übersetzt.</p>
      <div class="badges">
        <span class="badge"><span><small>Bald im</small><b>App Store</b></span></span>
        <span class="badge"><span><small>Bald bei</small><b>Google Play</b></span></span>
      </div>
      <p class="note">Für Erwachsene ab 18. Ohne Alkohol spielbar: Dann gibt es Punkte statt Schlucke.</p>
    </div>
    <div class="stage" aria-hidden="true">
      <img class="cover l" src="/img/cover_jul_en.jpg" alt="" style="--c:#E0473E" width="360" height="503">
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

<section id="packs" class="alt">
  <div class="wrap">
    <p class="kicker">Pakete</p>
    <h2>Eins für jeden Anlass, <em>das ganze Jahr</em></h2>
    <p class="lead">Die ersten deutschen Pakete sind in Arbeit. Danach kommen Pakete für jede Jahreszeit dazu.</p>
    <div class="group"><h3>In Arbeit</h3><div class="packs">
      {tiles}
    </div></div>
  </div>
</section>
</main>

<footer>
  <div class="wrap">
    <div class="footer-links"><a href="/privacy/">Datenschutz (EN)</a><a href="/terms/">Nutzungsbedingungen (EN)</a><a href="mailto:kontakt@getbusted.no">Kontakt</a></div>
    <div class="footer-firma">© 2026 Snikkerbua Holding AS · Org.-Nr. 927 118 300 · Voldgata 27, 2000 Lillestrøm, Norwegen · Ab 18</div>
  </div>
</footer>
</body>
</html>
"""
(ROOT / 'de' / 'index.html').write_text(page, encoding='utf-8')
print('ok')
