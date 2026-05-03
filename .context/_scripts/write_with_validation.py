#!/usr/bin/env python3
"""
write_with_validation.py — Gate de escrita cirurgica (Chain-Skills V3)
Valida task_id, scope, tier e strategy antes de permitir escrita.
Exit 0 = WRITE_AUTHORIZED | Exit 1 = BLOCKED
"""
import re, sys, os
from pathlib import Path

# Setup dos caminhos absolutos
CONTEXT_DIR = Path(__file__).resolve().parents[1]
SPECS_DIR = CONTEXT_DIR.parent / ".specs" / "features"

TIER_1_LIMIT = 15
TIER_2_LIMIT = 50

def validate_write(feature_id, task_id, file_path, line_count):
    """Retorna (ok: bool, reason: str)"""
    try:
        line_count = int(line_count)
    except ValueError:
        return False, f"line_count deve ser inteiro. Recebido: {line_count}"
        
    # ── 1. Task existe no tasks.md? ──
    tasks_file = SPECS_DIR / feature_id / "tasks.md"
    if not tasks_file.exists():
        return False, f"tasks.md nao encontrado para feature '{feature_id}'"
        
    with open(tasks_file, "r", encoding="utf-8") as f:
        tasks_content = f.read()
        
    if task_id not in tasks_content:
        return False, f"Task '{task_id}' nao encontrada em {tasks_file.name}"
        
    # ── 2. Task esta fechada? ──
    # Regex flexivel que procura por "- [x] **TASK_ID**"
    closed_pattern = rf"- \[x\] \*\*{task_id}\*\*"
    if re.search(closed_pattern, tasks_content):
        return False, f"Task '{task_id}' ja esta concluida ([x]). Escrita negada."
        
    # ── 3. Consultar STATE.md (Escopo e Estrategia) ──
    state_file = SPECS_DIR / feature_id / "STATE.md"
    if not state_file.exists():
        return False, f"STATE.md nao encontrado. Execute as skills anteriores primeiro."
        
    with open(state_file, "r", encoding="utf-8") as f:
        state_content = f.read()
        
    # ── 4. Escopo Lockado? ──
    if "## CHAIN_SPEC_DIGEST" not in state_content:
        return False, "CHAIN_SPEC_DIGEST nao encontrado. Escopo nao foi bloqueado."
        
    # ── 5. Arquivo na Whitelist? ──
    # Extrair lista de ALLOW
    allow_section = re.search(r"allow_list:\s*((?:-\s+.*?\n)+)", state_content)
    if not allow_section:
        return False, "allow_list nao definida no STATE.md"
        
    allowed_files = [line.strip().lstrip("- ") for line in allow_section.group(1).split("\n") if line.strip()]
    
    file_normalized = str(Path(file_path).as_posix())
    if file_normalized not in [str(Path(p).as_posix()) for p in allowed_files]:
        hint = ""
        if any(x in file_normalized for x in [".context/maintenance", "STATE.md", "tasks.md"]):
            hint = " | HINT: Arquivos de governança/logs DEVEM estar explicitamente na allow_list da spec V3."
        return False, f"Arquivo '{file_path}' FORA DO ESCOPO. Nao esta na allow_list.{hint}"
        
    # ── 6. Estrategia existe? ──
    if "## CHAIN_STRATEGY_LOG" not in state_content:
        return False, "CHAIN_STRATEGY_LOG ausente. Falta planejamento."
        
    if task_id not in state_content[state_content.find("## CHAIN_STRATEGY_LOG"):]:
        return False, f"Nenhuma estrategia definida para {task_id} no STRATEGY_LOG."
        
    # ── 7. Checar Limite de Linhas (Tiers) ──
    if line_count > TIER_2_LIMIT:
        # Tier 3 (50+): Permitido se o arquivo nao existir (arquivo novo)
        abs_file_path = CONTEXT_DIR.parent / file_path
        if abs_file_path.exists():
            return False, (
                f"Tier 3 violado ({line_count} linhas). Escritas > {TIER_2_LIMIT} linhas "
                f"so sao permitidas para arquivos NOVOS. O arquivo '{file_path}' ja existe."
            )
            
    if line_count > TIER_1_LIMIT:
        # Tier 2 (16-50): Verificar se ha justificativa no log de execucao do STATE.md
        exec_log_pos = state_content.find("## CHAIN_EXECUTION_LOG")
        if exec_log_pos == -1:
            return False, (
                f"Tier 2 ({line_count} linhas) requer justificativa no EXECUTION_LOG ANTES da escrita. "
                "Crie o CHAIN_EXECUTION_LOG no STATE.md e registre a justificativa."
            )
            
        exec_log_content = state_content[exec_log_pos:]
        justification_pattern = rf"### {task_id}.*?tier_justification:"
        if not re.search(justification_pattern, exec_log_content, re.DOTALL):
            return False, (
                f"Tier 2 ({line_count} linhas) requer justificativa no EXECUTION_LOG ANTES da escrita. "
                f"Registre 'tier_justification:' para {task_id} no log."
            )
            
    # ── 8. Tudo certo ──
    tier = '1' if line_count <= TIER_1_LIMIT else '2' if line_count <= TIER_2_LIMIT else '3'
    return True, f"WRITE_AUTHORIZED | task={task_id} | file={file_path} | lines={line_count} | tier={tier}"

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Uso: python write_with_validation.py <feature_id> <task_id> <file_path> <line_count>")
        print("Exemplo: python write_with_validation.py contract_sprints_v2_safe TASK-04 .context/_scripts/harness_runner.py 12")
        sys.exit(1)
        
    feature_id = sys.argv[1]
    task_id = sys.argv[2]
    file_path = sys.argv[3]
    line_count = sys.argv[4]
    
    ok, reason = validate_write(feature_id, task_id, file_path, line_count)
    
    if ok:
        print(f"[OK] {reason}")
        sys.exit(0)
    else:
        print(f"[BLOCKED] {reason}")
        print("\n🚨 GATILHO ANTI-LOOP ATIVADO:")
        print("Voce esta PROIBIDO de tentar a mesma acao cegamente.")
        print("Abra o AGENT_SCRATCHPAD.md da sua feature agora mesmo.")
        print("Se a solucao nao for obvia (Known Traps), preencha a secao INBOX e declare [HANDOFF: ESCALATION].")
        sys.exit(1)
