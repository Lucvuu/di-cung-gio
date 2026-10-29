import sys, urllib.request, ssl, re, json, csv, io
sys.stdout.reconfigure(encoding='utf-8')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sheet_id = '14zjDQpmG9MydZiRXmTY7NUI9nVjqT_xNVDxxkwXfyAo'

# 1. Fetch Sheet 0
csv_url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid=0'
req = urllib.request.Request(csv_url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, context=ctx) as resp:
    sheet0_csv = resp.read().decode('utf-8')

# 2. Fetch HTML to map hyperlinks
html_url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/edit'
req_html = urllib.request.Request(html_url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req_html, context=ctx) as resp:
    html = resp.read().decode('utf-8')

# Search for link mappings in html
# We can find occurrences of document IDs and preceding or nearby texts
reader = list(csv.reader(io.StringIO(sheet0_csv)))
tours = []
for row in reader[3:]: # start after headers
    if len(row) >= 7 and row[0].strip() and row[0].strip().isdigit():
        stt = row[0].strip()
        code = row[1].strip()
        name = row[2].strip()
        link_title = row[3].strip()
        min_pax = row[4].strip()
        departure = row[5].strip()
        price = row[6].strip()
        age_5_9 = row[7].strip() if len(row) > 7 else ''
        foreign = row[8].strip() if len(row) > 8 else ''
        single_room = row[9].strip() if len(row) > 9 else ''
        tours.append({
            'stt': stt,
            'code': code,
            'name': name,
            'link_title': link_title,
            'min_pax': min_pax,
            'departure': departure,
            'price': price,
            'age_5_9': age_5_9,
            'foreign': foreign,
            'single_room': single_room
        })

print(f"Total tours in sheet 0: {len(tours)}")
for t in tours:
    print(f"[{t['stt']}] Code: {t['code']:6} | Price: {t['price']:8} | Name: {t['name']}")

# Now let's extract all doc links with their anchor / cell texts from html
matches = re.findall(r'(\"https://docs\.google\.com/document/d/([a-zA-Z0-9_\-]+)[^\"]*\")', html)
doc_ids = set()
for full_url, doc_id in matches:
    doc_ids.add(doc_id)

print(f"\nUnique doc IDs found: {len(doc_ids)}")

# Download and inspect each doc
doc_contents = {}
for did in list(doc_ids):
    doc_url = f'https://docs.google.com/document/d/{did}/export?format=txt'
    try:
        req_d = urllib.request.Request(doc_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req_d, context=ctx) as resp_d:
            d_text = resp_d.read().decode('utf-8')
            first_line = d_text.strip().split('\n')[0] if d_text.strip() else 'EMPTY'
            # check if policy is inside
            has_policy = 'HOÀN HỦY' in d_text or 'hoàn hủy' in d_text.lower()
            doc_contents[did] = {
                'title': first_line[:80],
                'length': len(d_text),
                'has_policy': has_policy,
                'text': d_text
            }
            print(f"Doc {did}: '{first_line[:50]}' (Length: {len(d_text)}, Policy: {has_policy})")
    except Exception as e:
        print(f"Doc {did} failed: {e}")

# Save all doc contents to a json file for easy processing
with open('scripts/all_docs.json', 'w', encoding='utf-8') as f:
    json.dump({k: {'title': v['title'], 'has_policy': v['has_policy'], 'text': v['text']} for k, v in doc_contents.items()}, f, ensure_ascii=False, indent=2)

print("\nSaved all_docs.json successfully!")

