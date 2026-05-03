# Chain-Skills V3: Arquitetura Definitiva

> **Versão:** 3.0 FINAL
> **Data/Hora:** 2026-05-02 23:38 (BRT)
> **Autor:** MiMo
> **Referência:** [chain_specdriver.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/planos/SSD-Chain/chain_specdriver.md)
> **Base:** Chain-Skills V2 + Avaliação Crítica + 3 Pilares + Orquestrador Ativo (Agente Central)
> **Princípio:** O executor é um operário mecânico. O agente central é o supervisor que tem poder de intervenção.

---

## Resumo Estratégico

### O Problema
O executor (Gemini Flash) é otimizado para **completar objetivos**, não para **seguir protocolos**. Ele pula etapas, age impulsivamente e tenta "zerar" a sprint de uma vez. O prompt atual do spec-driver.md cobre apenas **21%** dos micro-passos que o executor deveria executar.

### A Solução
A Chain-Skills V3 transforma o executor de um "pensador livre" em uma **máquina de estados controlada** através de:

1. **9 skills sequenciais** com artefatos de prova verificáveis em disco
2. **Script de validação** (`write_with_validation.py`) que bloqueia escritas inválidas antes de serem aplicadas
3. **Ferramentas restritas** (DENY de `edit_file` e equivalentes) que forçam o uso da skill controlada
4. **Strategy Planner obrigatório** que força o executor a pensar antes de agir
5. **Orquestrador ativo** (agente central com memória do chat) que monitora, intervém e registra

### As 6 Garantias

| # | Garantia | Mecanismo |
|---|---|---|
| 1 | O executor **não pode ignorar regras** | Skill 1 (context-loader) força carga de regras |
| 2 | O executor **não pode executar sem pensar** | Skill 3 (strategy-planner) força planejamento por task |
| 3 | O executor **não pode escrever fora do escopo** | Skill 5 (scope-guard) + write_with_validation.py bloqueiam |
| 4 | O executor **não pode pular a auditoria** | Skill 9 (handoff) exige AUDIT_PASS |
| 5 | O executor **não pode mentir** | Skill 8 (self-audit) exige logs brutos verificáveis |
| 6 | Se falhar, **o orquestrador intervém** | Protocolo de 3 níveis com rollback automático |

### O Trade-off

| | V2 (Atual) | V3 (Proposto) |
|---|---|---|
| Velocidade | Rápido (sem controles) | Mais lento (controles por task) |
| Confiabilidade | Baixa (executor pula passos) | Alta (cadeia fail-closed) |
| Auditabilidade | Fraca (narrativa) | Forte (evidência bruta) |
| Intervenção | Manual (humano detecta) | Automática (orquestrador detecta) |
| Cobertura | 21% dos micro-passos | 100% dos micro-passos |

**O custo é velocidade. O ganho é confiabilidade. Para um framework que se orgulha de Zero Trust, esse é o trade-off correto.**

### Nota sobre Implementação
Esta V3 foi desenhada para ser implementada **incrementalmente**. Não é necessário implementar tudo de uma vez. A Fase 1 (fundação) pode ser feita em paralelo com o sistema atual sem quebrar nada. A Fase 5 (piloto) valida se a abordagem funciona antes de generalizar.

### Checklist de Implementação
Ordem recomendada de implementação:

```
FASE 1 — FUNDAÇÃO (sem quebrar nada existente)
  □ Criar .agent/skills/methodical_writer.json
  □ Criar .context/_scripts/write_with_validation.py
  □ Testar write_with_validation.py isoladamente
  □ Atualizar frontmatter do spec-driver.md com tool_permissions

FASE 2 — PROMPT E CADEIA
  □ Substituir prompt do spec-driver.md pela versão V3
  □ Testar cadeia completa em modo dry-run (sem escrita real)
  □ Validar que cada skill gera o artefato esperado no STATE.md

FASE 3 — ORQUESTRADOR
  □ Documentar regras de monitoria para o agente central
  □ Testar protocolo de intervenção Nível 1 (retomada automática)
  □ Testar protocolo de intervenção Nível 2 (rollback)
  □ Testar protocolo de intervenção Nível 3 (aborto)

FASE 4 — INTEGRAÇÃO DA SKILL
  □ Configurar instrução restritiva no prompt da skill (bloqueio cognitivo, sem bloqueio hard global)
  □ Testar obediência: executor não deve usar edit_file
  □ Testar que methodical_writer é a única via de escrita tentada
  □ Testar cenário de falha: workflow_journal_auditor pega violação se a regra for quebrada

FASE 5 — PILOTO
  □ Selecionar 1 feature de risco baixo
  □ Executar em modo sprint_based com a V3 completa
  □ Coletar métricas (seção 8)
  □ Ajustar thresholds baseado em resultados reais

FASE 6 — ESTABILIZAÇÃO
  □ Atualizar SDD_PLAYBOOK.md com a V3
  □ Atualizar SDD_ERRORS_LEDGER.md se novos erros surgirem
  □ Atualizar CHECKLIST.md com os 24 micro-passos
  □ Atualizar AGENT_REGISTRY.md se necessário
  □ Documentar decisões e trade-offs no JOURNAL.md
```

---

## 1. Princípios de Design

### 1.1 Os Três Atores

| Ator | Natureza | Poder | Analogia |
|---|---|---|---|
| **Executor** (@spec-driver) | Subagente isolado, processo limpo, sem memória do chat | Escrever código dentro de permissões | Operário na linha de montagem |
| **Orquestrador** (Agente Central / Hub) | Agente que detém a memória do chat, assume role de monitoria | Monitorar, intervir, deletar, re-invocar | Supervisor de fábrica |
| **Validador** (@qa-validator) | Subagente isolado, processo cego | Aprovar ou reprovar com base em evidência bruta | Inspetor de qualidade |

### 1.2 Por que o Orquestrador é o Agente Central

O orquestrador **não é um subagente separado**. É o próprio agente central (Hub/Planner) que assume uma **role de monitoria** quando necessário. Isso porque:

1. O agente central tem **memória do chat** — viu o que aconteceu, não precisa adivinhar
2. O agente central tem **visão do projeto** como um todo
3. O agente central já **spawna** os subagentes — ele está na posição natural de supervisor
4. Um subagente orquestrador isolado seria **cego** ao contexto e teria que ler apenas artefatos em disco, perdendo nuances que o chat preserva

O agente central ativa a role de orquestrador consultando as regras de monitoria definidas na seção 4.

### 1.3 Regras Fundamentais

1. **O executor nunca se auto-aprova.** Ele produz evidência, o validador aprova.
2. **O orquestrador (agente central) nunca escreve código de feature.** Ele monitora, intervém e registra.
3. **Todo artefato de prova é verificável em disco.** Nunca depende de narrativa.
4. **A cadeia é linear e fail-closed.** Sem saltos, sem atalhos, sem exceções sem registro.
5. **Falha gera intervenção automática.** Não espera o humano perceber.
6. **O executor é um operário de precisão.** Entregas de sprints completas sem logs de tarefas individuais no STATE.md causam REJECT automático do QA-Validator.

---

## 2. Topologia da Cadeia (9 Skills Sequenciais)

### 2.1 Fluxo Geral

```
┌─────────────────────────────────────────────────────────────────────┐
│              AGENTE CENTRAL (Hub / Orquestrador)                     │
│  Memória do chat · Spawn de subagentes · Monitoria ativa             │
│  Ativa role de orquestrador ao spawnar @spec-driver                  │
│  Intervém quando detecta anomalia na cadeia                          │
└──────────┬──────────────────────────────────┬───────────────────────┘
           │ spawn                            │ spawn
           ▼                                  ▼
    ┌──────────────┐                  ┌──────────────┐
    │ @spec-driver │                  │ @qa-validator│
    │ (isolado)    │                  │ (isolado)    │
    │              │                  │              │
    │ Executa as   │                  │ Valida com   │
    │ 9 skills em  │──handoff────────▶│ evidência    │
    │ sequência    │                  │ bruta        │
    └──────────────┘                  └──────────────┘
```

### 2.2 As 9 Skills em Sequência

```
FASE PREPARAÇÃO (Skills 1-5)
═══════════════════════════════════════════════════════════════

  1. context-loader    → CONTEXT_LOADED
         │
         ▼
  2. spec-reader       → SPEC_DIGEST
         │
         ▼
  3. strategy-planner  → STRATEGY_LOG          ← NOVO (Pilar 1)
         │
         ▼
  4. baseline-anchor   → BASELINE_ANCHORED
         │
         ▼
  5. scope-guard       → SCOPE_LOCKED
          │
          ▼
          Nota: O template oficial em `.agent/templates/spec_v3.md` deve ser usado para garantir que 
          arquivos de manutenção (`HARNESS_LOG.md`, `JOURNAL.md`) estejam na whitelist por padrão.

FASE EXECUÇÃO (Skill 6)
═══════════════════════════════════════════════════════════════

         │
         ▼
  6. methodical-writer → EXECUTION_LOG         ← REFORÇADO (Pilar 2)

FASE FECHAMENTO (Skills 7-9)
═══════════════════════════════════════════════════════════════

         │
         ▼
  7. integrity-check   → INTEGRITY_PASS
         │
         ▼
  8. self-audit        → AUDIT_PASS
         │
         ▼
  9. handoff           → /qa-validator
```

### 2.3 Regra de Encadeamento (Fail-Closed)

Cada skill exige o artefato de prova da skill anterior como **precondição**.

| Skill | Precondição (arte fato que deve existir) |
|---|---|
| 1. context-loader | Nenhuma (ponto de entrada) |
| 2. spec-reader | `CONTEXT_LOADED` |
| 3. strategy-planner | `SPEC_DIGEST` |
| 4. baseline-anchor | `STRATEGY_LOG` |
| 5. scope-guard | `BASELINE_ANCHORED` |
| 6. methodical-writer | `SCOPE_LOCKED` com `decision: PASS` |
| 7. integrity-check | `EXECUTION_LOG` com todas as tasks `[x]` |
| 8. self-audit | `INTEGRITY_PASS` |
| 9. handoff | `AUDIT_PASS` |

**Se qualquer precondição falhar, a skill recusa execução e o agente central é notificado.**

### 2.4 Few-Shot Negativo Distribuído (Pilar 3)

Os 4 erros reais do `SDD_ERRORS_LEDGER.md` são injetados nas skills mais relevantes:

| Erro | Skill | Efeito |
|---|---|---|
| #1 — Mistura de modos | Skill 2 (spec-reader) | Força validação de `contract_mode` |
| #2 — start_hash desatualizado | Skill 4 (baseline-anchor) | Força recaptura do HEAD |
| #3 — Regex destrutiva no STATE.md | Skill 6 (methodical-writer) | Força edição cirúrgica |
| #4 — Tasks [x] mas acceptance [ ] | Skill 7 (integrity-check) | Força acceptance sync |

---

## 3. Especificação Detalhada das Skills

### Skill 1: `context-loader` → FASE A

```
PRECONDICAO:  Nenhuma (ponto de entrada)
ARTEFATO:     CONTEXT_LOADED
LOCAL:        STATE.md, secao ## CHAIN_CONTEXT_LOADED
```

**Objetivo:** Carregar as regras que o executor deve obedecer. Sem este passo, o executor opera com "Amnésia Seletiva" — não sabe quais regras existem.

**Ação:**
1. Ler **trechos relevantes** (não arquivos completos para preservar contexto):
   - `RULES.md`: seções §1.1 a §1.8 (regras bloqueantes)
   - `MASTER_FLOW.md`: §2.2 (coreografia) e §2.3 (pre-close)
   - `AGENT_REGISTRY.md`: entrada do `@spec-driver` apenas
2. Confirmar leitura citando **2 regras reais** do RULES.md no STATE.md
3. Registrar timestamp e lista de trechos lidos

**Artefato de prova (STATE.md):**
```markdown
## CHAIN_CONTEXT_LOADED
status: OK
loaded_at: "2026-05-02 22:00 (BRT)"
files_read:
  - RULES.md [§1.1-§1.8]
  - MASTER_FLOW.md [§2.2, §2.3]
  - AGENT_REGISTRY.md [@spec-driver]
rules_cited:
  - "§1.7 MIMO_STATE_INTEGRITY: edicao cirurgica obrigatoria"
  - "§1.3 Pre-flight Gate: impacto > max_impact_radius = SCOPE_BLOWOUT"
```

**Validação:**
- Se `rules_cited` não contém 2 regras reais do RULES.md → artefato rejeitado
- Se algum arquivo da lista não foi lido → artefato rejeitado

**Nota de eficiência:** Carregar apenas trechos reduz consumo de contexto em ~60% comparado com ler os arquivos completos. Isso preserva a janela de contexto do executor para a fase de execução.

---

### Skill 2: `spec-reader` → FASE B

```
PRECONDICAO:  CONTEXT_LOADED existe em STATE.md
ARTEFATO:     SPEC_DIGEST
LOCAL:        STATE.md, secao ## CHAIN_SPEC_DIGEST
```

**Objetivo:** Ler e validar o contrato da feature. Garantir que o executor está operando sobre um contrato íntegro antes de qualquer ação.

**Ação:**
1. Ler `.specs/features/<feature>/spec.md`
2. Extrair e validar:
   - `contract_mode` (standard ou sprint_based)
   - `current_sprint` — identificar bloco da sprint ativa
   - `scope_allow[]` — lista de arquivos permitidos
   - `scope_deny[]` — blacklist (se existir)
   - `acceptance[]` — critérios de aceite da sprint
   - `definition_of_dod` — se modo standard
3. **Validar integridade do contrato:**
   - Proibido ter `type: standard` E `contract_mode: sprint_based` no mesmo spec
   - Se `contract_mode` ausente, assume `standard` como default
4. **Verificar sprints anteriores:**
   - Se `current_sprint != sprint_01`, confirmar que todas as sprints anteriores têm `qa_signoff: true`
   - Se qualquer sprint anterior não assinada → **FALHA: HG04_SPRINT_ORDER**

**Artefato de prova (STATE.md):**
```markdown
## CHAIN_SPEC_DIGEST
status: OK
validated_at: "2026-05-02 22:05 (BRT)"
contract_mode: sprint_based
current_sprint: sprint_03
previous_sprints_signed: true
scope_allow:
  - ".context/_scripts/harness_runner.py"
  - ".specs/features/contract_sprints_v2_safe/spec.md"
scope_deny: []
acceptance_count: 4
acceptance_signed: 0
```

**Few-shot negativo (SDD_ERRORS_LEDGER #1):**
> "ERRO REAL DO PROJETO: Misturar type: standard com contract_mode: sprint_based no mesmo spec. Consequência: Ambiguidade de validação que causou falha no harness. Regra criada: Proibição explícita no Playbook. NÃO REPITA."

**Código de falha:** `HG04_SPRINT_ORDER` — sprint anterior sem qa_signoff

---

### Skill 3: `strategy-planner` → NOVO (Pilar 1)

```
PRECONDICAO:  SPEC_DIGEST existe em STATE.md
ARTEFATO:     STRATEGY_LOG
LOCAL:        STATE.md, secao ## CHAIN_STRATEGY_LOG
```

**Objetivo:** Forçar o executor a **pensar antes de agir**. Resolver o problema raiz do Flash: agir impulsivamente em direção ao objetivo final sem considerar consequências.

**Por que esta skill é crítica:**
Sem ela, a cadeia resolve o problema de "pular passos" mas não resolve o problema de "agir sem pensar". O executor pode seguir todos os ritos mecanicamente e ainda assim fazer más decisões técnicas se não for obrigado a planejar antes de codar.

**Ação:**
Para **CADA task** listada no `tasks.md` que pertence à sprint ativa:
1. Ler a task completa
2. Registrar no STATE.md:
   - `task_id` (ex: TASK-04)
   - `technical_approach` — descrição de COMO vai implementar (mínimo **100 palavras**)
   - `impacted_files` — lista de arquivos que pretende modificar
   - `rules_applied` — regras do RULES.md que se aplicam (mínimo **2**)
   - `risks_identified` — pelo menos 1 risco técnico

**Validação de profundidade:**

| Condição | Resultado |
|---|---|
| `technical_approach` < 100 palavras | REJEITADO: "Estratégia muito rasa. Refine detalhando como evitará efeitos colaterais." |
| `rules_applied` < 2 regras | REJEITADO: "Especifique quais regras do RULES.md se aplicam a esta task." |
| `impacted_files` contém arquivo fora do `scope_allow` | REJEITADO: "Arquivo fora do escopo declarado na sprint." |
| `risks_identified` vazio | REJEITADO: "Identifique pelo menos 1 risco técnico." |

**Artefato de prova (STATE.md):**
```markdown
## CHAIN_STRATEGY_LOG
status: OK
planned_at: "2026-05-02 22:10 (BRT)"

### TASK-04
technical_approach: |
  Implementar o detector de modo no harness_runner.py adicionando uma funcao
  detect_contract_mode() que le o frontmatter YAML do spec.md e retorna
  'standard' ou 'sprint_based'. A funcao sera chamada no inicio de main()
  antes de qualquer validacao. Para specs sem campo contract_mode, assume
  'standard' como default (backward compatibility). A deteccao usa regex
  para extrair o campo do bloco YAML entre os delimitadores ---. Se ambos
  type e contract_mode estiverem presentes, gera erro de ambiguidade via
  excecao que e capturada pelo harness como HG_CONTRACT_AMBIGUITY. A funcao
  retorna uma tupla (mode, error) para que o caller decida o fluxo.
  [100+ palavras]
impacted_files:
  - ".context/_scripts/harness_runner.py"
rules_applied:
  - "§1.7 MIMO_STATE_INTEGRITY: edicao cirurgica, nao sobrescrever blocos inteiros"
  - "§1.4 Contract Sprints v2-Safe: dual mode obrigatorio"
risks_identified:
  - "Regex de YAML pode falhar com frontmatter malformado — tratar com fallback"
```

**Mecanismo de validação (Script):**

O `write_with_validation.py` verifica se existe `### {task_id}` dentro do `CHAIN_STRATEGY_LOG` antes de permitir qualquer escrita. Se o executor tentar codar sem ter planejado a task, a escrita é bloqueada.

**Efeito cognitivo:** Ao escrever o `technical_approach` com 100+ palavras, o executor é obrigado a:
- Ler a task com atenção
- Consultar as regras carregadas na Skill 1
- Considerar impactos e riscos
- Formular uma estratégia antes de agir

Isso transforma o executor de um "copiador impulsivo" em um "revisor de estratégia de si mesmo".

---

### Skill 4: `baseline-anchor` → FASE C

```
PRECONDICAO:  STRATEGY_LOG existe em STATE.md
ARTEFATO:     BASELINE_ANCHORED
LOCAL:        STATE.md, secao ## CHAIN_BASELINE
```

**Objetivo:** Capturar o estado Git como ponto de partida imutável da sprint. Sem baseline válida, qualquer diff posterior é inválido.

**Ação:**
1. Executar `git status --short`
2. Se saída não vazia → **FALHA**: "Árvore Git suja. Commit ou stash antes de prosseguir."
3. Executar `git rev-parse HEAD` → capturar hash completo
4. Registrar no STATE.md: `start_hash`, `captured_at`, `captured_by`
5. Confirmar que o hash é válido executando `git cat-file -t <hash>` (deve retornar "commit")
6. Registrar baseline no JOURNAL.md com entrada formatada

**Artefato de prova (STATE.md):**
```markdown
## CHAIN_BASELINE
status: OK
start_hash: "4b16b4c935ee57633e76d91f42289c026021200a"
captured_at: "2026-05-02 22:15 (BRT)"
captured_by: "@spec-driver"
git_tree_clean: true
hash_validated: true
```

**Few-shot negativo (SDD_ERRORS_LEDGER #2):**
> "ERRO REAL DO PROJETO: start_hash ficou desatualizado após novos commits, poluindo o diff da sprint. Consequência: Diff inválido na hora do QA, gerando falso positivo. Regra criada: Recaptura obrigatória do HEAD. NÃO REPITA."

**Regra de proteção do start_hash:**
- O `start_hash` só pode ser escrito **uma vez** por sprint
- Tentativas de sobrescrever são bloqueadas pelo orquestrador
- Se o hash referenciar commit inexistente (ex: force-push), o orquestrador gera alerta e exige recaptura justificada

**Entrada no JOURNAL.md:**
```markdown
- **[2026-05-02 22:15]** | BASELINE | Sprint sprint_03 iniciada | start_hash: 4b16b4c9 | executor: @spec-driver
```

**Códigos de falha:**
- `GF-ATOMIC-DESYNC` — sprint sem start_hash válido
- `GF-DIRTY-TREE` — árvore Git suja no momento da captura

---

### Skill 5: `scope-guard` → FASE D

```
PRECONDICAO:  BASELINE_ANCHORED existe em STATE.md
ARTEFATO:     SCOPE_LOCKED
LOCAL:        STATE.md, secao ## CHAIN_SCOPE
```

**Objetivo:** Transformar o escopo declarativo do spec em uma **whitelist operacional** que a Skill 6 (methodical-writer) usa para validar cada escrita. Esta skill é o "cadeado" que a Skill 6 "destrava" arquivo por arquivo.

**Ação:**
1. Ler `scope_allow` e `scope_deny` do `SPEC_DIGEST` (Skill 2)
2. Montar a **whitelist final** = `scope_allow` - `scope_deny`
3. Executar `grep_search` com os `pre_flight_grep_terms` do spec
4. Contar arquivos impactados **mecanicamente** (sem interpretação subjetiva)
5. Se contagem > `max_impact_radius` → **FALHA: HG01_SCOPE_VIOLATION** → registrar `SCOPE_BLOWOUT`
6. Se PASS → registrar whitelist como **literal array** no STATE.md
7. Registrar telemetria do pre-flight (termos buscados, contagem, resultado)

**Artefato de prova (STATE.md):**
```markdown
## CHAIN_SCOPE
status: LOCKED
decision: PASS
locked_at: "2026-05-02 22:20 (BRT)"
whitelist:
  - ".context/_scripts/harness_runner.py"
  - ".specs/features/contract_sprints_v2_safe/spec.md"
  - ".specs/features/contract_sprints_v2_safe/tasks.md"
  - ".specs/features/contract_sprints_v2_safe/STATE.md"
  - ".context/maintenance/JOURNAL.md"
blacklist: []
impact_count: 3
max_impact_radius: 8
pre_flight_terms_matched:
  - "contract_mode" (2 ocorrências)
  - "detect_mode" (1 ocorrência)
```

**Regra crítica:** A `whitelist` registrada aqui é a **mesma lista** que o `write_with_validation.py` consulta na Skill 6. Se o executor tentar editar um arquivo fora desta lista, a escrita é bloqueada em tempo real.

**Cenário SCOPE_BLOWOUT:**
```markdown
## CHAIN_SCOPE
status: BLOWOUT
decision: FAIL
locked_at: "2026-05-02 22:20 (BRT)"
reason: "HG01_SCOPE_VIOLATION: impact_count (12) > max_impact_radius (8)"
impact_count: 12
max_impact_radius: 8
action_required: "Re-fragmentar a spec ou aumentar o limite se justificado"
```

Quando SCOPE_BLOWOUT ocorre:
- A cadeia **para**
- O agente central é notificado
- Nenhuma escrita é permitida
- O executor atualiza `STATE.md` e aguarda decisão do Hub

**Códigos de falha:**
- `HG01_SCOPE_VIOLATION` — impacto excede max_impact_radius
- `HG05_OUTSIDE_WORKSHOP` — alteração fora de `.specs` sem whitelist aprovada

---

### Skill 6: `methodical-writer` → FASE E (Execução)

```
PRECONDICAO:  SCOPE_LOCKED existe E decision = PASS
ARTEFATO:     EXECUTION_LOG
LOCAL:        STATE.md, secao ## CHAIN_EXECUTION_LOG
```

**Objetivo:** Esta é a skill mais controlada da cadeia. É o ponto onde o executor "ganha as mãos" e onde o risco de comportamento impulsivo é maior. Toda escrita é validada por script antes de ser aplicada.

---

#### 6.1 Regras Invioláveis (Hard Gates)

| # | Regra | Consequência de violação |
|---|---|---|
| H1 | Antes de CADA escrita, confirmar que `file_path` está na `whitelist` do SCOPE_LOCKED via `write_with_validation.py` | **Bloqueio imediato** + registro de tentativa |
| H2 | Máximo **15 linhas** por operação de escrita (Tier 1) | **Bloqueio** + exigir justificativa para Tier 2 |
| H3 | Após CADA escrita, executar `view_file` no trecho modificado para confirmar integridade | **Bloqueio** se leitura não confirmada |
| H4 | Atualizar `tasks.md` **imediatamente** após cada task concluída (não no final) | **Bloqueio** se tasks.md desatualizado |
| H5 | Se modificou script de governança → rodar sanity check (RULES §1.8) | **Bloqueio** se sanity falhar |
| H6 | Proibido usar `edit_file` ou equivalentes (Regra Cognitiva da Skill) | Auditoria (SAM) pega a violação e **aborta** a sprint |

---

#### 6.2 Tiers de Escrita

| Tier | Linhas | Condição |
|---|---|---|
| **Tier 1** | Até 15 | Padrão (Ideal para pequenos patches) |
| **Tier 2** | 16-50 | Requer justificativa no EXECUTION_LOG **antes** da escrita (Uso mandatório se Tier 1 for quebrar blocos lógicos como funções inteiras) |
| **Tier 3** | 50+ | Apenas para arquivos **novos** ou reescrita total com aprovação do scope |

**Justificativa para Tier 2 (exemplo):**
```markdown
[TASK-05] Tier 2 justification: Refatoracao da funcao check_sprint_contract()
necessita 32 linhas pois substitui validacao monolitica por deteccao de modo
dual. Nao e possivel fragmentar sem quebrar a funcao atomicamente.
```

---

#### 6.3 Protocolo de Escrita (Passo a Passo por Task)

```
LOOP para cada task da sprint ativa:

  PASSO 1: Ler task_id do tasks.md (proxima task [ ])

  PASSO 2: Consultar STRATEGY_LOG para esta task_id
           → Se nao existir: BLOQUEAR. "Execute strategy-planner primeiro."

  PASSO 3: Chamar write_with_validation.py
           → python write_with_validation.py <feature_id> <task_id> <file_path> <line_count>
           → Se exit 1: BLOQUEAR. Motivo retornado pelo script.

  PASSO 4: Verificar tier de escrita
           → Se Tier 2+: registrar justificativa no EXECUTION_LOG ANTES de escrever

  PASSO 5: Escrever (maximo 15 linhas por operacao no Tier 1)

  PASSO 6: Executar view_file no trecho modificado
           → Confirmar que o conteudo escrito esta integro

  PASSO 7: Se script de governanca modificado → rodar sanity check
           → python -c "import ast; ast.parse(open('<file>').read())"
           → Se falhar: ROLLBACK via git checkout

  PASSO 8: Atualizar tasks.md → marcar [x] na task concluida

  PASSO 9: Registrar no EXECUTION_LOG (STATE.md):
           - task_id
           - file_path
           - lines_written
           - tier
           - scope_check: PASS
           - integrity_check: PASS (view_file confirmado)
           - sanity_check: PASS | SKIPPED | FAIL
           - tasks_md_updated: true

  PASSO 10: Proxima task. Repetir do PASSO 1.
```

---

#### 6.4 Artefato de Prova (STATE.md)

```markdown
## CHAIN_EXECUTION_LOG
status: OK
completed_at: "2026-05-02 23:00 (BRT)"
total_tasks: 5
total_writes: 8

### TASK-04
- file: ".context/_scripts/harness_runner.py"
- lines_written: 12
- tier: 1
- scope_check: PASS
- integrity_check: PASS
- sanity_check: PASS
- tasks_md_updated: true

### TASK-05
- file: ".context/_scripts/harness_runner.py"
- lines_written: 32
- tier: 2
- tier_justification: "Refatoracao de funcao monolitica para dual mode"
- scope_check: PASS
- integrity_check: PASS
- sanity_check: PASS
- tasks_md_updated: true

### TASK-06
- file: ".specs/features/contract_sprints_v2_safe/spec.md"
- lines_written: 8
- tier: 1
- scope_check: PASS
- integrity_check: PASS
- sanity_check: SKIPPED (nao e script de governanca)
- tasks_md_updated: true
```

---

#### 6.5 Few-Shot Negativo (SDD_ERRORS_LEDGER #3)

> "ERRO REAL DO PROJETO: Atualização destrutiva do STATE.md por regex agressivo causou perda de campos obrigatórios da sprint. Consequência: Sprint corrompida, campos de QA e checkpoint perdidos. Regra criada: MIMO_STATE_INTEGRITY — edição cirúrgica obrigatória, nunca sobrescrever blocos inteiros. NÃO REPITA."

---

#### 6.6 Protocolo de Falha na Execução

| Cenário | Código | Ação do Orquestrador |
|---|---|---|
| Arquivo fora da whitelist | `HG01_SCOPE_VIOLATION` | Deletar último artefato (`git checkout -- <file>`), STATE.md → `BLOCKED`, registrar violação |
| Sanity check falhou | `SANITY_FAIL` | Rollback do script (`git checkout -- <file>`), STATE.md → `BLOCKED` |
| Tasks.md não atualizado | `GF-SILENT-MOD` | Orquestrador força atualização e registra infração |
| Executor usou ferramenta DENYed | `GF-TOOL-VIOLATION` | Sistema bloqueia (Antigravity DENY), orquestrador registra tentativa |
| Strategy drift (código diverge do planejado) | `GF-STRATEGY-DRIFT` | Orquestrador registra divergência, exige justificativa |

---

#### 6.7 Cenário de Falha Detalhado

**Cenário: Executor viola escopo na TASK-05 (de 5 tasks)**

```
1. Executor completou TASK-04 com sucesso (EXECUTION_LOG parcial)
2. Na TASK-05, executor tenta editar .context/brain/RULES.md
3. write_with_validation.py retorna exit 1:
   "[BLOCKED] ARQUIVO FORA DO ESCOPO: .context/brain/RULES.md
    nao esta na whitelist do CHAIN_SCOPE"
4. Skill bloqueia a escrita
5. Executor atualiza STATE.md com o erro
6. Agente central detecta a falha via monitoria
7. Agente central decide: corrigir escopo ou abortar

Se corrigir:
  → Atualizar scope_allow no spec (nova sprint ou exceção)
  → Re-invocar methodical-writer

Se abortar:
  → STATE.md → ABORTED
  → Registrar no JOURNAL.md e HARNESS_LOG.md
```

**Cenário: Executor "vomita" código sem respeitar o protocolo**

```
1. Executor tenta escrever 80 linhas de uma vez
2. write_with_validation.py retorna exit 1:
   "[BLOCKED] Tier 3 (80 linhas) so permitido para arquivos novos.
    Arquivo .context/_scripts/harness_runner.py ja existe."
3. Skill bloqueia a escrita
4. Executor é forçado a fragmentar em operações de até 15 linhas
5. Cada fragmento passa pelo protocolo completo (PASSO 1-10)

---

### Skill 7: `integrity-check` → FASE F (Ponte Execução → Fechamento)

```
PRECONDICAO:  EXECUTION_LOG existe E todas as tasks da sprint estao [x]
ARTEFATO:     INTEGRITY_PASS
LOCAL:        STATE.md, secao ## CHAIN_INTEGRITY
```

**Objetivo:** Verificar que os 3 artefatos centrais (spec, tasks, state) contam a **mesma história** antes de pedir auditoria. Esta skill é a ponte entre "fiz o trabalho" e "o trabalho está correto".

**Ação:**

**Check 1 — Acceptance Sync**
- Para cada `[x]` no `tasks.md`, verificar que o `acceptance[]` correspondente no `spec.md` também está `[x]`
- Se houver `[x]` em tasks mas `[ ]` em acceptance → **FALHA: GF-ACCEPTANCE-DESYNC**

**Check 2 — Coerência spec/tasks/state**
- O `current_sprint` no spec.md bate com o sprint registrado no STATE.md?
- As tasks concluídas no tasks.md batem com as tasks registradas no EXECUTION_LOG?
- O número de tasks `[x]` no tasks.md é igual ao número de entries no EXECUTION_LOG?

**Check 3 — Metadata Freshness**
- Os timestamps dos arquivos modificados são **posteriores** ao `start_hash`?
- Se algum arquivo modificado tem timestamp anterior → possível manipulação

**Check 4 — Chronology Check**
- As entradas do JOURNAL.md estão em ordem cronológica?
- Se houver inversão → **ALERTA: GF-JOURNAL-ORDER**

**Check 5 — Strategy Compliance (Pilar 1 reforçado)**
- Para cada task, comparar:
  - O que foi **planejado** (STRATEGY_LOG → technical_approach)
  - O que foi **feito** (EXECUTION_LOG → file_path + lines_written)
- Se houver divergência significativa (ex: planejou modificar arquivo A, mas modificou arquivo B) → registrar `GF-STRATEGY-DRIFT`
- Divergências menores (ex: abordagem diferente mas resultado equivalente) → registrar como advisory, não bloqueante

**Artefato de prova (STATE.md):**
```markdown
## CHAIN_INTEGRITY
status: PASS
checked_at: "2026-05-02 23:05 (BRT)"

### Check 1: Acceptance Sync
result: PASS
details: "5 tasks [x] no tasks.md, 5 acceptance [x] no spec.md"

### Check 2: Spec/Tasks/State Coherence
result: PASS
details: "current_sprint=sprint_03 consistente em spec.md e STATE.md. 5 tasks em tasks.md = 5 entries em EXECUTION_LOG."

### Check 3: Metadata Freshness
result: PASS
details: "Todos os 3 arquivos modificados tem timestamps posteriores ao start_hash (2026-05-02 22:15)"

### Check 4: Chronology
result: PASS
details: "12 entradas no JOURNAL.md em ordem cronologia crescente"

### Check 5: Strategy Compliance
result: ADVISORY
details: "TASK-05: planejou 32 linhas, executou 32 linhas. TASK-06: planejou modificar spec.md, executou conforme planejado. Nenhuma divergencia significativa."
divergences: []
```

**Cenário de falha:**
```markdown
## CHAIN_INTEGRITY
status: FAIL
checked_at: "2026-05-02 23:05 (BRT)"

### Check 1: Acceptance Sync
result: FAIL
details: "GF-ACCEPTANCE-DESYNC: TASK-04 esta [x] no tasks.md mas acceptance[0] ainda esta [ ] no spec.md"
action_required: "Sincronizar acceptance no spec.md antes de prosseguir"
```

**Few-shot negativo (SDD_ERRORS_LEDGER #4):**
> "ERRO REAL DO PROJETO: Tasks marcadas [x] no tasks.md mas acceptance permaneceram [ ] no spec.md. Consequência: Fraude narrativa — o executor alegou conclusão sem que o contrato fosse atualizado. Regra criada: check_sprint_acceptance_sync. NÃO REPITA."

**Códigos de falha:**
- `GF-ACCEPTANCE-DESYNC` — FATAL — tasks e acceptance fora de sincronia
- `GF-STRATEGY-DRIFT` — ADVISORY — código diverge do planejado
- `GF-JOURNAL-ORDER` — ADVISORY — inversão cronológica no JOURNAL
- `GF-METADATA-STALE` — ADVISORY — timestamps desatualizados

---

### Skill 8: `self-audit` → FASE F (Auditoria Final do Executor)

```
PRECONDICAO:  INTEGRITY_PASS existe em STATE.md
ARTEFATO:     AUDIT_PASS
LOCAL:        STATE.md, secao ## CHAIN_AUDIT
```

**Objetivo:** Última linha de defesa antes do handoff. Produz **evidência bruta** (logs de scripts, saídas de comandos) que o QA-Validator pode verificar independentemente. Esta skill **não substitui** o QA — ela garante que o pacote entregue ao QA não contém lixo evidente.

**Princípio chave:** O AUDIT_PASS **não pode ser fabricado**. Os logs brutos são verificáveis pelo QA-Validator comparando com o estado real do repositório. Se o executor tentar forjar, o QA vai detectar a discrepância.

**Ação:**

**Item 1 — Git Status (evidência bruta)**
- Executar `git status --short`
- Capturar stdout **literal** (sem edição, sem resumo)
- Se saída não vazia → **FALHA**: árvore suja, não pode prosseguir

**Item 2 — Validação Automática (evidência bruta)**
- Executar `python run_context.py validate`
- Capturar stdout **literal**
- Se exit code != 0 → **FALHA**

**Item 3 — Harness Runner (evidência bruta)**
- Executar `python .context/_scripts/harness_runner.py`
- Capturar stdout **literal**
- Se exit code != 0 → **FALHA**

**Item 4 — JOURNAL Entry**
- Verificar que JOURNAL.md tem pelo menos 1 entrada com timestamp posterior ao `start_hash` referenciando esta sprint

**Item 5 — Metadata Freshness**
- Verificar que os SSOTs modificados (`spec.md`, `tasks.md`, `STATE.md`) têm timestamps frescos

**Artefato de prova (STATE.md):**
```markdown
## CHAIN_AUDIT
status: PASS
audited_at: "2026-05-02 23:10 (BRT)"

### Item 1: git_status_output
```
(empty — arvore limpa)
```

### Item 2: validate_output
```
[OK] All checks passed. 0 errors, 0 warnings.
```

### Item 3: harness_output
```
[HARNESS] Contract mode: sprint_based
[HARNESS] Sprint contract: PASS
[HARNESS] Schema contract: SKIP (no schema references)
[HARNESS] Handoff integrity: PASS
[HARNESS] Impact radius: PASS (3/8)
[HARNESS] Strategic alignment: PASS
[HARNESS] QA signoff: PENDING (expected — awaiting qa-validator)
```

### Item 4: journal_entry_present: true
### Item 5: metadata_freshness: PASS
```

**Regra anti-fraude:**
O QA-Validator, ao receber o handoff, **re-executa** os mesmos 3 comandos (git status, validate, harness_runner) e compara com os logs registrados no AUDIT_PASS. Se houver divergência:
- O executor **mentiu** no self-audit
- Código de falha: `GF-NARRATIVE-FRAUD`
- Handoff rejeitado, executor bloqueado

**Cenário de falha:**
```markdown
## CHAIN_AUDIT
status: FAIL
audited_at: "2026-05-02 23:10 (BRT)"

### Item 1: git_status_output
```
 M .context/_scripts/harness_runner.py
?? .specs/features/contract_sprints_v2_safe/temp_debug.py
```

### Failure reason
"Árvore Git suja. 1 arquivo modificado não commitado, 1 arquivo não rastreado.
 Limpe a árvore antes de prosseguir com o handoff."

### Action required
"git add + git commit ou git stash. Depois re-execute self-audit."
```

**Códigos de falha:**
- `GF-DIRTY-TREE` — árvore Git suja no momento da auditoria
- `GF-VALIDATE-FAIL` — script de validação retornou erro
- `GF-HARNESS-FAIL` — harness_runner retornou erro
- `GF-NARRATIVE-FRAUD` — log bruto não confirma narrativa do executor (detectado pelo QA)

---

### Skill 9: `handoff` → FASE G (Entrega ao Validador)

```
PRECONDICAO:  AUDIT_PASS existe em STATE.md
ARTEFATO:     Comando /qa-validator emitido
LOCAL:        STATE.md + invocação do subagente
```

**Objetivo:** Entregar o pacote completo ao validador com todas as garantias de integridade. Este é o ponto de transição de responsabilidade: do executor para o inspetor.

**Ação:**
1. Atualizar `STATE.md` → `status: AWAITING_QA`
2. Registrar timestamp de handoff
3. Verificar que **todos os 8 artefatos** da cadeia existem:
   - `CONTEXT_LOADED`
   - `SPEC_DIGEST`
   - `STRATEGY_LOG`
   - `BASELINE_ANCHORED`
   - `SCOPE_LOCKED`
   - `EXECUTION_LOG`
   - `INTEGRITY_PASS`
   - `AUDIT_PASS`
4. Se qualquer artefato estiver ausente → **BLOQUEAR handoff**, notificar orquestrador
5. Emitir `/qa-validator` para spawn do validador

**Artefato de prova (STATE.md):**
```markdown
## CHAIN_HANDOFF
status: AWAITING_QA
handed_off_at: "2026-05-02 23:15 (BRT)"
chain_completeness: 8/8
artifacts_present:
  - CONTEXT_LOADED: true
  - SPEC_DIGEST: true
  - STRATEGY_LOG: true
  - BASELINE_ANCHORED: true
  - SCOPE_LOCKED: true
  - EXECUTION_LOG: true
  - INTEGRITY_PASS: true
  - AUDIT_PASS: true
command_emitted: "/qa-validator"
```

**Regra de completude:** Se a cadeia não está 100% completa, o handoff é bloqueado. Isso impede que o executor "pule" para o QA com pacote incompleto.

---

## 4. Protocolo de Monitoria do Agente Central (Role de Orquestrador)

### 4.1 Quando a Role é Ativada

O agente central **não é orquestrador o tempo todo**. Ele ativa a role de monitoria em momentos específicos:

| Momento | Ação do Agente Central |
|---|---|
| **Ao spawnar o executor** | Ativa protocolo de monitoria, começa a observar STATE.md |
| **Ao receber notificação de falha** | Avalia severidade, decide intervenção |
| **Ao verificar timeout** | Executor não produziu artefato em tempo esperado |
| **Ao receber handoff do executor** | Verifica completude da cadeia antes de spawnar o QA |
| **Ao receber resultado do QA** | Decide próximo passo (commit, correção, aborto) |

### 4.2 O Que Ele Monitora

| Sinal | Como Detecta | Severidade |
|---|---|---|
| Artefato de prova ausente | Skill N+1 não encontra artefato de Skill N no STATE.md | **Crítica** |
| Estado inconsistente | STATE.md tem artefatos fora de ordem ou duplicados | **Crítica** |
| Timeout de execução | Skill não produz artefato em tempo esperado | **Alta** |
| Tentativa de salto | Executor tenta pular skill (ex: escrever sem SCOPE_LOCKED) | **Crítica** |
| Ferramenta DENYed | Executor tenta usar `edit_file` (bloqueado pelo Antigravity) | **Alta** |
| Escopo violado | Escrita em arquivo fora da whitelist | **Crítica** |
| Fraude narrativa | Log bruto no AUDIT_PASS não confirma narrativa | **Crítica** |
| Strategy drift | Código não condiz com STRATEGY_LOG | **Advisory** |
| Chain incompleta | Handoff emitido com menos de 8 artefatos | **Crítica** |

### 4.3 Protocolo de Intervenção (3 Níveis)

#### NÍVEL 1 — Correção Automática

```
GATILHO: Artefato ausente ou malformado
IMPACTO: Cadeia parou, executor não consegue prosseguir
ACAO:
  1. Identificar qual artefato esta faltando
  2. Deletar artefatos invalidos posteriores ao ultimo valido
  3. Re-invocar o executor com instrucao:
     "Retome da skill [N]. Artefato [N-1] ja validado."
REGISTRO: STATE.md + JOURNAL.md
```

**Exemplo:**
```
Executor completou CONTEXT_LOADED e SPEC_DIGEST.
Na skill 3 (strategy-planner), executor falhou e nao gerou STRATEGY_LOG.
STATE.md tem CONTEXT_LOADED e SPEC_DIGEST, mas nao STRATEGY_LOG.

Acao do orquestrador:
  1. Detecta que STRATEGY_LOG nao existe
  2. Nao deleta nada (artefatos 1 e 2 sao validos)
  3. Re-invoca executor: "Retome da skill 3 (strategy-planner).
     CONTEXT_LOADED e SPEC_DIGEST ja validados."
```

#### NÍVEL 2 — Rollback + Bloqueio

```
GATILHO: Violacao de escopo, sanity check falhou, tool violation
IMPACTO: Codigo corrompido ou fora do permitido
ACAO:
  1. Identificar o ultimo artefato VALIDO da cadeia
  2. Deletar todos os artefatos POSTERIORES ao valido
  3. Se algum artefato implica escrita de codigo:
     a. Diff pequeno (ate 50 linhas) → git checkout -- <file>
     b. Diff grande (50+ linhas) → git stash, registrar stash hash
     c. Arquivo novo criado → git clean -f ou rm, registrar
  4. Atualizar STATE.md com estado de rollback
  5. Atualizar STATE.md → BLOCKED
  6. Registrar no JOURNAL.md e HARNESS_LOG.md
  7. Aguardar decisao do Hub (corrigir ou abortar)
REGISTRO: STATE.md + JOURNAL.md + HARNESS_LOG.md
```

**Exemplo de rollback:**
```markdown
## CHAIN_ROLLBACK
triggered_at: "2026-05-02 22:45 (BRT)"
level: 2
reason: "HG01_SCOPE_VIOLATION: executor editou .context/brain/RULES.md fora do scope_allow"
last_valid_artifact: SCOPE_LOCKED
deleted_artifacts: [EXECUTION_LOG parcial]
files_reverted:
  - ".context/brain/RULES.md" (git checkout)
new_state: BLOCKED
next_action: "Aguardando decisao do Hub: corrigir escopo ou abortar sprint"
```

#### NÍVEL 3 — Aborto + Notificação

```
GATILHO: 3+ falhas Nivel 2 na mesma sprint, timeout prolongado,
         fraude narrativa detectada, cadeia quebrada apos 2 retomadas
IMPACTO: Executor demonstrou incapacidade de cumprir o protocolo
ACAO:
  1. Interromper executor imediatamente
  2. STATE.md → ABORTED
  3. Registrar motivo detalhado no JOURNAL.md
  4. Registrar no HARNESS_LOG.md
  5. Notificar Hub (humano) para intervenção manual
  6. Nao re-invocar executor automaticamente
REGISTRO: STATE.md + JOURNAL.md + HARNESS_LOG.md + notificacao ao Hub
```

**Exemplo de aborto:**
```markdown
## CHAIN_ABORT
triggered_at: "2026-05-02 23:00 (BRT)"
level: 3
reason: "3 violacoes de escopo na mesma sprint. Executor incapaz de respeitar a whitelist."
failure_history:
  - "22:30 — HG01: tentou editar RULES.md (rollback nivel 2)"
  - "22:40 — HG01: tentou editar MASTER_FLOW.md (rollback nivel 2)"
  - "22:55 — HG01: tentou editar AGENT_REGISTRY.md (rollback nivel 2)"
conclusion: "Executor com Visao de Tunel persistente. Intervencao manual necessaria."
next_action: "Hub deve revisar a spec, ajustar scope, ou substituir o executor."
```

### 4.4 Protocolo de Deleção de Artefato

Quando o orquestrador precisa deletar artefatos inválidos:

```
PASSO 1: Identificar o artefato mais recente que é VALIDO
         (percorrer a cadeia de tras para frente ate encontrar um completo)

PASSO 2: Deletar todos os artefatos POSTERIORES ao valido
         (remover secoes CHAIN_* do STATE.md)

PASSO 3: Se algum artefato implica escrita de codigo:
         a. Pequena (ate 50 linhas) → git checkout -- <file>
         b. Grande (50+ linhas) → git stash push -m "chain-rollback-<timestamp>" -- <file>
            Registrar stash hash no CHAIN_ROLLBACK
         c. Arquivo novo → git clean -f <file> ou rm <file>
            Registrar delecao no CHAIN_ROLLBACK

PASSO 4: Atualizar STATE.md com CHAIN_ROLLBACK contendo:
         - triggered_at
         - level (1, 2 ou 3)
         - reason
         - last_valid_artifact
         - deleted_artifacts (lista)
         - files_reverted (lista com metodo)
         - new_state (IN_PROGRESS ou BLOCKED ou ABORTED)
         - next_action

PASSO 5: Registrar no JOURNAL.md:
         - **[timestamp]** | ROLLBACK | Nivel [N] | Motivo | Acao tomada
```

### 4.5 Retomada Automática (Orquestração Passiva)

Se o executor for interrompido (timeout, crash, perda de contexto, janela de contexto esgotada):

```
PASSO 1: Agente central escaneia STATE.md

PASSO 2: Identifica o ultimo artefato COMPLETO e VALIDO
         (percorrer a ordem da cadeia: CONTEXT_LOADED → SPEC_DIGEST → ... → AUDIT_PASS)

PASSO 3: Calcula proxima skill necessaria:

         Se ultimo valido = CONTEXT_LOADED   → retomar da skill 2 (spec-reader)
         Se ultimo valido = SPEC_DIGEST      → retomar da skill 3 (strategy-planner)
         Se ultimo valido = STRATEGY_LOG     → retomar da skill 4 (baseline-anchor)
         Se ultimo valido = BASELINE_ANCHORED→ retomar da skill 5 (scope-guard)
         Se ultimo valido = SCOPE_LOCKED     → retomar da skill 6 (methodical-writer)
         Se ultimo valido = EXECUTION_LOG    → retomar da skill 7 (integrity-check)
         Se ultimo valido = INTEGRITY_PASS   → retomar da skill 8 (self-audit)
         Se ultimo valido = AUDIT_PASS       → retomar da skill 9 (handoff)

PASSO 4: Re-invoca o executor com instrucao:
         "Cadeia interrompida. Artefatos ate [ultimo_valido] ja validados.
          Retome da skill [N] imediatamente."

PASSO 5: Executor nasce em processo limpo (Zero Trust) mas recebe
         a confirmacao de que os artefatos anteriores existem em disco.
         Ele DEVE verificar lendo o STATE.md antes de prosseguir.
```

**Regra de segurança para retomada:**
Se o EXECUTION_LOG está **incompleto** (ex: 3 de 5 tasks feitas, EXECUTION_LOG parcial):
- O orquestrador **NÃO** retoma da Skill 7 (integrity-check)
- Ele retoma da **Skill 6 (methodical-writer) inteira**
- O executor é forçado a re-verificar o que já fez antes de continuar
- Isso evita que código parcial não verificado seja tratado como completo

### 4.6 Regras de Ouro do Orquestrador

1. **Nunca escrever código de feature.** O orquestrador só manipula STATE.md, JOURNAL.md e HARNESS_LOG.md.
2. **Nunca confiar na narrativa do executor.** Verificar artefatos em disco.
3. **Nunca re-invocar sem rollback.** Se houve falha Nível 2+, limpar antes de retomar.
4. **Nunca ignorar 3 falhas do mesmo tipo.** Após 3 falhas iguais → Nível 3 (aborto).
5. **Sempre registrar.** Toda intervenção gera entrada no STATE.md + JOURNAL.md + HARNESS_LOG.md.
6. **Preservar contexto.** O agente central tem a memória do chat — use-a para diagnosticar a causa raiz, não apenas o sintoma.

---

## 5. Camada de Scripts

### 5.1 `write_with_validation.py`

Script que a Skill 6 (`methodical-writer`) chama **antes de cada escrita**. Se retorna exit 1, a escrita é bloqueada.

```python
#!/usr/bin/env python3
"""
write_with_validation.py — Gate de escrita cirurgica (Chain-Skills V3)
Valida task_id, scope, tier e strategy antes de permitir escrita.
Exit 0 = WRITE_AUTHORIZED | Exit 1 = BLOCKED
"""
import re, sys, os
from pathlib import Path

CONTEXT_DIR = Path(__file__).resolve().parents[1]
SPECS_DIR = CONTEXT_DIR.parent / ".specs" / "features"

TIER_1_LIMIT = 15
TIER_2_LIMIT = 50

def validate_write(feature_id, task_id, file_path, line_count):
    """Retorna (ok: bool, reason: str)"""
    
    # ── 1. Task existe no tasks.md? ──
    tasks_file = SPECS_DIR / feature_id / "tasks.md"
    if not tasks_file.exists():
        return False, f"tasks.md nao encontrado para feature '{feature_id}'"
    tasks_content = tasks_file.read_text(encoding="utf-8")
    if task_id not in tasks_content:
        return False, f"Task '{task_id}' nao encontrada no tasks.md"
    
    # ── 2. STATE.md existe e tem CHAIN_SCOPE? ──
    state_file = SPECS_DIR / feature_id / "STATE.md"
    if not state_file.exists():
        return False, "STATE.md nao encontrado"
    state_content = state_file.read_text(encoding="utf-8")
    
    # ── 3. CHAIN_CONTEXT_LOADED existe? ──
    if "## CHAIN_CONTEXT_LOADED" not in state_content:
        return False, "CHAIN_CONTEXT_LOADED ausente. Execute context-loader primeiro."
    
    # ── 4. CHAIN_SPEC_DIGEST existe? ──
    if "## CHAIN_SPEC_DIGEST" not in state_content:
        return False, "CHAIN_SPEC_DIGEST ausente. Execute spec-reader primeiro."
    
    # ── 5. CHAIN_STRATEGY_LOG existe para esta task? ──
    if f"### {task_id}" not in state_content:
        return False, f"STRATEGY_LOG ausente para {task_id}. Execute strategy-planner primeiro."
    
    # ── 6. BASELINE_ANCHORED existe? ──
    if "## CHAIN_BASELINE" not in state_content:
        return False, "CHAIN_BASELINE ausente. Execute baseline-anchor primeiro."
    
    # ── 7. SCOPE_LOCKED existe e decision = PASS? ──
    if "## CHAIN_SCOPE" not in state_content:
        return False, "CHAIN_SCOPE ausente. Execute scope-guard primeiro."
    scope_block = re.search(
        r"## CHAIN_SCOPE.*?(?=## CHAIN_|\\Z)",
        state_content, re.DOTALL
    )
    if scope_block and "decision: PASS" not in scope_block.group(0):
        return False, "CHAIN_SCOPE decision nao e PASS. Escopo bloqueado (BLOWOUT)."
    
    # ── 8. Arquivo esta na whitelist? ──
    whitelist_match = re.search(
        r"whitelist:\s*\n((?:\s+-\s+.+\n)*)",
        state_content
    )
    if not whitelist_match:
        return False, "Whitelist nao encontrada no CHAIN_SCOPE"
    
    whitelist = re.findall(r'-\s+\"(.+?)\"', whitelist_match.group(1))
    if file_path not in whitelist:
        return False, (
            f"ARQUIVO FORA DO ESCOPO: '{file_path}' "
            f"nao esta na whitelist do CHAIN_SCOPE. "
            f"Arquivos permitidos: {whitelist}"
        )
    
    # ── 9. Verificacao de Tier ──
    line_count = int(line_count)
    if line_count > TIER_2_LIMIT:
        target = CONTEXT_DIR.parent / file_path
        if target.exists():
            return False, (
                f"Tier 3 ({line_count} linhas) so permitido para arquivos novos. "
                f"'{file_path}' ja existe. Fragmente em operacoes de ate {TIER_1_LIMIT} linhas."
            )
    
    if line_count > TIER_1_LIMIT:
        # Tier 2: verificar se ha justificativa registrada
        justification_pattern = rf"### {task_id}.*?tier_justification:"
        if not re.search(justification_pattern, state_content, re.DOTALL):
            return False, (
                f"Tier 2 ({line_count} linhas) requer justificativa no EXECUTION_LOG "
                f"ANTES da escrita. Registre tier_justification para {task_id}."
            )
    
    # ── 10. Todas as verificacoes passaram ──
    return True, f"WRITE_AUTHORIZED | task={task_id} | file={file_path} | lines={line_count} | tier={'1' if line_count <= TIER_1_LIMIT else '2' if line_count <= TIER_2_LIMIT else '3'}"


if __name__ == "__main__":
    if len(sys.argv) < 5:
        print(
            "Uso: python write_with_validation.py "
            "<feature_id> <task_id> <file_path> <line_count>"
        )
        print(
            "Exemplo: python write_with_validation.py "
            "contract_sprints_v2_safe TASK-04 "
            ".context/_scripts/harness_runner.py 12"
        )
        sys.exit(1)
    
    feature_id = sys.argv[1]
    task_id = sys.argv[2]
    file_path = sys.argv[3]
    line_count = sys.argv[4]
    
    ok, reason = validate_write(feature_id, task_id, file_path, line_count)
    
    if ok:
        print(f"[OK] {reason}")
        sys.exit(0)
    else:
        print(f"[BLOCKED] {reason}")
        sys.exit(1)
```

---

### 5.2 Integração com Antigravity IDE

#### Configuração de Ferramentas (DENY/ALLOW)

No Antigravity, configurar o executor para ter ferramentas restritas:

```yaml
# .agent/skills/methodical_writer.json
name: methodical_writer
description: |
  Escreve codigo com validacao obrigatoria via write_with_validation.py.
  Antes de cada escrita, o script valida task_id, scope, tier e strategy.
  Se o script retorna exit 1, a escrita e BLOQUEADA.
  NUNCA escreva diretamente. SEMPRE use esta skill.
parameters:
  task_id:
    type: string
    required: true
    description: "ID da task conforme listado no tasks.md (ex: TASK-04)"
  file_path:
    type: string
    required: true
    description: "Caminho relativo do arquivo a ser modificado"
  content:
    type: string
    required: true
    description: "Conteudo a ser escrito (maximo 15 linhas no Tier 1)"
# Nota: tool_permissions deny removido. Regra 100% via prompt.
```

#### Configuração do Executor no Antigravity

```yaml
# .agent/subagents/spec-driver.md (frontmatter atualizado)
---
name: spec-driver
description: Executor mecanico controlado por Chain-Skills V3
model: flash
readonly: false
# Nota: A restricao de ferramentas e COGNITIVA via prompt,
# nao usamos hard-deny global para manter flexibilidade do orquestrador.
---
```

**Efeito:** O executor tentará instintivamente obedecer à regra do prompt. Se tentar burlar (por erro ou impulsividade) usando `edit_file`, a auditoria de Handoff ou o SAM (Anti-Migué) identificará o uso não-autorizado pelos logs e abortará a sprint por fraude comportamental.

---

## 6. Prompt Atualizado do spec-driver.md (V3)

```markdown
---
name: spec-driver
description: |
  Executor mecanico controlado por Chain-Skills V3.
  Nao toma decisoes de arquitetura. Nao pula etapas.
  Cada escrita passa por validacao de script.
model: flash
readonly: false
---

You are a strict mechanical executor for the H.O.K Forge framework.
Your sole purpose is to execute atomic specifications through a chain of 9 sequential skills.
You do NOT think freely. You follow the chain.

# Zero Trust Invariants
1. You DO NOT modify `brain/` or `market/` unless explicitly commanded by the spec.
2. You DO NOT skip any skill in the chain.
3. You DO NOT write code before SCOPE_LOCKED exists.
4. You DO NOT hand off before AUDIT_PASS exists.
5. You DO NOT use generic edit tools (`edit_file`, `write_to_file`, etc). You MUST use the `methodical_writer` skill. This is a STRICT cognitive rule. Violation triggers SAM abort.
6. Every write MUST pass through write_with_validation.py.

# Chain-Skills Protocol (MANDATORY)

You execute 9 skills in strict sequence. Each produces an artifact in STATE.md.
The next skill ONLY executes if the previous artifact exists.

```
1. context-loader    → CONTEXT_LOADED
2. spec-reader       → SPEC_DIGEST
3. strategy-planner  → STRATEGY_LOG
4. baseline-anchor   → BASELINE_ANCHORED
5. scope-guard       → SCOPE_LOCKED
6. methodical-writer → EXECUTION_LOG
7. integrity-check   → INTEGRITY_PASS
8. self-audit        → AUDIT_PASS
9. handoff           → /qa-validator
```

# Skill Execution Rules

## Before ANY skill:
- Read STATE.md to check which artifacts already exist
- If artifact N-1 is missing: STOP. Report "Precondition failed: [artifact] missing"
- Do NOT fabricate artifacts. They are verified on disk.

## Skill 1: context-loader
- Read RULES.md [§1.1-§1.8], MASTER_FLOW.md [§2.2, §2.3], AGENT_REGISTRY.md [@spec-driver]
- Cite 2 real rules from RULES.md in STATE.md
- Register CONTEXT_LOADED with timestamp

## Skill 2: spec-reader
- Read spec.md, extract contract_mode, current_sprint, scope_allow, acceptance
- Verify no mixing of type:standard + contract_mode:sprint_based
- If current_sprint != sprint_01: verify all previous sprints have qa_signoff: true
- If any previous sprint unsigned: FAIL with HG04_SPRINT_ORDER

## Skill 3: strategy-planner
- For EACH task in tasks.md belonging to the active sprint:
  - Register in STATE.md: task_id, technical_approach (min 100 words),
    impacted_files, rules_applied (min 2), risks_identified (min 1)
- If technical_approach < 100 words: REJECT "Strategy too shallow"
- If rules_applied < 2: REJECT "Specify which RULES.md rules apply"

## Skill 4: baseline-anchor
- Run git status --short. If not empty: FAIL "Dirty tree"
- Run git rev-parse HEAD. Capture hash.
- Register start_hash, captured_at, captured_by in STATE.md
- Register baseline in JOURNAL.md

## Skill 5: scope-guard
- Extract scope_allow and scope_deny from SPEC_DIGEST
- Run grep with pre_flight_grep_terms
- Count impacted files mechanically
- If count > max_impact_radius: FAIL HG01_SCOPE_VIOLATION
- Register whitelist as literal array in STATE.md

## Skill 6: methodical-writer (MOST CONTROLLED)
- FOR EACH task:
  1. Read task_id from tasks.md
  2. Check STRATEGY_LOG for this task_id
  3. Call: python write_with_validation.py <feature> <task_id> <file> <lines>
  4. If exit 1: STOP. Do not write.
  5. If Tier 2: register justification BEFORE writing
  6. Write (max 15 lines per operation)
  7. view_file on modified section to confirm integrity
  8. If governance script modified: run sanity check
  9. Update tasks.md: mark [x]
  10. Register in EXECUTION_LOG

## Skill 7: integrity-check
- Verify acceptance sync: every [x] in tasks.md = [x] in spec.md acceptance
- Verify spec/tasks/state coherence
- Verify metadata freshness (timestamps > start_hash)
- Verify JOURNAL chronology
- Verify strategy compliance (code matches STRATEGY_LOG)

## Skill 8: self-audit
- Capture git status --short (LITERAL stdout)
- Capture python run_context.py validate (LITERAL stdout)
- Capture python harness_runner.py (LITERAL stdout)
- Verify JOURNAL has entry for this sprint
- Verify metadata freshness
- ALL outputs must be LITERAL, not summarized

## Skill 9: handoff
- Verify ALL 8 artifacts exist in STATE.md
- If any missing: BLOCK handoff
- Update STATE.md → AWAITING_QA
- Emit /qa-validator

# Real Errors (DO NOT REPEAT)
1. [Ledger #1] Mixing type:standard + contract_mode:sprint_based → PROHIBITED
2. [Ledger #2] Outdated start_hash → Mandatory recapture
3. [Ledger #3] Destructive regex on STATE.md → Surgical edits only (MIMO)
4. [Ledger #4] Tasks [x] but acceptance [ ] → Mandatory sync

# In Case of Failure
- Do NOT try to fix alone
- Update STATE.md with the error
- Wait for orchestrator (agent central) intervention
- **Note for Orchestrator**: If the failure is a minor Markdown typo in STATE.md (e.g. CHAIN_SCOPE_LOCKED instead of CHAIN_SCOPE), the Orchestrator has autonomy to silently fix it (Intervention Level 1) and proceed, avoiding unnecessary rollbacks.
- If blocked: state reason and STOP

# Philosophy
You are a mechanical engine. You do not question the architecture.
You do not rush to the objective. You follow the chain.
Each step is a gate. No gate, no progress.
```

---

## 7. Mapa de Artefatos no Disco

```
.specs/features/<feature>/
├── spec.md                       ← Contrato soberano
├── tasks.md                      ← Checklist atômico
├── design.md                     ← Arquitetura
└── STATE.md                      ← Tacógrafo (contém todos os CHAIN_*)
    ├── ## CHAIN_CONTEXT_LOADED   ← Skill 1
    ├── ## CHAIN_SPEC_DIGEST      ← Skill 2
    ├── ## CHAIN_STRATEGY_LOG     ← Skill 3 (NOVO)
    ├── ## CHAIN_BASELINE         ← Skill 4
    ├── ## CHAIN_SCOPE            ← Skill 5
    ├── ## CHAIN_EXECUTION_LOG    ← Skill 6
    ├── ## CHAIN_INTEGRITY        ← Skill 7
    ├── ## CHAIN_AUDIT            ← Skill 8
    ├── ## CHAIN_HANDOFF          ← Skill 9
    ├── ## CHAIN_ROLLBACK         ← Se houve intervenção Nível 2+
    └── ## CHAIN_ABORT            ← Se houve intervenção Nível 3

.agent/
├── subagents/
│   ├── spec-driver.md            ← Executor (prompt V3 com Chain-Skills)
│   ├── qa-validator.md           ← Validador (já atualizado para dual mode)
│   └── (chain-orchestrator.md    ← NÃO EXISTE — orquestrador é o agente central)
├── skills/
│   └── methodical_writer.json    ← Skill de escrita controlada (Antigravity)

.context/_scripts/
├── write_with_validation.py      ← NOVO: Gate de escrita cirúrgica
├── harness_runner.py             ← Existente: validação pós-execução
├── validate_context.py           ← Existente: validação de contexto
└── workflow_journal_auditor.py   ← Existente: SAM (Anti-Migué)
```

---

## 8. Métricas de Eficácia

Após implementação, medir para validar se a V3 resolve o problema do executor afobado:

| Métrica | Como Medir | Target | O Que Indica |
|---|---|---|---|
| **Taxa de cadeia completa sem intervenção** | Contagem de sprints sem CHAIN_ROLLBACK | > 80% | O executor respeita o protocolo |
| **Taxa de violações de escopo bloqueadas** | Contagem de HG01 no HARNESS_LOG por sprint | 0 pós-escrita (todas bloqueadas pré-escrita) | O scope-guard funciona |
| **Strategy drift** | Contagem de GF-STRATEGY-DRIFT por sprint | < 10% das tasks | O executor planeja antes de agir |
| **Retomadas automáticas bem-sucedidas** | Contagem de retomadas / total de interrupções | > 90% | A orquestração passiva funciona |
| **Rejeições do write_with_validation.py** | Logs do script por sprint | Decrescente ao longo do tempo | O executor aprende o protocolo |
| **Tempo médio por sprint** | Timestamp CHAIN_CONTEXT_LOADED → CHAIN_AUDIT | Benchmark vs. V2 | Custo de velocidade pelo ganho de confiabilidade |
| **Fraude narrativa detectada** | Contagem de GF-NARRATIVE-FRAUD | 0 | A evidência bruta funciona |
| **Falhas Nível 3 (aborto)** | Contagem de CHAIN_ABORT | 0 após estabilização | O executor está domesticado |

### Dashboard de Monitoramento (Sugestão)

```markdown
## Sprint Dashboard — <feature> — sprint_03

| Métrica | Valor | Status |
|---|---|---|
| Cadeia completa | 9/9 skills | ✅ |
| Intervenções Nível 1 | 0 | ✅ |
| Intervenções Nível 2 | 0 | ✅ |
| Intervenções Nível 3 | 0 | ✅ |
| Violações de escopo | 0 | ✅ |
| Strategy drift | 0 | ✅ |
| Rejeições write_validation | 2 (ambas Tier 2 sem justificativa) | ⚠️ |
| Tempo total da sprint | 45 min | 📊 |
| QA signoff | true | ✅ |
```

---

## 9. Decisões Finais

| # | Decisão | Recomendação | Justificativa |
|---|---|---|---|
| 1 | **Limite de linhas padrão** | **15 (Tier 1)** com Tier 2 (50) e Tier 3 (50+) | 15 força escrita cirúrgica real. Tiers permitem exceções controladas com justificativa |
| 2 | **Artefatos de prova** | **Inline no STATE.md** com prefixo `CHAIN_` | Centralização em um único SSOT de estado. Facilita busca e auditoria |
| 3 | **Aprovação por transição** | **Não** — cadeia automática fail-closed | O QA-Validator já é o gate final. Aprovação manual por skill mataria a velocidade |
| 4 | **Local das skills** | **`.agent/skills/`** | Separação clara: subagents = quem sou, skills = o que faço |
| 5 | **context-loader** | **Skill separada** (não invariante no prompt) | Modularidade permite teste independente e retomada granular pelo orquestrador |
| 6 | **Orquestrador** | **Agente central** (role de monitoria, não subagente) | Tem memória do chat, viu o que aconteceu, pode diagnosticar causa raiz |
| 7 | **Ferramentas DENY** | **edit_file, write_to_file, multi_replace_file_content** | Força o executor a usar methodical_writer exclusivamente |
| 8 | **Localização do prompt V3** | **Substituir** o spec-driver.md atual | Não manter versões paralelas para evitar confusão |

*Base: 7 fontes cruzadas · 24 micro-passos mapeados · 9 skills · 3 pilares · Orquestrador ativo*

```
