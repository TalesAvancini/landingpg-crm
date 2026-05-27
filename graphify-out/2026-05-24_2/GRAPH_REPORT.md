# Graph Report - template_inicío_de_projeto  (2026-05-24)

## Corpus Check
- 116 files · ~84,607 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1190 nodes · 1230 edges · 109 communities (91 shown, 18 thin omitted)
- Extraction: 99% EXTRACTED · 1% INFERRED · 0% AMBIGUOUS · INFERRED: 9 edges (avg confidence: 0.8)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `feafa835`
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
- [[_COMMUNITY_Community 35|Community 35]]
- [[_COMMUNITY_Community 36|Community 36]]
- [[_COMMUNITY_Community 37|Community 37]]
- [[_COMMUNITY_Community 38|Community 38]]
- [[_COMMUNITY_Community 39|Community 39]]
- [[_COMMUNITY_Community 40|Community 40]]
- [[_COMMUNITY_Community 41|Community 41]]
- [[_COMMUNITY_Community 42|Community 42]]
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
- [[_COMMUNITY_Community 71|Community 71]]
- [[_COMMUNITY_Community 72|Community 72]]
- [[_COMMUNITY_Community 73|Community 73]]
- [[_COMMUNITY_Community 74|Community 74]]
- [[_COMMUNITY_Community 75|Community 75]]
- [[_COMMUNITY_Community 76|Community 76]]
- [[_COMMUNITY_Community 77|Community 77]]
- [[_COMMUNITY_Community 78|Community 78]]
- [[_COMMUNITY_Community 79|Community 79]]
- [[_COMMUNITY_Community 80|Community 80]]
- [[_COMMUNITY_Community 81|Community 81]]
- [[_COMMUNITY_Community 82|Community 82]]
- [[_COMMUNITY_Community 83|Community 83]]
- [[_COMMUNITY_Community 84|Community 84]]
- [[_COMMUNITY_Community 85|Community 85]]
- [[_COMMUNITY_Community 86|Community 86]]
- [[_COMMUNITY_Community 87|Community 87]]
- [[_COMMUNITY_Community 88|Community 88]]
- [[_COMMUNITY_Community 89|Community 89]]
- [[_COMMUNITY_Community 90|Community 90]]
- [[_COMMUNITY_Community 91|Community 91]]
- [[_COMMUNITY_Community 92|Community 92]]
- [[_COMMUNITY_Community 93|Community 93]]
- [[_COMMUNITY_Community 94|Community 94]]
- [[_COMMUNITY_Community 95|Community 95]]
- [[_COMMUNITY_Community 97|Community 97]]
- [[_COMMUNITY_Community 98|Community 98]]
- [[_COMMUNITY_Community 99|Community 99]]
- [[_COMMUNITY_Community 101|Community 101]]
- [[_COMMUNITY_Community 102|Community 102]]

## God Nodes (most connected - your core abstractions)
1. `scripts` - 29 edges
2. `📜 RULES.md — Template Universal de Contexto & Governança` - 28 edges
3. `JOURNAL.md (Memoria Curta)` - 26 edges
4. `TestOracleV3` - 16 edges
5. `validate()` - 15 edges
6. `collect_files()` - 13 edges
7. `main()` - 12 edges
8. `TestContextGovernance` - 12 edges
9. `AffinityLite` - 9 edges
10. `generate_context_markdown()` - 9 edges

## Surprising Connections (you probably didn't know these)
- `update_state_md()` --calls--> `format_ts()`  [INFERRED]
  .context/_scripts/harness_runner.py → .context/_scripts/_tz_utils.py
- `update_dashboard()` --calls--> `format_ts()`  [INFERRED]
  .context/_scripts/health_sync.py → .context/_scripts/_tz_utils.py
- `purge_journal()` --calls--> `format_ts()`  [INFERRED]
  .context/_scripts/purge_journal.py → .context/_scripts/_tz_utils.py
- `sync_requirements()` --calls--> `format_ts()`  [INFERRED]
  .context/_scripts/sync_project.py → .context/_scripts/_tz_utils.py

## Communities (109 total, 18 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.01
Nodes (169): [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:34, [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:34, [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:34, [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:34, [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:34, [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:34, [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:34, [GOVERNANCE-FRICTION] GF-JOURNAL-ORDER | 2026-04-30 22:34 (+161 more)

### Community 1 - "Community 1"
Cohesion: 0.06
Nodes (45): check_enrichment_integrity(), check_epistemological_gate(), check_handoff_integrity(), check_impact_radius(), check_journal_sam(), check_schema_contract(), check_sprint_contract(), check_strategic_alignment() (+37 more)

### Community 2 - "Community 2"
Cohesion: 0.05
Nodes (37): author, description, devDependencies, husky, keywords, license, name, scripts (+29 more)

### Community 3 - "Community 3"
Cohesion: 0.07
Nodes (29): 🔄 0.1 Ciclo de Vida do Inception (Hybrid Discovery), 🏗️ 0. Máquina de Estados (`PROJECT_MODE`), 📊 10. Dashboard Health Sync, 🛡️ 1.10 Regra `EXECUTION_GATEKEEPER` (Fail-Closed & Resume Protocol), 🛡️ 1.11 Regra `MIMO_MANDATORY_INJECTION` (Memória Ativa), 🛡️ 1.12 Regra `SAM_SYNTAX_STRICTNESS` (Rigidez de Sintaxe), 🛡️ 1.13 Protocolo de Sincronia de Metadados (Metadata-Only Propagation), 🛡️ 1.14 Protocolo de Fechamento de Feature (Closure Thinking) (+21 more)

### Community 4 - "Community 4"
Cohesion: 0.09
Nodes (13): Artigo com aliases no frontmatter deve ser encontrado por alias., Busca por 'QA' não deve retornar vazio., Buscas por 'testar', 'teste' e 'testes' devem convergir para a mesma raiz., Match por tag (1.0) deve ter confidence > match por corpo acumulado., Top-N: Rank 1 retorna integral, Ranks 2 e 3 retornam apenas o ## Resumo se aplic, Query com termo existente retorna resultado com confidence > 0., Query sem match retorna status missing (ou msg informativa) e confidence 0., Busca por 'harness' retorna artigo de harness, não outro. (+5 more)

### Community 5 - "Community 5"
Cohesion: 0.10
Nodes (20): check_freshness(), classify(), load_graph_as_file_adjacency(), main(), normalize_seed(), parse_rx_communications(), Retorna (commits_behind, is_stale)., Normaliza paths do seed. (+12 more)

### Community 6 - "Community 6"
Cohesion: 0.07
Nodes (26): 📅 2026-05-20 17:45 | 🚀 Instalação: Integração do Graphify no Repositório #Tooling #Installation #Graphify, 📅 2026-05-20 19:10 | 🛠️ Ajuste: Exclusão do Graphify do Bundle de Contexto #Tooling #Refactor #Graphify, 📅 2026-05-22 00:37 | 🚀 Implantação: Calculadora Blast Radius MVP & Sincronização #Governance #Verification #Tooling #Hardening, 📅 2026-05-22 01:08 | 🛠️ Ajuste: Setup Pre-Flight do SDD Orchestrator #Setup #Governance #Roles #Agents, 📅 2026-05-22 01:25 | 🏁 Closure: Blast Radius MVP #Governance #Verification #Tooling, 📅 2026-05-22 01:35 | 🏁 Signoff: Homologação e Assinatura do QA #Governance #Validation, 📅 2026-05-22 01:48 | 🛠️ Ajuste: Reforço de Git Cleanliness na Skill do SDD Orquestrador #Setup #Governance #Rules, 📅 2026-05-22 13:42 | 🚀 Implantação: FLOW_PROPAGATION.md, Skill flow-auditor e Alinhamento de Governança #Documentation #Governance #Setup #Governança #Regras (+18 more)

### Community 7 - "Community 7"
Cohesion: 0.15
Nodes (26): BundleConfig, Chunk, chunk_content(), classify_domain(), collect_files(), extract_imports(), extract_symbols(), FileRecord (+18 more)

### Community 8 - "Community 8"
Cohesion: 0.13
Nodes (26): check_atomic_transition(), check_files(), check_journal_chronology(), check_journal_lines(), check_metadata_freshness(), check_registry_structure(), check_specs_structure(), check_sprint_acceptance_sync() (+18 more)

### Community 9 - "Community 9"
Cohesion: 0.08
Nodes (24): 🗺️ 1. Diagrama de Arquitetura (Visão Holística), 1. `RULES.md` — As Leis do Ecossistema, 2. `MASTER_FLOW.md` — A Orquestração, 🧬 2. Perfil Individual dos 9 Arquivos, 3. `AGENT_REGISTRY.md` — O DNS Cognitivo, 🔄 3. Matriz de Propagação de Mudanças, ⛓️ 4. Sequência de Execução (A Cadeia das 9 Skills), 4. `spec-driver.md` — O Executor Mecânico (+16 more)

### Community 10 - "Community 10"
Cohesion: 0.10
Nodes (20): 1.1 Ordem Cronológica Reversa, 1.2 O Limite Heurístico e o `purge_journal.py`, 1.3 Anatomia de uma Entrada Perfeita, 🧭 1. A Mecânica do Journal (O Diário de Bordo), 🤖 2. SAM (Auditoria Anti-Migué) e a Regra do Jogo, 3.1 Zonas Ignoradas (`IGNORED_PREFIXES`), 3.2 Os Shadow Files (`SHADOW_FILES`), 3.3 O Curto-Circuito do Diário (Gatilho de Estado) (+12 more)

### Community 11 - "Community 11"
Cohesion: 0.10
Nodes (20): 🌌 1. Mapa Mestre de Conectividade (Visão Holística), 🔗 2. Tabela de Sinais de Conectividade, 🛡️ 3. Governança da Conectividade, 🕸️ 4. Matriz de Acoplamento Granular (Adjacency List), ⚙️ 5. Matriz de Acoplamento de Automação (Scripts), 🤖 Agentes (`.agent/`), code:mermaid (graph TD), 🧠 Córtex (`.context/brain/`) (+12 more)

### Community 12 - "Community 12"
Cohesion: 0.11
Nodes (17): 1. @spec-driver (Pre-close Self-Audit), 2. @qa-validator (Audit & Signoff), 🤖 AGENT_REGISTRY.md, 🛡️ Blindagem de Subagente (Chain-Skills V3), 📊 Camada de Telemetria [GOVERNANCE-FRICTION], code:text (1. Receber comando → 2. Consultar AGENT_REGISTRY.md → 3. Ide), code:markdown (### `@nome-da-nova-role`), code:text (✅ Registry está sincronizado com o código? (Novas pastas têm) (+9 more)

### Community 13 - "Community 13"
Cohesion: 0.16
Nodes (6): ACTIVE + Valid Context -> Exit 0, DRAFT + No Vision + Clean Context -> Exit 0, DRAFT + VISION.md -> Exit 2, TRANSLATION_LOCK -> Exit 2, DRAFT + Existing Code -> Exit 1 (Strategic Breach), TestContextGovernance

### Community 14 - "Community 14"
Cohesion: 0.12
Nodes (15): description, required, type, description, description, required, type, name (+7 more)

### Community 15 - "Community 15"
Cohesion: 0.12
Nodes (15): 1. `.context/` - A Camada de Governança, 2. `.specs/` - A Camada de Execução (TLC), 🛡️ A Tríade H.O.K. (Governança Nível 3), 📂 Anatomia do Repositório, 🛸 Antigravity Kit v2.5.2 Hardened (H.O.K. Enabled), Cenário 1: Repositório Novo (Template), Cenário 2: Aplicando a projetos existentes (Bootstrapper), code:bash (npm install) (+7 more)

### Community 16 - "Community 16"
Cohesion: 0.13
Nodes (14): 1. Tolerância à Exploração (Escopo vs. Burocracia), 2. Correção Estrutural (Anti-Bypass), 3. Paradigma de Alertas e Conflitos (Evolução Contínua), 4. A Bússola Cognitiva (Prevenção de Poluição de Domínio), 5. Protocolo de Estudo Tectônico (Sistematização), 6. Propagação de Mudança Dinâmica (Anti-Drift), 📥 CARGA DE CONTEXTO SUPREMA (Protocolo Boot), code:mermaid (graph TD) (+6 more)

### Community 17 - "Community 17"
Cohesion: 0.14
Nodes (13): 🗺️ 1. Visão Holística (A Pedra no Lago), ⚙️ 2. O Motor Duplo (A Física vs A Política), 🧮 3. A Matemática dos 3 Buckets, 📝 4. Tabela de Ação (Cheat Sheet), 🎬 5. O Fluxo de Execução (Nos Bastidores), code:mermaid (graph TD), code:mermaid (sequenceDiagram), 🔵 DECLARED ONLY (Só na Política) (+5 more)

### Community 18 - "Community 18"
Cohesion: 0.14
Nodes (13): Anti-Patterns (NÃO faça), Error: Fraude Narrativa, Error: Propagação incompleta, Error: SAM pre-commit fails, Instructions, Journal Sync & Blast Radius Propagator (v2.3.0 - Recursive Reasoning), Step 0: Reality Check (Short-Circuit), Step 1: Journal & SAM Sync (+5 more)

### Community 19 - "Community 19"
Cohesion: 0.14
Nodes (13): 1. Clonar o Template, 2. Romper o vínculo com o Antigravity (Reset do Git), 3. Iniciar seu novo Repositório, 4. Conectar ao seu NOVO repositório no GitHub, 5. Ativar o Motor de Governança, code:powershell (git clone https://github.com/TalesAvancini/template-ai-conte), code:powershell (# No Windows (PowerShell)), code:powershell (git init) (+5 more)

### Community 20 - "Community 20"
Cohesion: 0.15
Nodes (12): 🏗️ 1. Setup do Ambiente, ⚙️ 2. Ferramentas de Automação, 🗃️ 3. Recuperação de Contexto (Archive), 🚨 4. Troubleshooting, code:bash (npm run context:validate  # Checa integridade e tokens), code:bash (make validate), code:bash (./run_context.sh validate), 🛠️ Manual de Reconstrução & Automação (+4 more)

### Community 21 - "Community 21"
Cohesion: 0.15
Nodes (12): 1. O Que é o SAM?, 2. Fluxograma de Execução (Husky Gate), 🌪️ 3.1 Blast Radius Recursivo, 👥 3.2 Segregação de Contexto (4-Eyes Principle), 🛑 3.3 Fail-Closed Gatekeeper, 🤖 3.4 Arquivos Sombra e o Gatilho de Estado do Diário (Curto-Circuito), 3. Conceitos Avançados de Governança, 4. Tipos de Violação Detectados (+4 more)

### Community 22 - "Community 22"
Cohesion: 0.15
Nodes (12): code:bash (python .context/_scripts/blast_radius.py --changed <PROPAGAT), code:bash (npm run context:inject), Example 1: Escalation Handling, Examples, Instructions, SDD Orchestrator, Step 0: Pre-Flight Check (Git Cleanliness Baseline), Step 1: Blast Radius Calculation (Propagation Matrix) (+4 more)

### Community 23 - "Community 23"
Cohesion: 0.17
Nodes (11): ✅ Checklist de Arquivos do Flow, code:mermaid (graph TD), code:block2 (1. Humano deposita dossiê → market/RAW/nome.md), 📂 Dados e Armazenamento, 📊 Diagrama do Pipeline, 📡 Documentação de Topologia, 🔍 Flow Oracle & Wiki — Mapeamento Completo, 📜 Governança (Regras que restringem o Flow) (+3 more)

### Community 24 - "Community 24"
Cohesion: 0.17
Nodes (11): 🕒 1. Metadados Obrigatórios, 📂 2. Estrutura de Governança (Context & Specs), 🔄 3. O Ciclo Macro do TLC (Ponteiros de Execução), 4.1. O Gatilho de Fricção Operacional `[GOVERNANCE-FRICTION]`, 4.2. Arquivamento e Imutabilidade (PRD e Schema), 4.3. A Regra do Purge (JOURNAL.md), 4.4. Efemeridade do Workshop (.specs/), 🛡️ 4. As Leis de Macro-Manutenção (+3 more)

### Community 25 - "Community 25"
Cohesion: 0.17
Nodes (11): code:markdown (### Goal), gov-friction-analyst (Governance Friction Analyst), ⚠️ Limitações e Contenções, Passo 1: Diagnóstico Mapeado, Passo 2: O Filtro "Overkill Radar", Passo 3: Checklist de Causa -> Efeito -> Vacina, Passo 4: Plano de Ação Estruturado, 🎯 Purpose (+3 more)

### Community 26 - "Community 26"
Cohesion: 0.17
Nodes (11): ⚙️ 1. O Agregador (`learnings_aggregator.py`), 1. O Que é o Learnings Framework?, 📚 2. A Memória Central (`LEARNINGS.md`), 2. Arquitetura Visual (O Fluxo da Memória), 💉 3. O Injetor (`inject_learnings.py`), 3. Os Componentes Vitais, 🧪 4. A Spec Enriquecida (`.enriched.md`), 4. Mecânicas Avançadas de Governança (+3 more)

### Community 27 - "Community 27"
Cohesion: 0.17
Nodes (11): 1. Introdução: O Fim do "Vibe Coding", 2. A Ontologia do Harness, 3.1. Guias (Feedforward), 3.2. Sensores (Feedback), 3. A Teoria de Controle: Feedforward vs. Feedback, 4. As Três Categorias de Harness de Software, 5. Patologias de IA e a Separação de Papéis, 6. Padrões de Execução: O "Ralph Wiggum Loop" (+3 more)

### Community 28 - "Community 28"
Cohesion: 0.17
Nodes (11): 1. [FATAL] Modificação Silenciosa (Harness / SAM), 2. [HG01] Violação de Escopo Sprint, 3. [BLOCKED] Task 'X' já está concluída, 4. 💉 Injeção de Contexto (MiMo), 5. [BLOCKED] Falta de Justificativa de Tier, 6. [FAIL] Substituição Vazia (Empty Diff), 🧠 AGENT_SCRATCHPAD, 📤 DIRECTIVES (Resoluções do Orquestrador) (+3 more)

### Community 29 - "Community 29"
Cohesion: 0.26
Nodes (5): calculate_jaccard(), find_references(), Busca referências ao nome do arquivo (stem) no conteúdo usando Word Boundaries., Calcula o índice de Jaccard entre dois conjuntos., TestAffinityLogic

### Community 30 - "Community 30"
Cohesion: 0.18
Nodes (10): ⚠️ Alertas Automáticos (Harness Log), 🧠 LEARNINGS.md (Memória Estratégica MiMo), [SCAR-001] Edição Destrutiva de Estado (Regex Agressivo) (Score: 324), [SCAR-002] Execução Irresponsável (Bypass de Planejamento) (Score: 171), [SCAR-003] Configuração Híbrida Inválida (Modo Sprint vs Standard) (Score: 108), [SCAR-004] Drift de Baseline (start_hash desatualizado) (Score: 108), [SCAR-005] Fechamento Prematuro de Task (Acceptance Pendente) (Score: 108), [SCAR-006] Deriva de Atenção e Falhas de Regex (Surgical Edits) (Score: 90) (+2 more)

### Community 31 - "Community 31"
Cohesion: 0.18
Nodes (10): 1. O Sistema Nervoso Central (`run_context.py`), 2. O Sistema Imunológico (`harness_runner.py`), 3. A Glândula de Crescimento (`sync_project.py` & `enrich_context.py`), 4. O Sistema de Excreção (`purge_journal.py` & `cleanup_specs.py`), code:mermaid (graph LR), 📈 Evolução (O Futuro RX do Produto), 🔄 O Metabolismo (Ciclo de Vida do Contexto), 🛡️ Regras de Homeostase (Estabilidade) (+2 more)

### Community 32 - "Community 32"
Cohesion: 0.18
Nodes (10): 1. Modelo de Linguagem Flash (Velocidade & Sync), 2. Sobriedade Operacional (Anti-Overengineering), 3. Função de Orquestrador SDD, 4. Contratos de Sprint, Commits e Sincronia de Journal, 5. Alteração de Código Fonte e Controle de Escrita, 6. Banco de Dados e Prevenção de Duplicidades (Monolith & Components), 7. Ingestão de Conhecimento e Karpathy Guard, 8. Perguntas sobre Código e Arquitetura (Graphify) (+2 more)

### Community 33 - "Community 33"
Cohesion: 0.33
Nodes (10): append_to_wiki_log(), build_index(), load_index_file(), normalize_text(), query_oracle(), Busca no oráculo de forma imparcial e robusta.     O parâmetro 'role' foi removi, Remove acentos, markdown e normaliza para lowercase., Reduz palavras a sua raiz com base em uma whitelist rigorosa. (+2 more)

### Community 34 - "Community 34"
Cohesion: 0.20
Nodes (9): 🤖 `.agent/` (Inteligência Autônoma), 🧠 `.context/brain/` (Estratégia e Cognição), 🔧 `.context/maintenance/` (Registros, RX e Evidências Físicas), 📈 `.context/market/` (Negócios e Compliance), 📊 `.context/monitoring/` (Tempo Real), 📚 FILE_GLOSSARY.md (Dicionário de Arquivos do Framework), 📅 `planos/` (Ideação e Estratégia), 🏛️ Raiz do Projeto (Comandos Globais) (+1 more)

### Community 35 - "Community 35"
Cohesion: 0.20
Nodes (9): 1) Visão Geral Rápida, 2) Mapa Estrutural da Raiz, 3) Detalhamento das Pastas Críticas, 4) Pontos de Atenção e Diagnóstico, 5) Hierarquia Funcional de Verdade, 🤖 `.agent/` (Subagentes e Autonomia), 🧠 `.context/` (Governança e Memória), 🔬 RX: Raio-X do Repositório `Antigravity-Template` (v2.5.2) (+1 more)

### Community 37 - "Community 37"
Cohesion: 0.29
Nodes (9): get_active_features(), inject_to_feature(), main(), parse_learnings_md(), rank_scars_by_relevance(), Retorna uma lista de diretórios de features que possuem spec.md., Lê o LEARNINGS.md e retorna lista de dicionários de scars., Rankeia scars baseadas em palavras-chave da spec. (+1 more)

### Community 38 - "Community 38"
Cohesion: 0.31
Nodes (9): calculate_score(), generate_learnings_md(), main(), Gera o arquivo LEARNINGS.md estruturado., Lê o Ledger focado no Formato B (Scars)., Analisa o HARNESS_LOG.md em busca de falhas recorrentes., Calcula a relevância da Scar com Decaimento e Frequência., safe_parse_harness_log() (+1 more)

### Community 39 - "Community 39"
Cohesion: 0.20
Nodes (9): 1. O Problema (Copiado da Spec), 2. O que Planejamos vs. O que Entregamos, 3. Modificações Realizadas, 4. Blast Radius Real, 5. Cicatrizes (→ LEARNINGS.md), 6. Backlog Gerado, 7. Governança, Closure Report: [feature_id] (+1 more)

### Community 40 - "Community 40"
Cohesion: 0.22
Nodes (8): 🛠️ EXECUTION GATE (Skill 6), 🚨 IN CASE OF FAILURE, 🕸️ MATRIZ DE ACOPLAMENTO (CUIDADO), Nota: Restricao de ferramentas e COGNITIVA via prompt para manter flexibilidade do Orquestrador., 🛑 [REGRA ANTI-LOOP] - HANDOFF OBRIGATÓRIO, 🔄 [RESUME] - PROTOCOLO DE RE-IGNIÇÃO, ⛓️ THE 9-SKILL CHAIN, 🛡️ THE SUPREME RULE (FAIL-CLOSED)

### Community 41 - "Community 41"
Cohesion: 0.22
Nodes (8): Checklist Final, Closure Thinker — O Protocolo de Síntese, Instruções de Execução, Protocolo de Refatoração (Para Closures mal feitos), Step 1: Mapeamento de Realidade (Audit), Step 2: Análise de Delta (Plano vs. Entrega), Step 3: Extração de Cicatrizes (The Scar Tissue), Step 4: Redação do CLOSURE.md

### Community 42 - "Community 42"
Cohesion: 0.22
Nodes (8): results, run_id, stats, dead_refs, ghosts, healthy, processed, timestamp

### Community 43 - "Community 43"
Cohesion: 0.33
Nodes (8): check_market_coverage(), get_inception_status(), main(), Verifica se entidades críticas possuem lastro REAL em compliance/ ou research/., Registra gaps detectados no MARKET_INBOX.md (uma linha por entidade)., Lê o status do Inception mestre., scan_entities(), update_inbox()

### Community 44 - "Community 44"
Cohesion: 0.22
Nodes (8): 1. Origem e Filosofia, 2. O Problema: Context Rot e Context Anxiety, 3. A Mecânica do Loop, 4. A Anatomia do Prompt Perfeito e o Backpressure, 5. O Funil de Execução: Nunca comece pelo Loop, 6. Casos Reais: Sucessos, Falhas e Ferramentas, Resenha Ultra-Completa: O Padrão "Ralph Wiggum Loop" na Engenharia de Agentes, Veredito

### Community 45 - "Community 45"
Cohesion: 0.22
Nodes (8): 1. A Ilusão das "9 Skills", 2. O Triângulo de Ferro (Por que a IA não escapa?), 3. O Detetor de Mentiras em Tempo Real (Harness Runner), 4. Conclusão: O Imposto sobre a Malandragem, A. O Executor (`@spec-driver`), B. O Gatekeeper Físico (`write_with_validation.py`), C. O Auditor (`@qa-validator`), Desvendando o Spec-Driver V3: A Engenharia da Paranoia

### Community 46 - "Community 46"
Cohesion: 0.22
Nodes (8): 🎯 1. Visão Geral, 📂 2. Estrutura em Camadas, 🔄 3. O Fluxo Chain-Skills (9 Skills), 🤖 4. Operando com o Anti-Loop, ⚙️ 5. Comandos Rápidos (v3.0.0), code:bash (# Validar integridade e conformidade SAM), 🧩 Pilares de Operação (v3.0.0+), 📖 README_CONTEXT.md — Guia de Operação Chain-Skills V3

### Community 47 - "Community 47"
Cohesion: 0.25
Nodes (7): 🛡️ Gates de Governança (O "Zero Trust"), 🧹 Metabolismo e Manutenção (Limpeza), 📡 Motores de Visão e Mapeamento, 🧠 Motores Epistemológicos (Oráculo e Conhecimento), 🚀 Orquestrador Universal (Raiz), ⚙️ SCRIPT_GLOSSARY.md (Motores de Automação do Framework), 🔧 Utilitários Compartilhados (Módulos Base)

### Community 48 - "Community 48"
Cohesion: 0.25
Nodes (7): 1. Declare sua Visão, 2. Solicite a Tradução Cognitiva, 3. Ratifique os Limites, 📈 Comandos Úteis, 🧭 O Ciclo de Vida da Descoberta, 🛠️ Passo a Passo para Inicializar, 🚀 START_HERE: Seu Guia de Onboarding

### Community 49 - "Community 49"
Cohesion: 0.36
Nodes (7): append_to_wiki_log(), check_wiki(), find_raw_sources(), Lista arquivos na inbox RAW para sugestão., Heurística simples: busca palavras-chave do claim nos nomes dos arquivos RAW., Varre a wiki em busca de claims sem citação., suggest_source()

### Community 50 - "Community 50"
Cohesion: 0.36
Nodes (7): audit(), get_git_state(), get_latest_journal_entry(), get_synapse_rules(), Retorna dicionário com arquivos modificados e novos., Extrai JSON do JOURNAL_SYNAPSE.md., Extrai a última entrada (seção ## 📅) do JOURNAL.md.

### Community 51 - "Community 51"
Cohesion: 0.25
Nodes (7): 🚀 1. Preparação do Ambiente (Obrigatório), 🛠️ 2. Correção de Dependências (O "Soro"), 🔑 3. O Fluxo de Login Definitivo, 🧠 4. Como o MCP funciona na prática?, code:powershell ($env:PYTHONUTF8=1), code:powershell (uv pip install --python C:\Users\User\AppData\Roaming\uv\too), 🛠️ Guia de Estabilização: NotebookLM + Antigravity

### Community 52 - "Community 52"
Cohesion: 0.25
Nodes (7): 0. Origem, 1. O Problema, 2. A Solução, 3. Requisitos Funcionais (Acceptance), 4. Critérios de Integridade V3 (Não Negociáveis), 5. Raw Payloads (Injeção Atômica), Feature: [Nome Amigável]

### Community 53 - "Community 53"
Cohesion: 0.25
Nodes (4): Valida se o decaimento temporal altera o score corretamente., Valida se falhas no harness aumentam o score., Valida se o injetor prioriza scars com palavras-chave da spec., TestMiMoMemory

### Community 54 - "Community 54"
Cohesion: 0.29
Nodes (6): 🎭 1. Roles (Personas) vs. Sub-Agents (Firmwares), A. Roles Lógicas (Personas), B. Sub-Agents (Firmwares de Execução), 📁 Estrutura do Diretório, 🤖 Inteligência Autônoma (.agent/), 🛡️ Regra de Ouro (Anti-Alucinação)

### Community 55 - "Community 55"
Cohesion: 0.29
Nodes (6): A Nossa Realidade: Engenharia para PMEs, A Tríade H.O.K.: O Governador Cibernético, Conclusão, Do Vibe Coding à Governança Cognitiva:  H.O.K Forge v2.5, O Canteiro de Obras Efêmero e o Ralph Wiggum Loop, O Horizonte: A Engenharia de Concepção

### Community 56 - "Community 56"
Cohesion: 0.29
Nodes (6): code:python (# Código de referência rápida), Exemplo Mínimo, Links Relacionados, Regras / Fluxo, Resumo, [Título Descritivo]

### Community 57 - "Community 57"
Cohesion: 0.29
Nodes (6): 1. Extração de Entidades (Parsing do FLOW), 2. Reality Check (O Cruzamento Físico), 3. Veredicto e Execução (Fail-Closed), Flow Auditor - Reality Check de Documentos H.O.K., Integração (Cadeia de Skills - Skills Chain), Protocolo de Auditoria Rigorosa

### Community 58 - "Community 58"
Cohesion: 0.29
Nodes (6): 1. Ingestão de Contexto Frio (Read Phase), 2. Mapeamento Reverso (Mental Sandbox), 3. Edição Física ou Invocação de Motor (A Cirurgia), 4. Handoff de Retorno (The Signoff), Cadeia de Execução Obrigatória (Propagation Chain), Propagation Auditor (O Arqueólogo H.O.K)

### Community 59 - "Community 59"
Cohesion: 0.29
Nodes (6): code:markdown (## 🚨 Critical Dependencies), Entrega Obrigatória (Output Format), Protocolo Determinístico Obrigatório, Regras Inegociáveis, Seu Objetivo, Spec Enricher (@spec-enricher)

### Community 60 - "Community 60"
Cohesion: 0.38
Nodes (3): check_deps(), detect_pkg_mgr(), error()

### Community 61 - "Community 61"
Cohesion: 0.33
Nodes (5): 🛡️ Checklist Estratégico (Preenchimento Obrigatório), 🧭 INCEPTION - Fronteiras Estratégicas (SSOT), 🛑 NUNCA (Boundaries), 🟢 SEMPRE (Restrições de Processo), 🎯 Visão Mestra

### Community 62 - "Community 62"
Cohesion: 0.33
Nodes (5): 📌 1. Visão Geral, 🚀 2. Requisitos Funcionais (Épicos), 🛡️ 3. Critical Dependencies & Limites, 📓 4. Lógica de Negócio Categórica (Regras), 📦 Product Requirements Document (PRD)

### Community 63 - "Community 63"
Cohesion: 0.33
Nodes (5): Architecture Fitness Harness (Harness de Arquitetura), 🏢 Exemplos Práticos na Indústria (Como as Big Techs fazem), ⚙️ Integração no Antigravity Kit (H.O.K. v2.5.2), Key Takeaways, Related

### Community 64 - "Community 64"
Cohesion: 0.33
Nodes (5): Behaviour Harness (Harness de Comportamento), 🏢 Exemplos Práticos na Indústria (Como as Big Techs fazem), ⚙️ Integração no Antigravity Kit (H.O.K. v2.5.2), Key Takeaways, Related

### Community 65 - "Community 65"
Cohesion: 0.33
Nodes (5): 🏢 Exemplos de Implementação (Padrões Globais), ⚙️ Integração no Antigravity Kit (H.O.K. v2.5.2), Key Takeaways, Maintainability Harness (Harness de Manutenibilidade), Related

### Community 66 - "Community 66"
Cohesion: 0.33
Nodes (5): Key Takeaways, ⚙️ Mecânica de Funcionamento (H.O.K. Integration), 🛑 O Funil de Execução, Ralph Wiggum Loop, Related

### Community 67 - "Community 67"
Cohesion: 0.33
Nodes (5): 🔄 Ciclo de Vida TLC na Arquitetura V3.5 (A Prática), 📖 Glossário de Referências (Pasta: `C:\Users\User\.gemini\skills\tlc-spec-driven`), 📏 Regras de Ouro (Zero Migué), skill mãe: tlc-spec-driven, 🔗 TLC_INTEGRATION.md: O Córtex de Execução

### Community 68 - "Community 68"
Cohesion: 0.53
Nodes (5): archive_spec(), cleanup(), get_specs(), is_protected(), Verifica se a spec está protegida (ex: sprint ativa em modo sprint_based).

### Community 69 - "Community 69"
Cohesion: 0.33
Nodes (5): 📍 Ghost Coupling, 📍 Healthy, 🕸️ Matriz de Drift (Lista de Adjacência), 📊 Relatório de Afinidade e Drift (Affinity Lite), 📈 Resumo Executivo

### Community 70 - "Community 70"
Cohesion: 0.33
Nodes (5): 1. Minimalismo Semântico e de Nomenclatura, 2. Estabilidade de Versão (Anti-Inflação), 3. Abordagem Cirúrgica e Simples, 4. Verificação de Sobriedade, Sobriedade Semântica, Operacional e de Versão

### Community 71 - "Community 71"
Cohesion: 0.53
Nodes (5): append_to_wiki_log(), main(), Reconstrói o _index.md de forma atômica para evitar corrupção de leitura., rebuild_index_atomic(), validate_article()

### Community 72 - "Community 72"
Cohesion: 0.33
Nodes (5): Cadeia de Restrições Obrigatórias:, Como Executar Sua Tarefa, O Que Você Faz, Saída Esperada no Fim da Atuação:, Vision Architect (@vision-architect)

### Community 73 - "Community 73"
Cohesion: 0.33
Nodes (5): 🤖 DIRETIVAS COMPORTAMENTAIS (Regras de Ouro), 🛑 DIRETIVAS PRIMÁRIAS (Leitura Obrigatória no Boot), 🧭 DIRETIVAS SECUNDÁRIAS (Leitura Sob Demanda), 🛡️ MANIFESTO DE GOVERNANÇA: H.O.K FORGE (LEIA-ME PRIMEIRO), ⚖️ O SAM ESTÁ OBSERVANDO

### Community 74 - "Community 74"
Cohesion: 0.40
Nodes (4): Como Usar?, Governance Friction Analyst (`gov-friction-analyst`), O que é?, Quando Usar?

### Community 75 - "Community 75"
Cohesion: 0.40
Nodes (4): DevDependencies, 🔧 Requisitos Mínimos (Motor), 🚫 Restrições de Infraestrutura (Guerrilha), Tabelas no Schema (schema.sql)

### Community 76 - "Community 76"
Cohesion: 0.60
Nodes (4): get_inception_status(), main(), Lê o status do Inception mestre., run_script()

### Community 77 - "Community 77"
Cohesion: 0.50
Nodes (3): Análise de Impacto, Goal, Plan

### Community 78 - "Community 78"
Cohesion: 0.50
Nodes (3): 🛡️ HARNESS_REGISTRY.md, ⚙️ Regras de Execução, 📋 Tabela de Harnesses Ativos

### Community 79 - "Community 79"
Cohesion: 0.50
Nodes (3): 📂 Estrutura de Pastas, 🧬 rx-anatomy.md (Raio-X de Anatomia), 🧪 .specs/ (Workbench de Execução Atômica)

### Community 80 - "Community 80"
Cohesion: 0.50
Nodes (3): 🏗️ Hierarquia da Verdade Local (SSOT), 🔮 Oracle Baseline (Memória Externa), 🗺️ SSOT_MAP: Roteador do Oráculo & Hierarquia da Verdade

### Community 81 - "Community 81"
Cohesion: 0.50
Nodes (3): 📊 Health Check do Contexto - Dashboard, 📅 Histórico de Saúde (Log de Purges), 🚨 Regras de Degradação & Ações

### Community 82 - "Community 82"
Cohesion: 0.50
Nodes (3): INDEX_BY_DOMAIN, INDEX_BY_PATH, Project Context Bundle

### Community 83 - "Community 83"
Cohesion: 0.50
Nodes (3): 1. Resumo Tático: A Filosofia dos Contratos de Sprint, 2. Excertos Brutos e Evidências da Literatura (Citação Obrigatória), 🧠 Pesquisa: Contratos de Sprint e Leniency Bias em Sessões de LLM

## Knowledge Gaps
- **637 isolated node(s):** `name`, `version`, `description`, `context:validate`, `context:sync` (+632 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **18 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What connects `name`, `version`, `description` to the rest of the system?**
  _722 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.011695906432748537 - nodes in this community are weakly interconnected._
- **Should `Community 1` be split into smaller, more focused modules?**
  _Cohesion score 0.05959183673469388 - nodes in this community are weakly interconnected._
- **Should `Community 2` be split into smaller, more focused modules?**
  _Cohesion score 0.05263157894736842 - nodes in this community are weakly interconnected._
- **Should `Community 3` be split into smaller, more focused modules?**
  _Cohesion score 0.06666666666666667 - nodes in this community are weakly interconnected._
- **Should `Community 4` be split into smaller, more focused modules?**
  _Cohesion score 0.09359605911330049 - nodes in this community are weakly interconnected._
- **Should `Community 5` be split into smaller, more focused modules?**
  _Cohesion score 0.09523809523809523 - nodes in this community are weakly interconnected._