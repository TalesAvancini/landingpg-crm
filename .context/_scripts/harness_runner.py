#!/usr/bin/env python3
"""
🛡️ harness_runner.py — Validação reativa de contratos (Harness Layer)
Valida spec vs schema, PRD vs código, e integridade de handoffs.
"""

import os, re, sys, json, io, subprocess
from datetime import datetime
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from _tz_utils import format_ts
except ImportError:
    format_ts = lambda dt=None, fmt="%Y-%m-%d %H:%M": (dt or datetime.now()).strftime(
        fmt
    )
    print("[WARN] _tz_utils inacessivel. Usando timezone local MS-WIN.")

CONTEXT_DIR = Path(__file__).resolve().parents[1]
JOURNAL = CONTEXT_DIR / "maintenance" / "JOURNAL.md"
HARNESS_LOG = CONTEXT_DIR / "maintenance" / "HARNESS_LOG.md"
SCHEMA = CONTEXT_DIR / "maintenance" / "schema.sql"
HARNESS_REG = CONTEXT_DIR / "brain" / "HARNESS_REGISTRY.md"
PRD = CONTEXT_DIR / "brain" / "PRD.md"
INCEPTION = CONTEXT_DIR / "brain" / "INCEPTION.md"


def check_schema_contract(spec_path):
    """Valida se campos/tabelas da spec existem no schema.sql"""
    if not spec_path.exists() or not SCHEMA.exists():
        return True, "Schema/spec indisponivel (skip)"
    spec_text = spec_path.read_text(encoding="utf-8")
    schema_text = SCHEMA.read_text(encoding="utf-8")
    tables_spec = set(re.findall(r"`(tabela|table)[\s_]+(\w+)", spec_text, re.I))
    tables_schema = set(
        re.findall(
            r"CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?[\"\']?(\w+)", schema_text, re.I
        )
    )

    # We only care about the table name captured in group 2 for specs if the matched syntax was used.
    # A robust extraction gets just the table name.
    spec_tnames = {t[1] for t in tables_spec}
    missing = spec_tnames - tables_schema
    if missing:
        return False, f"Spec pede tabelas inexistentes: {missing}"
    return True, "Schema contract OK"


def check_handoff_integrity(journal_text):
    """Verifica se handoffs recentes estao completos (suporta historico e padrao atual)"""
    fails = []

    # Previne loop: ignora linhas de log do próprio harness (- **Detalhe:** handoff: ...)
    clean_lines = [
        line
        for line in journal_text.splitlines()
        if "[HARNESS-" not in line and "Handoffs malformados:" not in line
    ]
    clean_text = "\n".join(clean_lines)

    # 1. Checa padrão legado: [handoff:...]
    legados = re.findall(r"\[handoff:(.*?)\]", clean_text, re.I)
    for h in legados:
        if h.count("|") < 2:
            fails.append(f"Legado incompleto: {h[:30]}")

    # 2. Checa padrão moderno: (🔄 )Handoff: RoleA -> RoleB | Info | Info
    modernos = re.findall(r"(?:🔄\s*)?Handoff:\s*(.*?)(?=\n|$)", clean_text, re.I)
    for h in modernos:
        if h.count("|") < 2:
            fails.append(f"Handoff incompleto: {h[:30]}")

    if fails:
        return False, f"Handoffs malformados: {fails}"
    return True, "Handoffs integros"


def check_strategic_alignment():
    if not INCEPTION.exists() or not PRD.exists():
        return True, "INCEPTION/PRD ausentes (skip estratégico)"
    prd_text = PRD.read_text(encoding="utf-8").lower()
    inception_text = INCEPTION.read_text(encoding="utf-8")
    boundaries = re.findall(r"^-\s*NUNCA:\s*(.+)$", inception_text, re.I | re.MULTILINE)
    violations = [
        b.strip()
        for b in boundaries
        if re.search(re.escape(b.strip().lower()), prd_text)
    ]
    if violations:
        return False, f"PRD viola boundaries estrategicas: {violations}"
    return True, "Strategic alignment OK"


def check_enrichment_integrity(prd_path: Path):
    """Valida seção Critical Dependencies semanticamente (bullet + Fonte: + market/)."""
    if not prd_path.exists():
        return True, "PRD ausente (skip)"
    text = prd_path.read_text(encoding="utf-8")
    text_lower = text.lower()

    # Só exige a seção se o PRD mencionar integrações, compliance ou APIs externas
    trigger_keywords = [
        "integração",
        "integracao",
        "integration",
        "compliance",
        "api externa",
        "external api",
        "stripe",
        "lgpd",
        "meta",
        "aws",
        "webhook",
    ]
    if not any(kw in text_lower for kw in trigger_keywords):
        return True, "Sem menção a integrações/compliance (skip)"

    section_match = re.search(
        r"^##\s*.*?Critical Dependencies.*?\n(.*?)(?=\n## |\Z)",
        text,
        re.I | re.DOTALL | re.MULTILINE,
    )
    if not section_match:
        return (
            False,
            "Seção Critical Dependencies obrigatória para PRDs com integrações/compliance",
        )

    deps_text = section_match.group(1)
    missing = []
    for line in deps_text.splitlines():
        line = line.strip()
        if line.startswith("-"):
            # Validação semântica: deve conter "Fonte:" e "market/"
            if "fonte:" not in line.lower() or "market/" not in line.lower():
                missing.append(line[:60])

    if missing:
        return False, f"Dependencies sem lastro em market/: {missing}"
    return True, "Enrichment contract OK"


# Whitelist Operacional para Plano V2-Safe (Seção 15)
WHITELIST_V2 = {
    ".context/_scripts/harness_runner.py",
    ".agent/subagents/qa-validator.md",
    ".agent/subagents/spec-driver.md",
    ".specs/_template.md",
    ".context/_scripts/cleanup_specs.py",
    ".context/brain/MASTER_FLOW.md",
    ".context/brain/SCRIPT_GLOSSARY.md",
    ".context/brain/FILE_GLOSSARY.md",
    ".context/brain/HARNESS_REGISTRY.md",
    "tests/test_context.py",
    ".context/maintenance/JOURNAL.md",
    ".context/maintenance/HARNESS_LOG.md",
    "planos/mudanca_specdriven/plano_v2_caminho_seguro_falsh.md",
    "planos/mudanca_specdriven/mudanca_specdriven.md", # Movido pelo usuário
    "planos/mudanca_specdriven/relatorio_auditoria_contract_sprints.md", # Documentação de auditoria
    ".context/brain/RULES.md", # Documentação mestre
    ".context/brain/MASTER_FLOW.md" # Fluxo mestre
}

def _get_modified_files(start_hash):
    """Retorna lista de arquivos modificados desde o start_hash (inclui working tree)."""
    try:
        res = subprocess.run(
            ["git", "diff", "--name-only", start_hash],
            capture_output=True, text=True, encoding="utf-8"
        )
        return [f.strip() for f in res.stdout.splitlines() if f.strip()]
    except:
        return []

def _get_diff_stats(start_hash):
    """Calcula estatísticas de churn (linhas +/-) desde o start_hash."""
    try:
        res = subprocess.run(
            ["git", "diff", "--shortstat", start_hash],
            capture_output=True, text=True, encoding="utf-8"
        )
        return res.stdout.strip()
    except:
        return "Nenhuma alteração detectada"

def _validate_standard_contract(contract):
    """Lógica original v2.5.2 para contratos standard binários."""
    has_dod = "definition_of_done:" in contract
    has_signoff = re.search(r"qa_signoff:\s*true", contract, re.I)
    has_signed_by = re.search(r'signed_by:\s*["\']?@qa-validator["\']?', contract, re.I)

    if not has_dod:
        return False, "Campo definition_of_done obrigatório"
    if not has_signoff:
        return False, "Contrato standard não assinado pelo @qa-validator (qa_signoff: false)"
    if not has_signed_by:
        return False, "Campo signed_by inválido ou ausente"

    # Verificação de segregação
    exec_match = re.search(r"^\s*executor_context_id:\s*(.+?)\s*$", contract, re.I | re.M)
    valid_match = re.search(r"^\s*validator_context_id:\s*(.+?)\s*$", contract, re.I | re.M)

    executor_id = exec_match.group(1).strip().strip('"').strip("'") if exec_match else ""
    validator_id = valid_match.group(1).strip().strip('"').strip("'") if valid_match else ""

    if not executor_id or not validator_id or executor_id.lower() in {"null", "none"}:
        return False, "Spec standard requer context_ids preenchidos"
    if executor_id == validator_id:
        return False, "Spec standard requer segregação de contextos (dev != qa)"
    
    return True, "Sprint contract (Standard) validado"

def _validate_sprint_contract(contract, spec_path):
    """Modo Contract Sprints com Enforcement Real (HG01-07)."""
    # HG03: Contract Break
    current_sprint_match = re.search(r"current_sprint:\s*(\w+)", contract, re.I)
    if not current_sprint_match:
        return False, "[HG03] Modo sprint_based exige campo current_sprint"
    
    curr = current_sprint_match.group(1)
    
    # HG04: Sprint Order & Enforcement Real
    # Coleta todas as sprints definidas para validar a ordem
    all_sprints = re.findall(r"(sprint_\d+):", contract)
    for s in all_sprints:
        # Se a sprint for anterior à atual, EXIGE qa_signoff: true
        if s < curr:
            s_block = re.search(rf"{s}:(.*?)(?=sprint_\d+:|\Z)", contract, re.I | re.DOTALL)
            if not s_block or "qa_signoff: true" not in s_block.group(1).lower():
                return False, f"[HG04] Sprint anterior ({s}) pendente de signoff. Impossível avançar para {curr}."
    
    # Busca bloco da sprint atual
    block_match = re.search(rf"{curr}:(.*?)(?=sprint_\d+:|\Z)", contract, re.I | re.DOTALL)
    if not block_match:
        return False, f"[HG03] Bloco de definição da sprint {curr} não encontrado na spec"
    
    sprint_block = block_match.group(1)
    
    # HG06: Start Hash (Obrigatório em sprint_based)
    state_path = spec_path.parent / "STATE.md"
    if not state_path.exists():
        return False, "[HG06] STATE.md ausente. Impossível validar baseline de sprint."
    
    state_text = state_path.read_text(encoding="utf-8")
    # Regex refinado para Markdown Headings (Seção 8)
    hash_match = re.search(rf"##\s*{curr}.*?start_hash:\s*([a-f0-9]+)", state_text, re.I | re.DOTALL)
    
    if not hash_match:
        return False, f"[HG06] start_hash não encontrado para {curr} no STATE.md (Formato esperado: ## {curr} \n start_hash: ...)"
    
    start_hash = hash_match.group(1)
    # Valida se o hash existe no git
    check_hash = subprocess.run(["git", "cat-file", "-t", start_hash], capture_output=True)
    if check_hash.returncode != 0:
        return False, f"[HG06] Start_hash inválido ou não resolvível: {start_hash}"

    # Coleta arquivos modificados desde o início da sprint
    modified = _get_modified_files(start_hash)
    
    # HG07: Outside Whitelist (Para tarefas de framework)
    if "contract_sprints_v2_safe" in str(spec_path):
        for f in modified:
            f_clean = f.replace("\\", "/")
            if f_clean.startswith(".specs/features/"): continue 
            if f_clean not in WHITELIST_V2:
                return False, f"[HG07] Violação de Whitelist Operacional: Arquivo '{f}' proibido nesta missão."

    # HG01: Scope Violation
    allow_match = re.search(r"scope_allow:\s*\[(.*?)\]", sprint_block)
    if allow_match:
        allowed = [s.strip().strip('"').strip("'") for s in allow_match.group(1).split(",") if s.strip()]
        if allowed:
            for f in modified:
                if not any(f.startswith(a) or a in f for a in allowed):
                    return False, f"[HG01] Violação de Escopo Sprint: Arquivo '{f}' fora do planejado para {curr}."

    # Exibe impacto incremental (D1/D2)
    stats = _get_diff_stats(start_hash)
    print(f"[IMPACTO] {curr}: {stats}")
    
    # D1 Real: Persiste métricas no STATE.md
    _update_sprint_state(state_path, curr, stats)

    # C2: Bloqueio de feature_done global
    global_signoff = re.search(r"^qa_signoff:\s*true", contract, re.I | re.M)
    if global_signoff:
        # Se tentou fechar a feature, a sprint atual DEVE ser a última e DEVE estar assinada
        last_sprint = all_sprints[-1] if all_sprints else None
        if curr != last_sprint:
            return False, f"[HG04] Bloqueio Final: Não é possível dar signoff global se a sprint atual ({curr}) não é a última ({last_sprint})."
        if "qa_signoff: true" not in sprint_block.lower():
            return False, "[HG04] Bloqueio Final: A última sprint deve ter signoff interno antes do signoff global."

    return True, f"Sprint contract ({curr}) validado com Hardening Pass (C2 Enforced)"

def check_sprint_contract(spec_path: Path):
    """Valida o contrato da spec detectando o modo de operação (Dual Mode)."""
    if not spec_path.exists():
        return False, "Nenhuma Spec ativa detectada."

    text = spec_path.read_text(encoding="utf-8")
    yaml_match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not yaml_match:
        return False, "Bloco de contrato (---) ausente no topo da spec"

    contract = yaml_match.group(1)
    
    # Detector de Modo
    is_sprint_mode = "contract_mode: sprint_based" in contract
    type_match = re.search(r'^\s*type:\s*["\']?(\w+)["\']?\s*$', contract, re.I | re.M)
    spec_type = type_match.group(1).strip().lower() if type_match else None

    if is_sprint_mode:
        return _validate_sprint_contract(contract, spec_path)
    elif spec_type == "standard" or "definition_of_done:" in contract:
        return _validate_standard_contract(contract)
    
    return False, "Modo de contrato não identificado ou malformado"


def check_impact_radius(spec_path: Path):
    """Valida se o numero de arquivos modificados excede o max_impact_radius definido na spec."""
    if not spec_path.exists():
        return True, "Spec ausente (skip impact check)"

    text = spec_path.read_text(encoding="utf-8")
    # Extrai bloco YAML
    yaml_match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not yaml_match:
        return True, "YAML ausente para impact check (skip)"

    contract = yaml_match.group(1)
    # Procura por max_impact_radius: N
    radius_match = re.search(r"max_impact_radius:\s*(\d+)", contract, re.I)
    if not radius_match:
        return True, "max_impact_radius nao definido na spec (skip)"

    max_radius = int(radius_match.group(1))

    # Executa git diff para ver o que mudou no working tree
    try:
        # Pega a lista de arquivos modificados, deletados ou novos (staging + working tree)
        # --name-only lista os nomes, wc -l conta.
        res = subprocess.run(
            ["git", "diff", "--name-only", "HEAD"],
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        # Filtra linhas vazias
        modified_files = [f for f in res.stdout.splitlines() if f.strip()]
        count = len(modified_files)

        if count > max_radius:
            return (
                False,
                f"Raio de impacto excedido! (Modificados: {count} > Limite: {max_radius}). Re-fragmente a SPEC ou aumente o limite se justificado.",
            )

        return True, f"Impact radius OK ({count}/{max_radius})"
    except Exception as e:
        return True, f"Erro ao verificar git diff: {e} (skip)"


def check_journal_sam():
    """Executa o Auditor Anti-Migué (SAM)."""
    script_path = Path(__file__).resolve().parent / "workflow_journal_auditor.py"
    if not script_path.exists():
        return True, "SAM Auditor indisponivel (skip)"

    print("[RUN] Executando Auditoria Anti-Migué (SAM)...")
    try:
        # Tenta carregar o modo do Synapse para decidir se o erro é fatal
        syn_path = CONTEXT_DIR / "maintenance" / "JOURNAL_SYNAPSE.md"
        mode = "assist"
        if syn_path.exists():
            content = syn_path.read_text(encoding="utf-8")
            match = re.search(
                r"<!-- SYNAPSE_JSON_START -->\s*(.*?)\s*<!-- SYNAPSE_JSON_END -->",
                content,
                re.DOTALL,
            )
            if match:
                syn_json = json.loads(match.group(1))
                mode = syn_json.get("mode", "assist")

        res = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=True,
            text=True,
            encoding="utf-8",
        )

        if res.returncode != 0:
            msg = f"Violações SAM detectadas.\n{res.stdout}"
            if mode == "strict":
                return False, msg
            else:
                print(
                    f"[WARN] SAM detectou pendencias mas está em modo ASSIST:\n{res.stdout}"
                )
                return True, "SAM PASS (Assist Mode)"

        return True, "SAM Audit OK"
    except Exception as e:
        msg = f"Erro crítico ao executar SAM Auditor: {e}"
        if mode == "strict":
            return False, msg
        print(f"[WARN] {msg} (skip em assist)")
        return True, msg


def log_harness(status, detail, spec_name="unknown"):
    """Registra no HARNESS_LOG.md de forma compacta e atomica"""
    entry = f"\n## [HARNESS-{status.upper()}] Report | spec:{spec_name}\n- **Detalhe:** {detail}\n"
    try:
        tmp = HARNESS_LOG.with_suffix(".tmp")
        header = (
            "---\n"
            "Criado em: 2026-04-24 15:20\n"
            "Ultima Atualizacao: 2026-04-24 15:20\n"
            "Status: Ativo\n"
            "---\n\n"
            "# HARNESS_LOG.md\n"
            "> Log tecnico automatico do Harness (PASS/FAIL).\n"
        )
        content = (
            HARNESS_LOG.read_text(encoding="utf-8") if HARNESS_LOG.exists() else header
        )
        tmp.write_text(content + entry, encoding="utf-8")
        tmp.replace(HARNESS_LOG)
    except Exception as e:
        print(f"[WARN] Falha ao logar harness: {e}")


def _update_sprint_state(state_path: Path, sprint_name: str, stats: str):
    """Injeta estatísticas de impacto diretamente no bloco da sprint no STATE.md."""
    if not state_path.exists(): return
    try:
        content = state_path.read_text(encoding="utf-8")
        
        file_match = re.search(r"(\d+)\s*files?\s*changed", stats)
        add_match = re.search(r"(\d+)\s*insertions?", stats)
        del_match = re.search(r"(\d+)\s*deletions?", stats)
        
        files = file_match.group(1) if file_match else "0"
        adds = add_match.group(1) if add_match else "0"
        dels = del_match.group(1) if del_match else "0"
        
        # Atualiza impact_snapshot (Seção 8 e D1)
        impact_block = (
            f"impact_snapshot:\n"
            f"  files_changed: {files}\n"
            f"  churn_added: {adds}\n"
            f"  churn_removed: {dels}"
        )
        
        # Procura o bloco da sprint e substitui APENAS o impact_snapshot
        # O regex busca a seção da sprint e captura o bloco impact_snapshot para substituição
        pattern = rf"(##\s*{sprint_name}.*?)(impact_snapshot:.*?\n\s*churn_removed:\s*\d+)"
        
        # O grupo 1 (\1) contém o heading e campos anteriores (start_hash, etc)
        # Substituímos o grupo 2 (impact_snapshot) pelo novo bloco
        new_content = re.sub(pattern, rf"\1{impact_block}", content, flags=re.DOTALL | re.I)
        
        if new_content != content:
            state_path.write_text(new_content, encoding="utf-8")
            print(f"[D1] STATE.md sincronizado com impacto real ({sprint_name})")
    except Exception as e:
        print(f"[WARN] Falha ao atualizar impacto no STATE.md: {e}")

def update_state_md(spec_dir: Path, status: str, detail: str = ""):
    state_path = spec_dir / "STATE.md"
    if not state_path.exists():
        return
    
    current_content = state_path.read_text(encoding="utf-8")
    # Tenta separar o YAML do corpo
    parts = re.split(r"^---\s*$", current_content, maxsplit=2, flags=re.MULTILINE)
    
    body = ""
    if len(parts) >= 3:
        body = parts[2]
    else:
        body = current_content # Fallback se não houver YAML claro
        
    new_yaml = f"---\nstatus: {status}\nupdated: {format_ts()}\ndetail: {detail}\n---\n"
    state_path.write_text(new_yaml + body, encoding="utf-8")
    
    status_print = status.replace("✅", "[OK]").replace("❌", "[FAIL]")
    print(f"[STATE.md] -> {status_print} na spec {spec_dir.name}")


def get_inception_status():
    """Lê o status do Inception mestre."""
    if not INCEPTION.exists():
        return "MISSING"
    try:
        content = INCEPTION.read_text(encoding="utf-8")
        for line in content.splitlines():
            if line.strip().startswith("status:"):
                # Captura o valor antes de qualquer comentário #
                return line.split(":")[1].strip().split("#")[0].strip()
    except:
        return "ERROR"
    return "UNKNOWN"

def check_epistemological_gate(spec_path: Path):
    """Fase 2.6: Gate Epistemológico (Oracle como Pré-Gate do Harness)"""
    if not spec_path.exists():
        return True, "Spec ausente (skip oracle check)"
    
    try:
        from context_oracle import query_oracle
    except ImportError:
        return True, "context_oracle indisponível (skip oracle check)"
        
    text = spec_path.read_text(encoding="utf-8")
    title_match = re.search(r'^#\s+(.+)$', text, re.MULTILINE)
    query = title_match.group(1) if title_match else spec_path.parent.name
    
    import concurrent.futures
    try:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(query_oracle, query)
            res = future.result(timeout=2.0)
            
        conf = res.get("confidence", 0)
        if conf < 0.4:
            print(f"[WARN] Gate Epistemológico: Baixa confiança ({conf:.2f}) no oráculo para o termo '{query}'. Considere refinar o conhecimento.")
            return True, f"Gate Epistemológico avisado (conf: {conf:.2f})"
            
        return True, f"Gate Epistemológico OK (conf: {conf:.2f})"
        
    except concurrent.futures.TimeoutError:
        print("[WARN] Gate Epistemológico: Timeout ao consultar o Oráculo (> 2s). Bypass permitido.")
        return True, "Gate Epistemológico Timeout"
    except Exception as e:
        print(f"[WARN] Gate Epistemológico falhou: {e}")
        return True, "Gate Epistemológico Erro"


def run_env_drift_gate():
    """Executa o Harness de Variáveis de Ambiente."""
    gate_path = CONTEXT_DIR / "_scripts" / "env_drift_gate.py"
    if not gate_path.exists():
        return True, "Env Drift Gate ausente (skip)"
    res = subprocess.run([sys.executable, str(gate_path)], capture_output=True, text=True, encoding="utf-8")
    if res.returncode != 0:
        return False, res.stdout + res.stderr
    print(res.stdout)
    return True, "Env Drift OK"

def run_complexity_coverage_gate():
    """Executa o Harness de Complexidade e Cobertura Semântica (Consultivo)."""
    gate_path = CONTEXT_DIR / "_scripts" / "complexity_coverage_gate.py"
    if not gate_path.exists():
        return True, "Complexity Gate ausente (skip)"
    res = subprocess.run([sys.executable, str(gate_path)], capture_output=True, text=True, encoding="utf-8")
    print(res.stdout)
    return True, "Complexity and Coverage evaluated"

def main():
    # 0. Verificação de Estado (Hybrid Discovery)
    status = get_inception_status()
    if status == "DRAFT":
        root = CONTEXT_DIR.parent
        code_exts = {
            ".py", ".js", ".jsx", ".ts", ".tsx", ".go", ".rs", ".java", ".kt", ".cs", ".php",
        }
        ignore_names = {".gitkeep", ".keep"}
        ignore_prefixes = ("README",)
        ignore_dirs = {"node_modules", ".git", ".venv", "__pycache__", "dist", "build"}

        def has_real_code_activity():
            for code_root in ["src", "app", "packages", "services", "lib"]:
                base = root / code_root
                if not base.exists() or not base.is_dir():
                    continue
                for cur, dirs, files in os.walk(base):
                    dirs[:] = [d for d in dirs if d not in ignore_dirs]
                    for fname in files:
                        if fname in ignore_names: continue
                        if fname.startswith(ignore_prefixes): continue
                        path = Path(cur) / fname
                        if path.suffix.lower() in code_exts and path.stat().st_size > 0:
                            return True
            return False

        def has_real_spec_activity():
            specs_dir = root / ".specs" / "features"
            if not specs_dir.exists() or not specs_dir.is_dir():
                return False
            for spec in specs_dir.iterdir():
                if not spec.is_dir() or spec.name.startswith("_"): continue
                spec_file = spec / "spec.md"
                state_file = spec / "STATE.md"
                if spec_file.exists() and state_file.exists() and spec_file.stat().st_size > 0:
                    return True
            return False

        if has_real_code_activity() or has_real_spec_activity():
            print("[FATAL] Projeto possui atividade real (código/specs) mas INCEPTION.md está em DRAFT.")
            print("[DICA] Ative a governança: altere status para ACTIVE em INCEPTION.md.")
            sys.exit(1)

        print("[INFO] Modo Onboarding (DRAFT). Bypass permitido até ativação.")
        sys.exit(0)

    # 1. Definindo a pasta spec ativa
    features_dir = CONTEXT_DIR.parent / ".specs" / "features"
    spec_dir_env = os.environ.get("ACTIVE_SPEC")

    if spec_dir_env and (features_dir / spec_dir_env).exists():
        spec_dir = features_dir / spec_dir_env
    else:
        # Fallback: spec modificada mais recentemente
        if features_dir.exists():
            active = sorted(
                [d for d in features_dir.iterdir() if d.is_dir() and not d.name.startswith("_")],
                key=os.path.getmtime,
                reverse=True,
            )
            spec_dir = active[0] if active else None
        else:
            spec_dir = None

    spec_name = spec_dir.name if spec_dir else "manual"
    spec_path = spec_dir / "spec.md" if spec_dir else Path("dummy")

    checks = {
        "env_drift": run_env_drift_gate(),
        "complexity_coverage": run_complexity_coverage_gate(),
        "schema": check_schema_contract(spec_path),
        "handoff": check_handoff_integrity(
            JOURNAL.read_text(encoding="utf-8") if JOURNAL.exists() else ""
        ),
        "strategy": check_strategic_alignment(),
        "enrichment": check_enrichment_integrity(PRD),
        "sprint_contract": check_sprint_contract(spec_path),
        "impact_radius": check_impact_radius(spec_path),
        "epistemological": check_epistemological_gate(spec_path),
        "journal_sam": check_journal_sam(),
    }

    fails = [f"{k}: {v[1]}" for k, v in checks.items() if not v[0]]
    if fails:
        detail = " | ".join(fails)
        log_harness("fail", detail, spec_name)
        if spec_dir:
            update_state_md(spec_dir, "❌ FAILED", detail)
        print(f"[ERROR] Harness fail: {detail}")
        sys.exit(1)

    log_harness("pass", "All contracts valid", spec_name)
    if spec_dir:
        update_state_md(spec_dir, "✅ PASSED", "All checks passed")
    print("[OK] Harness pass: Contracts validated.")
    sys.exit(0)


if __name__ == "__main__":
    main()
