# ✅ Tasks: Governance Rules Hardening

## 🏗️ Fase 0: Rito de Início (Ovo)
- [x] **TASK-00**: Executar rito de início (start_hash, captured_at, captured_by).
  - *Verify*: Registro no STATE.md e JOURNAL.md.

## 🏗️ Sprint 01: Regras Canônicas & Self-Audit
- [x] **TASK-01**: Inserir `CLOSE_WAVE` + `ANTI_FALSE_PASS` em RULES.md.
  - *Verify*: `npm run context:validate` (HG01).
- [x] **TASK-02**: Inserir `Pre-Close Audit` em MASTER_FLOW.md.
- [x] **TASK-03**: Adicionar passo `Pre-close Self-Audit` no workflow do @spec-driver.

## 🏗️ Sprint 02: Integridade SSOT & Scripts Críticos
- [x] **TASK-04**: Formalizar `MIMO_STATE_INTEGRITY` e `CRITICAL_SCRIPT_SANITY` no RULES.md.
- [x] **TASK-05**: Implementar política de edição cirúrgica obrigatória.

## 🏗️ Sprint 03: Runbook & Métricas Operacionais
- [ ] **TASK-06**: Inserir checklist anti-reincidência no MASTER_FLOW.md.
- [ ] **TASK-07**: Definir métricas mínimas por onda.
- [ ] **TASK-07A**: Adicionar checagem de ordem cronológica do `JOURNAL.md` como WARN (advisory, sem bloqueio).
- [ ] **TASK-07B**: Reforçar no checklist a disciplina de atualização do campo `updated` no `STATE.md` (sem gate duro).
- [ ] **TASK-07C**: Iniciar emissão de eventos `[GOVERNANCE-FRICTION]` em modo advisory no `HARNESS_LOG.md`.

## 🏗️ Sprint 04: Sincronização Institucional
- [ ] **TASK-08**: Atualizar HARNESS_REGISTRY.md e glossários (Script/File).
- [ ] **TASK-09**: Atualizar PROMPT_LIBRARY.md.

## 🏗️ Sprint 05: Enforcement Automático (Músculos)
- [ ] **TASK-10**: Implementar validação automática em `validate_context.py`.
- [ ] **TASK-11**: Adicionar testes de não regressão em `tests/test_context.py`.

## 🏗️ Sprint 06: Hardening de Agenciamento (Nervos)
- [ ] **TASK-12**: Atualizar papéis spec-driver e qa-validator com protocolo Hardened Closing.
- [ ] **TASK-13**: Implementar transição atômica para `IN_PROGRESS` via código.

## 🏗️ Sprint 07: Hardening SAM & Telemetria
- [ ] **TASK-14**: Implementar detecção de fraude narrativa no `workflow_journal_auditor.py`.
- [ ] **TASK-15**: Implantar schema de telemetria `[GOVERNANCE-FRICTION]`.
- [ ] **TASK-16**: Atualizar AGENT_REGISTRY.md.

## 🏗️ Sprint 08: Visão: RX Communications
- [ ] **TASK-17**: Criar `.context/maintenance/rx-communications.md`.
- [ ] **TASK-18**: Referenciar explicitamente no MASTER_FLOW.md e FILE_GLOSSARY.md.
