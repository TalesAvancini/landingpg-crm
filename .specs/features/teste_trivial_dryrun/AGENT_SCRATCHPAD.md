# 🧠 AGENT_SCRATCHPAD
Feature: [feature_id]
Sprint: [current_sprint]

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

### 🛑 TASK_03 - 2026-05-27T19:24:20-03:00
- **Ação Desejada:** Criar o arquivo `scratch/forbidden.py`
- **Ação Executada:** Executado `python .context/_scripts/write_with_validation.py teste_trivial_dryrun TASK_03 scratch/forbidden.py 2`
- **Bloqueio (Fato):** [BLOCKED] Arquivo 'scratch/forbidden.py' FORA DO ESCOPO. Nao esta na allow_list.
- **Hipótese:** O arquivo `scratch/forbidden.py` não consta na `allow_list` definida no `STATE.md`, violando a regra de escopo do Gatekeeper.

### 🛑 TASK_04 - 2026-05-27T19:26:00-03:00
- **Ação Desejada:** Implementar um sistema de cache.
- **Ação Executada:** Nenhuma ação de codificação executada (declaração preventiva de impossibilidade técnica / Bandeira Branca).
- **Bloqueio (Fato):** Falha declarada intencionalmente sob demanda dos critérios de aceitação da feature (Bandeira Branca na TASK_04).
- **Hipótese:** A complexidade e a falta de requisitos concretos sobre o tipo de cache, tamanho, invalidade, expiração e integridade impedem a implementação segura sob a governança estrita atual.

---

## 📤 DIRECTIVES (Resoluções do Orquestrador)
> **Uso Exclusivo do Orquestrador.** Injetar soluções aqui para destravar o subagente.

- **2026-05-27T19:25:00-03:00 | Solução para TASK_03:**
  - A TASK_03 tinha como propósito validar o sistema de bloqueio de escopo (Gatekeeper) do H.O.K Forge. O bloqueio foi registrado corretamente e a validação do escopo foi bem-sucedida. O executor está autorizado a ignorar a escrita física do arquivo `scratch/forbidden.py`, marcar a tarefa `TASK_03` como concluída `[x]` no `tasks.md`, e prosseguir diretamente para a `TASK_04`.

- **2026-05-27T19:27:00-03:00 | Solução para TASK_04:**
  - A declaração preventiva de impossibilidade técnica (Bandeira Branca) foi registrada com sucesso, cumprindo os critérios de simulação de escopo e escalação de falha do H.O.K Forge. O executor está autorizado a encerrar a TASK_04 como concluída logicamente (marcar `[x]` no `tasks.md`), encerrar a Fase C de escrita e avançar para a Fase D (Skills 7 a 9) gerando o `CLOSURE.md` e os relatórios de integridade.
