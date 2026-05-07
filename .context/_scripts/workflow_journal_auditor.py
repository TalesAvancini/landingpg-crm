#!/usr/bin/env python3
"""
🛡️ workflow_journal_auditor.py — Sistema Anti-Migué (SAM)
Audita a coerência entre Promessa (Journal), Obrigação (Synapse) e Realidade (Git).
"""

import os, re, sys, json, subprocess
from pathlib import Path

# Configuração de encoding para Windows
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

CONTEXT_DIR = Path(__file__).resolve().parents[1]
JOURNAL_PATH = CONTEXT_DIR / "maintenance" / "JOURNAL.md"
SYNAPSE_PATH = CONTEXT_DIR / "maintenance" / "JOURNAL_SYNAPSE.md"

def get_git_state():
    """Retorna dicionário com arquivos modificados e novos."""
    # Pastas ignoradas para auditoria SAM (Zona Segura de Rascunho)
    IGNORED_PREFIXES = ("planos/", "scratch/", "temp/", ".agents/")
    
    try:
        res = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True, check=True)
        lines = res.stdout.splitlines()
        
        modified = set()
        new_files = set()
        
        for line in lines:
            status = line[:2]
            path = line[3:].strip()
            
            # Skip arquivos em pastas de rascunho
            if path.startswith(IGNORED_PREFIXES):
                continue
                
            if "??" in status or "A" in status:
                new_files.add(path)
            else:
                modified.add(path)
        
        return {"modified": modified, "new": new_files, "all": modified.union(new_files)}
    except Exception as e:
        print(f"[ERROR] Falha ao ler Git: {e}")
        return {"modified": set(), "new": set(), "all": set()}

def get_synapse_rules():
    """Extrai JSON do JOURNAL_SYNAPSE.md."""
    if not SYNAPSE_PATH.exists():
        return {"rules": []}
    content = SYNAPSE_PATH.read_text(encoding="utf-8")
    match = re.search(r"<!-- SYNAPSE_JSON_START -->\s*(.*?)\s*<!-- SYNAPSE_JSON_END -->", content, re.DOTALL)
    if not match:
        print("[WARN] Bloco JSON não encontrado no Synapse. Usando regras vazias.")
        return {"rules": []}
    try:
        return json.loads(match.group(1))
    except Exception as e:
        print(f"[ERROR] Falha ao parsear JSON do Synapse: {e}")
        return {"rules": []}

def get_latest_journal_entry():
    """Extrai a última entrada (seção ## 📅) do JOURNAL.md."""
    if not JOURNAL_PATH.exists():
        return ""
    content = JOURNAL_PATH.read_text(encoding="utf-8")
    # Usa um separador que garanta o início da linha para evitar sub-seções
    entries = re.split(r"(?m)^## 📅", content)
    valid_entries = [e for e in entries if e.strip()]
    # Em Ordem Cronológica Reversa, a entrada mais recente é a primeira após o cabeçalho (índice 1)
    return "## 📅" + valid_entries[1] if len(valid_entries) > 1 else ""

def audit():
    print("🤖 Iniciando Auditoria Anti-Migué (SAM)...")
    
    git = get_git_state()
    synapse = get_synapse_rules()
    mode = synapse.get("mode", "assist")
    entry = get_latest_journal_entry()
    
    if not entry:
        print("[FAIL] Nenhuma entrada recente encontrada no JOURNAL.md.")
        return 1

    violations = []

    for rule in synapse.get("rules", []):
        rule_id = rule.get("id")
        triggered = False
        
        for pattern in rule.get("when_any_changed", []):
            if any(re.search(re.escape(pattern), f) for f in git["all"]):
                triggered = True
                break
        
        if not triggered:
            for pattern in rule.get("when_new_path_under", []):
                if any(f.startswith(pattern) for f in git["new"]):
                    triggered = True
                    break

        if triggered:
            print(f"[INFO] Regra '{rule_id}' disparada.")
            for tag in rule.get("require_journal_tags", []):
                if tag.lower() not in entry.lower():
                    violations.append(f"Regra '{rule_id}': Tag '{tag}' ausente no Journal.")
            
            for req_file in rule.get("require_files_touched", []):
                if not any(f.endswith(req_file) for f in git["all"]):
                    violations.append(f"Regra '{rule_id}': Arquivo '{req_file}' não foi propagado (ausente no diff).")
                
                checkbox_pattern = rf"-\s*\[x\]\s*`?{re.escape(req_file)}`?"
                if not re.search(checkbox_pattern, entry, re.I):
                    violations.append(f"Regra '{rule_id}': Checkbox [x] para '{req_file}' ausente ou desmarcado no Journal.")

    # Validação de Segregação de Contexto (REGEX ROBUSTO)
    if mode == "strict" or "### Contrato de Validacao" in entry:
        # Regex captura o conteúdo dentro de backticks ou texto puro, ignorando espaços
        e_id_match = re.search(r"executor_context_id:\s*`?([\w\-_]+)`?", entry, re.I)
        v_id_match = re.search(r"validator_context_id:\s*`?([\w\-_]+)`?", entry, re.I)
        # Status busca por emojis ou texto READY TO COMMIT
        status_match = re.search(r"status:\s*`?(.*?)`?\n", entry, re.I)
        
        e_id = e_id_match.group(1).strip() if e_id_match else ""
        v_id = v_id_match.group(1).strip() if v_id_match else ""
        status = status_match.group(1).strip() if status_match else ""

        if not e_id or not v_id or v_id == "[PENDENTE]":
            violations.append(f"Contrato incompleto. Detectado: executor='{e_id}', validator='{v_id}'.")
        elif e_id == v_id:
            violations.append(f"Violação de Segregação: executor_context_id == validator_context_id ('{e_id}').")
        
        if not any(x in status for x in ["READY TO COMMIT", "🟢"]):
            violations.append(f"Status de validação inválido: '{status}'. Esperado 'READY TO COMMIT'.")

    # --- Detecção de Fraude Narrativa & Modificação Silenciosa (Sprint 07) ---
    # Extrai arquivos marcados como propagados no Journal: - [x] `path`
    journal_propagated = set()
    propagation_matches = re.findall(r"-\s*\[x\]\s*`?(.*?)`?\s*->", entry, re.I)
    for p in propagation_matches:
        journal_propagated.add(p.strip())

    # 1. Fraude Narrativa: Alegar que mudou algo que o Git não viu.
    for p_file in journal_propagated:
        # Se o arquivo não está no Git e não é um diretório/padrão genérico
        if not any(f.endswith(p_file) or p_file in f for f in git["all"]):
            violations.append(f"Fraude Narrativa: Arquivo '{p_file}' marcado como [x] no Journal, mas não há alterações no Git.")

    # 2. Modificação Silenciosa: Mudar algo no Git e não avisar no Journal.
    # Ignora arquivos de contexto que são atualizados automaticamente e diretórios de sistema
    ignore_silent = [".context/maintenance/JOURNAL.md", ".context/maintenance/HARNESS_LOG.md", ".context/maintenance/STATE.md"]
    for g_file in git["all"]:
        if any(g_file.endswith(ex) for ex in ignore_silent):
            continue
        
        # Se o arquivo Git não foi mencionado no Journal como [x]
        if not any(g_file.endswith(p) or p in g_file for p in journal_propagated):
            # Verifica se está em alguma regra de obrigatoriedade (require_files_touched) para evitar erro duplo
            # Mas aqui o foco é: se mudou, tem que estar na Matriz de Propagação.
            violations.append(f"Modificação Silenciosa: Arquivo '{g_file}' alterado no Git mas ausente na Matriz de Propagação do Journal.")

    if violations:
        print("\n❌ VIOLAÇÕES DETECTADAS:")
        for v in violations:
            print(f"  - {v}")
        
        if mode == "strict":
            print("\n[FATAL] Modo STRICT: Pipeline bloqueado.")
            return 1
        else:
            print("\n[WARN] Modo ASSIST: Pipeline prosseguindo com avisos.")
            return 0
    else:
        print("\n✅ AUDITORIA PASSOU: Reality Check coerente com a Promessa.")
        return 0

if __name__ == "__main__":
    sys.exit(audit())
