---
feature_id: melhoria_spec_driver
type: standard
contract_mode: sprint_based
current_sprint: sprint_01
executor_context_id: spec-driver
validator_context_id: qa-validator

sprint_01:
  scope_allow: 
    # Global/Maintenance (Obrigatório para V3)
    - .specs/features/melhoria_spec_driver/STATE.md
    - .specs/features/melhoria_spec_driver/tasks.md
    - .specs/features/melhoria_spec_driver/*.enriched.md
    - .context/maintenance/HARNESS_LOG.md
    - .context/maintenance/JOURNAL.md
    - .specs/features/melhoria_spec_driver/AGENT_SCRATCHPAD.md
    # Feature Scope
    - .agent/templates/spec_v3.md
    - .specs/features/SSD_PLAYBOOK.md
    - .agent/subagents/spec-driver.md
    - .agent/templates/AGENT_SCRATCHPAD.md
    - .context/brain/RULES.md
    - .specs/features/SSD_ERRORS_LEDGER.md
  dod:
    - spec_v3.md e SSD_PLAYBOOK atualizados com a vacina de Injeção Atômica.
    - spec-driver.md instruído para executar Physical Check no scope-guard.
    - AGENT_SCRATCHPAD.md enriquecido com as Traps de Tier Justification e Surgical Edits.
    - RULES.md atualizado com a regra Windows (PowerShell) baseline.
    - SSD_ERRORS_LEDGER.md enriquecido com a Scar #006.
  qa_signoff: true

---

# Feature: Otimização Spec-Driven V3 (Cura de Dores do Executor)

## 1. O Problema
O executor subagente (`spec-driver`) tem sofrido com dores como "Deriva de Atenção" (caçando IDs fora da spec), "Estagnação de Shell" (usando sintaxe Bash `&&` em PowerShell) e falhas contínuas de Regex em edições pontuais, gerando alta fricção com o SAM e Gatekeeper.

## 2. A Solução
Otimizar os artefatos de governança do Spec-Driven V3 (Templates, Prompts de Agente e Regras Globais) introduzindo regras de rito, blindagens cross-platform e fallback protocols, tudo dentro do escopo do Fail-Closed.

## 3. Requisitos Funcionais (Acceptance)
- [x] Injeção Atômica (Prevenção de Deriva de Atenção) configurada em `.agent/templates/spec_v3.md` e `.specs/features/SSD_PLAYBOOK.md`.
- [x] Sync Prévio (Mitigação de Scope Block) no `.agent/subagents/spec-driver.md`.
- [x] Protocolo Rígido de Tier (Prevenção de Anti-Loop) injetado no `.agent/templates/AGENT_SCRATCHPAD.md`.
- [x] Estagnação de Shell (Adaptação Cross-Platform) registrada em `.context/brain/RULES.md`.
- [x] Surgical Edits (Resiliência de Parser e Regex) ativado no `.specs/features/SSD_ERRORS_LEDGER.md` e `AGENT_SCRATCHPAD.md`.


## 4. Critérios de Integridade V3 (Não Negociáveis)
Para que esta Spec seja considerada completa, o executor deve gerar um `STATE.md` contendo TODAS as 9 evidências da cadeia (CHAIN_CONTEXT_LOADED até CHAIN_HANDOFF).
