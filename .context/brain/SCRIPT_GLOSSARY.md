---
Criado em: 2026-04-26
Ultima Atualizacao: 2026-05-30 21:45
Status: Ativo

---

# ⚙️ SCRIPT_GLOSSARY.md (Motores de Automação do Framework)

> **O Sistema Nervoso Central do H.O.K.**  
> Este documento mapeia todos os scripts executáveis da pasta `.context/_scripts/` e da raiz do projeto. Eles são os "órgãos vitais" que garantem que as regras escritas no `RULES.md` sejam cumpridas fisicamente, transformando governança passiva em **Governança Ativa e Determinística**.

---

## 🚀 Orquestrador Universal (Raiz)

| Script | O Órgão | Responsabilidade | Como Invocá-lo |
| :--- | :--- | :--- | :--- |
| `run_context.py` | **O Cérebro Motor** | O roteador de comandos CLI. Todos os comandos `npm run context:*` batem aqui. Ele encapsula chamadas para o `_scripts/` abstraindo o sistema operacional (funciona em Windows, Mac, Linux nativamente). | `npm run context:all` ou `python run_context.py [comando]` |

---

## 📡 Motores de Visão e Mapeamento
| Script | O Órgão | Responsabilidade | Como Invocá-lo |
| :--- | :--- | :--- | :--- |
| `project_bundler.py` | **Olho que Tudo Vê** | Um bundler de contexto. Na versão `map` (--toc-only), ele gera um índice de todos os arquivos do projeto para `PROJECT_INDEX.md`, servindo como mapa para IAs e subagentes não criarem código duplicado. Na versão `bundle`, empacota o repositório inteiro em um markdown gigantesco (`contexto.md`). | `npm run context:map` ou `npm run context:bundle` |

---

## 🛡️ Gates de Governança (O "Zero Trust")
*Scripts que fiscalizam IAs e Humanos, impedindo que lixo ou desvios entrem no código base.*

| Script | O Órgão | Responsabilidade | Como Invocá-lo |
| :--- | :--- | :--- | :--- |
| `harness_runner.py` | **Coração** | O Validador de Contratos. Verifica se as specs em `.specs/features/` possuem `definition_of_done`, valida o uso do banco de dados vs `schema.sql` e exige a assinatura formal de QA (Segregação de Contexto). | Roda via Husky no `pre-commit` ou `npm run context:harness` |
| `workflow_journal_auditor.py` | **SAM (Anti-Migué)** | Auditor H.O.K. Verifica se as decisões ou resoluções logadas no `JOURNAL.md` realmente correspondem à verdade física verificando o Git Diff. Se a IA mentir no Journal, o commit falha. | Roda no pipeline `context:all` |
| `validate_context.py` | **Sistema Imunológico** | **Radar de Fricção e Integridade.** Faz o check-up de metadados, estima Token Bloat e monitora a ordem cronológica do Journal e o frescor dos estados das specs (Modo Advisory). | `npm run context:validate` |
| `check_version_consistency.py` | **Medula Espinhal** | Analisa se a versão oficial declarada no `VERSION.md` está coerente no `package.json`, `INCEPTION.md` e em `version_targets.json`. Impede "Drifting" de versões. | Roda no pipeline `context:all` |
| `secrets_scanner.py` | **Leucócito** | Varre ativamente o código e arquivos markdown atrás de chaves de API, senhas ou tokens que o desenvolvedor/IA possa ter "hardcoded" por acidente. | Roda no pipeline `context:all` |
| `write_with_validation.py` | **Músculo Esquelético** | Validador Físico de Escrita (Skill 6). Impede que o agente modifique arquivos se não houver um Plano de Implementação (Tier Justification) ou se houver um bloqueio (exigindo `RESUME_DIRECTIVE`). | Chamado pela IA no terminal (`methodical-writer`) |
| `validate_commit_msg.py` | **Radar Semântico** | Validador de mensagens de commit (Conventional Commits). Garante que a história do projeto seja parseável e profissional. | Roda via Husky no `commit-msg` |
| `env_drift_gate.py` | **Leucócito de Ambiente** | Harness de Variáveis de Ambiente. Varre o código do projeto em busca de leituras de process.env.* e garante que estejam listadas no .env.example. | Roda integrado no `harness_runner.py` |
| `loop_exhaustion_harness.py` | **Anti-Loop Físico** | Harness de Exaustão de Loop. Monitora falhas consecutivas e bloqueia a execução subsequente de testes se a IA entrar em loop sem mudar código. | Invocado ao término de testes locais |
| `complexity_coverage_gate.py` | **Consultor Pedagógico** | Gate de Complexidade & Cobertura Semântica. Emite alertas didáticos sobre complexidade de código e ausência de testes mínimos. | Roda integrado no `harness_runner.py` (WARNING) |

---

## 🧠 Motores Epistemológicos (Oráculo e Conhecimento)
*Scripts responsáveis por transformar arquivos cru em conhecimento auditável e indexado para a IA.*

| Script | O Órgão | Responsabilidade | Como Invocá-lo |
| :--- | :--- | :--- | :--- |
| `affinity_lite.py` | **Detector de Drift** | Motor de análise de afinidade. Identifica Acoplamentos Fantasmas (temporal) e Referências Mortas (referencial) usando Jaccard e Word Boundary Scanning. | `npm run context:affinity` |
| `context_oracle.py` | **Memória RAG** | Implementa uma busca semântica leve usando `stdlib` (sem Chroma/VectorDBs de terceiros). Utilizado pelas IAs para resolver ambiguidades e varrer a Wiki em busca da verdade. | `npm run context:oracle "sua dúvida"` |
| `enrich_context.py` | **Córtex Pré-Frontal**| Analisa a narrativa livre do arquivo `VISION.md` e a traduz em limites técnicos estritos (`INCEPTION.md`). Detecta "gaps" de lógica antes do código ser escrito. | `npm run context:enrich` |
| `ingest_wiki_guard.py` | **Sistema Digestório**| Consome arquivos pesados de PDFs ou pesquisas da pasta `RAW/` e os destila (resume e formata) em pequenas pílulas indexadas na pasta `WIKI/`. | `npm run context:ingest-guard` |
| `lint_wiki.py` | **Linter Epistemológico**| A Regra Karpathy de código. Verifica se os documentos da Wiki contêm a citação de procedência (`> Fonte: raw/X`). Se for "achismo", o commit é bloqueado no modo Strict. | `npm run context:lint` |
| `oracle_analytics.py` | **Lobo Temporal** | Analisa a qualidade da base de dados e do histórico RAG do projeto, emitindo relatórios de eficácia analítica e apontando inconsistências de domínio. | `npm run context:oracle-analytics` |
| `learnings_aggregator.py` | **Memória Estratégica** | O "Lobo Temporal". Varre logs de erro e o Ledger tático para consolidar cicatrizes e recorrências no `LEARNINGS.md`. | `npm run context:learnings` |
| `inject_learnings.py` | **Córtex de Contexto** | Injeta as cicatrizes mais relevantes na spec de trabalho atual, gerando o `.enriched.md` para evitar reincidência de erros. | `npm run context:inject` |
| `blast_radius.py` | **Radar de Blast Radius** | Calculadora híbrida de impacto de propagação. Combina o grafo estrutural do Graphify (`graph.json`) com o mapa de governança (`rx-communications.md`) para retornar 3 buckets priorizados: `must_update` (ambas concordam), `likely_update` (só estrutural), `declared_only` (só governança). Consumido pelo skill `journal-sync` no Step 2. Degrada graciosamente quando Graphify não está disponível. | `npm run context:blast-radius -- --changed file1.py file2.md` |

---

## 🧹 Metabolismo e Manutenção (Limpeza)
*Scripts de manutenção higiênica, responsáveis por limpar lixo e manter o repositório leve (Token Efficiency).*

| Script | O Órgão | Responsabilidade | Como Invocá-lo |
| :--- | :--- | :--- | :--- |
| `purge_journal.py` | **Sistema Excretor** | Monitora o tamanho do `JOURNAL.md`. Quando ele atinge mais de ~600 linhas, ele "corta" os 70% mais velhos, condensa em um resumo semente e move o histórico para o arquivo morto (`_archive_context`). | `npm run context:purge` |
| `cleanup_specs.py` | **Linfócito Macrófago**| Fiscaliza a pasta `.specs/features/`. Specs com status `DONE` ou que não foram tocadas há >48h são arquivadas para evitar confusão. | `npm run context:cleanup` |
| `health_sync.py` | **Monitor de Batimentos**| Coleta dados de dezenas de métricas do repositório e compila tudo visualmente no arquivo `monitoring/CONTEXT_HEALTH.md`. | Executado periodicamente |
| `sync_project.py` | **Endócrino** | Sincroniza o ecossistema. Atualiza a matriz técnica com novas libs do `package.json` e reflete mudanças do banco de dados na governança. | `npm run context:sync` |
| `migration_registry.py` | **Cartório** | Varre a pasta de migrations SQL e gera um registro legível sobre qual a versão real do banco de dados em um formato "IA-Friendly". | Interno / Via Sync |

---

## 🔧 Utilitários Compartilhados (Módulos Base)
*Scripts auxiliares (não executáveis diretamente por linha de comando) usados para importar código repetitivo para os motores maiores.*

| Script | O Órgão | Responsabilidade | Como Invocá-lo |
| :--- | :--- | :--- | :--- |
| `_tz_utils.py` | **Relógio Biológico** | Padroniza estritamente os metadados de data/hora (Fuso Horário -3h Brasília) em toda a automação. | *Via `import _tz_utils`* |
| `_wiki_log_utils.py` | **Cartilagem** | Helper interno para centralizar as rotinas de escrita na Wiki e registro unificado no `wiki_log.md`. | *Via `import _wiki_log_utils`* |

---

> 💡 **Nota aos Agentes e Usuários:** Nunca altere a lógica de retorno de um script do `.context/_scripts/` para contornar um erro do Husky (ex: "comentar a linha de Exit 1"). Eles foram criados intencionalmente para "falhar fechado" (Fail-Closed). Se a governança quebrar, a execução deve quebrar.
 
