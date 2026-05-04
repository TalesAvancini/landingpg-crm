---
id: gov_v3_stabilization
name: Governança V3 Stabilization
type: standard
status: active
qa_signoff: true
signed_by: "@qa-validator"
executor_context_id: CTX_HARDENING_V3_5
validator_context_id: CTX_QA_SAM
definition_of_done:
  - Prompt [RESUME] injetado no subagente.
  - Validador físico bloqueando escrita sem diretriz.
  - SAM Auditor aprovando todas as sinapses no Journal.
---

# Spec: Governança V3 Stabilization

## Objetivo
Estabilizar e endurecer o framework H.O.K Forge v2.5.2 através da implementação física do protocolo [RESUME] e sincronização com o Auditor SAM.

## Requisitos
- [x] Codificar [RESUME] no spec-driver.md.
- [x] Implementar trava física no write_with_validation.py.
- [x] Sincronizar Matriz de Propagação no JOURNAL.md.

## Allow List
- `.agent/subagents/spec-driver.md`
- `.context/_scripts/write_with_validation.py`
- `.context/maintenance/TECHNICAL_REQUIREMENTS.md`
- `.context/monitoring/PROJECT_INDEX.md`
- `.context/maintenance/JOURNAL.md`
- `.specs/features/SSD_ERRORS_LEDGER.md`
- `.specs/features/gov_v3_stabilization/STATE.md`
- `.specs/features/gov_v3_stabilization/tasks.md`
