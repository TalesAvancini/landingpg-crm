# 🚀 Templates Iniciais - Antigravity Kit v2.3.1 (Hardened)

Abaixo estão os templates essenciais para inicializar um novo projeto com governança de contexto e defesas ativadas (Fail-Fast Pipeline).

---

## 📁 Estrutura Mínima Recomendada

```
meu-projeto/
├── .context/
│   ├── brain/
│   │   ├── RULES.md
│   │   ├── MASTER_FLOW.md
│   │   ├── ROADMAP.md
│   │   ├── AGENT_REGISTRY.md
│   │   ├── PRD.md
│   │   └── PROMPT_LIBRARY.md
│   ├── maintenance/
│   │   ├── JOURNAL.md
│   │   ├── TECHNICAL_REQUIREMENTS.md
│   │   ├── TESTS.md
│   │   ├── rx-biology.md
│   │   ├── schema.sql
│   │   ├── rebuild_guide.md
│   │   └── _archive_context/
│   │       └── raw/
│   ├── monitoring/
│   │   └── CONTEXT_HEALTH.md
│   └── _scripts/
│       ├── _tz_utils.py
│       ├── validate_context.py
│       ├── secrets_scanner.py
│       ├── sync_project.py
│       ├── migration_registry.py
│       ├── harness_runner.py
│       ├── lint_wiki.py
│       ├── health_sync.py
│       ├── context_oracle.py
│       └── cleanup_specs.py
├── .specs/
│   └── features/
├── .github/workflows/
│   └── context-health.yml
├── .husky/
├── tests/
├── package.json
├── run_context.py
├── run_context.sh
├── .gitignore
├── .env.example
├── README.md
└── README_CONTEXT.md
```

---

## 📄 `package.json` (Template Base)

```json
{
  "name": "meu-projeto-ai",
  "version": "1.0.0",
  "description": "Projeto AI-Ready com Antigravity Kit",
  "scripts": {
    "context:validate": "python run_context.py validate",
    "context:sync": "python run_context.py sync",
    "context:cleanup": "python run_context.py cleanup",
    "context:purge": "python run_context.py purge",
    "context:harness": "python run_context.py harness",
    "context:lint": "python run_context.py lint",
    "context:oracle": "python run_context.py oracle",
    "context:health": "python run_context.py health",
    "context:all": "python run_context.py all",
    "context:test": "python tests/test_context.py",
    "prepare": "husky"
  },
  "keywords": ["ai", "context-governance", "spec-driven"],
  "author": "Seu Nome",
  "license": "MIT",
  "devDependencies": {
    "husky": "^9.1.7"
  }
}
```

---

## 📜 `.context/brain/RULES.md` (Template Base)

```markdown
---
Criado em: {{DATA_ATUAL}}
Última Atualização: {{DATA_ATUAL}}
Status: Ativo
---

# 📜 RULES.md — Template Universal de Contexto & Governança
**Projeto:** {{NOME_DO_PROJETO}}  
**Arquitetura:** AI-Agent Driven (Layered Context Architecture)  
**PROJECT_MODE:** `[BOOTSTRAP]` *(Fases finitas: BOOTSTRAP, HARDENING, PRODUCTION)*

> **Conceito Central:** A pasta `.context` é a **fonte da verdade** (Single Source of Truth). O projeto é dividido em camadas para garantir escala e rastreabilidade.

---

## 🏗️ 0. Máquina de Estados do Projeto (`PROJECT_MODE`)
O template governa a si mesmo e ao projeto através de três estados rígidos:
1. **`[BOOTSTRAP]`**: Focado na criação da infraestrutura do projeto e arquitetura.
2. **`[HARDENING]`**: Ajustes em segurança (ci/cd, secret-scanners), estabilização e redução de dívida técnica.
3. **`[PRODUCTION]`**: Desenvolvimento maduro de features.
> ⚠️ **Regra de Transição:** Qualquer mudança de estado deve ser registrada no `JOURNAL.md` via `[handoff]`.

---

## 🛡️ 1. Checklist de Carga (Obrigatório)
Antes de gerar código, validar:
1. [ ] **Global:** `brain/RULES.md`, `brain/MASTER_FLOW.md`, `brain/ROADMAP.md`
2. [ ] **Role:** Conforme `brain/AGENT_REGISTRY.md`
3. [ ] **Ephemeral:** `brain/PRD.md` + `maintenance/schema.sql` + `JOURNAL.md` (últimas 30 linhas)
> ⚠️ Se qualquer item estiver ausente → parar e solicitar correção.

---

## 🔢 2. Session Budget & Heurísticas de Token
- **Alerta:** ~50k caracteres OU ~15-20 trocas densas
- **Ação:** Oferecer purge do JOURNAL ou snapshot de sessão

---

## 🧠 3. Protocolo de Manutenção
- **JOURNAL.md:** Apenas decisões arquiteturais e bugs complexos. Limite: ~600 linhas.
- **TECHNICAL_REQUIREMENTS.md:** Atualizar com mudanças em deps/schema.
- **.specs/:** Specs efêmeras → arquivar pós-merge ou >48h inativo.

---

## 🗄️ 4. Protocolo Database-First
1. Validar `maintenance/schema.sql` antes de criar UI/lógica dependente.
2. Se campo inexistente → avisar e sugerir migration.

---

## 🤖 5. Comportamento do Agente
- **Ativação:** `🤖 Ativando @[role] | Escopo: [descrição]`
- **Isolamento:** Carregar APENAS `Global + Role-Specific + Task-Ephemeral`
- **Handoff:** Registrar em `JOURNAL.md` ao cruzar domínios

---

## 🚨 6. Segurança
- **Segredos:** Nunca hardcoded. Usar `[VAR_NAME]` + `.env`
- **Depreciação:** Marcar como `[DEPRECATED]` ao remover
```

---

## 📊 `.context/monitoring/CONTEXT_HEALTH.md` (Template Base)

```markdown
---
Criado em: {{DATA_ATUAL}}
Última Atualização: {{DATA_ATUAL}}
Status: Ativo
---

# 📊 Health Check do Contexto - Dashboard

💡 *Insight Humano: Este dashboard informa se o contexto está "poluído" ou "desatualizado".*

<!-- HEALTH_TABLE_START -->
| Metrica | Valor Atual | Limite Ideal | Pilar | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Governanca** | | | | |
| Project Mode | `BOOTSTRAP` | N/A | Lifecycle | [OK] |
| Fila de Hardening | 0 | 0 | Roadmap | [OK] |
| **Manutencao** | | | | |
| Linhas do Journal | 10 | 600 | Tracker | [OK] |
| Carga do Journal | 500 chars | 50k chars | Tracker | [OK] |
| **Cognitivo** | | | | |
| Estimativa Tokens | ~1k | 128k (Max) | Eficiencia | [OK] |
| **Consistencia** | | | | |
| Tabelas no Schema | 0 | N/A | DB-First | [OK] |
| Migrations Pendentes| 0 file(s) | N/A | DB-First | [OK] |
| Ultimo Harness | Seed Check | Pass/Fail | Integridade | [PASS] |
| Ultima Sincronia | {{DATA_ATUAL}} | Real-Time | Automacao | [OK] |
<!-- HEALTH_TABLE_END -->

---

## 🚨 Regras de Degradação & Ações
- **Se Journal > 550 linhas ou > 45k char:** Ativar `@context-keeper` para rodar `_scripts/purge_journal.py`.
- **Se Schema vs PRD divergir:** Bloquear geração de UI até migration.
```

---

## 🔄 `run_context.py` (Orquestrador V2.3.1 HARDENED)

```python
#!/usr/bin/env python3
"""
🐍 run_context.py - Gestor Universal de Contexto (v2.3.1 Hardened)
Orquestrador multiplataforma protegido com Fail-Fast estrito.
"""
import sys
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).parent
SCRIPTS_DIR = BASE_DIR / ".context" / "_scripts"

def run_script(name, args=None):
    if args is None: args = []
    script_path = SCRIPTS_DIR / name
    if not script_path.exists():
        print(f"[ERROR] Script {name} não encontrado em {SCRIPTS_DIR}")
        sys.exit(1)
    
    print(f"\n[RUN] Executando {name}...")
    try:
        subprocess.run([sys.executable, str(script_path)] + args, check=True)
    except subprocess.CalledProcessError:
        print(f"\n[FATAL] Falha na etapa: {name}.")
        print("[FATAL] O pipeline foi interrompido para manter a integridade do repositório.")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("[USAGE] python run_context.py [validate|purge|sync|cleanup|harness|oracle|health|lint|all]")
        sys.exit(1)

    cmd = sys.argv[1]
    extra_args = sys.argv[2:]

    if cmd == "validate": run_script("validate_context.py", extra_args)
    elif cmd == "sync":   run_script("sync_project.py", extra_args)
    elif cmd == "purge":  run_script("purge_journal.py", extra_args)
    elif cmd == "oracle": run_script("context_oracle.py", extra_args)
    elif cmd == "harness": run_script("harness_runner.py", extra_args)
    elif cmd == "lint":   run_script("lint_wiki.py", extra_args)
    elif cmd == "health": run_script("health_sync.py", extra_args)
    elif cmd == "cleanup": run_script("cleanup_specs.py", extra_args)
    elif cmd == "all":
        # Fail-Fast Pipeline Crítico (Hardened v2.3.1)
        run_script("validate_context.py")
        run_script("secrets_scanner.py")
        run_script("sync_project.py")
        run_script("migration_registry.py")
        run_script("harness_runner.py")
        run_script("lint_wiki.py", ["--strict"])
        run_script("health_sync.py")
        print("\n[DONE] Pipeline H.O.K. + Security + Migrations + Health concluído com sucesso.")
    else:
        print(f"❌ Comando desconhecido: {cmd}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

---

## 🧹 `.context/_scripts/validate_context.py` (V2.3.1 HARDENED)

```python
#!/usr/bin/env python3
"""
🔍 validate_context.py (v2.3.1 Hardened)
Verifica saúde do .context, tokens e valida arquivos. Bloqueia pipeline em caso de falha.
"""
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
CONTEXT_DIR = SCRIPT_DIR.parent

REQUIRED_FILES = [
    "brain/RULES.md", 
    "brain/MASTER_FLOW.md", 
    "brain/ROADMAP.md",
    "brain/AGENT_REGISTRY.md",
    "brain/PRD.md", 
    "maintenance/JOURNAL.md", 
    "maintenance/schema.sql", 
    "maintenance/TECHNICAL_REQUIREMENTS.md",
    "monitoring/CONTEXT_HEALTH.md"
]

JOURNAL_MAX_LINES = 600
TOKEN_WARN_THRESHOLD_CHARS = 400_000

def check_files():
    return [f for f in REQUIRED_FILES if not (CONTEXT_DIR / f).exists()]

def validate():
    print(f"--- Iniciando validação de contexto (v2.3 Hardened) ---")
    issues = []

    missing = check_files()
    if missing: 
        issues.append(f"[ERROR] Arquivos ausentes: {', '.join(missing)}")
    else: 
        print("[OK] Todos os arquivos obrigatórios presentes.")

    # Simulação da contagem do Journal e Tokens para o Template Base
    journal = CONTEXT_DIR / "maintenance/JOURNAL.md"
    if journal.exists():
        lines = len(journal.read_text(encoding="utf-8").splitlines())
        if lines > JOURNAL_MAX_LINES: issues.append(f"[ERROR] JOURNAL excedeu: {lines} linhas.")
        else: print(f"[OK] JOURNAL.md dentro do limite: {lines}/{JOURNAL_MAX_LINES}")

    print("\n--- Relatório Final ---")
    if not issues:
        print("[SUCCESS] Contexto íntegro. Pronto para execução.")
        sys.exit(0) # IMPORTANT: Exit 0 forces CI/CD to proceed safely
    else:
        for issue in issues: 
            print(issue)
        print("[FATAL] Resolva os corrompimentos de contexto antes de continuar.")
        sys.exit(1) # IMPORTANT: Exit 1 blocks CI/CD on failure

if __name__ == "__main__":
    validate()
```

---

## 🚀 Script de Bootstrap Rápido (`init_project.sh`)

```bash
#!/usr/bin/env bash
# init_project.sh - Inicializa template Antigravity Kit v2.3.1 (Hardened)
set -euo pipefail

PROJECT_NAME="${1:-meu-projeto}"
NOW=$(date +%Y-%m-%d\ %H:%M)

echo "🚀 Inicializando $PROJECT_NAME com Antigravity Kit v2.3.1..."

# Correção Sintática: Criar estrutura
mkdir -p "$PROJECT_NAME"/.context/{brain,maintenance,maintenance/_archive_context/raw,monitoring,_scripts}
mkdir -p "$PROJECT_NAME"/.specs/features
mkdir -p "$PROJECT_NAME"/tests
mkdir -p "$PROJECT_NAME"/.github/workflows
mkdir -p "$PROJECT_NAME"/.husky

cd "$PROJECT_NAME"

# Criar .gitignore
cat > .gitignore << 'EOF'
__pycache__/
*.py[cod]
.venv/
node_modules/
.env
.env.local
.vscode/
*.log
EOF

# Criar .env.example
cat > .env.example << 'EOF'
CONTEXT_TIMEZONE=America/Sao_Paulo
PROJECT_NAME=meu-projeto
STRIPE_SECRET_KEY=[STRIPE_SECRET_KEY]
DATABASE_URL=[DATABASE_URL]
EOF

echo "✅ Estrutura criada em $PROJECT_NAME/"
echo ""
echo "📋 Próximos passos:"
echo "1. Configure os .md e Python scripts nas subpastas apropriadas de .context/"
echo "2. Rode: npm install"
echo "3. Validação V2.3.1: npm run context:all"
```
