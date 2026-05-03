---
contract_version: 2.5.2
parties: ["@spec-driver", "@qa-validator"]
contract_mode: sprint_based
current_sprint: sprint_01
policy_profile: hybrid
plan_source: "[CAMINHO_DO_PLANO]"
qa_signoff: false
signed_by: null

sprints:
  sprint_01:
    goal: "[Objetivo da Sprint 01]"
    scope_allow:
      - ".context/brain/RULES.md"
      - ".context/brain/MASTER_FLOW.md"
      - ".specs/features/[NOME_DA_FEATURE]/spec.md"
      - ".specs/features/[NOME_DA_FEATURE]/tasks.md"
      - ".specs/features/[NOME_DA_FEATURE]/STATE.md"
      - ".context/maintenance/JOURNAL.md"
      - ".context/maintenance/HARNESS_LOG.md"
    scope_deny: []
    acceptance:
      - "[ ] Criterio 1"
      - "[ ] Criterio 2"
    qa_signoff: false

  sprint_02:
    goal: "[Objetivo da Sprint 02]"
    scope_allow: []
    scope_deny: []
    acceptance: []
    qa_signoff: false
---

# Spec: [NOME_DA_FEATURE]
> Modo: Sprint-based

## Objetivo
[Descricao objetiva da feature]

## Regras de Execucao
- Fechamento de sprint exige `qa_signoff: true` no bloco da sprint.
- Fechamento global exige consistencia entre `spec.md`, `tasks.md`, `STATE.md` e arvore Git limpa.
