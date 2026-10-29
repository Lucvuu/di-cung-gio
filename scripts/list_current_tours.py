import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/generate_main_js.py', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r"id:\s*([0-9]+),\s*title:\s*['\"]([^'\"]+)['\"],\s*category:\s*['\"]([^'\"]+)['\"].*?price:\s*['\"]([^'\"]+)['\"]", text, re.DOTALL)
for mid, title, cat, price in matches:
    print(f"ID {mid:2}: {price:12} | [{cat:12}] {title}")

