---
status: AUDIT_REPORT
topic: Auditoria de Aderencia - Spec-Driven Contract Sprints
date: 2026-04-30
scope:
  - .context/brain/FILE_GLOSSARY.md
  - .context/brain/SCRIPT_GLOSSARY.md
  - .context/monitoring/PROJECT_INDEX.md
  - planos/mudanca_specdriven/mudanca_specdriven.md
---

# Relatorio de Auditoria Tecnica

## 1) Resumo Executivo

A proposta de Contract Sprints esta conceitualmente forte, mas hoje ha incompatibilidades objetivas com as amarracoes reais do framework. O principal risco nao e de conceito; e de **acoplamento com automacoes existentes** que ainda esperam contrato `standard` (v2.5.2) e validacoes binarias.

Veredito:
- A ideia e viavel;
- O rollout direto quebraria o fluxo atual de Harness/QA em pontos criticos;
- E necessario um plano de migracao em camadas para manter compatibilidade e evitar bloqueio operacional falso.

---

## 2) Base da Auditoria (Evidencias)

Evidencias chave observadas:
- `.specs/_template.md` usa contrato `2.5.2`, `type: standard`, `max_impact_radius`, `definition_of_done`, `qa_signoff` binario.
- `.context/_scripts/harness_runner.py` valida contrato com regex simples e pressupostos de `standard`:
  - exige `definition_of_done`;
  - exige `qa_signoff: true` e `signed_by: @qa-validator` para passar;
  - valida impacto por `git diff --name-only HEAD` com contagem total;
  - nao possui parser de `sprints`, `current_sprint`, `scope_allow/scope_deny`.
- `.agent/subagents/qa-validator.md` assina contrato em modo unico final (`qa_signoff: true`, `STATE.md -> DONE`), sem checkpoint por sprint.
- `MASTER_FLOW.md` e `AGENT_REGISTRY.md` reforcam segregacao, zero-trust e efemeridade da `.specs`, mas nao descrevem contrato multi-sprint.
- `PROJECT_INDEX.md` confirma presenca dos scripts e specs ativos, e mostra que `planos/` esta em `ignored_dirs` no bundler de contexto.

---

## 3) Falhas Antecipaveis (com severidade)

## F01 - Incompatibilidade de contrato entre plano novo e Harness atual
- Severidade: Critica
- Probabilidade: Alta
- Impacto: Commits bloqueados ou falsos passes dependendo do formato final da spec.
- Causa raiz: `harness_runner.py` nao entende `contract_mode: sprint_based` nem checkpoints parciais.
- Sinal de falha: erro de contrato ausente/invalido, ou exigencia de `qa_signoff: true` global antes do fim real da feature.
- Mitigacao:
  - adicionar branch de validacao por `contract_mode`;
  - manter `standard` intacto;
  - introduzir `sprint_based` com schema minimo validado.

## F02 - QA Validator assina estado final cedo ou tarde demais
- Severidade: Critica
- Probabilidade: Alta
- Impacto: quebra da logica de checkpoint; sprint pode liberar sem criterio correto.
- Causa raiz: subagente atual so conhece assinatura final (`DONE`) e nao assinatura incremental por sprint.
- Mitigacao:
  - atualizar `.agent/subagents/qa-validator.md` para assinatura por sprint;
  - diferenciar `sprint_signoff` de `feature_done`;
  - registrar evidencia por sprint no `STATE.md`.

## F03 - Scope Blowout com medicao errada
- Severidade: Alta
- Probabilidade: Alta
- Impacto: falsos positivos (bloqueio indevido) e falsos negativos (vazamento de escopo).
- Causa raiz: impacto atual usa `git diff HEAD` global + contagem simples de arquivos.
- Mitigacao:
  - calcular diff contra `start_hash` da sprint;
  - separar staged/unstaged se necessario;
  - adicionar score ponderado por caminho critico.

## F04 - Conflito com efemeridade de specs (>48h)
- Severidade: Alta
- Probabilidade: Media
- Impacto: `cleanup_specs.py` pode arquivar feature multi-sprint ativa por inatividade entre fases.
- Causa raiz: regra atual presume spec atomica de curta duracao.
- Mitigacao:
  - marcar estado de sprint ativa no `STATE.md` com heartbeat;
  - isentar features `sprint_based` com status `IN_PROGRESS` do auto-cleanup.

## F05 - Falha de rastreabilidade no JOURNAL/SAM
- Severidade: Alta
- Probabilidade: Media
- Impacto: divergencia entre o que foi executado e o que foi narrado; auditoria SAM pode reprovar.
- Causa raiz: handoff/checkpoint por sprint ainda sem padrao textual canonical para o auditor.
- Mitigacao:
  - definir formato padrao de log por sprint (handoff + evidencias + hash);
  - atualizar `workflow_journal_auditor.py` para reconhecer o padrao novo.

## F06 - Divergencia de documentos SSOT
- Severidade: Media
- Probabilidade: Alta
- Impacto: framework aparentemente adota sprint-based, mas guias oficiais continuam no modelo antigo.
- Causa raiz: glossarios, master flow, template e prompts ainda v2.5.2-like.
- Mitigacao:
  - atualizar `FILE_GLOSSARY.md`, `SCRIPT_GLOSSARY.md`, `MASTER_FLOW.md`, `PROMPT_LIBRARY.md` em pacote unico;
  - registrar mudanca no `JOURNAL.md`.

## F07 - Operacao fora de `.specs` sem cerca global
- Severidade: Alta
- Probabilidade: Media
- Impacto: fuga de escopo em arquivos estrategicos (`brain/`, `market/`, `maintenance/`).
- Causa raiz: plano novo permite excecoes fora de `.specs`, mas harness atual nao aplica whitelist global por feature.
- Mitigacao:
  - introduzir whitelist global no harness para `sprint_based`;
  - violacao fora de whitelist -> hard fail;
  - override temporal com expiracao e aprovador.

## F08 - Falha de onboarding de novos agentes/roles de sprint
- Severidade: Media
- Probabilidade: Media
- Impacto: agentes executam sem permissao formal (quebra de governanca).
- Causa raiz: `AGENT_REGISTRY.md` exige registro obrigatorio; novo ritual pode introduzir papeis sem cadastro.
- Mitigacao:
  - registrar toda role nova antes de ativar;
  - manter principio de menor privilegio por pasta/arquivo.

## F09 - Planos fora do radar do bundler
- Severidade: Baixa
- Probabilidade: Alta
- Impacto: aprendizado do plano nao entra no pacote de contexto automatico.
- Causa raiz: `planos/` esta em `ignored_dirs` no `PROJECT_INDEX.md`.
- Mitigacao:
  - se quiser que plano vire memoria operacional automatica, mover/espelhar decisao relevante em `.context/brain` e `maintenance/JOURNAL.md`.

---

## 4) Gaps de Implementacao (o que falta para nao quebrar)

1. Parser de contrato no harness com suporte dual (`standard` + `sprint_based`).
2. Evolucao do template `.specs/_template.md` para incluir frontmatter sprint-based (sem remover standard).
3. Evolucao do QA subagent para assinatura por sprint e atualizacao de `STATE.md` incremental.
4. Reescrita do modulo de impacto para base `start_hash` + score.
5. Regras de cleanup adaptadas para features longas.
6. Atualizacao dos docs de governanca (`MASTER_FLOW`, glossarios e prompts).
7. Testes automatizados cobrindo ambos os modos de contrato.

---

## 5) Matriz de Compatibilidade Recomendada

- Modo `standard`:
  - comportamento atual preservado;
  - zero regressao;
  - continua default ate estabilizar.

- Modo `sprint_based`:
  - ativacao explicita por frontmatter;
  - gates hard/soft por policy profile;
  - checkpoint por sprint + desbloqueio progressivo.

Rollback seguro:
- qualquer falha no novo modo deve permitir fallback para `standard` sem editar scripts manualmente.

---

## 6) Plano de Rollout Seguro (ordem tecnica)

Fase 0 - Preparacao
- congelar requisitos do contrato sprint-based;
- definir schema de `spec.md` e `STATE.md`.

Fase 1 - Harness compativel
- implementar parser dual + flags;
- manter validacao antiga intacta.

Fase 2 - QA e STATE
- atualizar `qa-validator` para checkpoint parcial;
- padronizar `STATE.md` por sprint.

Fase 3 - Impacto e escopo
- migrar para diff incremental por `start_hash`;
- adicionar whitelist global para operacao fora de `.specs`.

Fase 4 - Hygiene
- adaptar `cleanup_specs.py` e `workflow_journal_auditor.py`;
- atualizar docs SSOT.

Fase 5 - Hardening
- testes de regressao em `tests/test_context.py` (novo bloco para sprint-based);
- simular cenarios de falha (scope violation, signoff ausente, override expirado).

---

## 7) Resposta objetiva: "rodar como deuses fora da .spec"

Pode, mas com limite estrito.

Recomendacao formal:
- feature code continua dentro de `.specs/features/[feature]`;
- fora de `.specs` so para infraestrutura de framework/documentacao de governanca;
- toda escrita fora da whitelist da sprint deve falhar em hard gate;
- excecao apenas com override auditavel (motivo, aprovador, expiracao, rollback).

Sem isso, o modelo perde o principal beneficio: fail-closed real.

---

## 8) Decisao Tecnica Recomendada

A proposta deve seguir para implementacao, mas em **modo de migracao compativel**, nao em substituicao direta.

Criterio para promocao a padrao:
- zero regressao no `standard`;
- 3 features piloto sprint-based finalizadas sem bypass manual;
- taxa de falso bloqueio aceitavel;
- auditoria SAM consistente com checkpoints por sprint.

---
*Emitido em: 2026-04-30 16:34 (BRT)*