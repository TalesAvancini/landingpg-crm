# SDD Playbook (Spec-Driven Discipline)

## Objetivo
Este manual define o procedimento padrao para execucao de features `sprint_based` com governanca fail-closed.

## Escopo
Aplica-se a todas as features em `.specs/features/*` que usam `contract_mode: sprint_based`.

## Rito 0: Bootstrap Obrigatorio
1. Criar pasta da feature em `.specs/features/[feature_id]/`.
2. Criar arquivos: `spec.md`, `tasks.md`, `STATE.md`, `design.md`.
3. Garantir que `spec.md` esteja em modo sprint:
   - `contract_mode: sprint_based`
   - `current_sprint: sprint_01`
   - `policy_profile`
   - bloco `sprints:` com `sprint_01` definido
4. Proibido misturar `type: standard` com `contract_mode: sprint_based`.

## Rito 1: Start Hash e Baseline
1. Confirmar `git status --short` sem saida.
2. Capturar `start_hash` (HEAD atual) no `STATE.md`.
3. Registrar `captured_at` e `captured_by`.
4. Registrar baseline no `JOURNAL.md` com:
   - feature
   - start_hash
   - status inicial

## Rito 2: Escopo da Sprint
1. Definir `scope_allow` da sprint atual no `spec.md`.
2. Definir `scope_deny` quando necessario.
3. `tasks.md` deve refletir apenas tarefas da sprint ativa e proximas sprints planejadas.
4. Qualquer expansao de escopo exige justificativa + registro formal no `STATE.md`.

## Rito 3: Execucao
1. Implementar apenas dentro do `scope_allow`.
2. Atualizar `tasks.md` em tempo real.
3. Atualizar `STATE.md` com fatos e checkpoints.
4. Evitar edicoes destrutivas em SSOT (`STATE.md`, `spec.md`, `tasks.md`).

## Rito 4: Pre-close Self-Audit (Executor)
Antes de pedir QA:
1. `git status --short` limpo.
2. Coerencia entre `spec.md`, `tasks.md`, `STATE.md`.
3. Sprint atual com criterios de aceite objetivos.
4. Evidencia em `JOURNAL.md` e/ou `HARNESS_LOG.md`.
5. Rodar validacao aplicavel (`context:validate` ou equivalente).

## Rito 5: QA Signoff
1. `qa-validator` verifica requisitos da sprint atual.
2. Se aprovado:
   - `qa_signoff: true` no bloco da sprint
   - evidencias no `STATE.md`
3. Se reprovado:
   - registrar motivo objetivo
   - manter sprint em `IN_PROGRESS` ou `BLOCKED`

## Rito 6: Fechamento de Onda
Somente permitido se:
1. Harness PASS
2. Coerencia `spec/tasks/state`
3. Arvore Git limpa
4. Evidencias registradas
5. `qa_signoff` da sprint atual = true

Se qualquer item falhar: status obrigatorio `IN_PROGRESS`.

## Erros Recorrentes (Nao Repetir)
1. Declarar concluido com `git status` sujo.
2. Capturar `start_hash` e depois mudar baseline sem recaptura.
3. Misturar contrato `standard` com `sprint_based`.
4. Atualizar `STATE.md` com regex agressivo e perder campos obrigatorios.
5. Narrativa dizer "concluido" sem `qa_signoff` real.

## Regra de Ouro
Contrato escrito vence memoria de chat. Sempre decidir pelo SSOT.
