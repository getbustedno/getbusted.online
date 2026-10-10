/*
 * Været i hero på getbusted.no og getbusted.online.
 * Leser /vaer.json (skrevet hver time av GitHub Actions, se _kilde/vaer.py) og legger
 * regn, snø eller sol i bakgrunnen, og rim på heltekortet og overskriften ved minusgrader.
 * Ingen tredjepart: nettleseren henter bare filen fra vår egen side.
 * Land: no (norsk og engelsk side), se (svensk), dk (dansk).
 * Test: ?vaer=regn, ?vaer=sno, ?vaer=sol, ?vaer=frost, ?vaer=sno+frost, ?vaer=regn3 (styrke 1-3), ?vaer=ingen
 */
(function () {
  var hero = document.querySelector('.hero');
  if (!hero || !window.fetch) return;
  var LANG = (document.documentElement.lang || 'no').slice(0, 2);
  var LAND = { sv: 'se', da: 'dk' }[LANG] || 'no';
  var root = document.documentElement;

  var CSS =
    '.vaer-fx{position:absolute;inset:0;width:100%;height:100%;pointer-events:none;z-index:0}.hero>.wrap{position:relative;z-index:1}' +
    ':root[data-vaer-frost] .stage .card::after{content:"";position:absolute;inset:0;border-radius:22px;pointer-events:none;z-index:3;' +
      'box-shadow:0 0 0 2px rgba(214,236,255,.85),inset 0 0 22px rgba(214,236,255,.55),0 0 40px -6px rgba(170,215,255,.6);' +
      'background:url("data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 width=%27220%27 height=%27220%27%3E%3Cfilter id=%27f%27%3E%3CfeTurbulence type=%27fractalNoise%27 baseFrequency=%27.85%27 numOctaves=%273%27 seed=%277%27/%3E%3CfeColorMatrix values=%270 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 1.6 -.75%27/%3E%3C/filter%3E%3Crect width=%27100%25%27 height=%27100%25%27 filter=%27url(%23f)%27/%3E%3C/svg%3E");' +
      '-webkit-mask:radial-gradient(120% 70% at 0 0,#000 0,transparent 42%),radial-gradient(120% 70% at 100% 100%,#000 0,transparent 40%),radial-gradient(90% 50% at 100% 0,#000 0,transparent 34%),radial-gradient(90% 50% at 0 100%,#000 0,transparent 32%),linear-gradient(rgba(0,0,0,.1),rgba(0,0,0,.1));' +
      'mask:radial-gradient(120% 70% at 0 0,#000 0,transparent 42%),radial-gradient(120% 70% at 100% 100%,#000 0,transparent 40%),radial-gradient(90% 50% at 100% 0,#000 0,transparent 34%),radial-gradient(90% 50% at 0 100%,#000 0,transparent 32%),linear-gradient(rgba(0,0,0,.1),rgba(0,0,0,.1))}' +
    // Rimete bokstaver: hvit iskappe på toppen av hver linje, rimkorn over hele, glatt farge under
    ':root[data-vaer-frost] .hero h1,:root[data-vaer-frost] .hero h1 em,:root[data-vaer-frost] .stage .card .hk-b,:root[data-vaer-frost] .stage .card .hk-h{' +
      'background-image:linear-gradient(180deg,rgba(246,252,255,.98) 0,rgba(236,248,255,.92) calc(var(--lh,1em)*.2),rgba(225,243,255,0) calc(var(--lh,1em)*.42)),url("data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 width=%27160%27 height=%27160%27%3E%3Cfilter id=%27f%27%3E%3CfeTurbulence type=%27fractalNoise%27 baseFrequency=%271.1%27 numOctaves=%272%27 seed=%273%27/%3E%3CfeColorMatrix values=%270 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 2.2 -1%27/%3E%3C/filter%3E%3Crect width=%27100%25%27 height=%27100%25%27 filter=%27url(%23f)%27/%3E%3C/svg%3E"),linear-gradient(var(--is-farge),var(--is-farge));' +
      'background-size:100% var(--lh,1em),160px 160px,100% 100%;background-repeat:repeat-y,repeat,no-repeat;' +
      '-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent}' +
    ':root[data-vaer-frost] .hero h1{--is-farge:#F4F1EA;text-shadow:0 0 .2em rgba(190,228,255,.35)}' +
    ':root[data-vaer-frost] .hero h1 em{--is-farge:var(--lime,#B7D147);text-shadow:0 0 .3em rgba(183,209,71,.35),0 0 .15em rgba(200,235,255,.4)}' +
    ':root[data-vaer-frost] .stage .card .hk-b,:root[data-vaer-frost] .stage .card .hk-h{--is-farge:var(--lime,#B7D147);text-shadow:0 0 .12em rgba(220,240,255,.45)}' +
    // Iskappe og istapper på knapper, menylinja og heltekortet
    '.is-kappe{position:absolute;left:4px;right:4px;top:-4px;height:9px;border-radius:9px 9px 5px 5px;pointer-events:none;z-index:4;' +
      'background:linear-gradient(180deg,#FFFFFF,#E3F3FF 55%,rgba(200,232,255,.6)),url("data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 width=%27160%27 height=%27160%27%3E%3Cfilter id=%27f%27%3E%3CfeTurbulence type=%27fractalNoise%27 baseFrequency=%271.1%27 numOctaves=%272%27 seed=%273%27/%3E%3CfeColorMatrix values=%270 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 2.2 -1%27/%3E%3C/filter%3E%3Crect width=%27100%25%27 height=%27100%25%27 filter=%27url(%23f)%27/%3E%3C/svg%3E");background-blend-mode:multiply;' +
      'box-shadow:0 1px 3px rgba(150,200,240,.45),0 0 10px rgba(200,235,255,.35)}' +
    '.is-tapper{position:absolute;left:0;top:100%;width:100%;pointer-events:none;z-index:4;overflow:visible;filter:drop-shadow(0 2px 3px rgba(150,205,245,.35))}' +
    ':root[data-vaer-frost] .badge,:root[data-vaer-frost] .nav a.cta{position:relative;border-color:rgba(214,236,255,.55);box-shadow:inset 0 0 14px rgba(200,232,255,.22)}' +
    ':root[data-vaer-frost] .nav{border-bottom-color:rgba(214,236,255,.5)}' +
    ':root[data-vaer-frost] .stage .card.hk{overflow:visible}' +
    '.vaer-is{position:absolute;inset:0;width:100%;height:100%;pointer-events:none;z-index:0}';


  // ---------- Frost ----------
  var R0 = function (a, b) { return a + Math.random() * (b - a); };
  function istapper(el, tett, maks) {
    var w = el.getBoundingClientRect().width; if (!w) return;
    var ns = 'http://www.w3.org/2000/svg', svg = document.createElementNS(ns, 'svg');
    svg.setAttribute('class', 'is-tapper'); svg.setAttribute('aria-hidden', 'true');
    svg.style.width = w + 'px'; svg.style.height = (maks + 2) + 'px'; svg.style.fill = 'none';
    svg.setAttribute('viewBox', '0 0 ' + w + ' ' + (maks + 2));
    var id = 'isg' + Math.random().toString(36).slice(2, 7), d = '';
    var defs = '<defs><linearGradient id="' + id + '" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".95"/><stop offset=".55" stop-color="#DDF0FF" stop-opacity=".8"/><stop offset="1" stop-color="#BFE2FF" stop-opacity=".35"/></linearGradient></defs>';
    var x = R0(2, tett);
    while (x < w - 4) {
      var b = R0(2.5, 6), l = Math.random() < 0.25 ? R0(maks * 0.55, maks) : R0(3, maks * 0.45);
      d += 'M' + (x - b) + ' -1 Q' + (x - b * 0.35) + ' ' + (l * 0.6) + ' ' + x + ' ' + l + ' Q' + (x + b * 0.35) + ' ' + (l * 0.6) + ' ' + (x + b) + ' -1Z';
      x += R0(tett * 0.6, tett * 1.5);
    }
    svg.innerHTML = defs + '<path d="' + d + '" fill="url(#' + id + ')"/><path d="M0 0H' + w + '" stroke="#F4FBFF" stroke-opacity=".9" stroke-width="2.5"/>';
    if (getComputedStyle(el).position === 'static') el.style.position = 'relative';
    el.appendChild(svg);
  }
  function kappe(el) {
    var k = document.createElement('i'); k.className = 'is-kappe'; k.setAttribute('aria-hidden', 'true');
    if (getComputedStyle(el).position === 'static') el.style.position = 'relative';
    el.appendChild(k);
  }
  // Iskrystaller som kryper inn fra hjørnene, som rim på et vindu
  function rimVindu() {
    var cv = document.createElement('canvas'); cv.className = 'vaer-is'; cv.setAttribute('aria-hidden', 'true');
    hero.insertBefore(cv, hero.firstChild);
    var W = hero.clientWidth, H = hero.clientHeight, dpr = Math.min(window.devicePixelRatio || 1, 2);
    cv.width = W * dpr; cv.height = H * dpr; var c = cv.getContext('2d'); c.setTransform(dpr, 0, 0, dpr, 0, 0);
    c.lineCap = 'round';
    // Isbregner: korte, tette greiner med spisse vinkler, slik rim vokser fra kanten av en rute
    function gren(x, y, ang, len, w, dyb) {
      if (dyb > 6 || len < 3) return;
      var x2 = x + Math.cos(ang) * len, y2 = y + Math.sin(ang) * len;
      c.strokeStyle = 'rgba(226,243,255,' + Math.max(0.08, 0.3 - dyb * 0.035) + ')'; c.lineWidth = w;
      c.beginPath(); c.moveTo(x, y); c.lineTo(x2, y2); c.stroke();
      var n = 3 + Math.floor(Math.random() * 3);
      for (var i = 1; i <= n; i++) {
        var t = i / (n + 1), bx = x + (x2 - x) * t, by = y + (y2 - y) * t, bl = len * R0(0.22, 0.4) * (1 - t * 0.5);
        if (Math.random() < 0.85) gren(bx, by, ang + R0(0.5, 0.7), bl, w * 0.55, dyb + 2);
        if (Math.random() < 0.85) gren(bx, by, ang - R0(0.5, 0.7), bl, w * 0.55, dyb + 2);
      }
      gren(x2, y2, ang + R0(-0.25, 0.25), len * 0.7, w * 0.85, dyb + 1);
    }
    var s = Math.max(0.55, Math.min(W, 1100) / 1100);
    // røtter langs kantene, tettest i hjørnene
    function rot(x, y, ang) { gren(x, y, ang + R0(-0.35, 0.35), R0(28, 60) * s, R0(0.9, 1.5), 0); }
    for (var i = 0; i < 9; i++) { rot(R0(0, 260) * s * (i % 3 ? 1 : 0.3), 0, Math.PI / 2 - 0.25); rot(0, R0(0, 240) * s * (i % 3 ? 1 : 0.3), 0.25); }
    for (i = 0; i < 9; i++) { rot(W - R0(0, 260) * s * (i % 3 ? 1 : 0.3), H, -Math.PI / 2 - 0.25); rot(W, H - R0(0, 240) * s * (i % 3 ? 1 : 0.3), Math.PI + 0.25); }
    for (i = 0; i < 5; i++) { rot(W - R0(0, 160) * s, 0, Math.PI / 2 + 0.2); rot(W, R0(0, 130) * s, Math.PI - 0.2); }
    // rimslør i hjørnene
    [[0, 0], [W, H], [W, 0]].forEach(function (p, k) {
      var g = c.createRadialGradient(p[0], p[1], 0, p[0], p[1], (k === 2 ? 180 : 280) * s + 60);
      g.addColorStop(0, 'rgba(215,238,255,.22)'); g.addColorStop(1, 'rgba(215,238,255,0)');
      c.fillStyle = g; c.fillRect(0, 0, W, H);
    });
  }
  function frost() {
    try {
      rimVindu();
      var h1 = hero.querySelector('h1');
      if (h1) h1.style.setProperty('--lh', getComputedStyle(h1).lineHeight);
      var hb = document.querySelector('.stage .card .hk-b');
      if (hb) setTimeout(function () { hb.style.setProperty('--lh', getComputedStyle(hb).lineHeight); }, 300);
      var nav = document.querySelector('.nav, header');
      if (nav) istapper(nav, 22, 16);
      document.querySelectorAll('.hero .badge, .nav a.cta').forEach(function (b) { kappe(b); istapper(b, 13, 11); });
      var kort = document.querySelector('.stage .card');
      if (kort) { kappe(kort); istapper(kort, 16, 18); }
    } catch (e) {}
  }

  function start(v) {
    if (!v || !v.t) return;
    var t = v.t, styrke = Math.max(1, Math.min(3, v.styrke || 1));
    var st = document.createElement('style'); st.textContent = CSS; document.head.appendChild(st);
    if (v.frost) { root.setAttribute('data-vaer-frost', ''); (document.fonts && document.fonts.ready ? document.fonts.ready : Promise.resolve()).then(frost); }
    if (t !== 'ingen') root.setAttribute('data-vaer', t);
    if (t === 'ingen') return;

    // Været tar over for sesongpynten som ligner (løv, snø, lys). Flaggermus og konfetti får fly videre.
    var sfx = hero.querySelector('.season-fx');
    if (sfx && ['halloween', 'nyttar', 'mai17'].indexOf(root.getAttribute('data-season')) < 0) sfx.style.display = 'none';

    var cv = document.createElement('canvas'); cv.className = 'vaer-fx'; cv.setAttribute('aria-hidden', 'true');
    hero.insertBefore(cv, hero.firstChild);
    var ctx = cv.getContext('2d'), W = 0, H = 0, dpr = Math.min(window.devicePixelRatio || 1, 2);
    function size() { W = hero.clientWidth; H = hero.clientHeight; cv.width = W * dpr; cv.height = H * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0); }
    size(); window.addEventListener('resize', size);
    var R = function (a, b) { return a + Math.random() * (b - a); };
    var smal = W < 700 ? 0.55 : 1;
    var still = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var parts = [], i;

    if (t === 'regn') {
      for (i = 0; i < Math.round([0, 70, 130, 210][styrke] * smal); i++)
        parts.push({ x: R(-0.1, 1.1), y: R(0, 1), l: R(12, 26), v: R(0.012, 0.02), a: R(0.22, 0.45) });
    } else if (t === 'sno') {
      for (i = 0; i < Math.round([0, 60, 110, 170][styrke] * smal); i++)
        parts.push({ x: R(0, 1), y: R(0, 1), s: R(1.2, 3.6), v: R(0.0006, 0.0016), sw: R(0, 6.28), a: R(0.45, 0.85) });
    } else if (t === 'sol') {
      for (i = 0; i < 9; i++) parts.push({ ang: (i / 9) * 6.28 + R(-0.15, 0.15), w: R(0.05, 0.11), a: R(0.035, 0.07) });
      for (i = 0; i < 14; i++) parts.push({ mote: 1, x: R(0.35, 1), y: R(0, 0.8), s: R(1, 2.4), v: R(0.00015, 0.0004), sw: R(0, 6.28) });
    }

    var vind = -0.18; // regnet faller litt skrått
    function draw(ms) {
      ctx.clearRect(0, 0, W, H);
      if (t === 'regn') {
        ctx.lineCap = 'round'; ctx.lineWidth = 1.4;
        parts.forEach(function (p) {
          if (!still) { p.y += p.v; p.x += p.v * vind * 0.6; if (p.y > 1.05) { p.y = -0.05; p.x = R(-0.1, 1.15); } }
          var x = p.x * W, y = p.y * H;
          ctx.strokeStyle = 'rgba(176,206,236,' + p.a + ')';
          ctx.beginPath(); ctx.moveTo(x, y); ctx.lineTo(x + vind * p.l, y + p.l); ctx.stroke();
        });
      } else if (t === 'sno') {
        ctx.fillStyle = '#FFFFFF';
        parts.forEach(function (p) {
          if (!still) { p.y += p.v; p.sw += 0.015; if (p.y > 1.03) { p.y = -0.03; p.x = Math.random(); } }
          ctx.globalAlpha = p.a; ctx.beginPath(); ctx.arc(p.x * W + Math.sin(p.sw) * 10, p.y * H, p.s, 0, 6.28); ctx.fill();
        });
        ctx.globalAlpha = 1;
      } else if (t === 'sol') {
        var cx = W * 0.86, cy = -H * 0.08, r = Math.max(W, H) * 0.95, puls = still ? 1 : 0.92 + 0.08 * Math.sin(ms / 2600);
        var g = ctx.createRadialGradient(cx, cy, 0, cx, cy, r * 0.75);
        g.addColorStop(0, 'rgba(255,214,120,' + 0.30 * puls + ')'); g.addColorStop(0.35, 'rgba(255,190,90,' + 0.12 * puls + ')'); g.addColorStop(1, 'rgba(255,170,60,0)');
        ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
        var rot = still ? 0 : ms / 90000;
        parts.forEach(function (p) {
          if (p.mote) {
            if (!still) { p.y -= p.v; p.sw += 0.01; if (p.y < -0.02) { p.y = 0.85; p.x = R(0.35, 1); } }
            ctx.fillStyle = 'rgba(255,228,160,.45)'; ctx.beginPath(); ctx.arc(p.x * W + Math.sin(p.sw) * 6, p.y * H, p.s, 0, 6.28); ctx.fill();
            return;
          }
          var a = p.ang + rot, rg = ctx.createRadialGradient(cx, cy, 0, cx, cy, r);
          rg.addColorStop(0, 'rgba(255,220,140,' + p.a * puls + ')'); rg.addColorStop(1, 'rgba(255,220,140,0)');
          ctx.fillStyle = rg; ctx.beginPath(); ctx.moveTo(cx, cy);
          ctx.arc(cx, cy, r, a - p.w / 2, a + p.w / 2); ctx.closePath(); ctx.fill();
        });
      }
      if (!still) requestAnimationFrame(draw);
    }
    requestAnimationFrame(draw);
  }

  var q = (location.search.match(/[?&]vaer=([a-z0-9+]+)/) || [])[1];
  if (q) {
    var m = q.match(/(regn|sno|sol|ingen)(\d)?/);
    start({ t: m ? m[1] : 'ingen', styrke: m && m[2] ? +m[2] : 2, frost: q.indexOf('frost') >= 0 });
    return;
  }
  // Ny fil hver time (Pages mellomlagrer i 10 minutter)
  fetch('/vaer.json?h=' + Math.floor(Date.now() / 36e5)).then(function (r) { return r.ok ? r.json() : null; })
    .then(function (d) { if (d) start(d[LAND]); }).catch(function () {});
})();
