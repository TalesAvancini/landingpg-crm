---
Criado em: 2026-05-01 00:51
Ultima Atualizacao: 2026-05-01 00:51
Status: Ativo
---

# 📡 RX-COMMUNICATIONS: Mapa de Conectividade Global (v2)

Este documento é o SSOT da topologia técnica do projeto. Ele descreve o "sistema nervoso" do ecossistema, mapeando como os artefatos de governança e execução se comunicam através de sinais, dependências e gatilhos.

---

## 🌌 1. Mapa Mestre de Conectividade (Visão Holística)

```mermaid
graph TD
    %% ESTILOS (Dark/Technical)
    classDef strategic fill:#1a1a1a,stroke:#333,color:#fff,stroke-width:2px
    classDef tactical fill:#2a2a2a,stroke:#444,color:#fff,stroke-width:2px
    classDef immune fill:#000,stroke:#555,color:#fff,stroke-dasharray: 5 5
    classDef metabolic fill:#111,stroke:#444,color:#aaa
    classDef process fill:#1a1a1a,stroke:#666,color:#fff,stroke-width:3px

    subgraph "CAMADA ESTRATÉGICA (O Porquê)"
        VIS["VISION.md"]:::strategic
        INC["INCEPTION.md"]:::strategic
        PRD["PRD.md"]:::strategic
        VIS --> INC --> PRD
    end

    subgraph "CAMADA CONSTITUCIONAL (A Lei)"
        RUL["RULES.md"]:::process
        MF["MASTER_FLOW.md"]:::process
        RUL --> MF
    end

    subgraph "CAMADA TÁTICA (O Como)"
        SPEC["spec.md"]:::tactical
        TASK["tasks.md"]:::tactical
        STATE["STATE.md"]:::tactical
        SPEC --> TASK --> STATE
    end

    subgraph "SISTEMA IMUNOLÓGICO (A Governança)"
        VAL{{validate_context.py}}:::immune
        LOG["HARNESS_LOG.md"]:::immune
        HEALTH["CONTEXT_HEALTH.md"]:::immune
        VAL --> LOG --> HEALTH
    end

    subgraph "SISTEMA METABÓLICO (A Memória)"
        JOU["JOURNAL.md"]:::metabolic
        SYN{{JOURNAL_SYNAPSE.md}}:::metabolic
        ARC["_archive_context/"]:::metabolic
        JOU <--> SYN --> ARC
    end

    %% CONEXÕES DE FLUXO (As Linhas de Contato)
    
    %% Intenção para Tático
    PRD -.->|Diretriz| SPEC
    
    %% Constituição para todos
    MF -->|Orquestra| SPEC
    RUL -->|Restringe| MF
    RUL -->|Lógica de Validação| VAL
    
    %% Tático para Governança
    STATE -- "Baseline Hash" --> VAL
    SPEC -- "Acceptance Sync" --> VAL
    
    %% Execução para Memória
    STATE -- "Handoff/Registro" --> JOU
    VAL -- "Fricção/Sucesso" --> JOU
    
    %% Feedback Loop
    JOU -.->|Scars / Lições| RUL
    HEALTH -.->|Alerta de Saúde| MF
```

---

## 🔗 2. Tabela de Sinais de Conectividade

| Origem | Destino | Natureza do Sinal | Propósito |
| :--- | :--- | :--- | :--- |
| `PRD.md` | `spec.md` | **Diretriz** | Garante que o código atende ao requisito de negócio. |
| `RULES.md` | `validate_context.py` | **Protocolo** | Alimenta o "DNA" do que deve ser fiscalizado. |
| `MASTER_FLOW.md` | `spec.md` | **Orquestração** | Gatilho de nascimento de uma nova tarefa. |
| `STATE.md` | `validate_context.py` | **Evidência** | Foto física (hash) para garantir que não há drift. |
| `JOURNAL_SYNAPSE.md` | `JOURNAL.md` | **Metabólica** | Limpeza e compressão de memória para evitar bloat. |
| `JOURNAL.md` | `RULES.md` | **Aprendizado** | Cicatrizes (Scars) de erros passados viram novas leis. |

---

## 🛡️ 3. Governança da Conectividade
Qualquer alteração na responsabilidade de um arquivo (Glossário) ou na forma como eles se tocam deve ser refletida neste Mapa. Este documento é o guia definitivo para agentes de IA entenderem seu papel dentro do organismo H.O.K Forge.
