---
contract_version: 2.5.2
parties: ["@spec-driver", "@qa-validator"]
type: standard
executor_context_id: "ctx-dev-YYYYMMDD-HHMM"
validator_context_id: "ctx-qa-YYYYMMDD-HHMM"
impact_control:
  max_impact_radius: 3
  pre_flight_grep_terms: []
plan_source: "[NOME_DO_PLANO_ORIGINAL]"
definition_of_done:
  - [ ] Implementação reflete o plano original.
  - [ ] Código validado pelo @qa-validator.
  - [ ] Sem violações de governança detectadas pelo Harness.
qa_signoff: false
signed_by: ""
---

# 📄 Spec: [NOME_DA_FEATURE]
> **Origem:** [Plano Original / PRD]

## 🎯 Objetivo
[Breve descrição do objetivo técnico]

## 🏗️ Escopo Técnico
[Detalhes da implementação baseados no planejamento]
