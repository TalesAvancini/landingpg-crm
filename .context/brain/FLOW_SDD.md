# 🏛️ Flow SDD — A Constituição dos 9 Arquivos

> Mapa visual e funcional dos 9 arquivos que compõem o lastro do processo **Spec-Driven Development (SDD)** no framework H.O.K Forge.

---

## 🗺️ 1. Diagrama de Arquitetura (Visão Holística)

```mermaid
graph TB
    classDef law fill:#1a1a2e,stroke:#e94560,color:#fff,stroke-width:2px
    classDef engine fill:#0f3460,stroke:#16213e,color:#fff,stroke-width:2px
    classDef tactical fill:#533483,stroke:#2b2d42,color:#fff,stroke-width:2px
    classDef memory fill:#1b1b2f,stroke:#e2b714,color:#fff,stroke-width:2px
    classDef map fill:#162447,stroke:#1f4068,color:#aaa,stroke-width:1px

    subgraph "⚖️ CAMADA CONSTITUCIONAL — Define 'O Quê' e 'O Limite'"
        RULES["📜 RULES.md<br/>(As Leis)"]:::law
        MASTER["🏛️ MASTER_FLOW.md<br/>(A Orquestração)"]:::law
        REGISTRY["🤖 AGENT_REGISTRY.md<br/>(O DNS Cognitivo)"]:::law
    end

    subgraph "⚙️ CAMADA DE MOTOR — Define 'Como Executar'"
        DRIVER["🕹️ spec-driver.md<br/>(O Executor)"]:::engine
        PLAYBOOK["📜 SSD_PLAYBOOK.md<br/>(O Manual Tático)"]:::engine
        SPECV3["📋 spec_v3.md<br/>(O Molde da Spec)"]:::engine
    end

    subgraph "🧠 CAMADA DE ESTADO — Memória Volátil da Sprint"
        SCRATCHPAD["📥 AGENT_SCRATCHPAD.md<br/>(Rascunho + Escalation)"]:::tactical
        LEDGER["📕 SSD_ERRORS_LEDGER.md<br/>(Cicatrizes Permanentes)"]:::tactical
    end

    subgraph "📡 CAMADA TRANSVERSAL — O Sistema Nervoso"
        RXCOMM["📡 rx-communications.md<br/>(Mapa de Blast Radius)"]:::map
    end

    %% Conexões Constitucionais
    RULES -->|"Restringe"| MASTER
    RULES -->|"Alimenta regras"| DRIVER
    MASTER -->|"Orquestra sequência"| DRIVER
    REGISTRY -->|"Define escopo/permissões"| DRIVER

    %% Conexões de Motor
    PLAYBOOK -->|"Guia tático"| DRIVER
    SPECV3 -->|"Template base"| DRIVER
    DRIVER -->|"Consulta traps"| SCRATCHPAD
    DRIVER -->|"Consulta scars"| LEDGER

    %% Feedback Loops
    LEDGER -.->|"Scars viram Leis"| RULES
    SCRATCHPAD -.->|"Traps recorrentes promovidas"| LEDGER

    %% Transversal
    RXCOMM -.->|"Mapeia impacto de todos"| RULES
    RXCOMM -.->|"Mapeia impacto de todos"| MASTER
    RXCOMM -.->|"Mapeia impacto de todos"| DRIVER
```

---

## 🧬 2. Perfil Individual dos 9 Arquivos

### ⚖️ Camada Constitucional (A Lei)

#### 1. `RULES.md` — As Leis do Ecossistema
| Atributo | Detalhe |
|----------|---------|
| **Localização** | `.context/brain/RULES.md` |
| **Papel no SDD** | Fonte de todas as restrições. Contém 13+ regras formais (CLOSE_WAVE, SAM_SYNTAX, MIMO, etc.) que o executor **deve** obedecer. |
| **Lê de** | `LEARNINGS.md`, `JOURNAL.md` (cicatrizes viram leis) |
| **É consumido por** | `spec-driver.md`, `validate_context.py`, `MASTER_FLOW.md` |
| **Blast Radius** | 🔴 **CRÍTICO** — Alterar uma regra aqui impacta **todos** os arquivos do ecossistema. |

#### 2. `MASTER_FLOW.md` — A Orquestração
| Atributo | Detalhe |
|----------|---------|
| **Localização** | `.context/brain/MASTER_FLOW.md` |
| **Papel no SDD** | Define a coreografia completa Hub & Spoke, o ciclo de vida TLC (5 atos), e o rito de Pre-Close Audit. É o "manual de operações" do framework. |
| **Lê de** | `RULES.md` (restrições), `TLC_INTEGRATION.md` |
| **É consumido por** | `spec-driver.md`, `qa-validator.md` |
| **Blast Radius** | 🔴 Alterar o fluxo aqui desalinha o comportamento do `spec-driver` e do QA. |

#### 3. `AGENT_REGISTRY.md` — O DNS Cognitivo
| Atributo | Detalhe |
|----------|---------|
| **Localização** | `.context/brain/AGENT_REGISTRY.md` |
| **Papel no SDD** | Cadastro de todos os agentes com especialidade, permissões, contexto auto-load e gatilhos. Define **quem** pode fazer **o quê**. Contém a blindagem Chain-Skills V3. |
| **Lê de** | `.agent/subagents/` (definições de agentes) |
| **É consumido por** | Roteamento do Orquestrador, `spec-driver.md` (para saber suas próprias restrições) |
| **Blast Radius** | 🟡 Impacta o escopo de atuação de todas as IAs. Dessincronia aqui = agente operando fora do escopo. |

---

### ⚙️ Camada de Motor (O Como)

#### 4. `spec-driver.md` — O Executor Mecânico
| Atributo | Detalhe |
|----------|---------|
| **Localização** | `.agent/subagents/spec-driver.md` |
| **Papel no SDD** | Subagente determinístico que executa a cadeia de 9 skills. Opera sob Zero-Trust: proibido usar ferramentas genéricas de escrita. Contém protocolos ANTI-LOOP e RESUME. |
| **Lê de** | `RULES.md`, `MASTER_FLOW.md`, `AGENT_REGISTRY.md`, `SSD_PLAYBOOK.md`, `AGENT_SCRATCHPAD.md`, `SSD_ERRORS_LEDGER.md` |
| **Produz** | Mutações em `STATE.md`, código via `write_with_validation.py`, escalations no `SCRATCHPAD` |
| **Blast Radius** | 🔴 **Acoplamento Extremo** — O próprio arquivo declara: qualquer alteração DEVE ser sincronizada com `MASTER_FLOW`, `RULES`, `spec_v3`, `SCRATCHPAD` e `PLAYBOOK`. |

#### 5. `SSD_PLAYBOOK.md` — O Manual Tático
| Atributo | Detalhe |
|----------|---------|
| **Localização** | `.specs/features/SSD_PLAYBOOK.md` |
| **Papel no SDD** | Descreve as 4 fases (A-D) e as 9 skills em detalhe operacional. Documenta o Rito do Córtex (MiMo), protocolo Anti-Loop, e papel do Orquestrador no desbloqueio. |
| **Lê de** | `RULES.md` (restrições base), experiência acumulada |
| **É consumido por** | `spec-driver.md` (guia tático direto) |
| **Blast Radius** | 🟡 Mudança aqui altera o comportamento tático do executor sem alterar as leis formais. |

#### 6. `spec_v3.md` — O Molde da Spec
| Atributo | Detalhe |
|----------|---------|
| **Localização** | `.agent/templates/spec_v3.md` |
| **Papel no SDD** | Template YAML+Markdown que estrutura toda nova spec: frontmatter com `feature_id`, `type`, `contract_mode`, `sprint_allow`, `dod`, `qa_signoff`. Inclui seção de Raw Payloads (Injeção Atômica). |
| **Lê de** | Padrões definidos em `RULES.md` (regra 1.1, 1.4) |
| **É consumido por** | Hub/Planner ao criar nova feature, `spec-driver` ao interpretar o contrato |
| **Blast Radius** | 🟡 Alterar o template afeta **todas as specs futuras**. Specs existentes não são retroativamente afetadas. |

---

### 🧠 Camada de Estado (Memória)

#### 7. `AGENT_SCRATCHPAD.md` — O Rascunho Volátil
| Atributo | Detalhe |
|----------|---------|
| **Localização** | `.agent/templates/AGENT_SCRATCHPAD.md` |
| **Papel no SDD** | Buffer de comunicação entre Executor e Orquestrador. Contém **Known Traps** (soluções para erros comuns), **INBOX** (escalations do subagente) e **DIRECTIVES** (resoluções do humano). |
| **Lê de** | Erros em tempo de execução, `SSD_ERRORS_LEDGER.md` (traps promovidas) |
| **É consumido por** | `spec-driver.md` (primeira consulta em caso de erro) |
| **Blast Radius** | 🟢 Baixo impacto sistêmico. É volátil por design (limpo entre features). Traps crônicas são **promovidas** ao Ledger. |

#### 8. `SSD_ERRORS_LEDGER.md` — As Cicatrizes Permanentes
| Atributo | Detalhe |
|----------|---------|
| **Localização** | `.specs/features/SSD_ERRORS_LEDGER.md` |
| **Papel no SDD** | Registro permanente de erros recorrentes (Scars). Cada entrada documenta: data, feature, erro, causa raiz, correção e regra adicionada. Alimenta o sistema de vacinação (`inject_learnings.py`). |
| **Lê de** | Post-mortems do `JOURNAL.md`, escalations do `SCRATCHPAD` |
| **É consumido por** | `inject_learnings.py` → `*.enriched.md`, `RULES.md` (scars viram leis) |
| **Blast Radius** | 🟡 Nova scar → nova vacina injetada em todas as specs futuras via MiMo. |

---

### 📡 Camada Transversal

#### 9. `rx-communications.md` — O Sistema Nervoso
| Atributo | Detalhe |
|----------|---------|
| **Localização** | `.context/maintenance/rx-communications.md` |
| **Papel no SDD** | Mapa SSOT de toda a topologia de conectividade. Documenta quem afeta quem (blast radius) tanto para arquivos de governança quanto para scripts de automação. É o "raio-X" que previne modificações silenciosas. |
| **Lê de** | Estado real do repositório (reflete a realidade) |
| **É consumido por** | `@gov-friction-analyst`, qualquer agente que precise avaliar impacto antes de modificar |
| **Blast Radius** | 🟢 Não tem impacto executivo direto. É **descritivo**, não prescritivo. Mas se estiver desatualizado, agentes tomam decisões com mapa errado. |

---

## 🔄 3. Matriz de Propagação de Mudanças

> **"Se eu altero o Arquivo A, o que preciso revisar?"**

```mermaid
graph LR
    classDef critical fill:#e94560,stroke:#1a1a2e,color:#fff,stroke-width:3px
    classDef warn fill:#e2b714,stroke:#1a1a2e,color:#000,stroke-width:2px
    classDef info fill:#0f3460,stroke:#16213e,color:#fff,stroke-width:1px

    RULES["RULES.md"]:::critical
    MASTER["MASTER_FLOW.md"]:::critical
    DRIVER["spec-driver.md"]:::critical
    REGISTRY["AGENT_REGISTRY.md"]:::warn
    PLAYBOOK["SSD_PLAYBOOK.md"]:::warn
    SPECV3["spec_v3.md"]:::warn
    SCRATCHPAD["AGENT_SCRATCHPAD.md"]:::info
    LEDGER["SSD_ERRORS_LEDGER.md"]:::info
    RXCOMM["rx-communications.md"]:::info

    RULES -->|"MUST sync"| MASTER
    RULES -->|"MUST sync"| DRIVER
    RULES -->|"SHOULD review"| PLAYBOOK
    RULES -->|"SHOULD review"| SPECV3

    MASTER -->|"MUST sync"| DRIVER
    MASTER -->|"SHOULD review"| REGISTRY

    DRIVER -->|"MUST sync"| MASTER
    DRIVER -->|"MUST sync"| RULES
    DRIVER -->|"MUST sync"| SPECV3
    DRIVER -->|"MUST sync"| SCRATCHPAD
    DRIVER -->|"MUST sync"| PLAYBOOK

    LEDGER -->|"Promove para"| RULES
    SCRATCHPAD -->|"Promove para"| LEDGER

    RXCOMM -.->|"Descreve todos"| RULES
    RXCOMM -.->|"Descreve todos"| MASTER
    RXCOMM -.->|"Descreve todos"| DRIVER
```

### Tabela Resumo de Impacto

| Se alterar... | MUST sync (obrigatório) | SHOULD review (recomendado) |
|:---|:---|:---|
| `RULES.md` | `MASTER_FLOW`, `spec-driver` | `PLAYBOOK`, `spec_v3`, `REGISTRY` |
| `MASTER_FLOW.md` | `spec-driver` | `REGISTRY`, `PLAYBOOK` |
| `spec-driver.md` | `MASTER_FLOW`, `RULES`, `spec_v3`, `SCRATCHPAD`, `PLAYBOOK` | `REGISTRY` |
| `AGENT_REGISTRY.md` | — | `spec-driver` (se mudar permissões) |
| `SSD_PLAYBOOK.md` | — | `spec-driver` (se mudar fases/skills) |
| `spec_v3.md` | — | `spec-driver`, `PLAYBOOK` |
| `AGENT_SCRATCHPAD.md` | — | `LEDGER` (se trap recorrente) |
| `SSD_ERRORS_LEDGER.md` | — | `RULES` (se scar crônica), `SCRATCHPAD` |
| `rx-communications.md` | — | Todos (se topologia mudar) |

---

## ⛓️ 4. Sequência de Execução (A Cadeia das 9 Skills)

```mermaid
sequenceDiagram
    participant Hub as 🧑 Orquestrador (Hub)
    participant SD as 🕹️ spec-driver
    participant Gate as 🔒 write_with_validation.py
    participant QA as 🔍 qa-validator

    Note over Hub: Cria spec usando spec_v3.md template
    Hub->>SD: /spec-driver [instrução]

    rect rgb(26, 26, 46)
        Note over SD: FASE A — Preparação
        SD->>SD: Skill 1: CONTEXT_LOADED<br/>(Lê RULES + enriched.md)
        SD->>SD: Skill 2: SPEC_DIGEST<br/>(npm run context:inject + Fail-Fast)
        SD->>SD: Skill 3: STRATEGY_PLANNER<br/>(STRATEGY_LOG no STATE.md)
    end

    rect rgb(15, 52, 96)
        Note over SD: FASE B — Blindagem
        SD->>SD: Skill 4: BASELINE_ANCHOR<br/>(git hash de segurança)
        SD->>SD: Skill 5: SCOPE_GUARD<br/>(Physical Check: dir/ls allow_list)
    end

    rect rgb(83, 52, 131)
        Note over SD: FASE C — Execução
        SD->>Gate: Skill 6: METHODICAL_WRITER<br/>(Tier 1/2/3 + validação)
        Gate-->>SD: PASS / BLOCKED
        alt BLOCKED
            SD->>SD: Consulta AGENT_SCRATCHPAD Known Traps
            SD->>Hub: [HANDOFF: ESCALATION]
            Hub->>SD: @spec-driver [RESUME]
        end
        SD->>SD: Skill 7: INTEGRITY_CHECK<br/>(spec vs tasks vs state)
    end

    rect rgb(27, 27, 47)
        Note over SD: FASE D — Fechamento
        SD->>SD: Skill 8: SELF_AUDIT<br/>(npm run context:harness)
        SD->>QA: Skill 9: HANDOFF<br/>(/qa-validator)
    end

    QA->>QA: Cronologia + Baseline + Truthfulness
    QA-->>Hub: qa_signoff: true (ou rejeição)
```

---

## 🔑 5. Insights-Chave

> [!IMPORTANT]
> **O `spec-driver.md` é o ponto de convergência** — tudo converge nele porque é ele quem executa o SDD. A preocupação principal não é apenas "se eu altero o spec-driver, o que mais precisa mudar?", mas sobretudo o inverso: **"se eu altero qualquer outro arquivo do sistema, qual o impacto sobre o spec-driver?"**. Ele é o receptor final de todas as leis, fluxos e restrições. A Constituição inteira existe para que ele funcione corretamente.

> [!NOTE]
> **O fluxo de feedback é circular:** Erros em execução → `SCRATCHPAD` (volátil) → `LEDGER` (permanente) → `RULES` (lei). Essa espiral garante que o sistema aprende e endurece com o tempo, sem acumular burocracia temporária.

> [!TIP]
> **O `rx-communications.md` é o checkpoint cognitivo** — não é automatizável via script. É onde se gastam tokens pedindo a um modelo forte (ex: Opus) que verifique se as interações documentadas estão corretas. O `rx-affinity` existe como complemento automatizado (detecta acoplamentos fantasma via git log), mas o valor real do `rx-communications` está na verificação humana/IA das relações de impacto. Sem ele, agentes operam com mapa cego.

---

## 📊 6. Classificação por Camada

| Camada | Arquivo | Natureza | Volatilidade |
|:---|:---|:---|:---|
| ⚖️ Constitucional | `RULES.md` | Prescritiva (Lei) | Baixa (muda só com SCARs graves) |
| ⚖️ Constitucional | `MASTER_FLOW.md` | Prescritiva (Orquestração) | Baixa |
| ⚖️ Constitucional | `AGENT_REGISTRY.md` | Prescritiva (Permissões) | Média (novo agente = nova entrada) |
| ⚙️ Motor | `spec-driver.md` | Executiva (Comportamento) | Baixa (núcleo estável) |
| ⚙️ Motor | `SSD_PLAYBOOK.md` | Executiva (Guia Tático) | Média |
| ⚙️ Motor | `spec_v3.md` | Generativa (Template) | Baixa |
| 🧠 Estado | `AGENT_SCRATCHPAD.md` | Volátil (Buffer) | Alta (limpo entre features) |
| 🧠 Estado | `SSD_ERRORS_LEDGER.md` | Acumulativa (Memória) | Média (cresce monotonicamente) |
| 📡 Transversal | `rx-communications.md` | Descritiva (Mapa) | Média (sincroniza com realidade) |
