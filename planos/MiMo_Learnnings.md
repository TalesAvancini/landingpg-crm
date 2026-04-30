# Plano Ultra Completo: LEARNINGS — A Memória do H.O.K Forge

---

## PARTE 1: FUNDAMENTAÇÃO

### 1.1. O Problema que Estamos Resolvendo

O H.O.K Forge (v2.5.2) opera com um Harness Reativo (Fail-Closed). Quando uma execução falha, o agente corrige o mínimo necessário para passar no gate. O conhecimento gerado pela falha se perde. O framework não tem memória de longo prazo.

Cada execução começa do zero. Cada spec, cada harness run, cada validação é um evento isolado. Um desenvolvedor sênior tem "memória muscular" — já viu aquele padrão falhar antes, então aborda a situação de forma diferente. O H.O.K Forge não tem isso.

**Resultado:** os mesmos erros se repetem, as mesmas specs estouram o impact radius, os mesmos handoffs ficam malformados. O framework bloqueia, corrige, e esquece.

### 1.2. O que LEARNINGS É (e o que NÃO é)

**LEARNINGS é:**
- A memória de longo prazo do framework
- Um documento vivo em `brain/` ao lado de RULES.md, PROMPT_LIBRARY.md, PRD.md
- Alimentado automaticamente a partir de artefatos que já existem
- Lido pelos agentes ANTES da ação, não processado DEPOIS da falha

**LEARNINGS NÃO é:**
- Um pipeline de aprendizado de máquina
- Um engine de destilação
- Um sistema de RAG com embeddings
- Algo que depende da boa vontade de agentes preguiçosos
- Acoplado ao harness_runner.py

### 1.3. Princípios Fundadores

| Princípio | Descrição |
|---|---|
| **Memória, não máquina** | LEARNINGS é um documento, não um sistema. Conhecimento vive em Markdown, não em bancos de dados. |
| **Lido antes, não processado depois** | A memória serve para prevenir, não para diagnosticar post-mortem. |
| **Agentes leem, nunca escrevem** | O agente é consumidor de memória, nunca produtor. A memória se constrói sozinha. |
| **Camada paralela, nunca integrada** | LEARNINGS observa os mesmos artefatos que o harness, mas é independente. Relação de produtor-consumidor. |
| **Humano decide, script propõe** | O script nunca modifica documentos estratégicos (RULES.md, PROMPT_LIBRARY.md). Ele sugere. |
| **Esquecimento saudável** | Padrões que não se repetem devem enfraquecer. Memória infinita é ruído. |

---

## PARTE 2: ARQUITETURA

### 2.1. Visão Geral

```
┌─────────────────────────────────────────────────────────────────────┐
│                    ARTEFATOS EXISTENTES (Fontes)                     │
│                                                                      │
│  HARNESS_LOG.md    JOURNAL.md    wiki_log.md    git log    STATE.md │
└──────┬────────────────┬──────────────┬──────────────┬───────────────┘
       │                │              │              │
       └────────────────┴──────┬───────┴──────────────┘
                               │
                               ▼
              ┌────────────────────────────────┐
              │   learnings_aggregator.py       │
              │                                │
              │   Fonte 1: FAIL→SUCCESS diffs   │  (automático)
              │   Fonte 2: Oracle gaps          │  (automático)
              │   Fonte 3: Harness gate check   │  (automático)
              └────────────┬───────────────────┘
                           │
                           ▼
              ┌────────────────────────────────┐
              │       brain/LEARNINGS.md        │
              │                                │
              │   ## Scars (cicatrizes)         │
              │   ## Oracle Gaps                │
              │   ## Propostas de Regra         │
              │   ## Índice                     │
              └───────┬────────────┬───────────┘
                      │            │
            ┌─────────┘            └─────────┐
            ▼                                ▼
   ┌──────────────────┐            ┌──────────────────┐
   │   spec-driver    │            │  qa-validator    │
   │  lê ANTES de     │            │  lê ANTES de     │
   │  executar        │            │  validar         │
   └──────────────────┘            └──────────────────┘
```

### 2.2. Relação com o Harness Runner

O `harness_runner.py` **não é modificado em sua lógica interna**. A única alteração é uma verificação adicional em `check_sprint_contract()`:

```
Se esta spec teve um FAIL anterior no HARNESS_LOG
E o LEARNINGS.md não contém entrada para esta spec
ENTÃO bloquear com: "Cicatriz não registrada. Rode learnings_aggregator.py"
```

O harness continua sendo o gate reativo puro. Ele apenas agora também verifica se a memória está completa. O agente não precisa preencher nada — ele só precisa rodar o script (ou o script roda automaticamente antes do gate).

### 2.3. Três Fontes de Dados

| Fonte | Automação | O que captura | Cobertura estimada |
|---|---|---|---|
| **Agregador automático** | 100% | Padrões FAIL→SUCCESS, diffs, recorrências | ~70% |
| **Oracle gaps** | 100% | Queries com conf < 0.5, buracos na documentação | ~15% |
| **Humano** | Manual | Causas raiz estratégicas, ajustes de contexto | ~15% |

---

## PARTE 3: ESPECIFICAÇÃO DOS ARTEFATOS

### 3.1. `brain/LEARNINGS.md` — O Documento

**Localização:** `.context/brain/LEARNINGS.md`
**Domínio:** docs
**Formato:** Markdown

#### Estrutura Completa

```markdown
# 🧠 LEARNINGS — Memória do H.O.K Forge

> **Versão:** 1.0  
> **Última atualização:** [timestamp automático]  
> **Total de cicatrizes:** [N]  
> **Cicatrizes ativas:** [N] | **Dormentes:** [N]

---

## Como Usar Este Documento

**Se você é spec-driver:** Antes de executar qualquer spec, leia a seção Scars.
Se o padrão da spec atual se assemelha a alguma cicatriz registrada, aplique
a correção preventivamente.

**Se você é qa-validator:** Antes de validar, consulte as Scars.
Se a implementação reproduz um padrão que já foi cicatrizado, sinalize mesmo
que passe nos critérios formais.

**Se você é humano:** Revise a seção "Propostas de Regra" periodicamente.
Decida quais se tornam regras em RULES.md.

---

## 📊 Estatísticas

| Métrica | Valor |
|---|---|
| Total de cicatrizes registradas | [N] |
| Cicatrizes ativas (última ocorrência < 30 dias) | [N] |
| Cicatrizes dormentes (sem ocorrência > 30 dias) | [N] |
| Propostas de regra pendentes | [N] |
| Oracle gaps abertos | [N] |

---

## 🩸 Scars — Cicatrizes de Execução

<!-- Gerado automaticamente por learnings_aggregator.py -->
<!-- Formato: uma seção por cicatriz, ordenada por data (mais recente primeiro) -->

### Scar #001 — [Título descritivo do padrão]
- **ID:** SCAR-2026-04-22-001
- **Detectado em:** 2026-04-22
- **Última ocorrência:** 2026-04-28
- **Contagem:** 3 ocorrências
- **Status:** 🟢 Ativa
- **Tipo:** [Estrutural | Semântico | Comportamental]
- **Spec afetada:** `.specs/features/[nome]/spec.md`
- **Check do harness:** [nome da verificação que falhou, ex: schema_contract]
- **Padrão do erro:** [descrição objetiva do que falhou]
- **Correção aplicada:** [o que mudou entre o FAIL e o SUCCESS]
- **Diff relevante:** [trecho do git diff, se aplicável]
- **Causa raiz:** [preenchido pelo humano ou gerado automaticamente como PENDENTE]
- **Regra derivada:** [se gerou regra em RULES.md, referenciar aqui]

### Scar #002 — ...

---

## 🔍 Oracle Gaps — Lacunas de Conhecimento

<!-- Gerado automaticamente por learnings_aggregator.py a partir de wiki_log.md -->

### Gap #001 — [Tópico sem cobertura]
- **ID:** GAP-2026-04-29-001
- **Detectado em:** 2026-04-29
- **Fonte:** wiki_log.md (queries com conf < 0.5)
- **Queries relacionadas:** ["como mockar webhook?", "webhook testing"]
- **Confiança média:** 0.42
- **Arquivos WIKI consultados:** [lista de arquivos que retornaram baixa confiança]
- **Ação sugerida:** Criar `WIKI/concepts/[tópico].md`
- **Status:** 🔍 Aberto

---

## ⚠️ Propostas de Regra — Aguardando Decisão Humana

<!-- Gerado automaticamente quando um padrão se repete >= 3 vezes -->
<!-- O script NUNCA altera RULES.md diretamente -->

### Proposta #001 — [Regra sugerida]
- **ID:** PROP-2026-04-30-001
- **Gerada em:** 2026-04-30
- **Baseada em:** Scar #003, #007, #015
- **Frequência:** 3 ocorrências do mesmo padrão
- **Regra sugerida:** Adicionar a RULES.md §[N]: "[texto da regra]"
- **Justificativa:** [por que essa regra deveria existir]
- **Impacto estimado:** [quais checks do harness seriam afetados]
- **Status:** 🔍 Aguardando decisão

---

## 📋 Índice de Scars

<!-- Atualizado automaticamente pelo aggregator -->

| ID | Título | Tipo | Status | Última Ocorrência | Contagem |
|---|---|---|---|---|---|
| SCAR-... | ... | ... | 🟢/💤 | ... | ... |
```

### 3.2. `.context/_scripts/learnings_aggregator.py` — O Script

**Localização:** `.context/_scripts/learnings_aggregator.py`
**Domínio:** source
**Linguagem:** Python (stdlib-only)
**Linhas estimadas:** ~200-250

#### Contrato de Comportamento

| Aspecto | Especificação |
|---|---|
| **Input** | `HARNESS_LOG.md`, `JOURNAL.md`, `wiki_log.md`, `git log` |
| **Output** | Atualização de `brain/LEARNINGS.md` |
| **Execução** | Sob demanda (`npm run context:learnings`) ou CI pós-merge |
| **Timeout** | 5 segundos. Se estourar, aborta com `[WARN]` |
| **Idempotência** | Rodar duas vezes não duplica entradas. Cada scar tem ID único |
| **Regras imutáveis** | NUNCA modifica `RULES.md`, `PROMPT_LIBRARY.md`, ou qualquer arquivo em `brain/` exceto `LEARNINGS.md` |

#### Lógica Interna (Pseudocódigo)

```
FUNÇÃO PRINCIPAL:
  1. Parsear HARNESS_LOG.md
     → Extrair entradas [HARNESS-FAIL] e [HARNESS-PASS]
     → Para cada FAIL, identificar a spec associada e o check que falhou
  
  2. Para cada FAIL, buscar SUCCESS correspondente
     → Mesma spec + mesmo check + timestamp posterior
     → Se encontrado: extrair git diff entre os dois commits
     → Se NÃO encontrado: registrar como "falha não resolvida"
  
  3. Parsear wiki_log.md
     → Extrair queries com mode=QUERY e status=FAIL (conf < 0.5)
     → Agrupar por tópico similar (normalização de texto)
  
  4. Verificar recorrências
     → Se um mesmo padrão (check + tipo de falha) aparece >= 3 vezes
     → Gerar entrada em "Propostas de Regra"
  
  5. Aplicar decay
     → Scars sem ocorrência nos últimos 30 dias → status "💤 Dormente"
     → Scars dormentes continuam no arquivo mas não aparecem no índice ativo
  
  6. Atualizar LEARNINGS.md
     → Preservar seções manuais (causas raiz preenchidas pelo humano)
     → Atualizar seções automáticas (scars, gaps, propostas, índice)
     → Atualizar estatísticas no cabeçalho
```

#### Regex Chave para Parsing do HARNESS_LOG.md

```python
# Padrão de entrada de falha no HARNESS_LOG
FAIL_PATTERN = r'\[HARNESS-FAIL\]\s*spec:\s*(.+?)\s*\|\s*check:\s*(.+?)\s*\|\s*Detalhe:\s*(.+)'

# Padrão de entrada de sucesso
PASS_PATTERN = r'\[HARNESS-PASS\]\s*spec:\s*(.+)'

# Padrão de timestamp (compatível com _tz_utils)
TIMESTAMP_PATTERN = r'\[(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2})\]'
```

#### Estrutura de uma Scar Gerada

```python
scar = {
    "id": f"SCAR-{date}-{seq:03d}",
    "title": "",              # Gerado a partir do check + tipo de falha
    "detected_at": "",        # Data do primeiro FAIL
    "last_occurrence": "",    # Data da última ocorrência
    "count": 0,               # Número de ocorrências
    "status": "active",       # active | dormant
    "type": "",               # structural | semantic | behavioral
    "spec": "",               # Caminho da spec afetada
    "check": "",              # Nome do check do harness que falhou
    "error_pattern": "",      # Descrição extraída do "Detalhe"
    "fix_applied": "",        # Extraído do git diff entre FAIL e SUCCESS
    "diff_snippet": "",       # Trecho relevante do diff (max 10 linhas)
    "root_cause": "PENDENTE", # Preenchido pelo humano
    "derived_rule": ""        # Referência à regra se existir
}
```

### 3.3. Atualização do Prompt do `spec-driver.md`

**Arquivo:** `.agent/subagents/spec-driver.md`
**Alteração:** Adicionar passo 0 ao workflow

```markdown
# Workflow (atualizado):
0. **Memory Check:** Read `brain/LEARNINGS.md`. If the current spec's 
   pattern resembles any active scar, apply the recorded fix preemptively. 
   Do not repeat known mistakes.
1. **Locate Spec:** ...
[resto do workflow permanece igual]
```

### 3.4. Atualização do Prompt do `qa-validator.md`

**Arquivo:** `.agent/subagents/qa-validator.md`
**Alteração:** Adicionar verificação após passo 2

```markdown
When invoked:
1. ... [existente]
2. ... [existente]
3. **Memory Check:** Read `brain/LEARNINGS.md`. If the implementation 
   reproduces a pattern that was previously scarred, flag it as a 
   RISK even if formal criteria pass. Knowledge debt is a failure mode.
4. Check for architectural compliance ... [existente, renumerado]
```

### 3.5. Atualização do `harness_runner.py`

**Arquivo:** `.context/_scripts/harness_runner.py`
**Alteração:** Adicionar verificação em `check_sprint_contract()`

```python
def check_learnings_completeness(spec_path: Path):
    """Verifica se a memória do LEARNINGS está completa para esta spec."""
    learnings_path = CONTEXT_DIR / "brain" / "LEARNINGS.md"
    harness_log_path = CONTEXT_DIR / "maintenance" / "HARNESS_LOG.md"
    
    if not learnings_path.exists():
        return True, "LEARNINGS.md ausente (skip)"
    if not harness_log_path.exists():
        return True, "HARNESS_LOG.md ausente (skip)"
    
    # Verifica se a spec teve FAILs anteriores
    log_text = harness_log_path.read_text(encoding="utf-8")
    spec_name = spec_path.parent.name  # nome da feature
    
    # Conta FAILs para esta spec
    fail_count = len(re.findall(
        rf'\[HARNESS-FAIL\].*?spec:.*?{re.escape(spec_name)}',
        log_text, re.I
    ))
    
    if fail_count == 0:
        return True, "Sem histórico de falhas (skip)"
    
    # Verifica se LEARNINGS contém entrada para esta spec
    learnings_text = learnings_path.read_text(encoding="utf-8")
    if spec_name.lower() not in learnings_text.lower():
        return False, (
            f"Spec '{spec_name}' tem {fail_count} falha(s) no histórico "
            f"mas nenhuma cicatriz registrada. Rode: npm run context:learnings"
        )
    
    return True, "Memória completa"
```

### 3.6. Atualização do `package.json`

**Arquivo:** `package.json`
**Alteração:** Adicionar script

```json
"context:learnings": "python .context/_scripts/learnings_aggregator.py"
```

### 3.7. Integração com Fluxo Existente

O `run_context.py` (orquestrador principal) deve chamar o aggregator após cada ciclo completo de execução:

```
[spec-driver executa] → [qa-validator valida] → [harness passa]
                                                      ↓
                                          learnings_aggregator.py
                                                      ↓
                                              LEARNINGS.md atualizado
```

---

## PARTE 4: MECANISMOS

### 4.1. Mecanismo de Decay (Esquecimento Saudável)

| Regra | Descrição |
|---|---|
| **Ativa** | Scar com última ocorrência nos últimos 30 dias |
| **Dormente** | Scar sem ocorrência por mais de 30 dias. Continha no arquivo, mas não é consultada ativamente pelos agentes |
| **Arquivamento** | Scar dormente por mais de 90 dias pode ser movida para seção "Arquivo Histórico" no final do documento |
| **Exceção** | Scars do tipo "Estrutural" (erros de schema, drift de versão) nunca ficam dormentes — são permanentes |

**Implementação:** O `learnings_aggregator.py` compara `last_occurrence` com a data atual. Se `> 30 dias`, muda status para `💤 Dormente`. Se `> 90 dias`, move para seção de arquivo.

### 4.2. Mecanismo de Detecção de Oracle Gaps

**Input:** `wiki_log.md` (já existente, alimentado por `context_oracle.py` via `_wiki_log_utils.py`)

**Lógica:**
```
Para cada entrada no wiki_log.md:
  Se mode == "QUERY" e status == "FAIL" (conf < 0.5):
    Extrair: query, confidence, arquivos consultados
    Normalizar query (remover acentos, lowercase)
    Agrupar queries similares (mesmo tópico raiz)
    Se grupo tem >= 2 queries:
      Gerar entrada em "Oracle Gaps"
```

**Exemplo de agrupamento:**
- "como mockar webhook?" → raiz: "webhook"
- "webhook testing framework" → raiz: "webhook"
- "testar integração webhook" → raiz: "webhook"
- **Resultado:** 3 queries sobre "webhook" com conf média 0.42 → Gap registrado

### 4.3. Mecanismo de Propostas de Regra

**Trigger:** Um mesmo padrão (check + tipo de falha) aparece 3 ou mais vezes em scars diferentes.

**Lógica:**
```
Agrupar scars por campo "check" e "error_pattern" normalizado
Para cada grupo com contagem >= 3:
  Gerar entrada em "Propostas de Regra"
  Não alterar RULES.md
  Não alterar PROMPT_LIBRARY.md
  Apenas sugerir no LEARNINGS.md com status "🔍 Aguardando decisão"
```

**Exemplo:**
```markdown
## ⚠️ Proposta de Regra #001
- **Baseada em:** Scar #003, #007, #015
- **Padrão recorrente:** Specs do tipo "integration" estouram max_impact_radius
- **Regra sugerida:** Adicionar a RULES.md §5.1: "Specs do tipo integration 
  DEVEM ter max_impact_radius >= 15"
- **Frequência:** 3 ocorrências em 3 specs diferentes
- **Status:** 🔍 Aguardando decisão
```

### 4.4. Mecanismo de Proteção de Seções Manuais

O `learnings_aggregator.py` deve preservar edições humanas. Implementação:

```python
# Marcadores de seção manual (o script NÃO toca entre esses marcadores)
MANUAL_START = "<!-- MANUAL_START -->"
MANUAL_END = "<!-- MANUAL_END -->"

# Campos que o humano pode preencher e o script não sobrescreve:
# - root_cause (quando != "PENDENTE")
# - Seções inteiras escritas manualmente entre os marcadores
```

### 4.5. Mecanismo de Segurança

| Risco | Mitigação |
|---|---|
| Script modifica RULES.md ou PROMPT_LIBRARY.md | **Hardcoded:** script só tem permissão de escrita em `brain/LEARNINGS.md`. Qualquer tentativa de escrita em outros arquivos gera erro fatal |
| LEARNINGS.md cresce infinitamente | Decay + arquivamento a 90 dias. Seção de arquivo é comprimida (apenas ID + título + data) |
| Parsing frágil de logs | Regex estrito + fallback `WARN`. Se formato do log mudar, script pausa e reporta `[WARN] Log schema drift` |
| Agentes ignoram LEARNINGS.md | `check_learnings_completeness()` no harness bloqueia commit se cicatriz não registrada |
| Duplicação de entradas | Cada scar tem ID único gerado a partir de data + sequência. Script verifica antes de inserir |
| Performance | Timeout de 5 segundos. Se estourar, aborta silenciosamente |

---

## PARTE 5: CLASSIFICAÇÃO DAS CICATRIZES

### 5.1. Tipos de Cicatriz

| Tipo | Descrição | Exemplo | Decay |
|---|---|---|---|
| **Estrutural** | Erro determinístico detectável mecanicamente | Drift de versão, campo YAML ausente, tabela inexistente no schema | **Nunca decai** (permanente) |
| **Semântico** | Erro parcialmente detectável, requer interpretação | PRD violando boundaries do INCEPTION, dependencies sem lastro em market/ | Decai após 30 dias sem recorrência |
| **Comportamental** | Padrão de comportamento do agente que leva a falha | Specs que estouram impact radius, handoffs circulares, loops improdutivos | Decai após 30 dias sem recorrência |
| **Gap** | Buraco de documentação detectado via Oracle | Queries com conf < 0.5, tópicos sem cobertura na WIKI | Decai após criação do documento WIKI correspondente |

### 5.2. Mapeamento Fonte → Tipo

| Fonte de Dados | Tipo de Cicatriz Gerada |
|---|---|
| `harness_runner.py: check_schema_contract()` | Estrutural |
| `harness_runner.py: check_sprint_contract()` | Estrutural |
| `harness_runner.py: check_handoff_integrity()` | Comportamental |
| `harness_runner.py: check_strategic_alignment()` | Semântico |
| `harness_runner.py: check_enrichment_integrity()` | Semântico |
| `harness_runner.py: check_impact_radius()` | Comportamental |
| `harness_runner.py: check_journal_sam()` | Comportamental |
| `spec-driver: SCOPE_BLOWOUT` | Comportamental |
| `context_oracle.py: conf < 0.5` | Gap |
| `check_version_consistency.py` | Estrutural |
| `cleanup_specs.py: arquivamento por inatividade` | Comportamental |

---

## PARTE 6: FLUXOS DE TRABALHO

### 6.1. Fluxo de Geração (Automático)

```
1. Desenvolvedor executa feature
2. spec-driver executa (agora lê LEARNINGS.md antes)
3. qa-validator valida (agora lê LEARNINGS.md antes)
4. harness_runner valida contratos
5. Commit é feito
6. CI pós-merge roda: npm run context:learnings
7. learnings_aggregator.py:
   a. Lê HARNESS_LOG.md → identifica novos FAILs e PASSes
   b. Para cada FAIL com SUCCESS correspondente → extrai diff → gera scar
   c. Lê wiki_log.md → identifica Oracle gaps
   d. Verifica recorrências → gera propostas de regra se aplicável
   e. Aplica decay → marca scars inativas como dormentes
   f. Atualiza LEARNINGS.md (preservando edições manuais)
```

### 6.2. Fluxo de Consulta (Pelo Agente)

```
1. spec-driver é invocado para uma spec
2. spec-driver lê brain/LEARNINGS.md (passo 0 do workflow)
3. Se a spec atual se parece com uma scar ativa:
   a. Aplica a correção preventivamente
   b. Não repete o erro conhecido
4. Se não há correspondência: executa normalmente
```

### 6.3. Fluxo de Decisão Humana

```
1. Humano abre brain/LEARNINGS.md periodicamente
2. Revisa seção "Propostas de Regra"
3. Para cada proposta:
   a. Se concorda: aplica a regra em RULES.md manualmente
      e marca como "✅ Aplicada" no LEARNINGS.md
   b. Se discorda: marca como "❌ Rejeitada" com justificativa
   c. Se precisa de mais dados: deixa como "🔍 Aguardando"
4. Revisa scars com root_cause == "PENDENTE"
5. Preenche causa raiz quando possível
```

### 6.4. Fluxo de Proteção (Gate do Harness)

```
1. harness_runner.check_sprint_contract() é chamado
2. check_learnings_completeness() é chamado como parte da validação
3. Se a spec teve FAILs anteriores no HARNESS_LOG:
   a. Verifica se LEARNINGS.md contém entrada para esta spec
   b. Se NÃO contém → bloqueia: "Cicatriz não registrada"
   c. O agente é forçado a rodar: npm run context:learnings
4. Se a spec não tem histórico de falhas → skip (sem overhead)
```

---

## PARTE 7: PLANO DE IMPLEMENTAÇÃO

### Fase 1: Fundação (Semana 1)

| Tarefa | Artefato | Esforço |
|---|---|---|
| Criar template do LEARNINGS.md | `brain/LEARNINGS.md` | Baixo |
| Preencher primeiras cicatrizes retroativamente (análise manual do HARNESS_LOG.md e JOURNAL.md existentes) | `brain/LEARNINGS.md` | Médio |
| Adicionar script npm | `package.json` | Baixo |

**Entregável:** LEARNINGS.md com 3-5 cicatrizes reais extraídas do histórico existente.

### Fase 2: Automação (Semana 2)

| Tarefa | Artefato | Esforço |
|---|---|---|
| Criar learnings_aggregator.py | `.context/_scripts/learnings_aggregator.py` | Alto |
| Testar com dados reais do HARNESS_LOG.md | - | Médio |
| Validar idempotência (rodar 2x, não duplicar) | - | Baixo |

**Entregável:** Script funcional que gera/atualiza LEARNINGS.md automaticamente.

### Fase 3: Integração com Agentes (Semana 2-3)

| Tarefa | Artefato | Esforço |
|---|---|---|
| Atualizar prompt do spec-driver | `.agent/subagents/spec-driver.md` | Baixo |
| Atualizar prompt do qa-validator | `.agent/subagents/qa-validator.md` | Baixo |
| Adicionar check_learnings_completeness() no harness | `.context/_scripts/harness_runner.py` | Médio |

**Entregável:** Agentes consultam LEARNINGS antes de agir. Harness bloqueia se memória incompleta.

### Fase 4: Refinamento (Semana 3-4)

| Tarefa | Artefato | Esforço |
|---|---|---|
| Implementar mecanismo de decay | `learnings_aggregator.py` | Médio |
| Implementar detecção de Oracle gaps | `learnings_aggregator.py` | Médio |
| Implementar detecção de propostas de regra | `learnings_aggregator.py` | Médio |
| Primeira revisão humana de propostas | `brain/LEARNINGS.md` | Baixo |

**Entregável:** Sistema completo com decay, gaps, e propostas funcionando.

### Fase 5: Validação (Semana 4)

| Tarefa | Artefato | Esforço |
|---|---|---|
| Rodar ciclo completo (executar feature → gerar scar → consultar scar → prevenir erro) | - | Médio |
| Validar que agentes preguiçosos não conseguem escapar | - | Médio |
| Documentar no SCRIPT_GLOSSARY.md | `.context/brain/SCRIPT_GLOSSARY.md` | Baixo |
| Atualizar FILE_GLOSSARY.md | `.context/brain/FILE_GLOSSARY.md` | Baixo |

**Entregável:** LEARNINGS em produção, validado end-to-end.

---

## PARTE 8: MÉTRICAS DE SUCESSO

| Métrica | Como Medir | Meta |
|---|---|---|
| **Redução de erros repetidos** | Contagem de scars com mesmo check+pattern antes e depois da implantação | -50% em 30 dias |
| **Cobertura de memória** | Scars ativas / total de FAILs no HARNESS_LOG | > 80% |
| **Tempo de preenchimento** | Latência entre FAIL e registro da scar | < 1 minuto (automático) |
| **Agentes consultando memória** | Presença de padrões de correção preventiva no git diff | Presença detectável |
| **Propostas de regra aceitas** | Propostas marcadas como ✅ / total de propostas | > 50% |

---

## PARTE 9: ARQUIVOS A CRIAR/MODIFICAR (Resumo Final)

| # | Ação | Arquivo | Tipo |
|---|---|---|---|
| 1 | **CRIAR** | `.context/brain/LEARNINGS.md` | Documento |
| 2 | **CRIAR** | `.context/_scripts/learnings_aggregator.py` | Script |
| 3 | **MODIFICAR** | `.agent/subagents/spec-driver.md` | Prompt (+3 linhas) |
| 4 | **MODIFICAR** | `.agent/subagents/qa-validator.md` | Prompt (+3 linhas) |
| 5 | **MODIFICAR** | `.context/_scripts/harness_runner.py` | Script (+25 linhas) |
| 6 | **MODIFICAR** | `package.json` | Config (+1 linha) |
| 7 | **MODIFICAR** | `.context/brain/SCRIPT_GLOSSARY.md` | Documento (documentação) |
| 8 | **MODIFICAR** | `.context/brain/FILE_GLOSSARY.md` | Documento (documentação) |

**Total: 2 artefatos novos, 6 modificações.**

---
