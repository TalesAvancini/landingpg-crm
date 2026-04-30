#!/usr/bin/env python3
"""
🧹 cleanup_specs.py
Gerencia a efemeridade da bancada de trabalho (.specs/).
Aplica a regra de 48h de inatividade e limite de 3 specs ativas simultâneas.
Arquiva specs excedentes ou obsoletas em _archive_context/specs/.
"""
import os
import shutil
import time
from pathlib import Path
from datetime import datetime

# Caminhos base
SCRIPT_DIR = Path(__file__).parent
CONTEXT_DIR = SCRIPT_DIR.parent
SPECS_DIR = CONTEXT_DIR.parent / ".specs" / "features"
ARCHIVE_DIR = CONTEXT_DIR / "maintenance" / "_archive_context" / "specs"

# Configurações
MAX_INACTIVITY_SECONDS = 48 * 3600  # 48 horas
MAX_ACTIVE_SPECS = 3

def get_specs():
    if not SPECS_DIR.exists():
        return []
    return [d for d in SPECS_DIR.iterdir() if d.is_dir() and not d.name.startswith("_")]

def archive_spec(spec_path):
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_name = f"{spec_path.name}_{timestamp}"
    dest_path = ARCHIVE_DIR / archive_name
    
    print(f"[INFO] Arquivando spec: {spec_path.name} -> {archive_name}")
    shutil.move(str(spec_path), str(dest_path))

def cleanup():
    specs = get_specs()
    if not specs:
        print("[OK] Nenhuma spec ativa encontrada.")
        return

    now = time.time()
    active_specs = []

    # 1. Limpeza por inatividade (48h)
    for spec in specs:
        last_mod = max(os.path.getmtime(root) for root, _, _ in os.walk(spec))
        if (now - last_mod) > MAX_INACTIVITY_SECONDS:
            print(f"[AUTO] Inatividade detectada (>48h) em: {spec.name}")
            archive_spec(spec)
        else:
            active_specs.append(spec)

    # 2. Limpeza por limite de volume (Max 3)
    # Ordena por data de modificação (mais antiga primeiro)
    active_specs.sort(key=lambda s: max(os.path.getmtime(root) for root, _, _ in os.walk(s)))
    
    while len(active_specs) > MAX_ACTIVE_SPECS:
        oldest = active_specs.pop(0)
        print(f"[AUTO] Limite de volume excedido (Max {MAX_ACTIVE_SPECS}). Removendo spec mais antiga: {oldest.name}")
        archive_spec(oldest)

    print(f"[OK] Manutencao de specs concluida. Specs ativas: {len(active_specs)}/{MAX_ACTIVE_SPECS}")

if __name__ == "__main__":
    try:
        cleanup()
    except Exception as e:
        print(f"[ERROR] Falha na limpeza de specs: {e}")
