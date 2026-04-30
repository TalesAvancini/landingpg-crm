---
contract_version: 2.5.2
parties: ["@antigravity-agent", "@qa-validator"]
type: standard
executor_context_id: "CTX_IMPL_QA_SUBAGENT"
validator_context_id: "CTX_QA_VALIDATOR"
definition_of_done:
  - [x] Criar diretório `.agent/subagents`
  - [x] Criar arquivo `qa-validator.md` com as instruções corretas
  - [x] Incluir metadata recomendada pelo skill subagent-creator
qa_signoff: true
signed_by: "@qa-validator"
---

# 📄 Spec: QA Subagent (Orquestração Autônoma)

## 🎯 Objetivo
Eliminar o humano como gargalo na validação de código, consolidando o "Zero Trust". Instanciar um Subagente especializado que atue como Validador de QA, assumindo a persona de auditor do SAM para validar tarefas sem precisar que o usuário assine manualmente o `spec.md`.

## 🛠️ Solução (Caminho B)
Baseado no Padrão de Subagents, a pasta `.agent/subagents/` receberá o modelo `qa-validator.md`.
A descrição do subagente foi forjada com gatilhos cognitivos ("Automatically delegate...", "Use proactively...") para que a IA orquestradora (eu, no chat) sempre delegue para ele a responsabilidade de auditar a spec e o código e liberar o commit de forma isolada.
