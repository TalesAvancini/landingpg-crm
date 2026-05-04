#!/usr/bin/env python3
"""
💉 inject_learnings.py (Injetor de Memória)
Lê o LEARNINGS.md gerado pelo Aggregator e cria o `.enriched.md` 
nas features ativas para garantir que o Agente tenha contexto estratégico (Fase A - Skill 1).
"""
import sys
from pathlib import Path
import re

# Configurações de Path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
CONTEXT_DIR = PROJECT_ROOT / ".context"
BRAIN_DIR = CONTEXT_DIR / "brain"
SPECS_DIR = PROJECT_ROOT / ".specs" / "features"

LEARNINGS_FILE = BRAIN_DIR / "LEARNINGS.md"

# Output encoding
stdout_reconfigure = getattr(sys.stdout, "reconfigure", None)
if callable(stdout_reconfigure):
    stdout_reconfigure(encoding="utf-8", errors="replace")

def get_active_features():
    """Retorna uma lista de diretórios de features que possuem spec.md."""
    if not SPECS_DIR.exists():
        return []
    
    features = []
    for d in SPECS_DIR.iterdir():
        if d.is_dir() and not d.name.startswith("_"):
            spec_file = d / "spec.md"
            if spec_file.exists():
                features.append(d)
    return features

def extract_top_scars():
    """Lê o LEARNINGS.md e extrai o bloco de Top Scars."""
    if not LEARNINGS_FILE.exists():
        return "Nenhuma memória estratégica (LEARNINGS.md) encontrada."
        
    content = LEARNINGS_FILE.read_text(encoding="utf-8", errors="replace")
    
    # Busca a seção de Scars
    # Pega tudo entre '## 🚨 Top Cicatrizes Ativas (Scars)' e '---' ou fim do arquivo
    match = re.search(r'## 🚨 Top Cicatrizes Ativas.*?(\n.*?)(\n---|## ⚠️|$)', content, re.DOTALL)
    if match:
        scars_content = match.group(1).strip()
        if scars_content:
            return scars_content
            
    return "Nenhuma Scar ativa no momento."

def inject_to_feature(feature_dir, scars_content):
    """Gera/Atualiza o .enriched.md na feature."""
    spec_file = feature_dir / "spec.md"
    enriched_file = feature_dir / ".enriched.md"
    
    # Lê a spec original (para V2 poderíamos cruzar keywords aqui)
    spec_content = spec_file.read_text(encoding="utf-8", errors="replace")
    
    enriched_md = f"""# 💉 Spec Enriquecida (MiMo)
> Este arquivo injeta memória estratégica na Spec original. O Agente deve usar ESTE arquivo como guia.

## 🚨 MEMÓRIA ESTRATÉGICA (NÃO REPITA ESTES ERROS)
{scars_content}

---
## 📄 SPEC ORIGINAL
{spec_content}
"""
    
    enriched_file.write_text(enriched_md, encoding="utf-8")
    return enriched_file

def main():
    print("💉 [INJECTOR] Iniciando injeção de contexto (MiMo v2)...")
    
    features = get_active_features()
    if not features:
        print("[WARN] Nenhuma feature ativa encontrada.")
        sys.exit(0)
        
    scars_content = extract_top_scars()
    
    for feature in features:
        enriched_path = inject_to_feature(feature, scars_content)
        print(f"[OK] Injetado em: {feature.name}/.enriched.md")
        
    print(f"✅ [SUCCESS] Contexto estratégico injetado em {len(features)} features.")

if __name__ == "__main__":
    main()
