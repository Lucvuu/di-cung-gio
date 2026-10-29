import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/all_docs.json', 'r', encoding='utf-8') as f:
    docs = json.load(f)

for did, d in docs.items():
    print(f"==================================================")
    print(f"DOC ID: {did}")
    print(f"TITLE: {d['title']}")
    # print first 500 chars
    lines = [l.strip() for l in d['text'].split('\n') if l.strip()]
    for l in lines[:10]:
        print("  ", l)
