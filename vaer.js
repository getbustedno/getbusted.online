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
    ':root[data-vaer-frost] .stage .card .hk-b,:root[data-vaer-frost] .stage .card .hk-h{text-shadow:0 0 .1em rgba(225,242,255,.55),0 0 .4em rgba(170,215,255,.35);' +
      'background:linear-gradient(180deg,#EAF6FF 0%,#D3E89A 22%,var(--lime,#B7D147) 45%,var(--lime,#B7D147) 72%,#DDF0FF 100%);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}' +
    ':root[data-vaer-frost] .hero h1{text-shadow:0 0 .18em rgba(200,232,255,.35),0 .02em 0 rgba(235,247,255,.5)}';

  function start(v) {
    if (!v || !v.t) return;
    var t = v.t, styrke = Math.max(1, Math.min(3, v.styrke || 1));
    if (v.frost) root.setAttribute('data-vaer-frost', '');
    if (t !== 'ingen') root.setAttribute('data-vaer', t);
    var st = document.createElement('style'); st.textContent = CSS; document.head.appendChild(st);
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
