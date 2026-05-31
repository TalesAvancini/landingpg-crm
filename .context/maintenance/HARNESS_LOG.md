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

## [HARNESS-PASS] Report | spec:contract_sprints_v2_safe
- **Detalhe:** All contracts valid

## [HARNESS-FAIL] Report | spec:contract_sprints_v2_safe
- **Detalhe:** sprint_contract: [HG07] Violação de Whitelist Operacional: Arquivo '.context/brain/RULES.md' proibido nesta missão. | journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...
[INFO] Regra 'rules_change' disparada.

❌ VIOLAÇÕES DETECTADAS:
  - Regra 'rules_change': Tag 'Regras' ausente no Journal.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-FAIL] Report | spec:contract_sprints_v2_safe
- **Detalhe:** sprint_contract: [HG01] Violação de Escopo Sprint: Arquivo '.context/_scripts/harness_runner.py' fora do planejado para sprint_05.

## [HARNESS-FAIL] Report | spec:contract_sprints_v2_safe
- **Detalhe:** sprint_contract: [HG01] Violação de Escopo Sprint: Arquivo '.context/maintenance/JOURNAL.md' fora do planejado para sprint_05.

## [HARNESS-PASS] Report | spec:contract_sprints_v2_safe
- **Detalhe:** All contracts valid

## [HARNESS-FAIL] Report | spec:contract_sprints_v2_safe
- **Detalhe:** sprint_contract: [HG06] Start_hash inválido ou não resolvível: dece4ab578453483b8b152d1921f00a5d290744e

## [HARNESS-PASS] Report | spec:contract_sprints_v2_safe
- **Detalhe:** All contracts valid

## [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:34
- **Detalhe:** Inversão detectada: 2026-04-30 03:40 aparece após 2026-04-30 18:55

## [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:34
- **Detalhe:** Inversão detectada: 2026-04-30 02:45 aparece após 2026-04-30 03:40

## [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:34
- **Detalhe:** Inversão detectada: 2026-04-30 00:15 aparece após 2026-04-30 02:45

## [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:34
- **Detalhe:** Inversão detectada: 2026-04-29 01:35 aparece após 2026-04-30 00:15

## [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:34
- **Detalhe:** Inversão detectada: 2026-04-28 23:55 aparece após 2026-04-29 01:35

## [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:34
- **Detalhe:** Inversão detectada: 2026-04-28 23:45 aparece após 2026-04-28 23:55

## [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:34
- **Detalhe:** Inversão detectada: 2026-04-28 23:00 aparece após 2026-04-28 23:45

## [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:34
- **Detalhe:** Inversão detectada: 2026-04-26 23:58 aparece após 2026-04-28 23:00

## [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:34
- **Detalhe:** Inversão detectada: 2026-04-26 17:30 aparece após 2026-04-26 23:58

## [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:34
- **Detalhe:** Inversão detectada: 2026-04-26 17:20 aparece após 2026-04-26 17:30

## [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:34
- **Detalhe:** Inversão detectada: 2026-04-26 17:00 aparece após 2026-04-26 17:20

## [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:34
- **Detalhe:** Inversão detectada: 2026-04-26 16:30 aparece após 2026-04-26 17:00

## [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:34
- **Detalhe:** Inversão detectada: 2026-04-26 15:30 aparece após 2026-04-26 16:30

## [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:34
- **Detalhe:** Inversão detectada: 2026-04-26 14:20 aparece após 2026-04-26 15:30

## [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:34
- **Detalhe:** Inversão detectada: 2026-04-26 01:32 aparece após 2026-04-26 14:20

## [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:34
- **Detalhe:** Inversão detectada: 2026-04-26 01:18 aparece após 2026-04-26 01:32

## [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:34
- **Detalhe:** Inversão detectada: 2026-04-26 00:54 aparece após 2026-04-26 01:18

## [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:34
- **Detalhe:** Inversão detectada: 2026-04-26 00:08 aparece após 2026-04-26 00:54

## [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:34
- **Detalhe:** Inversão detectada: 2026-04-24 15:20 aparece após 2026-04-26 00:08

## [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:34
- **Detalhe:** Inversão detectada: 2026-04-24 13:52 aparece após 2026-04-24 15:20

## [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:34
- **Detalhe:** Inversão detectada: 2026-04-23 22:20 aparece após 2026-04-24 13:52

## [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:34
- **Detalhe:** Inversão detectada: 2026-04-22 09:50 aparece após 2026-04-23 22:20

## [GOVERNANCE-FRICTION] GF-STATE-FRESHNESS | 2026-04-30 22:34
- **Detalhe:** contract_sprints_v2_safe: status desatualizado (2026-04-30 18:57 < 2026-04-30 22:34)

## [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:35
- **Detalhe:** Inversão detectada: 2026-04-30 03:40 aparece após 2026-04-30 18:55

## [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:35
- **Detalhe:** Inversão detectada: 2026-04-30 02:45 aparece após 2026-04-30 03:40

## [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:35
- **Detalhe:** Inversão detectada: 2026-04-30 00:15 aparece após 2026-04-30 02:45

## [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:35
- **Detalhe:** Inversão detectada: 2026-04-29 01:35 aparece após 2026-04-30 00:15

## [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:35
- **Detalhe:** Inversão detectada: 2026-04-28 23:55 aparece após 2026-04-29 01:35

## [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:35
- **Detalhe:** Inversão detectada: 2026-04-28 23:45 aparece após 2026-04-28 23:55

## [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:35
- **Detalhe:** Inversão detectada: 2026-04-28 23:00 aparece após 2026-04-28 23:45

## [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:35
- **Detalhe:** Inversão detectada: 2026-04-26 23:58 aparece após 2026-04-28 23:00

## [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:35
- **Detalhe:** Inversão detectada: 2026-04-26 17:30 aparece após 2026-04-26 23:58

## [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:35
- **Detalhe:** Inversão detectada: 2026-04-26 17:20 aparece após 2026-04-26 17:30

## [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:35
- **Detalhe:** Inversão detectada: 2026-04-26 17:00 aparece após 2026-04-26 17:20

## [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:35
- **Detalhe:** Inversão detectada: 2026-04-26 16:30 aparece após 2026-04-26 17:00

## [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:35
- **Detalhe:** Inversão detectada: 2026-04-26 15:30 aparece após 2026-04-26 16:30

## [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:35
- **Detalhe:** Inversão detectada: 2026-04-26 14:20 aparece após 2026-04-26 15:30

## [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:35
- **Detalhe:** Inversão detectada: 2026-04-26 01:32 aparece após 2026-04-26 14:20

## [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:35
- **Detalhe:** Inversão detectada: 2026-04-26 01:18 aparece após 2026-04-26 01:32

## [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:35
- **Detalhe:** Inversão detectada: 2026-04-26 00:54 aparece após 2026-04-26 01:18

## [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:35
- **Detalhe:** Inversão detectada: 2026-04-26 00:08 aparece após 2026-04-26 00:54

## [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:35
- **Detalhe:** Inversão detectada: 2026-04-24 15:20 aparece após 2026-04-26 00:08

## [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:35
- **Detalhe:** Inversão detectada: 2026-04-24 13:52 aparece após 2026-04-24 15:20

## [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:35
- **Detalhe:** Inversão detectada: 2026-04-23 22:20 aparece após 2026-04-24 13:52

## [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:35
- **Detalhe:** Inversão detectada: 2026-04-22 09:50 aparece após 2026-04-23 22:20

## [GOVERNANCE-FRICTION] GF-STATE-FRESHNESS | 2026-04-30 22:35
- **Detalhe:** contract_sprints_v2_safe: status desatualizado (2026-04-30 18:57 < 2026-04-30 22:35)

## [HARNESS-FAIL] Report | spec:gov_chain_v3_phase2_dryrun
- **Detalhe:** handoff: Handoffs malformados: ['Handoff incompleto: ** `@spec-driver` ⮕ `@qa-valid'] | sprint_contract: [HG03] Modo sprint_based exige campo current_sprint | journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...
[INFO] Regra 'new_context_path' disparada.

❌ VIOLAÇÕES DETECTADAS:
  - Regra 'new_context_path': Arquivo '.context/maintenance/rx-anatomy.md' não foi propagado (ausente no diff).
  - Regra 'new_context_path': Checkbox [x] para '.context/maintenance/rx-anatomy.md' ausente ou desmarcado no Journal.
  - Contrato incompleto. Detectado: executor='', validator=''.
  - Status de validação inválido: ''. Esperado 'READY TO COMMIT'.
  - Modificação Silenciosa: Arquivo 'SDD_Report.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.context/monitoring/PROJECT_INDEX.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo 'contexto_v2.5.2.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '_flash_report/log_extracao_v2.5.2.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo 'contexto_v2.5.2_toc.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo 'planos/SSD-Chain/chain_specdriver.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.context/_scripts/__pycache__/write_with_validation.cpython-314.pyc' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo 'planos/SSD-Chain/RAW_SSD-Chain.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.specs/features/gov_chain_v3_phase2_dryrun/STATE.md' alterado no Git mas ausente na Matriz de Propagação do Journal.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-FAIL] Report | spec:gov_chain_v3_phase2_dryrun
- **Detalhe:** handoff: Handoffs malformados: ['Handoff incompleto: ** `@spec-driver` ⮕ `@qa-valid'] | sprint_contract: [HG03] Modo sprint_based exige campo current_sprint | journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...
[INFO] Regra 'new_context_path' disparada.

❌ VIOLAÇÕES DETECTADAS:
  - Regra 'new_context_path': Arquivo '.context/maintenance/rx-anatomy.md' não foi propagado (ausente no diff).
  - Regra 'new_context_path': Checkbox [x] para '.context/maintenance/rx-anatomy.md' ausente ou desmarcado no Journal.
  - Contrato incompleto. Detectado: executor='', validator=''.
  - Fraude Narrativa: Arquivo 'scratch/dummy_test.txt' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo '.specs/features/gov_chain_v3_phase2_dryrun/tasks.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Modificação Silenciosa: Arquivo '.context/monitoring/PROJECT_INDEX.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo 'contexto_v2.5.2_toc.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo 'planos/SSD-Chain/RAW_SSD-Chain.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo 'planos/SSD-Chain/chain_specdriver.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo 'SDD_Report.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo 'contexto_v2.5.2.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.context/_scripts/__pycache__/write_with_validation.cpython-314.pyc' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '_flash_report/log_extracao_v2.5.2.md' alterado no Git mas ausente na Matriz de Propagação do Journal.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-FAIL] Report | spec:gov_chain_v3_phase2_dryrun
- **Detalhe:** handoff: Handoffs malformados: ['Handoff incompleto: ** `@spec-driver` ⮕ `@qa-valid'] | sprint_contract: [HG03] Modo sprint_based exige campo current_sprint | journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...
[INFO] Regra 'new_context_path' disparada.

❌ VIOLAÇÕES DETECTADAS:
  - Regra 'new_context_path': Arquivo '.context/maintenance/rx-anatomy.md' não foi propagado (ausente no diff).
  - Regra 'new_context_path': Checkbox [x] para '.context/maintenance/rx-anatomy.md' ausente ou desmarcado no Journal.
  - Contrato incompleto. Detectado: executor='', validator=''.
  - Fraude Narrativa: Arquivo 'scratch/dummy_test.txt' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo '.specs/features/gov_chain_v3_phase2_dryrun/tasks.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Modificação Silenciosa: Arquivo '.context/_scripts/__pycache__/write_with_validation.cpython-314.pyc' alterado no Git mas ausente na Matriz de Propagação do Journal.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-FAIL] Report | spec:gov_chain_v3_phase2_dryrun
- **Detalhe:** handoff: Handoffs malformados: ['Handoff incompleto: ** `@spec-driver` ⮕ `@qa-valid'] | sprint_contract: [HG03] Modo sprint_based exige campo current_sprint | journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...
[INFO] Regra 'new_context_path' disparada.

❌ VIOLAÇÕES DETECTADAS:
  - Regra 'new_context_path': Arquivo '.context/maintenance/rx-anatomy.md' não foi propagado (ausente no diff).
  - Regra 'new_context_path': Checkbox [x] para '.context/maintenance/rx-anatomy.md' ausente ou desmarcado no Journal.
  - Contrato incompleto. Detectado: executor='', validator=''.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-FAIL] Report | spec:gov_chain_v3_phase2_dryrun
- **Detalhe:** handoff: Handoffs malformados: ['Handoff incompleto: ** `@spec-driver` ⮕ `@qa-valid'] | sprint_contract: Contrato standard não assinado pelo @qa-validator (qa_signoff: false) | journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...
[INFO] Regra 'new_context_path' disparada.

❌ VIOLAÇÕES DETECTADAS:
  - Regra 'new_context_path': Arquivo '.context/maintenance/rx-anatomy.md' não foi propagado (ausente no diff).
  - Regra 'new_context_path': Checkbox [x] para '.context/maintenance/rx-anatomy.md' ausente ou desmarcado no Journal.
  - Modificação Silenciosa: Arquivo '.specs/features/gov_chain_v3_phase2_dryrun/spec.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.context/_scripts/__pycache__/write_with_validation.cpython-314.pyc' alterado no Git mas ausente na Matriz de Propagação do Journal.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-FAIL] Report | spec:gov_chain_v3_phase2_dryrun
- **Detalhe:** handoff: Handoffs malformados: ['Handoff incompleto: ** `@spec-driver` ⮕ `@qa-valid'] | sprint_contract: Contrato standard não assinado pelo @qa-validator (qa_signoff: false)

## [HARNESS-FAIL] Report | spec:gov_chain_v3_phase2_dryrun
- **Detalhe:** handoff: Handoffs malformados: ['Handoff incompleto: ** `@spec-driver` ⮕ `@qa-valid'] | sprint_contract: Contrato standard não assinado pelo @qa-validator (qa_signoff: false)

## [HARNESS-FAIL] Report | spec:gov_chain_v3_phase2_dryrun
- **Detalhe:** sprint_contract: Contrato standard não assinado pelo @qa-validator (qa_signoff: false)

## [HARNESS-FAIL] Report | spec:gov_chain_v3_phase2_dryrun
- **Detalhe:** sprint_contract: Modo de contrato não identificado ou malformado

## [HARNESS-FAIL] Report | spec:gov_chain_v3_phase2_dryrun
- **Detalhe:** sprint_contract: [HG03] Modo sprint_based exige campo current_sprint

## [HARNESS-FAIL] Report | spec:gov_chain_v3_phase2_dryrun
- **Detalhe:** sprint_contract: [HG06] start_hash não encontrado para sprint_01 no STATE.md (Formato esperado: ## sprint_01 
 start_hash: ...)

## [HARNESS-FAIL] Report | spec:gov_chain_v3_phase2_dryrun
- **Detalhe:** sprint_contract: [HG01] Violação de Escopo Sprint: Arquivo '.context/maintenance/HARNESS_LOG.md' fora do planejado para sprint_01.

## [HARNESS-PASS] Report | spec:gov_chain_v3_phase2_dryrun
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:gov_chain_v3_phase2_dryrun
- **Detalhe:** All contracts valid

## [HARNESS-FAIL] Report | spec:gov_v3_stress_test
- **Detalhe:** sprint_contract: [HG06] start_hash não encontrado para sprint_01 no STATE.md (Formato esperado: ## sprint_01 
 start_hash: ...) | journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...

❌ VIOLAÇÕES DETECTADAS:
  - Fraude Narrativa: Arquivo '.specs/features/gov_v3_stress_test/spec.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo '.specs/features/gov_v3_stress_test/STATE.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo '.specs/features/gov_v3_stress_test/tasks.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Modificação Silenciosa: Arquivo 'planos/SSD-Chain/RAW_SSD-Chain.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.specs/features/gov_v3_stress_test/' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.context/monitoring/PROJECT_INDEX.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.gitignore' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo 'contexto_v2.5.2.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.agent/subagents/spec-driver.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.context/_scripts/write_with_validation.py' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo 'contexto_v2.5.2_toc.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo 'planos/SSD-Chain/chain_specdriver.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.agent/templates/' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo 'SDD_Report.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.specs/features/gov_chain_v3_phase2_dryrun/STATE.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '"planos/SSD-Chain/Chain-Skills V3.md"' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo 'scratch/dummy_test.txt' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '_flash_report/log_extracao_v2.5.2.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.specs/features/gov_chain_v3_phase2_dryrun/spec.md' alterado no Git mas ausente na Matriz de Propagação do Journal.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-FAIL] Report | spec:gov_v3_stress_test
- **Detalhe:** journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...

❌ VIOLAÇÕES DETECTADAS:
  - Modificação Silenciosa: Arquivo '.context/_scripts/write_with_validation.py' alterado no Git mas ausente na Matriz de Propagação do Journal.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-FAIL] Report | spec:gov_v3_stress_test
- **Detalhe:** sprint_contract: [HG06] start_hash não encontrado para sprint_01 no STATE.md (Formato esperado: ## sprint_01 
 start_hash: ...)

## [HARNESS-PASS] Report | spec:gov_v3_stress_test
- **Detalhe:** All contracts valid

## [HARNESS-FAIL] Report | spec:governance_rules_hardening
- **Detalhe:** sprint_contract: [HG04] Sprint anterior (sprint_06) pendente de signoff. Impossível avançar para sprint_08. | journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...

❌ VIOLAÇÕES DETECTADAS:
  - Fraude Narrativa: Arquivo '.context/maintenance/JOURNAL.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo '.context/brain/MASTER_FLOW.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo '.context/brain/RULES.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo 'VERSION.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Modificação Silenciosa: Arquivo 'README_CONTEXT.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.specs/features/SDD_ERRORS_LEDGER.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.specs/features/SSD_PLAYBOOK.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.specs/features/SSD_ERRORS_LEDGER.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.specs/features/_template_operacional_sprint/CHECKLIST.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.context/brain/AGENT_REGISTRY.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo 'init_ai_project.sh' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.specs/features/SDD_PLAYBOOK.md' alterado no Git mas ausente na Matriz de Propagação do Journal.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-FAIL] Report | spec:governance_rules_hardening
- **Detalhe:** sprint_contract: [HG04] Sprint anterior (sprint_06) pendente de signoff. Impossível avançar para sprint_08. | journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...

❌ VIOLAÇÕES DETECTADAS:
  - Modificação Silenciosa: Arquivo '.specs/features/SDD_ERRORS_LEDGER.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.specs/features/governance_rules_hardening/STATE.md' alterado no Git mas ausente na Matriz de Propagação do Journal.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-FAIL] Report | spec:contract_sprints_v2_safe
- **Detalhe:** sprint_contract: [HG07] Violação de Whitelist Operacional: Arquivo '.agent/skills/methodical_writer.json' proibido nesta missão. | journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...

❌ VIOLAÇÕES DETECTADAS:
  - Modificação Silenciosa: Arquivo '.specs/features/governance_rules_hardening/tasks.md -> .specs/features/_arquive_features/governance_rules_hardening/tasks.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.specs/features/governance_rules_hardening/design.md -> .specs/features/_arquive_features/governance_rules_hardening/design.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.specs/features/governance_rules_hardening/spec.md -> .specs/features/_arquive_features/governance_rules_hardening/spec.md' alterado no Git mas ausente na Matriz de Propagação do Journal.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-FAIL] Report | spec:contract_sprints_v2_safe
- **Detalhe:** sprint_contract: [HG07] Violação de Whitelist Operacional: Arquivo '.agent/skills/methodical_writer.json' proibido nesta missão. | journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...

❌ VIOLAÇÕES DETECTADAS:
  - Modificação Silenciosa: Arquivo '.specs/features/contract_sprints_v2_safe/STATE.md' alterado no Git mas ausente na Matriz de Propagação do Journal.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-FAIL] Report | spec:manual
- **Detalhe:** sprint_contract: Nenhuma Spec ativa detectada. | journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...

❌ VIOLAÇÕES DETECTADAS:
  - Fraude Narrativa: Arquivo 'init_ai_project.sh' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo '.specs/features/governance_rules_hardening/spec.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo '.context/brain/FILE_GLOSSARY.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo 'README_CONTEXT.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo '.context/brain/AGENT_REGISTRY.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo '.specs/features/SSD_ERRORS_LEDGER.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo '.specs/features/governance_rules_hardening/STATE.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo '.specs/features/SDD_ERRORS_LEDGER.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo '.specs/features/governance_rules_hardening/design.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo '.specs/features/governance_rules_hardening/tasks.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo '.specs/features/SDD_PLAYBOOK.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo '.specs/features/SSD_PLAYBOOK.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo '.specs/features/_template_operacional_sprint/CHECKLIST.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo '.context/maintenance/rx-anatomy.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Modificação Silenciosa: Arquivo '.context/maintenance/TECHNICAL_REQUIREMENTS.md' alterado no Git mas ausente na Matriz de Propagação do Journal.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-FAIL] Report | spec:manual
- **Detalhe:** sprint_contract: Nenhuma Spec ativa detectada. | journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...

❌ VIOLAÇÕES DETECTADAS:
  - Fraude Narrativa: Arquivo '.specs/features/governance_rules_hardening/tasks.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo '.specs/features/governance_rules_hardening/spec.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo '.specs/features/governance_rules_hardening/STATE.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo '.specs/features/SSD_PLAYBOOK.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo '.specs/features/SDD_ERRORS_LEDGER.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo '.context/brain/FILE_GLOSSARY.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo '.specs/features/SSD_ERRORS_LEDGER.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo '.context/brain/AGENT_REGISTRY.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo '.specs/features/SDD_PLAYBOOK.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo 'README_CONTEXT.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo '.specs/features/_template_operacional_sprint/CHECKLIST.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo 'init_ai_project.sh' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo '.context/maintenance/rx-anatomy.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo '.specs/features/governance_rules_hardening/design.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Modificação Silenciosa: Arquivo 'contexto_v2.5.2.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.agent/subagents/spec-driver.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo 'contexto_v2.5.2_toc.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.context/monitoring/PROJECT_INDEX.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.context/_scripts/write_with_validation.py' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.context/maintenance/TECHNICAL_REQUIREMENTS.md' alterado no Git mas ausente na Matriz de Propagação do Journal.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-FAIL] Report | spec:manual
- **Detalhe:** sprint_contract: Nenhuma Spec ativa detectada. | journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...

❌ VIOLAÇÕES DETECTADAS:
  - Modificação Silenciosa: Arquivo 'contexto_v2.5.2.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.context/maintenance/TECHNICAL_REQUIREMENTS.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.context/monitoring/PROJECT_INDEX.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo 'contexto_v2.5.2_toc.md' alterado no Git mas ausente na Matriz de Propagação do Journal.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-FAIL] Report | spec:manual
- **Detalhe:** sprint_contract: Nenhuma Spec ativa detectada. | journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...

❌ VIOLAÇÕES DETECTADAS:
  - Fraude Narrativa: Arquivo 'contexto_v2.5.2.md` / `contexto_v2.5.2_toc.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Modificação Silenciosa: Arquivo 'contexto_v2.5.2.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo 'contexto_v2.5.2_toc.md' alterado no Git mas ausente na Matriz de Propagação do Journal.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-FAIL] Report | spec:manual
- **Detalhe:** sprint_contract: Nenhuma Spec ativa detectada.

## [HARNESS-FAIL] Report | spec:gov_v3_stabilization
- **Detalhe:** sprint_contract: Bloco de contrato (---) ausente no topo da spec | journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...

❌ VIOLAÇÕES DETECTADAS:
  - Modificação Silenciosa: Arquivo '.specs/features/SSD_ERRORS_LEDGER.md' alterado no Git mas ausente na Matriz de Propagação do Journal.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-FAIL] Report | spec:gov_v3_stabilization
- **Detalhe:** sprint_contract: Modo de contrato não identificado ou malformado

## [HARNESS-FAIL] Report | spec:gov_v3_stabilization
- **Detalhe:** sprint_contract: Campo definition_of_done obrigatório

## [HARNESS-FAIL] Report | spec:gov_v3_stabilization
- **Detalhe:** sprint_contract: Contrato standard não assinado pelo @qa-validator (qa_signoff: false)

## [HARNESS-FAIL] Report | spec:gov_v3_stabilization
- **Detalhe:** sprint_contract: Campo signed_by inválido ou ausente

## [HARNESS-FAIL] Report | spec:gov_v3_stabilization
- **Detalhe:** sprint_contract: Spec standard requer context_ids preenchidos

## [HARNESS-PASS] Report | spec:gov_v3_stabilization
- **Detalhe:** All contracts valid

## [HARNESS-FAIL] Report | spec:gov_v3_stabilization
- **Detalhe:** journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...
[INFO] Regra 'new_context_path' disparada.

❌ VIOLAÇÕES DETECTADAS:
  - Regra 'new_context_path': Arquivo '.context/maintenance/rx-anatomy.md' não foi propagado (ausente no diff).
  - Regra 'new_context_path': Checkbox [x] para '.context/maintenance/rx-anatomy.md' ausente ou desmarcado no Journal.
  - Modificação Silenciosa: Arquivo '.context/_scripts/inject_learnings.py' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo 'planos/Learnnings/' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.context/brain/LEARNINGS.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.context/maintenance/TECHNICAL_REQUIREMENTS.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.context/_scripts/learnings_aggregator.py' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo 'planos/MiMo_Learnings_Consolidado.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.specs/features/gov_v3_stabilization/.enriched.md' alterado no Git mas ausente na Matriz de Propagação do Journal.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-FAIL] Report | spec:gov_v3_stabilization
- **Detalhe:** journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...
[INFO] Regra 'new_context_path' disparada.

❌ VIOLAÇÕES DETECTADAS:
  - Regra 'new_context_path': Arquivo '.context/maintenance/rx-anatomy.md' não foi propagado (ausente no diff).
  - Regra 'new_context_path': Checkbox [x] para '.context/maintenance/rx-anatomy.md' ausente ou desmarcado no Journal.
  - Contrato incompleto. Detectado: executor='', validator=''.
  - Status de validação inválido: ''. Esperado 'READY TO COMMIT'.
  - Fraude Narrativa: Arquivo 'planos/Learnnings/Learnings_MiMo_v2.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Modificação Silenciosa: Arquivo '.context/brain/SCRIPT_GLOSSARY.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.context/_scripts/validate_commit_msg.py' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.context/brain/FILE_GLOSSARY.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo 'run_context.py' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo 'planos/Learnnings/' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.specs/features/SSD_ERRORS_LEDGER.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.specs/features/gov_v3_stabilization/STATE.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.husky/commit-msg' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.specs/features/SSD_PLAYBOOK.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo 'package.json' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.context/maintenance/TECHNICAL_REQUIREMENTS.md' alterado no Git mas ausente na Matriz de Propagação do Journal.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-FAIL] Report | spec:gov_v3_stabilization
- **Detalhe:** journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...

❌ VIOLAÇÕES DETECTADAS:
  - Contrato incompleto. Detectado: executor='', validator=''.
  - Status de validação inválido: ''. Esperado 'READY TO COMMIT'.
  - Fraude Narrativa: Arquivo '.context/_scripts/inject_learnings.py' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo 'planos/MiMo_Learnings_Consolidado.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo '.specs/features/gov_v3_stabilization/.enriched.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo '.context/maintenance/JOURNAL.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo '.context/_scripts/learnings_aggregator.py' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo 'planos/Learnnings/Learnings_MiMo_v2.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Modificação Silenciosa: Arquivo '.context/maintenance/TECHNICAL_REQUIREMENTS.md' alterado no Git mas ausente na Matriz de Propagação do Journal.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-FAIL] Report | spec:blast_radius_mvp
- **Detalhe:** sprint_contract: [HG06] start_hash não encontrado para sprint_01 no STATE.md (Formato esperado: ## sprint_01 
 start_hash: ...) | journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...
[INFO] Regra 'roles_registry_change' disparada.
[INFO] Regra 'new_context_path' disparada.

❌ VIOLAÇÕES DETECTADAS:
  - Regra 'roles_registry_change': Tag 'Roles' ausente no Journal.
  - Regra 'roles_registry_change': Tag 'Agents' ausente no Journal.
  - Regra 'roles_registry_change': Arquivo '.context/brain/FILE_GLOSSARY.md' não foi propagado (ausente no diff).
  - Regra 'roles_registry_change': Checkbox [x] para '.context/brain/FILE_GLOSSARY.md' ausente ou desmarcado no Journal.
  - Regra 'new_context_path': Arquivo '.context/brain/FILE_GLOSSARY.md' não foi propagado (ausente no diff).
  - Regra 'new_context_path': Checkbox [x] para '.context/brain/FILE_GLOSSARY.md' ausente ou desmarcado no Journal.
  - Modificação Silenciosa: Arquivo '.specs/features/blast_radius_mvp/' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.context/brain/AGENT_REGISTRY.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.agent/skills/sdd-orchestrator/' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.context/maintenance/TECHNICAL_REQUIREMENTS.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.context/brain/LEARNINGS.md' alterado no Git mas ausente na Matriz de Propagação do Journal.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-FAIL] Report | spec:blast_radius_mvp
- **Detalhe:** journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...
[INFO] Regra 'roles_registry_change' disparada.
[INFO] Regra 'new_context_path' disparada.

❌ VIOLAÇÕES DETECTADAS:
  - Regra 'roles_registry_change': Tag 'Roles' ausente no Journal.
  - Regra 'roles_registry_change': Tag 'Agents' ausente no Journal.
  - Regra 'roles_registry_change': Arquivo '.context/brain/FILE_GLOSSARY.md' não foi propagado (ausente no diff).
  - Regra 'roles_registry_change': Checkbox [x] para '.context/brain/FILE_GLOSSARY.md' ausente ou desmarcado no Journal.
  - Regra 'new_context_path': Arquivo '.context/brain/FILE_GLOSSARY.md' não foi propagado (ausente no diff).
  - Regra 'new_context_path': Checkbox [x] para '.context/brain/FILE_GLOSSARY.md' ausente ou desmarcado no Journal.
  - Modificação Silenciosa: Arquivo '.context/maintenance/TECHNICAL_REQUIREMENTS.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.context/brain/AGENT_REGISTRY.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.agent/skills/sdd-orchestrator/' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.context/brain/LEARNINGS.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.specs/features/blast_radius_mvp/' alterado no Git mas ausente na Matriz de Propagação do Journal.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-FAIL] Report | spec:blast_radius_mvp
- **Detalhe:** journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...
[INFO] Regra 'new_context_path' disparada.
[INFO] Regra 'rules_change' disparada.

❌ VIOLAÇÕES DETECTADAS:
  - Modificação Silenciosa: Arquivo '.context/maintenance/TECHNICAL_REQUIREMENTS.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.context/brain/LEARNINGS.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.specs/features/blast_radius_mvp/STATE.md' alterado no Git mas ausente na Matriz de Propagação do Journal.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-PASS] Report | spec:blast_radius_mvp
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:blast_radius_mvp
- **Detalhe:** All contracts valid

## [HARNESS-FAIL] Report | spec:blast_radius_mvp
- **Detalhe:** journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...
[INFO] Regra 'new_context_path' disparada.

❌ VIOLAÇÕES DETECTADAS:
  - Regra 'new_context_path': Arquivo '.context/brain/FILE_GLOSSARY.md' não foi propagado (ausente no diff).
  - Regra 'new_context_path': Checkbox [x] para '.context/brain/FILE_GLOSSARY.md' ausente ou desmarcado no Journal.
  - Fraude Narrativa: Arquivo '.context/monitoring/CONTEXT_HEALTH.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo '.context/market/wiki_log.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo '.context/monitoring/PROJECT_INDEX_03.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo '.context/monitoring/PROJECT_INDEX_02.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo '.context/monitoring/PROJECT_INDEX_01.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Modificação Silenciosa: Arquivo '.context/brain/LEARNINGS.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.specs/features/blast_radius_mvp/STATE.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.context/maintenance/TECHNICAL_REQUIREMENTS.md' alterado no Git mas ausente na Matriz de Propagação do Journal.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-FAIL] Report | spec:blast_radius_mvp
- **Detalhe:** journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...

❌ VIOLAÇÕES DETECTADAS:
  - Fraude Narrativa: Arquivo '.context/monitoring/PROJECT_INDEX_02.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo '.context/maintenance/_archive_context/journals/journal_archive_20260522_143007.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo '.context/monitoring/PROJECT_INDEX_01.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo '.context/monitoring/CONTEXT_HEALTH.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo '.context/monitoring/PROJECT_INDEX_03.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo '.context/market/wiki_log.md' marcado como [x] no Journal, mas não há alterações no Git.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-PASS] Report | spec:blast_radius_mvp
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:blast_radius_mvp
- **Detalhe:** All contracts valid

## [HARNESS-FAIL] Report | spec:blast_radius_mvp
- **Detalhe:** journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...

❌ VIOLAÇÕES DETECTADAS:
  - Fraude Narrativa: Arquivo '.context/_scripts/purge_journal.py' marcado como [x] no Journal, mas não há alterações no Git.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-FAIL] Report | spec:blast_radius_mvp
- **Detalhe:** journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...

❌ VIOLAÇÕES DETECTADAS:
  - Modificação Silenciosa: Arquivo '.specs/features/blast_radius_mvp/STATE.md' alterado no Git mas ausente na Matriz de Propagação do Journal.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-PASS] Report | spec:blast_radius_mvp
- **Detalhe:** All contracts valid

## [HARNESS-FAIL] Report | spec:manual
- **Detalhe:** sprint_contract: Nenhuma Spec ativa detectada.

## [HARNESS-FAIL] Report | spec:manual
- **Detalhe:** sprint_contract: Nenhuma Spec ativa detectada.

## [HARNESS-FAIL] Report | spec:manual
- **Detalhe:** sprint_contract: Nenhuma Spec ativa detectada. | journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...

❌ [FATAL] Modificação Silenciosa: Foram detectados arquivos governados alterados, mas o JOURNAL.md não possui uma nova entrada para este commit.
Arquivos governados detectados (exemplo):
  - .context/_scripts/validate_context.py
  - .agent/skills/sdd-orchestrator/SKILL.md
  - .context/maintenance/rx-learnings.md

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-FAIL] Report | spec:manual
- **Detalhe:** sprint_contract: Nenhuma Spec ativa detectada.

## [HARNESS-FAIL] Report | spec:teste_trivial_dryrun
- **Detalhe:** handoff: Handoffs malformados: ['Handoff incompleto: ** Atualizados os prompts de `'] | journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...

❌ [FATAL] Modificação Silenciosa: Foram detectados arquivos governados alterados, mas o JOURNAL.md não possui uma nova entrada para este commit.
Arquivos governados detectados (exemplo):
  - .specs/features/teste_trivial_dryrun/tasks.md
  - .specs/features/teste_trivial_dryrun/STATE.md
  - .specs/features/teste_trivial_dryrun/AGENT_SCRATCHPAD.md

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-FAIL] Report | spec:teste_trivial_dryrun
- **Detalhe:** handoff: Handoffs malformados: ['Handoff incompleto: ** Atualizados os prompts de `'] | journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...

❌ VIOLAÇÕES DETECTADAS:
  - Fraude Narrativa: Arquivo '.specs/features/teste_trivial_dryrun/CLOSURE.md' marcado como [x] no Journal, mas não há alterações no Git.
  - Modificação Silenciosa: Arquivo '.specs/features/teste_trivial_dryrun/AGENT_SCRATCHPAD.md' alterado no Git mas ausente na Matriz de Propagação do Journal.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-FAIL] Report | spec:teste_trivial_dryrun
- **Detalhe:** handoff: Handoffs malformados: ['Handoff incompleto: ** Atualizados os prompts de `']

## [HARNESS-PASS] Report | spec:teste_trivial_dryrun
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:teste_trivial_dryrun
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:teste_trivial_dryrun
- **Detalhe:** All contracts valid

## [HARNESS-FAIL] Report | spec:teste_trivial_dryrun
- **Detalhe:** journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...
[INFO] Regra 'spec_driver_integrity' disparada.
[INFO] Regra 'roles_registry_change' disparada.

❌ VIOLAÇÕES DETECTADAS:
  - Regra 'spec_driver_integrity': Tag 'Firmware' ausente no Journal.
  - Regra 'spec_driver_integrity': Tag 'Governance Core' ausente no Journal.
  - Regra 'spec_driver_integrity': Arquivo '.context/brain/RULES.md' não foi propagado (ausente no diff).
  - Regra 'spec_driver_integrity': Checkbox [x] para '.context/brain/RULES.md' ausente ou desmarcado no Journal.
  - Regra 'spec_driver_integrity': Arquivo '.context/brain/MASTER_FLOW.md' não foi propagado (ausente no diff).
  - Regra 'spec_driver_integrity': Checkbox [x] para '.context/brain/MASTER_FLOW.md' ausente ou desmarcado no Journal.
  - Regra 'roles_registry_change': Tag 'Roles' ausente no Journal.
  - Regra 'roles_registry_change': Arquivo '.context/brain/FILE_GLOSSARY.md' não foi propagado (ausente no diff).
  - Regra 'roles_registry_change': Checkbox [x] para '.context/brain/FILE_GLOSSARY.md' ausente ou desmarcado no Journal.
  - Regra 'roles_registry_change': Arquivo '.context/brain/SCRIPT_GLOSSARY.md' não foi propagado (ausente no diff).
  - Regra 'roles_registry_change': Checkbox [x] para '.context/brain/SCRIPT_GLOSSARY.md' ausente ou desmarcado no Journal.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-FAIL] Report | spec:teste_trivial_dryrun
- **Detalhe:** impact_radius: Raio de impacto excedido! (Modificados: 13 > Limite: 8). Re-fragmente a SPEC ou aumente o limite se justificado. | journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...
[INFO] Regra 'spec_driver_integrity' disparada.
[INFO] Regra 'roles_registry_change' disparada.
[INFO] Regra 'rules_change' disparada.

❌ VIOLAÇÕES DETECTADAS:
  - Modificação Silenciosa: Arquivo '.specs/features/teste_trivial_dryrun/STATE.md' alterado no Git mas ausente na Matriz de Propagação do Journal.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-PASS] Report | spec:teste_trivial_dryrun
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:teste_trivial_dryrun
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:teste_trivial_dryrun
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:teste_trivial_dryrun
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:teste_trivial_dryrun
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:teste_trivial_dryrun
- **Detalhe:** All contracts valid

## [HARNESS-FAIL] Report | spec:api_notion_crm
- **Detalhe:** enrichment: Seção Critical Dependencies obrigatória para PRDs com integrações/compliance | sprint_contract: [HG06] start_hash não encontrado para sprint_01 no STATE.md (Formato esperado: ## sprint_01 
 start_hash: ...) | journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...

❌ [FATAL] Modificação Silenciosa: Foram detectados arquivos governados alterados, mas o JOURNAL.md não possui uma nova entrada para este commit.
Arquivos governados detectados (exemplo):
  - docs/
  - .context/_scripts/__pycache__/context_oracle.cpython-314.pyc
  - .context/_scripts/__pycache__/_wiki_log_utils.cpython-314.pyc

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-FAIL] Report | spec:api_notion_crm
- **Detalhe:** sprint_contract: [HG06] start_hash não encontrado para sprint_01 no STATE.md (Formato esperado: ## sprint_01 
 start_hash: ...) | impact_radius: Raio de impacto excedido! (Modificados: 7 > Limite: 6). Re-fragmente a SPEC ou aumente o limite se justificado. | journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...

❌ [FATAL] Modificação Silenciosa: Foram detectados arquivos governados alterados, mas o JOURNAL.md não possui uma nova entrada para este commit.
Arquivos governados detectados (exemplo):
  - .context/_scripts/__pycache__/_tz_utils.cpython-314.pyc
  - .context/_scripts/__pycache__/_wiki_log_utils.cpython-314.pyc
  - .context/brain/PRD.md

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-FAIL] Report | spec:api_notion_crm
- **Detalhe:** journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...

❌ [FATAL] Modificação Silenciosa: Foram detectados arquivos governados alterados, mas o JOURNAL.md não possui uma nova entrada para este commit.
Arquivos governados detectados (exemplo):
  - .context/_scripts/__pycache__/_tz_utils.cpython-314.pyc
  - .specs/features/api_notion_crm/STATE.md
  - .context/brain/PRD.md

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-FAIL] Report | spec:api_notion_crm
- **Detalhe:** journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...

❌ VIOLAÇÕES DETECTADAS:
  - Modificação Silenciosa: Arquivo '.context/_scripts/__pycache__/_tz_utils.cpython-314.pyc' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.context/_scripts/__pycache__/_wiki_log_utils.cpython-314.pyc' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.context/_scripts/__pycache__/context_oracle.cpython-314.pyc' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo 'docs/' alterado no Git mas ausente na Matriz de Propagação do Journal.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-FAIL] Report | spec:api_notion_crm
- **Detalhe:** journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...

❌ VIOLAÇÕES DETECTADAS:
  - Modificação Silenciosa: Arquivo '.context/_scripts/__pycache__/context_oracle.cpython-314.pyc' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.context/_scripts/__pycache__/_wiki_log_utils.cpython-314.pyc' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.context/_scripts/__pycache__/_tz_utils.cpython-314.pyc' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo 'docs/PLAN-api-notion-crm.md' alterado no Git mas ausente na Matriz de Propagação do Journal.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-FAIL] Report | spec:api_notion_crm
- **Detalhe:** journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...

❌ VIOLAÇÕES DETECTADAS:
  - Fraude Narrativa: Arquivo 'scripts/setup-crm.js' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo 'api/webhook-intake.js' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo '.env.example' marcado como [x] no Journal, mas não há alterações no Git.
  - Modificação Silenciosa: Arquivo '.context/_scripts/workflow_journal_auditor.py' alterado no Git mas ausente na Matriz de Propagação do Journal.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-FAIL] Report | spec:api_notion_crm
- **Detalhe:** journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...

❌ VIOLAÇÕES DETECTADAS:
  - Fraude Narrativa: Arquivo 'scripts/setup-crm.js' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo 'api/webhook-intake.js' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo '.env.example' marcado como [x] no Journal, mas não há alterações no Git.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-FAIL] Report | spec:api_notion_crm
- **Detalhe:** journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...

❌ VIOLAÇÕES DETECTADAS:
  - Fraude Narrativa: Arquivo 'scripts/setup-crm.js' marcado como [x] no Journal, mas não há alterações no Git.
  - Fraude Narrativa: Arquivo 'api/webhook-intake.js' marcado como [x] no Journal, mas não há alterações no Git.
  - Modificação Silenciosa: Arquivo 'scripts/' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo 'api/' alterado no Git mas ausente na Matriz de Propagação do Journal.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-FAIL] Report | spec:api_notion_crm
- **Detalhe:** impact_radius: Raio de impacto excedido! (Modificados: 15 > Limite: 12). Re-fragmente a SPEC ou aumente o limite se justificado.

## [HARNESS-PASS] Report | spec:api_notion_crm
- **Detalhe:** All contracts valid

## [HARNESS-FAIL] Report | spec:api_notion_crm
- **Detalhe:** impact_radius: Raio de impacto excedido! (Modificados: 18 > Limite: 16). Re-fragmente a SPEC ou aumente o limite se justificado. | journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...

❌ VIOLAÇÕES DETECTADAS:
  - Modificação Silenciosa: Arquivo 'package-lock.json' alterado no Git mas ausente na Matriz de Propagação do Journal.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-PASS] Report | spec:api_notion_crm
- **Detalhe:** All contracts valid

## [HARNESS-FAIL] Report | spec:api_notion_crm
- **Detalhe:** journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...

❌ VIOLAÇÕES DETECTADAS:
  - Modificação Silenciosa: Arquivo '.specs/features/api_notion_crm/tasks.md' alterado no Git mas ausente na Matriz de Propagação do Journal.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-PASS] Report | spec:api_notion_crm
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:api_notion_crm
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:api_notion_crm
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:api_notion_crm
- **Detalhe:** All contracts valid

## [HARNESS-FAIL] Report | spec:api_notion_crm
- **Detalhe:** journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...

❌ VIOLAÇÕES DETECTADAS:
  - Modificação Silenciosa: Arquivo 'index.html' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo 'style.css' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo 'assets/' alterado no Git mas ausente na Matriz de Propagação do Journal.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-FAIL] Report | spec:api_notion_crm
- **Detalhe:** journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...

❌ VIOLAÇÕES DETECTADAS:
  - Fraude Narrativa: Arquivo 'assets/crm_dashboard_mockup.png' marcado como [x] no Journal, mas não há alterações no Git.
  - Modificação Silenciosa: Arquivo 'assets/' alterado no Git mas ausente na Matriz de Propagação do Journal.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-PASS] Report | spec:api_notion_crm
- **Detalhe:** All contracts valid

## [HARNESS-FAIL] Report | spec:manual
- **Detalhe:** sprint_contract: Nenhuma Spec ativa detectada. | journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...

❌ VIOLAÇÕES DETECTADAS:
  - Modificação Silenciosa: Arquivo '.context/_scripts/workflow_journal_auditor.py' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.specs/features/landing_page_crm/AGENT_SCRATCHPAD.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.env.example' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo 'api/webhook-intake.js' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo 'docs/PLAN-api-notion-crm.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo 'tests/webhook-intake.test.js' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.specs/features/api_notion_crm/AGENT_SCRATCHPAD.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo 'style.css' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo 'assets/crm_dashboard_mockup.png' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.specs/features/api_notion_crm/tasks.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo 'index.html' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo 'package.json' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.specs/features/api_notion_crm/CLOSURE.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.context/brain/FILE_GLOSSARY.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo 'scripts/setup-crm.js' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo 'package-lock.json' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.context/maintenance/rx-communications.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.context/maintenance/ARCHITECTURE.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.context/brain/PRD.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.specs/features/api_notion_crm/.enriched.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.specs/features/SSD_ERRORS_LEDGER.md' alterado no Git mas ausente na Matriz de Propagação do Journal.
  - Modificação Silenciosa: Arquivo '.specs/features/landing_page_crm/.enriched.md' alterado no Git mas ausente na Matriz de Propagação do Journal.

[FATAL] Modo STRICT: Pipeline bloqueado.


## [HARNESS-FAIL] Report | spec:api_notion_crm
- **Detalhe:** impact_radius: Raio de impacto excedido! (Modificados: 31 > Limite: 28). Re-fragmente a SPEC ou aumente o limite se justificado.

## [HARNESS-PASS] Report | spec:api_notion_crm
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:api_notion_crm
- **Detalhe:** All contracts valid

## [HARNESS-FAIL] Report | spec:manual
- **Detalhe:** sprint_contract: Nenhuma Spec ativa detectada. | journal_sam: Violações SAM detectadas.
🤖 Iniciando Auditoria Anti-Migué (SAM)...

❌ [FATAL] Modificação Silenciosa: Foram detectados arquivos governados alterados, mas o JOURNAL.md não possui uma nova entrada para este commit.
Arquivos governados detectados (exemplo):
  - .context/_scripts/complexity_coverage_gate.py
  - .context/_scripts/loop_exhaustion_harness.py
  - .context/_scripts/workflow_journal_auditor.py

[FATAL] Modo STRICT: Pipeline bloqueado.

