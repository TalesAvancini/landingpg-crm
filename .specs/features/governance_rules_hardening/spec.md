---
contract_version: 2.5.2
parties: ["@spec-driver", "@qa-validator"]
contract_mode: sprint_based
current_sprint: sprint_07
policy_profile: hybrid
plan_source: planos/governance_rules_hardening/plano_governance_rules_hardening.md
qa_signoff: false
signed_by: null

sprints:
  sprint_01:
    goal: "Implementar Regras Canônicas (CLOSE_WAVE, ANTI_FALSE_PASS) e rito de Pre-Close Audit."
    scope_allow:
      - ".context/brain/RULES.md"
      - ".context/brain/MASTER_FLOW.md"
      - ".specs/features/governance_rules_hardening/spec.md"
      - ".specs/features/governance_rules_hardening/tasks.md"
      - ".specs/features/governance_rules_hardening/STATE.md"
      - ".context/maintenance/JOURNAL.md"
      - ".context/maintenance/HARNESS_LOG.md"
    scope_deny: []
    acceptance:
      - "[x] Regras CLOSE_WAVE e ANTI_FALSE_PASS publicadas no RULES.md"
      - "[x] Rito Pre-Close Audit inserido no MASTER_FLOW.md"
      - "[x] Passo Pre-close Self-Audit adicionado ao workflow do spec-driver"
      - "[x] Exemplos PASS/FAIL incluídos no RULES.md"
    qa_signoff: true
    signed_by: "@qa-validator"

  sprint_02:
    goal: "Integridade SSOT (MIMO_STATE_INTEGRITY) e Sanidade de Script (CRITICAL_SCRIPT_SANITY)."
    scope_allow:
      - ".context/brain/RULES.md"
      - ".context/brain/MASTER_FLOW.md"
      - ".specs/features/governance_rules_hardening/spec.md"
      - ".specs/features/governance_rules_hardening/tasks.md"
      - ".specs/features/governance_rules_hardening/STATE.md"
      - ".context/maintenance/JOURNAL.md"
      - ".context/maintenance/HARNESS_LOG.md"
    scope_deny: []
    acceptance:
      - "[x] Regra MIMO_STATE_INTEGRITY (Integridade de Estado) formalizada no RULES.md"
      - "[x] Regra CRITICAL_SCRIPT_SANITY (Sanidade de Scripts) formalizada no RULES.md"
      - "[x] Mapeamento de sanidade de scripts inserido no MASTER_FLOW.md"
      - "[x] Metadados de freshness atualizados em ambos os arquivos normais"
    qa_signoff: true
    signed_by: "@qa-validator"

  sprint_03:
    goal: "Runbook & Métricas Operacionais com modo advisory para fricção de governança."
    scope_allow:
      - ".context/brain/MASTER_FLOW.md"
      - ".context/_scripts/validate_context.py"
      - ".context/maintenance/HARNESS_LOG.md"
      - ".specs/features/governance_rules_hardening/spec.md"
      - ".specs/features/governance_rules_hardening/tasks.md"
      - ".specs/features/governance_rules_hardening/STATE.md"
      - ".context/maintenance/JOURNAL.md"
    scope_deny: []
    acceptance:
      - "[x] Ordem cronológica do JOURNAL tratada como WARN (não bloqueante)"
      - "[x] Disciplina de `STATE.updated` reforçada no checklist (datetime completo)"
      - "[x] Eventos `[GOVERNANCE-FRICTION]` automatizados no HARNESS_LOG.md"
    qa_signoff: true
    signed_by: "@qa-validator"

  sprint_04:
    goal: "Sincronização Institucional: Glossários, Bibliotecas e Runbooks finais."
    scope_allow:
      - ".context/brain/MASTER_FLOW.md"
      - ".context/brain/RULES.md"
      - ".context/maintenance/JOURNAL.md"
      - ".specs/features/governance_rules_hardening/spec.md"
      - ".specs/features/governance_rules_hardening/tasks.md"
      - ".specs/features/governance_rules_hardening/STATE.md"
    scope_deny: []
    acceptance:
      - "[x] HARNESS_REGISTRY.md e glossários atualizados"
      - "[x] PROMPT_LIBRARY.md atualizada com padrões de hardening"
    qa_signoff: true
    signed_by: "@qa-validator"

  sprint_05:
    goal: "Enforcement Automático (Músculos): Implementar validações automáticas em validate_context.py."
    scope_allow:
      - ".context/_scripts/validate_context.py"
      - ".specs/features/governance_rules_hardening/spec.md"
      - ".specs/features/governance_rules_hardening/tasks.md"
      - ".specs/features/governance_rules_hardening/STATE.md"
      - ".context/maintenance/JOURNAL.md"
    scope_deny: []
    acceptance:
      - "[x] Validação de meta-data freshness bloqueante (Fail-Closed)"
      - "[x] Validação de sync de acceptance/tasks bloqueante"
    qa_signoff: true
    signed_by: "@qa-validator"

  sprint_06:
    goal: "Hardening de Agenciamento (Nervos): Atualizar papéis e ritos de fechamento."
    scope_allow:
      - ".context/brain/AGENT_REGISTRY.md"
      - ".context/brain/MASTER_FLOW.md"
      - ".specs/features/governance_rules_hardening/spec.md"
      - ".specs/features/governance_rules_hardening/tasks.md"
      - ".specs/features/governance_rules_hardening/STATE.md"
    scope_deny: []
    acceptance:
      - "[x] Papéis spec-driver e qa-validator atualizados com Hardened Closing"
      - "[x] Implementada transição atômica para IN_PROGRESS via protocolo"
    qa_signoff: false
    signed_by: null

  sprint_07:
    goal: "Hardening SAM & Telemetria: Detecção de fraude narrativa e métricas."
    scope_allow:
      - ".context/_scripts/workflow_journal_auditor.py"
      - ".context/brain/AGENT_REGISTRY.md"
      - ".context/maintenance/HARNESS_LOG.md"
    scope_deny: []
    acceptance:
      - "[x] Detecção de Fraude Narrativa implementada no auditor"
      - "[x] Schema de telemetria [GOVERNANCE-FRICTION] integrado"
    qa_signoff: false
    signed_by: null

  sprint_08:
    goal: "Visão: RX Communications e Documentação de Transparência."
    scope_allow:
      - ".context/maintenance/rx-communications.md"
      - ".context/brain/MASTER_FLOW.md"
      - ".context/brain/FILE_GLOSSARY.md"
    scope_deny: []
    acceptance:
      - "[ ] Arquivo rx-communications.md criado e populado"
      - "[ ] Referências cruzadas inseridas na governança central"
    qa_signoff: false
    signed_by: null
---

# Spec: Governance Rules Hardening
> Modo: Sprint-based (Hardened)

## Objetivo
Transformar aprendizados do pós-missão em governança executável end-to-end, eliminando fraudes narrativas e incoerências de fechamento.

## Regras de Execução
- Fechamento de sprint exige `qa_signoff: true` no bloco da sprint.
- Fechamento global exige consistência entre `spec.md`, `tasks.md`, `STATE.md` e árvore Git limpa.
