# 🧠 Córtex de Execução: TLC Spec-Driven + H.O.K Forge v2.5.2 (Enriquecido)

**Data:** 2026-04-30
**Objetivo:** Protocolo definitivo de execução técnica. Transição do planejamento narrativo (PRDzinho) para a implementação mecânica atômica.

---

## 1. O que é o TLC Spec-Driven? (A Filosofia)

O TLC Spec-Driven é um motor de desenvolvimento determinístico baseado em quatro fases adaptativas. A profundidade é ditada pelo **Auto-Sizing** (Complexidade do problema).

### 🔄 O Ciclo de Vida Adaptativo
1.  **SPECIFY (Obrigatório):** Define **O QUE** será feito. Transforma o PRDzinho do Plano Mestre em requisitos técnicos com IDs rastreáveis.
2.  **DESIGN (Opcional):** Define **COMO** será feito. Se for óbvio (CRUD, Markdown, Config), pula-se.
3.  **TASKS (Obrigatório):** Define a **ESTRATÉGIA DE ATAQUE**. Uma lista de tarefas atômicas com **Critério de Verificação**.
4.  **EXECUTE (Obrigatório):** A codificação real via **Subagente Executor**.

### ⚖️ O Princípio do Auto-Sizing (Ajuste de Carga)
*   **Small (≤3 arquivos):** Quick Mode (Implementa + Verifica direto).
*   **Medium (Feature clara, <10 tasks):** Spec (breve) + Tasks -> Execução.
*   **Large (Multi-componente):** Full Spec + Design + Tasks -> Execução.

---

## 2. A Estrutura do "Ovo" (Feature SSOT)

Para evitar a "subscrição" desnecessária de arquivos e manter a integridade da feature, usamos o modelo **Single Spec / Multi-Sprint**. Toda feature reside em `.specs/features/[feature_nome]/`.

### 📄 `spec.md` (O Contrato Único)
Contém todos os requisitos técnicos da feature completa.
*   **IDs de Requisitos:** Essenciais para o Husky e o Aggregator (ex: `[LRN-01]`).
*   **Impact Control:** Bloco YAML definindo `max_impact_radius` para o Harness.

### 📄 `tasks.md` (O Motor das Sprints)
A lista de passos técnicos dividida por **Milestones de Sprint**.
*   **Sprint 1:** [X] Task 1 | Verify: [Command]
*   **Sprint 2:** [ ] Task 5 | Verify: [Command]
*   **Vantagem:** Mantém o histórico de progresso sem fragmentar o plano técnico em múltiplos arquivos de Spec.

### 📄 `STATE.md` (A Telemetria)
Repositório de estado do subagente (Bloqueios, `SCOPE_BLOWOUT`, `IN_PROGRESS`, `AWAITING_QA`).

---

## 3. Ecossistema de Skills e Coreografia

O TLC Spec-Driven não atua sozinho; ele orquestra outras skills durante o ciclo:

*   🎨 **mermaid-studio:** Invocado durante a fase de **Design** para gerar diagramas de fluxo ou arquitetura.
*   🔍 **codenavi / grep_search:** Invocado no **Pre-flight Gate** para validar o `impact_radius` antes de qualquer escrita.
*   ⚡ **flash-harness:** Invocado no início da fase de **Execute** para gerar o **Diário de Bordo (Thought Log)** e garantir o compliance de governança.

---

## 4. O Papel do Executor (@spec-driver)

O Executor é um subagente mecânico (Zero Trust) que opera sob as regras do Córtex:

1.  **Leitura do Contrato:** Lê o `spec.md` e o `tasks.md`.
2.  **Pre-flight Gate:** Checa se o raio de impacto físico condiz com o planejado. Se exceder, gera `SCOPE_BLOWOUT`.
3.  **Execução Atômica:** Realiza uma task por vez, valida tecnicamente, e atualiza o `STATE.md`.
4.  **Handoff:** Solicita o `@qa-validator` apenas quando a Milestone da Sprint está pronta.

---

> [!IMPORTANT]
> **O Plano Mestre é a Base (PRDzinho).** O TLC é a **Lança**. 
> O Agente deve sempre converter o plano em uma Spec TLC antes de iniciar qualquer ciclo de execução, garantindo que as Sprints sejam visíveis e rastreáveis no `tasks.md`.
