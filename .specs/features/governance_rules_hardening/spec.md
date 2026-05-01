---
contract_version: 2.5.2
contract_mode: sprint_based
current_sprint: sprint_01
plan_source: planos/governance_rules_hardening/plano_governance_rules_hardening.md
parties: ["@spec-driver", "@qa-validator"]
executor_context_id: "ctx-dev-20260430-2111"
validator_context_id: "ctx-qa-20260430-2111"
policy_profile: hybrid
impact_control:
  max_impact_radius: 5
  pre_flight_grep_terms: ["CLOSE_WAVE", "ANTI_FALSE_PASS", "start_hash"]

sprints:
  sprint_01:
    name: "Regras Canônicas & Self-Audit"
    status: IN_PROGRESS
    qa_signoff: false
    scope_allow:
      - .context/brain/RULES.md
      - .context/brain/MASTER_FLOW.md
      - .specs/features/governance_rules_hardening/spec.md
      - .specs/features/governance_rules_hardening/tasks.md
      - .specs/features/governance_rules_hardening/STATE.md
      - .context/maintenance/JOURNAL.md
      - .context/maintenance/HARNESS_LOG.md
---

# Spec: Governance Rules Hardening
> Contrato de implementação da governança determinística e anti-fraude narrativa.
