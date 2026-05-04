## Plano LEARNINGS v2 — Consolidado com todas as correções

Aqui está o plano atualizado, incorporando tudo que discutimos:

---

### O que mudou em relação ao plano original

| Ponto | Plano Original | Plano v2 |
|---|---|---|
| SSD_ERRORS_LEDGER | Não mencionado | Fonte 4 do aggregator |
| Formato do HARNESS_LOG | Regex inline assumido | Adaptado ao formato real (heading + Detalhe) |
| Mapeamento de checks | 9 checks | 11 checks (+epistemological, +journal_sam) |
| Glossários | Fase 4 | Fase 4 (inalterado) |
| Testes | Não previsto | Fase 2.12 — `tests/test_learnings.py` |
| Rollback | Não previsto | Backup do LEARNINGS.md antes de escrita |
| Métricas CONTEXT_HEALTH | Não previsto | Fase 4.7 — extensão do dashboard |

---

### PARTE 1: FUNDAMENTAÇÃO (inalterada)

#### 1.1. O Problema

O H.O.K Forge (v2.5.2) opera com um Harness Reativo (Fail-Closed). Quando uma execução falha, o agente corrige o mínimo necessário para passar no gate. O conhecimento gerado pela falha se perde. O framework não tem memória de longo prazo.

Cada execução começa do zero. Cada spec, cada harness run, cada validação é um evento isolado. Um desenvolvedor sênior tem "memória muscular" — já viu aquele padrão falhar antes, então aborda a situação de forma diferente. O H.O.K Forge não tem isso.

**Resultado:** os mesmos erros se repetem, as mesmas specs estouram o impact radius, os mesmos handoffs ficam malformados. O framework bloqueia, corrige, e esquece.

#### 1.2. O que LEARNINGS É (e o que NÃO é)

**LEARNINGS é:**
- A memória de longo prazo do framework
- Um documento vivo em `brain/` ao lado de RULES.md, PROMPT_LIBRARY.md, PRD.md
- Alimentado automaticamente a partir de artefatos que já existem, incluindo o SSD_ERRORS_LEDGER
- Injetado em cópia temporária da spec — o agente não precisa procurar, a memória já está no caminho

**LEARNINGS NÃO é:**
- Um substituto do SSD_ERRORS_LEDGER (LEDGER é tático, LEARNINGS é estratégico)
- Um pipeline de aprendizado de máquina
- Um engine de destilação
- Um sistema de RAG com embeddings
- Acoplado ao harness_runner.py (camada paralela)

#### 1.3. Princípios Fundadores

| Princípio | Descrição |
|---|---|
| **Memória, não máquina** | LEARNINGS é um documento, não um sistema. Conhecimento vive em Markdown. |
| **Injetado, não pedido** | O agente não é convidado a ler — a memória é injetada em cópia temporária da spec que ele já lê. |
| **Agentes leem, nunca escrevem** | O agente é consumidor de memória, nunca produtor. |
| **Camada paralela, nunca integrada** | LEARNINGS observa os mesmos artefatos que o harness, mas é independente. Relação produtor-consumidor. |
| **Humano decide, script propõe** | O script nunca modifica RULES.md ou PROMPT_LIBRARY.md diretamente. |
| **Esquecimento por ciclos, não por dias** | Padrões enfraquecem por inatividade em ciclos de execução, não por calendário. Projeto parado não enfraquece scars. |
| **Dados limpos desde a origem** | Conventional Commits + Husky garantem que o aggregator tenha dados parseáveis. |
| **Original intocável** | O spec.md versionado nunca é modificado. Injeção ocorre em cópia `.enriched.md`. |
| **Pipeline tático→estratégico** | LEDGER (`.specs/`) é a memória curta. LEARNINGS (`.context/brain/`) é a memória longa. Um alimenta o outro, mas nunca o contrário. |

#### 1.4. Origens da Convergência

| Fonte | Contribuição Principal | Status |
|---|---|---|
| **Gemini Flash** (Blueprint original) | Diagnóstico do problema, conceito Miner/Teacher/Optimizer | Conceito base, reformulado |
| **MiMo** (Arquitetura) | LEARNINGS como memória, camada paralela, injeção de memória, agentes nunca escrevem | Arquitetura final |
| **Qwen** (Auditoria) | Decay, Oracle gaps, circuit breaker, Spec-ID linking, prevention_snippet, triagem, scoring de relevância | 7 ideias filtradas, 3 aceitas integralmente, 4 adaptadas |
| **Flash** (Auditoria) | Cap de 5 scars, safe_parse_log(), F-LRN-005 | 3 correções, todas aceitas |
| **Codex** (Auditoria) | Cópia temporária, impacto estimado, schema versioning, triage ordering, SLO | 5 correções, todas aceitas |
| **Humano** (Correções) | Decay em ciclos, Conventional Commits já existe na prática, Few-Shot como futuro | 3 correções críticas aplicadas |

---

### PARTE 2: ARQUITETURA

#### 2.1. Visão Geral (atualizada com LEDGER)

```
┌──────────────────────────────────────────────────────────────────────┐
│                     ARTEFATOS EXISTENTES (Fontes)                     │
│                                                                       │
│  HARNESS_LOG.md   JOURNAL.md   wiki_log.md   git log   STATE.md     │
│                                                                       │
│  SSD_ERRORS_LEDGER.md  ← NOVA FONTE (memória tática curada)         │
└───────┬───────────────┬──────────────┬──────────────┬────────────────┘
        │               │              │              │
        └───────────────┴──────┬───────┴──────────────┘
                               │
                               ▼
              ┌──────────────────────────────────┐
              │    learnings_aggregator.py         │
              │                                  │
              │  Fonte 1: FAIL→SUCCESS diffs      │  (automático)
              │  Fonte 2: Oracle gaps (conf<0.5)  │  (automático)
              │  Fonte 3: Recorrências            │  (automático)
              │  Fonte 4: LEDGER entries          │  (importação)
              └──────────────┬───────────────────┘
                             │
                             ▼
              ┌──────────────────────────────────┐
              │       brain/LEARNINGS.md          │
              │                                  │
              │  ## Scars (cicatrizes)            │
              │  ## Oracle Gaps                   │
              │  ## Propostas de Regra            │
              │  ## Roadmap Futuro                │
              │  ## Índice                        │
              └──────────┬───────────────────────┘
                         │
                         ▼
              ┌──────────────────────────────────┐
              │      inject_learnings.py          │
              │                                  │
              │  Lê LEARNINGS.md + spec.md        │
              │  Calcula relevância (50/30/10)    │
              │  Top 5 scars → copia .enriched.md │
              └──────┬──────────────┬────────────┘
                     │              │
           ┌─────────┘              └─────────┐
           ▼                                  ▼
  ┌──────────────────┐              ┌──────────────────┐
  │   spec-driver    │              │  qa-validator    │
  │  lê .enriched.md │              │  lê .enriched.md │
  │  (original limpo)│              │  (original limpo)│
  └──────────────────┘              └──────────────────┘
```

#### 2.2. Relação com os Sistemas Existentes

| Sistema | Relação com LEARNINGS |
|---|---|
| `harness_runner.py` | **Produtor.** Gera HARNESS_LOG.md. Adiciona `check_learnings_completeness()` como WARN. Lógica interna inalterada. |
| `context_oracle.py` | **Produtor.** Gera wiki_log.md. LEARNINGS consome para Oracle gaps. Integração reversa adiada (F-LRN-002). |
| `SSD_ERRORS_LEDGER.md` | **Produtor (Fonte 4).** Memória tática curada pelo humano. O aggregator consome entradas com causa raiz preenchida como seeds para scars. Escrita no LEDGER pelo aggregator: **NUNCA**. |
| `spec-driver` | **Consumidor passivo.** Recebe caminho de `.enriched.md`. Não lê LEARNINGS.md diretamente. |
| `qa-validator` | **Consumidor passivo.** Recebe caminho de `.enriched.md`. Não lê LEARNINGS.md diretamente. |
| `cleanup_specs.py` | **Produtor.** Gera dados sobre specs arquivadas. LEARNINGS consome. **NOTA:** O LEDGER em `.specs/` está sujeito a este cleanup. Entradas do LEDGER devem ser consumidas pelo aggregator antes do arquivamento. |
| `workflow_journal_auditor.py` (SAM) | **Produtor.** Gera dados sobre inconsistências. LEARNINGS consome. |
| `SSD_PLAYBOOK.md` | **Referência de processo.** Define o ciclo das 9 Skills. A injeção de memória ocorre antes da Skill 6 (EVIDENCE_GENERATION). |
| `Husky` | **Guardião de dados limpos.** Hook commit-msg garante Conventional Commits. |

#### 2.3. Quatro Fontes de Dados

| Fonte | Automação | O que captura | Cobertura |
|---|---|---|---|
| **Agregador** (FAIL→SUCCESS) | 100% | Padrões de falha, diffs, recorrências | ~55% |
| **Agregador** (Oracle gaps) | 100% | Queries conf < 0.5, buracos na documentação | ~15% |
| **Agregador** (LEDGER import) | 100% | Causas raiz já curadas, erros já classificados | ~10% |
| **Humano** (triagem) | Manual | Validação de propostas, causas raiz residuais | ~20% |

---

### PARTE 3: ESPECIFICAÇÃO DOS ARTEFATOS

#### 3.1. `brain/LEARNINGS.md` — O Documento

**Localização:** `.context/brain/LEARNINGS.md`
**Domínio:** docs
**Formato:** Markdown

##### Template Completo

```markdown
# 🧠 LEARNINGS — Memória do H.O.K Forge

> **Versão:** 1.0
> **Ciclo atual:** #0
> **Última atualização:** [timestamp automático]
> **Total de cicatrizes:** [N]
> **Ativas:** [N] | **Dormentes:** [N] | **Resolvidas:** [N] | **Pendentes:** [N]

---

## Como Usar Este Documento

Este documento é lido automaticamente pelo sistema de injeção de memória.
As scars relevantes para cada spec são injetadas em cópia temporária
(.enriched.md) antes da execução. O spec.md original nunca é modificado.

Para triagem: `npm run context:learnings --triage`

---

## 📊 Estatísticas

| Métrica | Valor |
|---|---|
| Total de cicatrizes registradas | [N] |
| Ativas (< 20 ciclos) | [N] |
| Dormentes (>= 20 ciclos) | [N] |
| Resolvidas estruturalmente | [N] |
| Pendentes (FAIL sem SUCCESS) | [N] |
| Propostas de regra pendentes | [N] |
| Oracle gaps abertos | [N] |
| Importadas do LEDGER | [N] |

---

## 🩸 Scars — Cicatrizes de Execução

<!-- Gerado automaticamente por learnings_aggregator.py -->
<!-- Seções manuais entre <!-- MANUAL_START --> e <!-- MANUAL_END --> são preservadas -->

### Scar #001 — [Título descritivo]
- **ID:** SCAR-YYYY-MM-DD-NNN
- **Detectado em:** YYYY-MM-DD
- **Última ocorrência:** ciclo #N
- **Ciclos desde última ocorrência:** N
- **Threshold de decay:** 20 ciclos
- **Contagem:** N ocorrências
- **Status:** 🟢 Ativa / 💤 Dormente / ✅ Resolvida / 🔍 Pendente
- **Tipo:** Estrutural / Semântico / Comportamental
- **Impacto estimado:** Baixo / Médio / Alto
- **Spec afetada:** `.specs/features/[nome]/spec.md`
- **Check do harness:** [nome do check que falhou]
- **Padrão do erro:** [descrição objetiva do que falhou]
- **Correção aplicada:** [o que mudou entre o FAIL e o SUCCESS]
- **Linked commit:** [hash do commit que resolveu]
- **Diff relevante:** [trecho do git diff, max 10 linhas]
- **Prevention snippet:** [código preventivo, opcional, preenchido pelo humano]
- **Causa raiz:** [preenchido pelo humano, importado do LEDGER, ou "PENDENTE"]
- **Regra derivada:** [referência à regra em RULES.md, se aplicável]
- **Fonte:** [HARNESS_LOG | LEDGER | MANUAL]

<!-- MANUAL_START -->
<!-- Adicione observações manuais aqui. O script não toca esta seção. -->
<!-- MANUAL_END -->

---

## 🔍 Oracle Gaps — Lacunas de Conhecimento

<!-- Gerado automaticamente a partir de wiki_log.md -->

### Gap #001 — [Tópico sem cobertura]
- **ID:** GAP-YYYY-MM-DD-NNN
- **Detectado em:** YYYY-MM-DD
- **Fonte:** wiki_log.md
- **Queries relacionadas:** ["query 1", "query 2"]
- **Confiança média:** 0.XX
- **Arquivos consultados:** [lista]
- **Ação sugerida:** Criar `WIKI/concepts/[tópico].md`
- **Status:** 🔍 Aberto / ✅ Resolvido

---

## ⚠️ Propostas de Regra — Aguardando Decisão Humana

<!-- Gerado quando padrão se repete >= 3 vezes -->
<!-- NUNCA altera RULES.md diretamente -->

### Proposta #001 — [Regra sugerida]
- **ID:** PROP-YYYY-MM-DD-NNN
- **Gerada em:** YYYY-MM-DD
- **Baseada em:** Scar #N, #N, #N
- **Frequência:** N ocorrências do mesmo padrão
- **Regra sugerida:** Adicionar a RULES.md §[N]: "[texto]"
- **Justificativa:** [por que essa regra deveria existir]
- **Impacto estimado:** [checks do harness afetados]
- **Status:** 🔍 Aguardando / ✅ Aplicada / ❌ Rejeitada

---

## 🔮 Roadmap Futuro — Ideias Validadas, Aguardando Maturação

### F-LRN-001: LEARNINGS como Few-Shot Training Data
- **O que:** Estruturar scars no formato Context→Erro→Correção e usá-las
  como exemplos few-shot no PROMPT_LIBRARY.md automaticamente
- **Por que é valioso:** O agente aprende com exemplos reais do projeto,
  não com instruções genéricas
- **Por que não agora:** Depende de LEARNINGS.md populado com 20+ scars
  e validado por pelo menos 2 ciclos de maturação
- **Pré-requisitos:** LEARNINGS.md em produção, scars no formato C→E→C,
  mecanismo de injeção funcionando
- **Estimativa:** Fase 6+

### F-LRN-002: Integração Oracle ↔ LEARNINGS (Memória Just-in-Time)
- **O que:** Indexar LEARNINGS.md no Oracle para consulta seletiva de scars
- **Por que é valioso:** Quando LEARNINGS.md atingir 30+ scars, leitura
  direta gera context bloat
- **Por que não agora:** LEARNINGS.md começa pequeno (~2k tokens)
- **Pré-requisitos:** 30+ scars, Oracle v3 funcionando
- **Estimativa:** Fase 4+

### F-LRN-003: Bloqueio Rígido no Harness Gate (exit 1)
- **O que:** Transformar [WARN] em exit 1 no check_learnings_completeness()
- **Por que é valioso:** Força ciclo completo de memória, sem escape
- **Por que não agora:** Aggregator novo. Falso positivo é pior que falso negativo
- **Pré-requisitos:** Aggregator validado 30+ dias, taxa FP < 5%
- **Estimativa:** Fase 5+

### F-LRN-004: Detecção Automática de Resolução Estrutural
- **O que:** Script detecta refatoração do código fonte e marca scar como ✅ Resolvida
- **Por que é valioso:** Elimina intervenção humana para scars resolvidas organicamente
- **Por que não agora:** Complexo e frágil na v1
- **Pré-requisitos:** Maturidade do aggregator, histórico de diffs acumulado
- **Estimativa:** Fase 5+

### F-LRN-005: Subagente @memory-distiller
- **O que:** Subagente sugere causa raiz automaticamente. Humano apenas dá signoff.
- **Por que é valioso:** Reduz tempo de triagem humana em ~90%
- **Por que não agora:** Requer aggregator coletando diffs limpos e consistentes
- **Pré-requisitos:** Aggregator em produção, Conventional Commits maduro
- **Estimativa:** Fase 5+

---

## 📋 Índice de Scars

<!-- Atualizado automaticamente pelo aggregator -->

| ID | Título | Tipo | Impacto | Status | Última Ocorrência | Contagem | Fonte |
|---|---|---|---|---|---|---|---|
| SCAR-... | ... | ... | ... | 🟢/💤/✅/🔍 | ciclo #N | N | HARNESS/LEDGER/MANUAL |
```

#### 3.2. `.context/_scripts/learnings_aggregator.py` — O Script Principal

**Localização:** `.context/_scripts/learnings_aggregator.py`
**Domínio:** source
**Linguagem:** Python (stdlib-only)
**Linhas estimadas:** ~350

##### Contrato de Comportamento

| Aspecto | Especificação |
|---|---|
| **Input** | `HARNESS_LOG.md`, `JOURNAL.md`, `wiki_log.md`, `git log`, `SSD_ERRORS_LEDGER.md` |
| **Output** | Atualização atômica de `brain/LEARNINGS.md` |
| **Execução** | Sob demanda (`npm run context:learnings`) ou CI pós-merge |
| **Timeout** | 5 segundos. Se estourar, aborta com `[WARN]` |
| **SLO** | Sucesso > 99%, tempo p95 < 3s local. Loga performance ao final. |
| **Idempotência** | Rodar 2x não duplica. Cada scar tem ID único. |
| **Escrita atômica** | tempfile + os.replace(). Verifica mtime antes de escrever. |
| **Backup** | Copia LEARNINGS.md para `.context/brain/LEARNINGS.md.bak` antes de sobrescrever. |
| **Regras imutáveis** | NUNCA modifica nada em `brain/` exceto `LEARNINGS.md`. NUNCA modifica `SSD_ERRORS_LEDGER.md`. |
| **Preservação manual** | Seções entre `<!-- MANUAL_START -->` e `<!-- MANUAL_END -->` são preservadas. |
| **Modo triagem** | Flag `--triage` imprime scars PENDENTE ordenadas por recorrência × recência × impacto. |
| **Resiliência** | `safe_parse_log()` com validação de sanidade. Drift de schema reporta explicitamente. |

##### Lógica Interna (atualizada com Fonte 4)

```
FUNÇÃO PRINCIPAL:
  1. Verificar schema version do HARNESS_LOG.md
     → Se header <!-- HARNESS_LOG_SCHEMA: X.Y --> não confere → [WARN] e abortar

  2. Incrementar contador de ciclo no cabeçalho de LEARNINGS.md

  3. Parsear HARNESS_LOG.md via safe_parse_log()
     → Extrair [HARNESS-FAIL] e [HARNESS-PASS]
     → Para cada FAIL: spec, detalhe, timestamp
     → NOTA: Formato real é heading + Detalhe, não inline.
       Regex deve capturar:
         ## [HARNESS-FAIL] Report | spec:(.+)
         - \*\*Detalhe:\*\* (.+)

  4. Para cada FAIL, buscar SUCCESS correspondente
     → Prioridade 1: git log com [Spec: feature_nome]
     → Prioridade 2: commits entre timestamp do FAIL e próximo PASS da mesma spec
     → Se encontrado: extrair git diff
     → Se NÃO: registrar como scar "🔍 Pendente"

  5. Calcular impacto estimado para cada scar
     → FAIL que bloqueou commit (exit 1) → Alto
     → FAIL que foi WARN → Médio
     → SCOPE_BLOWOUT → Alto
     → Outros → Baixo

  6. Parsear wiki_log.md via safe_parse_log()
     → Queries com mode=QUERY e status=FAIL (conf < 0.5)
     → Agrupar por tópico raiz (stemming via STEM_WHITELIST)
     → Se grupo >= 2: gerar Oracle Gap

  7. Parsear SSD_ERRORS_LEDGER.md (FONTE 4 - NOVO)
     → Extrair entradas com campos: Data, Feature, Causa raiz, Correção
     → Para cada entrada do LEDGER:
       → Buscar scar correspondente no LEARNINGS por feature + tipo de erro
       → Se existe: enriquecer root_cause se estiver PENDENTE
       → Se não existe: criar scar nova com root_cause pre-preenchido
       → Marcar campo Fonte como "LEDGER"
     → NUNCA escrever no LEDGER

  8. Verificar recorrências
     → Agrupar scars por check + error_pattern
     → Se grupo >= 3: gerar Proposta de Regra

  9. Aplicar decay por ciclos
     → ciclos_since = ciclo_atual - ciclo_última_ocorrência
     → Se ciclos_since >= 20 E tipo != Estrutural → 💤 Dormente
     → Se humano marcou ✅ → manter

  10. Backup + Escrita atômica de LEARNINGS.md
      → Copiar para .bak
      → Verificar mtime
      → Se mudou → abortar: "[WARN] Concorrência detectada"
      → tempfile + os.replace()
      → Preservar seções manuais

  11. Log de performance
      → "[OK] learnings_aggregator: N scars, N gaps, N propostas, N do LEDGER.
         Tempo: X.Xs. Ciclo #N."
```

##### safe_parse_log()

```python
def safe_parse_log(log_path, pattern, pattern_name):
    """Parse resiliente com validação de sanidade."""
    try:
        text = log_path.read_text(encoding="utf-8")
        matches = re.findall(pattern, text)

        if text.strip() and not matches:
            print(f"[WARN] {pattern_name}: Log tem {len(text)} chars mas "
                  f"regex não capturou entradas. Formato pode ter mudado.")
            print(f"[WARN] Amostra (200 chars): {text[:200]}")
            return []

        return matches

    except FileNotFoundError:
        print(f"[WARN] {pattern_name}: Arquivo não encontrado: {log_path}")
        return []
    except Exception as e:
        print(f"[WARN] {pattern_name}: Erro inesperado: {e}")
        return []
```

##### Regex Chave (adaptados ao formato real)

```python
# Formato real do log_harness():
#   ## [HARNESS-FAIL] Report | spec:nome
#   - **Detalhe:** texto
FAIL_HEADING = r'##\s*\[HARNESS-FAIL\]\s*Report\s*\|\s*spec:\s*(.+?)\s*$'
FAIL_DETAIL = r'-\s*\*\*Detalhe:\*\*\s*(.+)'
PASS_HEADING = r'##\s*\[HARNESS-PASS\]\s*Report\s*\|\s*spec:\s*(.+?)\s*$'

# Para vinculação com git
SPEC_ID_PATTERN = r'\[Spec:\s*(.+?)\]'

# Para LEDGER (formato: ### 2026-04-30 | feature | sprint)
LEDGER_ENTRY = r'###\s*(\d{4}-\d{2}-\d{2})\s*\|\s*(.+?)\s*\|\s*(.+?)\s*$'
LEDGER_FIELD = r'-\s*(Erro|Causa raiz|Correcao aplicada|Feature):\s*(.+)'
```

##### Estrutura de Dados de uma Scar (atualizada)

```python
scar = {
    "id": "",                    # SCAR-YYYY-MM-DD-NNN
    "title": "",                 # Gerado a partir do check + tipo de falha
    "detected_at": "",           # Data do primeiro FAIL
    "last_occurrence_cycle": 0,  # Ciclo da última ocorrência
    "cycles_since": 0,           # Ciclos desde última ocorrência
    "decay_threshold": 20,       # Ciclos para dormir
    "count": 0,                  # Número de ocorrências
    "status": "active",          # active | dormant | resolved | pending
    "type": "",                  # structural | semantic | behavioral
    "impact": "medium",          # low | medium | high
    "spec": "",                  # Caminho da spec afetada
    "check": "",                 # Nome do check do harness
    "error_pattern": "",         # Descrição extraída do "Detalhe"
    "fix_applied": "",           # Descrição da correção
    "linked_commit": "",         # Hash do commit que resolveu
    "diff_snippet": "",          # Trecho relevante do diff (max 10 linhas)
    "prevention_snippet": "",    # Código preventivo (opcional, manual)
    "root_cause": "PENDENTE",    # Preenchido pelo humano ou importado do LEDGER
    "derived_rule": "",          # Referência à regra se existir
    "source": "HARNESS_LOG",     # HARNESS_LOG | LEDGER | MANUAL (NOVO)
}
```

##### Mapeamento Fonte → Tipo de Cicatriz (atualizado)

| Fonte de Dados | Tipo | Decay | Impacto Padrão |
|---|---|---|---|
| `check_schema_contract()` | Estrutural | Nunca decai | Alto |
| `check_sprint_contract()` | Estrutural | Nunca decai | Alto |
| `check_version_consistency()` | Estrutural | Nunca decai | Alto |
| `check_handoff_integrity()` | Comportamental | 20 ciclos | Médio |
| `check_strategic_alignment()` | Semântico | 20 ciclos | Médio |
| `check_enrichment_integrity()` | Semântico | 20 ciclos | Médio |
| `check_impact_radius()` | Comportamental | 20 ciclos | Alto |
| `check_journal_sam()` | Comportamental | 20 ciclos | Médio |
| `check_epistemological_gate()` | Semântico | 20 ciclos | Baixo |
| `check_learnings_completeness()` | Comportamental | 20 ciclos | Baixo |
| `spec-driver: SCOPE_BLOWOUT` | Comportamental | 20 ciclos | Alto |
| `context_oracle: conf < 0.5` | Gap | Até criação doc | Baixo |
| `cleanup_specs: arquivamento` | Comportamental | 20 ciclos | Baixo |
| `SSD_ERRORS_LEDGER: entrada` | Importação | 20 ciclos | Conforme LEDGER |

##### Modo Triage — Ordenação

```
Score = (contagem × 2) + (recência × 1.5) + (impacto × 3)

Onde:
  contagem = número de ocorrências
  recência = 1 / ciclos_since_last
  impacto  = Alto=3, Médio=2, Baixo=1

Ordenação: score descendente (mais urgente primeiro)
Limite: 3 scars por execução do triage
```

#### 3.3. `.context/_scripts/inject_learnings.py` — O Injetor de Memória

**Localização:** `.context/_scripts/inject_learnings.py`
**Domínio:** source
**Linguagem:** Python (stdlib-only)
**Linhas estimadas:** ~100

##### Contrato de Comportamento

| Aspecto | Especificação |
|---|---|
| **Input** | `brain/LEARNINGS.md` + caminho do `spec.md` |
| **Output** | Arquivo `.enriched.md` (cópia temporária). **spec.md original nunca é modificado.** |
| **Execução** | Antes de cada invocação do spec-driver (antes da Skill 6 do SSD_PLAYBOOK) |
| **Timeout** | 2 segundos |
| **Cap** | Máximo 5 scars injetadas por spec |
| **Scoring** | Feature: +50, Check: +30, Keyword: +10 cada |
| **Ordenação** | Score descendente. Empates: mais recente primeiro. |
| **Limpeza** | `.enriched.md` é deletado após execução do spec-driver |
| **Fallback** | Se LEARNINGS.md não existe ou está vazio → retorna spec original sem cópia |

##### Fluxo

```
FUNÇÃO inject(spec_path):
  1. Ler LEARNINGS.md
     → Se não existir ou vazio → retornar spec_path original

  2. Ler spec.md
     → Extrair frontmatter YAML (entre --- e ---)
     → Extrair corpo do documento

  3. Para cada scar ativa em LEARNINGS.md:
     → Calcular score de relevância:
         feature name na spec:      +50 pontos
         check name na spec:        +30 pontos
         keyword do error_pattern:  +10 pontos cada (len > 3)
     → Se score > 0: adicionar à lista candidata

  4. Se lista não está vazia:
     → Ordenar por score descendente, empate por data mais recente
     → Cortar em 5 (cap máximo)
     → Gerar bloco de memória formatado
     → Criar spec_path.enriched.md com:
         - Frontmatter YAML original
         - Bloco de memória demarcado
         - Corpo original da spec
     → Retornar caminho do .enriched.md

  5. Se lista está vazia:
     → Retornar spec_path original (sem cópia)
```

##### Formato do Bloco Injetado

```markdown
<!-- LEARNINGS_INJECTION: auto-gerado, não editar -->
## ⚠️ MEMÓRIA DO FRAMEWORK (auto-injetado)

Scars ativas relevantes para esta spec:

**[Scar #003] schema_contract: missing_column** | Impacto: Alto | Fonte: HARNESS_LOG
Última ocorrência: ciclo #42 | Ocorrências: 3x
Correção: Adicionar migration antes do código
→ Verifique schema.sql ANTES de codar

**[Scar #007] impact_radius: scope_blowout** | Impacto: Alto | Fonte: LEDGER
Última ocorrência: ciclo #38 | Ocorrências: 2x
Causa raiz: Spec não foi fragmentada antes da execução
→ Se diff > 5 arquivos, re-avalie o escopo

<!-- /LEARNINGS_INJECTION -->
```

#### 3.4. Atualização do `harness_runner.py`

**Arquivo:** `.context/_scripts/harness_runner.py`
**Função a adicionar:** `check_learnings_completeness()`
**Linhas adicionadas:** ~25
**Comportamento:** `[WARN]` sempre (nunca exit 1 na v1)

```python
def check_learnings_completeness(spec_path: Path):
    """Verifica se memória do LEARNINGS está completa para esta spec.
    v1: retorna WARN. Ver F-LRN-003 para endurecimento futuro."""
    learnings_path = CONTEXT_DIR / "brain" / "LEARNINGS.md"
    harness_log_path = CONTEXT_DIR / "maintenance" / "HARNESS_LOG.md"
    aggregator_script = CONTEXT_DIR / "_scripts" / "learnings_aggregator.py"

    if not aggregator_script.exists():
        return True, "Aggregator ausente (skip)"

    if not learnings_path.exists():
        return True, "[WARN] LEARNINGS.md ausente. Rode: npm run context:learnings"

    if not harness_log_path.exists():
        return True, "HARNESS_LOG.md ausente (skip)"

    log_text = harness_log_path.read_text(encoding="utf-8")
    spec_name = spec_path.parent.name

    fail_count = len(re.findall(
        rf'\[HARNESS-FAIL\].*?spec:.*?{re.escape(spec_name)}',
        log_text, re.I
    ))

    if fail_count == 0:
        return True, "Sem histórico de falhas (skip)"

    learnings_text = learnings_path.read_text(encoding="utf-8")
    if spec_name.lower() not in learnings_text.lower():
        return True, (
            f"[WARN] Spec '{spec_name}' tem {fail_count} falha(s) no histórico "
            f"mas nenhuma cicatriz registrada. Execute: npm run context:learnings"
        )

    return True, "Memória completa"
```

**Adição ao HARNESS_LOG.md:** Schema version header

```markdown
<!-- HARNESS_LOG_SCHEMA: 1.0 -->
```

#### 3.5. Hook Husky: `.husky/commit-msg`

**Arquivo:** `.husky/commit-msg`
**Tipo:** Shell script

```bash
#!/bin/sh
# Validação de Conventional Commits
# Formato: tipo(escopo): descrição

COMMIT_MSG=$(cat "$1")
PATTERN="^(feat|fix|chore|docs|refactor|test|maint)(\(.+\))?:\s.{10,}"

if ! echo "$COMMIT_MSG" | grep -qE "$PATTERN"; then
  echo "❌ Commit message inválido."
  echo "Formato obrigatório: tipo(escopo): descrição"
  echo "Tipos válidos: feat, fix, chore, docs, refactor, test, maint"
  echo "Exemplo: fix(schema): adiciona tabela users [Spec: feature_checkout]"
  exit 1
fi
```

#### 3.6. Adição ao `brain/RULES.md`

```markdown
## §1.4 Conventional Commits

Toda mensagem de commit DEVE seguir o padrão:
  `tipo(escopo): descrição`

Tipos válidos: feat, fix, chore, docs, refactor, test, maint
O campo [Spec: feature_nome] é RECOMENDADO para commits que afetam specs ativas.
Obrigatório para commits do tipo fix que resolvem falhas de harness.

Exemplos:
  fix(schema): adiciona tabela users [Spec: feature_checkout]
  feat(oracle): indexa LEARNINGS.md [Spec: oracle_v3]
  chore(ci): atualiza workflow de health check
  docs(learnings): preenche causa raiz da Scar #003
```

#### 3.7. Adição ao `package.json`

```json
"context:learnings": "python .context/_scripts/learnings_aggregator.py",
"context:learnings:triage": "python .context/_scripts/learnings_aggregator.py --triage",
"context:inject": "python .context/_scripts/inject_learnings.py"
```

---

### PARTE 4: MECANISMOS

#### 4.1. Decay por Ciclos

| Regra | Descrição |
|---|---|
| **Contador de ciclos** | Cabeçalho do LEARNINGS.md: `Ciclo atual: #N`. Incrementa pós-commit válido. |
| **Ativa** | `ciclos_since_last < 20` |
| **Dormente** | `ciclos_since_last >= 20` e tipo != Estrutural |
| **Resolvida** | Humano marca OU script detecta refatoração (F-LRN-004) |
| **Pendente** | FAIL sem SUCCESS correspondente |
| **Estruturais** | Nunca decaem |
| **Projeto parado** | Contador não avança. Nenhum enfraquecimento fantasma. |

#### 4.2. Injeção de Memória

| Aspecto | Especificação |
|---|---|
| **Quando** | Antes de cada invocação do spec-driver (antes da Skill 6 do SSD_PLAYBOOK) |
| **Como** | `inject_learnings.py` cria `.enriched.md` (cópia temporária) |
| **Original** | Nunca é modificado |
| **Scoring** | Feature: +50, Check: +30, Keyword: +10 |
| **Cap** | Máximo 5 scars |
| **Demarcação** | `<!-- LEARNINGS_INJECTION -->` / `<!-- /LEARNINGS_INJECTION -->` |
| **Reversibilidade** | Bloco pode ser removido por regex limpa |
| **Performance** | Timeout de 2 segundos |
| **Fallback** | Se LEARNINGS vazio → spec original sem cópia |

#### 4.3. Vinculação FAIL→SUCCESS

| Prioridade | Método | Confiabilidade |
|---|---|---|
| 1ª | `git log` com `[Spec: feature_nome]` | Alta |
| 2ª | Commits entre timestamps (FAIL→PASS da mesma spec) | Média |
| 3ª | Scar sem diff, `fix_applied: "NÃO EXTRAÍVEL"` | Baixa (pendente) |

#### 4.4. Pipeline LEDGER → LEARNINGS (NOVO)

| Aspecto | Especificação |
|---|---|
| **Direção** | LEDGER → LEARNINGS apenas. Nunca o contrário. |
| **Quando** | A cada execução do aggregator |
| **O que consome** | Entradas do LEDGER com campo "Causa raiz" preenchido |
| **Match** | Por feature name + tipo de erro (heurística textual) |
| **Se há match** | Enriquece `root_cause` da scar existente se estiver PENDENTE |
| **Se não há match** | Cria scar nova com `root_cause` pre-preenchido, `source: LEDGER` |
| **Se duplica** | Enriquece scar existente (não cria cópia) |
| **Impacto no LEDGER** | Zero. Nenhuma escrita. Nenhuma modificação. |
| **Risco do cleanup** | LEDGER em `.specs/` está sujeito a arquivamento por 48h. Aggregator deve consumir antes. |

#### 4.5. Propostas de Regra

| Aspecto | Especificação |
|---|---|
| **Trigger** | Mesmo padrão >= 3 vezes (incluindo padrões vindos do LEDGER) |
| **Output** | Seção "Propostas de Regra" no LEARNINGS.md |
| **Script** | NUNCA altera RULES.md |
| **Humano** | Revisa, aplica em RULES.md se concorda |

#### 4.6. Triagem Humana

| Aspecto | Especificação |
|---|---|
| **Comando** | `npm run context:learnings --triage` |
| **Output** | Scars com `root_cause: PENDENTE` |
| **Ordenação** | Recorrência × Recência × Impacto |
| **Limite** | 3 scars por execução |
| **Tempo** | ~30 segundos por scar |

#### 4.7. Segurança

| Risco | Mitigação |
|---|---|
| Script modifica RULES.md/PROMPT_LIBRARY.md | Hardcoded: só escreve em LEARNINGS.md. Tentativa em outro path = erro fatal. |
| Script modifica SSD_ERRORS_LEDGER.md | Hardcoded: só lê do LEDGER, nunca escreve. |
| LEARNINGS.md cresce infinitamente | Decay + arquivamento. 60+ ciclos → arquivo histórico (ID + título + data). |
| Parsing frágil de logs | `safe_parse_log()` com validação de sanidade. Drift reportado explicitamente. |
| Formato do HARNESS_LOG mudou | Header `<!-- HARNESS_LOG_SCHEMA: 1.0 -->`. Aggregator verifica antes de parsear. Regex adaptado ao formato real (heading + Detalhe). |
| Agentes ignoram memória | Injeção automática em `.enriched.md`. Agente não precisa procurar. |
| Duplicação | ID único (data + sequência). Verificação antes de inserir. |
| Concorrência CI + local | Escrita atômica (tempfile + os.replace). Verificação mtime. Aborta se mudou. |
| Corrupção do LEARNINGS.md | Backup (.bak) antes de cada escrita atômica. |
| Performance | Timeout: 5s aggregator, 2s injector. Aborta silenciosamente. |
| Loop de culpa | `check_learnings_completeness()` retorna WARN (nunca exit 1). |
| LEDGER arquivado antes de consumir | Aggregator roda no CI pós-merge (antes do cleanup de 48h). |
| Ruído no git diff | spec.md original nunca é modificado. `.enriched.md` é temporário. |

---

### PARTE 5: FLUXOS DE TRABALHO

#### 5.1. Fluxo de Geração (Automático)

```
1. Desenvolvedor executa feature
2. inject_learnings.py → cria spec.md.enriched (máx 5 scars, scoring 50/30/10)
3. spec-driver lê spec.md.enriched (original intocado)
4. qa-validator lê spec.md.enriched (original intocado)
5. harness_runner valida contratos + check_learnings_completeness() [WARN]
6. Commit (Husky valida Conventional Commit)
7. spec.md.enriched é deletado
8. CI pós-merge: npm run context:learnings
9. Aggregator:
   a. Verifica schema version do log
   b. Incrementa ciclo
   c. Parseia HARNESS_LOG.md (safe_parse_log, formato heading)
   d. Vincula FAIL→SUCCESS (Spec-ID → fallback timestamp → pendente)
   e. Calcula impacto estimado
   f. Extrai diff → gera/atualiza scar
   g. Parseia wiki_log.md → Oracle gaps
   h. Parseia SSD_ERRORS_LEDGER.md → importa causas raiz (Fonte 4)
   i. Verifica recorrências → propostas de regra
   j. Aplica decay por ciclos
   k. Backup + Escrita atômica (mtime check)
   l. Log de performance
```

#### 5.2. Fluxo de Consulta (Transparente para o Agente)

```
1. Hub invoca spec-driver para uma spec
2. inject_learnings.py roda automaticamente
3. Calcula relevância de cada scar (50/30/10)
4. Top 5 scars → injeta em cópia .enriched.md
5. spec-driver recebe caminho de .enriched.md
6. spec-driver lê a spec — memória já está lá
7. Se pattern coincide com scar → aplica correção preventivamente
8. Após execução → .enriched.md deletado
```

#### 5.3. Fluxo de Triagem Humana

```
1. npm run context:learnings --triage
2. Terminal:
   === TRIAGEM DE LEARNINGS ===
   Pendentes de causa raiz: 3 (ordenadas por urgência)

   [1] Scar #015 — schema_contract: missing_column
       Impacto: Alto | Ocorrências: 3 | Ciclo: #55
       Fonte: HARNESS_LOG
       Correção: Adicionada tabela users no migration 002
       → Causa raiz: ______

   [2] Scar #012 — impact_radius: scope_blowout
       Impacto: Alto | Ocorrências: 2 | Ciclo: #52
       Fonte: LEDGER (causa raiz pré-importada)
       Causa raiz: Spec não fragmentada antes da execução
       → Verificar se regra derivada é necessária

3. Humano edita LEARNINGS.md, preenche/valida root_cause
4. Humano avalia "Propostas de Regra"
5. Aplica em RULES.md se concorda → marca ✅ ou ❌
```

#### 5.4. Fluxo de Proteção (Gate do Harness)

```
1. check_learnings_completeness() é chamado
2. Aggregator não existe → skip
3. LEARNINGS.md não existe → [WARN]
4. Spec teve FAILs mas não tem cicatriz → [WARN]
5. Tudo OK → "Memória completa"
6. Na v1: nenhum cenário resulta em exit 1
```

---

### PARTE 6: PLANO DE IMPLEMENTAÇÃO

#### Fase 1: Fundação (Semana 1)

| # | Tarefa | Artefato | Esforço |
|---|---|---|---|
| 1.1 | Criar template do LEARNINGS.md | `brain/LEARNINGS.md` | Baixo |
| 1.2 | Analisar HARNESS_LOG.md e JOURNAL.md existentes | - | Médio |
| 1.3 | Analisar SSD_ERRORS_LEDGER.md para seeds iniciais | - | Médio |
| 1.4 | Preencher primeiras 3-5 cicatrizes retroativamente (incluindo imports do LEDGER) | `brain/LEARNINGS.md` | Médio |
| 1.5 | Formalizar Conventional Commits | `brain/RULES.md` (+§1.4) | Baixo |
| 1.6 | Criar hook commit-msg | `.husky/commit-msg` | Baixo |
| 1.7 | Adicionar schema version ao HARNESS_LOG.md | `HARNESS_LOG.md` (header) | Baixo |
| 1.8 | Adicionar scripts npm | `package.json` (+3 linhas) | Baixo |

**Entregável:** LEARNINGS.md com cicatrizes reais (incluindo seeds do LEDGER). Conventional Commits ativo. Husky validando. Schema version no log.

**Critério de sucesso:** LEARNINGS.md contém >= 3 scars do histórico real, pelo menos 1 importada do LEDGER. Commits inválidos bloqueados pelo Husky.

#### Fase 2: Automação do Aggregator (Semana 2)

| # | Tarefa | Artefato | Esforço |
|---|---|---|---|
| 2.1 | Criar learnings_aggregator.py | `.context/_scripts/learnings_aggregator.py` | Alto |
| 2.2 | Implementar safe_parse_log() | `learnings_aggregator.py` | Médio |
| 2.3 | Implementar vinculação FAIL→SUCCESS (Spec-ID + fallback) | `learnings_aggregator.py` | Médio |
| 2.4 | Implementar cálculo de impacto estimado | `learnings_aggregator.py` | Baixo |
| 2.5 | Implementar detecção de Oracle gaps | `learnings_aggregator.py` | Médio |
| 2.6 | Implementar importação do LEDGER (Fonte 4) | `learnings_aggregator.py` | Médio |
| 2.7 | Implementar decay por ciclos | `learnings_aggregator.py` | Médio |
| 2.8 | Implementar detecção de propostas de regra | `learnings_aggregator.py` | Médio |
| 2.9 | Implementar modo --triage (ordenado por urgência) | `learnings_aggregator.py` | Baixo |
| 2.10 | Implementar backup + escrita atômica + mtime + log de performance | `learnings_aggregator.py" | Baixo |
| 2.11 | Adaptar regex ao formato real do HARNESS_LOG (heading + Detalhe) | `learnings_aggregator.py` | Médio |
| 2.12 | Testar com dados reais | - | Médio |
| 2.13 | Validar idempotência | - | Baixo |
| 2.14 | Criar testes | `tests/test_learnings.py` | Médio |

**Entregável:** Script funcional. `npm run context:learnings` roda sem erros.

**Critério de sucesso:** Gera scars reais. Rodar 2x não duplica. Timeout 5s respeitado. Log de performance presente. Importa pelo menos 1 entrada do LEDGER. Testes passam.

#### Fase 3: Injeção de Memória (Semana 2-3)

| # | Tarefa | Artefato | Esforço |
|---|---|---|---|
| 3.1 | Criar inject_learnings.py | `.context/_scripts/inject_learnings.py` | Médio |
| 3.2 | Implementar scoring de relevância (50/30/10) | `inject_learnings.py` | Médio |
| 3.3 | Implementar cap de 5 scars | `inject_learnings.py` | Baixo |
| 3.4 | Implementar criação de .enriched.md (cópia temporária) | `inject_learnings.py` | Médio |
| 3.5 | Integrar injeção no fluxo de execução (antes da Skill 6) | `run_context.py` / `MASTER_FLOW.md` | Médio |
| 3.6 | Adicionar check_learnings_completeness() | `harness_runner.py` | Baixo |
| 3.7 | Testar fluxo completo end-to-end | - | Médio |

**Entregável:** Memória injetada automaticamente em cópia temporária. Original nunca é tocado.

**Critério de sucesso:** `.enriched.md` contém scars relevantes (max 5). Original inalterado. `.enriched.md` deletado após execução. Agentes incorporam correções preventivas.

#### Fase 4: Refinamento (Semana 3-4)

| # | Tarefa | Artefato | Esforço |
|---|---|---|---|
| 4.1 | Primeira triagem humana (`--triage`) | `brain/LEARNINGS.md` | Baixo |
| 4.2 | Preencher causas raiz pendentes | `brain/LEARNINGS.md` | Médio |
| 4.3 | Avaliar propostas de regra | `brain/RULES.md` + `LEARNINGS.md` | Médio |
| 4.4 | Ajustar thresholds de decay se necessário | `learnings_aggregator.py` | Baixo |
| 4.5 | Documentar no SCRIPT_GLOSSARY.md | `brain/SCRIPT_GLOSSARY.md` | Baixo |
| 4.6 | Documentar no FILE_GLOSSARY.md | `brain/FILE_GLOSSARY.md` | Baixo |
| 4.7 | Adicionar métricas de LEARNINGS ao CONTEXT_HEALTH.md | `monitoring/CONTEXT_HEALTH.md` | Baixo |

**Entregável:** Sistema refinado com curadoria humana aplicada.

**Critério de sucesso:** >= 50% scars com causa raiz. Propostas avaliadas. Glossários atualizados. Dashboard estendido.

#### Fase 5: Validação End-to-End (Semana 4)

| # | Tarefa | Artefato | Esforço |
|---|---|---|---|
| 5.1 | Rodar ciclo completo: feature → scar → injeção → prevenção | - | Médio |
| 5.2 | Validar que agentes não escapam da memória | - | Médio |
| 5.3 | Validar que aggregator não duplica, corrompe ou estoura timeout | - | Médio |
| 5.4 | Validar pipeline LEDGER → LEARNINGS | - | Médio |
| 5.5 | Validar Conventional Commits | - | Baixo |
| 5.6 | Coletar métricas de sucesso | - | Médio |

**Entregável:** LEARNINGS em produção, validado end-to-end.

**Critério de sucesso:** Redução de erros repetidos detectável. Nenhum falso positivo bloqueou commits. Performance dentro do SLO. Pipeline LEDGER → LEARNINGS funcionando.

---

### PARTE 7: MÉTRICAS DE SUCESSO

| Métrica | Como Medir | Meta |
|---|---|---|
| Redução de erros repetidos | Scars com mesmo check+pattern antes vs depois | -50% em 30 dias |
| Cobertura de memória | Scars ativas / total de FAILs no HARNESS_LOG | > 80% |
| Tempo de preenchimento | Latência FAIL → registro da scar | < 1 min (automático) |
| Prevenção detectável | Correções preventivas visíveis no git diff | Presença detectável |
| Propostas aceitas | Propostas ✅ / total | > 50% |
| Taxa de triagem | Scars com causa raiz / total | > 50% |
| Importação LEDGER | Scars com `source: LEDGER` / total scars do LEDGER | > 80% |
| Falsos positivos do gate | Commits bloqueados indevidamente | 0 (WARN na v1) |
| SLO do aggregator | Sucesso > 99%, p95 < 3s | Conforme log |

---

### PARTE 8: ARQUIVOS A CRIAR/MODIFICAR

| # | Ação | Arquivo | Tipo | Fase |
|---|---|---|---|---|
| 1 | **CRIAR** | `.context/brain/LEARNINGS.md` | Documento | 1 |
| 2 | **CRIAR** | `.context/_scripts/learnings_aggregator.py` | Script | 2 |
| 3 | **CRIAR** | `.context/_scripts/inject_learnings.py` | Script | 3 |
| 4 | **CRIAR** | `.husky/commit-msg` | Hook | 1 |
| 5 | **CRIAR** | `tests/test_learnings.py` | Testes | 2 |
| 6 | **MODIFICAR** | `brain/RULES.md` | Documento (+§1.4) | 1 |
| 7 | **MODIFICAR** | `.context/_scripts/harness_runner.py` | Script (+25 linhas + schema header) | 3 |
| 8 | **MODIFICAR** | `package.json` | Config (+3 linhas) | 1 |
| 9 | **MODIFICAR** | `brain/SCRIPT_GLOSSARY.md` | Documento | 4 |
| 10 | **MODIFICAR** | `brain/FILE_GLOSSARY.md` | Documento | 4 |
| 11 | **MODIFICAR** | `monitoring/CONTEXT_HEALTH.md` | Documento (métricas LEARNINGS) | 4 |
| 12 | **OBSERVAR** | `.specs/features/SSD_ERRORS_LEDGER.md` | Fonte (não modificar) | 1 |

**Total: 5 artefatos novos, 6 modificações, 1 observação.**

---

### PARTE 9: ROADMAP FUTURO

| ID | Item | Pré-requisitos | Estimativa |
|---|---|---|---|
| **F-LRN-001** | LEARNINGS como Few-Shot Training Data | 20+ scars, formato C→E→C, injeção funcionando | Fase 6+ |
| **F-LRN-002** | Integração Oracle ↔ LEARNINGS | 30+ scars, Oracle v3 funcionando | Fase 4+ |
| **F-LRN-003** | Bloqueio rígido no Harness Gate (exit 1) | Aggregator validado 30+ dias, FP < 5% | Fase 5+ |
| **F-LRN-004** | Detecção automática de resolução estrutural | Maturidade do aggregator | Fase 5+ |
| **F-LRN-005** | Subagente @memory-distiller | Aggregator em produção, Conventional Commits maduro | Fase 5+ |

---

### PARTE 10: REGISTRO DE DECISÕES ARQUITETURAIS

| # | Decisão | Alternativa Rejeitada | Rationale |
|---|---|---|---|
| D-01 | Camada paralela (não integrada ao harness) | Integrar no harness_runner | Separar validação de aprendizado. Preserva zero-trust e performance do gate. |
| D-02 | LEARNINGS como documento Markdown | JSONL, banco de dados, embeddings | Agentes leem Markdown. Complexidade desnecessária para v1. |
| D-03 | Injeção em cópia temporária (.enriched.md) | Modificar spec.md original | Evita ruído no git diff, poluição de revisão, reset do timer de cleanup_specs. |
| D-04 | Decay por ciclos, não por dias | Decay por calendário | Projeto parado não deve enfraquecer scars. |
| D-05 | Agentes nunca escrevem LEARNINGS | Depender de agentes para preencher | Agentes preguiçosos não cooperam. Memória se constrói sozinha. |
| D-06 | Gate em WARN na v1, exit 1 no futuro | Bloquear desde o início | Falso positivo é pior que falso negativo com aggregator novo. |
| D-07 | Scoring numérico (50/30/10) | Tiers qualitativos (forte/médio/fraco) | Determinístico. Sem ambiguidade no corte de 5 scars. |
| D-08 | safe_parse_log() com validação de sanidade | Regex puro com fallback silencioso | Drift de formato deve ser detectado, não ignorado. |
| D-09 | Schema version nos logs | Sem versionamento | Aggregator precisa saber se o formato mudou antes de parsear. |
| D-10 | Pipeline LEDGER → LEARNINGS (leitura, nunca escrita) | Absorver LEDGER no LEARNINGS | LEDGER é tático (`.specs/`), LEARNINGS é estratégico (`brain/`). Separar camadas. Importar dados, não duplicar funções. |
| D-11 | Backup antes de escrita atômica | Confiar apenas em tempfile + os.replace | Lógica errada do próprio script pode corromper. Rollback é trivial. |
| D-12 | Regex adaptado ao formato real do HARNESS_LOG | Assumir formato inline | Formato real usa heading + Detalhe, não pipe-separated inline. |

---

Fim do plano. Tudo consolidado. LEDGER integrado. Formato real respeitado. Nada esquecido. 
