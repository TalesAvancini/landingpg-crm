# 🚀 Guia de Migração H.O.K. Modo Light & Harnesses (Handoff para Autobuilder)

> **Destinatário**: Engenheiro de DevOps / IA do Repositório Mãe `autobuilder`  
> **Assunto**: Implantação de flexibilização de governança (SAM Light) e 3 novos validadores físicos de Harness.  
> **Data/Versão**: 2026-05-31 — Governança H.O.K. Nível 3

Este guia descreve as decisões de design, a topologia de dependências e os códigos-fonte exatos para migrar as melhorias de governança implementadas e testadas com sucesso no repositório de produção para o repositório mãe **autobuilder**.

---

## 🏗️ 1. Topologia da Governança V3 (A Fiação)

As novas regras do Modo Light e os validadores locais de Harness se integram da seguinte forma na esteira de commit do Husky:

```
[ git commit ]
       │
       ▼
 [ Husky Hook ] ───► Roda validate_context.py, secrets_scanner.py, check_version_consistency.py
       │
       ├─► [ workflow_journal_auditor.py (SAM) ]
       │         ├── Se Branch == main/master ──► STRICT (Exit Code 1)
       │         └── Se Branch == feature/*   ──► ASSIST/WARNING (Exit Code 0)
       │
       └─► [ harness_runner.py (Mestre) ]
                 ├─► check_schema_contract()
                 ├─► check_handoff_integrity()
                 ├─► run_env_drift_gate() ───► env_drift_gate.py (STRICT - Exit Code 1)
                 └─► run_complexity_coverage_gate() ───► complexity_coverage_gate.py (WARNING)
```

---

## 🛠️ 2. Novos Scripts a Serem Criados (Salvar sob `.context/_scripts/`)

### A. Harness de Variáveis de Ambiente (`env_drift_gate.py`)
Varre recursivamente arquivos de código JS e TS em busca de leituras de `process.env` e garante que estejam listadas no `.env.example`.

```python
#!/usr/bin/env python3
import os
import re
import sys
from pathlib import Path

# Configuração de encoding para Windows
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parents[2]
ENV_EXAMPLE_PATH = BASE_DIR / ".env.example"

IGNORED_DIRS = {
    "node_modules", ".git", ".context", "scratch", "planos", "temp", ".agent", ".agents", "graphify-out"
}

def get_env_example_vars():
    if not ENV_EXAMPLE_PATH.exists():
        return set()
    content = ENV_EXAMPLE_PATH.read_text(encoding="utf-8", errors="ignore")
    vars_found = set()
    for line in content.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split("=", 1)
        if parts:
            var_name = parts[0].strip()
            if re.match(r"^[A-Z_][A-Z0-9_]*$", var_name):
                vars_found.add(var_name)
    return vars_found

def scan_code_for_env_vars():
    vars_in_code = {}
    pattern = r"process\.env\.([a-zA-Z_][a-zA-Z0-9_]*)|process\.env\[['\"]([a-zA-Z_][a-zA-Z0-9_]*)['\"]\]"
    
    for root, dirs, files in os.walk(BASE_DIR):
        dirs[:] = [d for d in dirs if d not in IGNORED_DIRS]
        for file in files:
            if not file.endswith((".js", ".ts", ".jsx", ".tsx")):
                continue
            file_path = Path(root) / file
            try:
                content = file_path.read_text(encoding="utf-8", errors="ignore")
                matches = re.findall(pattern, content)
                for m in matches:
                    var_name = m[0] or m[1]
                    if var_name:
                        rel_path = file_path.relative_to(BASE_DIR)
                        vars_in_code.setdefault(var_name, []).append(str(rel_path).replace("\\", "/"))
            except Exception as e:
                print(f"[WARN] Falha ao ler {file_path}: {e}")
    return vars_in_code

def check_drift():
    print("🛡️ Executando Env Drift Gate (Harness)...")
    example_vars = get_env_example_vars()
    code_vars = scan_code_for_env_vars()
    violations = []
    for var, files in code_vars.items():
        if var not in example_vars:
            violations.append(f"Variável '{var}' consumida no código mas ausente no .env.example. Arquivos: {', '.join(files)}")
    if violations:
        print("\n❌ VIOLAÇÕES DE DRIFT DE AMBIENTE:")
        for v in violations:
            print(f"  - {v}")
        return 1
    print("✅ Env Drift Gate: Todas as variáveis de ambiente utilizadas estão documentadas no .env.example.")
    return 0

if __name__ == "__main__":
    sys.exit(check_drift())
```

---

### B. Detector de Exaustão de Loop (`loop_exhaustion_harness.py`)
Monitora falhas consecutivas de testes locais e as armazena no log efêmero `scratch/loop_state.json`. Se a IA falhar 5 vezes sem alterar fisicamente o código (verificado por hash do `git diff`), o pipeline de testes é bloqueado exigindo intervenção humana (Bandeira Branca).

```python
#!/usr/bin/env python3
import os
import sys
import json
import hashlib
import subprocess
from pathlib import Path

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parents[2]
SCRATCH_DIR = BASE_DIR / "scratch"
STATE_FILE = SCRATCH_DIR / "loop_state.json"

def get_git_diff_hash():
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
    test_state = state.setdefault(test_name, {"fail_count": 0, "last_git_diff_hash": ""})
    
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
        print(f"ℹ️ Loop Exhaustion: Mudança física de código detectada. Contador reiniciado.")
        return 0
    else:
        test_state["fail_count"] += 1
        save_state(state)
        fail_count = test_state["fail_count"]
        print(f"⚠️ Loop Exhaustion: Falha {fail_count}/5 consecutiva no teste '{test_name}' sem alterações no Git.")
        if fail_count >= 5:
            print("\n❌ [FATAL] EXAUSTÃO DE LOOP DE EXECUÇÃO DE IA!")
            print("Você falhou 5 vezes consecutivas no mesmo teste sem alterar fisicamente o código.")
            print("👉 AÇÃO REQUERIDA: Chame o Humano ou altere o código para quebrar o loop.")
            return 1
        return 0

if __name__ == "__main__":
    sys.exit(main())
```

---

### C. Gate de Complexidade e Cobertura Semântica (`complexity_coverage_gate.py`)
Gera avisos de lint e cobertura sem abortar com erro (WARNING pedagógico).

```python
#!/usr/bin/env python3
import os
import re
import sys
import subprocess
from pathlib import Path

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parents[2]

def get_modified_js_files():
    try:
        res = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True, check=True, cwd=str(BASE_DIR))
        files = []
        for line in res.stdout.splitlines():
            path = line[3:].strip()
            if path.endswith(".js") and not path.startswith((".context", "scratch", "node_modules")):
                files.append(path)
        return files
    except Exception:
        return []

def check_file_complexity(file_path: Path):
    if not file_path.exists():
        return []
    content = file_path.read_text(encoding="utf-8", errors="ignore")
    lines = content.splitlines()
    num_lines = len(lines)
    warnings = []
    if num_lines > 250:
        warnings.append(f"Arquivo longo ({num_lines} linhas). Ideal é abaixo de 250 linhas.")
    max_nesting = 0
    curr_nesting = 0
    for line in lines:
        curr_nesting += line.count("{") - line.count("}")
        if curr_nesting > max_nesting:
            max_nesting = curr_nesting
    if max_nesting > 4:
        warnings.append(f"Aninhamento de chaves excessivo ({max_nesting} níveis).")
    return warnings

def check_semantic_coverage(file_path: Path):
    if not file_path.exists():
        return []
    content = file_path.read_text(encoding="utf-8", errors="ignore")
    test_file_candidates = [
        BASE_DIR / "tests" / f"{file_path.stem}.test.js",
        BASE_DIR / "tests" / f"{file_path.name}",
    ]
    test_path = None
    for candidate in test_file_candidates:
        if candidate.exists():
            test_path = candidate
            break
    if not test_path:
        return [f"Arquivo de testes '{file_path.stem}.test.js' não encontrado na pasta tests/."]
    test_content = test_path.read_text(encoding="utf-8", errors="ignore")
    funcs = re.findall(r"function\s+([a-zA-Z_][a-zA-Z0-9_]*)|(?:const|let|var)\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*(?:\(|async\s*\(|function)", content)
    func_names = [f[0] or f[1] for f in funcs if f[0] or f[1]]
    warnings = []
    for func in func_names:
        if func.startswith("_") or func in {"require", "exports", "module"}:
            continue
        if func not in test_content:
            warnings.append(f"Função '{func}' não possui referências no arquivo de teste '{test_path.name}'.")
    return warnings

def check_complexity_and_coverage():
    print("🛡️ Executando Complexity & Semantic Coverage Gate (Consultivo)...")
    js_files = get_modified_js_files()
    has_warnings = False
    for rel_path in js_files:
        abs_path = BASE_DIR / rel_path
        comp_warns = check_file_complexity(abs_path)
        cov_warns = check_semantic_coverage(abs_path)
        all_warns = comp_warns + cov_warns
        if all_warns:
            has_warnings = True
            print(f"\n⚠️ Alertas pedagógicos em '{rel_path}':")
            for w in all_warns:
                print(f"  - {w}")
    return 0

if __name__ == "__main__":
    sys.exit(check_complexity_and_coverage())
```

---

## 🛠️ 3. Modificações nos Motores Existentes

### A. Modificar `.context/_scripts/workflow_journal_auditor.py` (SAM)
Injetar a lógica para obter a branch e desviar o modo para `assist` (WARNING) em feature branches.

```python
# 1. Inserir a função acima de audit():
def get_current_branch():
    """Retorna o nome da branch git atual ou 'main' em caso de erro."""
    try:
        res = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], capture_output=True, text=True, check=True)
        return res.stdout.strip()
    except Exception:
        return "main"

# 2. Modificar as linhas iniciais de audit() para:
def audit():
    print("🤖 Iniciando Auditoria Anti-Migué (SAM)...")
    
    git = get_git_state()
    synapse = get_synapse_rules()
    
    branch = get_current_branch()
    strict_branches = {"main", "master"}
    
    if branch in strict_branches:
        mode = synapse.get("mode", "strict")
    else:
        mode = "assist"
        print(f"ℹ️ [SAM] Feature branch '{branch}' detectada. Modo: ASSIST (WARNING).")
```

---

### B. Modificar `.context/_scripts/harness_runner.py` (Harness Mestre)
Adicionar as funções executoras globais e registrá-las no dicionário `checks`.

```python
# 1. Inserir as funções de gate fora de main() (no escopo global):
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

# 2. No dicionário checks da função main(), injetar as chamadas:
    checks = {
        "env_drift": run_env_drift_gate(),
        "complexity_coverage": run_complexity_coverage_gate(),
        "schema": check_schema_contract(spec_path),
        # ...
    }
```

---

### C. Modificar `AGENTS.md` (Constituição de Boot)
Adicionar a nova diretiva de conduta sob Diretivas Comportamentais:

```markdown
9. **Protocolo de Pre-Push & Sunset (Validação & Inquisição):** Antes de realizar ou sugerir qualquer `git push` ou encerramento de feature (Sunset), você é **OBRIGADO** a carregar a skill `semantic-propagation`, executar a validação local (`npm run context:all`), e caso existam warnings de código, invocar o subagente `Warning Inquisitor` para gerar o rascunho de justificativas no `JOURNAL.md` (sob a seção `Bypasses/Justificativas`) antes de submeter as mudanças para validação humana.
```

---

## 📈 4. Roteiro Recomendado de Implantação no Autobuilder

Para migrar sem travar o pipeline no meio do processo, siga este passo a passo cirúrgico:

1.  **Fase de Criação:** Copie e salve os três arquivos Python (`env_drift_gate.py`, `loop_exhaustion_harness.py`, `complexity_coverage_gate.py`) sob `.context/_scripts/` no `autobuilder`.
2.  **Fase de Atualização de Motores:** Aplique os diffs em `workflow_journal_auditor.py` e `harness_runner.py`.
3.  **Fase de Atualização de Condutas:** Insira a Regra 9 em `AGENTS.md` e adicione as notas de modo dinâmico nos fluxos (`FLOW_JOURNAL_SYNC.md` e na skill `hok-governor/SKILL.md`).
4.  **Fase de Sincronia dos Glossários:** Atualize os arquivos `FILE_GLOSSARY.md` e `SCRIPT_GLOSSARY.md` no `autobuilder` para registrar a responsabilidade dos três novos scripts e da ata de alteração.
5.  **Fase de Registro no Diário:** Crie a entrada de diário no topo do `JOURNAL.md` do `autobuilder` declarando todas essas modificações na Matriz de Propagação.
6.  **Fase de Commit:** Enscene todos os arquivos (`git add`) e faça o commit para consolidar.
