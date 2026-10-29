import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/all_docs.json', 'r', encoding='utf-8') as f:
    docs = json.load(f)

print(f"Loaded {len(docs)} docs.")
policies = set()
for did, d in docs.items():
    text = d['text']
    # find section starting from HOÀN HỦY or CHÍNH SÁCH
    m = re.search(r'(CHÍNH SÁCH HOÀN HỦY[^\n]*\n.*)', text, re.DOTALL | re.IGNORECASE)
    if m:
        policy_text = m.group(1)[:400].strip()
        policies.add(policy_text)
        print(f"\n--- DOC {did} ({d['title']}) ---")
        print(policy_text[:250])
    else:
        print(f"\n--- DOC {did} ({d['title']}) NO DIRECT REGEX MATCH ---")

print("\n\n=== UNIQUE POLICIES FOUND ===")
for p in policies:
    print("----------------")
    print(p[:300])

