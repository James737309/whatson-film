"""Build WhatsOn Film.

1. raw_tv.txt  -> the TV list inside data.js   (python3 src/build.py --tv)
2. app.html + data.js -> index.html             (python3 src/build.py)

raw_tv.txt format, one showing per line:
  MM-DD|HH:MM|Channel|Title|Year|genre codes|cert
  cert: U, PG, 12, 15, 18, blank = TBC, * = premiere (cert TBC)
  genre codes: A Action, Ad Adventure, An Animation, X Christmas, C Comedy,
  Cr Crime, D Drama, F Family, Fa Fantasy, H Horror, R Romance, S Sci-fi,
  T Thriller, W War, We Western, Do Documentary
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
YEAR = '2026'
G = {'A': 'Action', 'Ad': 'Adventure', 'An': 'Animation', 'X': 'Christmas', 'C': 'Comedy',
     'Cr': 'Crime', 'D': 'Drama', 'F': 'Family', 'Fa': 'Fantasy', 'H': 'Horror', 'R': 'Romance',
     'S': 'Sci-fi', 'T': 'Thriller', 'W': 'War', 'We': 'Western', 'Do': 'Documentary'}


def tv_rows():
    rows = []
    for ln in open(os.path.join(HERE, 'raw_tv.txt'), encoding='utf-8'):
        ln = ln.rstrip('\n')
        if not ln or ln.startswith('#'):
            continue
        d, t, ch, title, y, g, c = ln.split('|')
        prem = c == '*'
        row = [f'{YEAR}-{d}', t, ch, title, int(y), ','.join(G[x] for x in g.split(',')),
               'TBC' if prem or not c else c]
        if prem:
            row.append('Premiere')
        rows.append(row)
    rows.sort(key=lambda r: (r[0], r[1], r[2]))
    return rows


def update_data():
    path = os.path.join(HERE, 'data.js')
    d = open(path, encoding='utf-8').read()
    s = d.index('const TV = ')
    e = d.index('];', s) + 2
    tv = json.dumps(tv_rows(), ensure_ascii=False).replace('],[', '],\n[')
    open(path, 'w', encoding='utf-8').write(d[:s] + 'const TV = ' + tv + ';' + d[e:])


def build():
    app = open(os.path.join(HERE, 'app.html'), encoding='utf-8').read()
    data = open(os.path.join(HERE, 'data.js'), encoding='utf-8').read()
    open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8').write(app.replace('/*DATA*/', data))
    print('Built index.html')


if __name__ == '__main__':
    if '--tv' in sys.argv:
        update_data()
    build()
