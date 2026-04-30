---
version: 2.6-DRAFT
status: PROPOSAL
topic: Sprints de Contratos (Fragmentação por Marcos)
date: 2026-04-30
---

# 🚀 Proposta: Sprints de Contratos (v2.6)

## 🎯 Objetivo
Resolver a dicotomia entre **Planos Grandes** (Estratégicos) e **Specs Atômicas** (TLC), permitindo que uma funcionalidade complexa seja executada em uma única pasta de feature, mas com segurança de "fail-closed" por fases (Milestones).

---

## 🏗️ Arquitetura do "Contrato Evolutivo"

### 1. Polimorfismo da Spec
A `spec.md` passa a suportar um modo hierárquico. Se a feature é simples, o fluxo v2.5.2 permanece. Se complexa, ativa-se o modo `sprints`.

**Exemplo de Frontmatter Evolutivo:**
```yaml
contract_mode: sprint_based  # [standard | sprint_based]
current_sprint: 1
sprints:
  sprint_01:
    goal: "Fundação e Estruturas Base"
    qa_signoff: true
    signed_by: "@qa-validator"
  sprint_02:
    goal: "Lógica de Negócio e Integração"
    qa_signoff: false  # BLOQUEADO
```

### 2. Tasks por Marcos
O arquivo `tasks.md` deixa de ser uma lista plana e passa a ser agrupado por sprints.
- O Agente Executor foca apenas na Sprint `ACTIVE`.
- O Harness bloqueia qualquer tentativa de iniciar tarefas da Sprint `LOCKED`.

### 3. O Papel do STATE.md (Handoff de Milestone)
O `STATE.md` registra o rito de passagem:
- A IA termina a Sprint 1.
- O `@qa-validator` audita os arquivos daquela fase específica.
- O `@qa-validator` assina o checkpoint na `spec.md`.

---

## 🔍 Estudo de Amarrações e Implicações

### 🛡️ Automação (Harness Runner)
*   **Seletividade de Contrato:** O `harness_runner.py` deve deixar de ser binário. Ele precisa validar apenas o `qa_signoff` da **Sprint Atual**. Avançar sem a assinatura da sprint anterior causa `Exit 1`.
*   **Âncora de Impacto (Git Diff):** Para evitar falsos positivos de *Scope Blowout*, cada sprint deve registrar seu `start_commit_hash` no `STATE.md`. O cálculo de impacto será feito apenas entre o hash inicial da sprint e o estado atual.

### 📜 Governança e Regras
*   **Isolamento de Contexto:** Nova regra obrigando a IA a carregar apenas os arquivos da Sprint Ativa. Isso combate o *Context Bloat* e alucinações em specs longas.
*   **Frequência de Handoff:** O rito do `@qa-validator` torna-se mais frequente e atômico. A validação é feita em "micro-entregas", garantindo que erros não se propaguem para a sprint seguinte.

### 🧠 Memória Viva (STATE.md)
*   **Segmentação de Histórico:** O `STATE.md` exige cabeçalhos de Sprint. Isso permite que o `purge_journal.py` identifique o que é ruído técnico de uma fase concluída e o que deve ser preservado.

---

## ⚖️ Veredito Técnico

- **Prós:** Transforma o Agente em um maratonista (corre km a km) em vez de um velocista que cansa no meio do caminho. Elimina a necessidade de criar dezenas de pastas para um mesmo projeto grande.
- **Contras:** Exige uma refatoração no parser de YAML e na lógica de Git Diff do framework.

---
*Atualizado em: 2026-04-30 14:13*
