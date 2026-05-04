#!/usr/bin/env python3
"""
✅ validate_commit_msg.py
Validador cross-platform de Conventional Commits.
Padrão: tipo(escopo): descrição
"""
import sys
import re
from pathlib import Path

# Configuração de encoding para Windows
stdout_reconfigure = getattr(sys.stdout, "reconfigure", None)
if callable(stdout_reconfigure):
    stdout_reconfigure(encoding="utf-8", errors="replace")

def validate(msg):
    # Tipo: feat|fix|docs|style|refactor|test|chore|build|ci|perf|revert
    # Escopo opcional entre parênteses
    # Dois pontos e espaço obrigatórios
    pattern = r'^(feat|fix|docs|style|refactor|test|chore|build|ci|perf|revert)(\([\w\-\.]+\))?:\s+.+'
    return re.match(pattern, msg)

def main():
    if len(sys.argv) < 2:
        print("[ERROR] Arquivo de mensagem de commit nao fornecido.")
        sys.exit(1)
        
    msg_file = Path(sys.argv[1])
    if not msg_file.exists():
        # Husky às vezes passa o caminho relativo ou absoluto dependendo da configuração
        print(f"[ERROR] Arquivo de commit nao encontrado: {msg_file}")
        sys.exit(1)
        
    try:
        with open(msg_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
            if not lines:
                print("[FAIL] Mensagem de commit vazia!")
                sys.exit(1)
            
            first_line = lines[0].strip()
            
            # Ignora comentários do git (linhas começando com #)
            if first_line.startswith("#"):
                print("[SKIP] Linha de comentario detectada.")
                sys.exit(0)

            if validate(first_line):
                print(f"[OK] Mensagem de commit valida: {first_line}")
                sys.exit(0)
            else:
                print("\n❌ [FAIL] Mensagem de commit fora do padrão Conventional Commits!")
                print("   Padrão: tipo(escopo): descricao")
                print("   Exemplo: feat(auth): adiciona login social")
                print("   Tipos: feat, fix, docs, style, refactor, test, chore, build, ci, perf, revert")
                print(f"   Recebido: \"{first_line}\"\n")
                sys.exit(1)
    except Exception as e:
        print(f"[ERROR] Falha tecnica na validação: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
