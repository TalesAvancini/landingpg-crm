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

---

## 📝 Thought Log (Anti-Loop Memory)

Use esta seção para registrar falhas que NÃO estão nos Known Traps acima:

### 🛑 [Task ID] - [Timestamp]
- **Erro:** [Descreva o erro exato]
- **Hipótese:** [Por que falhou?]
- **Novo Plano:** [O que vai tentar de diferente?]
