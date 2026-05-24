---
Criado em: 2026-05-22 15:35
Ultima Atualizacao: 2026-05-22 15:35
Status: Ativo
---

# 🌊 FLOW PROPAGATION: O Sistema de Blast Radius

> Mapa visual e didático do sistema de propagação de mudanças (Blast Radius) do H.O.K Forge (SSOT). Entenda como o sistema calcula as ondas de impacto quando você altera um arquivo.

---

## 🗺️ 1. Visão Holística (A Pedra no Lago)

Imagine que o nosso repositório é um lago calmo. Quando você edita um arquivo (seja código, seja regra), é como jogar uma pedra nesse lago. A pedra cai em um ponto central (a **Semente/Seed**), mas cria ondas que se espalham, balançando barcos que estão longe. 

O sistema de propagação existe para **mapear essas ondas antes de você jogar a pedra**, garantindo que nenhum barco afunde sem você saber.

```mermaid
graph TD
    classDef seed fill:#e94560,stroke:#1a1a2e,color:#fff,stroke-width:2px
    classDef motor fill:#0f3460,stroke:#16213e,color:#fff,stroke-width:2px
    classDef must fill:#e94560,stroke:#2b2d42,color:#fff,stroke-width:2px
    classDef likely fill:#e2b714,stroke:#2b2d42,color:#000,stroke-width:2px
    classDef declared fill:#0088cc,stroke:#2b2d42,color:#fff,stroke-width:2px
    classDef semantic fill:#533483,stroke:#2b2d42,color:#fff,stroke-width:2px

    A(("O Arquivo\nModificado\n(A Semente)")):::seed
    
    subgraph "⚙️ O Motor de Sensores (Análise de Propagação)"
        B["Física (AST)<br>Quem importa o quê?"]:::motor
        C["Política (rx-comm)<br>Quem manda em quem?"]:::motor
        D["Semântica (Graphify Explain)<br>O que está correlacionado?"]:::semantic
    end

    A --> B
    A --> C
    A --> D

    subgraph "Os 3 Baldes (Buckets) de Impacto"
        B -->|Mapeou| E["🔴 MUST UPDATE<br>(Física + Política)"]:::must
        C -->|Mapeou| E
        
        B -->|Mapeou só aqui| F["🟡 LIKELY UPDATE<br>(Apenas Física)"]:::likely
        
        C -->|Mapeou só aqui| G["🔵 DECLARED ONLY<br>(Política e Semântica)"]:::declared
        D -->|Mapeou semântica| G
    end
```

---

## ⚙️ 2. O Motor Duplo (A Física vs A Política)

Para calcular até onde as ondas vão, o script principal (`blast_radius.py`) usa **dois sensores** completamente diferentes. Eles olham para o mesmo lago, mas procuram coisas diferentes.

### 🔬 O Sensor Estrutural (A Física)
- **Quem gera:** O *Graphify* (um arquivo chamado `graph.json`).
- **Como pensa:** Ele é um scanner de gravidade. Ele varre o código e vê: *"A função Login chama a função Senha. Logo, se Senha mudar, Login quebra."*
- **Sua limitação:** Ele é cego para regras e humanos. Ele não sabe que se você alterar um PDF de Negócios, um manual em `.md` precisa ser reescrito. Ele só lê código importando código.

### 📜 O Sensor de Governança (A Política)
- **Quem gera:** O `rx-communications.md`.
- **Como pensa:** Ele é a "Constituição". Ele mapeia coisas que o computador não vê, como: *"Se a Regra 1.5 mudar, o Comportamento do Agente de Testes deve mudar."*
- **Sua limitação:** Ele é mantido por humanos e IAs. Se alguém não o atualizou, a lei fica defasada.

### 🧠 O Sensor Semântico (A Semântica Lógica)
- **Quem gera:** O *Graphify* (via comando `$env:PYTHONUTF8=1; graphify explain`).
- **Como pensa:** Ele é um scanner conceitual. Ele analisa o propósito lógico dos arquivos e percebe relações não mapeadas pelo código físico (ex: *"Esta alteração no agregador de erros impacta conceitualmente a especificação do rx-learnings.md"*).
- **Sua utilidade:** Ele serve como o terceiro olho da propagação, revelando ao auditor quais documentos manuais ou de design devem ser visitados, carimbados ou atualizados.

**Por que usar os três?** Porque a física nos dá as quebras de compilação, a política nos dá o contrato legal, e a semântica nos dá a consistência conceitual da documentação.

---

## 🧮 3. A Matemática dos 3 Buckets

Quando o script processa os arquivos que você quer modificar, ele cruza as informações da Física com a Política e joga os arquivos afetados em 3 baldes (buckets) priorizados. 

Aqui está o que cada cor significa para você, traduzido de forma simples:

### 🔴 MUST UPDATE (Apareceu em Ambos)
- **O que significa:** O arquivo foi detectado pela "Física" (estão acoplados no código) E pela "Política" (alguém registrou que um afeta o outro).
- **Tradução Lúdica:** *A casa está pegando fogo e o alarme soou. Você precisa agir!*
- **O que fazer:** Edite e atualize esse arquivo, pois ele quase certamente quebrou ou perdeu sincronia.

### 🟡 LIKELY UPDATE (Só na Física)
- **O que significa:** O *Graphify* notou que eles estão ligados no código, mas o arquivo de governança não mapeou isso como algo crítico.
- **Tradução Lúdica:** *Tem fumaça, mas o alarme não tocou.* Pode ser um acoplamento bobo (ex: dois arquivos usam o mesmo botão), ou pode ser um "acoplamento fantasma" que ninguém notou.
- **O que fazer:** O Agente deve investigar visualmente. Se a mudança afetou a lógica dele, ele entra no pacote. Se não, ignore.

### 🔵 DECLARED ONLY (Só na Política)
- **O que significa:** O código em si não se toca, mas a regra burocrática diz que um afeta o outro (ex: atualizar a versão do app exige atualizar o Changelog).
- **Tradução Lúdica:** *O burocrata está te ligando para assinar o formulário.* 
- **O que fazer:** Se a mudança não exigir reescrever o texto, aplique o **Metadata-Only Propagation** (apenas atualize a data de "Última Atualização" do arquivo afetado para provar que você o visitou e validou).

---

## 📝 4. Tabela de Ação (Cheat Sheet)

Se você é um Subagente (ou um humano), aqui está a sua cartilha de reação quando o Blast Radius jogar arquivos nesses buckets:

| Cor / Balde | Nível de Perigo | O que eu faço com o arquivo afetado? |
| :--- | :--- | :--- |
| 🔴 **MUST UPDATE** | Crítico | Leia o arquivo, adapte a lógica/regras, e **adicione no commit**. |
| 🟡 **LIKELY UPDATE** | Moderado | Faça um `grep` ou leia o arquivo. Ele quebrou? Se sim, conserte. Se não, deixe-o em paz. |
| 🔵 **DECLARED ONLY** | Governança | Faça um "Carimbo Burocrático". Atualize o frontmatter (`Ultima Atualizacao`) do arquivo afetado para atestar que o protocolo foi cumprido, a menos que a mudança exija alterar o conteúdo lógico. |

---

## 🎬 5. O Fluxo de Execução (O Fechamento Semântico)

Como esse motor de sensores e o rito de fechamento são ativados na prática?

```mermaid
sequenceDiagram
    participant SD as 🕹️ spec-driver
    participant Hub as 🧑 Orquestrador (Hub)
    participant QA as 🔍 qa-validator
    participant Skill as 🧠 semantic-propagation (Skill)
    participant Aud as 🕵️ propagation-auditor

    SD->>Hub: Solicita Signoff da Spec
    Hub->>QA: Invoca para Auditoria e QA
    QA->>QA: Valida Diffs e Critérios DoD
    QA-->>Hub: Assina qa_signoff e pergunta: "Devo rodar a propagação?"
    
    alt Spec Pequena/Média (Fusão de Papéis)
        Hub->>QA: Directs: "@qa-validator, execute a skill"
        QA->>Skill: Executa a skill com as Seeds
        Skill-->>QA: Retorna plano de atualização e executa
        QA-->>Hub: Relata conclusão e finaliza
    else Spec Grande (Fallback Tradicional)
        Hub->>QA: Finaliza com Sucesso
        Hub->>Aud: Invoca e envia as Seeds da propagação
        Aud->>Skill: Executa a skill com as Seeds
        Skill-->>Aud: Retorna plano de atualização e executa
        Aud-->>Hub: Relata conclusão e finaliza
    end
    
    Note over Hub: Orquestrador realiza o commit final e cleanup.
```

> [!TIP]
> **A Mágica do Orquestrador:** O `sdd-orchestrator` atua como uma superskill de gestão, direcionando o fluxo. Ele envia os caminhos de arquivos (Seeds) e as diretrizes do que fazer via handoff para o subagente responsável, garantindo controle total sobre o tamanho e complexidade do Blast Radius do projeto.
