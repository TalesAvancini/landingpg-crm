#!/usr/bin/env python3
"""
🧠 learnings_aggregator.py (Memória Estratégica - Lobo Temporal)
Varre o SSD_ERRORS_LEDGER.md (Tático) e o HARNESS_LOG.md (Técnico)
para gerar o LEARNINGS.md (Estratégico).
"""
import sys
import re
from pathlib import Path
from datetime import datetime

# Configurações de Path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
CONTEXT_DIR = PROJECT_ROOT / ".context"
BRAIN_DIR = CONTEXT_DIR / "brain"
MAINTENANCE_DIR = CONTEXT_DIR / "maintenance"
SPECS_DIR = PROJECT_ROOT / ".specs" / "features"

LEDGER_FILE = SPECS_DIR / "SSD_ERRORS_LEDGER.md"
HARNESS_LOG_FILE = MAINTENANCE_DIR / "HARNESS_LOG.md"
LEARNINGS_FILE = BRAIN_DIR / "LEARNINGS.md"

# Output encoding
stdout_reconfigure = getattr(sys.stdout, "reconfigure", None)
if callable(stdout_reconfigure):
    stdout_reconfigure(encoding="utf-8", errors="replace")

def safe_parse_ledger():
    """Lê o Ledger focado no Formato B (Scars)."""
    scars = []
    if not LEDGER_FILE.exists():
        print(f"[WARN] Ledger não encontrado em {LEDGER_FILE}")
        return scars

    content = LEDGER_FILE.read_text(encoding="utf-8", errors="replace")
    
    # Regex para capturar ### Scar #NNN — Título
    # Seguido de campos da scar até a próxima scar ou EOF
    scar_blocks = re.split(r'(?m)^###\s*Scar\s*#\d+\s*[—\-]\s*', content)
    
    if len(scar_blocks) <= 1:
        # Tenta checar se há blocos, senao retorna vazio
        return scars
        
    for block in scar_blocks[1:]:
        lines = block.strip().split('\n')
        title = lines[0].strip()
        
        scar_data = {
            "title": title,
            "data": "",
            "feature": "",
            "erro": "",
            "sintoma": "",
            "causa_raiz": "",
            "correcao": "",
            "regra": ""
        }
        
        for line in lines[1:]:
            line = line.strip()
            if not line: continue
            if line == "---": break
            
            if line.startswith("- **Data:**"): scar_data["data"] = line.split(":**", 1)[1].strip()
            elif line.startswith("- **Feature:**"): scar_data["feature"] = line.split(":**", 1)[1].strip()
            elif line.startswith("- **Erro:**"): scar_data["erro"] = line.split(":**", 1)[1].strip()
            elif line.startswith("- **Sintoma observado:**"): scar_data["sintoma"] = line.split(":**", 1)[1].strip()
            elif line.startswith("- **Causa raiz:**"): scar_data["causa_raiz"] = line.split(":**", 1)[1].strip()
            elif line.startswith("- **Correcao aplicada:**"): scar_data["correcao"] = line.split(":**", 1)[1].strip()
            elif line.startswith("- **Regra adicionada/ajustada:**"): scar_data["regra"] = line.split(":**", 1)[1].strip()

        scars.append(scar_data)
        
    return scars

def calculate_score(scar):
    """Calcula a relevância da Scar. Base simples para V1."""
    score = 50 # Base
    # Penalidade por idade poderia entrar aqui
    return score

def generate_learnings_md(scars):
    """Gera o arquivo LEARNINGS.md estruturado."""
    
    # Ordena scars por score (aqui todas têm 50, mantemos a ordem de extração)
    scars = sorted(scars, key=lambda x: calculate_score(x), reverse=True)
    
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    md = f"""---
Criado em: 2026-05-04
Ultima Atualizacao: {now}
Status: Ativo
---

# 🧠 LEARNINGS.md (Memória Estratégica MiMo)

> "Aquele que não lembra o passado está condenado a repeti-lo."
> Gerado automaticamente por `learnings_aggregator.py`.

## 🚨 Top Cicatrizes Ativas (Scars)
*(Erros que custaram caro e NÃO devem ser repetidos)*

"""
    for i, scar in enumerate(scars[:10], 1):
        md += f"### [SCAR-{i:03d}] {scar['title']} (Score: {calculate_score(scar)})\n"
        md += f"- **Última vez:** {scar['feature']} ({scar['data']})\n"
        md += f"- **O que aconteceu:** {scar['erro']} -> {scar['causa_raiz']}\n"
        md += f"- **A Regra:** {scar['regra']}\n\n"
        
    md += "---\n\n## ⚠️ Propostas de Novas Regras\n*(Nenhuma regra nova consolidada neste ciclo)*\n"
    
    return md

def main():
    triage_mode = "--triage" in sys.argv
    
    print("🧠 [LEARNINGS] Iniciando agregação de memória (MiMo v2)...")
    
    scars = safe_parse_ledger()
    print(f"[INFO] {len(scars)} Scars lidas do Ledger.")
    
    if triage_mode:
        print("\n--- TRIAGE MODE ---")
        for scar in scars:
            print(f"Scar: {scar['title']} | Feature: {scar['feature']}")
        print("-------------------\n")
        sys.exit(0)
        
    content = generate_learnings_md(scars)
    
    LEARNINGS_FILE.parent.mkdir(parents=True, exist_ok=True)
    LEARNINGS_FILE.write_text(content, encoding="utf-8")
    
    print(f"✅ [SUCCESS] LEARNINGS.md atualizado com {len(scars)} memórias estratégicas.")

if __name__ == "__main__":
    main()
