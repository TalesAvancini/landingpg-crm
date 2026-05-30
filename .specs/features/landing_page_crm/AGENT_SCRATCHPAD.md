# 🧠 AGENT_SCRATCHPAD
Feature: landing_page_crm
Sprint: sprint_01

## 💡 Known Traps (Leia Antes de Bater a Cabeça!)

Se você recebeu um erro e parou aqui, verifique se a solução já está abaixo:

### 1. [FATAL] Modificação Silenciosa (Harness / SAM)
- **Causa:** Você alterou/criou um arquivo, mas o `JOURNAL.md` não registra essa alteração na "Matriz de Propagação".
- **Solução:** Abra o `JOURNAL.md`, adicione o arquivo modificado na entrada da Sprint atual e re-execute o Harness.

### 2. [HG01] Violação de Escopo Sprint
- **Causa:** O arquivo (ex: `.context/maintenance/HARNESS_LOG.md`) não está na `allow_list` da sprint no `spec.md`.
- **Solução:** Edite o `spec.md` da feature e adicione o arquivo explicitamente na lista `scope_allow` da sprint ativa.

### 3. [BLOCKED] Task 'X' já está concluída
- **Causa:** Você marcou a task como concluída no `tasks.md` ANTES de tentar escrever ou validar.
- **Solução:** A marcação `[x]` deve ser o ÚLTIMO passo após a escrita e validação bem-sucedidas. Desmarque a task, faça o trabalho e marque novamente.

### 4. 💉 Injeção de Contexto (MiMo)
- **Causa:** Falhas contínuas e "Agent Amnesia".
- **Solução:** O arquivo `*.enriched.md` contém a lista de *Scars* (Cicatrizes) do sistema. O MiMo injetou as regras que você DEVE seguir para não morrer nas armadilhas de ciclos passados. Consulte o topo da Spec!

### 5. [BLOCKED] Falta de Justificativa de Tier
- **Causa:** Você tentou uma escrita de Tier 2 (16-50 linhas) ou Tier 3 (50+) sem registrar o campo `tier_justification:` no `STATE.md`.
- **Solução:** Vá ao `STATE.md`, localize a `TASK ID` correspondente no `CHAIN_EXECUTION_LOG` e adicione a justificativa. Re-valide a escrita.

### 6. [FAIL] Substituição Vazia (Empty Diff)
- **Causa:** Você tentou alterar um arquivo via "Search/Replace", mas o texto alvo não corresponde à realidade do arquivo. Ocorreu Drift de Memória.
- **Solução:** NUNCA tente editar um arquivo baseando-se apenas na memória. OBRIGATÓRIO rodar `view_file` ou `grep` nas linhas que deseja alterar para capturar a literalidade exata antes de chamar a ferramenta de escrita.

---

## 📥 INBOX (Escalation & Dúvidas)
> **Uso Exclusivo do Subagente.** Se você travou ou não sabe como seguir, preencha o card abaixo e pare. Lance o gatilho `[HANDOFF: ESCALATION]` no terminal.

### 🛑 [Task ID] - [Timestamp]
- **Ação Desejada:** [O que você queria fazer?]
- **Ação Executada:** [O que você tentou na prática?]
- **Bloqueio (Fato):** [Qual foi o erro exato do Gatekeeper/Harness?]
- **Hipótese:** [Por que você acha que falhou?]

---

## 📤 DIRECTIVES (Resoluções do Orquestrador)
> **Uso Exclusivo do Orquestrador.** Injetar soluções aqui para destravar o subagente.

- **2026-05-29 23:30 | Solução para Handoff Inicial:** 
  - **Diretriz:** Buscar as skills em `C:\Users\compartilhadoAntigravity\AntigravityKit\ag-kit-main\.agent`.
