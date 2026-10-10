#!/usr/bin/env python3
"""Pakkeinfo til nettsidene: antall kort per nivå, kortmiks og to smakebiter per pakke og språk.
Leser cards.json fra appen (master) og skriver pakkeinfo.json. Kjør på nytt når kortene endres:
  python3 _kilde/pakkeinfo.py <sti til cards.json> pakkeinfo.json no        (getbusted.no)
  python3 _kilde/pakkeinfo.py <sti til cards.json> pakkeinfo.json sv da en  (getbusted.online)
Smakebitene er nivå 1, uten drikke og uten spillernavn (nettsidene viser aldri alkohol)."""
import json, re, sys, collections, random
src, ut, langs = sys.argv[1], sys.argv[2], sys.argv[3:]
cs = json.load(open(src, encoding='utf-8')); cs = cs if isinstance(cs, list) else cs['cards']
DRIKK = re.compile(r'drikk|drick|drik|drink|slurk|klunk|tår\b|sip|shot|skål|skål|cheers|øl\b|öl\b|beer|vin\b|wine|sprit|vodka|tequila|champagne|alkohol|alcohol|fyll|full\b|fuld|drunk|bånn|botten|vors|förfest|pregame|promille|bakfull|bakrus|tømmermænd|hungover|bar\b|pub\b|baren|del ut|dela ut|deler ut|hand out|give out|uddel|giv \d|ge bort', re.I)
SAMPLE_TYPES = ['pekeleken', 'drikk_om', 'sannhet', 'navnekort']
TYPER = {'drikk_om', 'pekeleken', 'navnekort', 'sannhet', 'duell', 'regel', 'hemmelig', 'runde', 'sang', 'quiz'}
ut_data = {}
for L in langs:
    by = collections.defaultdict(list)
    for c in cs:
        if c.get('lang') == L: by[c['pack']].append(c)
    d = {}
    for pack, kort in by.items():
        niv = collections.Counter(c.get('spice', 1) for c in kort)
        typ = collections.Counter(c['type'] for c in kort if c['type'] in TYPER)
        r = random.Random(pack + L)
        cand = [c for c in kort if c.get('spice', 1) == 1 and c['type'] in SAMPLE_TYPES and '{' not in c['text']
                and not DRIKK.search(c['text'] + ' ' + str(c.get('twist', ''))) and len(c['text']) <= 95]
        cand.sort(key=lambda c: (SAMPLE_TYPES.index(c['type']), c['id'])); r.shuffle(cand)
        smak, brukt = [], set()
        for c in cand:  # helst to ulike korttyper
            if c['type'] in brukt and len(cand) > 4: continue
            smak.append({'t': c['type'], 'x': c['text']}); brukt.add(c['type'])
            if len(smak) == 2: break
        d[pack] = {'n': len(kort), 'niv': [niv.get(1, 0), niv.get(2, 0), niv.get(3, 0)],
                   'typer': typ.most_common(), 'smak': smak}
    ut_data[L] = d
json.dump(ut_data, open(ut, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print({L: {p: v['n'] for p, v in d.items()} for L, d in ut_data.items()})
