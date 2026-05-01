---
Criado em: 2026-04-30 23:30
Ultima Atualizacao: 2026-04-30 23:30
Status: Ativo
---

# 📡 RX-COMMUNICATIONS: Protocolos de Transparência Narrativa

Este documento define os ritos de comunicação externa e interna para garantir que a execução autônoma seja auditável, transparente e livre de "caixas pretas".

---

## 🗣️ 1. Comunicação Agente-Humano (Interface)

### 1.1 Rito de Transparência Total
- O Agente deve reportar falhas de governança (SAM) de forma imediata e honesta, sem tentar "esconder" erros técnicos sob narrativas de sucesso.
- **Protocolo de Erro:** Se o Husky ou o validador bloquear um commit, o Agente deve explicar o motivo técnico exato (ex: hash inválido, desync de tarefas).

### 1.2 Uso de Emojis de Status
- `🛡️` : Rito de Governança/Início.
- `✅` : Conclusão técnica com evidência.
- `🚧` : Em progresso (bloqueios ou desafios).
- `❌` : Violação de regra ou erro fatal.
- `🟢` : Pronto para auditoria/signoff.

---

## 🧠 2. Comunicação Inter-Agente (Nervos)

### 2.1 Handoff Atômico
- Toda transição entre `@spec-driver` e `@qa-validator` deve ser registrada no `JOURNAL.md` com o ID do contexto.
- O `@spec-driver` não pode apenas "parar"; ele deve convocar explicitamente o auditor.

### 2.2 Sincronia de Contrato
- O `spec.md` é a única fonte de verdade para a aceitação de uma feature. 
- Se um agente detecta que o contrato está defasado vs `tasks.md`, ele deve interromper a execução e realizar a **Sincronização de Contrato** antes de prosseguir.

---

## 🛡️ 3. Ritos de Conflito (Escalonamento)

### 3.1 Detecção de Drift
- Se o SAM detectar uma **Fraude Narrativa**, o agente executor deve realizar um rito de **"Autocrítica Técnica"** no Journal, corrigindo a narrativa antes de tentar um novo commit.

### 3.2 Bloqueio de Pipeline
- Em caso de bloqueio por `GF-ATOMIC-DESYNC`, é proibido "chutar" hashes. O agente deve executar `git log` para recuperar a âncora física real.

---

## 📈 4. Telemetria de Fricção
- Toda fricção registrada no `HARNESS_LOG.md` deve ser sumarizada no rito de fechamento da Sprint para visibilidade do Usuário.
