/*
 * Sesongtema for getbusted.no. Samme regler som i appen (src/ui/season.ts):
 * høst, halloween, julebord, jul, nyttår, vinter, påske, vår, 17. mai og sommer.
 * Alt regnes ut i nettleseren ut fra dagens dato, så siden bytter tema av seg selv.
 *
 * - Logoen får hatt (heksehatt / nisselue), og toppen får glød og pynt i sesongfargen.
 * - Pakken som passer sesongen (eller en helt ny pakke) flyttes fram og får merket «Aktuell nå» / «Ny».
 * - «Kommer snart»-merkene står til pakken fjernes fra build.py (ingen datoer på de utenlandske sidene).
 * - Linjen over overskriften sier «... er med fra start» før LAUNCH og «... er ute» etterpå.
 * - Fra LAUNCH blir butikkmerkene (data-store) lenker til STORE, og data-launch-feltene får lanseringstekst.
 *   Mangler App Store-lenken, står det «Snart på App Store». Test: ?launch=1 i adressen.
 * Test et tema: legg ?season=julebord (eller halloween, vinter ...) til i adressen.
 * Samme fil brukes på getbusted.online: språket leses fra <html lang> (no, en, sv, da).
 */
(function () {
  var LAUNCH = null; // Ingen lanseringsdato er vedtatt for en/sv/da. Sett en dato (ÅÅÅÅ-MM-DD) først når den er bestemt. Norge lanseres på getbusted.no.
  // iPhone klar til LAUNCH? false = App Store-merket sier «Snart på» før lansering, og FAQ sier Android først.
  // Etter lansering styres App Store-merket av STORE.ios (tom = «Snart på»).
  var IOS_READY = true && !/[?&]ios=0/.test(location.search); // test: ?ios=0
  var STORE = {
    play: 'https://play.google.com/store/apps/details?id=no.getbusted.app',
    ios: '' // Lim inn App Store-lenken (https://apps.apple.com/...) når Apple har godkjent appen.
  };
  var NEW_DAYS = 10;
  var S = {
    host:      { c: '#E08A3C', p: 'leaves',   col: ['#E08A3C', '#C8612E', '#D9A441', '#9C4A2A'], packs: ['hytta', 'nach'], k: 'Høstkvelder' },
    halloween: { c: '#FF8A1F', p: 'bats',     col: ['#7A4FB5'], hat: 'halloween', packs: ['halloween'], k: 'Klar til halloween' },
    julebord:  { c: '#E0473E', p: 'snow',     col: ['#FFFFFF'], hat: 'jul', packs: ['jul'], k: 'Skal dere på julebord?' },
    jul:       { c: '#E0473E', p: 'snow',     col: ['#FFFFFF'], hat: 'jul', packs: ['jul'], k: 'God jul' },
    nyttar:    { c: '#FFD23F', p: 'confetti', col: ['#FFD23F', '#B7D147', '#FFFFFF', '#E94B8A'], packs: ['jul', 'nach'], k: 'Nyttår' },
    vinter:    { c: '#9FD3F0', p: 'snow',     col: ['#DDEFFA'], packs: ['afterski', 'hytta'], k: 'Vinter' },
    paske:     { c: '#FFD23F', p: 'sun',      col: ['#FFD23F', '#FFF2A8'], packs: ['paske', 'hytta'], k: 'Påske' },
    vaar:      { c: '#B7D147', p: 'sun',      col: ['#B7D147', '#FFF2A8'], packs: ['sommer', 'utdrikning'], k: 'Vår' },
    mai17:     { c: '#E0473E', p: 'confetti', col: ['#E0473E', '#FFFFFF', '#3B5BDB'], packs: ['sommer', 'original'], k: '17. mai' },
    sommer:    { c: '#F2A93B', p: 'sun',      col: ['#F2A93B', '#FFE08A'], packs: ['sommer', 'reise'], k: 'Sommer' }
  };
  var STRONG = ['halloween', 'julebord', 'jul', 'paske'];
  var LANG = (document.documentElement.lang || 'no').slice(0, 2);
  var TX = {
    no: { k: {}, isNew: 'Ny', hot: 'Aktuell nå', newPack: 'Ny pakke', out: ' er ute', ready: '-pakken er klar', start: '-pakken er med fra start',
          L: { dl: 'Last ned fra', soon: 'Snart på', cta: 'Last ned', group: 'Ute nå', q: 'Hvor laster jeg ned appen?', a: 'Søk etter «Get Busted» i App Store eller Google Play, eller trykk på knappene øverst på siden.', pre: 'Kommer snart.', a1: 'Get Busted er ute på Google Play. iPhone-versjonen kommer veldig snart. Trykk på knappen øverst på siden.' } },
    en: { k: { host: 'Autumn nights', halloween: 'Ready for Halloween', julebord: 'Office party season?', jul: 'Merry Christmas', nyttar: 'New Year', vinter: 'Winter', paske: 'Happy Easter', vaar: 'Spring', mai17: 'Spring', sommer: 'Summer' },
          isNew: 'New', hot: 'In season', newPack: 'New pack', out: ' is out', ready: ' pack is ready', start: ' pack is in from day one',
          L: { dl: 'Download on', soon: 'Coming soon to', cta: 'Download', group: 'Out now', q: 'Where do I get it?', a: 'Search for “Get Busted” in the App Store or on Google Play, or tap the buttons at the top of the page.', pre: 'Coming soon.', a1: 'Get Busted is out on Google Play. The iPhone version is coming very soon. Tap the button at the top of the page.' } },
    sv: { k: { host: 'Höstkvällar', halloween: 'Redo för halloween', julebord: 'Dags för julbord?', jul: 'God jul', nyttar: 'Gott nytt år', vinter: 'Vinter', paske: 'Glad påsk', vaar: 'Vår', mai17: 'Vår', sommer: 'Sommar' },
          isNew: 'Ny', hot: 'Aktuell nu', newPack: 'Nytt paket', out: ' är ute', ready: '-paketet är klart', start: '-paketet är med från start',
          L: { dl: 'Hämta i', soon: 'Snart i', cta: 'Ladda ner', group: 'Ute nu', q: 'Var laddar jag ner den?', a: 'Sök på «Get Busted» i App Store eller Google Play, eller tryck på knapparna högst upp på sidan.', pre: 'Kommer snart.', a1: 'Get Busted finns på Google Play. iPhone-versionen kommer väldigt snart. Tryck på knappen högst upp på sidan.' } },
    da: { k: { host: 'Efterårsaftener', halloween: 'Klar til halloween', julebord: 'Skal I til julefrokost?', jul: 'Glædelig jul', nyttar: 'Godt nytår', vinter: 'Vinter', paske: 'God påske', vaar: 'Forår', mai17: 'Forår', sommer: 'Sommer' },
          isNew: 'Ny', hot: 'Aktuel nu', newPack: 'Ny pakke', out: ' er ude', ready: '-pakken er klar', start: '-pakken er med fra start',
          L: { dl: 'Hent i', soon: 'Snart i', cta: 'Hent appen', group: 'Ude nu', q: 'Hvor henter jeg appen?', a: 'Søg efter «Get Busted» i App Store eller Google Play, eller tryk på knapperne øverst på siden.', pre: 'Kommer snart.', a1: 'Get Busted er ude på Google Play. iPhone-versionen kommer meget snart. Tryk på knappen øverst på siden.' } }
  }[LANG] || null;
  if (!TX) return;

  function easter(y) {
    var a = y % 19, b = Math.floor(y / 100), c = y % 100, d = Math.floor(b / 4), e = b % 4,
      f = Math.floor((b + 8) / 25), g = Math.floor((b - f + 1) / 3), h = (19 * a + b - d - g + 15) % 30,
      i = Math.floor(c / 4), k = c % 4, l = (32 + 2 * e + 2 * i - h - k) % 7, m = Math.floor((a + 11 * h + 22 * l) / 451),
      mo = Math.floor((h + l - 7 * m + 114) / 31), da = ((h + l - 7 * m + 114) % 31) + 1;
    return Date.UTC(y, mo - 1, da);
  }
  function seasonFor(now) {
    var t = new Date(now.getTime() + 3600e3), y = t.getUTCFullYear();
    var md = (t.getUTCMonth() + 1) * 100 + t.getUTCDate(), day = Date.UTC(y, t.getUTCMonth(), t.getUTCDate()), e = easter(y);
    if (day >= e - 7 * 864e5 && day <= e + 864e5) return 'paske';
    if (md >= 1010 && md <= 1101) return 'halloween';
    if (md >= 1113 && md <= 1220) return 'julebord';
    if (md >= 1221 && md <= 1226) return 'jul';
    if (md >= 1227 || md <= 101) return 'nyttar';
    if (md <= 331) return 'vinter';
    if (md >= 510 && md <= 517) return 'mai17';
    if (md >= 518 && md <= 820) return 'sommer';
    if (md < 510) return 'vaar';
    return 'host';
  }
  var at = function (d) { return new Date(d + 'T00:00:00+01:00').getTime(); };

  var now = new Date();
  var q = (location.search.match(/[?&]season=([a-z0-9]+)/) || [])[1];
  var season = S[q] ? q : seasonFor(now);
  var T = S[season];
  if (LANG !== 'no' && season === 'mai17') T = S.vaar; // 17. mai bare på norsk
  var kicker = TX.k[season] || T.k;
  var launched = (!!LAUNCH && now.getTime() >= at(LAUNCH)) || /[?&]launch=1/.test(location.search);
  var root = document.documentElement;
  root.setAttribute('data-season', season);
  root.style.setProperty('--season', T.c);

  // Overskriften følger sesongen: siste ord («kvelden») byttes. Google ser fortsatt originalen i HTML.
  var ORD = {
    no: { re: /kvelden\s*$/i, halloween: 'halloweenfesten', julebord: 'julebordet', jul: 'juleselskapet', nyttar: 'nyttårsaften', vinter: 'hytteturen', paske: 'påskefjellet', mai17: '17. mai', sommer: 'sommerfesten' },
    sv: { re: /kvällen\s*$/i, halloween: 'halloweenfesten', julebord: 'julbordet', jul: 'julfesten', nyttar: 'nyårsafton', vinter: 'stugresan', paske: 'påskhelgen', sommer: 'sommarfesten' },
    da: { re: /aftenen\s*$/i, halloween: 'halloweenfesten', julebord: 'julefrokosten', jul: 'julefesten', nyttar: 'nytårsaften', vinter: 'skiferien', paske: 'påskefrokosten', sommer: 'sommerfesten' },
    en: { re: /the night\s*$/i, halloween: 'the Halloween party', julebord: 'the Christmas party', jul: 'the holidays', nyttar: "New Year's Eve", vinter: 'the ski trip', paske: 'Easter weekend', sommer: 'the summer party' }
  }[LANG];
  var h1 = document.querySelector('.hero h1');
  if (ORD && ORD[season] && h1) {
    var tw = document.createTreeWalker(h1, NodeFilter.SHOW_TEXT), tn, sist = null;
    while ((tn = tw.nextNode())) if (tn.nodeValue.trim()) sist = tn;
    if (sist && ORD.re.test(sist.nodeValue)) {
      sist.nodeValue = sist.nodeValue.replace(ORD.re, ORD[season]);
      h1.style.overflowWrap = 'normal';
      // Lange ord: krymp skriften litt til linja får plass
      var fit = function () {
        h1.style.fontSize = '';
        var fs = parseFloat(getComputedStyle(h1).fontSize), n = 0, rg = document.createRange();
        rg.selectNodeContents(h1);
        var plass = function () {
          var l = h1.getBoundingClientRect().left, lim = document.documentElement.clientWidth - l - 16;
          var st = document.querySelector('.hero .stage');
          if (st) { var sr = st.getBoundingClientRect(); if (sr.left > l + 50 && sr.top < h1.getBoundingClientRect().bottom) lim = Math.min(lim, sr.left - l - 24); }
          return lim;
        };
        while (rg.getBoundingClientRect().width > plass() && n++ < 40) { fs *= 0.96; h1.style.fontSize = fs + 'px'; }
      };
      fit(); window.addEventListener('resize', fit);
      if (document.fonts && document.fonts.ready) document.fonts.ready.then(fit);
    }
  }

  // Seksjoner med sluttdato (data-until): fjernes etter datoen
  document.querySelectorAll('[data-until]').forEach(function (el) {
    if (now.getTime() >= at(el.getAttribute('data-until')) + 864e5) el.remove();
  });

  // iPhone ikke klar før lansering: App Store-merket og FAQ sier Android først
  if (!launched && !IOS_READY) {
    document.querySelectorAll('.badge[data-store="ios"] small').forEach(function (el) { el.textContent = TX.L.soon; });
    document.querySelectorAll('[data-launch="faq"] p').forEach(function (el) { el.textContent = TX.L.pre; });
  }

  // Lansering: butikkmerkene blir lenker, og data-launch-feltene får ny tekst
  if (launched) {
    document.querySelectorAll('.badge[data-store]').forEach(function (el) {
      var url = STORE[el.getAttribute('data-store')], small = el.querySelector('small');
      if (!url) { if (small) small.textContent = TX.L.soon; return; }
      if (small) small.textContent = TX.L.dl;
      var a = document.createElement('a');
      a.className = el.className + ' live'; a.href = url; a.rel = 'noopener'; a.innerHTML = el.innerHTML;
      el.parentNode.replaceChild(a, el);
    });
    document.querySelectorAll('[data-launch]').forEach(function (el) {
      var k = el.getAttribute('data-launch');
      if (k === 'faq') {
        var sm = el.querySelector('summary'), p = el.querySelector('p');
        if (sm) sm.textContent = TX.L.q;
        if (p) p.textContent = STORE.ios ? TX.L.a : TX.L.a1;
      } else if (k === 'cta') {
        el.textContent = TX.L.cta;
        var ua = navigator.userAgent; // rett til butikken på mobil, ellers til merkene på siden
        if (STORE.ios && /iPhone|iPad/i.test(ua)) el.href = STORE.ios;
        else if (/Android/i.test(ua)) el.href = STORE.play;
      } else if (TX.L[k]) el.textContent = TX.L[k];
    });
  }

  // Logo med hatt
  if (T.hat) document.querySelectorAll('img.logo, .brand img').forEach(function (img) {
    img.src = '/img/logo_' + T.hat + '.png';
  });

  // Pakkeflisene: slipp «Kommer»-merket når datoen er passert, og løft fram sesongens pakke
  var tiles = {};
  document.querySelectorAll('.pack[data-pack]').forEach(function (el) {
    tiles[el.getAttribute('data-pack')] = el;
  });
  // Utenlandske sider har ingen slippdatoer: en flis med «Kommer snart»-merke regnes som ikke sluppet.
  var released = function (el) { return !el.querySelector('.soon'); };
  var ready = function (slug) { return !!tiles[slug] && slug !== 'original' && released(tiles[slug]); };
  var feat = null, own = T.packs.filter(ready)[0];
  if (own && STRONG.indexOf(season) >= 0) feat = { slug: own, why: 'sesong' };
  if (!feat && launched) {
    var fresh = Object.keys(tiles).map(function (s) { return { s: s, r: tiles[s].getAttribute('data-release') }; })
      .filter(function (x) { return x.r && now.getTime() >= at(x.r) && now.getTime() - at(x.r) < NEW_DAYS * 864e5; })
      .sort(function (a, b) { return at(b.r) - at(a.r); })[0];
    if (fresh) feat = { slug: fresh.s, why: 'ny' };
  }
  if (!feat && own) feat = { slug: own, why: 'sesong' };
  if (feat) {
    var el = tiles[feat.slug], first = tiles.original;
    if (first && first.nextElementSibling !== el) first.parentNode.insertBefore(el, first.nextSibling);
    var b = document.createElement('i'); b.className = 'soon hot'; b.textContent = feat.why === 'ny' ? TX.isNew : TX.hot;
    el.appendChild(b); el.classList.add('featured');
    var pill = document.querySelector('.season-pill');
    if (pill) {
      var name = el.querySelector('b').textContent;
      var kick = feat.why === 'ny' ? TX.newPack : kicker;
      pill.textContent = kick + (/[?!]$/.test(kick) ? ' ' : ' · ') + name + (launched ? (feat.why === 'ny' ? TX.out : TX.ready) : TX.start) + ' ›';
      pill.hidden = false;
    }
  }

  // Pynt i toppen: fallende løv/snø/konfetti, stigende lys eller flaggermus
  var hero = document.querySelector('.hero');
  if (!hero || !window.HTMLCanvasElement) return;
  var cv = document.createElement('canvas'); cv.className = 'season-fx'; cv.setAttribute('aria-hidden', 'true');
  hero.insertBefore(cv, hero.firstChild);
  var ctx = cv.getContext('2d'), W = 0, H = 0, dpr = Math.min(window.devicePixelRatio || 1, 2);
  function size() { W = hero.clientWidth; H = hero.clientHeight; cv.width = W * dpr; cv.height = H * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0); }
  size(); window.addEventListener('resize', size);
  var BAT = new Path2D('M32 9c2-4 4-5 4-5l1 4c3 0 5 2 5 5 5-6 13-9 22-8-4 3-5 7-4 11-4-2-8-2-11 1-2-3-6-3-8 0-2-1-4-1-6 1h-6c-2-2-4-2-6-1-2-3-6-3-8 0-3-3-7-3-11-1 1-4 0-8-4-11 9-1 17 2 22 8 0-3 2-5 5-5l1-4s2 1 4 5z');
  var n = { leaves: 22, snow: 60, confetti: 50, sun: 26, bats: 6 }[T.p] || 0;
  var R = function (a, b) { return a + Math.random() * (b - a); };
  var parts = [];
  for (var i = 0; i < n; i++) parts.push({
    x: R(0, 1), y: R(0, 1), s: T.p === 'snow' ? R(1.5, 4) : T.p === 'bats' ? R(44, 72) : R(5, 11),
    v: T.p === 'bats' ? R(0.0006, 0.0012) : R(0.0004, 0.0011), dir: Math.random() < 0.5 ? 1 : -1,
    rot: R(0, 6.28), vr: R(-0.03, 0.03), sw: R(0, 6.28), c: T.col[i % T.col.length]
  });
  var still = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function draw(t) {
    ctx.clearRect(0, 0, W, H);
    parts.forEach(function (p) {
      if (!still) {
        if (T.p === 'bats') { p.x += p.v * p.dir * 1.6; if (p.x > 1.15) p.x = -0.15; if (p.x < -0.15) p.x = 1.15; }
        else if (T.p === 'sun') { p.y -= p.v * 0.6; if (p.y < -0.05) { p.y = 1.05; p.x = Math.random(); } }
        else { p.y += p.v; if (p.y > 1.05) { p.y = -0.05; p.x = Math.random(); } }
        p.rot += p.vr; p.sw += 0.02;
      }
      var x = p.x * W + Math.sin(p.sw) * (T.p === 'snow' ? 8 : 22), y = T.p === 'bats' ? 20 + p.y * 24 : p.y * H; // flaggermus flyr i stripa øverst i hero, aldri over tekst, knapper eller kort
      ctx.save(); ctx.translate(x, y); ctx.fillStyle = p.c;
      if (T.p === 'snow' || T.p === 'sun') {
        ctx.globalAlpha = T.p === 'sun' ? 0.35 : 0.55; ctx.beginPath(); ctx.arc(0, 0, p.s, 0, 6.28); ctx.fill();
      } else if (T.p === 'leaves') {
        ctx.globalAlpha = 0.6; ctx.rotate(p.rot); ctx.beginPath(); ctx.ellipse(0, 0, p.s, p.s * 0.5, 0, 0, 6.28); ctx.fill();
      } else if (T.p === 'confetti') {
        ctx.globalAlpha = 0.8; ctx.rotate(p.rot); ctx.fillRect(-p.s / 2, -p.s / 4, p.s, p.s / 2);
      } else if (T.p === 'bats') {
        var k = p.s / 64, flap = 0.55 + 0.45 * Math.abs(Math.sin(t / 110 + p.sw * 10));
        ctx.globalAlpha = 0.85; ctx.scale(k * p.dir, k * flap); ctx.translate(-32, -14 + Math.sin(p.sw) * 6); ctx.fill(BAT);
      }
      ctx.restore();
    });
    if (!still) requestAnimationFrame(draw);
  }
  requestAnimationFrame(draw);
})();
