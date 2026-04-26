# Plano Completo: workflow_Journal + S.A.M. (Anti-Migué)

## Objetivo
Implementar um circuito inviolável de governança para impedir migué por comissão (marcar sem fazer) e por omissão (mudar arquivo sensível sem declarar no Journal), com validação por evidência real do Git e fechamento independente.

## 1) Contrato único de governança
- Definir fronteiras sem ambiguidade:
  - `JOURNAL.md`: promessa + narrativa de decisão.
  - `CONTEXT_PATCH.md`: evidência técnica estruturada de alteração de contexto.
- Regra de autoridade:
  - Executor abre `[ ]`.
  - Validador independente fecha `[x]`.
- Lei da Densidade:
  - `git diff` prevalece sobre narrativa textual.
- Definition of Done:
  - Regras explícitas em `RULES.md` e refletidas em `MASTER_FLOW.md`.

## 2) Matriz de Sinapses estável (SSOT)
- Consolidar `JOURNAL_SYNAPSE` em formato parseável (YAML no topo + tabela humana abaixo).
- Cada sinal deve declarar:
  - `required_files`
  - `evidence_rules`
  - `severity` (`critical` | `normal`)
- Definition of Done:
  - Matriz validável por script e com fallback mínimo embutido no harness.

## 3) Comando único `workflow_Journal`
- Criar comando operacional que execute o fluxo completo:
  1. Ler entrada ativa do Journal.
  2. Resolver sinapses obrigatórias.
  3. Cruzar com `git diff --name-only`.
  4. Verificar evidência mínima por arquivo obrigatório.
  5. Emitir `HARNESS-PASS` ou `HARNESS-FAIL` com causa determinística.
- Definition of Done:
  - Um único comando entrega diagnóstico completo e acionável.

## 4) Validação anti-migué em 3 camadas
- Camada A (formato): template obrigatório preenchido.
- Camada B (realidade): mudanças no Git batem com a promessa.
- Camada C (independência): bloqueio se `[x]` não vier do validador.
- Falhas esperadas (mensagem objetiva):
  - `schema.sql mudou sem trilha SQL no Journal`.
  - `TECHNICAL_REQUIREMENTS.md sem evidência da promessa`.
  - `executor tentou auto-fechar [x]`.
- Definition of Done:
  - As três classes de fraude são bloqueadas antes do commit.

## 5) Ergonomia (evitar bureaucracy stalling)
- `assist` (local): bloqueia apenas violações críticas; demais como warning.
- `strict` (CI/branch protegida): bloqueio total de violações de contrato.
- Mensagens curtas e acionáveis + modo `--fix-suggest` (sugestão textual, sem escrita automática).
- Definition of Done:
  - Fluxo local rápido e portão final rigoroso.

## 6) Rollout de baixo risco
- Semana 1: `shadow mode` (somente alertas, sem bloqueio).
- Semana 2: bloqueio apenas de severidade `critical`.
- Semana 3: `strict` completo no CI.
- Definition of Done:
  - Sem deadlock operacional e com adoção progressiva.

## 7) Critérios finais de aceite
- Não existe commit com mudança sensível sem trilha correspondente no Journal.
- Não existe `[x]` autoassinado pelo executor.
- Não existe `PASS` manual sem evidência verificável.
- O comando único sempre aponta pendência e causa raiz com precisão.
- `RULES.md`, `MASTER_FLOW.md` e harness convergem sem conflito.

## Resultado esperado
Circuito fechado ponta a ponta: promessa -> propagação -> auditoria -> selo.

Isso entrega alta integridade com atrito operacional controlado: fail-closed para segurança, fail-soft para experiência de uso.
