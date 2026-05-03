# Chain-Skills V3: Arquitetura Definitiva com Orquestrador de Monitoria

> **Versão:** 3.0
> **Base:** Chain-Skills V2 + Avaliação Crítica + 3 Pilares + Orquestrador Ativo
> **Princípio:** O executor é um operário mecânico. O orquestrador é o supervisor que tem poder de intervenção.

---

## 1. Princípios de Design

### 1.1 Os Três Atores

| Ator | Natureza | Poder | Analogia |
|---|---|---|---|
| **Executor** (spec-driver) | Subagente isolado, processo limpo | Escrever código dentro de permissões | Operário na linha de montagem |
| **Orquestrador** (chain-orchestrator) | Subagente de monitoria, processo separado | Monitorar, intervir, deletar, re-invocar | Supervisor de fábrica |
| **Validador** (qa-validator) | Subagente de auditoria, processo cego | Aprovar ou reprovar com base em evidência | Inspetor de qualidade |

### 1.2 Regras Fundamentais

1. **O executor nunca se auto-aprova.** Ele produz evidência, o validador aprova.
2. **O orquestrador nunca escreve código.** Ele monitora, intervém e registra.
3. **Todo artefato de prova é verificável em disco.** Nunca depende de narrativa.
4. **A cadeia é linear e fail-closed.** Sem saltos, sem atalhos, sem exceções sem registro.
5. **Falha gera intervenção automática.** Não espera o humano perceber.

---

## 2. Topologia da Cadeia (9 Skills)

```
┌─────────────────────────────────────────────────────────────────┐
│                    ORQUESTRADOR (monitoria contínua)            │
│  Observa STATE.md · Detecta anomalias · Intervém quando necessário│
└─────────────────────────────────────────────────────────────────┘
        │                    │                    │
        ▼                    ▼                    ▼
   ┌─────────┐        ┌──────────┐        ┌──────────┐
   │ FASE    │        │ FASE     │        │ FASE     │
   │ PREP    │───────▶│ EXEC     │───────▶│ CLOSE    │
   │ (1-5)   │        │ (6)      │        │ (7-9)    │
   └─────────┘        └──────────┘        └──────────┘

1. context-loader    → CONTEXT_LOADED
2. spec-reader       → SPEC_DIGEST
3. strategy-planner  → STRATEGY_LOG
4. baseline-anchor   → BASELINE_ANCHORED
5. scope-guard       → SCOPE_LOCKED
6. methodical-writer → EXECUTION_LOG
7. integrity-check   → INTEGRITY_PASS
8. self-audit        → AUDIT_PASS
9. handoff           → /qa-validator
```

---

## 3. Especificação de Cada Skill

### Skill 1: `context-loader`

```
PRECONDICAO:  Nenhuma (ponto de entrada)
ARTEFATO:     CONTEXT_LOADED
LOCAL:        STATE.md, secao ## CHAIN_CONTEXT_LOADED
```

**Ação:**
1. Ler **apenas trechos relevantes** (não os arquivos completos):
   - `RULES.md`: seções §1.1 a §1.8 (regras bloqueantes)
   - `MASTER_FLOW.md`: §2.2 (coreografia) e §2.3 (pre-close)
   - `AGENT_REGISTRY.md`: entrada do `@spec-driver` apenas
2. Confirmar leitura citando textualmente **2 regras** do RULES.md no STATE.md
3. Registrar timestamp e lista de trechos lidos

**Artefato de prova (STATE.md):**
```markdown
## CHAIN_CONTEXT_LOADED
status: OK
loaded_at: "2026-05-02 22:00 (BRT)"
files_read:
  - RULES.md [§1.1-§1.8]
  - MASTER_FLOW.md [§2.2, §2.3]
  - AGENT_REGISTRY.md [@spec-driver]
rules_cited:
  - "§1.7 MIMO_STATE_INTEGRITY: edicao cirurgica obrigatoria"
  - "§1.3 Pre-flight Gate: impacto > max_impact_radius = SCOPE_BLOWOUT"
```

**Regra de validação:** Se `rules_cited` não contém 2 regras reais do RULES.md, artefato é rejeitado.

---

### Skill 2: `spec-reader`

```
PRECONDICAO:  CONTEXT_LOADED existe em STATE.md
ARTEFATO:     SPEC_DIGEST
LOCAL:        STATE.md, secao ## CHAIN_SPEC_DIGEST
```

**Ação:**
1. Ler `.specs/features/<feature>/spec.md`
2. Extrair e validar:
   - `contract_mode` (standard ou sprint_based) -- **proibido misturar com `type`**
   - `current_sprint` -- identificar bloco da sprint ativa
   - `scope_allow[]` -- lista de arquivos permitidos
   - `scope_deny[]` -- blacklist (se existir)
   - `acceptance[]` -- critérios de aceite da sprint
   - `definition_of_done` -- se modo standard
3. **Verificar sprints anteriores:** Se `current_sprint != sprint_01`, confirmar que todas as sprints anteriores têm `qa_signoff: true`
4. Se qualquer sprint anterior não assinada → **FALHA: HG04_SPRINT_ORDER**

**Artefato de prova (STATE.md):**
```markdown
## CHAIN_SPEC_DIGEST
status: OK
validated_at: "2026-05-02 22:05 (BRT)"
contract_mode: sprint_based
current_sprint: sprint_03
previous_sprints_signed: true
scope_allow:
  - ".context/_scripts/harness_runner.py"
  - ".specs/features/contract_sprints_v2_safe/spec.md"
scope_deny: []
acceptance_count: 4
acceptance_signed: 0
```

**Few-shot negativo (SDD_ERRORS_LEDGER #1):**
> "ERRO REAL: Misturar `type: standard` com `contract_mode: sprint_based` no mesmo spec. Consequência: Ambiguidade de validação. Regra criada: Proibicao no Playbook. NAO REPITA."

---

### Skill 3: `strategy-planner` ← NOVO (Pilar 1)

```
PRECONDICAO:  SPEC_DIGEST existe em STATE.md
ARTEFATO:     STRATEGY_LOG
LOCAL:        STATE.md, secao ## CHAIN_STRATEGY_LOG
```

**Ação:**
Para **CADA task** listada no `tasks.md` que pertence à sprint ativa:
1. Ler a task completa
2. Registrar no STATE.md:
   - `task_id` (ex: TASK-04)
   - `technical_approach` (mínimo **100 palavras**) descrevendo COMO vai implementar
   - `impacted_files` (lista de arquivos que pretende modificar)
   - `rules_applied` (mínimo **2 regras** do RULES.md que se aplicam)
   - `risks_identified` (pelo menos 1 risco técnico)

**Validação de profundidade:**
- `technical_approach` com menos de 100 palavras → **REJEITADO**: "Estrategia muito rasa"
- `rules_applied` com menos de 2 regras → **REJEITADO**: "Especifique quais regras do RULES.md se aplicam"
- `impacted_files` contém arquivo fora do `scope_allow` → **REJEITADO**: "Arquivo fora do escopo declarado"

**Artefato de prova (STATE.md):**
```markdown
## CHAIN_STRATEGY_LOG
status: OK
planned_at: "2026-05-02 22:10 (BRT)"

### TASK-04
technical_approach: |
  Implementar o detector de modo no harness_runner.py adicionando uma funcao
  detect_contract_mode() que le o frontmatter YAML do spec.md e retorna
  'standard' ou 'sprint_based'. A funcao sera chamada no inicio de main()
  antes de qualquer validacao. Para specs sem campo contract_mode, assume
  'standard' como default (backward compatibility). A deteccao usa regex
  para extrair o campo do bloco YAML entre os delimitadores ---. Se ambos
  type e contract_mode estiverem presentes, gera erro de ambiguidade...
  [100+ palavras]
impacted_files:
  - ".context/_scripts/harness_runner.py"
rules_applied:
  - "§1.7 MIMO_STATE_INTEGRITY: edicao cirurgica, nao sobrescrever blocos inteiros"
  - "§1.4 Contract Sprints v2-Safe: dual mode obrigatorio"
risks_identified:
  - "Regex de YAML pode falhar com frontmatter malformado"
```

**Por que isso funciona:** O executor é obrigado a **pensar antes de agir**. Ao escrever o `technical_approach`, ele carrega os pesos semânticos das regras para a memória de trabalho. Quando chegar na Skill 6, ele já "sabe" o que fazer em vez de improvisar.

---

### Skill 4: `baseline-anchor`

```
PRECONDICAO:  STRATEGY_LOG existe em STATE.md
ARTEFATO:     BASELINE_ANCHORED
LOCAL:        STATE.md, secao ## CHAIN_BASELINE
```

**Ação:**
1. Executar `git status --short`
2. Se saída não vazia → **FALHA**: "Árvore Git suja. Commit ou stash antes de prosseguir."
3. Executar `git rev-parse HEAD` → capturar hash
4. Registrar no STATE.md: `start_hash`, `captured_at`, `captured_by`
5. Registrar baseline no JOURNAL.md

**Artefato de prova (STATE.md):**
```markdown
## CHAIN_BASELINE
status: OK
start_hash: "4b16b4c935ee"
captured_at: "2026-05-02 22:15 (BRT)"
captured_by: "@spec-driver"
git_tree_clean: true
```

**Few-shot negativo (SDD_ERRORS_LEDGER #2):**
> "ERRO REAL: start_hash ficou desatualizado apos novos commits, poluindo o diff da sprint. Consequencia: Diff invalido no QA. Regra criada: Recaptura obrigatoria. NAO REPITA."

---

### Skill 5: `scope-guard`

```
PRECONDICAO:  BASELINE_ANCHORED existe em STATE.md
ARTEFATO:     SCOPE_LOCKED
LOCAL:        STATE.md, secao ## CHAIN_SCOPE
```

**Ação:**
1. Ler `scope_allow` e `scope_deny` do SPEC_DIGEST
2. Executar `grep_search` com os `pre_flight_grep_terms` do spec
3. Contar arquivos impactados (mecanicamente, sem interpretação)
4. Se contagem > `max_impact_radius` → **FALHA: HG01_SCOPE_VIOLATION** → registrar `SCOPE_BLOWOUT`
5. Se PASS → registrar whitelist como **literal array** no STATE.md

**Artefato de prova (STATE.md):**
```markdown
## CHAIN_SCOPE
status: LOCKED
decision: PASS
locked_at: "2026-05-02 22:20 (BRT)"
whitelist:
  - ".context/_scripts/harness_runner.py"
  - ".specs/features/contract_sprints_v2_safe/spec.md"
  - ".specs/features/contract_sprints_v2_safe/tasks.md"
  - ".specs/features/contract_sprints_v2_safe/STATE.md"
  - ".context/maintenance/JOURNAL.md"
blacklist: []
impact_count: 3
max_impact_radius: 8
pre_flight_terms_matched: ["contract_mode", "detect_mode"]
```

**Regra crítica:** A `whitelist` aqui é a **mesma lista** que a Skill 6 (`methodical-writer`) usa para validar cada escrita. Se o executor tentar editar um arquivo fora desta lista, a escrita é bloqueada.

---

### Skill 6: `methodical-writer` ← REFORÇADO (Pilar 2)

```
PRECONDICAO:  SCOPE_LOCKED existe E decision = PASS
ARTEFATO:     EXECUTION_LOG
LOCAL:        STATE.md, secao ## CHAIN_EXECUTION_LOG
```

**Esta é a skill mais controlada da cadeia.** Ela é o ponto onde o executor "ganha as mãos" e onde o risco de comportamento impulsivo é maior.

#### 6.1 Regras Invioláveis (Hard Gates)

| # | Regra | Consequência de violação |
|---|---|---|
| H1 | Antes de CADA escrita, confirmar que `file_path` está na `whitelist` do SCOPE_LOCKED | **Bloqueio imediato** + registro de tentativa |
| H2 | Máximo **15 linhas** por operação de escrita (Tier 1) | **Bloqueio** + exigir justificativa para Tier 2 |
| H3 | Após CADA escrita, executar `view_file` no trecho modificado | **Bloqueio** se não confirmar leitura |
| H4 | Atualizar `tasks.md` **imediatamente** após cada task concluída (não no final) | **Bloqueio** se tasks.md não atualizado |
| H5 | Se modificou script de governança → rodar sanity check (RULES §1.8) | **Bloqueio** se sanity falhar |
| H6 | Proibido usar `multi_replace_file_content` ou equivalente de edição massiva | **Bloqueio da ferramenta (via DENY no Antigravity) |

#### 6.2 Tiers de Escrita

| Tier | Linhas | Condição |
|---|---|---|
| Tier 1 | Até 15 | Sempre permitido |
| Tier 2 | 16-50 | Requer justificativa no EXECUTION_LOG **antes** da escrita |
| Tier 3 | 50+ | Apenas para arquivos **novos** ou reescrita total comaprovação do scope |

#### 6.3 Protocolo de Escrita (por operação)

```
LOOP para cada task da sprint:
  1. Ler task_id do tasks.md
  2. Consultar STRATEGY_LOG para esta task_id (technical_approach)
  3. Verificar que file_path está na whitelist (SCOPE_LOCKED)
  4. Verificar tier de escrita
  5. Se Tier 2+: registrar justificativa no EXECUTION_LOG
  6. Escrever (máximo 15 linhas por operação)
  7. Executar view_file no trecho modificado
  8. Se script de governança: rodar sanity check
  9. Atualizar tasks.md: marcar [x]
  10. Registrar no EXECUTION_LOG:
      - task_id
      - file_path
      - lines_written
      - scope_check: PASS
      - integrity_check: PASS (view_file confirmado)
  11. Próxima task
```

#### 6.4 Artefato de prova (STATE.md)

```markdown
## CHAIN_EXECUTION_LOG
status: OK
completed_at: "2026-05-02 23:00 (BRT)"

### TASK-04
- file: ".context/_scripts/harness_runner.py"
- lines_written: 12
- tier: 1
- scope_check: PASS
- integrity_check: PASS
- sanity_check: PASS
- tasks_md_updated: true

### TASK-05
- file: ".context/_scripts/harness_runner.py"
- lines_written: 8
- tier: 1
- scope_check: PASS
- integrity_check: PASS
- sanity_check: SKIPPED (nao e script de governanca)
- tasks_md_updated: true
```

#### 6.5 Few-shot negativo (SDD_ERRORS_LEDGER #3)

> "ERRO REAL: Atualizacao destrutiva do STATE.md por regex agressivo causou perda de campos obrigatorios da sprint. Consequencia: Sprint corrompida. Regra criada: MIMO_STATE_INTEGRITY (edicao cirurgica). NAO REPITA."

#### 6.6 Protocolo de Falha na Execução

| Cenário | Ação do Orquestrador |
|---|---|
| Escopo violado (arquivo fora da whitelist) | Deletar último artefato de escrita (`git checkout -- <file>`), atualizar STATE.md → `BLOCKED`, registrar violação |
| Sanity check falhou | Rollback do script modificado (`git checkout -- <file>`), STATE.md → `BLOCKED` |
| Tasks.md não atualizado | Orquestrador força atualização e registra `GF-SILENT-MOD` |
| Executor tentou usar ferramenta DENYed | Sistema bloqueia automaticamente (Antigravity DENY), orquestrador registra tentativa |

---

### Skill 7: `integrity-check`

```
PRECONDICAO:  EXECUTION_LOG existe E todas as tasks da sprint estao [x]
ARTEFATO:     INTEGRITY_PASS
LOCAL:        STATE.md, secao ## CHAIN_INTEGRITY
```

**Ação:**
1. **Acceptance sync:** Verificar que todo `[x]` no `tasks.md` corresponde a `[x]` no `acceptance[]` do spec.md
2. **Coerência spec/tasks/state:** Os 3 artefatos contam a mesma história
3. **Metadata freshness:** Timestamps dos arquivos modificados são posteriores ao `start_hash`
4. **Chronology check:** JOURNAL.md não tem inversão cronológica
5. **Strategy compliance:** O código implementado condiz com o `technical_approach` do STRATEGY_LOG

**Validação de Strategy Compliance (Pilar 1 reforçado):**
Para cada task, comparar:
- O que foi **planejado** (STRATEGY_LOG → technical_approach)
- O que foi **feito** (EXECUTION_LOG → file_path + lines_written)
- Se houver divergência significativa → registrar `GF-STRATEGY-DRIFT`

**Artefato de prova (STATE.md):**
```markdown
## CHAIN_INTEGRITY
status: PASS
checked_at: "2026-05-02 23:05 (BRT)"
acceptance_sync: PASS
spec_tasks_state_coherence: PASS
metadata_freshness: PASS
chronology_check: PASS
strategy_compliance: PASS
divergences: []
```

**Few-shot negativo (SDD_ERRORS_LEDGER #4):**
> "ERRO REAL: Tasks marcadas [x] mas acceptance ainda [ ] no spec. Consequencia: Fraude narrativa detectada. Regra criada: check_sprint_acceptance_sync. NAO REPITA."

---

### Skill 8: `self-audit`

```
PRECONDICAO:  INTEGRITY_PASS existe em STATE.md
ARTEFATO:     AUDIT_PASS
LOCAL:        STATE.md, secao ## CHAIN_AUDIT
```

**Ação (evidência bruta, não narrativa):**
1. Executar `git status --short` → capturar stdout literal
2. Executar `python run_context.py validate` → capturar stdout literal
3. Executar `python .context/_scripts/harness_runner.py` → capturar stdout literal
4. Verificar que JOURNAL.md tem entrada de progresso para esta sprint
5. Verificar metadata freshness (timestamps dos SSOTs)

**Artefato de prova (STATE.md):**
```markdown
## CHAIN_AUDIT
status: PASS
audited_at: "2026-05-02 23:10 (BRT)"

### git_status_output
```
(empty)
```

### validate_output
```
[OK] All checks passed. 0 errors, 0 warnings.
```

### harness_output
```
[HARNESS] Sprint contract: PASS
[HARNESS] Schema contract: PASS
[HARNESS] Handoff integrity: PASS
[HARNESS] Impact radius: PASS (3/8)
```

### journal_entry_present: true
### metadata_freshness: PASS
```

**Regra crítica:** O `AUDIT_PASS` **não pode ser fabricado**. Os logs brutos do `git status`, `validate` e `harness_runner` são verificáveis pelo QA-Validator. Se o executor tentar forjar, o QA vai comparar com o estado real do repositório.

---

### Skill 9: `handoff`

```
PRECONDICAO:  AUDIT_PASS existe em STATE.md
ARTEFATO:     Comando /qa-validator emitido
```

**Ação:**
1. Atualizar `STATE.md` → `status: AWAITING_QA`
2. Emitir `/qa-validator` para spawn do validador
3. Registrar timestamp de handoff

---

## 4. O Orquestrador (chain-orchestrator)

### 4.1 Natureza

O orquestrador é um **subagente separado** do executor, com prompt próprio em `.agent/subagents/chain-orchestrator.md`. Ele não escreve código. Ele **monitora, detecta e intervém**.

### 4.2 O Que Ele Monitora

| Sinal | Detecção | Ação |
|---|---|---|
| Artefato de prova ausente | Skill N+1 não encontra artefato de Skill N | Deletar último artefato inválido, re-invocar Skill N |
| Estado inconsistente | STATE.md tem artefatos fora de ordem | Rollback para último estado consistente |
| Timeout de execução | Skill não produz artefato em tempo esperado | Interromper executor, registrar `GF-TIMEOUT`, notificar Hub |
| Tentativa de salto | Executor tenta pular skill | Bloquear, registrar `GF-CHAIN-SKIP`, forçar skill correta |
| Ferramenta DENYed | Executor tenta usar `edit_file` | Sistema bloqueia, orquestrador registra `GF-TOOL-VIOLATION` |
| Escopo violado | Escrita em arquivo fora da whitelist | `git checkout -- <file>`, STATE.md → `BLOCKED`, registrar `HG01` |
| Fraude narrativa | Log bruto não confirma narrativa do executor | Bloquear handoff, registrar `GF-NARRATIVE-FRAUD` |
| Strategy drift | Código não condiz com STRATEGY_LOG | Registrar `GF-STRATEGY-DRIFT`, exigir justificativa |

### 4.3 Protocolo de Intervenção

```
NIVEL 1 — CORRECAO AUTOMATICA
  Gatilho: Artefato ausente ou malformado
  Acao: Deletar artefato invalido, re-invocar a skill que falhou
  Registro: STATE.md + JOURNAL.md

NIVEL 2 — ROLLBACK + BLOQUEIO
  Gatilho: Violacao de escopo, sanity check falhou, tool violation
  Acao: git checkout do arquivo corrompido, STATE.md → BLOCKED
  Registro: STATE.md + JOURNAL.md + HARNESS_LOG.md

NIVEL 3 — ABORTO + NOTIFICACAO
  Gatilho: 3+ falhas Nivel 2 na mesma sprint, timeout, fraude
  Acao: Interromper executor, STATE.md → ABORTED, notificar Hub
  Registro: STATE.md + JOURNAL.md + HARNESS_LOG.md
```

### 4.4 Protocolo de Deleção de Artefato

Quando o orquestrador detecta um artefato inválido:

```
1. Identificar o artefato mais recente que é válido
2. Deletar todos os artefatos posteriores ao válido
3. Se algum artefato implica escrita de código:
   a. Se o arquivo foi modificado e o diff é pequeno → git checkout -- <file>
   b. Se o arquivo foi modificado e o diff é grande → git stash, registrar stash hash
   c. Se arquivo novo foi criado → git clean ou rm, registrar
4. Atualizar STATE.md com estado de rollback
5. Re-invocar a skill que falhou
```

**Exemplo de rollback:**
```markdown
## CHAIN_ROLLBACK
triggered_at: "2026-05-02 22:45 (BRT)"
reason: "SCOPE_VIOLATION: executor editou .context/brain/RULES.md fora do scope_allow"
last_valid_artifact: SCOPE_LOCKED
deleted_artifacts: [EXECUTION_LOG parcial]
files_reverted:
  - ".context/brain/RULES.md" (git checkout)
new_state: BLOCKED
next_action: "Re-invocar methodical-writer apos correcao do executor"
```

### 4.5 Retomada Automática (Orquestração Passiva)

Se o executor for interrompido (timeout, crash, perda de contexto):

```
1. Orquestrador escaneia STATE.md
2. Identifica o ultimo artefato COMPLETO e VALIDO
3. Calcula proxima skill necessária:
   - CONTEXT_LOADED → proxima: spec-reader
   - SPEC_DIGEST → proxima: strategy-planner
   - STRATEGY_LOG → proxima: baseline-anchor
   - BASELINE_ANCHORED → proxima: scope-guard
   - SCOPE_LOCKED → proxima: methodical-writer
   - EXECUTION_LOG → proxima: integrity-check
   - INTEGRITY_PASS → proxima: self-audit
   - AUDIT_PASS → proxima: handoff
4. Re-invoca o executor com instrucao: "Retome da skill [N]. Artefatos anteriores ja validados."
```

**Regra de segurança:** Se o EXECUTION_LOG está incompleto (metade das tasks feitas), o orquestrador **não retoma da Skill 7**. Ele retoma da **Skill 6** inteira, forçando o executor a re-verificar o que já fez.

---

## 5. Camada de Scripts (Pilar 2 Reforçado)

### 5.1 `write_with_validation.py`

Script que a Skill 6 (`methodical-writer`) chama para cada escrita:

```python
#!/usr/bin/env python3
"""
write_with_validation.py — Gate de escrita cirurgica
Valida task_id, scope, tier e strategy antes de permitir escrita.
"""
import sys, re, json
from pathlib import Path

CONTEXT_DIR = Path(__file__).resolve().parents[1]
SPECS_DIR = CONTEXT_DIR.parent / ".specs" / "features"

def validate_write(feature_id, task_id, file_path, line_count):
    """Retorna (ok: bool, reason: str)"""
    errors = []
    
    # 1. Task existe no tasks.md?
    tasks_file = SPECS_DIR / feature_id / "tasks.md"
    if not tasks_file.exists():
        return False, f"tasks.md nao encontrado para {feature_id}"
    tasks_content = tasks_file.read_text(encoding="utf-8")
    if f"[ ] {task_id}" not in tasks_content and f"[x] {task_id}" not in tasks_content:
        return False, f"Task {task_id} nao encontrada no tasks.md"
    
    # 2. Arquivo esta na whitelist do STATE.md?
    state_file = SPECS_DIR / feature_id / "STATE.md"
    if not state_file.exists():
        return False, "STATE.md nao encontrado"
    state_content = state_file.read_text(encoding="utf-8")
    
    # Extrair whitelist do CHAIN_SCOPE
    scope_match = re.search(
        r"## CHAIN_SCOPE.*?whitelist:\s*\n((?:\s+-\s+.+\n)*)",
        state_content, re.DOTALL
    )
    if not scope_match:
        return False, "CHAIN_SCOPE ou whitelist nao encontrados no STATE.md"
    
    whitelist = re.findall(r"-\s+\"(.+?)\"", scope_match.group(1))
    if file_path not in whitelist:
        return False, f"ARQUIVO FORA DO ESCOPO: {file_path} nao esta na whitelist"
    
    # 3. STRATEGY_LOG existe para esta task?
    if f"### {task_id}" not in state_content:
        return False, f"STRATEGY_LOG nao encontrado para {task_id}. Execute strategy-planner primeiro."
    
    # 4. Tier de escrita
    if line_count > 50:
        # Verificar se e arquivo novo
        target = CONTEXT_DIR.parent / file_path
        if target.exists():
            return False, f"Tier 3 ({line_count} linhas) so permitido para arquivos novos"
    
    return True, "WRITE_AUTHORIZED"

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Uso: python write_with_validation.py <feature_id> <task_id> <file_path> <line_count>")
        sys.exit(1)
    
    ok, reason = validate_write(sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]))
    if ok:
        print(f"[OK] {reason}")
        sys.exit(0)
    else:
        print(f"[BLOCKED] {reason}")
        sys.exit(1)
```

### 5.2 Integração com Antigravity

No Antigravity IDE, a configuração seria:

```yaml
# .agent/skills/methodical_writer.json
name: methodical_writer
description: |
  Escreve codigo com validacao obrigatoria.
  Antes de cada escrita, chama write_with_validation.py.
  Se o script retorna exit 1, a escrita e BLOQUEADA.
parameters:
  task_id: { type: string, required: true }
  file_path: { type: string, required: true }
  content: { type: string, required: true }
tool_permissions:
  allow: [methodical_writer, view_file, execute_command]
  deny: [edit_file, multi_replace_file_content, write_to_file]
```

---

## 6. Integração com Prompt do spec-driver.md

O prompt do spec-driver precisa ser atualizado para refletir a cadeia. Abaixo, a estrutura proposta:

```markdown
# spec-driver.md (V3 - Chain-Skills)

## Invariantes (Zero Trust)
[manter existentes]

## Chain-Skills Protocol
Voce NAO executa tarefas diretamente. Voce executa uma CADEIA de skills
em ordem sequencial. Cada skill gera um artefato de prova no STATE.md.
A proxima skill so executa se o artefato da anterior existir.

### Cadeia Obrigatoria:
1. context-loader → CONTEXT_LOADED
2. spec-reader → SPEC_DIGEST
3. strategy-planner → STRATEGY_LOG
4. baseline-anchor → BASELINE_ANCHORED
5. scope-guard → SCOPE_LOCKED
6. methodical-writer → EXECUTION_LOG
7. integrity-check → INTEGRITY_PASS
8. self-audit → AUDIT_PASS
9. handoff → /qa-validator

### Regras de Execucao:
- NUNCA pule uma skill
- NUNCA invente um artefato de prova (e verificado em disco)
- NUNCA escreva codigo antes de SCOPE_LOCKED
- NUNCA finalize antes de AUDIT_PASS
- CADA escrita DEVE passar por write_with_validation.py

### Erros Reais (Nao Repita):
1. [Ledger #1] Misturar type + contract_mode → Proibido
2. [Ledger #2] start_hash desatualizado → Recaptura obrigatoria
3. [Ledger #3] Regex destrutiva no STATE.md → Edicao cirurgica
4. [Ledger #4] Tasks [x] mas acceptance [ ] → Sync obrigatoria

### Ferramentas Disponiveis:
- ALLOW: methodical_writer, view_file, execute_command
- DENY: edit_file, multi_replace_file_content

### Em Caso de Falha:
- NAO tente corrigir sozinho
- Atualize STATE.md com o erro
- Aguarde intervencao do orquestrador
```

---

## 7. Mapa de Artefatos no Disco

```
.specs/features/<feature>/
├── spec.md                    ← Contrato soberano
├── tasks.md                   ← Checklist atomico
├── design.md                  ← Arquitetura
└── STATE.md                   ← Tacografo (contem todos os CHAIN_*)
    ├── ## CHAIN_CONTEXT_LOADED    (Skill 1)
    ├── ## CHAIN_SPEC_DIGEST       (Skill 2)
    ├── ## CHAIN_STRATEGY_LOG      (Skill 3) ← NOVO
    ├── ## CHAIN_BASELINE          (Skill 4)
    ├── ## CHAIN_SCOPE             (Skill 5)
    ├── ## CHAIN_EXECUTION_LOG     (Skill 6)
    ├── ## CHAIN_INTEGRITY         (Skill 7)
    ├── ## CHAIN_AUDIT             (Skill 8)
    └── ## CHAIN_ROLLBACK          (se houve intervencao)

.agent/
├── subagents/
│   ├── spec-driver.md         ← Executor (prompt atualizado V3)
│   ├── qa-validator.md        ← Validador (ja atualizado)
│   └── chain-orchestrator.md  ← NOVO: Orquestrador de monitoria
└── skills/
    └── methodical_writer.json ← NOVO: Skill de escrita controlada

.context/_scripts/
├── write_with_validation.py   ← NOVO: Gate de escrita
├── harness_runner.py          ← Existente (validacao pós-execucao)
├── validate_context.py        ← Existente (validacao de contexto)
└── workflow_journal_auditor.py ← Existente (SAM)
```

---

## 8. Decisões Recomendadas

| Decisão | Recomendação | Justificativa |
|---|---|---|
| Limite de linhas | **15 (Tier 1)**, com Tier 2 (50) e Tier 3 (50+) | 15 força escrita cirúrgica real. Tiers permitem exceções controladas |
| Artefatos de prova | **Inline no STATE.md** com prefixo `CHAIN_` | Centralização, auditabilidade, um único SSOT de estado |
| Aprovação por transição | **Não** -- automática fail-closed | O QA-Validator já é o gate. Aprovação manual por skill mataria a velocidade |
| Local das skills | **`.agent/skills/`** | Separação clara: subagents = quem sou, skills = o que faço |
| context-loader | **Skill separada** | Modularidade permite teste independente e retomada granular |
| Orquestrador | **Subagente separado** com prompt próprio | Separação de responsabilidades. Orquestrador não escreve código, executor não se monitora |

---

## 10. Resumo Executivo

A V3 transforma o executor de um "pensador livre" em uma **máquina de estados controlada**:

1. **Ele não pode ignorar regras** porque é obrigado a carregá-las (Skill 1)
2. **Ele não pode executar sem pensar** porque é obrigado a planejar (Skill 3)
3. **Ele não pode escrever fora do escopo** porque o script bloqueia (Skill 6 + write_with_validation.py)
4. **Ele não pode pular a auditoria** porque o handoff exige AUDIT_PASS (Skill 9)
5. **Ele não pode mentir** porque os logs brutos são verificáveis (Skill 8)
6. **Se falhar, o orquestrador intervém** com rollback automático (Orquestrador Nível 1-3)

O custo é velocidade. O ganho é **confiabilidade**. Para um framework que se orgulha de Zero Trust, esse é o trade-off correto.
