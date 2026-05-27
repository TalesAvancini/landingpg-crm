# 📓 Diário de Bordo: SDD Dry-Run Simulation

> **Objetivo:** Executar o ciclo SDD completo com tarefas triviais para validar empiricamente se o fluxo documentado no `FLOW_SDD.md` corresponde à realidade do repositório.
> **Branch:** `test/sdd-dry-run`
> **Feature ID:** `teste_trivial_dryrun`
> **Início:** 2026-05-27 18:55

---

## 📋 Checklist Master (Orquestrador SDD)

### Fase Hub: Preparação do Orquestrador
- [x] Ler `sdd-orchestrator/SKILL.md` (instrução)
- [x] Ler `spec_v3.md` (template)
- [x] Ler `AGENT_SCRATCHPAD.md` (template)
- [x] Ler `CLOSURE.md` (template)
- [x] Ler `SSD_PLAYBOOK.md` (manual tático)
- [x] Ler `spec-driver.md` (subagente executor)
- [x] Ler `rx-learnings.md` (sistema de memória)
- [x] Ler `JOURNAL.md` (estado atual)
- [x] Ler `HARNESS_LOG.md` (histórico de erros)

### Step 0: Pre-Flight Check
- [x] `git status --short` → Workspace sujo
- [x] Criado branch `test/sdd-dry-run`
- [/] Commit de limpeza → aguardando SAM
- [ ] `git status --short` → Limpo (validação final)

### Step 1: Blast Radius Calculation
- [ ] Identificar sementes de propagação
- [ ] Executar `blast_radius.py`
- [ ] Analisar buckets

### Step 2: Draft the Spec
- [ ] Preencher YAML frontmatter completo
- [ ] Definir `scope_allow` com todos os arquivos
- [ ] Definir `max_impact_radius`
- [ ] Injetar Raw Payloads na seção 5
- [ ] Salvar spec em `.specs/features/teste_trivial_dryrun/`

### Step 3: Human Ratification & Vaccine
- [ ] Mostrar spec ao usuário para ratificação
- [ ] `npm run context:inject` (MiMo)
- [ ] Verificar `.enriched.md` gerado
- [ ] Copiar template SCRATCHPAD para feature
- [ ] Criar STATE.md e tasks.md
- [ ] Commit do setup da spec
- [ ] Delegar ao spec-driver (subagente isolado)

### Step 4: Handle Escalations
- [ ] Aguardar/tratar BLOCKED
- [ ] Aguardar/tratar HANDOFF: ESCALATION
- [ ] Injetar DIRECTIVES no Scratchpad
- [ ] Emitir RESUME

### Step 5: Final Closure
- [ ] Aguardar qa_signoff
- [ ] `npm run context:harness`
- [ ] `npm run context:workflow-journal`
- [ ] Orquestrar propagação semântica
- [ ] `npm run context:learnings`
- [ ] Verificar CLOSURE.md
- [ ] Commit final
- [ ] `npm run context:cleanup`

---

## 🔬 Tarefas Triviais Definidas

As tarefas são INTENCIONALMENTE triviais. O objetivo não é o código — é o FLUXO.

| Task | Descrição | Caminho Esperado | O que Testa |
|:-----|:----------|:-----------------|:------------|
| TASK_01 | Criar `scratch/sum.py`: função que soma dois números | Happy path | Fases A→D completas |
| TASK_02 | Criar `scratch/avg.py`: função que calcula média de uma lista | Happy path variante | Skill 6 (Tier 1 write) |
| TASK_03 | Spec-driver tenta escrever arquivo FORA do `scope_allow` | BLOCKED → Escalation | Skill 5 (SCOPE_GUARD) |
| TASK_04 | Spec-driver declara FALHA e pede orientação | Bandeira Branca | Protocolo ANTI-LOOP + HANDOFF + RESUME |

---

## 📝 Narrativa em Tempo Real

### [2026-05-27 18:55] — Boot do Orquestrador
Li todos os documentos obrigatórios listados no checklist acima. Internalizei a mecânica das 9 skills, o fluxo de 5 steps do orquestrador, os templates, e o sistema de memória (MiMo/Learnings).

**Observação importante (SCRATCHPAD template vs instância):**
- O **template** vive em `.agent/templates/AGENT_SCRATCHPAD.md` (read-only, nunca editado em produção)
- O **instância** é copiado para `.specs/features/<feature_id>/AGENT_SCRATCHPAD.md` no Step 3 do Orquestrador
- O spec-driver escreve EXCLUSIVAMENTE na instância (INBOX/DIRECTIVES)
- O Orquestrador também escreve na instância (DIRECTIVES)
- Após fechamento, a instância é arquivada junto com a spec
→ **Delta com FLOW_SDD.md:** O FLOW_SDD (seção 2.7) lista apenas `.agent/templates/AGENT_SCRATCHPAD.md` como localização, sem explicar essa dualidade.

### [2026-05-27 18:56] — Step 0: Pre-Flight Check
Executei `git status --short`. Workspace estava sujo com:
- PROJECT_INDEX_01/02.md (auto-gerados)
- graphify-out/ (cache do Graphify)
- planos/ (relatórios e análises)

Criei branch `test/sdd-dry-run` e estou commitando a limpeza.
Aguardando resultado do commit (SAM pode bloquear por falta de entrada no JOURNAL).

**Observação:** O Step 0 do sdd-orchestrator não menciona a criação de branch. Em teoria, num projeto real, você estaria no branch de feature. Isso é um gap menor — o orquestrador deveria sugerir criar um branch de feature antes do commit de limpeza.

---

## 🔍 Deltas Encontrados (Acumulativo)

| # | Local no FLOW_SDD.md | Delta | Origem |
|:--|:---------------------|:------|:-------|
| D-01 | §2.7 (SCRATCHPAD) | Template vs instância não distinguidos | Leitura dos templates |
| D-02 | §4 (Sequência) | Step 0 não sugere criação de branch de feature | Step 0 Pre-Flight |
