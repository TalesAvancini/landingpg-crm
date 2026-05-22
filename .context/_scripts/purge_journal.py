#!/usr/bin/env python3
"""
🗜️ purge_journal.py
Arquiva 70% das entradas mais antigas do JOURNAL.md.
Mantém 30% mais recentes como semente. Backup automático e escrita atômica.
"""
import re
import sys
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from _tz_utils import format_ts
except ImportError:
    format_ts = lambda dt=None, fmt="%Y-%m-%d %H:%M": (dt or datetime.now()).strftime(fmt)
    print("[WARN] _tz_utils inacessivel. Usando timezone local MS-WIN.")

SCRIPT_DIR = Path(__file__).parent
CONTEXT_DIR = SCRIPT_DIR.parent
JOURNAL_FILE = CONTEXT_DIR / "maintenance" / "JOURNAL.md"
ARCHIVE_DIR = CONTEXT_DIR / "maintenance" / "_archive_context" / "journals"
KEEP_RATIO = 0.3  # 30% mais recentes

def parse_entries(content):
    # Divide por headers markdown (## 📅, ##, etc.) mantendo o header na entrada
    parts = re.split(r'(?=^## )', content, flags=re.MULTILINE)
    return [p.strip() for p in parts if p.strip()]

def purge_journal():
    if not JOURNAL_FILE.exists():
        print("[WARN] JOURNAL.md nao encontrado. Nada a fazer.")
        return

    content = JOURNAL_FILE.read_text(encoding="utf-8")
    entries = parse_entries(content)

    if len(entries) <= 2:
        print("[INFO] Poucas entradas para purgar.")
        return

    header = entries[0]
    logs = entries[1:]

    keep_count = max(1, int(len(logs) * KEEP_RATIO))
    keep_entries = logs[:keep_count]
    archive_entries = logs[keep_count:]

    # Garante diretório de arquivo
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)

    # Backup com timestamp
    timestamp = format_ts(fmt="%Y%m%d_%H%M%S")
    archive_file = ARCHIVE_DIR / f"journal_archive_{timestamp}.md"
    archive_content = f"# Arquivo de Journal - {timestamp}\n\n" + "\n\n".join(archive_entries) + "\n"
    archive_file.write_text(archive_content, encoding="utf-8")

    # Nova semente
    now = format_ts()
    seed = f"""---
Criado em: {now}
Ultima Atualizacao: {now}
Status: Ativo
Nota: Semente pos-purge. {len(archive_entries)} entradas arquivadas em {archive_file.name}.
---

# JOURNAL.md (Memoria Curta)
> Mantido por purge_journal.py. Limite heuristico de caracteres atingido.

""" + "\n\n".join(keep_entries) + "\n"

    # Escrita atomica (previne corrupcao se interrupcao ocorrer)
    temp_file = JOURNAL_FILE.with_suffix(".tmp")
    temp_file.write_text(seed, encoding="utf-8")
    temp_file.replace(JOURNAL_FILE)

    print(f"[OK] Purge concluido.")
    print(f"[OK] Arquivadas: {len(archive_entries)} entradas -> {archive_file.name}")
    print(f"[OK] Mantidas: {len(keep_entries)} entradas mais recentes.")

if __name__ == "__main__":
    try:
        purge_journal()
    except Exception as e:
        print(f"[ERROR] Erro no purge: {e}")
