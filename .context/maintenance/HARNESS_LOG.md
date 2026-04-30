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

## [HARNESS-FAIL] Report | spec:synapse_workflow
- **Detalhe:** journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...

❌ VIOLAÇÕES DETECTADAS:
  - Contrato incompleto. Detectado: executor='', validator=''.
  - Status de validação inválido: ''. Esperado 'READY TO COMMIT'.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-PASS] Report | spec:synapse_workflow
- **Detalhe:** All contracts valid

## [HARNESS-FAIL] Report | spec:synapse_workflow
- **Detalhe:** journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...

❌ VIOLAÇÕES DETECTADAS:
  - Contrato incompleto. Detectado: executor='', validator=''.
  - Status de validação inválido: '** [CONSISTENT & HARDENED]'. Esperado 'READY TO COMMIT'.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-FAIL] Report | spec:sam_chronology_fix
- **Detalhe:** sprint_contract: Contrato não assinado pelo @qa-validator (qa_signoff: false)

## [HARNESS-FAIL] Report | spec:sam_chronology_fix
- **Detalhe:** sprint_contract: Campo signed_by inválido ou ausente

## [HARNESS-PASS] Report | spec:sam_chronology_fix
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:qa_subagent
- **Detalhe:** All contracts valid

## [HARNESS-FAIL] Report | spec:qa_subagent
- **Detalhe:** journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...
[INFO] Regra 'new_context_path' disparada.

❌ VIOLAÇÕES DETECTADAS:
  - Regra 'new_context_path': Arquivo '.context/maintenance/rx-anatomy.md' não foi propagado (ausente no diff).
  - Regra 'new_context_path': Checkbox [x] para '.context/maintenance/rx-anatomy.md' ausente ou desmarcado no Journal.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-PASS] Report | spec:qa_subagent
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:qa_subagent
- **Detalhe:** All contracts valid

## [HARNESS-FAIL] Report | spec:multi_agent_choreography
- **Detalhe:** sprint_contract: Contrato não assinado pelo @qa-validator (qa_signoff: false) | impact_radius: Raio de impacto excedido! (Modificados: 6 > Limite: 5). Re-fragmente a SPEC ou aumente o limite se justificado. | journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...
[INFO] Regra 'rules_change' disparada.

❌ VIOLAÇÕES DETECTADAS:
  - Regra 'rules_change': Tag 'Governança' ausente no Journal.
  - Regra 'rules_change': Tag 'Regras' ausente no Journal.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-PASS] Report | spec:multi_agent_choreography
- **Detalhe:** All contracts valid

## [HARNESS-FAIL] Report | spec:multi_agent_choreography
- **Detalhe:** impact_radius: Raio de impacto excedido! (Modificados: 11 > Limite: 7). Re-fragmente a SPEC ou aumente o limite se justificado. | journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...
[INFO] Regra 'rules_change' disparada.

❌ VIOLAÇÕES DETECTADAS:
  - Regra 'rules_change': Tag 'Regras' ausente no Journal.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-PASS] Report | spec:multi_agent_choreography
- **Detalhe:** All contracts valid

## [HARNESS-FAIL] Report | spec:oracle_v3
- **Detalhe:** sprint_contract: Contrato não assinado pelo @qa-validator (qa_signoff: false) | impact_radius: Raio de impacto excedido! (Modificados: 8 > Limite: 6). Re-fragmente a SPEC ou aumente o limite se justificado. | journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...
[INFO] Regra 'new_context_path' disparada.

❌ VIOLAÇÕES DETECTADAS:
  - Regra 'new_context_path': Arquivo '.context/maintenance/rx-anatomy.md' não foi propagado (ausente no diff).
  - Regra 'new_context_path': Checkbox [x] para '.context/maintenance/rx-anatomy.md' ausente ou desmarcado no Journal.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-FAIL] Report | spec:oracle_v3
- **Detalhe:** sprint_contract: Contrato não assinado pelo @qa-validator (qa_signoff: false) | impact_radius: Raio de impacto excedido! (Modificados: 9 > Limite: 6). Re-fragmente a SPEC ou aumente o limite se justificado. | journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...
[INFO] Regra 'new_context_path' disparada.

❌ VIOLAÇÕES DETECTADAS:
  - Regra 'new_context_path': Arquivo '.context/maintenance/rx-anatomy.md' não foi propagado (ausente no diff).
  - Regra 'new_context_path': Checkbox [x] para '.context/maintenance/rx-anatomy.md' ausente ou desmarcado no Journal.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-FAIL] Report | spec:oracle_v3
- **Detalhe:** handoff: Handoffs malformados: ['Handoff incompleto: ** @flash -> @user | Estado: S'] | impact_radius: Raio de impacto excedido! (Modificados: 29 > Limite: 10). Re-fragmente a SPEC ou aumente o limite se justificado.

## [HARNESS-FAIL] Report | spec:oracle_v3
- **Detalhe:** handoff: Handoffs malformados: ['Handoff incompleto: ** @flash -> @user | Estado: S']

## [HARNESS-PASS] Report | spec:oracle_v3
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:oracle_v3
- **Detalhe:** All contracts valid

## [HARNESS-FAIL] Report | spec:oracle_v3
- **Detalhe:** journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...

❌ VIOLAÇÕES DETECTADAS:
  - Contrato incompleto. Detectado: executor='', validator=''.
  - Status de validação inválido: ''. Esperado 'READY TO COMMIT'.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-PASS] Report | spec:oracle_v3
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:oracle_v3
- **Detalhe:** All contracts valid

## [HARNESS-FAIL] Report | spec:contract_sprints_v2_safe
- **Detalhe:** sprint_contract: Contrato standard não assinado pelo @qa-validator (qa_signoff: false)

## [HARNESS-PASS] Report | spec:test_sprint
- **Detalhe:** All contracts valid

## [HARNESS-FAIL] Report | spec:test_sprint
- **Detalhe:** sprint_contract: [HG04] Sprint ativa (sprint_02) não possui signoff do @qa-validator no contrato

## [HARNESS-FAIL] Report | spec:contract_sprints_v2_safe
- **Detalhe:** sprint_contract: [HG07] Violação de Whitelist: Arquivo 'planos/mudanca_specdriven.md' não autorizado para esta missão.

## [HARNESS-FAIL] Report | spec:contract_sprints_v2_safe
- **Detalhe:** sprint_contract: [HG01] Violação de Escopo: Arquivo '.context/maintenance/HARNESS_LOG.md' fora da whitelist da sprint (sprint_01).

## [HARNESS-FAIL] Report | spec:contract_sprints_v2_safe
- **Detalhe:** sprint_contract: [HG01] Violação de Escopo: Arquivo 'planos/mudanca_specdriven.md' fora da whitelist da sprint (sprint_01).

## [HARNESS-PASS] Report | spec:contract_sprints_v2_safe
- **Detalhe:** All contracts valid

## [HARNESS-FAIL] Report | spec:contract_sprints_v2_safe
- **Detalhe:** sprint_contract: [HG07] Violação de Whitelist Operacional: Arquivo 'planos/mudanca_specdriven.md' proibido nesta missão.

## [HARNESS-FAIL] Report | spec:contract_sprints_v2_safe
- **Detalhe:** sprint_contract: [HG06] start_hash não encontrado para sprint_01 no STATE.md (Formato esperado: ## sprint_01 
 start_hash: ...)

## [HARNESS-FAIL] Report | spec:contract_sprints_v2_safe
- **Detalhe:** sprint_contract: [HG01] Violação de Escopo Sprint: Arquivo '.specs/features/contract_sprints_v2_safe/STATE.md' fora do planejado para sprint_01.

## [HARNESS-FAIL] Report | spec:contract_sprints_v2_safe
- **Detalhe:** sprint_contract: [HG01] Violação de Escopo Sprint: Arquivo '.specs/features/contract_sprints_v2_safe/spec.md' fora do planejado para sprint_01.

## [HARNESS-FAIL] Report | spec:contract_sprints_v2_safe
- **Detalhe:** sprint_contract: [HG01] Violação de Escopo Sprint: Arquivo '.specs/features/contract_sprints_v2_safe/tasks.md' fora do planejado para sprint_01.

## [HARNESS-PASS] Report | spec:contract_sprints_v2_safe
- **Detalhe:** All contracts valid

## [HARNESS-FAIL] Report | spec:contract_sprints_v2_safe
- **Detalhe:** sprint_contract: [HG07] Violação de Whitelist Operacional: Arquivo 'planos/mudanca_specdriven.md' proibido nesta missão.

## [HARNESS-FAIL] Report | spec:contract_sprints_v2_safe
- **Detalhe:** sprint_contract: [HG07] Violação de Whitelist Operacional: Arquivo 'planos/mudanca_specdriven/mudanca_specdriven.md' proibido nesta missão.

## [HARNESS-FAIL] Report | spec:contract_sprints_v2_safe
- **Detalhe:** sprint_contract: [HG07] Violação de Whitelist Operacional: Arquivo 'planos/mudanca_specdriven/relatorio_auditoria_contract_sprints.md' proibido nesta missão.

## [HARNESS-FAIL] Report | spec:contract_sprints_v2_safe
- **Detalhe:** sprint_contract: [HG01] Violação de Escopo Sprint: Arquivo 'planos/mudanca_specdriven/mudanca_specdriven.md' fora do planejado para sprint_01.

## [HARNESS-FAIL] Report | spec:contract_sprints_v2_safe
- **Detalhe:** sprint_contract: [HG01] Violação de Escopo Sprint: Arquivo 'planos/mudanca_specdriven/mudanca_specdriven.md' fora do planejado para sprint_01.

## [HARNESS-PASS] Report | spec:contract_sprints_v2_safe
- **Detalhe:** All contracts valid

## [HARNESS-FAIL] Report | spec:contract_sprints_v2_safe
- **Detalhe:** sprint_contract: [HG07] Violação de Whitelist Operacional: Arquivo 'planos/mudanca_specdriven.md' proibido nesta missão.

## [HARNESS-FAIL] Report | spec:contract_sprints_v2_safe
- **Detalhe:** sprint_contract: [HG06] Start_hash inválido ou não resolvível: d9225d61486791e813f019a552805ef96e1a49f5

## [HARNESS-PASS] Report | spec:contract_sprints_v2_safe
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:contract_sprints_v2_safe
- **Detalhe:** All contracts valid

## [HARNESS-FAIL] Report | spec:contract_sprints_v2_safe
- **Detalhe:** sprint_contract: [HG06] Start_hash inválido ou não resolvível: ca3e14811f0627e942a49c8ffbcd0aec71e04ea2a

## [HARNESS-FAIL] Report | spec:contract_sprints_v2_safe
- **Detalhe:** sprint_contract: [HG01] Violação de Escopo Sprint: Arquivo '.context/maintenance/HARNESS_LOG.md' fora do planejado para sprint_03.

## [HARNESS-PASS] Report | spec:contract_sprints_v2_safe
- **Detalhe:** All contracts valid

## [HARNESS-FAIL] Report | spec:contract_sprints_v2_safe
- **Detalhe:** sprint_contract: [HG01] Violação de Escopo Sprint: Arquivo '.context/_scripts/harness_runner.py' fora do planejado para sprint_03.

## [HARNESS-FAIL] Report | spec:contract_sprints_v2_safe
- **Detalhe:** sprint_contract: [HG04] Bloqueio Final: A última sprint deve ter signoff interno antes do signoff global.

## [HARNESS-PASS] Report | spec:contract_sprints_v2_safe
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:contract_sprints_v2_safe
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:contract_sprints_v2_safe
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:contract_sprints_v2_safe
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:contract_sprints_v2_safe
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:contract_sprints_v2_safe
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:contract_sprints_v2_safe
- **Detalhe:** All contracts valid
