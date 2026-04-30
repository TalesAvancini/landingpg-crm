---
# ==============================================================================
# H.O.K FORGE - CONTRATO DE ESPECIFICAÇÃO (TLC)
# ==============================================================================
contract_version: 2.5.2
parties: ["@spec-driver", "@qa-validator"]

# MODO DE OPERAÇÃO: Escolha um dos blocos abaixo
# ------------------------------------------------------------------------------

# [MODO A] STANDARD: Para funcionalidades atômicas e rápidas (padrão)
type: standard
executor_context_id: "ctx-dev-YYYYMMDD-HHMM"
validator_context_id: "ctx-qa-YYYYMMDD-HHMM"
impact_control:
  max_impact_radius: 3
  pre_flight_grep_terms: []
definition_of_done:
  - [ ] Requisito 1
  - [ ] Requisito 2
qa_signoff: false
signed_by: null

# [MODO B] SPRINT_BASED: Para planos complexos (Contratos Evolutivos MiMo)
# contract_mode: sprint_based
# current_sprint: sprint_01
# plan_source: "caminho/do/plano_original.md"
# policy_profile: hybrid  # [strict | advisory | hybrid]
# sprints:
#   sprint_01:
#     goal: "Objetivo da Fase"
#     captured_at: "YYYY-MM-DD HH:MM" # Data de início da sprint
#     captured_by: "@spec-driver"     # Agente que iniciou a sprint
#     scope_allow: ["caminho/permitido/*"] # HG01: Whitelist obrigatória
#     scope_deny: []                       # HG01: Blacklist preventiva
#     acceptance: ["- [ ] Critério A"]
#     unblock_history: []                  # Justificativas para Soft Gates
#     qa_signoff: false
#   sprint_02:
#     goal: "..."
#     captured_at: "..."
#     captured_by: "..."
#     scope_allow: []
#     acceptance: []
#     qa_signoff: false
---

# 📄 Spec: [Nome da Feature]
> **Baseado em:** [Link/Referência do Plano se houver]

## 🎯 Objetivo
[Descreva o objetivo técnico e o impacto esperado no sistema.]

## 🛠️ Solução Proposta
[Visão geral da implementação.]

## ✅ Critérios de Aceite (Global)
- [ ] Funcionalidade reflete os requisitos do plano.
- [ ] Código validado e sem violações de governança.
- [ ] Histórico de execução registrado no STATE.md seguindo Seção 8.

## 🔎 Regras de Governança
1. **Segregação:** O validator_context_id deve ser diferente do executor_context_id.
2. **Impacto:** Alterações fora do `max_impact_radius` ou `scope_allow` exigem justificativa e unblock record.
3. **Checkpoints:** Cada sprint exige signoff do @qa-validator para transição de fase.
