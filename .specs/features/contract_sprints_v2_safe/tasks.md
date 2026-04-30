# ✅ Tasks: Evolução Contract Sprints

## 🏗️ Onda 1: Contrato e Template (Fase A)
- [x] **TASK-01 (A1)**: Atualizar `.specs/_template.md` para suportar dual mode (Standard/Sprint-based).
- [x] **TASK-02 (A2)**: Incluir exemplo sprint-based mínimo válido no template.
- [x] **TASK-03 (A3)**: Documentar obrigatoriedade de `scope_allow/scope_deny` no template.
- [x] **Verify A**: Validar que o parser atual do framework não quebra com o novo template.

## 💻 Onda 2: Harness Runner (Fase B)
- [x] **TASK-04 (B1)**: Implementar detector de modo no `harness_runner.py`.
- [x] **TASK-05 (B2)**: Encapsular validação `standard` em função dedicada.
- [x] **TASK-06 (B3)**: Criar validador estrutural sprint-based.
- [x] **TASK-07 (B4)**: Implementar engine de Hard/Soft gates (HG01-07, SG01-05).
- [x] **HARDENING (B-Pass)**: 
  - [x] Corrigir parser de start_hash para headings Markdown.
  - [x] Flexibilizar HG04 para sprint ativa.
  - [x] Sincronizar Whitelist (Remover legado).
  - [x] Normalização total MiMo no STATE.md.
  - [x] Consolidação Git (Add baseline).
- [x] **Verify B**: Auditoria Codex validada com sucesso.

## 🧪 Onda 3: QA Validator (Fase C)
- [x] **TASK-08 (C1)**: Revisar prompt do subagente para checkpoint incremental.
- [x] **TASK-C2**: Implementar bloqueio de `feature_done` global sem signoff de sprint (C2).
- [x] **Verify C**: Teste de migué e assinatura parcial validado.

## 📊 Onda 4: Impacto Incremental (Fase D)
- [x] **TASK-09 (D1)**: Captura de `start_hash` no início da sprint.
- [x] **TASK-10 (D2)**: Implementar diff incremental (`start_hash..HEAD`).
- [x] **Verify D**: Teste de métricas de churn por sprint validado.

## 🧹 Onda 5: Higiene & SAM (Fase E)
- [x] **TASK-11 (E1)**: Adaptar `cleanup_specs.py` (proteger sprint ativa).
- [x] **TASK-12 (E3)**: Atualizar documentação SSOT (MASTER_FLOW, RULES).
- [x] **Verify E**: Pipeline completo sem regressão.

---
**MISSÃO CONCLUÍDA: H.O.K FORGE v2.5.2 HARDENED**
