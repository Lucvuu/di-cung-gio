import sys, urllib.request, ssl, re, json
sys.stdout.reconfigure(encoding='utf-8')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sheet_id = '14zjDQpmG9MydZiRXmTY7NUI9nVjqT_xNVDxxkwXfyAo'
url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/edit'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, context=ctx) as resp:
    html = resp.read().decode('utf-8')

# Search for HYPERLINK formulas or doc links in bootstrapData
# E.g. find patterns like ["TREKKING...", "https://docs.google.com/document/d/..."]
matches = re.findall(r'(https://docs\.google\.com/document/d/[a-zA-Z0-9_\-]+[^\"]*)', html)
clean_docs = []
for m in matches:
    clean = m.split('\\')[0].split('"')[0]
    if clean not in clean_docs:
        clean_docs.append(clean)

print(f"Found {len(clean_docs)} unique Google Docs:")
for d in clean_docs:
    print(d)

