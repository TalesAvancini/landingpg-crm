---
Criado em: 2026-04-10 23:28
Ultima Atualizacao: 2026-05-04 22:50
Status: Ativo
---

# 🏛️ MASTER_FLOW: Estrutura de Contexto em Camadas

Este documento é a diretriz mestre para a condução de projetos "AI-Ready". Ele define uma arquitetura de memória persistente em camadas para garantir foco, rastreabilidade e performance.

---

## 🕒 1. Metadados Obrigatórios
Todo arquivo dentro de `.context/` (exceto scripts) de conter este cabeçalho:
```markdown
---
Criado em: YYYY-MM-DD HH:MM
Ultima Atualizacao: YYYY-MM-DD HH:MM
Status: [Ativo | Arquivado | Depreciado]
---
```

---

## 📂 2. Estrutura de Governança (Context & Specs)

```text
/ (Root do Projeto)
├── .specs/                 # 🆕 WORKBENCH EFÊMERO (The Workshop - TLC)
│   └── features/           # Specs e tasks atômicas em execução
│
└── .context/               # 🏛️ GOVERNO E MEMÓRIA DE LONGO PRAZO
    ├── 🧠 brain/
    │   ├── ...
    │   ├── INCEPTION.md               # Fronteiras estratégicas (SSOT) [DRAFT|ACTIVE]
    │   ├── INCEPTION.proposed.md      # Proposta gerada pela IA (Aguardando Ratificação)
    │   └── VISION.md                  # Entrada narrativa humana (Input de Visão)
    │
    ├── 🌐 market/                      # CAMADA ESTRATÉGICA (Restrições Externas)
    │   ├── RAW/                       # Minério Bruto (Humano deposita)
    │   ├── WIKI/                      # Conhecimento Destilado (Atômico)
    │   ├── SSOT_MAP.md
    │   ├── wiki_log.md                # Log de Transação (Ingest/Lint)
    │   ├── MARKET_INBOX.md
    │   ├── economics.md
    │   ├── compliance/
    │   └── research/
    │
    ├── 🛠️ maintenance/                 # CAMADA DE MANUTENÇÃO (The Housekeeper)
    │   ├── JOURNAL.md                 # Log vivo (Máx ~50k char - Memória Contínua)
    │   ├── HARNESS_LOG.md             # Telemetria técnica automática do Harness (PASS/FAIL)
    │   ├── JOURNAL_SYNAPSE.md         # Matriz de Gatilhos Anti-Migué (SAM)
    │   ├── TECHNICAL_REQUIREMENTS.md  # Stack, libs e infra (Inventário)
    │   ├── rebuild_guide.md           # Guia de setup e infra (Pós-Mortem Vivo)
    │   ├── schema.sql                 # Snapshot do Banco de Dados (Verdade Real)
    │   ├── ARCHITECTURE.md            # Blueprint técnico evolutivo (O DNA)
    │   ├── TESTS.md                   # Ledger de padrões e TDDs
    │   ├── rx-anatomy.md              # Raio-X de pastas (Anatomia do Repositório)
    │   ├── rx-biology.md              # Raio-X de fluxos (Biologia do Negócio)
    │   ├── rx-communications.md       # Log de transparência narrativa (Transversal)
    │   └── _archive_context/          # Histórico imutável (A Biblioteca)
    │
    ├── monitoring/             # CAMADA DE MONITORAMENTO (The Guardian)
    │   ├── CONTEXT_HEALTH.md   # Dashboard de saúde técnica e cognitiva
    │   └── PROJECT_INDEX.md    # Mapa do repositório atualizado a cada commit (Radar)
    │
    └── _scripts/               # CAMADA DE AUTOMACAO (The Motor)
        ├── project_bundler.py         # Motor gerador do PROJECT_INDEX
        ├── validate_context.py        # Validador de integridade e status
        ├── enrich_context.py          # Tradutor cognitivo e Gap Check
        ├── purge_journal.py           # Gerenciador de memória (Purge)
        ├── cleanup_specs.py           # Gerenciador de efemeridade (.specs)
        ├── sync_project.py            # Sincronizador de requisitos
        └── workflow_journal_auditor.py # Auditor do Sistema Anti-Migué (SAM)

> ⚠️ **Script Sanity:** Qualquer alteração nos scripts da camada `_scripts/` exige execução de sanidade imediata e registro de não-regressão conforme Regra 1.8.

---

## 🔄 2.1 Ciclo de Vida TLC Autobuilder (5 Atos)
| Ato | Gatilho | Ferramenta/Script | Saída Esperada |
|-----|---------|-------------------|----------------|
| **1. [Semente]** | `INCEPTION.md` ativo + gaps | `npm run context:enrich` | `PRD.md` lastreado + `market/` populado |
| **2. [Engenharia]** | Criação de `.specs/features/X/` | `qa_signoff: true` no frontmatter | Contrato assinado; se `type: standard`, validador em contexto distinto |
| **3. [Ingestão]** | `RAW/` novo ou `WIKI/` modificado | `npm run context:ingest-guard` | Artigo validado + `wiki_log.md` |
| **4. [Vacinação]** | Início da Atuação do Agente | `npm run context:inject` | `*.enriched.md` gerado com Scars |
| **5. [Execução]** | `npm run context:harness` + SAM | `harness_runner.py` + `SAM Auditor` | Código validado + `STATE.md: ✅ PASSED` (Suporta **v2-Safe**) |
| **6. [Rito]** | Merge ou >48h inativo | `npm run context:cleanup` | Spec arquivada (Respeita Imunidade Sprint) |

> 🤖 [SYSTEM HOOK] IA: Este fluxo é imutável. Não pule o Ato 2. Não gere código sem `qa_signoff`. Em `type: standard`, `executor_context_id` e `validator_context_id` devem ser diferentes. Em features complexas, use o **Protocolo v2-Safe** (Contract Sprints).

---

---

## 🔄 2.2 Coreografia Hub & Spoke (A Dança)
Para projetos de complexidade média/alta, o Antigravity utiliza a segregação de agentes em processos isolados para atingir **Zero Trust**.

> **Mecanismo de Spawn (Isolamento Físico):**
> Os Spokes (Executores e Validadores) não são apenas personas da IA Principal. Eles residem fisicamente em `.agent/subagents/` (ex: `spec-driver.md`, `qa-validator.md`). Para invocá-los sem poluição de contexto, o Hub deve finalizar a execução usando a sintaxe de delegação explícita do Host: `/[nome-do-subagente] [instrução]`.

1.  **[Planner - Hub]**: IA Principal desenha a SPEC na janela atual, define `max_impact_radius` e emite o comando de Spawn (`/spec-driver`).
2.  **[Pre-flight - Executor]**: Novo processo limpo nasce e roda `grep` (Pre-flight Gate). Se impacto > Limite → `SCOPE_BLOWOUT` (Telemetria no `STATE.md`).
3.  **[Execution - Executor]**: O subagente (`spec-driver`) assume o controle operando sob a doutrina **Chain-Skills V3** (Uma corrente determinística de 9 skills).
    - **A Vacina Cognitiva:** A primeira ação do agente é injetar a memória rodando `npm run context:inject` e carregar o `*.enriched.md`.
    - As edições físicas (Skill 6) são monitoradas de forma Fail-Closed pelo `write_with_validation.py`.
    - Ao terminar as modificações, ele deve obrigatoriamente rodar o **Pre-close Self-Audit** (Skill 8). Se passar, emite `/qa-validator`.
4.  **[Auditoria - Validador]**: Novo processo cego nasce. Realiza a auditoria final de fechamento (Pre-Close Audit). Valida Semântica (Lógica) + Telemetria (Impacto resolvido). Assina o `spec.md` se correto.
5.  **[Finalização - Hub]**: IA Principal (Humano aciona o Hub) verifica a SPEC assinada, valida o SAM, emite o rito final e comita/arquiva.

---

## 🛡️ 2.3 Rito de Pre-Close Audit (Anti-Drift)
Protocolo obrigatório para transição de `IN_PROGRESS` para `PASSED` ou `COMPLETED`.

1. **Validação de Harness:** Executar checks automáticos (`npm run context:validate`).
2. **Coerência de Artefatos:** Cruzar `spec.md` (objetivo) vs `tasks.md` (check) vs `STATE.md` (estado real).
3. **Check de Higiene:** `git status --short` **DEVE** ser vazio. Sujeira na árvore bloqueia o fechamento.
4. **Evidência de Fechamento:** Registrar hash final, data e signoff do auditor no `STATE.md`.
5. **Registro de Legado:** Migrar decisões críticas para o `JOURNAL.md`.

> ⚠️ **Bloqueio Fail-Closed:** Se qualquer item da auditoria falhar, a onda permanece aberta. A declaração de conclusão sem este rito é classificada como **Fraude Narrativa**.

---

## 🛡️ 2.4 Checklist Anti-Reincidência (Runbook)
Para evitar a repetição de erros operacionais detectados em auditorias anteriores:

1. **[ ] Git Status Check:** Rodar `git status --short` antes de qualquer claim de "árvore limpa".
2. **[ ] Hash Anchor:** Usar o commit estável imediatamente anterior como `start_hash`, nunca o commit em formação.
3. **[ ] Metadata Freshness:** Atualizar `Ultima Atualizacao` em arquivos normais a cada modificação.
4. **[ ] Acceptance Sync:** Garantir que `acceptance: [x]` no `spec.md` reflita as tarefas concluídas no `tasks.md`.
5. **[ ] Chronology Radar:** Verificar se novos logs no `JOURNAL.md` mantêm a ordem cronológica do projeto.

### 📊 Log de Fricção `[GOVERNANCE-FRICTION]`
Sempre que uma regra advisory for violada (ex: cronologia do Journal ou Metadata Freshness), o Agente deve registrar o evento no `maintenance/HARNESS_LOG.md`:
- `[GOVERNANCE-FRICTION] <data> | <arquivo> | <descrição do desvio>`
- *Nota:* Este log não bloqueia o commit, mas serve para métricas de "Dívida de Governança" na próxima auditoria.

---

## ⚙️ 3. Regras de Manutenção & Ciclo de Vida

### 🔄 Ciclo de Vida de PRD e Schema
1.  **Upgrade:** Antes de alterar o `brain/PRD.md` ou `maintenance/schema.sql`, uma cópia do estado atual deve ser movida para a respectiva subpasta no `_archive_context/`.
2.  **Snapshot:** O arquivo na raiz da camada deve representar sempre o estado "Em Execução" ou "Produção".

### 🧪 Gestão do `.specs/` (The Workshop)
- **Efemeridade:** Specs são rascunhos de execução. Pós-merge ou >48h inativo → arquivar em `_archive_context/specs/` ou deletar.
- **Validação Leve:** O validador checa apenas a existência e a presença do `STATE.md`, sem fiscalizar o conteúdo interno para manter a agilidade.
- **Sincronia:** Decisões arquiteturais tomadas durante o TLC **devem** ser migradas para o `JOURNAL.md` antes da limpeza da spec.

### 🤖 Roteamento & Isolamento Multi-Agent
1.  **Ativação:** Consultar `brain/AGENT_REGISTRY.md` + template de `brain/PROMPT_LIBRARY.md` e declarar ativação.
2.  **Janela de Contexto:** Global + Role-Specific + Task-Ephemeral. Nunca carregar o `_archive/` sem comando explícito.
3.  **Radar Arquitetural:** Sempre consulte `monitoring/PROJECT_INDEX.md` ANTES de criar novos arquivos, utilitários ou componentes para evitar duplicação de código.
4.  **Sync Pós-Execução:** Ao finalizar uma tarefa, valide a consistência entre código, `schema.sql` e `JOURNAL.md` antes de encerrar.

### 📝 Gestão do JOURNAL.md
- **Limite:** Máximo de 600 linhas.
- **O Purge:** Ao atingir o limite, os 70% mais antigos vão para o arquivo e os 30% mais novos ficam como semente.

---

> *Este template transforma um repositório comum em um ecossistema inteligível para IAs de alta performance.*
