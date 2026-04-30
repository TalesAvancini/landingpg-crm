---
type: standard
executor_context_id: "CTX_FLASH_SAM_FIX"
validator_context_id: "CTX_QA_AUDIT_FINAL"
qa_signoff: true
signed_by: "@qa-validator"
definition_of_done:
  - Criar JOURNAL_SYNAPSE.md contendo bloco JSON nativo e tabela de humanos (sem pyyaml).
  - Implementar comando `workflow-journal` em run_context.py cruzando Git diff, Synapse (JSON) e Journal.
  - Integrar checagem no harness_runner.py para bloquear falhas de contrato.
  - Implementar modos shadow/assist/strict (apenas strict veta o commit).
  - Segregação de contexto obrigatória no strict (`executor_context_id` != `validator_context_id`).
  - Atualizar RULES.md e MASTER_FLOW.md incorporando `journal_mode: strict`.
  - Criar script npm `context:workflow-journal`.
  - Passar nos 6 cenários de teste MVP com evidência de saída.
---

# Feature: Sistema Anti-Migué (Synapse + workflow_Journal)

**Objetivo:** Eliminar o viés de leniência da IA forçando um circuito fechado entre Intenção (Journal), Obrigação (Synapse) e Realidade (Git). O Validador autônomo é o único que pode aprovar o merge.

**Condição Obrigatória:**
- O arquivo parseável Synapse deve usar JSON embutido no `JOURNAL_SYNAPSE.md` (cercado pelas tags `<!-- SYNAPSE_JSON_START -->` e `<!-- SYNAPSE_JSON_END -->`). Sem dependências externas como pyyaml (stdlib-only).

**Escopo Confirmado:**
1) Comando `workflow-journal` no run_context.py + script npm.
2) Check no `harness_runner.py` cruzando Journal + Synapse(JSON) + git diff.
3) Modos shadow/assist/strict.
4) Segregação `executor_context_id != validator_context_id` na validação de contrato strict.
5) Testes MVP (6 cenários pass/fail) com evidências.

**Artefatos Modificados (Previstos):**
- `run_context.py`
- `.context/_scripts/harness_runner.py`
- `.context/brain/RULES.md`
- `.context/brain/MASTER_FLOW.md`
- `.context/maintenance/JOURNAL.md`
- `package.json`
