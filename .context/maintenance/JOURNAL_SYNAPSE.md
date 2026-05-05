# 🧠 JOURNAL_SYNAPSE.md (Matriz de Gatilhos)

Este arquivo define as regras determinísticas de propagação de contexto. 
O Agente Executor deve cumprir as promessas geradas por estas regras para liberar o commit.

<!-- SYNAPSE_JSON_START -->
{
  "version": 1,
  "mode": "strict",
  "rules": [
    {
      "id": "spec_driver_integrity",
      "when_any_changed": [".agent/subagents/spec-driver.md"],
      "require_journal_tags": ["Firmware", "Governance Core"],
      "require_files_touched": [
        ".context/brain/AGENT_REGISTRY.md",
        ".context/brain/RULES.md",
        ".context/brain/MASTER_FLOW.md"
      ],
      "severity": "critical"
    },
    {
      "id": "roles_registry_change",
      "when_any_changed": [".context/brain/AGENT_REGISTRY.md"],
      "require_journal_tags": ["Roles", "Agents"],
      "require_files_touched": [
        ".context/brain/FILE_GLOSSARY.md",
        ".context/brain/SCRIPT_GLOSSARY.md"
      ],
      "severity": "critical"
    },
    {
      "id": "sql_change",
      "when_any_changed": [".context/maintenance/schema.sql"],
      "require_journal_tags": ["SQL", "Schema"],
      "require_files_touched": [".context/maintenance/TECHNICAL_REQUIREMENTS.md"],
      "severity": "critical"
    },
    {
      "id": "new_context_path",
      "when_new_path_under": [".context/"],
      "require_files_touched": [".context/brain/FILE_GLOSSARY.md"],
      "severity": "critical"
    },
    {
      "id": "rules_change",
      "when_any_changed": [".context/brain/RULES.md"],
      "require_journal_tags": ["Governança", "Regras"],
      "severity": "warning",
      "note": "Deprecado: requirement_metadata_bump removido para reduzir fricção."
    },
    {
      "id": "market_change",
      "when_any_changed": [".context/market/SSOT_MAP.md"],
      "require_journal_tags": ["Market", "Roteamento"],
      "severity": "warning"
    }
  ]
}
<!-- SYNAPSE_JSON_END -->

## 📋 Tabela de Referência Humana

| ID | Se mudar... | Exige atualização em... | Gravidade |
| :--- | :--- | :--- | :--- |
| `spec_driver_integrity` | `spec-driver.md` | `REGISTRY`, `RULES`, `MASTER_FLOW` | 🔴 CRITICAL |
| `roles_registry_change`| `AGENT_REGISTRY.md` | Glossários (Files e Scripts) | 🔴 CRITICAL |
| `sql_change` | `schema.sql` | `TECHNICAL_REQUIREMENTS.md` | 🔴 CRITICAL |
| `new_context_path` | `.context/*` (novo) | `FILE_GLOSSARY.md` | 🔴 CRITICAL |
| `rules_change` | `RULES.md` | Apenas Tags no Journal | 🟡 WARNING |
| `market_change` | `SSOT_MAP.md` | Tags de Market no Journal | 🟡 WARNING |

---
*Gerado via Antigravity Kit v2.5.2 | Reforma Legislativa SAM v1.1*
