# Tasks: Wiki Level 2

Rifa de tarefas atômicas para implementação do paradigma Karpathy Wiki.

---

## [Phase 1] Foundation & Logs
- [x] **TASK-01**: Criar arquivos base da Wiki.
  - Criar `.context/market/WIKI/_index.md` (root index).
  - Criar `.context/market/wiki_log.md` (append-only log).
  - *Verify*: `ls .context/market/WIKI/_index.md`
- [x] **TASK-02**: Atualizar documentação de governança.
  - Injetar fluxo INGEST -> LINT -> LOG em `RULES.md` e `MASTER_FLOW.md`.
  - *Verify*: Check manual dos arquivos.

## [Phase 2] Oracle Cascade
- [x] **TASK-03**: Patch cirúrgico em `context_oracle.py`.
  - Injetar lógica de busca SSOT -> Index -> Lexical.
  - *Verify*: `python .context/_scripts/context_oracle.py "test"` deve retornar fallback (exit 2).

## [Phase 3] Guard & Lint
- [x] **TASK-04**: Implementar `ingest_wiki_guard.py`.
  - Validação de schema (Frontmatter, Fonte, Takeaways).
  - *Verify*: Rodar contra um mock inválido e esperar falha.
- [x] **TASK-05**: Atualizar `lint_wiki.py` para modo `--strict`.
  - Bloqueio de artigos sem meta-dados Karpathy.
  - *Verify*: `python .context/_scripts/lint_wiki.py --strict`
- [x] **TASK-06**: Integrar no pipeline Central.
  - Atualizar `run_context.py` e `package.json` com novos comandos.
  - *Verify*: `npm run context:all` verde.

## [Phase 4] Health Check
- [x] **TASK-07**: Patch em `validate_context.py`.
  - Injetar `check_wiki_integrity()`.
  - *Verify*: `npm run context:wiki-health`

## [Phase 5] Traceability & Hotfix v2.5.1
- [ ] **TASK-08**: Criar utilitário de log robusto.
  - Criar `.context/_scripts/_wiki_log_utils.py` (atomic append + escape).
  - *Verify*: Script manual de teste de escrita.
- [ ] **TASK-09**: Instrumentar Ingestão e Lint.
  - Patches em `ingest_wiki_guard.py` e `lint_wiki.py`.
  - *Verify*: Validar entradas `OK/FAIL/SKIP` no log.
- [ ] **TASK-10**: Instrumentar Oráculo (Resumo de Query).
  - Patch em `context_oracle.py`.
  - *Verify*: `npm run context:oracle` gera log.
- [ ] **TASK-11**: Validação Operacional (Stress Test).
  - Testar fluxo de erro e correção real.
  - *Verify*: `wiki_log.md` preenchido corretamente.
- [ ] **TASK-12**: Release Bump v2.5.1 (Global SSOT).
  - Atualizar VERSION.md, package.json, Inception e Vision.
  - *Verify*: `npm run context:check-version`.
- [ ] **TASK-13**: Refatoração Factual do Walkthrough.
  - Sincronizar narrativa com a realidade operacional.
  - *Verify*: Leitura final do artefato.
