---
contract_version: 2.5.2
parties: ["@spec-driver", "@qa-validator"]
contract_mode: sprint_based
current_sprint: sprint_05
policy_profile: hybrid
plan_source: "planos/mudanca_specdriven/plano_v2_caminho_seguro_falsh.md"
qa_signoff: true
signed_by: "@qa-validator"

sprints:
  sprint_01:
    goal: "Fundação: Contrato e Template"
    scope_allow: [".context/_scripts/harness_runner.py", ".specs/_template.md", ".context/maintenance/HARNESS_LOG.md", "planos/mudanca_specdriven/", ".specs/features/contract_sprints_v2_safe/STATE.md", ".specs/features/contract_sprints_v2_safe/spec.md", ".specs/features/contract_sprints_v2_safe/tasks.md"]
    acceptance:
      - "[x] Template atualizado"
    qa_signoff: true

  sprint_02:
    goal: "Harness Runner: Dual Mode & Hard Gates"
    scope_allow: [".context/_scripts/harness_runner.py", ".specs/_template.md", ".context/maintenance/HARNESS_LOG.md", "planos/mudanca_specdriven/", ".specs/features/contract_sprints_v2_safe/STATE.md", ".specs/features/contract_sprints_v2_safe/spec.md", ".specs/features/contract_sprints_v2_safe/tasks.md"]
    acceptance:
      - "[x] Harness polimórfico e hardened"
      - "[x] Enforcement real HG04"
    qa_signoff: true

  sprint_03:
    goal: "QA Validator: Assinatura Incremental & Bloqueio Final"
    scope_allow: [".agent/subagents/qa-validator.md", ".context/_scripts/harness_runner.py", ".specs/features/contract_sprints_v2_safe/STATE.md", ".specs/features/contract_sprints_v2_safe/spec.md", ".specs/features/contract_sprints_v2_safe/tasks.md", ".context/maintenance/HARNESS_LOG.md"]
    acceptance:
      - "[x] Subagente QA instruído sobre modo sprint"
      - "[x] Bloqueio de feature_done implementado"
    qa_signoff: true

  sprint_04:
    goal: "Impacto Incremental: Captura Automática de start_hash"
    scope_allow: [".context/_scripts/harness_runner.py", ".specs/features/contract_sprints_v2_safe/STATE.md", ".specs/features/contract_sprints_v2_safe/spec.md", ".specs/features/contract_sprints_v2_safe/tasks.md", ".context/maintenance/HARNESS_LOG.md"]
    acceptance:
      - "[x] Implementar captura automática de impacto (D1)"
      - "[x] Testar diff incremental (D2)"
    qa_signoff: true

  sprint_05:
    goal: "Higiene & SSOT: Proteção de Cleanup e Docs Mestre"
    scope_allow: [".context/_scripts/harness_runner.py", ".context/_scripts/cleanup_specs.py", ".context/brain/MASTER_FLOW.md", ".context/brain/RULES.md", ".context/maintenance/JOURNAL.md", ".specs/features/contract_sprints_v2_safe/STATE.md", ".specs/features/contract_sprints_v2_safe/spec.md", ".specs/features/contract_sprints_v2_safe/tasks.md", ".context/maintenance/HARNESS_LOG.md"]
    acceptance:
      - "[x] Adaptar cleanup_specs.py para proteger sprint ativa"
      - "[x] Atualizar MASTER_FLOW e RULES para v2-Safe"
    qa_signoff: true
---

# 📄 Spec: Evolução Contract Sprints (v2-Safe)
> **Modo:** Sprint-based Finalizado (CONCLUÍDO)
