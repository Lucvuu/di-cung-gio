import sys, urllib.request, ssl, re
from bs4 import BeautifulSoup
sys.stdout.reconfigure(encoding='utf-8')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sheet_id = '14zjDQpmG9MydZiRXmTY7NUI9nVjqT_xNVDxxkwXfyAo'
url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/htmlview'

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, context=ctx) as resp:
    html = resp.read().decode('utf-8')

soup = BeautifulSoup(html, 'html.parser')

print("All Sheet Tabs found in HTML:")
for li in soup.find_all('li', id=re.compile(r'sheet-button')):
    print(" - ", li.get_text(strip=True), "id:", li.get('id'))

print("\n--- All Hyperlinks found in table ---")
for a in soup.find_all('a'):
    href = a.get('href', '')
    text = a.get_text(strip=True)
    if 'google.com' in href or 'drive.google.com' in href or 'docs.google.com' in href:
        print(f"Text: '{text}' -> Link: {href}")

print("\n--- Check all rows in all tables ---")
tables = soup.find_all('table')
print(f"Total tables: {len(tables)}")
for t_idx, table in enumerate(tables):
    print(f"\n=== Table {t_idx} ===")
    for tr in table.find_all('tr'):
        cells = [td.get_text(strip=True) for td in tr.find_all(['td', 'th'])]
        if any(cells):
            # check if any cell has link
            links_in_row = [a.get('href') for a in tr.find_all('a')]
            if links_in_row:
                print(f"Row: {cells} | Links: {links_in_row}")
            else:
                print(f"Row: {cells}")
