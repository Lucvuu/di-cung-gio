import sys, urllib.request, ssl, re, json
from bs4 import BeautifulSoup
sys.stdout.reconfigure(encoding='utf-8')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sheet_id = '14zjDQpmG9MydZiRXmTY7NUI9nVjqT_xNVDxxkwXfyAo'

for path in [
    f'https://docs.google.com/spreadsheets/d/{sheet_id}/pubhtml',
    f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:json&gid=0',
    f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:json&gid=2039270067'
]:
    print(f"\n=== FETCHING: {path} ===")
    req = urllib.request.Request(path, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, context=ctx) as resp:
            data = resp.read().decode('utf-8')
            print("Length:", len(data))
            if 'pubhtml' in path:
                soup = BeautifulSoup(data, 'html.parser')
                tables = soup.find_all('table')
                print("Tables in pubhtml:", len(tables))
                for a in soup.find_all('a'):
                    print("A tag:", a.get('href'), a.get_text(strip=True))
                # print text preview
                text = soup.get_text()
                lines = [l.strip() for l in text.split('\n') if l.strip()]
                print("First 20 lines of text:")
                for l in lines[:20]:
                    print("  ", l)
            elif 'gviz' in path:
                # remove /*O_o*/\ngoogle.visualization.Query.setResponse(...);
                m = re.search(r'setResponse\((.*)\);', data)
                if m:
                    jdata = json.loads(m.group(1))
                    cols = [c.get('label') or '' for c in jdata.get('table', {}).get('cols', [])]
                    print("Cols:", cols)
                    rows = jdata.get('table', {}).get('rows', [])
                    print(f"Total rows: {len(rows)}")
                    for r_idx, r in enumerate(rows[:5]):
                        cvals = [c.get('v') if c else '' for c in r.get('c', [])]
                        print(f"Row {r_idx}: {cvals}")
    except Exception as e:
        print("Error:", e)

