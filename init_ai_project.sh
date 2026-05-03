#!/usr/bin/env bash
# -----------------------------------------------------------------------------
# 🚀 init_ai_project.sh - Antigravity Kit Bootstrapper (v3.0.0 Chain-Skills)
# -----------------------------------------------------------------------------
# Versão Suprema: Governança Blindada V3 com Chain-Skills & Anti-Loop.
# Com detecção automática de gerenciador e motores de manutenção completos.
# -----------------------------------------------------------------------------
set -euo pipefail

# 🎨 Cores & Estética
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

log() { echo -e "\n${CYAN}🔹 $1${NC}"; }
success() { echo -e "${GREEN}✅ $1${NC}"; }
warn() { echo -e "${YELLOW}⚠️ $1${NC}"; }
error() { echo -e "${RED}❌ $1${NC}"; exit 1; }

# 🛡️ Pre-flight Checks
check_deps() {
  command -v git >/dev/null 2>&1 || error "git e obrigatorio."
  if command -v python3 >/dev/null 2>&1; then PYTHON="python3"
  elif command -v python >/dev/null 2>&1; then PYTHON="python"
  else error "python3 ou python e obrigatorio."
  fi
}

# 🔍 Detecção de Gerenciador de Pacotes
detect_pkg_mgr() {
  if command -v pnpm >/dev/null 2>&1; then echo "pnpm"
  elif command -v yarn >/dev/null 2>&1; then echo "yarn"
  elif command -v npm >/dev/null 2>&1; then echo "npm"
  else error "Nenhum gerenciador de pacotes encontrado (npm, yarn ou pnpm)."
  fi
}

# 🔒 Segurança
if [ -d ".context" ]; then
    error ".context/ ja existe. Abortando para proteger dados."
fi

check_deps
PKG_MGR=$(detect_pkg_mgr)
log "Gerenciador detectado: $PKG_MGR"
log "Inicializando Antigravity Chain-Skills Framework v3.0.0..."

# 📂 Estrutura de Diretorios
log "Criando estrutura de camadas e workshop V3..."
mkdir -p .context/{brain,maintenance,monitoring,_scripts}
mkdir -p .context/maintenance/_archive_context/{prds,schemas,journals,specs}
mkdir -p .specs/features/_arquive_features
mkdir -p .agent/{subagents,templates}
mkdir -p tests .husky

NOW=$(date +%Y-%m-%d\ %H:%M)

# 📄 Geração de Documentos de Governança
log "Gerando documentos de governança V3..."

cat > .context/brain/RULES.md << EOF
---
Criado em: $NOW
Status: Ativo
Versão: 3.0.0 (Chain-Skills)
---
# 📜 RULES.md — DNA de Governança V3

## 🧠 1. Protocolo Chain-Skills (Obrigatório)
Qualquer execução de feature DEVE seguir as 9 Skills definidas no SSD-Chain:
1. CONTEXT_LOADED | 2. CONSTRAINTS_EXTRACTED | 3. TECHNICAL_APPROACH
4. SCRATCHPAD_SYNCED | 5. SCOPE_LOCKED | 6. EVIDENCE_GENERATION
7. SELF_AUDIT | 8. REMEDIATION | 9. HANDOFF

## 🛡️ 2. Zero-Trust & Anti-Loop
- **AGENT_SCRATCHPAD.md**: Todo erro [BLOCKED] ou [FATAL] deve ser registrado no Scratchpad com Hipótese e Plano de Correção ANTES da nova tentativa.
- **Gatekeeper Físico**: Modificações de arquivos DEVEM usar 'write_with_validation.py'. Escrita direta em arquivos de regras é PROIBIDA.

## 🔄 3. Gatilhos Operacionais
- "Inicie a feature [NOME]": IA cria spec baseada no template .agent/templates/spec_v3.md.
EOF

# Injeta scripts no package.json via Node
[ -f package.json ] || npm init -y > /dev/null 2>&1
node -e "
const fs = require('fs');
const pkg = JSON.parse(fs.readFileSync('package.json','utf8'));
pkg.scripts = pkg.scripts || {};
Object.assign(pkg.scripts, {
  'context:validate': 'python run_context.py validate',
  'context:cleanup': 'python run_context.py cleanup',
  'context:purge': 'python run_context.py purge',
  'context:sync': 'python run_context.py sync',
  'context:oracle': 'python run_context.py oracle',
  'context:lint': 'python run_context.py lint',
  'context:harness': 'python run_context.py harness',
  'context:map': 'python run_context.py map',
  'context:bundle': 'python run_context.py bundle',
  'context:all': 'python run_context.py all',
  'prepare': 'husky'
});
fs.writeFileSync('package.json', JSON.stringify(pkg, null, 2));
"

log "Instalando Husky e configurando Hooks (SAM Enforcement)..."
npx husky init > /dev/null 2>&1
echo "$PKG_MGR run context:all" > .husky/pre-commit
chmod +x .context/_scripts/*.py .husky/pre-commit

success "Antigravity Chain-Skills V3 inicializado com sucesso!"
warn "Use os templates em .agent/templates/ para garantir conformidade."
