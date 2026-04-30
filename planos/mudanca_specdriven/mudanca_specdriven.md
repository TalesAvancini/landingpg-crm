---
version: DRAFT
status: PROPOSAL
topic: Spec-Driven Contract Sprints
date: 2026-04-30
owners:
  - framework-core
  - qa-validator
  - harness-runner
---

# Proposta Operacional: Spec-Driven Contract Sprints

## 1) Intenção e Resultado Esperado

Este plano consolida um modelo de execução **fail-closed** para features complexas, mantendo a ergonomia do framework atual e adicionando progressão por sprints contratuais.

Resultado esperado:
- reduzir deriva de IA em execuções longas;
- aumentar auditabilidade por micro-entregas;
- impedir avanço para fases futuras sem validação objetiva da fase atual;
- permitir evolução grande com baixo risco de scope blowout.

---

## 2) Escopo do que muda (e do que não muda)

### 2.1 Muda
- `spec.md` passa a suportar **modo sprint-based** com checkpoint por fase.
- `tasks.md` passa a ser agrupado por sprint com status de bloqueio/liberação.
- `STATE.md` passa a registrar telemetria obrigatória por sprint (`start_hash`, impacto, exceções, assinaturas).
- `harness_runner.py` passa a aplicar **gates hard/soft configuráveis**.
- fluxo de validação do `@qa-validator` passa a assinar por sprint, e não apenas no fim da feature.

### 2.2 Não muda
- estrutura principal de feature em `.specs/features/[feature]/` permanece.
- princípio de spec como contrato permanece.
- `design.md` continua como desenho técnico da feature.
- lógica de journalização e arquivamento continua (com refinamentos de segmentação).

---

## 3) Estrutura alvo de uma feature

```text
.specs/
  features/
    [nome-da-feature]/
      spec.md
      design.md
      tasks.md
      STATE.md
      JOURNAL.md
```

Observação: `JOURNAL.md` pode ser criado no fechamento da feature se ainda não existir.

---

## 4) Contrato de dados por arquivo

## `spec.md` (contrato executável)
Frontmatter mínimo sugerido:

```yaml
contract_mode: sprint_based   # standard | sprint_based
feature_status: in_progress   # in_progress | blocked | done
current_sprint: sprint_01
policy_profile: hybrid        # strict | advisory | hybrid

sprints:
  sprint_01:
    goal: "Fundação"
    scope_allow:
      - "src/core/**"
      - "src/shared/types/**"
    scope_deny:
      - "src/billing/**"
      - "infra/prod/**"
    acceptance:
      - "test:unit-core-pass"
      - "lint-pass"
    qa_signoff: true
    signed_by: "@qa-validator"
    signed_at: "2026-04-30T15:20:00-03:00"

  sprint_02:
    goal: "Integração"
    scope_allow:
      - "src/integration/**"
    scope_deny:
      - "infra/prod/**"
    acceptance:
      - "integration-tests-pass"
    qa_signoff: false
```

Regras:
- apenas 1 sprint ativa por vez (`current_sprint`).
- sprint seguinte só desbloqueia com `qa_signoff: true` da sprint atual.
- `scope_allow` e `scope_deny` são mandatórios em sprint-based.

## `tasks.md` (execução atômica)
Formato por sprint:
- sessão por sprint;
- tasks pequenas (ideal 15-90 min);
- cada task inclui `Verify` objetivo.

Exemplo:

```md
## sprint_01
- [ ] T1: Criar tipos base
  - Verify: `npm run test -- core-types`
- [ ] T2: Implementar parser inicial
  - Verify: `npm run lint && npm run test -- parser`

## sprint_02 (LOCKED)
- [ ] T3: Integrar parser no pipeline
  - Verify: `npm run test -- integration`
```

## `STATE.md` (telemetria e memória operacional)
Campos mínimos por sprint:
- `sprint_id`
- `start_hash`
- `status` (`IN_PROGRESS`, `BLOCKED`, `PASSED`, `FAILED`)
- `impact_snapshot` (arquivos, churn, impacto ponderado)
- `exceptions` (se houver)
- `qa_checkpoint` (assinatura, timestamp, evidência)

Exemplo de bloco:

```md
## sprint_01
start_hash: a1b2c3d
status: IN_PROGRESS
impact_snapshot:
  files_changed: 3
  churn: +120/-40
  impact_score: 18
exceptions: none
qa_checkpoint: pending
```

## `design.md` (desenho técnico por fase)
Obrigatório incluir:
- decisão técnica principal;
- trade-offs;
- alternativa rejeitada;
- implicação de compatibilidade.

---

## 5) Policy Matrix (gates configuráveis)

## 5.1 Gate types
- **hard gates**: bloqueiam progresso/commit.
- **soft gates**: alertam; em `hybrid`, exigem justificativa para continuar.

## 5.2 Regras padrão
Hard:
- `scope_violation` (arquivo fora de `scope_allow` ou dentro de `scope_deny`)
- `security_block` (tocou área sensível sem permissão)
- `contract_break` (aceite objetivo da sprint não cumprido)
- `sprint_order_break` (tentou avançar sem signoff)

Soft:
- `high_churn`
- `impact_growth`
- `architecture_warning`

## 5.3 Modos
- `strict`: hard bloqueia; soft também bloqueia.
- `advisory`: hard bloqueia; soft só alerta.
- `hybrid` (recomendado): hard bloqueia; soft exige justificativa registrada.

## 5.4 Thresholds por sprint
Exemplo:

```yaml
thresholds:
  max_files_changed: 5
  max_churn_lines: 350
  max_impact_score: 25
```

## 5.5 Override controlado
Campos obrigatórios:
- regra sobreposta;
- motivo técnico;
- aprovador;
- expiração;
- plano de rollback.

Registro em `STATE.md` obrigatório.

---

## 6) Algoritmo do Harness Runner

Pipeline por execução:
1. carregar `spec.md` e detectar `contract_mode`;
2. se `standard`, manter fluxo atual (compatibilidade retroativa);
3. se `sprint_based`:
   - ler `current_sprint`;
   - carregar escopo e aceite da sprint;
   - calcular diff entre `start_hash` e `HEAD`;
   - aplicar hard/soft gates;
   - escrever diagnóstico no `STATE.md`;
   - retornar `exit 1` em hard fail;
4. ao receber signoff válido do QA:
   - marcar sprint `PASSED`;
   - avançar `current_sprint`;
   - gerar novo `start_hash` da sprint seguinte.

Saídas mínimas de erro:
- código da regra;
- arquivos afetados;
- instrução de correção;
- indicação de possível `override` (quando permitido).

---

## 7) Fluxo do QA Validator por Sprint

Para cada sprint:
1. validar apenas artefatos dentro do escopo da sprint ativa;
2. verificar critérios de aceite definidos no `spec.md`;
3. registrar evidências objetivas (comando, resultado, hash);
4. assinar checkpoint da sprint em `spec.md`;
5. registrar checkpoint em `STATE.md`.

Sem assinatura, sprint seguinte permanece `LOCKED`.

---

## 8) Controle de Impacto (Scope Blowout)

O cálculo deve ser incremental por sprint (base `start_hash` da sprint):
- `files_changed`
- `churn_total`
- `impact_score` ponderado por criticidade de caminho

Sugestão de peso por caminho:
- `src/core/**`: 3
- `src/integration/**`: 2
- `tests/**`: 1
- `docs/**`: 0.5

Se ultrapassar limite:
- soft/hard conforme policy;
- exigir fragmentação da sprint ou `override` justificado.

---

## 9) Operação fora de `.specs` ("rodar como deuses fora da .spec")

Diretriz: **execução primária continua dentro de `.specs/features/...`**, mas é possível operar fora dela com governança.

### 9.1 Quando é permitido
- documentação de produto em `planos/`;
- scripts utilitários do framework;
- ajustes de integração CI/harness;
- migração de artefatos históricos.

### 9.2 Como não perder controle
- toda mudança fora de `.specs` deve referenciar `feature_id` no commit/log;
- `harness_runner.py` precisa de whitelist explícita de caminhos globais permitidos;
- alterações fora da whitelist viram `hard gate`.

### 9.3 Regra prática
- implementação de feature: dentro de `.specs/features/[feature]`;
- infraestrutura do framework: fora de `.specs`, mas com contrato e rastreio.

Conclusão: sim, dá para operar fora da `.specs`, mas não “livre”; precisa de política de escopo global para manter o fail-closed.

---

## 10) Migração de memória e arquivamento

Ao finalizar a última sprint:
1. consolidar decisões relevantes de `STATE.md` em `JOURNAL.md`;
2. marcar `feature_status: done` em `spec.md`;
3. mover feature para `_archive_features/`;
4. anexar entrada em `log_old_features.md` com `feature_id`, período, hashes e resultado.

Critério de consolidação (evitar ruído):
- mover apenas decisão, incidente, exceção e lição reutilizável;
- descartar logs operacionais repetitivos.

---

## 11) Plano de implementação técnica no framework

Fase A - Contratos e parser
- expandir parser de `spec.md` para `contract_mode` e `sprints`;
- validar schema mínimo obrigatório em sprint-based;
- manter backward compatibility com modo standard.

Fase B - Harness
- implementar avaliador de escopo allow/deny;
- implementar avaliação hard/soft + policy mode;
- implementar cálculo de impacto incremental por `start_hash`.

Fase C - QA Validator
- adaptar assinatura para checkpoint por sprint;
- persistir evidências em formato estável;
- negar assinatura se critérios de aceite não forem objetivos.

Fase D - Estado e memória
- normalizar template de `STATE.md` por sprint;
- adaptar `purge_journal.py` para segmentação por sprint;
- consolidar migração final para `JOURNAL.md`.

Fase E - Governança
- definir profile padrão (`hybrid`);
- definir thresholds default;
- definir fluxo oficial de override com expiração.

---

## 12) Critérios de pronto (Definition of Done)

O modelo é considerado pronto quando:
- harness bloqueia corretamente avanço sem signoff;
- escopo por sprint é respeitado com hard fail em violação;
- impacto é calculado por `start_hash` da sprint atual;
- QA assina sprint de forma parcial e auditável;
- fechamento migra memória útil e arquiva feature sem perda histórica.

---

## 13) Riscos e mitigação

- Spec mal definido -> mitigar com template obrigatório + lint de contrato.
- Excesso de burocracia -> mitigar com sprints curtas e campos mínimos.
- Falso positivo em impacto -> mitigar com score ponderado e tuning por repositório.
- Bypass operacional -> mitigar com hard gate em escopo global e trilha de override.

---

## 14) Veredito

Este desenho mantém a base do framework e adiciona governança de alto controle para execução de IA em features grandes. O ganho principal é transformar entrega longa em sequência de contratos curtos, verificáveis e bloqueáveis, com rastreabilidade técnica de ponta a ponta.

---
*Atualizado em: 2026-04-30 16:28*