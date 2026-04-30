#!/usr/bin/env python3
"""
🛠️ _wiki_log_utils.py — Utilitário de Rastreabilidade Wiki (H.O.K v2.5.1)
Centraliza a escrita robusta e sincronizada no wiki_log.md.
"""
import os
import sys
import time
from datetime import datetime
from pathlib import Path

CONTEXT_DIR = Path(__file__).resolve().parents[1]
LOG_FILE = CONTEXT_DIR / "market/wiki_log.md"
LOCK_FILE = CONTEXT_DIR / "_scripts/_wiki_log.lock"

def append_to_wiki_log(mode, description, files, status):
    """
    Adiciona uma entrada ao log da Wiki de forma robusta e sincronizada.
    mode: INGEST | LINT | QUERY | SKIP
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # Escape de pipes para não quebrar a tabela Markdown
    safe_desc = str(description).replace("|", "\\|")
    safe_files = str(files).replace("|", "\\|")
    
    line = f"| [{timestamp}] | {mode} | {safe_desc} | {safe_files} | {status} |\n"
    
    # Sincronização Simples (Spin Lock) para evitar concorrência
    timeout = 0.5 # Fire-and-forget: Timeout agressivo para não bloquear o usuário
    start_time = time.time()
    
    while True:
        try:
            # Tenta criar o arquivo de lock de forma exclusiva
            fd = os.open(LOCK_FILE, os.O_CREAT | os.O_EXCL | os.O_RDWR)
            try:
                # Se não existir o log, cria com cabeçalhos
                if not LOG_FILE.exists():
                    headers = [
                        "# Wiki Log (Append-only)\n\n",
                        "| Timestamp | Mode | Description | Files | Status |\n",
                        "|-----------|------|-------------|-------|--------|\n"
                    ]
                    LOG_FILE.write_text("".join(headers), encoding="utf-8")
                
                with open(LOG_FILE, "a", encoding="utf-8") as f:
                    f.write(line)
                break # Sucesso
            finally:
                os.close(fd)
                os.remove(LOCK_FILE)
        except FileExistsError:
            if time.time() - start_time > timeout:
                print(f"[WARN] Timeout ao aguardar lock do wiki_log.md", file=sys.stderr)
                break
            time.sleep(0.1)
        except Exception as e:
            print(f"[WARN] Falha ao gravar no wiki_log.md: {e}", file=sys.stderr)
            break

if __name__ == "__main__":
    # Teste rápido se chamado diretamente
    test_mode = sys.argv[1] if len(sys.argv) > 1 else "TEST"
    append_to_wiki_log(test_mode, "Teste de utilitário", "test.py", "OK")
    print(f"[OK] Entrada de teste '{test_mode}' gravada.")
