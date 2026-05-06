#!/usr/bin/env python3
"""
🔍 validate_context.py
Verifica saude do .context, estima consumo de tokens e valida conformidade.
Retorna exit 1 se houver qualquer alerta ou erro.
"""

import os
import sys
import re
import subprocess
from datetime import datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
CONTEXT_DIR = SCRIPT_DIR.parent

# Forçar UTF-8 em Windows
if sys.platform == "win32":
    import io

    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

REQUIRED_FILES = [
    "brain/RULES.md",
    "brain/MASTER_FLOW.md",
    "brain/AGENT_REGISTRY.md",
    "brain/PRD.md",
    "maintenance/JOURNAL.md",
    "maintenance/schema.sql",
    "maintenance/TECHNICAL_REQUIREMENTS.md",
]

OPTIONAL_FILES = ["brain/INCEPTION.md"]


JOURNAL_MAX_LINES = 600
TOKEN_WARN_THRESHOLD_CHARS = 400_000


def check_files():
    return [f for f in REQUIRED_FILES if not (CONTEXT_DIR / f).exists()]


def check_journal_lines():
    journal = CONTEXT_DIR / "maintenance/JOURNAL.md"
    if not journal.exists():
        return 0, True
    lines = journal.read_text(encoding="utf-8").splitlines()
    return len(lines), len(lines) <= JOURNAL_MAX_LINES


def estimate_tokens():
    total_chars = 0
    for f in REQUIRED_FILES:
        path = CONTEXT_DIR / f
        if path.exists():
            total_chars += len(path.read_text(encoding="utf-8", errors="ignore"))
    tokens_raw = total_chars // 4
    return total_chars, tokens_raw, total_chars < TOKEN_WARN_THRESHOLD_CHARS


def check_registry_structure():
    registry = CONTEXT_DIR / "brain/AGENT_REGISTRY.md"
    if not registry.exists():
        return False, "Arquivo ausente"
    content = registry.read_text(encoding="utf-8")
    if "| Role | " not in content and "| Role " not in content:
        return False, "Tabela de roles nao encontrada"
    return True, "OK"


def check_specs_structure():
    specs_dir = CONTEXT_DIR.parent / ".specs"
    if not specs_dir.exists():
        return True, "Workshop inativo (OK)"
    features_dir = specs_dir / "features"
    if not features_dir.exists():
        return False, "Diretorio features ausente no .specs"
    active_specs = [
        d for d in features_dir.iterdir() if d.is_dir() and not d.name.startswith("_")
    ]
    for spec in active_specs:
        if not (spec / "STATE.md").exists():
            return False, f"Falha de integridade: {spec.name}/STATE.md ausente"
    return True, f"OK ({len(active_specs)} specs ativas)"


def _normalize_sprint_label(sprint_key: str):
    m = re.search(r"(\d+)$", sprint_key)
    if not m:
        return sprint_key
    return f"Sprint {int(m.group(1)):02d}"


def check_sprint_acceptance_sync():
    """Falha se tasks da sprint atual estao concluídas, mas acceptance da sprint segue pendente."""
    specs_dir = CONTEXT_DIR.parent / ".specs" / "features"
    if not specs_dir.exists():
        return True, "Sem specs ativas"

    issues = []
    for spec_dir in [d for d in specs_dir.iterdir() if d.is_dir() and not d.name.startswith("_")]:
        spec_path = spec_dir / "spec.md"
        tasks_path = spec_dir / "tasks.md"
        if not spec_path.exists() or not tasks_path.exists():
            continue

        spec_text = spec_path.read_text(encoding="utf-8", errors="ignore")
        if "contract_mode: sprint_based" not in spec_text:
            continue

        curr_match = re.search(r"current_sprint:\s*(sprint_\d+)", spec_text, re.I)
        if not curr_match:
            continue
        curr = curr_match.group(1).lower()

        sprint_block = re.search(rf"{curr}:(.*?)(?=\n\s*sprint_\d+:|\Z)", spec_text, re.I | re.DOTALL)
        if not sprint_block:
            continue

        acceptance_pending = "[ ]" in sprint_block.group(1)
        sprint_label = _normalize_sprint_label(curr)
        tasks_text = tasks_path.read_text(encoding="utf-8", errors="ignore")
        section = re.search(rf"##\s+.*{re.escape(sprint_label)}.*?(?=\n##\s+|\Z)", tasks_text, re.I | re.DOTALL)
        if not section:
            continue

        unchecked_tasks = re.search(r"^-\s*\[\s\]", section.group(0), re.M)
        tasks_completed = unchecked_tasks is None

        if tasks_completed and acceptance_pending:
            issues.append(f"{spec_dir.name}: tasks de {curr} concluídas, mas acceptance no spec permanece pendente")

    if issues:
        return False, " | ".join(issues)
    return True, "OK"


def log_friction(event_code, detail):
    """Registra fricção de governança no HARNESS_LOG.md se a flag estiver ativa."""
    if os.environ.get("CONTEXT_WRITE_ADVISORY_LOG") != "1":
        return
        
    log_path = CONTEXT_DIR / "maintenance/HARNESS_LOG.md"
    if not log_path.exists():
        return
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = f"\n## [GOVERNANCE-FRICTION] {event_code} | {timestamp}\n- **Detalhe:** {detail}\n"
    
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(entry)


def check_journal_chronology():
    """Modo Advisory: Avisa se as datas no JOURNAL.md não estão em Ordem Reversa (Novo no Topo)."""
    journal = CONTEXT_DIR / "maintenance/JOURNAL.md"
    if not journal.exists():
        return True, "Sem Journal"

    content = journal.read_text(encoding="utf-8", errors="ignore")
    # Captura datas nos formatos ## 📅 YYYY-MM-DD HH:MM ou ## [YYYY-MM-DD HH:MM]
    date_patterns = re.findall(r"##\s+(?:📅\s+)?\[?(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2})\]?", content)
    
    if len(date_patterns) < 2:
        return True, "OK (Registros insuficientes para check)"

    warnings = []
    for i in range(1, len(date_patterns)):
        prev = date_patterns[i-1]
        curr = date_patterns[i]
        # Em ordem reversa, curr (item de baixo) deve ser <= prev (item de cima)
        if curr > prev:
            msg = f"Inversão detectada (Ordem Reversa): {curr} aparece abaixo de {prev}"
            warnings.append(msg)
            log_friction("GF-JOURNAL-ORDER", msg)

    if warnings:
        return False, " | ".join(warnings)
    return True, "OK"


def check_state_freshness():
    """Modo Advisory: Avisa se o campo 'updated' no STATE.md está defasado (datetime completo)."""
    specs_dir = CONTEXT_DIR.parent / ".specs" / "features"
    if not specs_dir.exists():
        return True, "Sem specs"

    warnings = []
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    for spec_dir in [d for d in specs_dir.iterdir() if d.is_dir() and not d.name.startswith("_")]:
        state_path = spec_dir / "STATE.md"
        if not state_path.exists():
            continue
        
        content = state_path.read_text(encoding="utf-8", errors="ignore")
        # Captura updated: YYYY-MM-DD HH:MM (Resiliente a formatação Markdown via \D*)
        match = re.search(r"updated:\D*(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2})", content, re.IGNORECASE)
        if not match:
            # Tenta capturar apenas data se hora estiver ausente
            match_date = re.search(r"updated:\D*(\d{4}-\d{2}-\d{2})", content, re.IGNORECASE)
            if not match_date:
                warnings.append(f"{spec_dir.name}: campo 'updated' ausente ou malformado")
                continue
            updated_val = match_date.group(1)
        else:
            updated_val = match.group(1)
            
        # Consideramos 'stale' se for anterior ao início da hora atual (tolerância simples)
        if updated_val < now_str[:10]: # Check de data simples primeiro
             msg = f"{spec_dir.name}: status defasado ({updated_val} < {now_str[:10]})"
             warnings.append(msg)
             log_friction("GF-STATE-FRESHNESS", msg)
        elif " " in updated_val and updated_val < now_str: # Check de hora se presente
             # Advisory apenas se a diferença for significativa (>1h)? 
             # Por enquanto, qualquer atraso gera advisory conforme pedido do QA.
             msg = f"{spec_dir.name}: status desatualizado ({updated_val} < {now_str})"
             warnings.append(msg)
             log_friction("GF-STATE-FRESHNESS", msg)

    if warnings:
        return False, " | ".join(warnings)
    return True, "OK"


def check_atomic_transition():
    """Valida se o start_hash de uma spec IN_PROGRESS existe no histórico Git."""
    specs_dir = CONTEXT_DIR.parent / ".specs" / "features"
    if not specs_dir.exists():
        return True, "Sem specs"

    issues = []
    for spec_dir in [d for d in specs_dir.iterdir() if d.is_dir() and not d.name.startswith("_")]:
        state_path = spec_dir / "STATE.md"
        if not state_path.exists():
            continue

        content = state_path.read_text(encoding="utf-8", errors="ignore")
        status_match = re.search(r"status:\D*IN_PROGRESS", content, re.I)
        if not status_match:
            continue

        hash_match = re.search(r"start_hash:\D*([a-f0-9]{7,40})", content, re.I)
        if not hash_match:
            issues.append(f"{spec_dir.name}: status IN_PROGRESS mas start_hash ausente")
            continue

        start_hash = hash_match.group(1)
        # Verifica se o hash existe no Git
        check_git = subprocess.run(
            ["git", "cat-file", "-t", start_hash],
            capture_output=True,
            text=True
        )
        if check_git.returncode != 0:
            issues.append(f"{spec_dir.name}: start_hash inválido ou inexistente ({start_hash})")

    if issues:
        return False, " | ".join(issues)
    return True, "OK"


def _extract_header_update(md_text: str):
    for line in md_text.splitlines()[:25]:
        if line.lower().startswith("última atualização:") or line.lower().startswith("ultima atualizacao:"):
            return line.split(":", 1)[1].strip()
    return None


def check_metadata_freshness():
    """Alerta se metadados de atualização parecem defasados vs ultimo commit do arquivo."""
    targets = [
        CONTEXT_DIR / "brain" / "RULES.md",
        CONTEXT_DIR / "brain" / "MASTER_FLOW.md",
    ]
    stale = []

    for path in targets:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        header = _extract_header_update(text)
        if not header:
            stale.append(f"{path.name}: metadado 'Ultima Atualizacao' ausente")
            continue

        try:
            git_dt = subprocess.run(
                ["git", "log", "-1", "--format=%ci", "--", str(path)],
                capture_output=True,
                text=True,
                encoding="utf-8",
            )
            if git_dt.returncode != 0 or not git_dt.stdout.strip():
                continue
            commit_date = git_dt.stdout.strip().split(" ")[0]

            m = re.search(r"(\d{4}-\d{2}-\d{2})", header)
            if not m:
                stale.append(f"{path.name}: metadado de data invalido ({header})")
                continue
            header_date = m.group(1)
            if header_date < commit_date:
                stale.append(f"{path.name}: metadado desatualizado ({header_date} < {commit_date})")
        except Exception:
            continue

    if stale:
        return False, " | ".join(stale)
    return True, "OK"


def get_inception_metadata():
    """Lê metadados do Inception."""
    path = CONTEXT_DIR / "brain" / "INCEPTION.md"
    if not path.exists():
        return None
    try:
        content = path.read_text(encoding="utf-8")
        metadata = {}
        for line in content.splitlines():
            if ":" in line:
                key, val = line.split(":", 1)
                metadata[key.strip()] = val.strip().split("#")[0].strip()
        return metadata
    except:
        return {}


def check_wiki_integrity():
    """Verifica se a infraestrutura base da WIKI Nível 2 existe."""
    index_file = CONTEXT_DIR / "market/WIKI/_index.md"
    log_file = CONTEXT_DIR / "market/wiki_log.md"
    
    if not index_file.exists():
        return False, "Índice mestre market/WIKI/_index.md ausente."
    if index_file.stat().st_size < 50:
        return False, "Índice mestre market/WIKI/_index.md parece estar vazio ou incompleto."
    if not log_file.exists():
        return False, "Log de transações market/wiki_log.md ausente."
        
    return True, "Estrutura Wiki OK"


def is_non_initial_context():
    """Detecta se o projeto já avançou além do estágio de onboarding."""
    # Critério sugerido pela auditoria: lista de code roots
    code_roots = ["src", "app", "packages", "services", "lib"]
    root_dir = CONTEXT_DIR.parent

    # 1. Verifica pastas de código
    for dr in code_roots:
        path = root_dir / dr
        if path.exists() and any(path.iterdir()):
            return True, f"Pasta de código ativa encontrada: {dr}/"

    # 2. Verifica .specs/features/ ativos
    specs_dir = root_dir / ".specs" / "features"
    if specs_dir.exists():
        active_specs = [d for d in specs_dir.iterdir() if d.is_dir()]
        if active_specs:
            return True, f"Especificações de feature ativas: {len(active_specs)}"

    return False, "Contexto inicial limpo"


def validate():
    print("--- Iniciando validação de contexto (v2.5.0 Hardened + Hybrid) ---")
    issues = []
    exit_code = 0

    missing = check_files()
    if missing:
        issues.append(f"[ERROR] Arquivos ausentes: {', '.join(missing)}")
    else:
        print("[OK] Todos os arquivos obrigatórios presentes.")

    # Inteligência de Onboarding & Inception
    vision_exists = (CONTEXT_DIR / "brain" / "VISION.md").exists()
    metadata = get_inception_metadata()
    inception_status = metadata.get("status") if metadata else None
    is_dirty, dirty_msg = is_non_initial_context()

    if inception_status == "DRAFT":
        if vision_exists:
            print(
                "[WARN] Tradução Pendente: VISION.md detectada. Solicite @spec-enricher."
            )
            exit_code = 2
        elif is_dirty:
            issues.append(
                f"[FATAL] Inception em DRAFT mas projeto possui código ({dirty_msg})."
            )
            exit_code = 1
        else:
            print(f"[INFO] Modo Onboarding: Projeto limpo. Consulte START_HERE.md.")
            exit_code = 0
    elif inception_status == "TRANSLATION_LOCK":
        print(
            "[WARN] Bloqueio de Tradução: INCEPTION.proposed.md aguardando ratificação."
        )
        exit_code = 2
    elif inception_status == "ACTIVE":
        print("[OK] Governança ACTIVE: Limites validados.")
        exit_code = 0
    elif inception_status is not None:
        issues.append(f"[ERROR] Status de Inception inválido: {inception_status}")
        exit_code = 1

    spec_ok, spec_msg = check_specs_structure()
    if not spec_ok:
        issues.append(f"[WARN] .specs/: {spec_msg}")
        if exit_code == 0:
            exit_code = 1
    else:
        print(f"[OK] .specs/: {spec_msg}")

    acceptance_ok, acceptance_msg = check_sprint_acceptance_sync()
    if not acceptance_ok:
        issues.append(f"[ERROR] Sprint Acceptance Sync: {acceptance_msg}")
        exit_code = 1
        log_friction("GF-ACCEPTANCE-DESYNC", acceptance_msg)
    else:
        print(f"[OK] Sprint Acceptance Sync: {acceptance_msg}")

    journal_lines, journal_ok = check_journal_lines()
    if not journal_ok:
        issues.append(
            f"[WARN] JOURNAL.md excede limite: {journal_lines}/{JOURNAL_MAX_LINES}"
        )
        if exit_code == 0:
            exit_code = 1
    else:
        print(f"[OK] JOURNAL.md dentro do limite: {journal_lines}/{JOURNAL_MAX_LINES}")

    total_chars, tokens_raw, token_ok = estimate_tokens()
    tokens_k = tokens_raw / 1000
    if not token_ok:
        issues.append(
            f"[WARN] Contexto estimado alto: tokens_raw={tokens_raw} (~{tokens_k:.1f}k). Execute purge."
        )
        if exit_code == 0:
            exit_code = 1
    else:
        print(
            f"[OK] Estimativa de contexto segura: tokens_raw={tokens_raw} (~{tokens_k:.1f}k)"
        )

    reg_ok, reg_msg = check_registry_structure()
    if not reg_ok:
        issues.append(f"[ERROR] AGENT_REGISTRY.md: {reg_msg}")
        exit_code = 1
    else:
        print("[OK] AGENT_REGISTRY.md estrutura válida.")

    meta_ok, meta_msg = check_metadata_freshness()
    if not meta_ok:
        issues.append(f"[ERROR] Metadata freshness: {meta_msg}")
        exit_code = 1
        log_friction("GF-METADATA-STALE", meta_msg)
    else:
        print(f"[OK] Metadata freshness: {meta_msg}")

    wiki_ok, wiki_msg = check_wiki_integrity()
    if not wiki_ok:
        issues.append(f"[ERROR] WIKI: {wiki_msg}")
        exit_code = 1
    else:
        print(f"[OK] WIKI: {wiki_msg}")

    atomic_ok, atomic_msg = check_atomic_transition()
    if not atomic_ok:
        issues.append(f"[ERROR] Atomic Transition: {atomic_msg}")
        exit_code = 1
        log_friction("GF-ATOMIC-DESYNC", atomic_msg)
    else:
        print(f"[OK] Atomic Transition: {atomic_msg}")

    # --- Camada ADVISORY (Sprint 03) ---
    j_chron_ok, j_chron_msg = check_journal_chronology()
    if not j_chron_ok:
        print(f"[ADVISORY] Journal Chronology: {j_chron_msg}")
    else:
        print(f"[OK] Journal Chronology: OK")

    s_fresh_ok, s_fresh_msg = check_state_freshness()
    if not s_fresh_ok:
        print(f"[ADVISORY] State Freshness: {s_fresh_msg}")
    else:
        print(f"[OK] State Freshness: OK")

    print("\n--- Relatório Final ---")
    if not issues:
        if exit_code == 2:
            print("[PENDING] Pendência estratégica detectada.")
            sys.exit(2)
        print("[SUCCESS] Contexto íntegro. Pronto para execução.")
        sys.exit(0)
    else:
        for issue in issues:
            print(issue)
        print("[FATAL] Erros de governança detectados.")
        sys.exit(1)


if __name__ == "__main__":
    try:
        validate()
    except Exception as e:
        print(f"[ERROR] Erro na execucao: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)
