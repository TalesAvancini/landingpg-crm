---
contract_version: 2.5.2
parties: ["@spec-driver", "@qa-validator"]
type: standard
executor_context_id: "CTX_EXE_HUB_SPOKE"
validator_context_id: "CTX_VAL_DANCE_VERIFIED"
impact_control:
  max_impact_radius: 7
  pre_flight_grep_terms: ["AGENT_REGISTRY.md", "MASTER_FLOW.md", "RULES.md", "harness_runner.py"]
definition_of_done:
  - [x] O arquivo `.specs/_template.md` deve conter o bloco `impact_control` no frontmatter YAML.
  - [x] O script `.context/_scripts/harness_runner.py` deve implementar a lógica de `check_impact_radius` (comparando `git diff --porcelain` com `max_impact_radius`).
  - [x] O `AGENT_REGISTRY.md` deve listar explicitamente as skills obrigatórias/proibidas do Executor e proibir escrita em `brain/` ou `market/`.
  - [x] O `MASTER_FLOW.md` e o `RULES.md` devem documentar a "Dança Multi-Agent" (Pre-flight, SCOPE_BLOWOUT e Telemetria no STATE.md).
qa_signoff: true
signed_by: "@qa-validator"
---

# 📄 Spec: Implementação da Arquitetura Hub & Spoke

## 🎯 Objetivo
Materializar as decisões documentadas no `plano_coreografia_multi_agent.md` nos arquivos de governança (brain) e na automação do framework (Harness). Isso tornará o Antigravity oficialmente um framework de orquestração Multi-Agent determinístico.

## ⚠️ Pre-Flight Gate (Impact Check)
O Executor (`@spec-driver`) deve usar `codenavi`/grep para os termos listados em `pre_flight_grep_terms`.
- Se o número de arquivos detectados exceder `max_impact_radius` (5), alterar o `STATE.md` para `Status: ⚠️ SCOPE_BLOWOUT`, logar a telemetria e abortar a execução.
- Se `<= 5`, registrar no `STATE.md` os alvos e iniciar a implementação, utilizando o `flash-harness` para registro sequencial.

## 🔎 Regra de Segregação
- Sendo `type: standard`, o Validador (`@qa-validator`) DEVE possuir um contexto isolado e o `validator_context_id` deve ser diferente do `executor_context_id`. O QA só poderá assinar `qa_signoff: true` se o formato do log e a telemetria estiverem presentes no `STATE.md`.
