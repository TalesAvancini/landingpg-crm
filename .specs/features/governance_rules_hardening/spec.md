---
contract_version: 2.5.2
parties: ["@spec-driver", "@qa-validator"]
contract_mode: sprint_based
current_sprint: sprint_01
policy_profile: hybrid
plan_source: planos/governance_rules_hardening/plano_governance_rules_hardening.md
qa_signoff: false
signed_by: null

sprints:
  sprint_01:
    goal: "Implementar Regras Canônicas (CLOSE_WAVE, ANTI_FALSE_PASS) e rito de Pre-Close Audit."
    scope_allow:
      - ".context/brain/RULES.md"
      - ".context/brain/MASTER_FLOW.md"
      - ".specs/features/governance_rules_hardening/spec.md"
      - ".specs/features/governance_rules_hardening/tasks.md"
      - ".specs/features/governance_rules_hardening/STATE.md"
      - ".context/maintenance/JOURNAL.md"
      - ".context/maintenance/HARNESS_LOG.md"
    scope_deny: []
    acceptance:
      - "[ ] Regras CLOSE_WAVE e ANTI_FALSE_PASS publicadas no RULES.md"
      - "[ ] Rito Pre-Close Audit inserido no MASTER_FLOW.md"
      - "[ ] Passo Pre-close Self-Audit adicionado ao workflow do spec-driver"
      - "[ ] Exemplos PASS/FAIL incluídos no RULES.md"
    qa_signoff: false

  sprint_02:
    goal: "Integridade SSOT (MIMO_STATE_INTEGRITY) e Sanidade de Script (CRITICAL_SCRIPT_SANITY)."
    scope_allow: []
    scope_deny: []
    acceptance: []
    qa_signoff: false
---

# Spec: Governance Rules Hardening
> Modo: Sprint-based (Hardened)

## Objetivo
Transformar aprendizados do pós-missão em governança executável end-to-end, eliminando fraudes narrativas e incoerências de fechamento.

## Regras de Execução
- Fechamento de sprint exige `qa_signoff: true` no bloco da sprint.
- Fechamento global exige consistência entre `spec.md`, `tasks.md`, `STATE.md` e árvore Git limpa.
