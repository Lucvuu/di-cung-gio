import sys, urllib.request, ssl, re
sys.stdout.reconfigure(encoding='utf-8')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sheet_id = '14zjDQpmG9MydZiRXmTY7NUI9nVjqT_xNVDxxkwXfyAo'
url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/edit'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, context=ctx) as resp:
    html = resp.read().decode('utf-8')

print('HTML length:', len(html))

# Let's search for "bootstrapData" or similar JS variables where Google Sheets embeds the sheet data!
matches = re.findall(r'var bootstrapData = (.*?);</script>', html, re.DOTALL)
print('bootstrapData matches:', len(matches))

# Find any links
urls = set(re.findall(r'https?://[^\s\"\'<>]+', html))
print(f'Total URLs found: {len(urls)}')
for u in sorted(urls):
    if any(k in u for k in ['drive.google', 'docs.google.com/document', 'docs.google.com/presentation', 'open?', 'id=', 'export']):
        print('Relevant URL:', u)

# Also search for "hoàn" or "hủy" or "hoan" or "huy" in html
keywords = ['hoàn', 'hủy', 'hoan', 'huy', 'chính sách', 'quy định', 'điều khoản', 'huỷ']
for kw in keywords:
    pos = 0
    found = []
    while True:
        idx = html.lower().find(kw, pos)
        if idx == -1 or len(found) > 5:
            break
        snippet = html[max(0, idx-50):min(len(html), idx+100)]
        found.append(snippet)
        pos = idx + len(kw)
    if found:
        print(f"\nKeyword '{kw}' found {len(found)} times. Sample:")
        for s in found[:2]:
            print("   ...", repr(s), "...")

