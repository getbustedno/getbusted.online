"""Heltekortet i hero (midtkortet i kortviften) på getbusted.online: engelsk (/), svensk (/se/) og dansk (/dk/).

Kortet er ekte HTML/CSS (stiler i style.css, .hk-*). Første kortet i listen per språk står server-rendret i HTML
(vises uten JS). En liten inline-JS velger ett kort tilfeldig (Math.random) ved hver sidelasting.
Ingen cookies, ingen localStorage, ingen sporing, ingen ekstern kode.
Brukes av build.py (hero_card_html). Bytt kort ved å endre KORT under og kjøre: python3 build.py

KORT-ID-ER (til regelvakt, ordrett fra getbusted-merge/src/data/cards.json):
  sv: SV1531 SV0063 SV0412 SV1529 GB066-SV SV1522 SV0418 SV0218
  da: DA0127 DA0133 DA0592 DA0417 DA0988 DA0593 DA0139 DA0595
  en: EN0064 EN0069 EN1527 EN0232 EN1523 EN1521 EN0420 EN0245
Valgt etter: pekeleken eller drikk_om, spice 1-2, ikke minPlayers, ingen {spiller}, ingen alkohol-, drikke-,
skole-, sex- eller kjendisord, ikke på listen over kort uten markedsføring i regelvakt.md, ikke GB013.
Alkoholfri tone, siden svensk alkoholreklame er strengt regulert: overskrifter og bunntekst følger appen i
alkoholfri modus (HEADERS sober i engine.ts, SOBER_RULES i i18n.ts).
"""
import json, pathlib, re


# Per språk: (id, type, tekst). type: 'pek' = pekeleken, 'drikk' = drikk_om. Tekst ordrett fra cards.json.
KORT = {
  'sv': [
    ('SV1531', 'pek', 'frågar efter wifi-lösenordet i en stuga utan rinnande vatten'),
    ('SV0063', 'pek', 'skickar Swish-förfrågan för en kaffe'),
    ('SV0412', 'pek', 'somnar först i soffan under Kalle Anka'),
    ('SV1529', 'pek', 'säger att de ska vara offline hela helgen och lägger upp tre stories första kvällen'),
    ('GB066-SV', 'pek', 'kallar sig skidåkare efter en helg i Sälen'),
    ('SV1522', 'pek', 'somnar först, mitt i ett parti Monopol'),
    ('SV0418', 'pek', 'bråkar om senapen på julskinkan som om det vore politik'),
    ('SV0218', 'pek', 'tycker halloween är amerikanskt trams men är mest utklädd ändå'),
  ],
  'da': [
    ('DA0127', 'pek', 'kalder alt vest for Valby for «Jylland»'),
    ('DA0133', 'pek', 'har flest ubetalte MobilePay-anmodninger liggende'),
    ('DA0592', 'pek', 'siger «vi giver ikke gaver i år» og så alligevel køber noget'),
    ('DA0417', 'pek', 'siger «halloween er amerikansk pjat» men har planlagt sit kostume siden august'),
    ('DA0988', 'pek', 'forsvinder, når der skal gøres rent til aflevering'),
    ('DA0593', 'pek', 'falder i søvn, før kongens nytårstale er slut'),
    ('DA0139', 'pek', 'regner fællesspisningen ud på MobilePay ned til 50 øre'),
    ('DA0595', 'pek', 'stadig får pakkekalender af sin mor'),
  ],
  'en': [
    ('EN0064', 'pek', 'has asked ChatGPT something embarrassing this week'),
    ('EN0069', 'pek', 'would get scammed by a deepfake of their own mum'),
    ('EN1527', 'pek', 'sends the Splitwise request before the car is even unpacked'),
    ('EN0232', 'pek', "would say “let's split up, it'll be quicker”"),
    ('EN1523', 'pek', 'turns into a completely different person during Monopoly'),
    ('EN1521', 'pek', 'has never once done the dishes at a cabin'),
    ('EN0420', 'pek', 'will buy every single present on Christmas Eve'),
    ('EN0245', 'pek', 'would buy half of Spirit Halloween and use none of it'),
  ],
}

# Alkoholfri tone, som appen skriver det (engine.ts HEADERS sober, i18n.ts footers.pek + SOBER_RULES).
HEAD = {
    'sv': {'pek': 'På tre - peka på den som', 'drikk': 'Ta en poäng om du har'},
    'da': {'pek': 'På tre - peg på den der', 'drikk': 'Point hvis du har'},
    'en': {'pek': 'On three, point at the one who', 'drikk': 'Points if you have'},
}
FOOT = {
    'sv': 'Den med flest pekningar får 2 poäng',
    'da': 'Den, flest peger på, får 2 point',
    'en': 'Whoever gets the most fingers gets 2 points',
}
HANDLE = {l: '@getbusted.no' for l in HEAD}  # samme som i de gamle kortbildene


def storrelse(tekst):
    """Startstørrelse på brødteksten i cqw (prosent av kortbredden), etter lengde og lengste ord.
    JS finjusterer etterpå hvis noe likevel flyter ut."""
    n = len(tekst)
    s = 14 if n <= 30 else 12.5 if n <= 60 else 11 if n <= 75 else 9.5 if n <= 95 else 8.5
    lengste = max(len(w) for w in re.split(r'[\s-]+', tekst))
    return round(min(s, 84 / (lengste * 0.58)), 1)


def kort_data(lang, kort):
    return [{'h': HEAD[lang][t], 'b': tekst, 'f': FOOT[lang] if t == 'pek' else '', 's': storrelse(tekst)}
            for _id, t, tekst in kort]


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')


def kort_html(lang, kort):
    data = kort_data(lang, kort)
    d0 = data[0]
    js_data = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    foot = f'<p class="hk-f">{esc(d0["f"])}</p>' if d0['f'] else '<p class="hk-f" hidden></p>'
    return (
        '<div class="card hk" data-hk>'
        '<div class="hk-in">'
        f'<p class="hk-h">{esc(d0["h"])}</p>'
        f'<p class="hk-b" style="--fs:{d0["s"]}cqw">{esc(d0["b"])}</p>'
        f'{foot}'
        '</div>'
        f'<p class="hk-t">{esc(HANDLE[lang])}</p>'
        '</div>\n'
        '<script>\n'
        '(function(){var c=document.querySelector("[data-hk]");if(!c)return;var K=' + js_data + ';'
        'var k=K[Math.floor(Math.random()*K.length)];'
        'var i=c.querySelector(".hk-in"),h=c.querySelector(".hk-h"),b=c.querySelector(".hk-b"),f=c.querySelector(".hk-f");'
        'h.textContent=k.h;b.textContent=k.b;f.textContent=k.f;f.hidden=!k.f;'
        'function fit(){var s=k.s;b.style.setProperty("--fs",s+"cqw");'
        'while(s>5&&(i.scrollHeight>i.clientHeight+1||b.scrollWidth>b.clientWidth+1)){s-=.5;b.style.setProperty("--fs",s+"cqw")}}'
        'fit();if(document.fonts&&document.fonts.ready)document.fonts.ready.then(fit)})();\n'
        '</script>'
    )


def hero_card_html(lang):
    return '<!--heltekort-->' + kort_html(lang, KORT[lang]) + '<!--/heltekort-->'
