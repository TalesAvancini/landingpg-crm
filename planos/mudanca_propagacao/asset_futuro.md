## O que preciso para as fases seguintes

Para a **Fase 1** (governance_edges.json), tenho tudo — o `rx-communications.md` completo.

Para as **Fases 3-4**, vou precisar de:

| Arquivo | Quando | Para quê |
|---------|--------|----------|
| `journal-sync/SKILL.md` | Fase 3 | Atualizar o Step 2 com precisão |
| `FILE_GLOSSARY.md` | Fase 4 | Saber o formato para adicionar entrada |
| `SCRIPT_GLOSSARY.md` | Fase 4 | Saber o formato para adicionar entrada |

Posso pedir esses quando chegar a hora. Começo agora pela **Fase 1**.

---

## Fase 1 — governance_edges.json

Extraí todas as edges da Seção 4 do `rx-communications.md`. A seguir o arquivo completo:

```json
{
  "$schema": "governance_edges_v1",
  "version": 1,
  "generated_from": "rx-communications.md",
  "generated_at": "2026-05-21",
  "maintainer_note": "Versão estruturada da Seção 4 do rx-communications.md. blast_radius.py consome este arquivo. O .md continua como documentação narrativa. Quando houver divergência, este JSON é a fonte para o script.",

  "categories": {
    "nature_types": [
      "diretriz", "protocolo", "orquestracao",
      "evidencia", "metabolica", "aprendizado",
      "mitigacao", "sintese", "referencia",
      "permissao", "roteamento", "formacao",
      "gatilho", "degradacao"
    ],
    "layers": [
      "raiz", "estrategica", "constitucional",
      "tatica", "imunologica", "metabolica",
      "motor", "monitoramento"
    ]
  },

  "edges": [

    {"id": "vision_to_inception",       "source": "VISION.md",       "source_path": ".context/brain/VISION.md",            "target": "INCEPTION.md",        "target_path": ".context/brain/INCEPTION.md",            "direction": "forward", "nature": "diretriz",       "layer": "estrategica",   "critical": false, "note": "A bússola do projeto. Tudo deriva daqui."},
    {"id": "vision_to_roadmap",         "source": "VISION.md",       "source_path": ".context/brain/VISION.md",            "target": "ROADMAP.md",          "target_path": ".context/brain/ROADMAP.md",              "direction": "forward", "nature": "diretriz",       "layer": "estrategica",   "critical": false, "note": "Bússola do projeto direciona priorização."},
    {"id": "inception_to_prd",          "source": "INCEPTION.md",    "source_path": ".context/brain/INCEPTION.md",         "target": "PRD.md",              "target_path": ".context/brain/PRD.md",                  "direction": "forward", "nature": "diretriz",       "layer": "estrategica",   "critical": false, "note": "Inception traça fronteira de onde o PRD pode atuar."},
    {"id": "prd_to_spec",               "source": "PRD.md",          "source_path": ".context/brain/PRD.md",               "target": "spec.md",             "target_path": ".specs/features/spec.md",                "direction": "forward", "nature": "diretriz",       "layer": "estrategica",   "critical": false, "note": "Repositório de requisitos que o Spec Driver consome."},
    {"id": "rules_to_master_flow",      "source": "RULES.md",        "source_path": ".context/brain/RULES.md",             "target": "MASTER_FLOW.md",      "target_path": ".context/brain/MASTER_FLOW.md",          "direction": "forward", "nature": "protocolo",      "layer": "constitucional", "critical": true,  "note": "Restringe ações do MASTER_FLOW."},
    {"id": "master_flow_to_spec_driver","source": "MASTER_FLOW.md",  "source_path": ".context/brain/MASTER_FLOW.md",       "target": "spec-driver.md",      "target_path": ".agent/subagents/spec-driver.md",        "direction": "forward", "nature": "orquestracao",   "layer": "constitucional", "critical": true,  "note": "Guia o comportamento e sequência lógica dos agentes."},
    {"id": "master_flow_to_qa",         "source": "MASTER_FLOW.md",  "source_path": ".context/brain/MASTER_FLOW.md",       "target": "qa-validator.md",     "target_path": ".agent/subagents/qa-validator.md",       "direction": "forward", "nature": "orquestracao",   "layer": "constitucional", "critical": false, "note": "Guia comportamento do QA Validator."},
    {"id": "agent_registry_to_agents",  "source": "AGENT_REGISTRY.md","source_path": ".context/brain/AGENT_REGISTRY.md",   "target": "*",                   "target_path": null,                                    "direction": "forward", "nature": "permissao",      "layer": "constitucional", "critical": false, "note": "Define escopo de atuação de todas as IAs. Alterar permissões afeta agentes operando fora do escopo."},

    {"id": "file_glossary_to_rx_comm",  "source": "FILE_GLOSSARY.md", "source_path": ".context/brain/FILE_GLOSSARY.md",   "target": "rx-communications.md","target_path": ".context/maintenance/rx-communications.md","direction": "forward", "nature": "referencia",     "layer": "constitucional", "critical": false, "note": "Se um nome muda aqui, a governança trava."},
    {"id": "file_glossary_to_sam",      "source": "FILE_GLOSSARY.md", "source_path": ".context/brain/FILE_GLOSSARY.md",   "target": "validate_context.py", "target_path": ".context/_scripts/validate_context.py",  "direction": "forward", "nature": "referencia",     "layer": "constitucional", "critical": false, "note": "SAM e validate_context usam glossário como referência."},
    {"id": "script_glossary_to_harness","source": "SCRIPT_GLOSSARY.md","source_path": ".context/brain/SCRIPT_GLOSSARY.md","target": "HARNESS_REGISTRY.md", "target_path": ".context/brain/HARNESS_REGISTRY.md",      "direction": "forward", "nature": "referencia",     "layer": "constitucional", "critical": false, "note": "Afeta orquestração do HARNESS_REGISTRY."},
    {"id": "harness_registry_to_log",   "source": "HARNESS_REGISTRY.md","source_path": ".context/brain/HARNESS_REGISTRY.md","target": "HARNESS_LOG.md",  "target_path": ".context/maintenance/HARNESS_LOG.md",  "direction": "forward", "nature": "gatilho",        "layer": "imunologica",    "critical": false, "note": "Dita quais portões de QA devem ser cruzados."},
    {"id": "learnings_to_rules",        "source": "LEARNINGS.md",    "source_path": ".context/brain/LEARNINGS.md",         "target": "RULES.md",            "target_path": ".context/brain/RULES.md",                "direction": "forward", "nature": "aprendizado",    "layer": "metabolica",     "critical": false, "note": "Transforma dor em lei sistêmica."},
    {"id": "learnings_to_ledger",       "source": "LEARNINGS.md",    "source_path": ".context/brain/LEARNINGS.md",         "target": "SSD_ERRORS_LEDGER.md","target_path": ".specs/features/SSD_ERRORS_LEDGER.md",   "direction": "forward", "nature": "aprendizado",    "layer": "metabolica",     "critical": false, "note": "Scars alimentam o ledger de erros."},
    {"id": "tlc_to_master_flow",        "source": "TLC_INTEGRATION.md","source_path": ".context/brain/TLC_INTEGRATION.md", "target": "MASTER_FLOW.md",      "target_path": ".context/brain/MASTER_FLOW.md",          "direction": "forward", "nature": "diretriz",       "layer": "constitucional", "critical": false, "note": "Filosofia de execução influencia orquestração."},

    {"id": "roadmap_to_journal",        "source": "ROADMAP.md",      "source_path": ".context/brain/ROADMAP.md",           "target": "JOURNAL.md",          "target_path": ".context/maintenance/JOURNAL.md",        "direction": "forward", "nature": "diretriz",       "layer": "estrategica",    "critical": false, "note": "Priorização de Sprints no JOURNAL."},
    {"id": "start_here_to_cortex",      "source": "START_HERE.md",   "source_path": ".context/brain/START_HERE.md",        "target": "*",                   "target_path": null,                                    "direction": "forward", "nature": "formacao",       "layer": "estrategica",    "critical": false, "note": "Afeta curva de aprendizado de humanos. Refatorações pesadas no Córtex afetam este arquivo.", "activation_rule": "only_if_cortex_files_in_seed"},
    {"id": "prompt_library_to_orch",    "source": "PROMPT_LIBRARY.md","source_path": ".context/brain/PROMPT_LIBRARY.md",   "target": "MASTER_FLOW.md",      "target_path": ".context/brain/MASTER_FLOW.md",          "direction": "forward", "nature": "referencia",     "layer": "constitucional", "critical": false, "note": "Qualidade da interação e taxa de acerto do Orquestrador."},

    {"id": "journal_to_learnings",      "source": "JOURNAL.md",      "source_path": ".context/maintenance/JOURNAL.md",     "target": "LEARNINGS.md",        "target_path": ".context/brain/LEARNINGS.md",            "direction": "forward", "nature": "aprendizado",    "layer": "metabolica",     "critical": false, "note": "Gera insumo de cicatrizes."},
    {"id": "harness_log_to_health",     "source": "HARNESS_LOG.md",  "source_path": ".context/maintenance/HARNESS_LOG.md", "target": "CONTEXT_HEALTH.md",   "target_path": ".context/monitoring/CONTEXT_HEALTH.md",  "direction": "forward", "nature": "evidencia",      "layer": "imunologica",    "critical": false, "note": "Painel visual de saúde e bloqueios de transição."},
    {"id": "tech_req_to_arch",          "source": "TECHNICAL_REQUIREMENTS.md","source_path": ".context/maintenance/TECHNICAL_REQUIREMENTS.md","target": "ARCHITECTURE.md","target_path": ".context/maintenance/ARCHITECTURE.md","direction": "forward", "nature": "diretriz",     "layer": "constitucional", "critical": false, "note": "Requisitos técnicos direcionam decisões de arquitetura."},
    {"id": "arch_to_spec",              "source": "ARCHITECTURE.md", "source_path": ".context/maintenance/ARCHITECTURE.md","target": "spec.md",             "target_path": ".specs/features/spec.md",                "direction": "forward", "nature": "diretriz",       "layer": "constitucional", "critical": false, "note": "Define como a spec resolve problemas técnicos."},
    {"id": "tests_to_qa",               "source": "TESTS.md",        "source_path": ".context/maintenance/TESTS.md",       "target": "qa-validator.md",     "target_path": ".agent/subagents/qa-validator.md",       "direction": "forward", "nature": "evidencia",      "layer": "imunologica",    "critical": false, "note": "Nível de exigência do QA Validator."},
    {"id": "synapse_to_journal",        "source": "JOURNAL_SYNAPSE.md","source_path": ".context/maintenance/JOURNAL_SYNAPSE.md","target": "JOURNAL.md",    "target_path": ".context/maintenance/JOURNAL.md",        "direction": "forward", "nature": "metabolica",     "layer": "metabolica",     "critical": false, "note": "Regras de purga de contexto."},

    {"id": "spec_to_source",            "source": "spec.md",         "source_path": ".specs/features/spec.md",             "target": "*",                   "target_path": null,                                    "direction": "forward", "nature": "orquestracao",   "layer": "tatica",         "critical": true,  "note": "[CRÍTICO] Source Code. Única ponte oficial que altera código de produção. Modifica STATE.md."},
    {"id": "spec_to_state",             "source": "spec.md",         "source_path": ".specs/features/spec.md",             "target": "STATE.md",            "target_path": ".specs/features/STATE.md",               "direction": "forward", "nature": "evidencia",      "layer": "tatica",         "critical": true,  "note": "Spec em progresso modifica STATE.md continuamente."},
    {"id": "state_to_journal",          "source": "STATE.md",        "source_path": ".specs/features/STATE.md",            "target": "JOURNAL.md",          "target_path": ".context/maintenance/JOURNAL.md",        "direction": "forward", "nature": "evidencia",      "layer": "tatica",         "critical": false, "note": "Dispara Handoffs no JOURNAL."},
    {"id": "state_to_validate",         "source": "STATE.md",        "source_path": ".specs/features/STATE.md",            "target": "validate_context.py", "target_path": ".context/_scripts/validate_context.py",  "direction": "forward", "nature": "evidencia",      "layer": "tatica",         "critical": false, "note": "Provê hashes criptográficas para validação."},
    {"id": "state_to_closure",          "source": "STATE.md",        "source_path": ".specs/features/STATE.md",            "target": "CLOSURE.md",          "target_path": ".specs/features/CLOSURE.md",             "direction": "forward", "nature": "evidencia",      "layer": "tatica",         "critical": false, "note": "Provê evidências para fechamento."},
    {"id": "closure_to_journal",        "source": "CLOSURE.md",      "source_path": ".specs/features/CLOSURE.md",          "target": "JOURNAL.md",          "target_path": ".context/maintenance/JOURNAL.md",        "direction": "forward", "nature": "sintese",        "layer": "tatica",         "critical": false, "note": "Consolida narrativa final no JOURNAL."},
    {"id": "closure_to_learnings",      "source": "CLOSURE.md",      "source_path": ".specs/features/CLOSURE.md",          "target": "LEARNINGS.md",        "target_path": ".context/brain/LEARNINGS.md",            "direction": "forward", "nature": "sintese",        "layer": "tatica",         "critical": false, "note": "Gera sementes de SCARs."},
    {"id": "playbook_to_spec_driver",   "source": "SSD_PLAYBOOK.md", "target_path": ".specs/features/SSD_PLAYBOOK.md",     "target": "spec-driver.md",      "target_path": ".agent/subagents/spec-driver.md",        "direction": "forward", "nature": "referencia",     "layer": "motor",          "critical": false, "note": "Comportamento tático do spec-driver."},
    {"id": "errors_ledger_to_driver",   "source": "SSD_ERRORS_LEDGER.md","source_path": ".specs/features/SSD_ERRORS_LEDGER.md","target": "spec-driver.md","target_path": ".agent/subagents/spec-driver.md",        "direction": "forward", "nature": "aprendizado",    "layer": "motor",          "critical": false, "note": "Cicatrizes influenciam comportamento tático do spec-driver."},

    {"id": "readme_sub_to_registry",    "source": "README_subagents.md","source_path": ".agent/README_subagents.md",       "target": "AGENT_REGISTRY.md",   "target_path": ".context/brain/AGENT_REGISTRY.md",       "direction": "reverse", "nature": "referencia",     "layer": "motor",          "critical": false, "note": "Documentação de agentes é afetada pelo registro."},
    {"id": "spec_v3_to_future_specs",   "source": "spec_v3.md",      "source_path": ".agent/templates/spec_v3.md",         "target": "spec.md",             "target_path": ".specs/features/spec.md",                "direction": "forward", "nature": "formacao",       "layer": "motor",          "critical": false, "note": "Template define esqueleto de toda spec futura. Specs existentes não são retroativamente afetadas."},
    {"id": "subagents_to_master_flow",  "source": "subagents/*.md",  "source_path": ".agent/subagents/",                   "target": "MASTER_FLOW.md",      "target_path": ".context/brain/MASTER_FLOW.md",          "direction": "reverse", "nature": "orquestracao",   "layer": "motor",          "critical": false, "note": "Subagentes são afetados por MASTER_FLOW e RULES."},
    {"id": "subagents_to_rules",        "source": "subagents/*.md",  "source_path": ".agent/subagents/",                   "target": "RULES.md",            "target_path": ".context/brain/RULES.md",                "direction": "reverse", "nature": "protocolo",      "layer": "motor",          "critical": false, "note": "Subagentes são afetados por RULES."},

    {"id": "context_health_to_buffer",  "source": "CONTEXT_HEALTH.md","source_path": ".context/monitoring/CONTEXT_HEALTH.md","target": "EXECUTION_BUFFER.md","target_path": ".context/monitoring/EXECUTION_BUFFER.md","direction": "forward", "nature": "degradacao",    "layer": "monitoramento",  "critical": false, "note": "Se saturado, paralisa avanço. Afeta controle de velocidade."},
    {"id": "project_index_to_bundler",  "source": "PROJECT_INDEX_01.md","source_path": ".context/monitoring/PROJECT_INDEX_01.md","target": "project_bundler.py","target_path": ".context/_scripts/project_bundler.py","direction": "reverse", "nature": "referencia",   "layer": "monitoramento",  "critical": false, "note": "Mapa topográfico gerado por autogeração."}
  ],

  "wildcard_edges": [

    {"id": "rules_to_all",              "source": "RULES.md",        "source_path": ".context/brain/RULES.md",             "target": "*",                   "nature": "protocolo",   "layer": "constitucional", "critical": true,  "note": "[CRÍTICO] TODOS. Restringe ações de MASTER_FLOW e alimenta scripts como validate_context.py.", "activation_rule": "always_if_seed_in_constitucional_or_critical"},
    {"id": "journal_from_all",          "source": "JOURNAL.md",      "source_path": ".context/maintenance/JOURNAL.md",     "target": "*",                   "nature": "metabolica",  "layer": "metabolica",     "critical": true,  "note": "[CRÍTICO] TODOS convergem aqui. Poço gravitacional — recebe dados de STATE, scripts SAM, e humano.", "activation_rule": "always_if_seed_generates_handoff_or_closure"},
    {"id": "vision_to_all",             "source": "VISION.md",       "source_path": ".context/brain/VISION.md",            "target": "*",                   "nature": "diretriz",    "layer": "estrategica",    "critical": false, "note": "Bússola do projeto. Mudança aqui pode pivotar qualquer artefato downstream.", "activation_rule": "always_if_seed_in_estrategica"}
  ]
}
```

**Nota:** Corrigi o campo `source_path` que faltava na entry `SSD_PLAYBOOK.md` — estava como `target_path`. Isso aconteceu em uma linha. Na implementação final, a validação de schema vai pegar esses erros.

---

### Contagem das edges

| Tipo | Quantidade |
|------|-----------|
| Edges normais (forward) | 33 |
| Edges reversas | 3 |
| Wildcard edges | 3 |
| **Total** | **39** |

### O que cobre e o que não cobre

| Coberto | Não coberto (Fase 2 do roadmap) |
|---------|-------------------------------|
| Seção 4 inteira: documentos de governança | Seção 5: scripts (reads/writes/trigger) |
| Wildcards para RULES, JOURNAL, VISION | Edges entre scripts e entre script↔documento |
| Layers e naturezas de todos os sinais da Seção 2 | `governance_edges.json` v2 com `script_edges` |

---

