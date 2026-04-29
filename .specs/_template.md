---
contract_version: 2.5.2
parties: ["@spec-driver", "@qa-validator"]
type: standard
executor_context_id: "ctx-dev-YYYYMMDD-HHMM"
validator_context_id: "ctx-qa-YYYYMMDD-HHMM"
impact_control:
  max_impact_radius: 3
  pre_flight_grep_terms: ["termo1", "termo2"]
definition_of_done:
  - [ ] Requisito 1
  - [ ] Requisito 2
qa_signoff: false
signed_by: null
---

# 📄 Spec: [Nome da Feature]

## 🎯 Objetivo
[Descreva o que sera construido.]

## ✅ Criterios de aceite
- [ ] O requisito principal foi implementado.
- [ ] Testes e/ou validacoes manuais executadas.
- [ ] Resultado registrado no STATE.md.

## 🔎 Regra de segregacao
- Se `type: standard`, o `validator_context_id` deve ser diferente do `executor_context_id` antes de `qa_signoff: true`.
