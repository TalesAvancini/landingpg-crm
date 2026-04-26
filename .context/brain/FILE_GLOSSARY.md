---
Criado em: 2026-04-26
Ultima Atualizacao: 2026-04-26
Status: Ativo
---

# 📚 FILE_GLOSSARY.md (Dicionário de Arquivos do Framework)

> **Fonte Única da Verdade para Responsabilidades de Arquivo.**  
> Este dicionário mapeia todos os documentos `.md` do ecossistema Antigravity/H.O.K. Se você não sabe o que um arquivo faz, quem deve editá-lo ou quando usá-lo, consulte este mapa.

---

## 🏛️ Raiz do Projeto (Comandos Globais)

| Arquivo | Responsabilidade Principal | Agente Guardião |
| :--- | :--- | :--- |
| `README.md` | Apresentação comercial/técnica do repositório para o mundo externo. | `@fullstack-generalist` |
| `README_CONTEXT.md` | O manual de operação do framework. Ensina IAs e humanos a interagirem com a pasta `.context`. | `@context-keeper` |
| `VERSION.md` | A versão semântica atual da aplicação e do framework. | Script de CI |
| `TEMPLATE_MIGRATION.md` | Molde para a geração padronizada de arquivos `.sql` de migração de banco de dados. | `@db-architect` |
| `GUIA_ESTABILIZACAO_NOTEBOOKLM.md` | Dicas e troubleshooting para manter o MCP do Google NotebookLM estável no VS Code. | Humano |

---

## 🧠 `.context/brain/` (Estratégia e Cognição)
*A "Constituição" do projeto. Dita as leis da física para qualquer IA orquestradora.*

| Arquivo | Responsabilidade Principal | Agente Guardião |
| :--- | :--- | :--- |
| `VISION.md` | **O "O Quê" e o "Porquê".** Escrito pelo humano. É o problema de negócio que queremos resolver na forma mais pura e abstrata. | Humano / `@vision-architect` |
| `INCEPTION.md` | **As Fronteiras.** Tradução técnica da Visão. Define claramente o que está dentro do escopo e o que **NUNCA** será feito. | `@spec-enricher` |
| `PRD.md` | **Requisitos de Produto.** O documento tático. Transforma o Inception em critérios de aceite, fluxos de usuário e regras de negócio testáveis. | `@spec-enricher` |
| `ROADMAP.md` | **Visão de Longo Prazo.** Mostra as macro-fases de entrega. O horizonte futuro. | `@vision-architect` |
| `RULES.md` | **A Constituição Inviolável.** Regras absolutas de conduta, segurança e arquitetura (ex: "Nunca chame o banco sem ORM", "Sempre verifique o Handoff"). | `@context-keeper` |
| `MASTER_FLOW.md` | **O Processo.** Descreve como as tarefas nascem, são executadas, sofrem QA e são fundidas. O fluxo de trabalho (Workflows). | `@context-keeper` |
| `AGENT_REGISTRY.md` | **O Catálogo de IAs.** Registra todas as *personas* (ex: `@qa-validator`), listando quais arquivos elas têm permissão de editar. | `@context-keeper` |
| `PROMPT_LIBRARY.md` | **O Vocabulário.** Coleção de prompts padronizados para acionar os agentes de forma previsível e sem alucinações. | Humano |
| `START_HERE.md` | **Onboarding.** Guia passo a passo para novos desenvolvedores entenderem o pipeline de descoberta (Visão -> Inception -> Execução). | Humano |
| `FILE_GLOSSARY.md` | **O Dicionário (Este arquivo).** Mapeia a responsabilidade estrita de cada `.md` dentro do ecossistema. | `@context-keeper` |
| `SCRIPT_GLOSSARY.md` | **O Dicionário de Automação.** Mapeia a função, responsabilidade e modo de invocação de todos os scripts Python da pasta `_scripts/`. | `@context-keeper` |

---

## 🔧 `.context/maintenance/` (Registros, RX e Evidências Físicas)
*A memória e os inventários do sistema.*

| Arquivo | Responsabilidade Principal | Agente Guardião |
| :--- | :--- | :--- |
| `JOURNAL.md` | **O Diário de Bordo (Memória Contínua).** Histórico de longo prazo em *Ordem Cronológica Reversa*. Registra handoffs, decisões técnicas e bugs. Quando atinge o limite de tokens, partes antigas vão para o arquivo morto (`_archive_context`), mas a linha do tempo nunca se perde. | Todos os Agentes |
| `HARNESS_LOG.md` | **A Caixa Preta.** Arquivo gerado por máquina contendo o pass/fail do pipeline de governança (`harness_runner.py`). | Scripts do Sistema |
| `TECHNICAL_REQUIREMENTS.md` | **Inventário Restrito.** Lista rígida das linguagens, frameworks, versões e ferramentas de CI obrigatórias. Proíbe invenção de modas. | `@devops-guardian` |
| `ARCHITECTURE.md` | **Padrões de Software.** Descreve os padrões (MVC, DDD, Clean Arch, etc) que o projeto segue. | `@backend-engineer` |
| `TESTS.md` | **Regras de Qualidade.** Como os testes unitários e de integração devem ser escritos. | `@qa-validator` |
| `rx-anatomy.md` | **Raio-X Físico.** Mapeia a hierarquia física das pastas do projeto (onde as coisas moram no disco). | `@context-keeper` |
| `rx-biology.md` | **Raio-X Lógico.** Mapeia como os dados fluem pela aplicação (sistemas conectando-se a outros sistemas). | `@backend-engineer` |
| `RX_REPOSITORIO.md` | **Raio-X de Governança.** Mapeia o ecossistema Antigravity, explicando os motores lógicos (SAM, Harness, Zero Trust). | `@context-keeper` |
| `JOURNAL_SYNAPSE.md` | **Regras de Expurgos.** Configurações de quando e como o Journal deve arquivar dados antigos para economizar tokens. | `@context-keeper` |
| `rebuild_guide.md` | **Recuperação de Desastres.** Instruções passo a passo para um desenvolvedor recriar a máquina do zero e rodar a aplicação. | `@devops-guardian` |

---

## 📊 `.context/monitoring/` (Tempo Real)

| Arquivo | Responsabilidade Principal | Agente Guardião |
| :--- | :--- | :--- |
| `CONTEXT_HEALTH.md` | **Dashboard Visual.** Gerado dinamicamente para exibir o nível de "Token Bloat" (peso do contexto), status de erros e saúde. | Scripts do Sistema |
| `EXECUTION_BUFFER.md` | **Fila de Tarefas (HOK).** Buffer que força IAs aceleradas a pausarem e sincronizarem contexto periodicamente. | HOK Governor |

---

## 📈 `.context/market/` (Negócios e Compliance)

| Arquivo | Responsabilidade Principal | Agente Guardião |
| :--- | :--- | :--- |
| `SSOT_MAP.md` | **Single Source of Truth de Mercado.** Mapeia os links oficiais dos concorrentes, leis e referências absolutas. | `@spec-enricher` |
| `MARKET_INBOX.md` | **Caixa de Entrada.** Área crua para depositar links soltos, artigos de blog e pesquisas antes de estruturar. | Humano |
| `wiki_log.md` | **Histórico de Wiki.** Log das publicações na documentação externa / Confluence. | Scripts do Sistema |

---

## 🧪 `.specs/` (O Workshop Tático)
*A bancada onde o código nasce.*

| Arquivo | Responsabilidade Principal | Agente Guardião |
| :--- | :--- | :--- |
| `features/<nome>/spec.md` | **Contrato de Código.** Define os `definition_of_done` da tarefa atômica. Contém as assinaturas do executor e do QA Validator (Zero Trust). | `@spec-driver` / `@qa-validator` |
| `features/<nome>/STATE.md` | **Gatekeeper de Estado.** Define se a spec está `WIP`, `WAITING_SIGNOFF` ou `DONE`. Lido diretamente pelo Pipeline SAM. | `@qa-validator` |
| `_template.md` | **Molde de Contrato.** O template que deve ser clonado para iniciar qualquer nova funcionalidade. | `@spec-driver` |

---

## 🤖 `.agent/` (Inteligência Autônoma)

| Arquivo | Responsabilidade Principal | Agente Guardião |
| :--- | :--- | :--- |
| `subagents/qa-validator.md` | **Padrão B de Subagente.** Validador Físico. Subagente que é invocado de forma autônoma (Zero Trust) para ler Diffs, Specs e autorizar o commit. | IA Orquestradora |
