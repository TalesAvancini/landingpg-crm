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

[Linhas 0001-0050]: Bundle gerado com schema_version 1 em 2026-04-30 contendo 91 arquivos e 362.035 bytes.
[Linhas 0051-0100]: O mapeamento INDEX_BY_DOMAIN categoriza o repositório em domínios técnicos (config, db, docs, source).
[Linhas 0101-0150]: A estrutura .specs/features/ armazena arquivos STATE.md e spec.md para controle de ciclo de vida de funcionalidades.
[Linhas 0151-0200]: O diretório .context/_scripts/ centraliza lógica de validação, limpeza, oráculo e sincronização de saúde do projeto.
[Linhas 0201-0250]: O subagent qa-validator (.agent/subagents/) é definido para auditoria técnica independente e autorização de commits.
[Linhas 0251-0300]: O QA Validator opera sob a filosofia Zero Trust, verificando Git Diff e Specs independentemente do agente executor.
[Linhas 0301-0350]: O spec-driver é obrigado a executar o Pre-flight Gate para validar o raio de impacto antes de qualquer escrita.
[Linhas 0351-0400]: O script _tz_utils.py implementa um TZ_MAP para suportar múltiplos offsets de fuso horário, com foco em Brasília (UTC-3).
[Linhas 0401-0450]: O utilitário _wiki_log_utils.py utiliza escape de pipes e spin locks para garantir escritas atômicas em tabelas Markdown.
[Linhas 0451-0500]: O sistema de consistência de versão normaliza padrões vX.Y ou vX.Y.Z para o formato SSOT X.Y.Z.
[Linhas 0501-0550]: O validador de versões encerra o processo com erro fatal se detectar drift entre o VERSION.md e os arquivos-alvo.
[Linhas 0551-0600]: O script cleanup_specs.py remove a spec mais antiga (baseado em mtime) quando o limite de 3 specs ativas é excedido.
[Linhas 0601-0650]: O context_oracle.py utiliza uma STEM_WHITELIST interna para processar termos técnicos sem dependências externas de NLP.
[Linhas 0651-0700]: O oráculo de contexto implementa um sistema de pesos onde tags explícitas no _index.md recebem peso massivo (10.0).
[Linhas 0701-0750]: A lógica de busca do oráculo utiliza Counter para agregar scores de hits determinísticos e léxicos por arquivo.
[Linhas 0751-0800]: O oráculo de contexto retorna 'baixa confiança' se o score do Top 1 for < 0.6, sugerindo refinamento da pesquisa.
[Linhas 0801-0850]: O script context_oracle.py registra cada consulta no wiki_log.md com o respectivo status (OK ou FAIL) e nível de confiança.
[Linhas 0851-0900]: O script enrich_context.py identifica entidades críticas (Stripe, AWS, LGPD, etc.) via regex no arquivo INCEPTION.md.
[Linhas 0901-0950]: Gaps de conformidade detectados pelo enrich_context.py são registrados automaticamente no MARKET_INBOX.md para pesquisa futura.
[Linhas 0951-1000]: O harness_runner.py valida a integridade de contratos técnicos entre specs e o arquivo de definição de banco de dados schema.sql.
[Linhas 1001-1050]: O validador de contratos de banco de dados ignora prefixos como IF NOT EXISTS ao extrair nomes de tabelas do schema.sql.
[Linhas 1051-1100]: O harness_runner valida handoffs modernos (🔄 Handoff:) exigindo pelo menos dois pipes para garantir dados completos de transferência.
[Linhas 1101-1150]: Violações estratégicas são detectadas se o PRD.md incluir termos explicitamente proibidos (seção NUNCA) no arquivo INCEPTION.md.
[Linhas 1151-1200]: A seção Critical Dependencies no PRD torna-se obrigatória e deve ter lastro em market/ se houver menção a integrações externas.
[Linhas 1201-1250]: Specs classificadas como 'standard' exigem segregação de contexto (IDs distintos para executor e validador) para serem autorizadas.
[Linhas 1251-1300]: No modo ASSIST, o SAM Auditor reporta violações no JOURNAL.md mas permite a continuidade do pipeline com aviso.
[Linhas 1301-1350]: O harness_runner.py atualiza arquivos STATE.md com timestamps e utiliza o Oráculo como gate epistemológico pré-execução.
[Linhas 1351-1400]: O Gate Epistemológico permite bypass automático caso a consulta ao Oráculo de Contexto exceda o timeout de 2 segundos.
[Linhas 1401-1450]: O pipeline de governança bloqueia execuções se detectar atividade de código real enquanto o INCEPTION.md estiver em DRAFT.
[Linhas 1451-1500]: O health_sync.py quantifica o volume do JOURNAL.md e rastreia o último status (FAIL/PASS) para o dashboard de saúde.
[Linhas 1501-1550]: A estimativa de tokens no health_sync.py é calculada dividindo o total de caracteres por 4 para as principais extensões de texto.
[Linhas 1551-1600]: O dashboard CONTEXT_HEALTH.md emite avisos de 'Context Bloat' quando a estimativa de tokens do repositório ultrapassa 100k.
[Linhas 1601-1650]: O script ingest_wiki_guard.py utiliza substituição atômica de arquivos e retry backoff para evitar corrupção do índice da Wiki.
[Linhas 1651-1700]: Para ser aceito na Wiki, um artigo deve possuir frontmatter YAML completo e uma seção de 'Key Takeaways'.
[Linhas 1701-1750]: O sistema Karpathy Layer impõe rastreabilidade mandatória, exigindo que claims técnicos apontem para fontes em market/RAW/.
[Linhas 1751-1800]: O linter da Wiki Karpathy bloqueia o pipeline caso artigos em market/WIKI não possuam citacão RAW obrigatória.
[Linhas 1801-1850]: Erros fatais são emitidos pelo linter se houver ausência de Frontmatter, Key Takeaways ou conectividade (links) na Wiki.
[Linhas 1851-1900]: O migration_registry.py impõe a convenção de nomenclatura 003d (001_*.sql) para garantir a ordem incremental de esquemas.
[Linhas 1901-1950]: O script oracle_analytics.py analisa a telemetria do wiki_log.md para identificar termos com baixa confiança de resposta.
[Linhas 1951-2000]: O project_bundler.py (v2.5.2) utiliza padrões universais de exclusão para filtrar diretórios de build, caches e ambientes virtuais.
[Linhas 2001-2050]: O bundler classifica semanticamente os arquivos (api, ui, lib, db, etc.) através de regras baseadas em regex no caminho do arquivo.
[Linhas 2051-2100]: A configuração do bundle é gerenciada via dataclasses, permitindo controle sobre o limite de linhas por arquivo e máscara de segredos.
[Linhas 2101-2150]: O project_bundler.py possui extratores de símbolos e importações para otimizar o entendimento da estrutura de dependências do código.
[Linhas 2151-2200]: O sistema de coleta de arquivos utiliza chunking determinístico para garantir que blocos de texto não sejam truncados de forma arbitrária.
[Linhas 2201-2250]: Um mecanismo de 'Isolamento Cirúrgico' é aplicado para ignorar pastas volumosas de conformidade (market/compliance) no bundle final.
[Linhas 2251-2300]: O project_bundler.py gera registros de arquivo (FileRecord) contendo hashes SHA1 e timestamps de modificação em formato ISO.
[Linhas 2301-2350]: O bundle markdown inclui índices automáticos INDEX_BY_DOMAIN e INDEX_BY_PATH com âncoras para navegação rápida entre arquivos.
[Linhas 2351-2400]: O sistema de geração utiliza delimitadores FILE_START e CHUNK_START para organizar o conteúdo de forma legível para modelos de IA.
[Linhas 2401-2450]: O script purge_journal.py executa a limpeza do JOURNAL.md, arquivando 70% das entradas e mantendo 30% como memória curta.
[Linhas 2451-2500]: O processo de purga do Journal utiliza substituição atômica de arquivos para garantir a integridade dos dados em caso de falha.
[Linhas 2501-2550]: O secrets_scanner.py utiliza 'git ls-files' para realizar uma varredura de segredos com performance otimizada O(N).
[Linhas 2551-2600]: O scanner de segredos suporta uma lista de exceções legítimas via arquivo .secrets-allowlist para evitar falsos positivos.
[Linhas 2601-2650]: O script sync_project.py utiliza comentários HTML de 'AUTO-SYNC' para preservar edições humanas em documentos técnicos.
[Linhas 2651-2700]: A sincronização do projeto consolida dependências de software e tabelas de banco de dados no TECHNICAL_REQUIREMENTS.md.
[Linhas 2701-2750]: O validador de contexto impõe a existência mandatória de arquivos como RULES.md, MASTER_FLOW.md e AGENT_REGISTRY.md.
[Linhas 2751-2800]: O validate_context.py verifica a presença de tabelas de papéis (roles) no arquivo AGENT_REGISTRY.md para governança.
[Linhas 2801-2850]: A infraestrutura da Wiki é validada pela presença mandatória do índice mestre (_index.md) e do log de transações.
[Linhas 2851-2900]: O validador detecta inconsistências se o projeto estiver em modo Onboarding (DRAFT) mas já possuir código ativo em src/ ou .specs/.
[Linhas 2901-2950]: O validate_context.py emite status PENDING (Exit 2) se houver um VISION.md aguardando tradução para o formato INCEPTION.md.
[Linhas 2951-3000]: O Auditor SAM utiliza o comando git status para obter a realidade física do repositório (arquivos novos e modificados).
[Linhas 3001-3050]: O auditor SAM extrai regras de conformidade em formato JSON a partir de marcadores no arquivo JOURNAL_SYNAPSE.md.
[Linhas 3051-3100]: O sistema SAM valida se tags obrigatórias e arquivos modificados foram devidamente reportados no Journal da sessão.
[Linhas 3101-3150]: A auditoria bloqueia o pipeline (Exit 1 em modo STRICT) se houver colisão entre os IDs de executor e validador no contrato.
[Linhas 3151-3200]: O AGENT_REGISTRY.md atua como o 'DNS cognitivo', proibindo a execução de qualquer agente ou role não registrado oficialmente.
[Linhas 3201-3250]: Cada role no AGENT_REGISTRY possui permissões de escrita explícitas e gatilhos de ativação para reduzir alucinações.
[Linhas 3251-3300]: O FILE_GLOSSARY.md define o README.md como a apresentação comercial externa e o README_CONTEXT.md como o manual de operação para IAs.
[Linhas 3301-3350]: O arquivo rx-anatomy.md mapeia a hierarquia física das pastas, enquanto o rx-biology.md mapeia o fluxo lógico de dados da aplicação.
[Linhas 3351-3400]: O HARNESS_REGISTRY.md cataloga validadores ativos (ex: H01 para Schema, H04 para Secrets) e define regras de fallback para falhas consecutivas.
[Linhas 3401-3450]: O INCEPTION.md estabelece limites inegociáveis (NUNCA), como a proibição de infraestruturas MLOps pesadas e a obrigatoriedade de citações Karpathy.
[Linhas 3451-3500]: O MASTER_FLOW.md exige que todos os arquivos em .context/ possuam metadados obrigatórios de criação, atualização e status no cabeçalho.
[Linhas 3501-3550]: O Ciclo de Vida TLC (4 Atos) proíbe a geração de código sem qa_signoff e exige IDs de contexto distintos para executor e validador.
[Linhas 3551-3600]: O MASTER_FLOW.md impõe o 'Radar Arquitetural', exigindo a inspeção do PROJECT_INDEX.md antes da criação de novos arquivos para evitar duplicidade.
[Linhas 3601-3650]: O PRD.md exige que todas as dependências críticas (externas ou de compliance) possuam lastro validado na camada market/.
[Linhas 3651-3700]: O prompt padrão para @frontend-specialist exige conformidade mínima WCAG 2.1 AA e proibição de dados hardcoded em componentes UI.
[Linhas 3701-3750]: O protocolo de auditoria SAM para @qa-validator exige a execução de 'git diff --name-only' para comprovar a realidade física das alterações.
[Linhas 3751-3800]: O @spec-enricher interrompe o processo (Exit 2) se identificar gaps de mercado não documentados em market/MARKET_INBOX.md.
[Linhas 3801-3850]: O prompt do @oracle-searcher instrui a IA a tratar informações com confiança (confidence) inferior a 0.6 apenas como sugestões.
[Linhas 3851-3900]: O ROADMAP.md define 4 fases (Discovery, Contratos, Features, Scale) e proíbe o salto de etapas sem cumprir os critérios de saída.
[Linhas 3901-3950]: O RULES.md define o status DRAFT no INCEPTION.md como um bloqueador global que permite apenas leitura e criação do VISION.md.
[Linhas 3951-4000]: O Ralph Wiggum Loop foca na execução absoluta e efêmera de specs atômicas, com aniquilação periódica da memória sintética da IA.
[Linhas 4001-4050]: Scripts de governança em Python devem forçar I/O em UTF-8 para garantir compatibilidade com consoles Windows.
[Linhas 4051-4100]: O script run_context.py encapsula chamadas CLI e abstrai o sistema operacional para os comandos do framework.
[Linhas 4101-4150]: Scripts de manutenção como purge_journal.py garantem a eficiência de tokens ao arquivar logs e limpar specs antigas.
[Linhas 4151-4200]: O framework bloqueia a escrita de código em src/ caso o Inception estratégico esteja em status DRAFT.
[Linhas 4201-4250]: O Ciclo de Vida Híbrido exige a transformação de intenções (PRD) em specs técnicas via sub-skill specify.md.
[Linhas 4251-4300]: A filosofia do kit define a equação Agente = Modelo + Harness para combater a dívida técnica gerada por IAs.
[Linhas 4301-4350]: O sistema adota a 'Divulgação Progressiva' para evitar o inchaço de contexto na janela de tokens do modelo.
[Linhas 4351-4400]: A arquitetura é estritamente DB-First, proibindo a construção de lógica sem a prévia validação do schema.sql.
[Linhas 4401-4450]: Caso o banco de dados esteja offline, o framework exige o uso de mocks fiéis ao formato declarado no schema.sql.
[Linhas 4451-4500]: O HARNESS_LOG.md registra falhas de conformidade que bloqueiam o pipeline de commit em modo STRICT.
[Linhas 4501-4550]: O JOURNAL.md mantém o histórico de longo prazo e aponta para arquivos mortos de entradas purgadas.
[Linhas 4551-4600]: O motor Oracle v3.0 utiliza Stemming pt-BR e suporte a siglas para aumentar a precisão das buscas de domínio.
[Linhas 4601-4650]: O waypoint de 'Consciência Sistêmica' marca o momento em que a IA concluiu a leitura física e auditada do contexto integral.
[Linhas 4651-4700]: O 'Circuit Breaker' de impacto (max_impact_radius) é usado para forçar a re-fragmentação de tarefas excessivamente complexas.
[Linhas 4701-4750]: O PROJECT_INDEX.md é regenerado autonomamente a cada commit para servir como radar arquitetural contra duplicidades.
[Linhas 4751-4800]: O FILE_GLOSSARY.md atua como o dicionário definitivo de responsabilidades, mapeando cada arquivo .md para seu respectivo agente guardião.
[Linhas 4801-4850]: O subagente @qa-validator assume o ID CTX_QA_VALIDATOR para realizar auditorias isoladas, eliminando o humano como gargalo mecânico.
[Linhas 4851-4900]: O script workflow_journal_auditor.py foi corrigido para suportar a Ordem Cronológica Reversa, focando na entrada do topo do JOURNAL.md.
[Linhas 4901-4950]: A implementação do Sistema Anti-Migué (SAM) bloqueia commits caso a propagação de mudanças não seja comprovada via Reality Check (Git Diff).
[Linhas 4951-5000]: O JOURNAL_SYNAPSE.md define regras de severidade (critical/warning) para mudanças em arquivos sensíveis como schema.sql e RULES.md.
[Linhas 5001-5050]: Mudanças no arquivo RULES.md exigem obrigatoriamente um bump de metadados no VERSION.md conforme a regra rules_change do Synapse.
[Linhas 5051-5100]: O RX_REPOSITORIO.md mapeia as 4 camadas de RX (Geral, Framework, Negócio, Produto) e define o estado Hardened com Zero Trust.
[Linhas 5101-5150]: A hierarquia de verdade do repositório coloca RULES.md, INCEPTION.md e AGENT_REGISTRY.md no Nível 0 (Leis Fundamentais).
[Linhas 5151-5200]: O framework proíbe expressamente o uso de Kubernetes (K8s) e Bancos Vetoriais no core para limitar a dívida técnica e custos.
[Linhas 5201-5250]: A seção AUTO-SYNC do TECHNICAL_REQUIREMENTS.md é populada automaticamente para refletir as dependências reais de desenvolvimento.
[Linhas 5251-5300]: O TESTS.md declara que nenhum caso de negócio pode operar sem cobertura declarada e validada pelo sistema de governança.
[Linhas 5301-5350]: A regra DB-First exige que todo novo campo de banco de dados nasça em uma nova migration numerada (ex: 002_*.sql).
[Linhas 5351-5400]: O manual de reconstrução oferece três opções de automação: NPM (recomendado para web), Make (Unix/CI) e Bash (universal).
[Linhas 5401-5450]: O rx-anatomy.md é um harness preventivo que proíbe a inserção de regras de negócio ou fluxos lógicos em sua estrutura.
[Linhas 5451-5500]: O rx-biology.md descreve o metabolismo funcional do framework através de um diagrama de fluxo que transforma intenções em código imunizado.
[Linhas 5501-5550]: O script harness_runner.py atua como o sistema imunológico, 'matando' processos que tentam burlar a segregação de papéis ou limites estratégicos.
[Linhas 5551-5600]: O snapshot real da tabela de pedidos (schema.sql) define campos críticos como stripe_session_id e total_amount para a lógica financeira.
[Linhas 5601-5650]: O version_targets.json estabelece que o VERSION.md é o SSOT, exigindo que package.json e INCEPTION.md mantenham paridade de versão.
[Linhas 5651-5700]: O SSOT_MAP.md instrui o humano a atualizar o oracle_mcp_id (NotebookLM) imediatamente após clonar o template do projeto.
[Linhas 5701-5750]: Na Hierarquia da Verdade, o Oráculo Externo (NotebookLM) possui precedência máxima, seguido pelas pílulas de conhecimento na Wiki local.
[Linhas 5751-5800]: O Architecture Fitness Harness protege as fronteiras modulares e direções de dependência, impedindo atalhos arquiteturais da IA.
[Linhas 5801-5850]: A integração do Architecture Harness no kit utiliza o script harness_runner.py como juiz definitivo contra o drift estratégico do DB.
[Linhas 5851-5900]: O Behaviour Harness combate o 'Viés de Leniência' através da separação obrigatória entre o agente que constrói e o agente que julga.
[Linhas 5901-5950]: O pipeline de segurança bloqueia o avanço se os IDs de contexto de executor e validador forem idênticos em especificações standard.
[Linhas 5951-6000]: O Maintainability Harness utiliza linters e formatadores como sensores computacionais determinísticos para bloquear códigos de baixa qualidade.
[Linhas 6001-6050]: O script lint_wiki.py garante que cada afirmação técnica na documentação possua uma fonte rastreável na pasta market/RAW/.
[Linhas 6051-6100]: O Ralph Wiggum Loop aniquila a memória de chat a cada tarefa para evitar o Context Rot e manter a sanidade cognitiva da IA.
[Linhas 6101-6150]: O Ralph Wiggum Loop é exclusivo para execução determinística, sendo proibido seu uso em fases de descoberta ou brainstorming.
[Linhas 6151-6200]: O wiki_log.md registra todas as transações de ingestão e linting da Wiki, permitindo a rastreabilidade da linhagem de conhecimento.
[Linhas 6201-6250]: O dashboard de saúde monitora o Token Bloat e a carga do Journal, disparando alertas se o limite de 50k caracteres for atingido.
[Linhas 6251-6300]: O PROJECT_INDEX.md organiza arquivos por domínio (config, db, docs, source), provendo IDs únicos para ancoragem de contexto.
[Linhas 6301-6350]: O mapeamento INDEX_BY_PATH permite que agentes localizem rapidamente metadados de arquivos críticos como validate_context.py e RULES.md.
[Linhas 6351-6400]: Os prompts dos subagentes (qa-validator, spec-driver) são omitidos do bundle TOC para economizar tokens em varreduras globais.
[Linhas 6401-6450]: O script _tz_utils.py centraliza a gestão de fusos horários, garantindo a consistência temporal dos logs em Brasília (-3h).
[Linhas 6451-6500]: O MASTER_FLOW.md v2.5.2 documenta o fluxo SAM de validação determinística entre o Diário e o Git Diff.
[Linhas 6501-6550]: O PROMPT_LIBRARY.md centraliza os artefatos cognitivos necessários para a execução fiel de papéis pelo Arquiteto e Executor.
[Linhas 6551-6600]: O HARNESS_LOG.md registra as evidências físicas de cada execução do Oráculo e do Bundler, servindo como trilha de auditoria.
[Linhas 6601-6650]: O rebuild_guide.md estabelece o protocolo de restauração do contexto a partir de snapshots arquivados por timestamp.
[Linhas 6651-6700]: A WIKI centraliza conceitos como Karpathy Protocol e Ralph Wiggum Loop para unificar a linguagem técnica entre humanos e IAs.
[Linhas 6701-6750]: O dashboard CONTEXT_HEALTH.md monitora a 'Carga do Journal' em caracteres para evitar a saturação da memória operativa.
[Linhas 6751-6800]: O workflow context-health.yml executa automaticamente o validate_context.py e o secrets_scanner.py a cada push/PR.
[Linhas 6801-6850]: A configuração legada do husky.sh em .husky/_/ foi depreciada em favor da integração nativa via scripts Python do framework.
[Linhas 6851-6900]: O template de specs exige o controle de impacto (max_impact_radius) para limitar o rastro de alteração em arquivos críticos.
[Linhas 6901-6950]: A feature 'harness_fail_closed' exige que o script runner trave o commit (Exit 1) se não localizar uma spec ativa assinada.
[Linhas 6951-7000]: O protocolo meta-inception exige que o agente execute a própria alteração que tranca o repositório sob uma spec atômica.
[Linhas 7001-7050]: A feature meta-inception exige a criação de templates-base para INCEPTION.md e SSOT_MAP.md, além do registro da role @vision-architect.
[Linhas 7051-7100]: A arquitetura Hub & Spoke exige que o script harness_runner.py implemente o check_impact_radius contra o limite max_impact_radius.
[Linhas 7101-7150]: O Oracle v3.0 calibra o cálculo de confidence para priorizar matches exatos e retorna o Top-N de resultados graduados.
[Linhas 7151-7200]: A implementação do subagente de QA utiliza o gatilho cognitivo 'Automatically delegate' para forçar a auditoria autônoma.
[Linhas 7201-7250]: O parser get_latest_journal_entry foi modificado para extrair o primeiro bloco válido (índice 1) após o cabeçalho do arquivo.
[Linhas 7251-7300]: O modo STRICT do pipeline SAM bloqueia commits se detectar contratos incompletos ou status de validação inválidos no Journal.
[Linhas 7301-7350]: O Sistema Anti-Migué exige que o JOURNAL_SYNAPSE.md utilize um bloco JSON nativo embutido entre tags de comentário HTML.
[Linhas 7351-7400]: A especificação da Wiki Nível 2 exige o roteamento determinístico: SSOT_MAP.md -> WIKI/_index.md -> Fallback Lexical.
[Linhas 7401-7450]: O cronograma da Wiki Nível 2 inclui a criação do utilitário _wiki_log_utils.py para escrita atômica e segura de logs.
[Linhas 7451-7500]: O guia de estabilização do NotebookLM exige o uso de undetected-chromedriver para evitar a detecção de robôs pelo Google.
[Linhas 7501-7550]: Em caso de falha de autenticação, o ritual exige mudar headless para false no config e logar manualmente na janela do navegador.
[Linhas 7551-7600]: O pilar Karpathy de governança v2.5.2 atua como um linter epistemológico que exige fontes para todo claim técnico.
[Linhas 7601-7650]: O script init_ai_project.sh aborta a execução se a pasta .context/ estruturada já existir no diretório de destino.
[Linhas 7651-7700]: O fuso horário global pode ser alterado via variável de ambiente CONTEXT_TIMEZONE ou no arquivo .env do projeto.
[Linhas 7701-7750]: O ritual de Sunrise exige que a IA execute npm run context:validate e leia as últimas 30 linhas do JOURNAL.md antes de agir.
[Linhas 7751-7800]: O comando npm run context:all orquestra o pipeline completo: validação, sincronização, limpeza, harness e lint em modo estrito.
[Linhas 7801-7850]: O onboarding de novos projetos exige a criação do VISION.md e a ratificação do INCEPTION.proposed.md gerado pela IA.
[Linhas 7851-7900]: O guia de migração instrui o usuário a realizar um reset do Git para romper o vínculo com o template e iniciar um novo histórico.
[Linhas 7901-7950]: A versão 2.5.2 do Antigravity Kit introduziu a segregação independente de QA e o radar arquitetural via PROJECT_INDEX.md.
[Linhas 7951-8000]: O Modo Light é recomendado para MVPs com duração inferior a 2 semanas e equipes reduzidas, priorizando velocidade sobre governança pesada.
[Linhas 8001-8050]: A ativação do Modo Light é feita através do arquivo MODE.md na raiz de .context/, instruindo a IA a ignorar camadas e scripts complexos.
[Linhas 8051-8100]: O script de bootstrap verifica a existência de Git e Python (3.x) como requisitos mínimos antes de inicializar a estrutura Antigravity.
[Linhas 8101-8150]: O bootstrapper cria automaticamente a estrutura de camadas (brain, maintenance, monitoring, _scripts) e o diretório efêmero .specs/.
[Linhas 8151-8200]: O script de inicialização utiliza Node.js para injetar dinamicamente os comandos context:* no package.json do projeto.
[Linhas 8201-8250]: O package.json v2.5.2 inclui scripts especializados como context:wiki-health, context:workflow-journal e context:bundle.
[Linhas 8251-8300]: O run_context.py trata o código de saída 2 como um 'Strategic Block', sinalizando pendências que travam o pipeline local.
[Linhas 8301-8350]: O projeto entra em TRANSLATION_LOCK caso o INCEPTION.md não esteja ratificado, bloqueando todos os comandos exceto 'enrich' e 'help'.
[Linhas 8351-8400]: A sequência do pipeline 'all' é: version -> validate -> secrets -> sync -> migrations -> harness -> ingest -> lint -> health -> map.
[Linhas 8401-8450]: O uso do run_context.sh foi depreciado na v2.4.1+, servindo apenas como redirecionador para a engine unificada em Python.
[Linhas 8451-8500]: A suíte de testes de governança utiliza diretórios temporários (tempfile) como sandboxes para validar os scripts sem afetar o repositório real.
[Linhas 8501-8550]: O validador de contexto retorna 0 para onboarding, 2 para tradução pendente/lock e 1 para violações estratégicas (código em DRAFT).
[Linhas 8551-8600]: Testes de purge do Journal garantem que entradas antigas sejam movidas para _archive_context/journals preservando a integridade do arquivo principal.
[Linhas 8601-8650]: A suíte de testes do Oráculo v3 utiliza Pathlib e diretórios temporários para garantir a independência de sistema operacional (Windows/Unix).
[Linhas 8651-8700]: O test_oracle.py valida a normalização de acentos e markdown em queries, garantindo que buscas por 'configuracao' encontrem 'Configuração'.
[Linhas 8701-8753]: A calibração de confiança do Oráculo garante que matches por tags no índice tenham precedência sobre matches por corpo de texto acumulado.
