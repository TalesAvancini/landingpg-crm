---
version: V2_SAFE_EXECUTION_DRAFT
status: READY_FOR_EXECUTION
topic: Contract Sprints - Caminho Seguro no Workshop
date: 2026-04-30
execution_mode: SAFE_PATH
primary_workspace: .specs/features/
orchestrator: Falsh
auditor: QA + Harness + SAM
---

# Plano Completo V2 (Caminho Seguro)

## 0) Proposito

Este plano define uma execucao **completa, detalhada e auditavel** para evoluir o framework para Contract Sprints sem quebrar o ecossistema atual.

Diretriz central:
- **Executar dentro da `.specs` como caminho oficial**;
- Preservar compatibilidade com o contrato atual (`standard` v2.5.2);
- Introduzir `sprint_based` de forma progressiva com gates fail-closed;
- Entregar evidencia suficiente para auditoria tecnica posterior.

---

## 1) Escopo

## 1.1 Em escopo
- Evolucao do contrato de spec para suportar `standard` e `sprint_based`.
- Evolucao do `harness_runner.py` para validacao dual mode.
- Evolucao do `qa-validator` para checkpoint por sprint.
- Evolucao de `STATE.md` para telemetria incremental de sprint.
- Ajustes em automacoes de higiene (`cleanup_specs.py`, SAM auditor quando necessario).
- Atualizacao de docs SSOT relacionados ao fluxo.
- Testes de regressao para nao quebrar o modo atual.

## 1.2 Fora de escopo
- Remocao do modo `standard`.
- Operacao livre fora da `.specs` sem whitelist.
- Mudancas de infraestrutura nao relacionadas ao fluxo de governanca.

---

## 2) Premissas e Restricoes

- Harness atual roda em pre-commit e deve continuar fail-closed.
- `qa_signoff` e requisito de aprovacao continuam obrigatorios.
- Zero Trust e segregacao de contexto permanecem.
- Toda feature de implementacao deste plano sera criada em `.specs/features/[feature-id]/`.
- Toda excecao precisa estar registrada em `STATE.md` e `JOURNAL.md`.

---

## 3) Definicao de Pronto (DoD do Plano V2)

A V2 sera considerada pronta somente quando:
1. Modo `standard` continuar funcional sem regressao.
2. Modo `sprint_based` validar sprint ativa com bloqueio de avancos indevidos.
3. QA assinar por sprint com evidencia objetiva.
4. Harness bloquear violacao de escopo e ordem de sprint.
5. Impacto por sprint usar `start_hash` (nao apenas diff global).
6. Cleanup nao arquivar indevidamente specs sprint-based ativas.
7. SAM/Journal manter rastreabilidade consistente com checkpoints.
8. Documentacao SSOT refletir o novo fluxo.

---

## 4) Estrategia de Execucao (Macrofases)

## Fase A - Fundacao de Contrato (compatibilidade primeiro)
Objetivo: manter sistema atual vivo e introduzir estrutura para dual mode.

Entregas:
- schema de frontmatter para `sprint_based`;
- atualizacao de `.specs/_template.md` com secao dual;
- validacao de campos obrigatorios por modo.

Critico:
- nao remover nenhum campo exigido pelo fluxo `standard`.

## Fase B - Harness Dual Mode
Objetivo: `harness_runner.py` entender dois modelos sem ambiguidade.

Entregas:
- detector de `contract_mode`/`type`;
- branch `standard` preservado;
- branch `sprint_based` com gates hard/soft;
- mensagens de erro com codigo de regra + acao corretiva.

## Fase C - QA por Sprint
Objetivo: substituir assinatura unica final por assinatura incremental no novo modo.

Entregas:
- update de `.agent/subagents/qa-validator.md`;
- assinatura por sprint no `spec.md`;
- update de `STATE.md` com checkpoint e evidencia.

## Fase D - Impacto Incremental
Objetivo: evitar falso positivo/falso negativo em scope blowout.

Entregas:
- leitura de `start_hash` por sprint;
- diff incremental por sprint;
- limiares por sprint (arquivos/churn/score).

## Fase E - Higiene e Governanca
Objetivo: impedir conflitos com automacoes paralelas.

Entregas:
- ajuste do `cleanup_specs.py` para respeitar sprint ativa;
- ajuste de padrao de journal/handoff para SAM;
- docs SSOT sincronizados.

## Fase F - Piloto Controlado
Objetivo: validar fluxo com risco baixo antes de generalizar.

Entregas:
- 3 features piloto em `sprint_based`;
- relatorio de bloqueios, falsos positivos, tempo de ciclo;
- tune de thresholds/policy.

---

## 5) Blueprint de Contrato (Detalhado)

## 5.1 Frontmatter `standard` (permanece)
Campos existentes mantidos:
- `contract_version`, `type: standard`, `executor_context_id`, `validator_context_id`, `impact_control.max_impact_radius`, `definition_of_done`, `qa_signoff`, `signed_by`.

## 5.2 Frontmatter `sprint_based` (novo)
Campos obrigatorios:
- `contract_mode: sprint_based`
- `feature_status: in_progress|blocked|done`
- `current_sprint`
- `policy_profile: strict|advisory|hybrid`
- `sprints.<id>.goal`
- `sprints.<id>.scope_allow[]`
- `sprints.<id>.scope_deny[]`
- `sprints.<id>.acceptance[]`
- `sprints.<id>.qa_signoff`

Campos recomendados:
- `sprints.<id>.signed_by`
- `sprints.<id>.signed_at`
- `thresholds` por sprint
- `override_policy`

Regra obrigatoria:
- apenas 1 sprint ativa por vez.

---

## 6) Policy Matrix Oficial (para o Falsh aplicar)

## 6.1 Hard Gates (bloqueia)
- `HG01_SCOPE_VIOLATION`: alterou arquivo fora do escopo permitido da sprint.
- `HG02_SECURITY_ZONE`: alterou area sensivel sem permissao.
- `HG03_CONTRACT_BREAK`: aceite obrigatorio nao cumprido.
- `HG04_SPRINT_ORDER`: tentativa de avancar sem signoff da sprint atual.
- `HG05_OUTSIDE_WORKSHOP`: alteracao fora de `.specs` sem whitelist aprovada para tarefa de framework.
- `HG06_INVALID_START_HASH`: `start_hash` da sprint atual invalido, ausente ou nao resolvivel no repositorio.
- `HG07_OUTSIDE_WHITELIST`: alteracao em arquivo fora da whitelist operacional do plano.

## 6.2 Soft Gates (alerta / justifica)
- `SG01_HIGH_CHURN`
- `SG02_IMPACT_GROWTH`
- `SG03_ARCH_WARNING`
- `SG04_HASH_ORPHANED`: hash de inicio orfao por reescrita de historico (ex.: force-push).
- `SG05_REPEAT_UNBLOCK`: sprint desbloqueada mais de 2 vezes.

## 6.3 Perfis de politica
- `strict`: hard e soft bloqueiam.
- `advisory`: hard bloqueia, soft alerta.
- `hybrid` (padrao recomendado): hard bloqueia, soft exige justificativa.

## 6.4 Override
Permitido somente com:
- regra alvo;
- motivo tecnico;
- aprovador;
- expiracao;
- rollback plan;
- registro em `STATE.md` e resumo no `JOURNAL.md`.

## 6.5 Modelo minimo de justificativa para Soft Gates (perfil `hybrid`)
Formato obrigatorio por ocorrencia:

```yaml
gate: <codigo_do_gate>
file: <arquivo_acionado>
reason: <1-2 frases objetivas>
decision: accepted | waived
approved_by: <identidade>
```

Regras de qualidade:
- `reason` com menos de 10 caracteres: rejeitar.
- justificativa identica para arquivos diferentes na mesma sprint: rejeitar.
- `reason` generico (`ok`, `necessario`): rejeitar.

Armazenamento:
- registrar em `STATE.md` no bloco `gates.soft_triggered[]` da sprint ativa.

---

## 7) Algoritmo Operacional do Harness (passo a passo)

1. Localizar spec ativa em `.specs/features/<feature>/spec.md`.
2. Extrair frontmatter e detectar modo.
3. Se `standard`:
   - executar validacoes atuais sem alteracao de semantica.
4. Se `sprint_based`:
   - ler `current_sprint`;
   - validar estrutura minima da sprint;
   - carregar `start_hash` da sprint em `STATE.md`;
   - validar `start_hash` com `git cat-file -t <hash>`;
   - bloquear com `HG06_INVALID_START_HASH` se hash ausente/invalido;
   - calcular diff incremental (`start_hash..HEAD` + staged quando aplicavel);
   - validar hard gates;
   - validar soft gates e justificativas;
   - validar whitelist operacional fora de `.specs` (`HG07_OUTSIDE_WHITELIST`);
   - produzir diagnostico estruturado;
   - `exit 1` em hard fail.
5. Em sucesso de checkpoint QA:
   - marcar sprint como `PASSED`;
   - atualizar `current_sprint`;
   - abrir proxima sprint com novo `start_hash`.

Invariantes adicionais de `start_hash`:
- o `start_hash` de cada sprint e write-once (nao sobrescrever); tentativa de overwrite sem override formal -> hard fail.
- se hash existir no `STATE.md` mas nao estiver mais acessivel no historico local/remoto esperado, acionar `SG04_HASH_ORPHANED` e exigir justificativa para continuar.

Saida padrao de erro:
- codigo da regra;
- evidencia (arquivo/linha/metrica);
- acao sugerida;
- opcao de override (se permitido).

---

## 8) Especificacao do `STATE.md` por Sprint

Template minimo por sprint:

```md
## sprint_01
start_hash: <git-hash>
captured_at: <timestamp>
captured_by: @spec-driver
status: IN_PROGRESS
policy_profile: hybrid
impact_snapshot:
  files_changed: 0
  churn_added: 0
  churn_removed: 0
  impact_score: 0
gates:
  hard_failed: []
  soft_triggered: []
exceptions: []
unblock_history: []
qa_checkpoint:
  signed: false
  signed_by: null
  signed_at: null
  evidence: []
```

Regra de captura:
- ao abrir sprint, registrar obrigatoriamente `start_hash`, `captured_at`, `captured_by`.
- o valor de `start_hash` so pode ser definido uma vez por sprint; redefinicao exige override formal.

Transicoes validas:
- `IN_PROGRESS -> WAITING_SIGNOFF -> PASSED`
- `IN_PROGRESS -> BLOCKED`
- `BLOCKED -> IN_PROGRESS` (com registro de desbloqueio)

Condicoes objetivas para `BLOCKED -> IN_PROGRESS`:
- bloqueio por hard gate (`HG01`-`HG07`): requer evidencia de correcao + harness PASS.
- bloqueio por dependencia externa: requer evidencia de desbloqueio (link, commit, aprovacao).
- bloqueio por decisao humana: requer motivo tecnico documentado + aprovacao.

Registro obrigatorio de desbloqueio:

```yaml
unblocked_at: <timestamp>
unblocked_by: <identidade>
unblock_reason: <motivo tecnico>
unblock_evidence: <referencia>
```

Regra de recorrencia:
- se uma sprint acumular mais de 2 desbloqueios, disparar `SG05_REPEAT_UNBLOCK` e exigir revisao de causa raiz antes de continuar.

Transicao invalida (bloquear):
- `IN_PROGRESS -> PASSED` sem `qa_checkpoint.signed: true`.

---

## 9) Playbook do Falsh (Execucao)

## 9.1 Preparacao
- criar feature de trabalho em `.specs/features/contract_sprints_v2_safe/`;
- clonar template de spec;
- definir modo inicial `standard` para baseline de regressao;
- criar backlog em `tasks.md` por fase.

## 9.2 Execucao por ondas
Onda 1 (contrato/template) -> Onda 2 (harness dual) -> Onda 3 (qa sprint) -> Onda 4 (impacto incremental) -> Onda 5 (cleanup/SAM/docs) -> Onda 6 (pilotos).

Dependencias internas das ondas:
- Onda 1: `A1 -> A2 -> A3 -> Verify A`.
- Onda 2: `B1 -> (B2 || B3) -> B4 -> B5 -> Verify B`.
- Onda 3: `C1 -> (C2 || C3) -> Verify C`.
- Onda 4: `D1 -> D2 -> D3 -> D4 -> Verify D`.
- Onda 5: `(E1 || E2 || E3) -> Verify E`.
- Onda 6: `F1 -> F2 -> F3 -> Verify F`.

Regra de ouro:
- nao iniciar Onda N+1 sem checkpoint validado da Onda N.

## 9.3 Evidencias obrigatorias por onda
- diff relevante;
- comandos de validacao executados;
- resultado PASS/FAIL;
- decisoes tecnicas e trade-offs;
- hash de checkpoint.

---

## 10) Playbook de Auditoria (pos-execucao)

Auditoria minima por onda:
1. verificar se entrega o artefato prometido;
2. validar se a regra fail-closed continua ativa;
3. checar nao regressao em `standard`;
4. checar consistencia de `STATE.md`, `spec.md`, `JOURNAL.md`;
5. checar coerencia entre bloqueios de harness e justificativas.

Checklist objetivo:
- [ ] hard gate realmente bloqueou cenarios proibidos
- [ ] soft gate gerou justificativa quando necessario
- [ ] QA assinou apenas com evidencia
- [ ] cleanup nao arquivou sprint ativa
- [ ] SAM nao apontou handoff inconsistente

---

## 11) Backlog Tecnico Detalhado (Task Pack)

## A. Contrato e Template
- A1: atualizar `.specs/_template.md` para dual mode.
- A2: incluir exemplo sprint-based minimo valido.
- A3: documentar obrigatoriedade de `scope_allow/scope_deny`.
- Verify A: validar parser atual nao quebra com template atualizado.

## B. Harness Runner
- B1: implementar detector de modo.
- B2: encapsular validacao `standard` em funcao dedicada.
- B3: criar validador estrutural sprint-based.
- B4: implementar hard/soft gate engine.
- B5: padronizar codigos de regra.
- Verify B: simular spec validas e invalidas para ambos os modos.

## C. QA Validator
- C1: revisar prompt/contrato do subagente para checkpoint por sprint.
- C2: impedir `feature_done` antes da ultima sprint.
- C3: registrar evidencias no `STATE.md`.
- Verify C: teste de assinatura parcial e bloqueio de assinatura indevida.

## D. Impacto Incremental
- D1: capturar `start_hash` no inicio da sprint.
- D2: diff incremental por sprint.
- D3: score por criticidade de path.
- D4: thresholds configuraveis por sprint.
- Verify D: cenario com estouro real e cenario sem estouro.

Dependencia obrigatoria da Onda D:
- sequencia estrita `D1 -> D2 -> D3 -> D4 -> Verify D`.

## E. Higiene
- E1: adaptar `cleanup_specs.py` para nao limpar sprint ativa.
- E2: alinhar padrao textual de handoff/checkpoint para SAM.
- E3: atualizar docs de governanca (MASTER_FLOW, glossarios, prompts).
- Verify E: rodar pipeline completo sem regressao.

## F. Piloto
- F1: selecionar 3 features de risco baixo/medio.
- F2: executar em `sprint_based` com `hybrid`.
- F3: coletar metricas (bloqueios, lead time, overrides).
- Verify F: emitir relatorio de estabilizacao com recomendacoes finais.

---

## 12) Matriz de Riscos e Mitigacoes (execucao)

- R1: regressao no modo `standard`
  - mitigacao: suite de teste dedicada antes/depois de cada onda.
- R2: falso bloqueio alto no novo impacto
  - mitigacao: thresholds conservadores no piloto + tuning.
- R3: QA assinar sem evidencia
  - mitigacao: assinatura condicionada a checklist e comando comprovavel.
- R4: conflito com cleanup automatico
  - mitigacao: lock de sprint ativa no `STATE.md`.
- R5: deriva documental
  - mitigacao: gate de docs SSOT na Onda 5.

---

## 13) Plano de Testes

## 13.1 Regressao `standard`
- validar spec standard valida -> PASS;
- spec sem signoff -> FAIL;
- spec com contexto nao segregado -> FAIL.

## 13.2 Novo `sprint_based`
- sprint 1 valida -> PASS;
- tentativa de editar fora escopo -> FAIL (HG01);
- tentativa de pular sprint -> FAIL (HG04);
- soft gate acionado sem justificativa em hybrid -> FAIL.
- `start_hash` ausente/invalido -> FAIL (HG06);
- arquivo alterado fora da whitelist operacional -> FAIL (HG07);
- hash orfao por reescrita de historico -> SOFT (SG04) + justificativa obrigatoria;
- desbloqueio recorrente (>2) -> SOFT (SG05) + revisao de causa raiz.

## 13.3 Integracao
- rodar pipeline `context:all`;
- rodar harness explicitamente;
- validar logs em `HARNESS_LOG.md` e consistencia no `JOURNAL.md`.

---

## 14) Observabilidade e Metricas

Metricas obrigatorias no piloto:
- taxa de bloqueio hard por sprint;
- taxa de soft gate por sprint;
- taxa de override e motivo;
- tempo medio ate signoff por sprint;
- taxa de falso positivo percebido.

Saidas:
- tabela consolidada por feature piloto;
- recomendacao de thresholds finais;
- decisao de promover ou manter em beta.

---

## 15) Regras sobre operacao fora da `.specs` (neste V2)

Neste V2 seguro:
- implementacao de feature: exclusivamente em `.specs/features/...`;
- fora da `.specs`: apenas arquivos de framework/documentacao necessarios para viabilizar a mudanca;
- qualquer alteracao fora do escopo declarado da onda deve gerar bloqueio e revisao.

Whitelist operacional explicita para execucao do plano V2:
- `.context/_scripts/harness_runner.py`
- `.agent/subagents/qa-validator.md`
- `.agent/subagents/spec-driver.md`
- `.specs/_template.md`
- `.context/_scripts/cleanup_specs.py`
- `.context/maintenance/schema.sql` (somente se necessario para viabilizar validacoes)
- `.context/brain/MASTER_FLOW.md`
- `.context/brain/SCRIPT_GLOSSARY.md`
- `.context/brain/FILE_GLOSSARY.md`
- `.context/brain/HARNESS_REGISTRY.md`
- `tests/test_context.py`
- `tests/test_oracle.py` (somente se impactado)
- `.context/maintenance/JOURNAL.md`
- `.context/maintenance/HARNESS_LOG.md`

Regra de exclusao:
- qualquer arquivo fora desta whitelist exige pre-registro no `STATE.md` com justificativa tecnica e aprovacao antes da alteracao.
- toda extensao excepcional de whitelist deve ser espelhada no `JOURNAL.md`.

Isso evita o risco de travar por falta de cerca global pronta.

---

## 16) Artefatos de Saida Esperados

Ao final da execucao do Falsh, devem existir:
- spec de execucao da feature V2 completa e assinada;
- `STATE.md` com checkpoints por onda;
- codigo atualizado dos scripts necessarios;
- docs SSOT atualizados;
- relatorio de piloto com metricas;
- relatorio de auditoria final (eu audito em cima desses artefatos).

---

## 17) Comando Operacional (resumo para o Falsh)

Objetivo operacional:
- executar V2 em modo seguro, faseado e fail-closed;
- preservar `standard`;
- ativar `sprint_based` com checkpoint incremental;
- produzir evidencias auditaveis em cada onda.

Prioridade:
1) compatibilidade,
2) seguranca de gate,
3) auditabilidade,
4) performance.

---

## 18) Veredito de Execucao

Este plano V2 esta pronto para execucao controlada no Workshop. Ele reduz o risco de travamento estrutural porque respeita as amarracoes atuais do framework e introduz a evolucao por camadas verificaveis.

---
*Atualizado em: 2026-04-30 17:08 (BRT)*
