# 🧠 Brainstorm: Simplificação da Governança (Modo Light)
> **Data/Hora**: 2026-05-30 19:43 - 20:10 (Horário de Brasília)
> **Participantes**: Usuário (Arquiteto) & Antigravity AI

---

## 🎯 Objetivo
Registrar a análise arquitetural do ecossistema de governança atual do **Antigravity Kit (H.O.K. Nível 3)** e documentar insights estratégicos para criar um sistema de regras mais flexível (menos engessado) para o futuro.

---

## 🏗️ 1. Mapeamento dos Compartimentos Atuais

O ecossistema opera sob três camadas que controlam e validam o comportamento do desenvolvedor (agente de IA ou humano):

```
                                  [ .context/ ]
                          (Camada Estratégica Mestre)
                                        │
                                        ▼
                                 [ .specs/features/ ]
                             (Fase de Execução - SDD)
                                        │
                                        ▼
                                 [ Git Commit Hook ]
                             (Fase de Validação - SAM)
```

### A. SDD (Spec-Driven Discipline / TLC)
*   **Finalidade**: Organizar o escopo da feature sob a pasta `.specs/features/` antes do início da codificação.
*   **Ficheiros-chave**: `spec.md` (definição e limites), `tasks.md` (lista de afazeres atômicos) e `STATE.md` (rastreador das 9 Skills).
*   **Ponto de Fricção**: Bloqueio mecânico de escrita fora dos arquivos declarados na `allow_list` e limite rígido do `max_impact_radius`.

### B. Journal & Oráculo (Memória Curta)
*   **Finalidade**: Mitigar a saturação de contexto do LLM.
*   **Ficheiros-chave**: `JOURNAL.md` (registro cronológico reverso das alterações) e o script `purge_journal.py` (corta o excesso do diário mantendo apenas os 30% mais recentes na memória de curto prazo).
*   **Ponto de Fricção**: Exigência de preenchimento manual rigoroso a cada entrega.

### C. SAM (Sistema Anti-Migué / Git Hooks)
*   **Finalidade**: O auditor final. Roda no Husky (`pre-commit`) para comparar a promessa declarada com as modificações reais do Git.
*   **Mecânicas**:
    *   **Fraude Narrativa**: Bloqueia se o diário alega mudança num arquivo que o Git não viu.
    *   **Modificação Silenciosa**: Bloqueia se um arquivo governado foi alterado no Git, mas está ausente da Matriz de Propagação do Journal.
    *   **Exceções**: `SHADOW_FILES` (arquivos gerados pelo pipeline) e caminhos em zonas de imunidade (como `planos/` e `scratch/`).
*   **Ponto de Fricção**: É o principal causador de bloqueios no terminal local. Qualquer arquivo órfão trava o commit.

### D. Harness (Validação de Contrato)
*   **Finalidade**: Verificar integridade estrutural (tabelas no `schema.sql` vs spec) e conformidade de Handoffs.
*   **Ponto de Fricção**: Exige preenchimento exaustivo de metadados e assinaturas estritas.

### E. Karpathy Layer (Linter Epistemológico)
*   **Finalidade**: Exigir citação de fontes (`> Fonte: RAW/...`) para claims técnicos.
*   **Ponto de Fricção**: Aplica restrições semânticas que necessitam de bypasses frequentes (ex: injeção de marcadores `SSOT` para pular a verificação).

---

## 📅 2. Ata de Decisão (Aprofundamento Técnico)
> **Data/Hora**: 2026-05-30 20:36 - 21:06 (Horário de Brasília)

Abaixo estão registradas as decisões e as diretrizes arquiteturais acordadas e assinadas pelo Arquiteto:

### Item 1: Vies Exploratório Controlado para o `spec-driver`
*   **Decisão**: O engessamento atual afeta principalmente o `spec-driver` (executor). Para flexibilizar sem permitir que o agente alucine ou leia arquivos arbitrários, adotaremos uma **regrar de solicitação de escopo**.
*   **Mecânica**: Se o `spec-driver` sentir necessidade de ler ou escrever em um arquivo fora da `allow_list` da Spec:
    1. Ele registra o pedido de expansão na seção `INBOX` do `AGENT_SCRATCHPAD.md`, justificando a necessidade técnica.
    2. Ele pausa a execução e aguarda a autorização.
    3. O `sdd-orchestrator` (que não deve ser vítima de bloqueio de escopo) avalia a solicitação, atualiza a Spec se for válida e acorda o `spec-driver`.
*   **Status**: Aprovado para especificação futura.

### Item 2: Automação Reativa do Journal ("Faxina Automática")
*   **Decisão**: Aprovada a automação. Criaremos uma **Skill de Contexto/Operação** acoplada ao `sdd-orchestrator` ou um subagente/rotina dedicada à faxina cognitiva.
*   **Mecânica**: Ao término do desenvolvimento (Skill 9/Handoff) ou imediatamente antes do commit, essa rotina inspeciona o `git diff` e o progresso da Spec para:
    1. Preencher automaticamente a Matriz de Propagação do `JOURNAL.md`.
    2. Identificar e marcar o que propagar.
    3. Sanitizar arquivos residuais, deixando o ambiente perfeitamente limpo para desenvolvedores que preferem focar apenas no código de negócio e deixar a documentação para o pós-processamento.
*   **Status**: Aprovado e priorizado.

### Item 3: Tolerância SAM em Branches Secundárias
*   **Decisão**: O SAM operará em modo `WARNING` em branches de feature (`feature/*`, `bugfix/*`), mas permanecerá em modo `STRICT` (bloqueio rígido / Exit 1) em branches estáveis como `main` ou `develop`/`production`.
*   **Ponto Cego Identificado & Mitigado**:
    *   *Risco*: Acúmulo excessivo de dívida de governança durante o desenvolvimento, resultando em dezenas de bloqueios acumulados que explodem no momento do Pull Request para a branch estável.
    *   *Mitigação*: O modo `WARNING` deve imprimir um relatório visual explícito no terminal a cada commit local contendo o sumário das violações acumuladas (ex: "Débito SAM detectado em 5 arquivos. Resolva-o antes do PR"), incentivando a auto-remediação contínua e impedindo surpresas no CI/CD.
*   **Status**: Aprovado com mitigação de ponto cego.

### Item 4: Validação Harness Dinâmica baseada em Testes
*   **Decisão**: Avaliar o uso de testes de integração automatizados e mocks em substituição ou complemento à análise estática de strings da spec/schema.
*   **Status**: Em avaliação (estudo de impacto sobre a latência local e complexidade de dependências).

### Item 5: Karpathy Layer / Oráculo / Second Brain
*   **Decisão**: Manter este compartimento em **stand-by/adormecido** até encontrarmos uma utilidade prática real que justifique um Second Brain robusto e um Oráculo performático.
*   **Insight Brilhante (Bypass de Manutenção)**:
    *   Para evitar a alimentação manual da Wiki pelo humano, o Oráculo pode ser alimentado de forma 100% automatizada a partir do arquivamento das specs (`CLOSURE.md` e `LEARNINGS.md`), transformando cada feature concluída em conhecimento contextual de forma transparente.
*   **Status**: Adormecido (Stand-by).

### Item 6: Avaliação de Novos Mecanismos de Harness
*   **Harness de Variáveis de Ambiente (Env Drift Gate)**:
    *   *Decisão*: **Aprovado**. Será implementado um scanner simples para mapear leituras de variáveis de ambiente (`process.env.*`) e garantir que estejam documentadas no `.env.example` e nos requisitos de segurança.
*   **Harness de Complexidade Cognitiva Máxima (Complexity Gate)**:
    *   *Decisão*: **Aprovado como apenas consultivo (WARNING)**. Para evitar deadlocks de engessamento cruzado (onde a IA é forçada a dividir o arquivo, mas é barrada pelo bloqueio físico de novos arquivos do SDD), o gate apenas gerará avisos educativos sem impedir o commit.
*   **Harness de Exaustão de Loop (Loop Exhaustion)**:
    *   *Decisão*: **Aprovado (Automático)**. Monitorará o estado do pipeline local via log efêmero (ex: arquivo JSON em `scratch/` ou `temp/`) incrementando falhas consecutivas e disparando travamento/escalation automático caso atinja 5 falhas no mesmo teste.
*   **Harness de Cobertura Semântica (Semantic Coverage)**:
    *   *Decisão*: **Aprovado no Modo Assist (checklist sem bloqueio físico)**. Não exigirá testes estritos ou percentuais. Apenas checará se novas funções públicas possuem referências correspondentes no arquivo de testes, emitindo avisos educacionais.

---

## 🚀 3. Próximos Passos (Workflow Simplificado)
*   **Meta**: Assegurar que:
    1. Commits locais rápidos funcionem sem bloqueios desnecessários.
    2. O diário seja atualizado de forma retroativa ou reativa.
    3. O SAM atue como monitor/educador no dia a dia e como gatekeeper físico apenas no servidor de build.
