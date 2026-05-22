# 🔍 Revisão Crítica: `plano_mimo_propagation.md`

> **Revisor:** Claude Opus 4.6 (Thinking)
> **Data:** 2026-05-21
> **Veredicto geral:** O plano é tecnicamente sólido e muito bem detalhado, mas **peca por excesso de engenharia para o estágio atual do projeto.** Ele transforma uma Proposta B (~150 linhas, 4 passos) em uma operação de 10 entregáveis, 6 fases, 12 testes e ~400 linhas de código. Isso viola diretamente a **Lei da Sobriedade** do próprio H.O.K.

---

## 1. Pontos Fortes (O que está bem)

| Aspecto | Avaliação |
|---------|-----------|
| **Degradação Graceful** | Excelente. A política de fallback (§3.5) é a melhor parte do plano. Se o graph não existe, usa só governança. Se nada existe, exit 4. Zero chance de travar o workflow. |
| **Classificação em 3 buckets** | Correto. `must_update` / `likely_update` / `declared_only` é a taxonomia certa. |
| **Exit codes** | Bem definidos e diferenciados (0, 2, 3, 4, 5). |
| **Fallback no journal-sync** | A cláusula "Se exit ≠ 0, ler rx-communications.md manualmente" (§4.1 linha 596) é a decisão mais inteligente do plano inteiro — garante que o novo sistema não pode ser pior que o atual. |
| **"O que NÃO fazer"** (§7.2) | Demonstra maturidade. Saber o que excluir é tão importante quanto saber o que incluir. |

---

## 2. Problemas Críticos

### 2.1 🔴 `file_to_node_id()` — O Elefante na Sala

O pseudocódigo do §3.6 (linha 256) faz:
```python
node_id = file_to_node_id(file)
if node_id in graph_data['nodes']:
```

**Problema:** O `graph.json` do Graphify usa IDs que **não são caminhos de arquivo.** Veja o exemplo real:

```json
{
  "label": "init_ai_project.sh",
  "source_file": "init_ai_project.sh",
  "id": "init_ai_project_sh"
}
```

O `id` é `init_ai_project_sh`, não `init_ai_project.sh`. A função `file_to_node_id()` precisa mapear um path relativo (`init_ai_project.sh`) para o `id` normalizado do nó (`init_ai_project_sh`). O plano **assume que isso é trivial mas não especifica o algoritmo de normalização**, e como o graphify usa convenções diferentes para código vs docs, essa função pode ter 20+ linhas de edge cases.

**Pior:** um nó de função (ex: `validate()`) tem `source_file` mas o `id` é algo como `template_início_de_projeto_validate_context_validate`. O BFS vai navegar para **nós de funções**, não de arquivos. O plano precisa de um passo de `node → source_file` para converter os resultados do BFS de volta para caminhos de arquivo.

> [!CAUTION]
> **Risco:** Se `file_to_node_id()` falha para 30% dos seeds, o bucket `structural` fica vazio e o sistema degrada para governance-only sem avisar claramente. O plano trata isso como `low_graph_coverage` warning, mas isso mascara um bug de mapping.

---

### 2.2 🔴 BFS em Grafo de Funções vs. Grafo de Arquivos

O grafo do Graphify tem **458 nós**, dos quais apenas **128 são source_files únicos**. Os outros ~330 nós são funções, classes, conceitos, etc. O BFS com depth=2 vai caminhar por:

```
harness_runner.py → validate() → HARNESS_LOG.md
                  → check_sprint_contract() → STATE.md
                  → get_inception_status() → run_context.py
```

Isso é correto semanticamente, mas gera uma explosão combinatória. Com depth=2 a partir de um script central como `harness_runner.py` (9 edges diretas), o BFS pode retornar **dezenas de arquivos**, incluindo muitos que são tangenciais.

**O plano menciona `--depth-docs 1` mas não define o critério de quando um nó intermediário é "doc" vs "code".** No grafo real, `HARNESS_LOG.md` é `file_type: "code"` (porque o graphify classifica todos os nós extraídos como `code` ou `docs` com base no source_file, não no nó individual).

> [!WARNING]
> **Risco:** O blast radius estrutural pode ser **excessivamente amplo**, transformando o journal-sync em algo mais ruidoso do que a leitura manual atual. O objetivo era focar em 3-5 arquivos, mas o BFS pode devolver 15+.

---

### 2.3 🟡 `governance_edges.json` é Duplicação Prematura

O plano cria `governance_edges.json` como versão estruturada da Seção 4 do `rx-communications.md`. Isso gera:

1. **Dois SSOTs** para a mesma informação (o .md e o .json)
2. **Obrigação de manter ambos sincronizados** — ironia: estamos criando um novo problema de propagação para resolver um problema de propagação
3. **O plano reconhece isso** (linha 56: "Quando este arquivo divergir do .md, este é o que blast_radius.py consome") — mas isso é exatamente o que vai acontecer 3 commits depois

A Proposta B original do `propagation_analysis.md` dizia: "Consulta `rx-communications.md` para encontrar o blast radius de governança." Sem JSON intermediário. O `parse_rx_markdown()` que o próprio plano define como fallback (§3.6 linha 238) **já resolve o problema.**

> [!IMPORTANT]
> **Sugestão:** Começar SEM `governance_edges.json`. Parsear o `rx-communications.md` diretamente. Se o parsing se tornar frágil na prática, ENTÃO criar o JSON. Isso elimina a Fase 1 inteira e reduz o plano de 6 para 5 fases.

---

### 2.4 🟡 FLOW_PROPAGATION.md — Burocracia Precoce

O plano propõe criar um documento de 7 seções (§5.1) espelhando o FLOW_SDD para um sistema que **ainda nem existe**. O FLOW_SDD documenta algo maduro e estável. Criar a documentação antes da implementação significa:

1. O documento vai ficar obsoleto durante a própria implementação
2. Consome ~1-2 sessões de trabalho (§8) em documentação de algo não validado
3. Viola o espírito "Ship → Validate → Document" que o próprio MASTER_FLOW prescreve

> [!TIP]
> **Sugestão:** Documentar DEPOIS de validar. Quando o `blast_radius.py` já estiver rodando há 2-3 sprints e a equipe entender os padrões reais de uso, aí sim criar o FLOW_PROPAGATION.md com dados reais. Por agora, uma seção no SCRIPT_GLOSSARY + um comentário no topo do script basta.

---

### 2.5 🟡 12 Testes Para Um Script de ~150 Linhas

Os 12 cenários de teste (§6.1) são tecnicamente corretos, mas representam um overhead desproporcional:

- `test_priority_ordering` — testa implementação interna, não comportamento
- `test_depth_adaptive` — testa uma otimização, não uma feature core
- `test_glossary_validation` — testa uma feature opcional (`--glossary-validate`)
- `test_reasons_have_source_and_via` — testa formato de output, não lógica

Para um MVP, 5-6 testes cobrem o core:
1. Ambos concordam → `must_update`
2. Só graph → `likely_update`
3. Só governance → `declared_only`
4. Graph ausente → degradação
5. Ambos ausentes → exit 4
6. Seed sem matches → buckets vazios

Os outros 6 testes são para a Fase 2 (se o script provar seu valor).

---

### 2.6 🟡 `--mode audit` Mistura Responsabilidades

O plano absorve a Proposta A (`rx_health_check.py`) dentro do `blast_radius.py` como `--mode audit`. Isso viola o princípio de responsabilidade única:

- **`propagate`** opera em tempo real, durante o journal-sync, sobre um seed específico
- **`audit`** é retrospectivo, periódico, sem seed, sobre o sistema inteiro

Combinar ambos num mesmo script cria:
- Complexidade no argparse (seed é obrigatório em propagate mas irrelevante em audit)
- Testes que precisam cobrir dois modos distintos
- Confusão sobre quando usar qual

> [!TIP]
> **Sugestão:** Manter como scripts separados. `blast_radius.py` faz propagação (core). `rx_health_check.py` faz auditoria (bônus). São scripts de 80-100 linhas cada, muito mais fáceis de manter do que um de 200+ com dois modos.

---

### 2.7 🟢 `post-commit` vs `pre-commit`

O plano usa `post-commit` (§4.2), o `propagation_analysis.md` original sugeria `pre-commit`. O **post-commit é a escolha certa** porque:
- Não bloqueia o fluxo do desenvolvedor
- O graphify `update` é idempotente e fire-and-forget
- Se falhar, o commit já está salvo (sem perda de trabalho)

Porém, o hook assume que `graphify` está instalado globalmente. Se não estiver, o `timeout 30 graphify update .` vai falhar silenciosamente (o `|| echo` engole o erro). O plano deveria adicionar um `which graphify > /dev/null 2>&1 ||` guard.

Também: **Windows.** O seu ambiente é Windows. `.husky/post-commit` precisa ser um script que funcione tanto em Git Bash quanto em PowerShell. O script atual usa `#!/bin/sh`, `grep -E`, `head -1`, `timeout` — todos assumem Unix. No Windows com Git Bash funciona, mas vale documentar essa dependência.

---

## 3. Premissas Não Validadas

| Premissa do Plano | Realidade |
|---|---|
| "graph.json tem meta.built_from_commit" (§3.11, linha 515) | **ERRADO.** O campo real é `built_at_commit` no nível raiz, não `meta.built_from_commit`. O `check_graph_freshness()` vai retornar 999 (stale) para TODO grafo. |
| "Nodes no graph.json são indexados por id num dict" (§3.6, linha 256: `if node_id in graph_data['nodes']`) | **ERRADO.** `graph_data['nodes']` é uma **lista**, não um dict. Precisa de um pré-processamento `{n['id']: n for n in graph_data['nodes']}` antes de fazer lookup. |
| "Links usam 'source' e 'target' como node IDs" | **CORRETO.** Mas os IDs não são file paths — são IDs normalizados. Confirma o problema 2.1. |

---

## 4. Análise de Esforço vs. Valor

O plano estima **6-8 sessões** de trabalho. Vou quebrar isso:

| Componente | Esforço Estimado | Valor Real | Veredicto |
|---|---|---|---|
| `governance_edges.json` (Fase 1) | ~1 sessão | Baixo — duplica rx-communications | ⚠️ **Eliminar** |
| `blast_radius.py` core (Fase 2) | ~2-3 sessões | **Alto** — é o motor inteiro | ✅ **Manter** |
| `journal-sync` update (Fase 3) | ~0.5 sessão | **Alto** — é a integração | ✅ **Manter** |
| `post-commit` hook (Fase 3) | ~0.25 sessão | Médio — nice-to-have | ✅ Manter |
| `package.json` scripts (Fase 3) | ~0.1 sessão | Baixo | ✅ Trivial |
| `FLOW_PROPAGATION.md` (Fase 4) | ~1-2 sessões | **Muito Baixo** — prematuro | ⚠️ **Adiar** |
| Glossários update (Fase 4) | ~0.25 sessão | Médio — necessário | ✅ Manter |
| `rx-communications.md` update (Fase 4) | ~0.25 sessão | Médio — necessário | ✅ Manter |
| 12 testes (Fase 5) | ~1 sessão | Parcial — 6 bastam | ⚠️ **Reduzir** |
| Handoff (Fase 6) | ~0.5 sessão | Médio | ✅ Manter |

**Total revisado: 4-5 sessões** (vs. 6-8 originais). Economia de ~40%.

---

## 5. Resumo do Veredicto

```
┌─────────────────────────────────────────────────────────┐
│                    SCORECARD                            │
├─────────────────────┬───────────────────────────────────┤
│ Qualidade Técnica   │ 8/10 — Bem estruturado, completo  │
│ Proporcionalidade   │ 4/10 — Overengineered para o MVP  │
│ Premissas Validadas │ 5/10 — 2 de 3 premissas erradas   │
│ Lei da Sobriedade   │ 3/10 — Viola diretamente          │
│ Risco de Execução   │ 6/10 — file_to_node_id é o ponto  │
│                     │        de falha mais provável      │
├─────────────────────┼───────────────────────────────────┤
│ NOTA FINAL          │ 5.2/10                            │
└─────────────────────┴───────────────────────────────────┘
```

> [!IMPORTANT]
> **Recomendação:** Não descartar o plano — ele tem o raciocínio certo. Mas **podar** até a essência. Ship o MVP lean (4 sessões), validar em produção, e ENTÃO expandir com governance_edges.json, modo audit, e FLOW_PROPAGATION.md quando houver dados reais de uso.
