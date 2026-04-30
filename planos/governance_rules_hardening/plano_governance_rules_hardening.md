---
version: V5
status: READY_FOR_SPEC_BOOTSTRAP
topic: Governance Rules Hardening
date: 2026-04-30
owner: @spec-driver
auditor: @qa-validator + Codex
source:
  - _flash_report/_flash_report.md
  - .context/brain/RULES.md
  - .context/brain/MASTER_FLOW.md
  - .context/monitoring/PROJECT_INDEX.md
---

# Plano: Governance Rules Hardening

## 1) Objetivo

Transformar aprendizados do pos-missao em governanca executavel end-to-end, eliminando reincidencia de:
- falso fechamento de onda com working tree suja;
- regressao estrutural em `STATE.md`;
- divergencia entre narrativa e estado real (`spec.md`/`tasks.md`/`STATE.md`/Git);
- fraude narrativa no SAM (journal indicando conclusao sem `qa_signoff`);
- desalinhamento entre regra documental e enforcement automatizado.

---

## 2) Diagnostico de Lacunas (a partir do PROJECT_INDEX)

Alem de `RULES.md` e `MASTER_FLOW.md`, o framework possui amarracoes sistemicas que precisam ser sincronizadas:

1. `HARNESS_REGISTRY.md` (catalogo oficial dos harnesses e gates)
2. `SCRIPT_GLOSSARY.md` (responsabilidades/efeitos dos scripts)
3. `FILE_GLOSSARY.md` (papel institucional dos arquivos SSOT)
4. `PROMPT_LIBRARY.md` (comandos e instrucoes para execucao consistente)
5. `AGENT_REGISTRY.md` (competencias e criterios de atuacao por papel)
6. `validate_context.py` e `tests/test_context.py` (enforcement automatico)
7. `workflow_journal_auditor.py` (SAM / anti-fraude narrativa)
8. `.github/workflows/context-health.yml` (cobertura de CI para governanca)

Lacunas especificas de agenciamento identificadas:
- ausencia de regra de fechamento hardened nos papeis `spec-driver` e `qa-validator`;
- falta de enforcement atomico de `start_hash` na transicao para `IN_PROGRESS`;
- ausencia de deteccao explicita para contradicao `Journal concluida` + `qa_signoff: false`;
- telemetria sem taxonomia de friccao governanca (`[GOVERNANCE-FRICTION]`).

Risco estrutural:
- `planos/` e `_flash_report/` estao em `ignored_dirs`; aprendizados nao viram operacao se nao migrarem para `.context/brain` + scripts/tests.

---

## 3) Escopo da Mudanca

## 3.1 Escopo primario (normas)
- `.context/brain/RULES.md`
- `.context/brain/MASTER_FLOW.md`

## 3.2 Escopo de sincronizacao (documentacao institucional)
- `.context/brain/HARNESS_REGISTRY.md`
- `.context/brain/SCRIPT_GLOSSARY.md`
- `.context/brain/FILE_GLOSSARY.md`
- `.context/brain/PROMPT_LIBRARY.md`
- `.context/brain/AGENT_REGISTRY.md`
- `.context/maintenance/rx-communications.md`

## 3.3 Escopo de enforcement (automacao)
- `.context/_scripts/harness_runner.py` (checks leves de fechamento, se necessario)
- `.context/_scripts/validate_context.py`
- `.context/_scripts/workflow_journal_auditor.py`
- `tests/test_context.py`
- `.github/workflows/context-health.yml` (se necessario para gate de CI)

## 3.4 Fora de escopo
- refatoracao ampla da arquitetura do harness;
- redesign de Oracle/Synapse;
- mudancas nao relacionadas a governanca de fechamento, integridade SSOT e anti-fraude narrativa.

---

## 4) Resultado Esperado

Ao fim da feature, o framework deve ter:
1. Regra canonica de fechamento (`CLOSE_WAVE`) obrigatoria e inequivoca;
2. Regra anti-falso-pass com estado minimo obrigatorio quando falhar;
3. Regra de transicao atomica para `IN_PROGRESS` com `start_hash` imutavel no ciclo;
4. SAM capaz de detectar fraude narrativa (`Journal concluida` com `qa_signoff: false`);
5. Telemetria padronizada com evento/tag `[GOVERNANCE-FRICTION]`;
6. papeis `spec-driver` e `qa-validator` com protocolo hardened de fechamento;
7. `AGENT_REGISTRY.md` atualizado com competencia `Hardened Closing`;
8. pelo menos 1 ponto de enforcement automatico ativo em script/teste/CI;
9. mapa oficial de conectividade institucionalizado em `.context/maintenance/rx-communications.md` com referencias cruzadas no `MASTER_FLOW.md` e `FILE_GLOSSARY.md`.

---

## 5) Propostas Normativas (conteudo a inserir)

## 5.1 RULES.md - Regra `CLOSE_WAVE`
Uma onda so pode ser declarada concluida se **todas** as condicoes forem verdadeiras:
- Harness PASS;
- coerencia entre `spec.md`, `STATE.md`, `tasks.md`;
- `git status --short` sem saida;
- evidencia registrada em `JOURNAL.md` e/ou `HARNESS_LOG.md`;
- `qa_signoff: true` no `STATE.md` da feature.

Falha em qualquer condicao:
- status obrigatorio: `IN_PROGRESS`;
- declaracao de conclusao proibida;
- emissao de evento de friccao `[GOVERNANCE-FRICTION]`.

## 5.2 RULES.md - Regra `ANTI_FALSE_PASS`
- E proibido marcar `Verify` completo quando ha divergencia entre artefatos e estado de Git.
- Claims narrativos (`100% concluido`, `baseline limpa`) devem ser comprovaveis por evidencia objetiva.
- Contradicao narrativa com `qa_signoff: false` e classificada como fraude narrativa de fechamento.
- Incluir exemplos binarios PASS/FAIL para reduzir interpretacao subjetiva.

## 5.3 RULES.md - Regra `MIMO_STATE_INTEGRITY`
Toda automacao que altera `STATE.md` deve:
- preservar campos obrigatorios por sprint: `start_hash`, `captured_at`, `captured_by`, `status`, `policy_profile`, `qa_checkpoint`, `qa_signoff`;
- atualizar somente bloco-alvo (edicao cirurgica);
- falhar de forma segura (`fail-closed`) sem corromper arquivo em caso de erro.

## 5.4 RULES.md - Regra `ATOMIC_START_HASH_ON_PROGRESS`
Na transicao de status para `IN_PROGRESS`:
- `start_hash` deve ser capturado uma unica vez, no mesmo commit logico de transicao;
- se `start_hash` ja existir, alteracao e proibida ate fechamento/cancelamento formal;
- ausencia de `start_hash` em `IN_PROGRESS` invalida a transicao;
- atualizacao parcial (status sem `start_hash`) deve falhar (`fail-closed`).

## 5.5 RULES.md - Regra `CRITICAL_SCRIPT_SANITY`
Mudancas em `cleanup_specs.py`, `harness_runner.py`, `validate_context.py`, `workflow_journal_auditor.py` exigem:
- checagem de escopo/import;
- execucao minima de sanidade do script alterado;
- evidencia de nao regressao no `STATE.md`/`HARNESS_LOG.md`.

## 5.6 MASTER_FLOW.md - `Pre-Close Audit` (rito obrigatorio)
Antes de fechar qualquer onda:
1) validar Harness
2) validar coerencia Spec/State/Tasks
3) validar arvore limpa
4) validar evidencia em log/journal
5) validar `qa_signoff: true`
6) registrar checkpoint
7) so entao declarar fechamento

## 5.7 MASTER_FLOW.md - `Runbook Anti-Reincidencia`
Checklist operacional obrigatorio por onda:
1. Implementar escopo
2. Rodar harness
3. Verificar integridade estrutural de `STATE.md`
4. Verificar consistencia cruzada (`spec`/`tasks`/`state`)
5. Garantir arvore limpa
6. Confirmar `qa_signoff: true`
7. Declarar conclusao com evidencia quantitativa

## 5.8 AGENT ROLES - Hardened Closing (spec-driver / qa-validator)
Adicionar ao contrato dos papeis:

### `spec-driver`
- so pode mover para concluida apos `CLOSE_WAVE PASS`;
- em transicao para `IN_PROGRESS`, deve garantir `start_hash` atomico;
- deve registrar evidencia objetiva (nao apenas narrativa) no `JOURNAL.md`;
- deve executar `Pre-close Self-Audit` antes do handoff para o QA.

### `qa-validator`
- deve bloquear fechamento quando `qa_signoff: false`;
- deve validar ausencia de fraude narrativa (journal vs estado real);
- deve emitir `NOK` com motivo verificavel quando houver contradicao.

---

## 6) Sincronizacao Institucional (obrigatoria)

## 6.1 HARNESS_REGISTRY.md
- registrar gates e funcoes reais em uso (`HG01-HG07`, `C2`, regras de fechamento);
- incluir gate de coerencia `qa_signoff` no fechamento.

## 6.2 SCRIPT_GLOSSARY.md
- atualizar descricoes de `harness_runner.py`, `cleanup_specs.py`, `validate_context.py`, `workflow_journal_auditor.py` com comportamento hardened.

## 6.3 FILE_GLOSSARY.md
- atualizar papel de `STATE.md`, `spec.md`, `tasks.md`, `HARNESS_LOG.md`, `JOURNAL.md` como conjunto de evidencia de fechamento auditavel;
- registrar `rx-communications.md` como artefato oficial de topologia de comunicacao de governanca.

## 6.4 PROMPT_LIBRARY.md
- incluir instrucao explicita para nao declarar conclusao sem `CLOSE_WAVE PASS` + `qa_signoff: true`.

## 6.5 AGENT_REGISTRY.md
- adicionar competencia transversal `Hardened Closing`;
- mapear capacidades minimas por papel (`spec-driver`, `qa-validator`);
- definir comportamento obrigatorio de bloqueio de fechamento por inconsistencia narrativa.

## 6.6 RX Communications (novo artefato operacional)
- criar `.context/maintenance/rx-communications.md` como SSOT de conectividade;
- incluir mapa de nos, arestas, eventos criticos, bloqueios fail-closed e telemetria `[GOVERNANCE-FRICTION]`;
- manter referencia cruzada obrigatoria com `MASTER_FLOW.md` (normativo) e `FILE_GLOSSARY.md` (papel institucional).

---

## 7) Enforcement Automatico Minimo (deve existir)

Implementar pelo menos **dois** pontos de enforcement (preferencia em ordem):

1. `validate_context.py` valida `CLOSE_WAVE` + `ATOMIC_START_HASH_ON_PROGRESS` em modo `sprint_based`.
2. `tests/test_context.py` cobre:
   - falso fechamento (arvore suja);
   - transicao `IN_PROGRESS` sem `start_hash`;
   - mutacao indevida de `start_hash`.
3. `workflow_journal_auditor.py` detecta fraude narrativa:
   - `JOURNAL` declara concluida;
   - `STATE.qa_signoff == false`.
4. `context-health.yml` executa essas verificacoes em CI.
5. logs estruturados com tag `[GOVERNANCE-FRICTION]` para todos os bloqueios de fechamento.

Criterio: sem enforcement minimo, mudancas ficam documentais e nao passam DoD.

---

## 8) Schema de Telemetria de Friccao (novo)

Eventos de friccao de governanca devem seguir schema minimo:

```yaml
event_tag: "[GOVERNANCE-FRICTION]"
event_code: "GF-<dominio>-<id>"
severity: "LOW|MEDIUM|HIGH|CRITICAL"
feature_id: "<feature>"
sprint_id: "<sprint>"
rule_id: "<RULES.md rule id>"
agent_role: "spec-driver|qa-validator|system"
state_status: "<STATE.status>"
qa_signoff: true|false
start_hash_present: true|false
journal_claim_done: true|false
detected_at: "<ISO-8601>"
action_taken: "blocked|warned|auto-remediated"
evidence_ref:
  - "<path-or-log-id>"
```

Regras:
- todo bloqueio de fechamento deve gerar evento `[GOVERNANCE-FRICTION]`;
- fraude narrativa detectada deve usar `severity: HIGH` ou `CRITICAL`;
- ausencia de evento em falha critica e nao conformidade.

---

## 9) Estrategia de Execucao (Sprints da Feature)

Regra de execucao inicial (obrigatoria antes da Sprint 01):
- aplicar o **Rito de Inicio** da secao 13.1;
- sem Rito de Inicio validado, a Sprint 01 nao pode ser marcada como iniciada.

## Sprint 01 - Regras Canonicas
- adicionar `CLOSE_WAVE` + `ANTI_FALSE_PASS` em `RULES.md`;
- adicionar `Pre-Close Audit` em `MASTER_FLOW.md`;
- adicionar no workflow do executor (`spec-driver`) o passo **Pre-close Self-Audit** antes de handoff ao QA;
- incluir exemplos PASS/FAIL no `RULES.md` para evitar interpretacao.

Aceite binario:
- PASS: regras publicadas, sem ambiguidade, com condicoes verificaveis.
- FAIL: qualquer regra depender de interpretacao subjetiva.

## Sprint 02 - Integridade SSOT e Sanidade de Script
- adicionar `MIMO_STATE_INTEGRITY` e `CRITICAL_SCRIPT_SANITY` em `RULES.md`;
- mapear relacao com fluxo mestre.

Aceite binario:
- PASS: campos obrigatorios e politica cirurgica explicitos.
- FAIL: ausencia de fail-closed ou campos obrigatorios incompletos.

## Sprint 03 - Runbook e Metricas
- inserir runbook anti-reincidencia no `MASTER_FLOW.md`;
- formalizar metricas minimas por onda (HG/SG/hotfix/rejeicoes).

Aceite binario:
- PASS: checklist executavel por executor e auditor.
- FAIL: checklist sem criterios objetivos de comprovacao.

## Sprint 04 - Sincronizacao Institucional
- atualizar `HARNESS_REGISTRY.md`, `SCRIPT_GLOSSARY.md`, `FILE_GLOSSARY.md`, `PROMPT_LIBRARY.md`.

Aceite binario:
- PASS: documentos institucionais sem conflito com regras novas.
- FAIL: qualquer documento divergir do contrato normativo.

## Sprint 05 - Enforcement minimo
- implementar validacao automatica em script/teste/CI (secao 7).

Aceite binario:
- PASS: cenario de falso fechado falha de forma deterministica.
- FAIL: falha nao detectada por automacao.

## Sprint 06 - Hardening de Agenciamento e Transicao Atomica
- atualizar papeis `spec-driver` e `qa-validator` com protocolo de `Hardened Closing`;
- implementar enforcement atomico de `start_hash` na transicao para `IN_PROGRESS`;
- cobrir testes de mutacao indevida de `start_hash`.

Aceite binario:
- PASS: transicao `IN_PROGRESS` sem `start_hash` e bloqueada e testada.
- PASS: alteracao de `start_hash` apos captura inicial e bloqueada e testada.
- FAIL: qualquer transicao parcial ou mutacao posterior passar sem bloqueio.

## Sprint 07 - Hardening SAM + Telemetria + Competencia
- endurecer `workflow_journal_auditor.py` para detectar fraude narrativa (`Journal concluida` + `qa_signoff: false`);
- implantar schema de telemetria com tag `[GOVERNANCE-FRICTION]`;
- atualizar `AGENT_REGISTRY.md` com competencia `Hardened Closing`.

Aceite binario:
- PASS: fraude narrativa gera bloqueio explicito e evento telemetrico.
- PASS: `AGENT_REGISTRY.md` contem competencia e criterios por papel.
- FAIL: deteccao apenas informativa (sem bloqueio) ou sem evento/tag.

## Sprint 08 - Institucionalizacao RX de Comunicacao
- criar `.context/maintenance/rx-communications.md` com topologia completa de comunicacao de governanca;
- adicionar referencia explicita no `MASTER_FLOW.md` para uso do RX como mapa oficial de conectividade;
- atualizar `FILE_GLOSSARY.md` com a funcao oficial do novo artefato.

Aceite binario:
- PASS: `rx-communications.md` existe e cobre nos, arestas, eventos, bloqueios e telemetria.
- PASS: `MASTER_FLOW.md` e `FILE_GLOSSARY.md` referenciam explicitamente o arquivo novo.
- FAIL: ausencia de referencia cruzada ou mapa incompleto de conectividade.

---

## 10) Definition of Done (Feature) - Ajustada

A feature so fecha quando **todas** as condicoes abaixo forem verdadeiras:
- `RULES.md` contem `CLOSE_WAVE`, `ANTI_FALSE_PASS`, `MIMO_STATE_INTEGRITY`, `ATOMIC_START_HASH_ON_PROGRESS`, `CRITICAL_SCRIPT_SANITY`;
- `MASTER_FLOW.md` contem `Pre-Close Audit` + Runbook com validacao de `qa_signoff`;
- `HARNESS_REGISTRY.md`, glossarios, `PROMPT_LIBRARY.md` e `AGENT_REGISTRY.md` estao sincronizados;
- `.context/maintenance/rx-communications.md` foi criado e referenciado em `MASTER_FLOW.md` e `FILE_GLOSSARY.md`;
- competencia `Hardened Closing` publicada para `spec-driver` e `qa-validator`;
- existem no minimo 2 pontos de enforcement automatico ativos (script/teste/CI);
- SAM detecta e bloqueia fraude narrativa (`journal_claim_done=true` com `qa_signoff=false`);
- telemetria `[GOVERNANCE-FRICTION]` e emitida em todo bloqueio critico;
- `tasks.md` da feature esta 100% marcado;
- `STATE.md` da feature em `PASSED` com evidencia quantitativa;
- arvore Git limpa no fechamento;
- auditoria final confirma zero contradicao entre narrativa e estado real.

---

## 11) Matriz de Riscos e Mitigacao

- Risco: burocracia sem execucao.
  - Mitigacao: exigir no minimo 2 pontos de enforcement automatico (secao 7).

- Risco: regra generica nao auditavel.
  - Mitigacao: criterios binarios PASS/FAIL por sprint.

- Risco: regressao por edicao de SSOT.
  - Mitigacao: politica cirurgica + validacao pos-escrita + fail-closed.

- Risco: fraude narrativa em fechamento.
  - Mitigacao: bloqueio SAM + validacao de `qa_signoff` + telemetria obrigatoria.

- Risco: aprendizado preso em `planos/`/`_flash_report`.
  - Mitigacao: migracao de norma para `.context/brain` e enforcement para scripts/tests/CI.

---

## 12) Plano de Testes

Casos minimos obrigatorios:
1. fechar onda com arvore suja -> deve falhar;
2. fechar onda com `tasks` marcado e `STATE` inconsistente -> deve falhar;
3. transicao para `IN_PROGRESS` sem `start_hash` -> deve falhar;
4. mutar `start_hash` apos captura inicial -> deve falhar;
5. `JOURNAL` com claim de conclusao e `qa_signoff: false` -> deve falhar no SAM;
6. bloqueio critico sem evento `[GOVERNANCE-FRICTION]` -> deve falhar;
7. fluxo valido completo (`CLOSE_WAVE` + `qa_signoff: true`) -> deve passar;
8. `rx-communications.md` ausente ou sem referencia cruzada no `MASTER_FLOW.md`/`FILE_GLOSSARY.md` -> deve falhar.

---

## 13) Bootstrap da Nova Feature Spec

Criar feature em:
- `.specs/features/governance_rules_hardening/`

Arquivos iniciais obrigatorios:
- `spec.md`
- `tasks.md`
- `STATE.md`

Parametros recomendados:
- `contract_mode: sprint_based`
- `policy_profile: hybrid`
- `current_sprint: sprint_01`
- `scope_allow` inicial:
  - `.context/brain/RULES.md`
  - `.context/brain/MASTER_FLOW.md`
  - `.context/brain/HARNESS_REGISTRY.md`
  - `.context/brain/SCRIPT_GLOSSARY.md`
  - `.context/brain/FILE_GLOSSARY.md`
  - `.context/brain/PROMPT_LIBRARY.md`
  - `.context/brain/AGENT_REGISTRY.md`
  - `.context/maintenance/rx-communications.md`
  - `.context/_scripts/validate_context.py`
  - `.context/_scripts/workflow_journal_auditor.py`
  - `tests/test_context.py`
  - `.specs/features/governance_rules_hardening/spec.md`
  - `.specs/features/governance_rules_hardening/tasks.md`
  - `.specs/features/governance_rules_hardening/STATE.md`
  - `.context/maintenance/HARNESS_LOG.md`
  - `.context/maintenance/JOURNAL.md`

## 13.1 Rito de Inicio (obrigatorio, anti-deriva)

Antes de qualquer alteracao de conteudo da Sprint 01, executar e registrar:

1. **Baseline de arranque**
- registrar `start_hash`, `captured_at`, `captured_by` no `STATE.md` da nova feature;
- registrar o commit base no `JOURNAL.md` com referencia de evidencia.

2. **Higiene inicial de arvore**
- validar `git status --short` sem saida;
- se houver sujeira, o status da sprint permanece `BLOCKED` ate saneamento.

3. **Escopo minimo travado**
- confirmar que a Sprint 01 toca apenas:
  - `.context/brain/RULES.md`
  - `.context/brain/MASTER_FLOW.md`
  - arquivos da propria feature em `.specs/features/governance_rules_hardening/`
- qualquer expansao de escopo exige justificativa e registro formal de override.

4. **Rito de re-sincronizacao cognitiva (Ralph Wiggum Check)**
- quando houver deriva por sessao longa, reexecutar leitura de `RULES.md`, `MASTER_FLOW.md`, `spec.md`, `tasks.md`, `STATE.md` antes de prosseguir;
- registrar o re-sync no `JOURNAL.md` como evento operacional (mitigacao de contexto).

Criterio binario de aceite do Rito de Inicio:
- PASS: os quatro itens acima registrados com evidencia.
- FAIL: ausencia de qualquer item bloqueia inicio de implementacao.

---

## 14) Veredito

Plano pronto para abrir a feature spec `governance_rules_hardening` com cobertura completa de norma, agenciamento hardened, enforcement automatico, telemetria de friccao e prevencao ativa de fraude narrativa.

---
*Atualizado em: 2026-04-30 20:55 (BRT)*
