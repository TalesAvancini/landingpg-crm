# Relatório Estratégico V2: Micro-Passos Reais do Executor & Chain-Skills

> **Data:** 2026-05-02 21:16 (BRT)
> **Autoria:** Antigravity (Opus 4.6 Thinking)
> **Método:** Cruzamento de 7 fontes (spec-driver.md × SDD_PLAYBOOK × MASTER_FLOW × RULES.md × CHECKLIST.md × _template.md × governance_rules_hardening real)

---

## 1. Fontes Cruzadas para Mapeamento

| Fonte | O que ela define | Micro-passos revelados |
|:---|:---|:---|
| [spec-driver.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.agent/subagents/spec-driver.md) | 5 passos genéricos do prompt | Locate, Pre-flight, Execution, Code, Handoff |
| [SDD_PLAYBOOK.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.specs/features/SDD_PLAYBOOK.md) | 7 Ritos (0-6) | Bootstrap, Baseline, Escopo, Execução, Self-Audit, QA, Fechamento |
| [MASTER_FLOW.md §2.2](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/brain/MASTER_FLOW.md) | Coreografia Hub & Spoke (5 atos) | Spawn, Pre-flight, Execution+Flash-Harness, Auditoria, Finalização |
| [MASTER_FLOW.md §2.3](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/brain/MASTER_FLOW.md) | Rito de Pre-Close Audit (5 itens) | Harness, Coerência, Higiene Git, Evidência, Legado |
| [MASTER_FLOW.md §2.4](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/brain/MASTER_FLOW.md) | Checklist Anti-Reincidência (5 itens) | Git Check, Hash Anchor, Metadata Freshness, Acceptance Sync, Chronology |
| [RULES.md §1-1.8](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/brain/RULES.md) | 8 regras constitucionais + Checklist de Carga | 13 gates bloqueantes |
| [CHECKLIST.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.specs/features/_template_operacional_sprint/CHECKLIST.md) | Checklist operacional por sprint (5 fases, 19 itens) | Bootstrap(6), Início(4), Escopo(3), Self-Audit(5), Fechamento(5) |

---

## 2. Todos os Micro-Passos Reais do Executor (Sprint-Based)

Cruzando as 7 fontes, o executor na verdade executa **24 micro-passos atômicos** organizados em 7 fases. O prompt atual do `spec-driver.md` só menciona 5 deles.

### FASE A: Carga de Contexto (RULES.md §1)
> **Fonte:** RULES.md Checklist de Carga · MASTER_FLOW §2.2 passo 1

| # | Micro-passo | Descrição | Coberto pelo spec-driver.md? |
|---|:---|:---|:---:|
| A1 | **Carregar Global Layer** | Ler RULES.md + MASTER_FLOW.md + ROADMAP.md | ❌ NÃO |
| A2 | **Carregar Role Layer** | Ler AGENT_REGISTRY.md + próprio prompt | ❌ NÃO |
| A3 | **Carregar Ephemeral Layer** | Ler PRD/INCEPTION + schema.sql + últimas linhas do JOURNAL | ❌ NÃO |
| A4 | **Consultar Navigation Layer** | Ler PROJECT_INDEX.md (Radar Arquitetural) | ❌ NÃO |

**Brecha A:** O executor começa a codar sem ter carregado as regras que deveria obedecer. A "Amnésia Seletiva" começa aqui — ele nem sabe quais regras existem.

---

### FASE B: Leitura da Spec (spec-driver.md Passo 1)
> **Fonte:** spec-driver.md passo 1 · CHECKLIST.md seção A · SDD_PLAYBOOK Rito 0

| # | Micro-passo | Descrição | Coberto? |
|---|:---|:---|:---:|
| B1 | **Localizar spec.md** | Ler `.specs/features/<feature>/spec.md` | ✅ SIM |
| B2 | **Validar modo de contrato** | Confirmar `contract_mode` (standard vs sprint_based), verificar ausência de conflito | ❌ NÃO |
| B3 | **Identificar sprint ativa** | Ler `current_sprint` e localizar o bloco da sprint no YAML | ❌ NÃO |
| B4 | **Verificar sprint anterior** | Confirmar que sprints anteriores têm `qa_signoff: true` (RULES §1.4 HG04) | ❌ NÃO |

**Brecha B:** O executor lê a spec mas não valida se o contrato está íntegro. Pode executar sobre uma sprint com a anterior ainda pendente.

---

### FASE C: Validação de Estado (CHECKLIST.md B · SDD_PLAYBOOK Rito 1)
> **Fonte:** SDD_PLAYBOOK Rito 1 · MASTER_FLOW §2.4 itens 1-2 · CHECKLIST.md seção B

| # | Micro-passo | Descrição | Coberto? |
|---|:---|:---|:---:|
| C1 | **Git status limpo** | Rodar `git status --short` e confirmar saída vazia | ❌ NÃO |
| C2 | **Validar start_hash** | Confirmar que `start_hash` no STATE.md é o HEAD atual | ❌ NÃO |
| C3 | **Validar captured_at/by** | Confirmar campos de rastreabilidade preenchidos | ❌ NÃO |
| C4 | **Registrar baseline no JOURNAL** | Escrever entrada de início da sprint no JOURNAL.md | ❌ NÃO |

**Brecha C:** O executor pula completamente o Rito 1. Começa a codar sem baseline estabelecida. Se o `start_hash` estiver desatualizado, o diff na hora do QA será poluído (erro real #2 do SDD_ERRORS_LEDGER).

---

### FASE D: Escopo e Pre-flight (spec-driver.md Passo 2 · SDD_PLAYBOOK Rito 2 · RULES §1.3)
> **Fonte:** spec-driver.md passo 2 · SDD_PLAYBOOK Rito 2 · RULES.md §1.3 · CHECKLIST.md seção C

| # | Micro-passo | Descrição | Coberto? |
|---|:---|:---|:---:|
| D1 | **Extrair scope_allow** | Ler lista de arquivos permitidos do bloco da sprint ativa | ⚠️ PARCIAL |
| D2 | **Extrair scope_deny** | Ler blacklist preventiva | ❌ NÃO |
| D3 | **Executar Pre-flight grep** | Rodar grep dos `pre_flight_grep_terms` | ✅ SIM |
| D4 | **Contar impacto (mecânico)** | Contar arquivos impactados — registro literal, sem interpretação | ⚠️ PARCIAL |
| D5 | **Decisão de gate** | Se impacto > `max_impact_radius` → SCOPE_BLOWOUT | ✅ SIM |
| D6 | **Registrar resultado no STATE.md** | Persistir telemetria do pre-flight (RULES §1.3 item 4) | ❌ NÃO |

**Brecha D:** O executor faz o grep mas (1) não extrai o scope explicitamente como uma whitelist, (2) não registra o resultado no STATE.md, e (3) pode interpretar subjetivamente o resultado.

---

### FASE E: Execução (spec-driver.md Passos 3-4 · SDD_PLAYBOOK Rito 3)
> **Fonte:** spec-driver.md passos 3-4 · SDD_PLAYBOOK Rito 3 · RULES §1.7 · RULES §1.8

| # | Micro-passo | Descrição | Coberto? |
|---|:---|:---|:---:|
| E1 | **Atualizar STATE → IN_PROGRESS** | Transição atômica de estado | ✅ SIM |
| E2 | **Verificar escopo antes de CADA escrita** | Confirmar que arquivo-alvo está no scope_allow | ❌ NÃO |
| E3 | **Escrever código (cirúrgico)** | Implementar mudanças — máximo N linhas por operação | ❌ NÃO (liberdade total) |
| E4 | **Verificar integridade após CADA escrita** | Ler o trecho modificado para confirmar que não corrompeu | ❌ NÃO |
| E5 | **Atualizar tasks.md em tempo real** | Marcar `[x]` conforme conclui cada task | ⚠️ PARCIAL |
| E6 | **Atualizar STATE.md com checkpoints** | Registrar fatos e progresso | ⚠️ PARCIAL |
| E7 | **Sanity Check (se script)** | Se modificou um script de governança → rodar teste mínimo (RULES §1.8) | ❌ NÃO |

**Brecha E:** Esta é a zona de maior risco. O executor tem **liberdade irrestrita** para escrever. Não há:
- Limite de linhas por operação
- Verificação de escopo por arquivo
- Checkpoint entre escritas
- Obrigação de ler o resultado

---

### FASE F: Pre-close Self-Audit (SDD_PLAYBOOK Rito 4 · MASTER_FLOW §2.3 · CHECKLIST.md D)
> **Fonte:** SDD_PLAYBOOK Rito 4 (6 itens) · MASTER_FLOW §2.3 (5 itens) · MASTER_FLOW §2.4 (5 itens)

| # | Micro-passo | Descrição | Coberto? |
|---|:---|:---|:---:|
| F1 | **Git status limpo** | `git status --short` sem saída | ❌ NÃO |
| F2 | **Coerência spec/tasks/state** | Os 3 artefatos contam a mesma história | ❌ NÃO |
| F3 | **Acceptance sync** | Se tasks `[x]` → acceptance no spec `[x]` | ❌ NÃO |
| F4 | **Evidência no JOURNAL** | Registrar progresso/decisões no JOURNAL.md | ❌ NÃO |
| F5 | **Rodar validação automática** | `python run_context.py validate` ou equivalente | ❌ NÃO |
| F6 | **Metadata freshness** | Atualizar timestamps dos arquivos modificados | ❌ NÃO |
| F7 | **Chronology check** | Verificar ordem cronológica do JOURNAL | ❌ NÃO |

**Brecha F:** O prompt do spec-driver **não menciona nenhum** destes 7 passos. O Self-Audit é suposto acontecer "automaticamente" mas o Flash pula direto para o Handoff.

---

### FASE G: Handoff (spec-driver.md Passo 5 · SDD_PLAYBOOK Rito 5 início)
> **Fonte:** spec-driver.md passo 5

| # | Micro-passo | Descrição | Coberto? |
|---|:---|:---|:---:|
| G1 | **Atualizar STATE → AWAITING_QA** | Transição de estado | ✅ SIM |
| G2 | **Emitir /qa-validator** | Spawn do validador | ✅ SIM |

**Brecha G:** O handoff acontece sem que os passos F1-F7 tenham sido executados. O QA recebe um pacote potencialmente sujo.

---

## 3. Resumo de Cobertura

```
COBERTO:      5 de 24 micro-passos (21%)
PARCIAL:      4 de 24 micro-passos (17%)
NÃO COBERTO: 15 de 24 micro-passos (62%)
```

**O prompt atual do spec-driver.md cobre apenas 21% do que o executor deveria fazer.** Os 62% descobertos são onde o Flash "corta caminho".

---

## 4. Proposta: Chain-Skills V2 (Cobertura Total)

Cada Chain-Skill cobre uma FASE inteira e gera um artefato de prova obrigatório.

### Chain-Skill 1: `context-loader` → FASE A

- **Ação:** Carrega e confirma leitura dos 4 layers obrigatórios (RULES, MASTER_FLOW, AGENT_REGISTRY, PROJECT_INDEX)
- **Artefato de prova:** `CONTEXT_LOADED` — flag com lista dos arquivos lidos e timestamp
- **Regras aplicadas:** RULES §1 Checklist de Carga
- **Brecha que fecha:** Amnésia Seletiva (o executor não pode ignorar regras que nunca leu)

### Chain-Skill 2: `spec-reader` → FASE B

- **Precondição:** `CONTEXT_LOADED` existe
- **Ação:** Lê spec.md, extrai campos obrigatórios (contract_mode, current_sprint, scope_allow, definition_of_done, impact_control), valida modo de contrato, verifica sprints anteriores assinadas
- **Artefato de prova:** `SPEC_DIGEST` — resumo estruturado + confirmação de integridade contratual
- **Regras aplicadas:** RULES §1.1 + §1.4 (HG04 ordem de sprint)
- **Brecha que fecha:** Execução sobre contrato corrompido ou sprint anterior pendente

### Chain-Skill 3: `baseline-anchor` → FASE C

- **Precondição:** `SPEC_DIGEST` existe
- **Ação:** Roda `git status --short`, captura HEAD como start_hash, preenche captured_at/by, registra baseline no JOURNAL.md
- **Artefato de prova:** `BASELINE_ANCHORED` — hash + timestamp + confirmação de árvore limpa
- **Regras aplicadas:** SDD_PLAYBOOK Rito 1 + MASTER_FLOW §2.4 itens 1-2
- **Brecha que fecha:** Start_hash desatualizado (erro real #2 do ERRORS_LEDGER)

### Chain-Skill 4: `scope-guard` → FASE D (Escopo + Pre-flight)

- **Precondição:** `BASELINE_ANCHORED` existe
- **Ação:** Extrai scope_allow + scope_deny como whitelist literal, executa grep dos pre_flight_grep_terms, conta impacto mecanicamente, registra telemetria no STATE.md
- **Artefato de prova:** `SCOPE_LOCKED` — whitelist + contagem de impacto + decisão (PASS ou BLOWOUT)
- **Regras aplicadas:** RULES §1.3 (4 itens) + SDD_PLAYBOOK Rito 2
- **Brecha que fecha:** Interpretação subjetiva do grep + falta de registro de telemetria

### Chain-Skill 5: `methodical-writer` → FASE E (Execução)

- **Precondição:** `SCOPE_LOCKED` existe e decisão = PASS
- **Regras invioláveis:**
  - **Máximo de 20 linhas por operação de escrita**
  - **Proibido `multi_replace_file_content`** — retirado do arsenal
  - **Antes de CADA escrita:** verificar se arquivo-alvo está no scope_allow (consultar SCOPE_LOCKED)
  - **Após CADA escrita:** executar `view_file` no trecho para confirmar integridade
  - **Se modificou script de governança:** rodar sanity check (RULES §1.8)
  - **Atualizar tasks.md após cada task concluída** (não no final)
- **Artefato de prova:** `EXECUTION_LOG` — registro de cada operação (arquivo, linhas, antes/depois, scope check)
- **Regras aplicadas:** RULES §1.7 (MIMO) + §1.8 (Sanity) + SDD_PLAYBOOK Rito 3
- **Brecha que fecha:** Escrita destrutiva + violação de escopo + corrupção de SSOTs

### Chain-Skill 6: `integrity-check` → FASE E→F (Ponte)

- **Precondição:** `EXECUTION_LOG` existe e todas as tasks da sprint estão `[x]`
- **Ação:** Verifica coerência spec↔tasks↔state, garante acceptance sync, verifica metadata freshness, verifica cronologia do JOURNAL
- **Artefato de prova:** `INTEGRITY_PASS` — relatório de integridade com cada item verificado
- **Regras aplicadas:** RULES §1.6 (ANTI_FALSE_PASS) + MASTER_FLOW §2.4 itens 3-5
- **Brecha que fecha:** GF-ACCEPTANCE-DESYNC (erro real #4 do ERRORS_LEDGER)

### Chain-Skill 7: `self-audit` → FASE F

- **Precondição:** `INTEGRITY_PASS` existe
- **Ação:** Executa o checklist completo do Rito 4 + Pre-Close Audit (MASTER_FLOW §2.3): git limpo, coerência, acceptance sync, evidência JOURNAL, validação automática
- **Artefato de prova:** `AUDIT_PASS` — checklist com cada item marcado e evidência
- **Regras aplicadas:** RULES §1.5 (CLOSE_WAVE) + SDD_PLAYBOOK Rito 4 (6 itens) + MASTER_FLOW §2.3 (5 itens)
- **Brecha que fecha:** Pulo do Self-Audit + Passagem Falsa

### Chain-Skill 8: `handoff` → FASE G

- **Precondição:** `AUDIT_PASS` existe
- **Ação:** Atualiza STATE.md → AWAITING_QA, emite `/qa-validator`
- **Artefato de prova:** Comando de spawn do validador
- **Regras aplicadas:** spec-driver.md passo 5
- **Brecha que fecha:** Handoff sem auditoria

---

## 5. Cobertura V2 vs V1

| Métrica | Prompt Atual (spec-driver.md) | Chain-Skills V1 (relatório anterior) | Chain-Skills V2 (este relatório) |
|:---|:---:|:---:|:---:|
| Micro-passos identificados | 5 | ~12 (estimativa) | **24** |
| Cobertura | 21% | ~50% | **100%** |
| Fontes cruzadas | 1 (spec-driver.md) | 3 | **7** |
| Gates bloqueantes | 1 (Pre-flight) | 4 | **8** |
| Artefatos de prova | 0 | 4 | **8** |

---

## 6. Cadeia de Dependências Completa (Fail-Closed)

```
context-loader → spec-reader → baseline-anchor → scope-guard
→ methodical-writer → integrity-check → self-audit → handoff
```

```mermaid
graph LR
    CL["1. context-loader<br/>CONTEXT_LOADED"] --> SR["2. spec-reader<br/>SPEC_DIGEST"]
    SR --> BA["3. baseline-anchor<br/>BASELINE_ANCHORED"]
    BA --> SG["4. scope-guard<br/>SCOPE_LOCKED"]
    SG --> MW["5. methodical-writer<br/>EXECUTION_LOG"]
    MW --> IC["6. integrity-check<br/>INTEGRITY_PASS"]
    IC --> SA["7. self-audit<br/>AUDIT_PASS"]
    SA --> HO["8. handoff<br/>/qa-validator"]

    style CL fill:#1a237e,color:#fff
    style SG fill:#b71c1c,color:#fff
    style MW fill:#4a148c,color:#fff
    style SA fill:#006400,color:#fff
    style HO fill:#ff6f00,color:#fff
```

> [!IMPORTANT]
> Se qualquer elo quebrar, toda a cadeia para. O executor não tem como "pular" um elo porque cada skill exige o artefato de prova do elo anterior como precondição.

---

## 7. Decisões Pendentes (Para o Hub)

| # | Decisão | Impacto |
|---|:---|:---|
| 1 | **Limite de linhas do methodical-writer:** 10, 15 ou 20 linhas? | Quanto menor, mais seguro mas mais lento |
| 2 | **Onde armazenar artefatos de prova?** Inline no STATE.md ou arquivo separado (CHAIN_LOG.md)? | STATE.md mantém tudo centralizado mas pode ficar grande |
| 3 | **Hub aprova cada transição?** Sim (máximo controle) ou Não (cadeia automática fail-closed)? | Aprovação manual = mais seguro mas mais lento |
| 4 | **Local das skills:** `.agent/subagents/` ou diretório dedicado `.agent/skills/`? | Separar de subagents mantém clareza de responsabilidade |
| 5 | **Criar skill `context-loader`?** Ou integrar no próprio prompt do spec-driver como invariante? | Skill separada = mais modular; invariante = menos overhead |

---

## 8. Considerações Adicionais (Gemini Pro) - Garantia de Execução em Cadeia e Hard Gates

A análise anterior (Opus) expôs de forma brilhante a necessidade de fragmentar a atuação do executor e a fraqueza de uma auto-auditoria baseada em "honestidade" (Fraude Narrativa). Para assegurar que o modelo obedeça a essa cadeia e *realmente* evoque a próxima skill, precisamos das seguintes garantias de arquitetura:

### 8.1. Self-Audit (Skill 7) como Hard Gate (Evidência Bruta)
O Self-Audit do executor **não substitui o QA-Validator**. Ele é a última linha de defesa antes do "Handoff", garantindo que o pacote entregue ao QA não contenha lixo evidente. 
Para que a Skill 7 efetivamente feche a brecha da "Passagem Falsa", o artefato `AUDIT_PASS` não pode ser um simples checklist textual. Ele **DEVE** ser um Dump de Telemetria mecânico, exigindo:
1. **Output do Script de Validação:** O log bruto (stdout) da execução de `python run_context.py validate`.
2. **Snapshot do Git:** A saída literal de `git status --short`.
Se o executor (Flash) tentar mentir, a exigência de log bruto torna a fraude impossível (ele teria que forjar o log do python, o que é detectável pelo QA-Validator ou pelo SAM).

### 8.2. Garantia de Invocação Encadeada (Inquebrabilidade)
Ter o design das skills não assegura que o executor (Flash) irá percorrê-las sem parar ou pular passos (devido à sua Visão de Túnel). Para que a Chain *não quebre* ou morra no meio:

1. **Gatilho Explícito (Trigger-Forward):** A definição de cada Chain-Skill deve conter a instrução mandatória: *"Ao finalizar com sucesso e registrar o artefato [N], você DEVE invocar a ferramenta/skill [N+1] imediatamente"*.
2. **Fail-Closed Estrito nas Skills:** A Skill N+1 não pode depender apenas da palavra do executor. A própria Skill N+1 deve, em sua lógica interna (ou código), verificar se o artefato/hash gerado pela Skill N realmente existe no disco. Se a prova não existir, a Skill N+1 **falha instantaneamente** (retorna um erro duro para o modelo).
3. **Orquestração Passiva (Opcional):** Caso o Flash perca o fôlego e encerre a execução no meio, a retomada deve ser automática. Ao ser re-invocado, a Skill 1 (Context Loader) deve ser inteligente o suficiente para escanear os artefatos existentes e dizer: *"Vejo que `SCOPE_LOCKED` já existe, saltando para a Skill 5 (Methodical Writer)"*.

O conceito é transformar o executor de um "pensador livre" em uma "cabeça de leitura de máquina de Turing", que só pode avançar se a fita (estado/artefatos) permitir.
