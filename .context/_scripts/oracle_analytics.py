#!/usr/bin/env python3
"""
📊 oracle_analytics.py — Analisador de Telemetria do Oráculo (H.O.K v2.5.2)
Processa o wiki_log.md para gerar insights de confiança e identificar gaps no mercado.
"""
import re, sys, io
from pathlib import Path
from collections import Counter

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

CONTEXT_DIR = Path(__file__).resolve().parents[1]
LOG_FILE = CONTEXT_DIR / "market" / "wiki_log.md"

def parse_logs():
    if not LOG_FILE.exists():
        print("Nenhum log encontrado em wiki_log.md")
        return

    content = LOG_FILE.read_text(encoding="utf-8")
    lines = content.strip().split("\n")
    
    total_queries = 0
    total_conf = 0.0
    failed_queries = []
    
    # Exemplo: | [2026-04-29 23:29:55] | QUERY | Busca: QA (conf: 1.00) | market/WIKI/concepts/harness_behavior.md | OK |
    pattern = r'\|\s*\[(.*?)\]\s*\|\s*QUERY\s*\|\s*Busca:\s*(.*?)\s*\(conf:\s*([0-9.]+)\)\s*\|\s*(.*?)\s*\|\s*(FAIL|OK)\s*\|'
    
    for line in lines:
        match = re.search(pattern, line)
        if match:
            total_queries += 1
            timestamp, query, conf_str, source, status = match.groups()
            conf = float(conf_str)
            total_conf += conf
            
            if conf < 0.6 or status == "FAIL":
                failed_queries.append(query)

    print("========================================")
    print(" 📊 ORACLE ANALYTICS (TELEMETRIA v3)")
    print("========================================")
    print(f"Total de Consultas: {total_queries}")
    if total_queries > 0:
        print(f"Confiança Média:    {total_conf / total_queries:.2f}")
    
    print("\n⚠️ Gaps de Conhecimento (Confiança Baixa / Falhas):")
    if not failed_queries:
        print("Nenhum gap detectado! Oráculo está calibrado.")
    else:
        counter = Counter(failed_queries)
        for q, count in counter.most_common(5):
            print(f" - {q} ({count}x)")
    print("========================================")

if __name__ == "__main__":
    parse_logs()
