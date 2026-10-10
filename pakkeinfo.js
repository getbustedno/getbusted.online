/*
 * Pakkeinfo på getbusted.no og getbusted.online: trykk på en pakke for å se hva den inneholder.
 * Data fra /pakkeinfo.json (lages av _kilde/pakkeinfo.py fra appens cards.json):
 * antall kort, fordeling på Mild/Frekk/Get Fu**ed, kortmiks og to smakebiter uten drikke.
 * Oppdaterer også «N kort» på flisene, så tallene alltid stemmer med appen.
 */
(function () {
  var tiles = document.querySelectorAll('.pack[data-pack]');
  if (!tiles.length || !window.fetch) return;
  var LANG = (document.documentElement.lang || 'no').slice(0, 2);
  var TX = {
    no: { kort: 'kort', niv: ['Mild', 'Frekk', 'Get Fu**ed'], nivT: 'Nivåer', mix: 'Kortmiks', smak: 'Smakebiter', lukk: 'Lukk',
      orig: 'Gratis: 50 kort hver kveld. Lås opp alt med Busted+.', start: 'Med fra start', hint: 'Trykk for å se innholdet',
      head: { pekeleken: 'På tre - pek på den som', drikk_om: 'Har du ...', sannhet: 'Sannhet', navnekort: 'Utfordring' },
      typ: { drikk_om: 'Har du', pekeleken: 'Pekeleken', navnekort: 'Utfordring', sannhet: 'Sannhet', duell: 'Duell', regel: 'Ny regel', hemmelig: 'Hemmelig oppdrag', runde: 'Runde', sang: 'Sangkort', quiz: 'Quiz' } },
    sv: { kort: 'kort', niv: ['Mild', 'Fräck', 'Get Fu**ed'], nivT: 'Nivåer', mix: 'Kortmix', smak: 'Smakprov', lukk: 'Stäng',
      orig: 'Gratis: 50 kort varje kväll. Lås upp allt med Busted+.', start: 'Med från start', hint: 'Tryck för att se innehållet',
      head: { pekeleken: 'På tre - peka på den som', drikk_om: 'Har du ...', sannhet: 'Sanning', navnekort: 'Utmaning' },
      typ: { drikk_om: 'Har du', pekeleken: 'Pekleken', navnekort: 'Utmaning', sannhet: 'Sanning', duell: 'Duell', regel: 'Ny regel', hemmelig: 'Hemligt uppdrag', runde: 'Runda', sang: 'Låtkort', quiz: 'Quiz' } },
    da: { kort: 'kort', niv: ['Mild', 'Fræk', 'Get Fu**ed'], nivT: 'Niveauer', mix: 'Kortmix', smak: 'Smagsprøver', lukk: 'Luk',
      orig: 'Gratis: 50 kort hver aften. Lås alt op med Busted+.', start: 'Med fra start', hint: 'Tryk for at se indholdet',
      head: { pekeleken: 'På tre - peg på den, der', drikk_om: 'Har du ...', sannhet: 'Sandhed', navnekort: 'Udfordring' },
      typ: { drikk_om: 'Har du', pekeleken: 'Pegelegen', navnekort: 'Udfordring', sannhet: 'Sandhed', duell: 'Duel', regel: 'Ny regel', hemmelig: 'Hemmelig mission', runde: 'Runde', sang: 'Sangkort', quiz: 'Quiz' } },
    en: { kort: 'cards', niv: ['Mild', 'Cheeky', 'Get Fu**ed'], nivT: 'Levels', mix: 'Card mix', smak: 'Sneak peek', lukk: 'Close',
      orig: 'Free: 50 cards every night. Unlock everything with Busted+.', start: 'In from day one', hint: 'Tap to see what is inside',
      head: { pekeleken: 'On three, point at the one who', drikk_om: 'Have you ever ...', sannhet: 'Truth', navnekort: 'Challenge' },
      typ: { drikk_om: 'Have you', pekeleken: 'Pointing game', navnekort: 'Challenge', sannhet: 'Truth', duell: 'Duel', regel: 'New rule', hemmelig: 'Secret mission', runde: 'Round', sang: 'Song card', quiz: 'Quiz' } }
  }[LANG];
  if (!TX) return;

  var css = document.createElement('style');
  css.textContent =
    '.pack[data-pack]{cursor:pointer}.pack[data-pack]:focus-visible{outline:2px solid var(--c,#B7D147);outline-offset:6px;border-radius:14px}' +
    '.pi{margin:auto;border:0;padding:0;background:transparent;max-width:min(760px,calc(100vw - 32px));width:100%;color:var(--fg,#F4F1EA);overflow:visible}' +
    '.pi::backdrop{background:rgba(8,8,10,.72);backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px)}' +
    '.pi-in{position:relative;display:grid;grid-template-columns:220px 1fr;gap:26px;background:#1d1d1f;border-radius:24px;padding:26px;' +
      'box-shadow:0 0 0 2px var(--c),0 0 60px -10px var(--c),0 40px 90px rgba(0,0,0,.6);max-height:calc(100dvh - 40px);overflow:auto;animation:pi-inn .28s cubic-bezier(.2,.9,.3,1.2)}' +
    '@keyframes pi-inn{from{opacity:0;transform:translateY(18px) scale(.96) rotate(-1deg)}to{opacity:1;transform:none}}' +
    '.pi-cov img{width:100%;height:auto;border-radius:14px;display:block;box-shadow:0 0 0 2px var(--c),0 18px 40px -10px var(--c);transform:rotate(-2deg)}' +
    '.pi-x{position:absolute;top:12px;right:12px;width:38px;height:38px;border-radius:50%;border:1.5px solid rgba(255,255,255,.2);background:#262628;color:#fff;font-size:20px;line-height:1;cursor:pointer}' +
    '.pi h3{margin:0;font-size:34px;line-height:1;color:var(--c);padding-right:40px}' +
    '.pi-tag{margin:6px 0 0;color:var(--muted,#B9B6AD);font-size:16px}' +
    '.pi-big{display:flex;align-items:baseline;gap:10px;margin:16px 0 4px}.pi-big b{font-size:44px;font-weight:900;font-style:italic;line-height:1}.pi-big span{color:var(--muted,#B9B6AD);font-weight:700;text-transform:uppercase;letter-spacing:.5px;font-size:13px}' +
    '.pi-st{display:inline-block;margin-top:4px;font-size:12px;font-weight:800;letter-spacing:.5px;text-transform:uppercase;color:#1E1E1E;background:var(--c);border-radius:999px;padding:3px 10px}' +
    '.pi h4{margin:18px 0 8px;font-size:13px;letter-spacing:.8px;text-transform:uppercase;color:#8F8D85;font-style:normal}' +
    '.pi-bar{display:grid;grid-template-columns:96px 1fr 38px;align-items:center;gap:10px;font-size:14px;font-weight:700;margin:6px 0}' +
    '.pi-bar i{display:block;height:10px;border-radius:9px;background:rgba(255,255,255,.08);overflow:hidden}.pi-bar i em{display:block;height:100%;border-radius:9px;background:var(--c);transform-origin:left;animation:pi-bar .7s .15s cubic-bezier(.2,.8,.2,1) both}' +
    '.pi-bar:nth-child(2) i em{opacity:.8}.pi-bar:nth-child(3) i em{opacity:.6}.pi-bar span{text-align:right;color:var(--muted,#B9B6AD)}' +
    '@keyframes pi-bar{from{transform:scaleX(0)}}' +
    '.pi-chips{display:flex;flex-wrap:wrap;gap:6px}.pi-chips span{font-size:13px;font-weight:700;border:1.5px solid rgba(255,255,255,.14);border-radius:999px;padding:4px 10px}.pi-chips b{color:var(--c);margin-left:4px}' +
    '.pi-smak{display:grid;grid-template-columns:1fr 1fr;gap:12px}' +
    '.pi-k{background:#2a2a2c;border-radius:14px;padding:14px 14px 16px;box-shadow:0 0 0 1.5px var(--c);font-style:italic;text-transform:uppercase;text-align:center}' +
    '.pi-k p{margin:0}.pi-k .h{font-size:11px;font-weight:800;color:var(--c);letter-spacing:.3px}.pi-k .t{font-size:16px;font-weight:900;line-height:1.1;margin-top:6px;color:#F4F1EA}' +
    '@media (max-width:640px){.pi-in{grid-template-columns:1fr;padding:20px;gap:14px}.pi-cov{width:120px}.pi h3{font-size:28px}.pi-smak{grid-template-columns:1fr}}' +
    '@media (prefers-reduced-motion:reduce){.pi-in,.pi-bar i em{animation:none}}';
  document.head.appendChild(css);

  var DATA = null;
  fetch('/pakkeinfo.json?d=' + Math.floor(Date.now() / 864e5)).then(function (r) { return r.ok ? r.json() : null; }).then(function (d) {
    DATA = d && d[LANG];
    if (!DATA) return;
    tiles.forEach(function (el) {
      var p = DATA[el.getAttribute('data-pack')], sm = el.querySelector('small');
      if (p && sm && el.getAttribute('data-pack') !== 'original' && /\d/.test(sm.textContent)) sm.textContent = p.n + ' ' + TX.kort;
    });
  }).catch(function () {});

  var esc = function (s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); };
  var dlg = null, last = null;
  function apne(el) {
    if (!DATA) return;
    var slug = el.getAttribute('data-pack'), p = DATA[slug];
    if (!p) return;
    last = el;
    var c = getComputedStyle(el).getPropertyValue('--c').trim() || '#B7D147';
    var img = el.querySelector('img'), navn = (el.querySelector('b') || {}).textContent || '', tag = (el.querySelector('span') || {}).textContent || '';
    var soon = el.querySelector('.soon:not(.hot)'), st = slug === 'original' ? TX.orig : soon ? soon.textContent : '';
    var maks = Math.max.apply(null, p.niv) || 1;
    var bars = p.niv.map(function (n, i) { return '<div class="pi-bar"><b>' + TX.niv[i] + '</b><i><em style="width:' + (100 * n / maks).toFixed(0) + '%"></em></i><span>' + n + '</span></div>'; }).join('');
    var chips = p.typer.slice(0, 6).map(function (t) { return '<span>' + esc(TX.typ[t[0]] || t[0]) + '<b>' + t[1] + '</b></span>'; }).join('');
    var smak = p.smak.map(function (k) { return '<div class="pi-k"><p class="h">' + esc(TX.head[k.t] || '') + '</p><p class="t">' + esc(k.x) + (k.t === 'drikk_om' ? '?' : '') + '</p></div>'; }).join('');
    if (!dlg) {
      dlg = document.createElement('dialog'); dlg.className = 'pi';
      dlg.addEventListener('click', function (e) { if (e.target === dlg) dlg.close(); });
      dlg.addEventListener('close', function () { if (last) last.focus(); });
      document.body.appendChild(dlg);
    }
    dlg.style.setProperty('--c', c);
    dlg.setAttribute('aria-label', navn);
    dlg.innerHTML = '<div class="pi-in"><button class="pi-x" type="button" aria-label="' + TX.lukk + '">×</button>' +
      '<div class="pi-cov"><img src="' + (img ? img.currentSrc || img.src : '') + '" alt=""></div><div>' +
      '<h3>' + esc(navn) + '</h3>' + (tag ? '<p class="pi-tag">' + esc(tag) + '</p>' : '') +
      '<div class="pi-big"><b>' + p.n + '</b><span>' + TX.kort + '</span></div>' + (st ? '<span class="pi-st">' + esc(st) + '</span>' : '') +
      '<h4>' + TX.nivT + '</h4>' + bars + '<h4>' + TX.mix + '</h4><div class="pi-chips">' + chips + '</div>' +
      (smak ? '<h4>' + TX.smak + '</h4><div class="pi-smak">' + smak + '</div>' : '') + '</div></div>';
    dlg.querySelector('.pi-x').addEventListener('click', function () { dlg.close(); });
    if (dlg.showModal) dlg.showModal(); else dlg.setAttribute('open', '');
  }
  tiles.forEach(function (el) {
    el.setAttribute('role', 'button'); el.setAttribute('tabindex', '0'); el.setAttribute('title', TX.hint);
    el.addEventListener('click', function (e) { if (!e.target.closest('a')) apne(el); });
    el.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); apne(el); } });
  });
})();
