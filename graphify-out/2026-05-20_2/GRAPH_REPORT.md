# Graph Report - .  (2026-05-20)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 458 nodes · 549 edges · 71 communities (33 shown, 38 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 19 edges (avg confidence: 0.82)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `6bf56fe1`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]
- [[_COMMUNITY_Community 13|Community 13]]
- [[_COMMUNITY_Community 14|Community 14]]
- [[_COMMUNITY_Community 15|Community 15]]
- [[_COMMUNITY_Community 16|Community 16]]
- [[_COMMUNITY_Community 17|Community 17]]
- [[_COMMUNITY_Community 18|Community 18]]
- [[_COMMUNITY_Community 19|Community 19]]
- [[_COMMUNITY_Community 20|Community 20]]
- [[_COMMUNITY_Community 21|Community 21]]
- [[_COMMUNITY_Community 22|Community 22]]
- [[_COMMUNITY_Community 23|Community 23]]
- [[_COMMUNITY_Community 24|Community 24]]
- [[_COMMUNITY_Community 25|Community 25]]
- [[_COMMUNITY_Community 26|Community 26]]
- [[_COMMUNITY_Community 27|Community 27]]
- [[_COMMUNITY_Community 28|Community 28]]
- [[_COMMUNITY_Community 29|Community 29]]
- [[_COMMUNITY_Community 30|Community 30]]
- [[_COMMUNITY_Community 31|Community 31]]
- [[_COMMUNITY_Community 32|Community 32]]
- [[_COMMUNITY_Community 33|Community 33]]
- [[_COMMUNITY_Community 34|Community 34]]
- [[_COMMUNITY_Community 37|Community 37]]
- [[_COMMUNITY_Community 38|Community 38]]
- [[_COMMUNITY_Community 39|Community 39]]
- [[_COMMUNITY_Community 40|Community 40]]
- [[_COMMUNITY_Community 41|Community 41]]
- [[_COMMUNITY_Community 43|Community 43]]
- [[_COMMUNITY_Community 44|Community 44]]
- [[_COMMUNITY_Community 45|Community 45]]
- [[_COMMUNITY_Community 46|Community 46]]
- [[_COMMUNITY_Community 47|Community 47]]
- [[_COMMUNITY_Community 48|Community 48]]
- [[_COMMUNITY_Community 49|Community 49]]
- [[_COMMUNITY_Community 50|Community 50]]
- [[_COMMUNITY_Community 51|Community 51]]
- [[_COMMUNITY_Community 52|Community 52]]
- [[_COMMUNITY_Community 53|Community 53]]
- [[_COMMUNITY_Community 54|Community 54]]
- [[_COMMUNITY_Community 55|Community 55]]
- [[_COMMUNITY_Community 56|Community 56]]
- [[_COMMUNITY_Community 57|Community 57]]
- [[_COMMUNITY_Community 58|Community 58]]
- [[_COMMUNITY_Community 59|Community 59]]
- [[_COMMUNITY_Community 60|Community 60]]
- [[_COMMUNITY_Community 61|Community 61]]
- [[_COMMUNITY_Community 62|Community 62]]
- [[_COMMUNITY_Community 63|Community 63]]
- [[_COMMUNITY_Community 64|Community 64]]
- [[_COMMUNITY_Community 65|Community 65]]
- [[_COMMUNITY_Community 66|Community 66]]
- [[_COMMUNITY_Community 67|Community 67]]
- [[_COMMUNITY_Community 68|Community 68]]
- [[_COMMUNITY_Community 69|Community 69]]
- [[_COMMUNITY_Community 70|Community 70]]

## God Nodes (most connected - your core abstractions)
1. `scripts` - 27 edges
2. `TestOracleV3` - 16 edges
3. `validate()` - 15 edges
4. `collect_files()` - 13 edges
5. `main()` - 12 edges
6. `TestContextGovernance` - 12 edges
7. `generate_context_markdown()` - 9 edges
8. `workflow_journal_auditor.py (SAM)` - 9 edges
9. `format_ts()` - 7 edges
10. `TestAffinityLogic` - 7 edges

## Surprising Connections (you probably didn't know these)
- `System Anti-Migué (SAM)` --implements--> `Harness Runner Script`  [INFERRED]
  .specs/features/SSD_PLAYBOOK.md → .context/_scripts/harness_runner.py
- `MiMo Memory Injection` --implements--> `Inject Learnings Script`  [EXTRACTED]
  .specs/features/SSD_PLAYBOOK.md → .context/_scripts/inject_learnings.py
- `Context Health Check Workflow` --calls--> `Validate Context Script`  [EXTRACTED]
  .github/workflows/context-health.yml → .context/_scripts/validate_context.py
- `Context Health Check Workflow` --calls--> `Secrets Scanner Script`  [EXTRACTED]
  .github/workflows/context-health.yml → .context/_scripts/secrets_scanner.py
- `SSD-Chain Playbook` --references--> `Write with Validation Script`  [EXTRACTED]
  .specs/features/SSD_PLAYBOOK.md → .context/_scripts/write_with_validation.py

## Communities (71 total, 38 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.08
Nodes (37): H.O.K Governor (Farol de Bom Senso), MASTER_FLOW.md: Estrutura de Contexto em Camadas, Antigravity Kit v2.5.2 Hardened, README_CONTEXT.md — Guia de Operação Chain-Skills V3, RULES.md — Template Universal de Governança, check_enrichment_integrity(), check_epistemological_gate(), check_handoff_integrity() (+29 more)

### Community 1 - "Community 1"
Cohesion: 0.06
Nodes (34): author, description, devDependencies, husky, keywords, license, name, scripts (+26 more)

### Community 2 - "Community 2"
Cohesion: 0.09
Nodes (13): Artigo com aliases no frontmatter deve ser encontrado por alias., Busca por 'QA' não deve retornar vazio., Buscas por 'testar', 'teste' e 'testes' devem convergir para a mesma raiz., Match por tag (1.0) deve ter confidence > match por corpo acumulado., Top-N: Rank 1 retorna integral, Ranks 2 e 3 retornam apenas o ## Resumo se aplic, Query com termo existente retorna resultado com confidence > 0., Query sem match retorna status missing (ou msg informativa) e confidence 0., Busca por 'harness' retorna artigo de harness, não outro. (+5 more)

### Community 3 - "Community 3"
Cohesion: 0.12
Nodes (27): Health Check do Contexto - Dashboard, check_atomic_transition(), check_files(), check_journal_chronology(), check_journal_lines(), check_metadata_freshness(), check_registry_structure(), check_specs_structure() (+19 more)

### Community 4 - "Community 4"
Cohesion: 0.15
Nodes (26): BundleConfig, Chunk, chunk_content(), classify_domain(), collect_files(), extract_imports(), extract_symbols(), FileRecord (+18 more)

### Community 5 - "Community 5"
Cohesion: 0.11
Nodes (21): AGENT_REGISTRY.md (DNS Cognitivo), Regra: Freio de Propagação (Flash Guard), Flow Journal-Sync Architecture, Governance Friction Analyst, Inception: Strategic Boundaries, JOURNAL.md (Diário de Bordo), Journal (Active Log), Journal Sync & Blast Radius Propagator (+13 more)

### Community 6 - "Community 6"
Cohesion: 0.15
Nodes (18): Harness Registry, Harness Runner Script, Inject Learnings Script, MiMo Memory Injection, Spec-Driver V3: Engineering of Paranoia, System Anti-Migué (SAM), get_active_features(), inject_to_feature() (+10 more)

### Community 7 - "Community 7"
Cohesion: 0.16
Nodes (6): ACTIVE + Valid Context -> Exit 0, DRAFT + No Vision + Clean Context -> Exit 0, DRAFT + VISION.md -> Exit 2, TRANSLATION_LOCK -> Exit 2, DRAFT + Existing Code -> Exit 1 (Strategic Breach), TestContextGovernance

### Community 8 - "Community 8"
Cohesion: 0.19
Nodes (5): JOURNAL.md (Memoria Curta), JOURNAL_SYNAPSE.md (Matriz de Gatilhos), RX: Biologia Funcional do Framework, RX-COMMUNICATIONS: Mapa de Conectividade Global, RX: H.O.K Learnings (Governança Cognitiva)

### Community 9 - "Community 9"
Cohesion: 0.20
Nodes (12): count_journal_metrics(), count_pending_migrations(), count_schema_tables(), estimate_tokens(), update_dashboard(), get_package_deps(), get_schema_tables(), sync_requirements() (+4 more)

### Community 10 - "Community 10"
Cohesion: 0.15
Nodes (13): affinity_scanner.py, Harness Engineering Manifesto, LEARNINGS.md, secrets_scanner.py, Oracle v3, harness_runner.py, JOURNAL_SYNAPSE, run_context.py (+5 more)

### Community 11 - "Community 11"
Cohesion: 0.29
Nodes (11): Flow Oracle & Wiki Mapping, append_to_wiki_log(), build_index(), load_index_file(), normalize_text(), query_oracle(), Busca no oráculo de forma imparcial e robusta.     O parâmetro 'role' foi removi, Remove acentos, markdown e normaliza para lowercase. (+3 more)

### Community 12 - "Community 12"
Cohesion: 0.26
Nodes (5): calculate_jaccard(), find_references(), Busca referências ao nome do arquivo (stem) no conteúdo usando Word Boundaries., Calcula o índice de Jaccard entre dois conjuntos., TestAffinityLogic

### Community 13 - "Community 13"
Cohesion: 0.17
Nodes (11): Behaviour Harness, Ralph Wiggum Loop, Global Rules, Retorna (ok: bool, reason: str), validate_write(), Spec-Driver Subagent, Feature: Otimização Spec-Driven V3, Spec V3 Template (+3 more)

### Community 14 - "Community 14"
Cohesion: 0.31
Nodes (9): calculate_score(), generate_learnings_md(), main(), Gera o arquivo LEARNINGS.md estruturado., Lê o Ledger focado no Formato B (Scars)., Analisa o HARNESS_LOG.md em busca de falhas recorrentes., Calcula a relevância da Scar com Decaimento e Frequência., safe_parse_harness_log() (+1 more)

### Community 15 - "Community 15"
Cohesion: 0.33
Nodes (8): check_market_coverage(), get_inception_status(), main(), Verifica se entidades críticas possuem lastro REAL em compliance/ ou research/., Registra gaps detectados no MARKET_INBOX.md (uma linha por entidade)., Lê o status do Inception mestre., scan_entities(), update_inbox()

### Community 16 - "Community 16"
Cohesion: 0.22
Nodes (8): results, run_id, stats, dead_refs, ghosts, healthy, processed, timestamp

### Community 17 - "Community 17"
Cohesion: 0.22
Nodes (9): Agent Registry, Governance Rules Hardening Spec, @qa-validator, Rules, Script Glossary, SDD Errors Ledger, SDD Playbook, Relatório Operacional SDD (+1 more)

### Community 18 - "Community 18"
Cohesion: 0.42
Nodes (8): description, name, parameters, content, file_path, task_id, required, type

### Community 19 - "Community 19"
Cohesion: 0.36
Nodes (7): append_to_wiki_log(), check_wiki(), find_raw_sources(), Lista arquivos na inbox RAW para sugestão., Heurística simples: busca palavras-chave do claim nos nomes dos arquivos RAW., Varre a wiki em busca de claims sem citação., suggest_source()

### Community 20 - "Community 20"
Cohesion: 0.25
Nodes (4): Valida se o decaimento temporal altera o score corretamente., Valida se falhas no harness aumentam o score., Valida se o injetor prioriza scars com palavras-chave da spec., TestMiMoMemory

### Community 21 - "Community 21"
Cohesion: 0.38
Nodes (3): check_deps(), detect_pkg_mgr(), error()

### Community 22 - "Community 22"
Cohesion: 0.53
Nodes (5): archive_spec(), cleanup(), get_specs(), is_protected(), Verifica se a spec está protegida (ex: sprint ativa em modo sprint_based).

### Community 23 - "Community 23"
Cohesion: 0.53
Nodes (5): append_to_wiki_log(), main(), Reconstrói o _index.md de forma atômica para evitar corrupção de leitura., rebuild_index_atomic(), validate_article()

### Community 24 - "Community 24"
Cohesion: 0.40
Nodes (5): Proposta Operacional: Spec-Driven Contract Sprints, Plano de Arquitetura: A Dança Multi-Agent (Hub & Spoke), Plano: Governance Rules Hardening, Plano Completo V2 (Caminho Seguro), RULES.md

### Community 25 - "Community 25"
Cohesion: 0.60
Nodes (4): get_inception_status(), main(), Lê o status do Inception mestre., run_script()

### Community 26 - "Community 26"
Cohesion: 0.40
Nodes (5): Context Health Check Workflow, Harness Log, Prompt Library, Secrets Scanner Script, Validate Context Script

### Community 27 - "Community 27"
Cohesion: 0.50
Nodes (4): Auditoria Crítica do Plano Consolidado Oracle v3, Plano LEARNINGS v2, Log Cronológico dos Planos Oracle v3, Plano Consolidado: Evolução do Oracle v3

### Community 31 - "Community 31"
Cohesion: 0.67
Nodes (3): INCEPTION.md, 🌐 market/, @spec-enricher

### Community 33 - "Community 33"
Cohesion: 0.67
Nodes (3): run_context.py (Orquestrador V2.3.1 HARDENED), validate_context.py (V2.3.1 HARDENED), Walkthrough: Implantação da Tríade H.O.K

## Knowledge Gaps
- **120 isolated node(s):** `name`, `version`, `description`, `context:validate`, `context:sync` (+115 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **38 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `workflow_journal_auditor.py (SAM)` connect `Community 5` to `Community 8`?**
  _High betweenness centrality (0.045) - this node is a cross-community bridge._
- **Why does `Governance Rules Hardening Spec` connect `Community 17` to `Community 0`, `Community 3`?**
  _High betweenness centrality (0.044) - this node is a cross-community bridge._
- **Why does `RX: SAM (Sistema Anti-Migué)` connect `Community 5` to `Community 0`?**
  _High betweenness centrality (0.030) - this node is a cross-community bridge._
- **What connects `name`, `version`, `description` to the rest of the system?**
  _196 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.07681365576102418 - nodes in this community are weakly interconnected._
- **Should `Community 1` be split into smaller, more focused modules?**
  _Cohesion score 0.05714285714285714 - nodes in this community are weakly interconnected._
- **Should `Community 2` be split into smaller, more focused modules?**
  _Cohesion score 0.09359605911330049 - nodes in this community are weakly interconnected._