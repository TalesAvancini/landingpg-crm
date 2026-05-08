---
Criado em: 2026-04-10 20:50
Última Atualização: 2026-05-06 21:30
Status: Ativo
---

# 🤖 AGENT_REGISTRY.md
> Catálogo central de especialidades, permissões e escopo de contexto.  
> **Regra de Ouro:** Se um agente não está registrado aqui, ele não existe. Nenhuma tarefa inicia sem roteamento explícito.

💡 *Insight Humano: Este arquivo é o "DNS cognitivo" do projeto. Ele evita que a IA atue de forma genérica, forçando especialização por tarefa. Isso reduz alucinações, melhora a qualidade do código e economiza tokens ao carregar apenas o contexto necessário.*

---

## 🚨 Regra de Registro Obrigatório
> ⚠️ **Atenção para IAs e Humanos:**  
> Antes de criar ou ativar qualquer nova role/agente, você **DEVE** registrá-lo nesta tabela com:  
> - Nome único (`@nome-da-role`)  
> - Especialidade clara e delimitada  
> - Permissões de escrita explícitas (princípio do menor privilégio)  
> - Contexto prioritário para carregamento  
> - Gatilhos de ativação objetivos  
>  
> *Não registrado = Não executado. Esta regra protege a integridade do contexto.*

---

## 📋 Tabela de Agentes Oficiais

| Role | Especialidade | Permissões de Escrita | Contexto Prioritário (Auto-Load) | Gatilho de Ativação |
|------|--------------|----------------------|----------------------------------|---------------------|
| `@db-architect` | Migrations, índices, normalização, otimização de queries | `maintenance/schema.sql`, `migrations/`, `maintenance/TECHNICAL_REQUIREMENTS.md` (seção DB) | `maintenance/schema.sql`, `maintenance/TECHNICAL_REQUIREMENTS.md`, `maintenance/JOURNAL.md` (bugs de performance) | "criar tabela", "migration", "otimizar query", "índice", "normalizar", "ERD" |
| `@frontend-specialist` | UI/UX, componentes, estado, acessibilidade, CSS, responsividade | `src/components/`, `src/pages/`, `src/styles/`, `maintenance/rx-anatomy.md` | `maintenance/rx-anatomy.md`, `maintenance/ARCHITECTURE.md` (UI Layer), `brain/PRD.md` (fluxos visuais) | "tela", "componente", "layout", "responsivo", "acessibilidade", "CSS", "estado" |
| `@backend-engineer` | APIs, auth, lógica de negócio, webhooks, cache, filas | `src/api/`, `src/services/`, `src/utils/`, `src/config/` | `maintenance/rx-biology.md`, `brain/PRD.md`, `maintenance/schema.sql`, `maintenance/TECHNICAL_REQUIREMENTS.md` (APIs) | "endpoint", "rota", "validação", "webhook", "auth", "serviço", "cache" |
| `@qa-validator` | Auditor do circuito SAM, revisor de DoD, validação física de evidências (git diff vs journal), **Gatekeeper de Cronologia V5** | `contract` (frontmatter `qa_signoff`), `tests/`, `maintenance/JOURNAL.md`, `STATE.md`, `HARNESS_LOG.md` | `*.enriched.md`, `STATE.md`, `maintenance/JOURNAL.md` | `"assine contrato"`, `"valide DoD"`, `"auditoria SAM"`, `"veredito QA"` |
| `@devops-guardian` | CI/CD, deploy, env vars, monitoramento, segurança infra | `.github/workflows/`, `Dockerfile`, `maintenance/rebuild_guide.md`, `.env.example` | `maintenance/rebuild_guide.md`, `maintenance/TECHNICAL_REQUIREMENTS.md` (infra), `brain/ROADMAP.md` (deploys) | "deploy", "CI/CD", "docker", "variável de ambiente", "monitoramento", "rollback" |
| `@vision-architect` | Estratégia, validação de market fit, definição de boundaries | `.context/brain/INCEPTION.md`, `.context/market/MARKET_INBOX.md` | `.context/brain/INCEPTION.md`, `.context/market/SSOT_MAP.md` | "definir boundary", "validar gap de mercado", "revisar inception" |
| `@spec-enricher` | Tradução estratégica em PRD, tradução cognitiva VISION -> INCEPTION, validação de gaps de mercado | `.context/brain/PRD.md`, `.context/brain/INCEPTION.proposed.md`, `maintenance/JOURNAL.md` | `.context/brain/INCEPTION.md`, `.context/brain/VISION.md`, `.context/market/SSOT_MAP.md` | "enriquecer spec", "gerar PRD", "traduzir visão", "propor inception", `npm run context:enrich` |
| `@spec-driver` | Executor Chain-Skills V3.2 (Fail-Fast, Grep-First), Physical Check, Raw Payloads | `.specs/`, `src/`, `tests/`, `contract` (frontmatter) | `*.enriched.md`, `STATE.md`, `JOURNAL.md`, `brain/RULES.md`, `AGENT_SCRATCHPAD.md` | `"inicie execução"`, `"autopilot"`, `"execute a spec"`, `"MIMO close"` |
| `@context-keeper` | Sync, purge, validação de consistência, saúde do contexto | `.context/` (exceto `_archive/`), `maintenance/JOURNAL.md`, `brain/RULES.md` | `brain/RULES.md`, `brain/MASTER_FLOW.md`, `maintenance/JOURNAL.md`, `monitoring/CONTEXT_HEALTH.md` | "atualize contexto", "purge", "health check", "validar consistência", "sincronizar" |
| `@fullstack-generalist` | Modo fallback para tarefas transversais ou projetos light | Leitura em todo o projeto; Escrita apenas com confirmação explícita | `brain/PRD.md`, `maintenance/schema.sql`, `maintenance/JOURNAL.md` (últimas 30 linhas) + Global | "modo light", "tarefa rápida", "projeto pequeno", "não especificado" |
| `@gov-friction-analyst` | Diagnóstico de atrito de governança e filtragem de overkill | `.agent/skills/gov-friction-analyst/`, `maintenance/JOURNAL.md` (Checklist de Propagação) | 9 arquivos core (MASTER_FLOW, RULES, etc.), `SSD_ERRORS_LEDGER.md`, `AGENT_SCRATCHPAD.md` | "analise as dores do executor", "resolva bloqueios do gatekeeper", "diagnostique falhas" |
| `@closure-thinker` | Síntese de fechamento analítica e rastreabilidade de origem | `.agent/skills/closure-thinker/`, `CLOSURE.md` | `spec.md`, `STATE.md`, `JOURNAL.md`, `.git/diff` | "gere o closure", "audite a entrega final", "extraia cicatrizes da feature" |

> [!IMPORTANT]
> **Diretriz Operacional (@gov-friction-analyst):**
> 1. Use o `SCRIPT_GLOSSARY` para saber **COMO** agir (buscar ferramentas existentes antes de sugerir novos scripts).
> 2. Use o `rx-communications` para saber **ONDE** o impacto vai bater (validar a topologia planejada).
> 3. Use o `rx-affinity-lite` para validar se a **REALIDADE** do código condiz com o Journal (detectar drift temporal e ghost couplings).
> 4. O objetivo final é sempre a **Sobriedade Arquitetural**: preferir ajustes em `RULES.md` ou templates a soluções burocráticas/overkill.




💡 *Insight Humano: A role `@fullstack-generalist` é sua válvula de escape para projetos simples ou tarefas rápidas. Use com moderação: ela carrega mais contexto e tem menos restrições, o que aumenta o risco de alucinação. Prefira sempre as roles especializadas.*

---

## 🛡️ Blindagem de Subagente (Chain-Skills V3)
> **Invariante de Segurança:** Agentes em modo Executor (`@spec-driver` / `@autopilot`) operam sob restrições físicas (Zero-Trust):
> 1. **Gatekeeper Físico:** Obrigatório usar `write_with_validation.py` para escrever código. Edição direta é bloqueada.
> 2. **Cadeia de 9 Skills:** A execução DEVE fluir linearmente da Skill 1 (Context Loaded) até a Skill 9 (Handoff).
> 3. **Anti-Loop:** Erros `[BLOCKED]` ou `[FATAL]` exigem documentação imediata no `AGENT_SCRATCHPAD.md` antes de nova tentativa.
> 4. **Backpressure:** Acionar `SCOPE_BLOWOUT` se o impacto real > `max_impact_radius`.
> 5. **SAM Compliance:** Proibido fechar tarefa se a "Matriz de Propagação" do Journal não for idêntica ao Git Diff.
> 6. **Acoplamento Extremo:** O `@spec-driver` não opera isolado. Qualquer alteração nele **DEVE** ser sincronizada com `MASTER_FLOW.md`, `RULES.md`, `spec_v3.md`, `AGENT_SCRATCHPAD.md` e `SSD_PLAYBOOK.md`.

---

## 🛡️ Protocolo Hardened Closing (V5)
> **Rito Obrigatório para fechamento de Sprints e Features:**

### 1. @spec-driver (Pre-close Self-Audit)
- [ ] **Higiene:** `git status --short` deve estar vazio (ou apenas arquivos da spec).
- [ ] **MIMO:** Validar que as edições foram cirúrgicas e não reescreveram arquivos desnecessariamente.
- [ ] **Evidência:** Registrar `Harness Check (hash)` e `Impact Radius` no `JOURNAL.md`.
- [ ] **Handoff:** Invocação explícita do `@qa-validator`.

### 2. @qa-validator (Audit & Signoff)
- [ ] **Cronologia:** Validar ordem crescente estrita no `JOURNAL.md`.
- [ ] **Baseline:** Validar que o `start_hash` no `STATE.md` existe no histórico Git.
- [ ] **Truthfulness:** Confrontar `git diff --stat` com a narrativa do `JOURNAL.md`.
- [ ] **Veredito:** Apenas após aprovação física, setar `qa_signoff: true` e assinar o contrato.

---

## 📊 Camada de Telemetria [GOVERNANCE-FRICTION]
> **Códigos oficiais para registro de desvios técnicos e narrativos:**

| Código | Severidade | Descrição |
|--------|------------|-----------|
| `GF-METADATA-STALE` | Advisory | Metadado `Ultima Atualizacao` < Data real do commit. |
| `GF-JOURNAL-ORDER` | Advisory | Inversão cronológica detectada no `JOURNAL.md`. |
| `GF-STATE-FRESHNESS` | Advisory | Campo `updated` do `STATE.md` defasado (> 1h). |
| `GF-ACCEPTANCE-DESYNC`| **FATAL** | Tarefas concluídas mas aceitação na spec pendente. |
| `GF-ATOMIC-DESYNC` | **FATAL** | Sprint em progresso sem `start_hash` válido no Git. |
| `GF-NARRATIVE-FRAUD` | **FATAL** | Alegação de propagação no Journal sem diff real no Git. |
| `GF-SILENT-MOD` | **FATAL** | Modificação física no Git sem registro na Matriz de Propagação. |

> **Uso:** Inserir em `maintenance/HARNESS_LOG.md` no formato:
> `## [GOVERNANCE-FRICTION] <CODIGO> | <YYYY-MM-DD HH:MM>`
> `- **Detalhe:** <Explicação do desvio>`

---

## 🔒 Protocolos de Execução

### 🧭 Roteamento de Tarefas & Spawn de Subagentes
```text
1. Receber comando → 2. Consultar AGENT_REGISTRY.md → 3. Identificar role(s) adequada(s)
4. Declarar ativação: "🤖 Ativando @[role] | Escopo: [descrição curta]"
5. Se for um Executor/Validator isolado (Hub & Spoke):
   - Os prompts de sistema físicos residem na pasta `.agent/subagents/`.
   - O Hub OBRIGATORIAMENTE encerra a sua resposta com o gatilho `/[nome-do-agente] [instrução]`.
   - Isso garante que o host (ex: Cline/Cursor) spawne o agente isolado sem poluição cognitiva.
6. Executar dentro das permissões → 7. Registrar handoff no JOURNAL.md se cruzar domínios
```

### 🤝 Handoff Obrigatório (Cruzamento de Domínios)
> Quando uma tarefa exigir atuação de 2+ agentes:
> 1. Agente atual pausa a execução
> 2. Registra no `JOURNAL.md`:  
>    `🔄 Handoff: @[role-atual] → @[role-próxima] | Estado: [resumo técnico] | Próximo passo: [ação]`
> 3. Aguarda confirmação humana ou prossegue automaticamente (se configurado)
> 4. Próximo agente carrega contexto limpo + estado transferido

💡 *Insight IA: Handoff não é só "passar a bola". É garantir que o próximo agente receba o estado exato da execução, sem ruído. Pense como uma função que retorna um objeto bem tipado: claro, mínimo e autoexplicativo.*

### 🧱 Isolamento de Contexto (Anti-Token-Bloat)
| Camada | Arquivos | Quando Carregar |
|--------|----------|-----------------|
| 🌍 Global | `brain/RULES.md`, `brain/MASTER_FLOW.md`, `brain/ROADMAP.md` | Sempre (regras imutáveis do jogo) |
| 🧭 Strategic | `brain/INCEPTION.md`, `market/SSOT_MAP.md` | Durante planejamento estratégico ou via `@vision-architect` |
| 🎯 Role-Specific | Definido na coluna "Contexto Prioritário" da tabela | Só durante a execução daquele agente |
| 📦 Task-Ephemeral | `brain/PRD.md` ativo, `maintenance/schema.sql`, `maintenance/JOURNAL.md` (últimas 30-50 linhas) | Durante a tarefa atual |
| 🗃️ Deep Archive | `_archive_context/` | Nunca por padrão. Só via comando explícito: "consulte o archive de X" |

> **Regra de Ouro:** `Se o agente não precisa do arquivo para completar a tarefa atual, ele não é carregado.`

---

## 🆕 Como Adicionar um Novo Agente (Template)
```markdown
### `@nome-da-nova-role`
- **Especialidade:** [Descreva em 1 linha o foco principal]
- **Permissões de Escrita:** [Liste pastas/arquivos exatos. Seja restritivo.]
- **Contexto Prioritário:** [Quais arquivos este agente carrega por padrão?]
- **Gatilho de Ativação:** [Palavras-chave ou padrões de comando que disparam esta role]
- **💡 Insight:** [Explique em 1 frase por que esta role é útil e quando usá-la]
```

---

## 📊 Health Check Rápido (Para @context-keeper)
```text
✅ Registry está sincronizado com o código? (Novas pastas têm dono?)
✅ Alguma role está com permissões excessivas? (Princípio do menor privilégio)
✅ Gatilhos de ativação ainda fazem sentido com o PRD atual?
✅ Insight humano está ajudando ou poluindo?
```

💡 *Insight Final: Este arquivo é vivo. Revise-o a cada nova fase do ROADMAP.md. Um registry desatualizado é pior que nenhum registry — ele dá falsa sensação de controle.*
 
