---
contract_version: 2.5.2
parties: ["@spec-driver", "@qa-validator"]
contract_mode: sprint_based
current_sprint: sprint_02
policy_profile: hybrid
plan_source: "planos/mudanca_specdriven/plano_v2_caminho_seguro_falsh.md"

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
    qa_signoff: true # CONCLUÍDO pós-auditoria
---

# 📄 Spec: Evolução Contract Sprints (v2-Safe)
> **Modo:** Sprint-based Ativado
