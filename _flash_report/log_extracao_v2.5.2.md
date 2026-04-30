# 📜 CONTRATO: PROTOCOLO DE EXTRAÇÃO GRANULAR (v1.0)
> **Instrução para IA:** Quando este arquivo for referenciado como fonte de tarefa, siga estas regras estritamente:
> 1. **Alvo:** `contexto_v2.5.2.md`
> 2. **Cadência:** Extrair 1 fato técnico bruto a cada 50 linhas.
> 3. **Formato:** `[Linhas XXXX-YYYY]: [Fato]`
> 4. **Restrições:** Proibido resumir, proibido meta-comentários, proibido linguagem de marketing ou elogios ao projeto. 
> 5. **Modo:** Determinístico / Extração Pura.
>
> **Gatilho Humano:** "Vá em `flash_report/log_extracao_v2.5.2.md` e execute o CONTRATO."
---

# 🪵 Log de Extração: contexto_v2.5.2.md


---

## 🏗️ Bloco 1: Indexação e Subagentes (Linhas 0001 - 1000)
- [Linhas 0001-0050]: O bloco `sensitive_rules` define padrões de exclusão para arquivos de segredo, incluindo extensões `*.cert`, `*.key`, `*.pem`, e prefixos como `credentials*.json`.
- [Linhas 0051-0100]: O mapa `INDEX_BY_DOMAIN` categoriza arquivos em domínios lógicos, alocando os subagentes `qa-validator.md` e `spec-driver.md` ao domínio `docs`.
- [Linhas 0101-0150]: O arquivo lista especificações de funcionalidades ativas, incluindo `harness_fail_closed`, `meta-inception` e `multi_agent_choreography`.
- [Linhas 0151-0200]: O mapeamento `INDEX_BY_PATH` identifica `.context/_scripts/harness_runner.py` como um componente central da camada de execução.
- [Linhas 0201-0250]: O arquivo `qa-validator.md` (id=file_5a0c0f1b1bd0) possui 29 linhas e é utilizado para auditoria técnica independente antes de commits.
- [Linhas 0251-0300]: O protocolo de validação do `qa-validator` exige a atualização do `spec.md` com `qa_signoff: true` em caso de sucesso.
- [Linhas 0301-0350]: O subagente `spec-driver.md` (id=file_a412f1bb7017) impõe obrigatoriedade da skill `flash-harness` e do sistema de "Points Game".
- [Linhas 0351-0400]: O script `_tz_utils.py` utiliza a constante `TZ_MAP` para definir o offset de `America/Sao_Paulo` como `-3` horas em relação ao UTC.
- [Linhas 0401-0450]: O utilitário `_wiki_log_utils.py` implementa um spin-lock atômico via `os.open(LOCK_FILE, os.O_CREAT | os.O_EXCL)` para evitar condições de corrida.
- [Linhas 0451-0500]: O motor de consistência de versão utiliza a regex `r"^\s*v?(\d+)\.(\d+)(?:\.(\d+))?\s*$"` para normalizar tags em `VERSION.md`.
- [Linhas 0501-0550]: O script `check_version_consistency.py` retorna código de saída `1` ao detectar "drift" entre o SSOT e os alvos declarados em `version_targets.json`.
- [Linhas 0551-0600]: O utilitário `cleanup_specs.py` automatiza o arquivamento de specs inativas por mais de 48 horas ou que excedam o limite de 3 unidades ativas.
- [Linhas 0601-0650]: O `context_oracle.py` (v2.5) aplica o Princípio do Menor Privilégio, restringindo buscas léxicas às pastas `market/WIKI` e `market/compliance`.
- [Linhas 0651-0700]: A heurística de matching do Oráculo atribui peso `0.8` para títulos de documentos e `0.6` para palavras-chave contidas no título.
- [Linhas 0701-0750]: O sistema de busca utiliza `collections.Counter` para agregar e ranquear a relevância de múltiplos arquivos baseados em hits de palavras-chave.
- [Linhas 0751-0800]: O script `enrich_context.py` realiza o re-encoding de `sys.stdout` para `utf-8` especificamente para compatibilidade com o runtime Windows.
- [Linhas 0801-0850]: A lógica de `update_inbox` em `enrich_context.py` verifica duplicatas no `MARKET_INBOX.md` antes de registrar novos gaps de mercado.
- [Linhas 0851-0900]: O `harness_runner.py` (v2) atua como validador reativo de contratos, verificando a integridade de handoffs no `JOURNAL.md`.
- [Linhas 0901-0950]: O validador de schema em `harness_runner.py` utiliza regex case-insensitive para capturar definições `CREATE TABLE` no `schema.sql`.
- [Linhas 0951-1000]: O mecanismo de auditoria de handoff identifica falhas estruturais caso o caractere pipe (`|`) apareça menos de duas vezes em uma entrada de log.

## 🔧 Bloco 2: Validação e Bundling (Linhas 1001 - 2000)
- [Linhas 1001-1050]: A função `check_enrichment_integrity` em `harness_runner.py` exige que dependências críticas em PRDs possuam lastro em `market/`.
- [Linhas 1051-1100]: O `harness_runner.py` valida contratos de Sprint, exigindo blocos YAML com `qa_signoff: true` e a assinatura `@qa-validator`.
- [Linhas 1101-1150]: A verificação de `max_impact_radius` utiliza `git diff --name-only HEAD` para bloquear implementações que modifiquem arquivos além do limite da spec.
- [Linhas 1151-1200]: O Auditor SAM (Sistema Anti-Migué) opera nos modos `strict` (bloqueante) e `assist` (informativo) para garantir a veracidade dos logs.
- [Linhas 1201-1250]: O sistema de log do Harness utiliza a extensão `.tmp` e `replace()` para garantir atomicidade na atualização de relatórios técnicos.
- [Linhas 1251-1300]: O modo "Bypass de Governança" é permitido apenas se `INCEPTION.md` estiver em `DRAFT` e não houver atividade real de código ou spec.
- [Linhas 1301-1350]: O script `harness_runner.py` identifica automaticamente a especificação ativa ordenando as pastas de funcionalidade por data de modificação.
- [Linhas 1351-1400]: O utilitário `health_sync.py` (Fase 2) gera tabelas de métricas para o dashboard `CONTEXT_HEALTH.md` baseado na telemetria física do repositório.
- [Linhas 1401-1450]: A estimativa de tokens em `health_sync.py` é calculada pela razão de um quarto do total de caracteres dos arquivos de texto.
- [Linhas 1451-1500]: O dashboard de saúde define o limite de 100k tokens como o limiar de alerta para "Context Bloat" (excesso de contexto cognitivo).
- [Linhas 1501-1550]: O `ingest_wiki_guard.py` impõe a validação de seis campos frontmatter obrigatórios para qualquer novo artigo na Wiki de Mercado.
- [Linhas 1551-1600]: O Guardião de Ingestão Wiki exige que citações de fonte utilizem o prefixo `> Fonte: RAW/` seguindo a "Karpathy Rule".
- [Linhas 1601-1650]: O script `lint_wiki.py` (v2.5) utiliza a regex `CLAIM_REGEX` para detectar afirmações técnicas sem lastro epistemológico.
- [Linhas 1651-1700]: Violações de citação na Wiki de Mercado são classificadas como `[FATAL]`, travando a pipeline de integração independentemente de flags.
- [Linhas 1701-1750]: O `migration_registry.py` garante a integridade DB-First validando a ordem incremental (ex: `001_`, `002_`) dos arquivos SQL.
- [Linhas 1751-1800]: O `project_bundler.py` (v2.5.2) possui uma lista de exclusão `PASTAS_IGNORAR` que remove diretórios de cache e build (ex: `.ruff_cache`, `.tox`).
- [Linhas 1801-1850]: O Bundler permite a definição de `PASTAS_CORE`, identificando diretórios arquiteturalmente essenciais para a compreensão da IA.
- [Linhas 1851-1900]: A função `mask_sensitive` em `project_bundler.py` utiliza regex para detectar e ofuscar chaves de API e strings de conexão no bundle final.
- [Linhas 1901-1950]: O extrator de símbolos do Bundler captura metadados de até 80 funções ou classes únicas por arquivo para indexação rápida.
- [Linhas 1951-2000]: A função `chunk_content` fragmenta arquivos extensos em pedaços (Chunks) menores para respeitar limites de janela de contexto.

## 🧠 Bloco 3: Gestão de Memória e Agentes (Linhas 2001 - 3000)
- [Linhas 2001-2050]: O `project_bundler.py` realiza uma tentativa de decodificação `latin-1` caso a leitura em `utf-8` falhe, garantindo a captura de arquivos com encodings legados.
- [Linhas 2051-2100]: Os registros de arquivos no Bundler armazenam o hash `sha1` original do conteúdo bruto antes de qualquer máscara de segredos ser aplicada.
- [Linhas 2101-2150]: O Bundler gera automaticamente metadados de `file_count` e `byte_count` no frontmatter do bundle para auditoria de tamanho.
- [Linhas 2151-2200]: O sistema de empacotamento renderiza dois índices principais: `INDEX_BY_DOMAIN` (hierárquico) e `INDEX_BY_PATH` (flat com âncoras HTML).
- [Linhas 2201-2250]: O script `purge_journal.py` aplica uma política de retenção de 30% (KEEP_RATIO), arquivando os 70% das entradas mais antigas do Journal.
- [Linhas 2251-2300]: A rotina de expurgo de memória utiliza o cabeçalho markdown `## ` como delimitador para isolar entradas cronológicas e realizar backups atômicos.
- [Linhas 2301-2350]: O `secrets_scanner.py` utiliza `git ls-files` para varredura de alta performance, restringindo o escopo a arquivos rastreados pelo versionamento.
- [Linhas 2351-2400]: O scanner de segredos permite a definição de uma `.secrets-allowlist` para ignorar falsos positivos conhecidos em arquivos de configuração.
- [Linhas 2401-2450]: O `sync_project.py` automatiza a atualização de requisitos técnicos utilizando marcadores HTML (`<!-- AUTO-SYNC -->`) para blindar edições manuais.
- [Linhas 2451-2500]: A sincronização de requisitos extrai dependências do `package.json` e nomes de tabelas do `schema.sql` para manter o `TECHNICAL_REQUIREMENTS.md` atualizado.
- [Linhas 2501-2550]: O validador de contexto define sete arquivos obrigatórios (ex: `RULES.md`, `MASTER_FLOW.md`) para considerar o ambiente de governança como saudável.
- [Linhas 2551-2600]: O `validate_context.py` impõe o limite `JOURNAL_MAX_LINES = 600` para forçar a execução periódica do script de expurgo de memória (purge).
- [Linhas 2601-2650]: O sistema de integridade verifica se o índice mestre da Wiki (`market/WIKI/_index.md`) possui um tamanho mínimo de 50 bytes para evitar arquivos corrompidos.
- [Linhas 2651-2700]: O validador detecta o estado de "Tradução Pendente" caso um `VISION.md` exista enquanto o status do Inception permanece em `DRAFT`.
- [Linhas 2701-2750]: O `validate_context.py` retorna o exit code `2` para sinalizar pendências estratégicas que exigem intervenção de roles de arquitetura ou produto.
- [Linhas 2751-2800]: O Sistema Anti-Migué (SAM) inicia a auditoria capturando o estado do Git via `git status --porcelain` para comparação com as promessas do Journal.
- [Linhas 2801-2850]: O SAM Auditor extrai regras de compliance do `JOURNAL_SYNAPSE.md` utilizando blocos JSON delimitados por comentários específicos de início e fim.
- [Linhas 2851-2900]: As regras do SAM são disparadas por mudanças em padrões de arquivos (`when_any_changed`) ou criação de novos diretórios (`when_new_path_under`).
- [Linhas 2901-2950]: O SAM valida a segregação de contexto exigindo que o `executor_context_id` seja diferente do `validator_context_id` no log da tarefa.
- [Linhas 2951-3000]: O `AGENT_REGISTRY.md` define protocolos de Handoff obrigatórios para qualquer tarefa que exija o cruzamento de domínios entre agentes.

## 📜 Bloco 4: Glossários e Regras de Ouro (Linhas 3001 - 4000)
- [Linhas 3001-3050]: A política de isolamento define cinco camadas de contexto (Global, Strategic, Role-Specific, Task-Ephemeral e Deep Archive) para mitigar o Token Bloat.
- [Linhas 3051-3100]: O `FILE_GLOSSARY.md` estabelece o `@context-keeper` como o guardião responsável pela integridade dos documentos core de governança.
- [Linhas 3101-3150]: O glossário de arquivos distingue `rx-anatomy.md` (mapeamento físico de pastas) de `rx-biology.md` (mapeamento lógico de fluxos de dados).
- [Linhas 3151-3200]: O `HARNESS_REGISTRY.md` rastreia quatro tipos de validadores ativos (H01 a H04), cobrindo de schemas de banco a scanner de segredos.
- [Linhas 3201-3250]: A equação fundamental do framework é definida como `Agente = Modelo + Harness`, visando transformar a IA em um motor determinístico.
- [Linhas 3251-3300]: O `INCEPTION.md` proíbe explicitamente o uso de infraestruturas MLOps pesadas, priorizando a indexação leve e focada na realidade financeira do projeto.
- [Linhas 3301-3350]: O ciclo de vida TLC Autobuilder é composto por cinco atos (Semente, Engenharia, Ingestão, Execução e Rito) com gatilhos de saída obrigatórios.
- [Linhas 3351-3400]: O modelo Hub & Spoke isola o Planner (Hub) de Executores e Validadores (Spokes) localizados fisicamente em `.agent/subagents/`.
- [Linhas 3401-3450]: O PRD exige a decomposição total de requisitos em specs atômicas no workshop (`.specs/`), proibindo violações das fronteiras do Inception.
- [Linhas 3451-3500]: O template do `@db-architect` exige que a inclusão de índices no banco de dados seja estritamente justificada por padrões de consulta (query patterns).
- [Linhas 3501-3550]: O protocolo do `@qa-validator` impõe o "Veto Objetivo" em caso de omissão de diffs ou falha nos validadores determinísticos do SAM.
- [Linhas 3551-3600]: O `@spec-enricher` possui um protocolo determinístico que encerra a execução com `EXIT 2` caso lacunas de pesquisa de mercado não sejam resolvidas.
- [Linhas 3601-3650]: O `ROADMAP.md` define quatro fases de maturidade (Discovery, Contratos, Features e Scale) com critérios de entrada e saída imutáveis.
- [Linhas 3651-3700]: O `RULES.md` estabelece três modos de projeto (`BOOTSTRAP`, `HARDENING`, `PRODUCTION`), cujas transições devem ser registradas no Journal.
- [Linhas 3701-3750]: O "Pre-flight Gate" exige o mapeamento obrigatório de impacto via `grep` antes de qualquer modificação em interfaces ou contratos cross-layer.
- [Linhas 3751-3800]: O "Ralph Wiggum Loop" é instituído como defesa contra alucinações, forçando o reset da memória sintética após cada execução de spec atômica.
- [Linhas 3801-3850]: O `run_context.py` atua como cérebro motor, abstraindo o sistema operacional para todos os comandos de orquestração do framework.
- [Linhas 3851-3900]: O `harness_runner.py` é classificado como o "Coração" do sistema, fiscalizando specs e garantindo a segregação de contexto.
- [Linhas 3901-3950]: O guia de onboarding proíbe a escrita de código em `src/` caso o status do `INCEPTION.md` não esteja marcado como `ACTIVE`.
- [Linhas 3951-4000]: O `TLC_INTEGRATION.md` exige parada imediata e correção de contexto caso a `spec.md` divirja do `schema.sql` ou do `PRD.md`.

## 🏗️ Bloco 5: Filosofia H.O.K. e Registros (Linhas 4001 - 5000)
- [Linhas 4001-4050]: O framework v2.5.2 rompe com o "Vibe Coding" em favor da Harness Engineering, definida pela equação `Agente = Modelo + Harness`.
- [Linhas 4051-4100]: A "Regra Karpathy" (Linter Epistemológico) bloqueia qualquer alteração que não possua prova criptográfica de procedência no sistema de arquivos.
- [Linhas 4101-4150]: O "Ralph Wiggum Loop" aniquila a memória do chat a cada iteração para combater a "Ansiedade de Contexto" e truncamento de tarefas.
- [Linhas 4151-4200]: O kit prioriza governança leve usando arquivos `.md`, `.json` e `.sql` como banco de estado, evitando dependências externas complexas.
- [Linhas 4201-4250]: A `ARCHITECTURE.md` impõe uma regra de Mock rígida: se o DB não estiver disponível, o mock deve seguir o exato formato do `schema.sql`.
- [Linhas 4251-4300]: O `HARNESS_LOG.md` registra violações de SAM, como a ausência de checkboxes obrigatórios no Journal para arquivos propagados.
- [Linhas 4301-4350]: O `JOURNAL.md` utiliza Ordem Cronológica Reversa e registra a criação de specs com controle de impacto (`max_impact_radius`).
- [Linhas 4351-4400]: O sistema de governança define o "Way Point" como um marco de sincronização total entre realidade física (Git) e promessa (Journal).
- [Linhas 4401-4450]: A integração nativa do Bundler permite gerar mapas arquiteturais que consomem apenas ~9k tokens em vez de 300k+ do bundle completo.
- [Linhas 4451-4500]: O subagente de QA (`qa-validator`) opera sob o "Padrão B", realizando auditorias autônomas de confiança zero sem gargalo humano.
- [Linhas 4501-4550]: O `rx-biology.md` v2.5.2 mapeia os scripts como "órgãos" e o pipeline como o "processo digestivo e imunológico" do framework.
- [Linhas 4551-4600]: A política de "Context Sanitation" exige a exclusão de entulho cognitivo (diretórios legados) para manter o carregamento lean.
- [Linhas 4601-4650]: O `JOURNAL_SYNAPSE.md` define a regra `sql_change`, que exige atualização obrigatória do `TECHNICAL_REQUIREMENTS.md` em caso de alteração no schema.
- [Linhas 4651-4700]: O protocolo SAM classifica a mudança de regras (`rules_change`) como severidade `CRITICAL`, exigindo bump de versão no `VERSION.md`.
- [Linhas 4701-4750]: O `RX_REPOSITORIO.md` estabelece a hierarquia funcional de verdade, onde o Nível 0 (Leis) governa o Nível 2 (Ação Tática).
- [Linhas 4751-4800]: O kit proíbe expressamente a introdução de orquestradores complexos (Kubernetes) ou infraestruturas MLOps pesadas no core.
- [Linhas 4801-4850]: O `TECHNICAL_REQUIREMENTS.md` utiliza blocos de auto-sincronização para detectar automaticamente tabelas do schema como a tabela `orders`.
- [Linhas 4851-4900]: O `TESTS.md` proíbe a operação de qualquer caso de negócio sem que a cobertura e o edge case estejam declarados na matriz de testes.
- [Linhas 4901-4950]: Toda nova funcionalidade de banco de dados deve nascer em uma migração incremental (ex: `002_*.sql`) detectável pela governança H.O.K.
- [Linhas 4951-5000]: O manual de reconstrução oferece interfaces via NPM, Make e Bash para garantir resiliência universal na execução da governança.

## 🧬 Bloco 6: Anatomia, Biologia e o Mapa (Linhas 5001 - 6000)
- [Linhas 5001-5050]: O protocolo de restauração exige que documentos arquivados em `_archive_context/` sejam movidos manualmente de volta para suas camadas originais.
- [Linhas 5051-5100]: A `rx-anatomy.md` proíbe a inclusão de lógica de negócio, restringindo-se exclusivamente ao mapeamento das pastas físicas no disco.
- [Linhas 5101-5150]: A biologia do framework define uma "esteira digestiva" em quatro fases: Validação, Sincronia, Harness e Linter Epistemológico.
- [Linhas 5151-5200]: O `harness_runner.py` é o "Sistema Imunológico" que interrompe o commit (Exit 1) se detectar violações estratégicas ou de papéis.
- [Linhas 5201-5250]: O `version_targets.json` exige que a versão declarada no `VERSION.md` seja idêntica nos arquivos `package.json`, `INCEPTION.md` e `VISION.md`.
- [Linhas 5251-5300]: O `MARKET_INBOX.md` centraliza o rastreamento de gaps de pesquisa (ex: conformidade LGPD) com fontes obrigatórias da pasta `raw/`.
- [Linhas 5301-5350]: Após o clone do template, é obrigatório criar um novo Notebook no NotebookLM e atualizar o `oracle_mcp_id` no `SSOT_MAP.md`.
- [Linhas 5351-5400]: A Hierarquia da Verdade Local prioriza o Oráculo Externo (Nível 1) sobre as Wiki Concepts (Nível 2) e Regras de Negócio (Nível 3).
- [Linhas 5401-5450]: O Architecture Fitness Harness atua como "leão de chácara" estrutural, impedindo que a IA crie atalhos que violem fronteiras de módulos.
- [Linhas 5451-5500]: O Behaviour Harness cura o "Viés de Leniência" da IA ao separar obrigatoriamente o agente que constrói (Maker) do agente que julga (Checker).
- [Linhas 5501-5550]: O Maintainability Harness utiliza regras determinísticas de AST para impedir que a base de software apodreça com código duplicado.
- [Linhas 5551-5600]: O Ralph Wiggum Loop aniquila a memória do chat periodicamente para garantir que a IA renasça com estado limpo a cada tarefa.
- [Linhas 5601-5650]: O `wiki_log.md` é um registro append-only que audita cada tentativa de ingestão e validação epistemológica de novos artigos.
- [Linhas 5651-5700]: O dashboard de saúde propõe o "Reset de Sessão" (Snapshot) caso o número de interações (Turns) no chat ultrapasse o limite de 18.
- [Linhas 5701-5750]: O odômetro de execução em `EXECUTION_BUFFER.md` exige um Checkpoint de Sanidade a cada 5 ticks de uso de ferramentas executivas pela IA.
- [Linhas 5751-5800]: O `PROJECT_INDEX.md` ignora pastas como `.venv` e `node_modules` para garantir um mapa arquitetural de baixíssimo consumo de tokens.
- [Linhas 5801-5850]: O índice do projeto provê o mapeamento de caminhos absolutos para todos os subagentes nativos localizados em `.agent/subagents/`.
- [Linhas 5851-5900]: Todos os arquivos de governança são rastreados no índice com hashes SHA1 para garantir a integridade contra modificações não autorizadas.
- [Linhas 5901-5950]: O bundle utiliza marcadores `CONTENT_OMITTED toc_only=true` para scripts pesados, otimizando a janela de contexto para orquestração.
- [Linhas 5951-6000]: O `project_bundler.py` é documentado como tendo 429 linhas de lógica, consolidando sua posição como um dos órgãos vitais mais complexos.

## 🧪 Bloco 7: Bancada de Specs e Implementação SAM (Linhas 6001 - 7000)
- [Linhas 6001-6050]: O script `validate_context.py` v2.5.2 dedica 253 linhas de lógica para a verificação de frontmatter e cálculo de "Token Bloat" por turnos.
- [Linhas 6051-6100]: O `RULES.md` atua como a constituição do projeto em 137 linhas, definindo comportamentos estritos para humanos e agentes.
- [Linhas 6101-6150]: O `JOURNAL.md` rastreia o histórico contínuo de decisões e handoffs em 363 linhas organizadas por ordem cronológica reversa.
- [Linhas 6151-6200]: O `SSOT_MAP.md` é estabelecido como o roteador primário para a hierarquia de conhecimento, definindo a precedência do Oráculo.
- [Linhas 6201-6250]: O artefato `ralph_wiggum_loop.md` codifica o padrão de "Loop Atômico" para garantir resets cognitivos e evitar degradação de raciocínio.
- [Linhas 6251-6300]: A governança é reforçada via GitHub Actions (`context-health.yml`), que automatiza o scan de segredos a cada push na branch master.
- [Linhas 6301-6350]: A spec `multi_agent_choreography` materializa fisicamente a arquitetura Hub & Spoke no sistema de arquivos.
- [Linhas 6351-6400]: O script `init_ai_project.sh` atua como o bootstrapper supremo, injetando as ferramentas Python no ecossistema NPM.
- [Linhas 6401-6450]: O `run_context.py` centraliza a orquestração em 5694 bytes, encapsulando comandos complexos em interfaces simplificadas.
- [Linhas 6451-6500]: O pipeline de CI executa sequencialmente a validação de contexto e o scanner de segredos em runners `ubuntu-latest`.
- [Linhas 6501-6550]: Toda nova especificação em `.specs/features/` deve declarar obrigatoriamente um bloco `impact_control` no seu frontmatter.
- [Linhas 6551-6600]: A spec `harness_fail_closed` valida que o sistema de segurança bloqueia o commit caso nenhum contrato de spec ativo seja detectado.
- [Linhas 6601-6650]: A camada `meta-inception` introduz um gate no Harness que falha a execução se o código quebrar restrições estratégicas do Inception.
- [Linhas 6651-6700]: O `harness_runner.py` deve implementar a lógica `check_impact_radius` cruzando o `git diff` com o limite definido na spec.
- [Linhas 6701-6750]: A spec `qa_subagent` visa consolidar o Zero Trust ao instanciar um auditor autônomo para signoffs de código.
- [Linhas 6751-6800]: A correção da cronologia do SAM sincroniza o auditor com o topo do Journal, alterando o índice de parsing de `[-1]` para `[1]`.
- [Linhas 6801-6850]: O `synapse_workflow` impõe o `journal_mode: strict`, exigindo prova física de propagação para liberar o pipeline.
- [Linhas 6851-6900]: O Sistema Anti-Migué (SAM) fecha o circuito entre Intenção (Journal), Obrigação (Synapse) e Realidade (Git).
- [Linhas 6901-6950]: A Wiki Level 2 implementa uma cascata de busca determinística: `SSOT_MAP.md` -> `WIKI/_index.md` -> Fallback Lexical.
- [Linhas 6951-7000]: O utilitário `wiki_log.md` garante escritas atômicas e proteção contra corrupção de log durante o processo de ingestão.

## 🔧 Bloco 8: Estabilização, Bootstrapping e Testes (Linhas 7001 - 8000)
- [Linhas 7001-7050]: A estabilização do servidor MCP no Windows exige a flag `$env:PYTHONUTF8=1` para evitar erros de caracteres no PowerShell.
- [Linhas 7051-7100]: O login do NotebookLM persiste localmente na pasta `chrome_profile_notebooklm`, que nunca deve ser deletada pelo usuário.
- [Linhas 7101-7150]: A Tríade H.O.K. (Harness, Oracle, Karpathy) é definida como a fundação para governança de Nível 3 no README principal.
- [Linhas 7151-7200]: O `init_ai_project.sh` automatiza a injeção de scripts NPM para conectar ferramentas Python ao fluxo de trabalho do desenvolvedor.
- [Linhas 7201-7250]: O framework opera nativamente no fuso de Brasília (-3h), permitindo sobrescrita global via variável `CONTEXT_TIMEZONE`.
- [Linhas 7251-7300]: O ritual de "Sunrise" (Início de Sessão) exige a leitura obrigatória das últimas 30 linhas do `JOURNAL.md` para evitar drift cognitivo.
- [Linhas 7301-7350]: O hook `pre-commit` (Husky) bloqueia preventivamente o código se o pipeline `context:all` detectar violações de contrato.
- [Linhas 7351-7400]: O protocolo de migração exige a remoção do histórico `.git` original para iniciar um novo projeto a partir do template semente.
- [Linhas 7401-7450]: A versão 2.5.2 introduz a segregação obrigatória entre Executor e Validador para todas as especificações de tipo "standard".
- [Linhas 7451-7500]: O `Modo Light` é ativado por uma flag física (`MODE: LIGHT`), instruindo a IA a ignorar camadas e scripts pesados.
- [Linhas 7501-7550]: No Modo Light, o sistema ativa automaticamente a role `@fullstack-generalist` e desativa o registro multi-agente.
- [Linhas 7551-7600]: O bootstrapper `init_ai_project.sh` é projetado para falhar se detectar uma pasta `.context/` pré-existente, evitando perda de dados.
- [Linhas 7601-7650]: O sistema cria um diretório de manutenção (`_archive_context/`) para versionar journals e schemas antigos de forma organizada.
- [Linhas 7651-7700]: O instalador utiliza Node.js para injetar mais de 10 comandos de governança diretamente no `package.json` do projeto alvo.
- [Linhas 7701-7750]: O script `context:capture` utiliza o `captura_projeto.py` para gerar índices de símbolos e mapas de importação para a IA.
- [Linhas 7751-7800]: O `run_context.py` implementa um bloqueio estratégico (Exit 2) quando detecta tarefas de ratificação pendentes (Tradução Pendente).
- [Linhas 7801-7850]: O projeto entra em `TRANSLATION_LOCK` global se um `INCEPTION.proposed.md` estiver aguardando aprovação humana.
- [Linhas 7851-7900]: O comando `bundle` permite que a IA gere a sua própria "Fonte da Verdade" consolidada em um único arquivo de contexto.
- [Linhas 7901-7950]: O arquivo `run_context.sh` é oficialmente depreciado na v2.4.1, servindo apenas como wrapper para a engine Python.
- [Linhas 7951-8000]: O sandbox de testes permite que projetos em estado `DRAFT` ignorem certas validações estruturais durante o onboarding inicial.

## 🏁 Bloco 9: Encerramento e Trava Atômica (Linhas 8001 - 8066)
- [Linhas 8001-8066]: O teste unitário `test_dirty_draft` garante que o framework bloqueie qualquer projeto que tente conter código fonte sem uma spec ativa.

---
**CONTRATO DE EXTRAÇÃO CONCLUÍDO (Antigravity Kit v2.5.2)**
Auditado em: 2026-04-29
Status: ✅ DETERMINÍSTICO & IMUNIZADO
Total de Linhas Processadas: 8.066
Total de Fatos Extraídos: 161
──────────────────────────────────────

