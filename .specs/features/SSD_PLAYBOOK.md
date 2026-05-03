# 📜 SSD-Chain Playbook (Spec-Driven Discipline Chain) - V3.0
> Manual definitivo para execução de features com Governança Blindada e Anti-Loop.

## 🎯 Objetivo
Eliminar a afobação do executor e garantir que toda mudança de código seja precedida por carregamento de contexto e validação de restrições.

## ⛓️ O Ciclo das 9 Skills (Obrigatório)
Toda feature deve progredir através destas skills no `STATE.md`:

### Fase A: Preparação (Skills 1-3)
1.  **CONTEXT_LOADED**: Ler as regras mestras (`RULES.md`) e a Spec.
2.  **CONSTRAINTS_EXTRACTED**: Identificar o que NÃO pode ser feito (escopo negativo).
3.  **TECHNICAL_APPROACH**: Definir o plano de implementação ANTES de tocar no código.

### Fase B: Blindagem (Skills 4-5)
4.  **SCRATCHPAD_SYNCED**: Inicializar o `AGENT_SCRATCHPAD.md` com a estratégia atual.
5.  **SCOPE_LOCKED**: Trancar a `allow_list` na Spec da sprint.

### Fase C: Execução (Skills 6-7)
6.  **EVIDENCE_GENERATION**: Escrita física de código via `write_with_validation.py`.
7.  **SELF_AUDIT**: O próprio executor roda o Harness para validar sua entrega.

### Fase D: Fechamento (Skills 8-9)
8.  **REMEDIATION**: Sincronizar o `JOURNAL.md` e limpar rastros de "Modificação Silenciosa".
9.  **HANDOFF**: Gerar o relatório final para o QA-Validator.

---

## 🛡️ Protocolo Anti-Loop (Metacognição)
Sempre que o Gatekeeper ou o Harness retornar um erro `[BLOCKED]` ou `[FATAL]`:
1.  **Não repita a ação.**
2.  Documente no **Scratchpad**:
    - **Erro exato**: O que o console disse.
    - **Hipótese**: Por que o sistema barrou?
    - **Correção**: Qual o ajuste na Spec ou no código?

## 🚫 Regras Proibidas (Zero-Trust)
- Proibido editar arquivos de regras (`RULES.md`, `MASTER_FLOW.md`) sem autorização de intervenção nível 3.
- Proibido marcar tarefas como concluídas `[x]` ANTES de validar a escrita física.
- Proibido ignorar erros do Harness (SAM). O pre-commit VAI barrar.

---

## 📅 Rito de Selagem
Uma feature só é considerada "CLOSED" quando o `JOURNAL.md` reflete o Git e o `STATE.md` exibe as 9 Skills com status `[x]`.

🚀 **Siga a Cadeia. Confie no Gatekeeper.**
