import re
from pathlib import Path

journal_path = Path("c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inicío_de_projeto/.context/maintenance/JOURNAL.md")
content = journal_path.read_text(encoding="utf-8", errors="ignore")

# Testando o regex
pattern = r"##\s+(?:📅\s+)?\[?(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2})\]?"
date_patterns = re.findall(pattern, content)

print(f"Datas encontradas: {len(date_patterns)}")
for d in date_patterns:
    print(f" - {d}")

warnings = []
for i in range(1, len(date_patterns)):
    prev = date_patterns[i-1]
    curr = date_patterns[i]
    if curr < prev:
        warnings.append(f"Inversão: {curr} após {prev}")

if warnings:
    print("\nAVISOS:")
    for w in warnings:
        print(f" [!] {w}")
else:
    print("\nNenhuma inversão detectada.")
