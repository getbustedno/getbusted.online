#!/usr/bin/env python3
"""Været i hero: henter værmeldingen fra Meteorologisk institutt (api.met.no) for
ti byer per land og skriver et landssnitt til vaer.json. Kjøres av GitHub Actions
hver time (.github/workflows/vaer.yml). Nettleseren til den besøkende henter bare
vaer.json fra vår egen side, så ingen data om besøkende går til tredjepart.

Bruk: python3 _kilde/vaer.py vaer.json no [se dk]

Filen skrives bare når tilstanden faktisk endres, så siden bygges ikke på nytt hver time.

Regler per land:
- nedbør i minst 4 av 10 byer  -> «regn», eller «sno» når de fleste byene med nedbør har snø
- ellers sol eller lettskyet på dagtid i minst halvparten av byene -> «sol»
- ellers ingenting (opphold, skyet eller klart om natta)
- snittemperatur under 0 -> frost (rim på kortet), i tillegg til tilstanden over
- styrke 1 til 3 etter hvor mye det kommer
"""
import json, sys, time, urllib.request
from datetime import datetime, timezone

UA = 'getbusted.no vaer/1.0 kontakt@getbusted.no'
BYER = {
    'no': [('Oslo', 59.91, 10.75), ('Bergen', 60.39, 5.32), ('Trondheim', 63.43, 10.39),
           ('Stavanger', 58.97, 5.73), ('Kristiansand', 58.15, 8.0), ('Tromsø', 69.65, 18.96),
           ('Bodø', 67.28, 14.4), ('Ålesund', 62.47, 6.15), ('Lillehammer', 61.12, 10.47),
           ('Lillestrøm', 59.96, 11.05)],
    'se': [('Stockholm', 59.33, 18.07), ('Göteborg', 57.71, 11.97), ('Malmö', 55.6, 13.0),
           ('Uppsala', 59.86, 17.64), ('Västerås', 59.61, 16.55), ('Örebro', 59.27, 15.21),
           ('Linköping', 58.41, 15.62), ('Umeå', 63.83, 20.26), ('Luleå', 65.58, 22.15),
           ('Sundsvall', 62.39, 17.31)],
    'dk': [('København', 55.68, 12.57), ('Aarhus', 56.16, 10.2), ('Odense', 55.4, 10.39),
           ('Aalborg', 57.05, 9.92), ('Esbjerg', 55.48, 8.46), ('Randers', 56.46, 10.04),
           ('Kolding', 55.49, 9.47), ('Horsens', 55.86, 9.85), ('Vejle', 55.71, 9.54),
           ('Roskilde', 55.64, 12.08)],
}


def hent(lat, lon):
    url = f'https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={lat}&lon={lon}'
    for forsok in range(3):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=20) as r:
                return json.load(r)
        except Exception:
            time.sleep(2 + forsok * 3)
    return None


def by_naa(data):
    """Tidspunktet i meldingen som ligger nærmest nå."""
    now = datetime.now(timezone.utc)
    ts = data['properties']['timeseries']
    t = min(ts, key=lambda x: abs((datetime.fromisoformat(x['time'].replace('Z', '+00:00')) - now).total_seconds()))
    d = t['data']
    temp = d['instant']['details'].get('air_temperature')
    n1 = d.get('next_1_hours') or d.get('next_6_hours') or {}
    sym = (n1.get('summary') or {}).get('symbol_code', '')
    mm = (n1.get('details') or {}).get('precipitation_amount', 0) or 0
    if 'next_6_hours' in d and 'next_1_hours' not in d:
        mm = mm / 6
    nedbor = mm >= 0.1 or any(w in sym for w in ('rain', 'sleet', 'snow', 'showers'))
    sno = 'snow' in sym or ('sleet' in sym and temp is not None and temp < 1) or (nedbor and temp is not None and temp <= 0.5)
    sol = sym.startswith(('clearsky_day', 'fair_day'))
    return {'temp': temp, 'nedbor': nedbor, 'sno': sno, 'sol': sol, 'mm': mm}


def land(kode):
    byer = [b for b in (hent(lat, lon) for _, lat, lon in BYER[kode]) if b]
    if len(byer) < 5:
        return None  # for lite data: behold det som står
    vs = [by_naa(b) for b in byer]
    n = len(vs)
    ned = [v for v in vs if v['nedbor']]
    temps = [v['temp'] for v in vs if v['temp'] is not None]
    snitt = sum(temps) / len(temps) if temps else 5
    t = 'ingen'
    styrke = 1
    if len(ned) / n >= 0.4:
        t = 'sno' if sum(v['sno'] for v in ned) > len(ned) / 2 else 'regn'
        mm = sum(v['mm'] for v in ned) / len(ned)
        styrke = 3 if mm >= 2 else 2 if mm >= 0.6 else 1
        if len(ned) / n >= 0.7:
            styrke = min(3, styrke + 1)
    elif sum(v['sol'] for v in vs) / n >= 0.5:
        t = 'sol'
    return {'t': t, 'styrke': styrke, 'frost': snitt < 0}


def main():
    ut, koder = sys.argv[1], sys.argv[2:] or ['no']
    try:
        gammel = json.load(open(ut, encoding='utf-8'))
    except Exception:
        gammel = {}
    ny = dict(gammel)
    for k in koder:
        r = land(k)
        if r:
            ny[k] = r
    print(json.dumps(ny, ensure_ascii=False))
    if ny != gammel:
        with open(ut, 'w', encoding='utf-8') as f:
            json.dump(ny, f, ensure_ascii=False, separators=(',', ':'))
            f.write('\n')
        print('endret')
    else:
        print('uendret')


if __name__ == '__main__':
    main()
