---
status: ATIVO
definition_of_done: O script 'harness_runner.py' deve travar o commit (Exit 1) se não localizar um spec.md ativo.
qa_signoff: true
signed_by: "@qa-validator"
---

# Spec: Reparo de Vulnerabilidade do Linter (Fail-Closed)

Esta spec é exigida pela nova física do repositório. Para conseguir submeter a própria alteração que tranca o repositório, o agente é obrigado a instanciar uma spec atômica que cumpra os mesmos critérios.

## Tarefas:
- [x] Mudar 'return True' para 'return False' em spec_path.exists().
- [x] Validar que o commit prossegue apenas devido à existência deste documento assinado.
