---
contract_version: 2.5.2
parties: ["@spec-driver", "@qa-validator"]
contract_mode: sprint_based
current_sprint: sprint_01
policy_profile: hybrid
plan_source: "planos/mudanca_specdriven/plano_v2_caminho_seguro_falsh.md"

sprints:
  sprint_01:
    goal: "Fundação: Contrato e Harness Dual Mode"
    scope_allow: [".context/_scripts/harness_runner.py", ".specs/_template.md", ".context/maintenance/HARNESS_LOG.md", "planos/mudanca_specdriven.md", ".specs/features/contract_sprints_v2_safe/STATE.md", ".specs/features/contract_sprints_v2_safe/spec.md", ".specs/features/contract_sprints_v2_safe/tasks.md"]
    acceptance:
      - "[x] Template atualizado"
      - "[x] Harness polimórfico"
      - "[x] Engine de Gates implementada"
    qa_signoff: true # Assinado para permitir evolução
---

# 📄 Spec: Evolução Contract Sprints (v2-Safe)
> **Modo:** Sprint-based Ativado

## 🎯 Objetivo
Implantar o novo paradigma de Sprints de Contratos de forma segura e auditável.
