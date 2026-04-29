---
Criado em: 2026-04-10 23:28
Ultima Atualizacao: 2026-04-24 13:51
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

---

## 🔄 2.1 Ciclo de Vida TLC Autobuilder (4 Atos)
| Ato | Gatilho | Ferramenta/Script | Saída Esperada |
|-----|---------|-------------------|----------------|
| **1. [Semente]** | `INCEPTION.md` ativo + gaps | `npm run context:enrich` | `PRD.md` lastreado + `market/` populado |
| **2. [Engenharia]** | Criação de `.specs/features/X/` | `qa_signoff: true` no frontmatter | Contrato assinado; se `type: standard`, validador em contexto distinto |
| **3. [Ingestão]** | `RAW/` novo ou `WIKI/` modificado | `npm run context:ingest-guard` | Artigo validado + `wiki_log.md` |
| **4. [Execução]** | `npm run context:harness` + SAM | `harness_runner.py` + `SAM Auditor` | Código validado + `STATE.md: ✅ PASSED` |
| **5. [Rito]** | Merge ou >48h inativo | `npm run context:cleanup` | Spec arquivada + `JOURNAL.md` atualizado |

> 🤖 [SYSTEM HOOK] IA: Este fluxo é imutável. Não pule o Ato 2. Não gere código sem `qa_signoff`. Em `type: standard`, `executor_context_id` e `validator_context_id` devem ser diferentes. Toda entrada no Journal deve passar pelo Reality Check (SAM).

---

---

## 🔄 2.2 Coreografia Hub & Spoke (A Dança)
Para projetos de complexidade média/alta, o Antigravity utiliza a segregação de agentes:

1.  **[Planner - Hub]**: IA Principal desenha a SPEC, define `max_impact_radius` e delega.
2.  **[Pre-flight - Executor]**: Subagente roda `grep` (Pre-flight Gate). Se impacto > Limite → `SCOPE_BLOWOUT` (Telemetria no `STATE.md`).
3.  **[Execution - Executor]**: Subagente coda sob rigor do `flash-harness` (Log sequencial).
4.  **[Auditoria - Validador]**: Subagente valida Semântica (Lógica) + Telemetria (Impacto resolvido).
5.  **[Finalização - Hub]**: IA Principal retoma, valida SAM e arquiva.

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
