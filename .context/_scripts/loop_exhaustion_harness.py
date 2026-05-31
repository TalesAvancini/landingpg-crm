#!/usr/bin/env python3
"""
🛡️ loop_exhaustion_harness.py — Harness de Exaustão de Loop de IA
Evita que agentes de IA entrem em loops cegos de tentativa e erro sem alterar código.
"""
import os
import sys
import json
import hashlib
import subprocess
from pathlib import Path

# Configuração de encoding para Windows
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parents[2]
SCRATCH_DIR = BASE_DIR / "scratch"
STATE_FILE = SCRATCH_DIR / "loop_state.json"

def get_git_diff_hash():
    """Retorna um hash SHA256 do diff atual do Git."""
    try:
        res = subprocess.run(["git", "diff", "HEAD"], capture_output=True, text=True, check=True, cwd=str(BASE_DIR))
        diff_text = res.stdout
        return hashlib.sha256(diff_text.encode("utf-8")).hexdigest()
    except Exception:
        return "no-git-diff"

def load_state():
    if not SCRATCH_DIR.exists():
        SCRATCH_DIR.mkdir(parents=True, exist_ok=True)
    if not STATE_FILE.exists():
        return {}
    try:
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    except Exception:
        return {}

def save_state(state):
    try:
        STATE_FILE.write_text(json.dumps(state, indent=2), encoding="utf-8")
    except Exception as e:
        print(f"[WARN] Falha ao salvar estado do loop: {e}")

def main():
    status = "fail"
    test_name = "global"
    
    args = sys.argv[1:]
    for i in range(len(args)):
        if args[i] == "--status" and i + 1 < len(args):
            status = args[i+1]
        elif args[i] == "--test" and i + 1 < len(args):
            test_name = args[i+1]
            
    state = load_state()
    current_diff_hash = get_git_diff_hash()
    
    test_state = state.setdefault(test_name, {
        "fail_count": 0,
        "last_git_diff_hash": ""
    })
    
    if status == "pass":
        test_state["fail_count"] = 0
        test_state["last_git_diff_hash"] = current_diff_hash
        save_state(state)
        print(f"✅ Loop Exhaustion: Teste '{test_name}' passou. Contador resetado.")
        return 0
        
    last_hash = test_state.get("last_git_diff_hash", "")
    
    if current_diff_hash != last_hash:
        test_state["fail_count"] = 1
        test_state["last_git_diff_hash"] = current_diff_hash
        save_state(state)
        print(f"ℹ️ Loop Exhaustion: Mudança física de código detectada. Contador de falhas reiniciado para 1.")
        return 0
    else:
        test_state["fail_count"] += 1
        save_state(state)
        fail_count = test_state["fail_count"]
        print(f"⚠️ Loop Exhaustion: Falha {fail_count}/5 consecutiva no teste '{test_name}' sem alterações no Git.")
        
        if fail_count >= 5:
            print("\n❌ [FATAL] EXAUSTÃO DE LOOP DE EXECUÇÃO DE IA!")
            print("Você falhou 5 vezes consecutivas no mesmo teste sem alterar fisicamente o código.")
            print("Isso indica Teimosia de Loop. O pipeline está bloqueado fisicamente.")
            print("👉 AÇÃO REQUERIDA: Aplique o Protocolo Bandeira Branca. Chame o Humano ou altere o código do teste/produção para quebrar o loop.")
            return 1
            
        return 0

if __name__ == "__main__":
    sys.exit(main())
