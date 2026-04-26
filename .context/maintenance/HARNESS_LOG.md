---
Criado em: 2026-04-24 15:20
Ultima Atualizacao: 2026-04-24 15:20
Status: Ativo
---

# HARNESS_LOG.md
> Log tecnico automatico do Harness (PASS/FAIL).

## [HARNESS-FAIL] Report | spec:synapse_workflow
- **Detalhe:** journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...
[INFO] Regra 'new_context_path' disparada.
[INFO] Regra 'rules_change' disparada.

❌ VIOLAÇÕES DETECTADAS:
  - Regra 'new_context_path': Arquivo '.context/maintenance/rx-anatomy.md' não foi propagado (ausente no diff).
  - Regra 'new_context_path': Checkbox [x] para '.context/maintenance/rx-anatomy.md' ausente ou desmarcado no Journal.
  - Regra 'rules_change': Tag 'Regras' ausente no Journal.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-FAIL] Report | spec:synapse_workflow
- **Detalhe:** journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...
[INFO] Regra 'new_context_path' disparada.
[INFO] Regra 'rules_change' disparada.

❌ VIOLAÇÕES DETECTADAS:
  - Regra 'rules_change': Tag 'Regras' ausente no Journal.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-PASS] Report | spec:synapse_workflow
- **Detalhe:** All contracts valid

## [HARNESS-FAIL] Report | spec:synapse_workflow
- **Detalhe:** handoff: Handoffs malformados: ['Handoff incompleto: ** @user -> @antigravity-agent'] | journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...
[INFO] Regra 'new_context_path' disparada.

❌ VIOLAÇÕES DETECTADAS:
  - Regra 'new_context_path': Arquivo '.context/maintenance/rx-anatomy.md' não foi propagado (ausente no diff).
  - Regra 'new_context_path': Checkbox [x] para '.context/maintenance/rx-anatomy.md' ausente ou desmarcado no Journal.
  - Contrato incompleto. Detectado: executor='', validator=''.
  - Status de validação inválido: ''. Esperado 'READY TO COMMIT'.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-FAIL] Report | spec:synapse_workflow
- **Detalhe:** journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...
[INFO] Regra 'new_context_path' disparada.

❌ VIOLAÇÕES DETECTADAS:
  - Regra 'new_context_path': Arquivo '.context/maintenance/rx-anatomy.md' não foi propagado (ausente no diff).
  - Regra 'new_context_path': Checkbox [x] para '.context/maintenance/rx-anatomy.md' ausente ou desmarcado no Journal.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-PASS] Report | spec:synapse_workflow
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:synapse_workflow
- **Detalhe:** All contracts valid
