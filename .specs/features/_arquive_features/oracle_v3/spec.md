---
contract_version: 2.5.2
parties: ["@spec-driver", "@qa-validator"]
type: standard
executor_context_id: "CTX_ORACLE_V3_DEV"
validator_context_id: "CTX_QA_VALIDATOR"
impact_control:
  max_impact_radius: 10
  pre_flight_grep_terms: ["context_oracle.py", "harness_runner.py", "ingest_wiki_guard.py", "lint_wiki.py", "test_oracle.py", "PROMPT_LIBRARY.md"]
definition_of_done:
  - [x] Fase -1: test_oracle.py criado usando pathlib estrito (sem hardcoded slashes).
  - [x] Fase 0.1: Normalização pré-query adicionada em context_oracle.py.
  - [x] Fase 0.2: _index.md regenerado atômicamente com retry backoff para PermissionError (Windows).
  - [x] Fase 0.3: Aliases extraídos do frontmatter e injetados com peso 1.0.
  - [x] Fase 0.4: Filtro léxico poupa siglas de 2 caracteres conhecidas no domínio.
  - [x] Fase 0.5: build_index levanta warnings formais em vez de except: continue.
  - [x] Fase 1.1: simple_stem() pt-br adicionado com whitelist enxuta e estática.
  - [x] Fase 1.2: Cálculo de confidence recalibrado para priorizar matches exatos sobre acúmulos.
  - [x] Fase 1.3: Oracle retorna Top-N (até 3 resultados) graduados (apenas ## Resumo para rank 2 e 3).
  - [x] Fase 1.4: Resposta padronizada no Schema JSON v3 (incluindo campo warnings).
  - [x] Fase 2.1: Lógica imparcial garantida (sem multiplicadores injustos por role).
  - [x] Fase 2.2: Gravação no wiki_log.md via try/except não-bloqueante (fire-and-forget).
  - [x] Fase 2.3: PROMPT_LIBRARY.md atualizado com a diretriz de consulta prévia ao Oracle.
  - [x] Fase 2.4: ~Cache em disco (.wiki_index.cache.json)~ CORTADO (Decisão The Fool: JSON paralelo é SSOT duplicado do _index.md).
  - [x] Fase 2.5: Script oracle_analytics.py criado para parseamento robusto do log.
  - [x] Fase 2.6: harness_runner.py usa oracle (Gate Epistemológico light) via import direto com timeout.

qa_signoff: true
signed_by: "@qa-validator"
---

# 📄 Spec: Evolução do Oracle v3 (Consolidado e Auditado)

## 🎯 Objetivo
Transformar o `context_oracle.py` e suas dependências de um MVP passivo em um subsistema resiliente e acurado, que serve de motor léxico tanto para a IA quanto para a automação do Antigravity (Harness). A reconstrução segue o rigor de **Consertar primeiro. Calibrar depois. Integrar por último.** 

O escopo é estrito ao estabelecido entre o Plano Consolidado original e a bateria dupla de auditorias The Fool + MiMo (v3).

## ✅ Critérios de Aceite Genéricos
1. **Zero Quebras:** `npm run context:all` deve passar integralmente no Windows sem travamentos de I/O.
2. **Cobertura Ativa:** O `tests/test_oracle.py` deve possuir todos os testes BASELINE e TARGET cobrindo o escopo das Fases -1 a 1.
3. **Módulo Nativo:** O Harness não perde mais do que 2s para invocar o Oracle internamente.
4. **Resiliência:** A reconstrução do índice não apaga o índice atual se a compilação falhar no meio do caminho.

## 🔎 Regra de Segregação
- Sendo de classe `type: standard` no Antigravity v2.5.2, esta spec só pode ser fechada (`qa_signoff: true`) se o `validator_context_id` (o subagente QA) aprovar o trabalho em uma sessão autônoma e dissociada do agente executor original (`@spec-driver`).
