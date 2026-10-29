import sys, urllib.request, ssl, re, csv, io
sys.stdout.reconfigure(encoding='utf-8')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sheet_id = '14zjDQpmG9MydZiRXmTY7NUI9nVjqT_xNVDxxkwXfyAo'

html_url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/htmlview'
req = urllib.request.Request(html_url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, context=ctx) as resp:
        html = resp.read().decode('utf-8')
        print("HTML length:", len(html))
        # Look for sheet names and gids in script tag or html
        matches = re.findall(r'item-name">([^<]+)<', html)
        print("Tab item-names:", matches)
        button_matches = re.findall(r'<li id="sheet-button-([0-9]+)".*?<a[^>]*>(.*?)</a>', html, re.DOTALL)
        print("Button tabs:", button_matches)
        all_gids = set(re.findall(r'gid=([0-9]+)', html))
        print("All gids found:", all_gids)
except Exception as e:
    print("Error reading htmlview:", e)

# Also dump gid=0
csv_url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid=0'
req2 = urllib.request.Request(csv_url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req2, context=ctx) as resp:
        content = resp.read().decode('utf-8')
        print("\n--- CONTENT OF GID=0 ---")
        reader = csv.reader(io.StringIO(content))
        for row_idx, row in enumerate(reader):
            if any(cell.strip() for cell in row):
                print(f"Row {row_idx}: {row}")
except Exception as e:
    print("Error reading gid=0:", e)
