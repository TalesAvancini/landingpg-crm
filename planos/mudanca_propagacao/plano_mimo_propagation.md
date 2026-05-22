## Plano de Implantação Ultra Completo — Sistema de Blast Radius Híbrido

---

## 0. Visão Executiva

```
ESTADO ATUAL                          ESTADO ALVO
─────────────                         ──────────
3 olhos desconectados                 3 olhos integrados via blast_radius.py
journal-sync lê 347 linhas manual    journal-sync recebe lista priorizada em JSON
SAM cego a rx-communications         SAM continua cego (por agora) — advisory only
governance no Markdown livre          governance em JSON estruturado
graphify atualizado "quando lembra"  graphify atualizado via post-commit hook
glossários vivem isolados             glossários validados contra blast radius
```

**Entregáveis do plano:**
1. `.context/maintenance/governance_edges.json`
2. `.context/_scripts/blast_radius.py`
3. `.agent/skills/journal-sync/SKILL.md` (atualizado)
4. `.husky/post-commit` (novo hook)
5. `.context/brain/FLOW_PROPAGATION.md`
6. `.context/brain/FILE_GLOSSARY.md` (atualizado com novos arquivos)
7. `.context/brain/SCRIPT_GLOSSARY.md` (atualizado com novo script)
8. `.context/maintenance/rx-communications.md` (atualizado com novos componentes)
9. `tests/test_blast_radius.py`
10. `package.json` (novos scripts)

---

## 1. Work Breakdown — Fases

### FASE 1: Fundação (governance_edges.json)
### FASE 2: Motor (blast_radius.py)
### FASE 3: Integração (journal-sync + hooks)
### FASE 4: Documentação (FLOW_PROPAGATION + glossários)
### FASE 5: Validação (testes + dry-run)
### FASE 6: Handoff (fechamento)

---

## 2. FASE 1 — governance_edges.json

### 2.1 Objetivo
Extrair a Seção 4 do `rx-communications.md` para um formato JSON estruturado e consumível por máquina.

### 2.2 Schema Final

```json
{
  "$schema": "governance_edges_v1",
  "version": 1,
  "generated_from": "rx-communications.md",
  "generated_at": "ISO-8601",
  "maintainer_note": "Este arquivo é a versão estruturada da Seção 4 do rx-communications.md. O arquivo .md continua como documentação narrativa. Quando este arquivo divergir do .md, este é o que blast_radius.py consome.",

  "edges": [
    {
      "id": "vision_to_inception",
      "source": "VISION.md",
      "source_path": ".context/brain/VISION.md",
      "target": "INCEPTION.md",
      "target_path": ".context/brain/INCEPTION.md",
      "direction": "forward",
      "nature": "diretriz",
      "layer": "estrategica",
      "critical": false,
      "bidirectional": false,
      "note": "A bússola do projeto. Tudo deriva daqui."
    }
  ],

  "wildcard_edges": [
    {
      "id": "rules_to_all",
      "source": "RULES.md",
      "source_path": ".context/brain/RULES.md",
      "target": "*",
      "nature": "protocolo",
      "layer": "constitucional",
      "critical": true,
      "note": "[CRÍTICO] TODOS. Restringe ações do MASTER_FLOW.md.",
      "activation_rule": "always_if_seed_in_same_layer_or_critical"
    }
  ],

  "categories": {
    "nature_types": [
      "diretriz", "protocolo", "orquestracao",
      "evidencia", "metabolica", "aprendizado",
      "mitigacao", "sintese"
    ],
    "layers": [
      "estrategica", "constitucional", "tatica",
      "imunologica", "metabolica"
    ]
  }
}
```

### 2.3 Decisões de Mapping

| Padrão no rx-communications.md | Tratamento no JSON |
|---|---|
| `Afeta: destino1, destino2` | Uma edge por destino, direction: "forward" |
| `É Afetado Por: origem1` | Edge inversa OU campo `bidirectional: true` |
| `[CRÍTICO] TODOS` | Vai para `wildcard_edges` com `critical: true` |
| `[CRÍTICO]` (sem TODOS) | Edge normal com `critical: true` |
| Seção 5 (Scripts) | **Fora do escopo MVP** — placeholder no JSON |

### 2.4 Regra de Wildcard Edges

Quando `RULES.md` (wildcard, target: `*`) está envolvido:

```
SE o seed contém QUALQUER arquivo ENTÃO:
  SE o arquivo está na layer "constitucional" OU é marcado critical
    ENTÃO RULES.md entra em must_update
  SENÃO
    RULES.md entra em declared_only (revisar, não obrigatório)
```

Isso evita que `RULES.md` apareça como `must_update` para cada commit trivial.

### 2.5 Entregável

| Item | Path | Ação |
|------|------|------|
| `governance_edges.json` | `.context/maintenance/governance_edges.json` | **CRIAR** |
| `rx-communications.md` | `.context/maintenance/rx-communications.md` | Adicionar nota no topo referenciando o JSON |

### 2.6 Critérios de Aceite da Fase 1

- [ ] JSON válido (json.load sem erro)
- [ ] Cada edge do JSON mapeável a uma entrada da Seção 4 do rx-communications.md
- [ ] Pelo menos 1 wildcard edge representada
- [ ] `categories` preenchido com os tipos reais encontrados no arquivo

---

## 3. FASE 2 — blast_radius.py

### 3.1 Objetivo
Script Python CLI que calcula blast radius híbrido (estrutural + governança) e retorna JSON priorizado.

### 3.2 Interface (CLI)

```
python .context/_scripts/blast_radius.py \
  --changed fileA.py fileB.md \
  [--graph graphify-out/graph.json] \
  [--governance .context/maintenance/governance_edges.json] \
  [--rx .context/maintenance/rx-communications.md] \
  [--depth 2] \
  [--depth-docs 1] \
  [--format json|text] \
  [--mode propagate|audit] \
  [--glossary-validate]
```

### 3.3 Parâmetros Detalhados

| Parâmetro | Obrigatório | Default | Descrição |
|-----------|------------|---------|-----------|
| `--changed` | Sim | — | Lista de arquivos seed (propagation seed) |
| `--graph` | Não | `graphify-out/graph.json` | Caminho para o grafo estrutural |
| `--governance` | Não | `.context/maintenance/governance_edges.json` | Caminho para edges de governança |
| `--rx` | Não | `.context/maintenance/rx-communications.md` | Fallback: se governance_edges.json não existir, parsear este |
| `--depth` | Não | `2` | BFS depth para nós do tipo code |
| `--depth-docs` | Não | `1` | BFS depth para nós do tipo docs/governance |
| `--format` | Não | `json` | Formato de saída |
| `--mode` | Não | `propagate` | `propagate` = buckets priorizados; `audit` = relatório de drift |
| `--glossary-validate` | Não | `false` | Se true, cruza resultados contra FILE_GLOSSARY e SCRIPT_GLOSSARY |

### 3.4 Exit Codes

| Code | Significado | Condição |
|------|------------|----------|
| `0` | Sucesso | Blast radius calculado com sucesso |
| `2` | Input inválido | `--changed` vazio ou arquivos inexistentes |
| `3` | Graph indisponível | graph.json não encontrado |
| `4` | Governance indisponível | governance_edges.json E rx-communications.md ambos ausentes |
| `5` | Erro interno | Exceção não tratada |

### 3.5 Política de Degradação

```
SE graph.json existe E governance_edges.json existe:
    → MODO PLENO: ambos contribuem
    → warnings: []

SE graph.json existe MAS governance_edges.json NÃO:
    → Tentar parsear rx-communications.md como fallback
    → warnings: ["governance_json_missing_using_rx_parse"]
    → Se parse falhar: warnings += ["rx_parse_failed_governance_disabled"]

SE graph.json NÃO existe MAS governance_edges.json existe:
    → MODO DEGRADADO: apenas governança
    → warnings: ["graph_unavailable_structural_disabled"]
    → Se graph.json idade > 10 commits: warnings += ["graph_stale"]

SE NENHUM existe:
    → EXIT 4 com mensagem de recuperação
```

### 3.6 Algoritmo Detalhado (pseudocódigo)

```python
def main():
    # ─── 1. VALIDAÇÃO DE INPUT ───
    seed = normalize_paths(args.changed)
    if not seed:
        exit(2)
    
    # ─── 2. CARREGAMENTO COM DEGRADAÇÃO ───
    graph_data = None
    governance_data = None
    warnings = []
    
    # Graph
    graph_path = Path(args.graph)
    if graph_path.exists():
        graph_data = json.loads(graph_path.read_text())
        graph_age = check_graph_freshness(graph_data)
        if graph_age > FRESHNESS_THRESHOLD:
            warnings.append("graph_stale")
    else:
        warnings.append("graph_unavailable")
    
    # Governance (JSON primeiro, fallback para .md)
    gov_path = Path(args.governance)
    rx_path = Path(args.rx)
    
    if gov_path.exists():
        governance_data = json.loads(gov_path.read_text())
    elif rx_path.exists():
        governance_data = parse_rx_markdown(rx_path)
        warnings.append("governance_json_missing_using_rx_parse")
        if governance_data is None:
            warnings.append("rx_parse_failed")
    else:
        warnings.append("governance_unavailable")
    
    if not graph_data and not governance_data:
        print_recovery_instructions()
        exit(4)
    
    # ─── 3. BLAST ESTRUTURAL (GRAPHIFY) ───
    structural = set()
    graph_edges_detail = []
    
    if graph_data:
        for file in seed:
            node_id = file_to_node_id(file)
            if node_id in graph_data['nodes']:
                neighbors = bfs(
                    graph_data, node_id,
                    depth=select_depth(file, args.depth, args.depth_docs)
                )
                structural.update(neighbors)
                for n in neighbors:
                    edge_info = get_edge_path(graph_data, node_id, n)
                    graph_edges_detail.append({
                        "from": file, "to": n, "via": edge_info
                    })
    
    # ─── 4. BLAST DE GOVERNANÇA ───
    governance = set()
    gov_edges_detail = []
    
    if governance_data:
        for file in seed:
            matches = find_governance_matches(
                governance_data, file,
                seed_critical=any_is_critical(seed)
            )
            governance.update(matches['files'])
            gov_edges_detail.extend(matches['details'])
    
    # ─── 5. COBERTURA DO GRAFO ───
    coverage = 0.0
    if graph_data and seed:
        found_in_graph = sum(1 for s in seed if s in graph_nodes)
        coverage = found_in_graph / len(seed)
        if coverage < 0.7:
            warnings.append(f"low_graph_coverage_{coverage:.0%}")
    
    # ─── 6. CLASSIFICAÇÃO EM BUCKETS ───
    if args.mode == "propagate":
        result = classify_buckets(
            seed, structural, governance,
            graph_edges_detail, gov_edges_detail
        )
    elif args.mode == "audit":
        result = generate_drift_report(
            structural, governance, graph_edges_detail, gov_edges_detail
        )
    
    # ─── 7. GLOSSARY VALIDATION (OPCIONAL) ───
    if args.glossary_validate:
        glossary_gaps = validate_against_glossaries(result)
        result['glossary_gaps'] = glossary_gaps
    
    # ─── 8. SAÍDA ───
    output = {
        "seed": seed,
        "mode": args.mode,
        **result,
        "meta": {
            "graph_depth_code": args.depth,
            "graph_depth_docs": args.depth_docs,
            "graph_edges_considered": [
                "calls", "references", "implements",
                "contains", "defines"
            ],
            "graph_available": graph_data is not None,
            "governance_available": governance_data is not None,
            "coverage_estimate": coverage,
            "warnings": warnings
        }
    }
    
    if args.format == "json":
        print(json.dumps(output, indent=2, ensure_ascii=False))
    elif args.format == "text":
        print(format_text_report(output))
    
    exit(0)
```

### 3.7 Função: select_depth (depth adaptativo)

```python
def select_depth(file, depth_code, depth_docs):
    """Retorna depth baseado no tipo do arquivo."""
    doc_extensions = {'.md', '.txt', '.rst'}
    suffix = Path(file).suffix.lower()
    
    if suffix in doc_extensions:
        return depth_docs      # default 1
    else:
        return depth_code      # default 2
```

### 3.8 Função: classify_buckets

```python
def classify_buckets(seed, structural, governance,
                     graph_details, gov_details):
    """
    Classifica em 3 buckets com reasons detalhados.
    """
    # Remove seed dos conjuntos (seed não é blast, é origem)
    structural = structural - set(seed)
    governance = governance - set(seed)
    
    must = structural & governance
    likely = structural - governance
    declared = governance - structural
    
    def build_entry(file, bucket):
        reasons = []
        
        if file in structural:
            edges = [d for d in graph_details if d['to'] == file]
            for e in edges:
                reasons.append({
                    "source": "graph",
                    "via": f"{e['from']} → {e['via']} → {file}"
                })
        
        if file in governance:
            edges = [d for d in gov_details if d['target'] == file]
            for e in edges:
                reasons.append({
                    "source": "governance",
                    "via": f"{e['rule_id']}: {e['source']} → {file}"
                })
        
        # Priorização
        base_priority = {
            "must_update": 100,
            "likely_update": 70,
            "declared_only": 60
        }[bucket]
        
        # +10 se distância no grafo = 1
        if any(d.get('depth', 99) == 1 for d in
               [e for e in graph_details if e['to'] == file]):
            base_priority += 10
        
        # +5 se múltiplos caminhos independentes
        sources = set(r['via'] for r in reasons)
        if len(sources) > 1:
            base_priority += 5
        
        return {
            "file": file,
            "reasons": reasons,
            "priority": min(base_priority, 115),
            "in_glossary": None  # preenchido se --glossary-validate
        }
    
    result = {
        "must_update": sorted(
            [build_entry(f, "must_update") for f in must],
            key=lambda x: (-x['priority'], x['file'])
        ),
        "likely_update": sorted(
            [build_entry(f, "likely_update") for f in likely],
            key=lambda x: (-x['priority'], x['file'])
        ),
        "declared_only": sorted(
            [build_entry(f, "declared_only") for f in declared],
            key=lambda x: (-x['priority'], x['file'])
        )
    }
    
    return result
```

### 3.9 Função: generate_drift_report (--mode audit)

```python
def generate_drift_report(structural, governance,
                          graph_details, gov_details):
    """
    Compara graph vs governance e gera relatório de drift.
    Substitui rx_health_check.py (Proposta A integrada).
    """
    only_structural = structural - governance
    only_governance = governance - structural
    both = structural & governance
    
    return {
        "drift_report": {
            "aligned": sorted(both),
            "graph_only": [
                {
                    "file": f,
                    "detail": next(
                        (d['via'] for d in graph_details
                         if d['to'] == f), "unknown"
                    ),
                    "recommendation": "Consider adding to governance_edges.json"
                }
                for f in sorted(only_structural)
            ],
            "governance_only": [
                {
                    "file": f,
                    "detail": next(
                        (d['rule_id'] for d in gov_details
                         if d['target'] == f), "unknown"
                    ),
                    "recommendation": "Verify edge still exists in codebase"
                }
                for f in sorted(only_governance)
            ],
            "summary": {
                "total_structural": len(structural),
                "total_governance": len(governance),
                "aligned_count": len(both),
                "drift_structural": len(only_structural),
                "drift_governance": len(only_governance),
                "alignment_ratio": (
                    len(both) / max(len(structural | governance), 1)
                )
            }
        }
    }
```

### 3.10 Função: validate_against_glossaries

```python
def validate_against_glossaries(result):
    """
    Cruza todos os arquivos nos buckets contra
    FILE_GLOSSARY e SCRIPT_GLOSSARY.
    """
    file_glossary = load_glossary(
        ".context/brain/FILE_GLOSSARY.md"
    )
    script_glossary = load_glossary(
        ".context/brain/SCRIPT_GLOSSARY.md"
    )
    all_known = file_glossary | script_glossary
    
    gaps = []
    for bucket in ["must_update", "likely_update", "declared_only"]:
        for entry in result.get(bucket, []):
            f = entry["file"]
            entry["in_glossary"] = f in all_known
            if f not in all_known:
                gaps.append({
                    "file": f,
                    "bucket": bucket,
                    "issue": "not_in_any_glossary",
                    "action": "Add to FILE_GLOSSARY.md or SCRIPT_GLOSSARY.md"
                })
    
    return gaps
```

### 3.11 Função: check_graph_freshness

```python
def check_graph_freshness(graph_data):
    """
    Verifica se graph.json está stale comparando
    com HEAD do git.
    """
    graph_commit = graph_data.get('meta', {}).get(
        'built_from_commit', ''
    )
    if not graph_commit:
        return 999  # desconhecido, tratar como stale
    
    try:
        result = subprocess.run(
            ["git", "rev-list", "--count",
             f"{graph_commit}..HEAD"],
            capture_output=True, text=True
        )
        return int(result.stdout.strip())
    except Exception:
        return 999
```

### 3.12 Modo de Saída `--format text`

```
═══ BLAST RADIUS ═══
Seed: fileA.py, fileB.md

🔴 MUST UPDATE (2)
   105  SCRIPT_GLOSSARY.md
        ← graph: project_bundler.py → calls → this
        ← governance: roles_registry_change → this
   100  HARNESS_LOG.md
        ← governance: journal_to_harness → this

🟡 LIKELY UPDATE (1)
    70  rx-anatomy.md
        ← graph: health_sync.py → references → this

🔵 DECLARED ONLY (0)
   (none)

⚠ WARNINGS: graph_stale (12 commits behind)
📊 Coverage: 85% of seed found in graph
```

### 3.13 Entregáveis da Fase 2

| Item | Path | Ação |
|------|------|------|
| `blast_radius.py` | `.context/_scripts/blast_radius.py` | **CRIAR** |

---

## 4. FASE 3 — Integração

### 4.1 Atualização do journal-sync/SKILL.md

**Arquivo:** `.agent/skills/journal-sync/SKILL.md`

**Mudança no Step 2 (Blast Radius Calculation):**

```diff
 ### Step 2: Blast Radius Calculation
-1. Use `view_file` to read `.context/maintenance/rx-communications.md`.
-2. Use the "Propagation Seed" as search keys in Section 4 and 5.
-3. Identify all files listed under "Afeta:" for those modified files.
-4. **Raciocínio Recursivo (OBRIGATÓRIO):** ...
+1. Execute `python .context/_scripts/blast_radius.py
+   --changed <PROPAGATION_SEED_FILES> --mode propagate
+   --glossary-validate`
+2. Consuma os três buckets da saída JSON:
+   - `must_update`: OBRIGATÓRIO revisar/atualizar ou
+     justificar explicitamente no Journal.
+   - `likely_update`: Revisão obrigatória com decisão
+     explícita (atualiza/não atualiza + motivo).
+   - `declared_only`: Auditoria de consistência (validar
+     se a edge de governança ainda faz sentido).
+3. Se `warnings` não estiver vazio, ler e tratar cada
+   warning individualmente.
+4. Se `glossary_gaps` não estiver vazio, registrar no
+   Journal como gap de manutenção.
+5. **Raciocínio Recursivo (OBRIGATÓRIO):** Aplique o
+   raciocínio recursivo SOMENTE sobre os arquivos nos
+   buckets acima, não sobre o rx-communications inteiro.
+6. **Fallback:** Se blast_radius.py retornar exit != 0,
+   ler rx-communications.md manualmente como no fluxo
+   legado e registrar no Journal que o modo degradado
+   foi usado.
```

### 4.2 Hook post-commit para graphify

**Arquivo:** `.husky/post-commit` (CRIAR)

```bash
#!/bin/sh
# Atualiza graphify após commit bem-sucedido.
# Não bloqueia o commit — é fire-and-forget.
# Apenas se houve mudanças em extensões relevantes.

CHANGED=$(git diff --name-only HEAD~1 HEAD 2>/dev/null \
  | grep -E '\.(py|ts|js|md|json|sql|yml|yaml)$' \
  | head -1)

if [ -n "$CHANGED" ]; then
  echo "[graphify] Updating graph after commit..."
  # Timeout de 30s para não travar
  timeout 30 graphify update . 2>/dev/null || \
    echo "[graphify] Update skipped (timeout or error)"
fi
```

**Tornar executável:** `chmod +x .husky/post-commit`

### 4.3 Novos scripts no package.json

```json
{
  "scripts": {
    "context:blast-radius": "python .context/_scripts/blast_radius.py",
    "context:blast-audit": "python .context/_scripts/blast_radius.py --mode audit",
    "context:affinity": "python .context/_scripts/affinity_lite.py"
  }
}
```

### 4.4 Entregáveis da Fase 3

| Item | Path | Ação |
|------|------|------|
| journal-sync SKILL.md | `.agent/skills/journal-sync/SKILL.md` | **ATUALIZAR** Step 2 |
| post-commit hook | `.husky/post-commit` | **CRIAR** |
| package.json | `package.json` | **ATUALIZAR** scripts |

---

## 5. FASE 4 — Documentação

### 5.1 FLOW_PROPAGATION.md

**Arquivo:** `.context/brain/FLOW_PROPAGATION.md` (CRIAR)

Espelhamento seção-a-seção com o FLOW_SDD:

```
## 1. Visão do Organismo
   (as 3 camadas: communications, affinity, graphify)
   (metáfora biológica adaptada)

## 2. Perfil Individual dos 9 Componentes
   Tabelas idênticas ao FLOW_SDD:
   - governance_edges.json
   - blast_radius.py
   - rx-communications.md
   - graphify-out/graph.json
   - rx-affinity-lite.json
   - FILE_GLOSSARY.md
   - SCRIPT_GLOSSARY.md
   - journal-sync/SKILL.md
   - JOURNAL_SYNAPSE.md

## 3. Matriz de Propagação do Próprio Sistema
   "Se alterar blast_radius.py, o que mais muda?"
   "Se criar governance_edges.json, o que registrar?"

## 4. Sequência Operacional
   - Rito de Auditoria ("Dar uma Geral")
   - Rito de Manutenção (arquivo novo/renomeado/deletado)
   - Rito de Diagnóstico (sintomas → causas → ações)

## 5. Insights-Chave
   (callout boxes no estilo do FLOW_SDD)

## 6. Classificação por Camada
   (tabela: camada, arquivo, natureza, volatilidade)

## 7. Roadmap de Evolução
   - Phase 2: script_edges no governance_edges.json
   - Phase 3: integração affinity_lite no blast_radius
   - Phase 4: SAM enforcement (lançamento do template)
```

### 5.2 Atualização dos Glossários

**FILE_GLOSSARY.md** — adicionar entrada:

```
| governance_edges.json | `.context/maintenance/` | Versão estruturada das
  regras de adjacência de governança extraídas de rx-communications.md.
  Consumida por blast_radius.py. Atualizar quando regras de propagação
  mudarem. |
```

**SCRIPT_GLOSSARY.md** — adicionar entrada:

```
| blast_radius.py | `.context/_scripts/` | Calculadora de blast radius
  híbrida. Lê graph.json (estrutural) + governance_edges.json (governança)
  e retorna buckets priorizados. Modos: propagate (default) e audit.
  Consumida por journal-sync. Gatilho: npm run context:blast-radius |
```

### 5.3 Atualização de rx-communications.md

Adicionar nota no topo da Seção 4:

```markdown
> **NOTA:** Esta seção tem agora uma versão estruturada em
> `.context/maintenance/governance_edges.json`. O script
> `blast_radius.py` consome o JSON, não este arquivo
> diretamente. Quando alterar adjacências aqui, atualize
> o JSON também.
```

Adicionar entrada para os novos componentes na Seção 4 e 5:

```markdown
### 🆕 Sistema de Blast Radius
- **`governance_edges.json`**
  - **Afeta:** `blast_radius.py` (fonte primária de dados de governança)
  - **É Afetado Por:** Alterações manuais em `rx-communications.md` Seção 4
- **`blast_radius.py`**
  - **Afeta:** Decisões de propagação do `journal-sync`
  - **É Afetado Por:** `graphify-out/graph.json`, `governance_edges.json`
```

### 5.4 Entregáveis da Fase 4

| Item | Path | Ação |
|------|------|------|
| FLOW_PROPAGATION.md | `.context/brain/FLOW_PROPAGATION.md` | **CRIAR** |
| FILE_GLOSSARY.md | `.context/brain/FILE_GLOSSARY.md` | **ATUALIZAR** |
| SCRIPT_GLOSSARY.md | `.context/brain/SCRIPT_GLOSSARY.md` | **ATUALIZAR** |
| rx-communications.md | `.context/maintenance/rx-communications.md` | **ATUALIZAR** |

---

## 6. FASE 5 — Validação

### 6.1 Testes Unitários

**Arquivo:** `tests/test_blast_radius.py` (CRIAR)

```python
# Cenários de aceite:
class TestBlastRadius:
    
    def test_must_update_intersection(self):
        """Arquivo presente em ambos os conjuntos
        gera must_update."""
        # Seed: file que está no graph E na governance
        # Esperado: must_update contém o arquivo
    
    def test_structural_only_gives_likely(self):
        """Arquivo só no graph gera likely_update."""
        # Seed: file que está no graph mas NÃO na governance
        # Esperado: likely_update contém o arquivo
    
    def test_governance_only_gives_declared(self):
        """Arquivo só na governance gera declared_only."""
        # Seed: file que está na governance mas NÃO no graph
        # Esperado: declared_only contém o arquivo
    
    def test_new_file_with_no_edges(self):
        """Arquivo novo sem arestas gera buckets vazios
        sem erro."""
        # Seed: file que não existe em nenhum mapa
        # Esperado: 3 buckets vazios, exit 0
    
    def test_graph_unavailable_graceful(self):
        """Sem graph.json, degrada para governança."""
        # Setup: remover graph.json
        # Esperado: must_update e declared_only preenchidos,
        #   likely_update vazio, warning "graph_unavailable"
    
    def test_governance_unavailable_graceful(self):
        """Sem governance, degrada para estrutural."""
        # Setup: remover governance_edges.json e rx-communications
        # Esperado: must_update e likely_update preenchidos,
        #   declared_only vazio, warning "governance_unavailable"
    
    def test_both_unavailable_exits_4(self):
        """Sem nenhum, exit 4 com instruções."""
        # Setup: remover ambos
        # Esperado: exit 4
    
    def test_reasons_have_source_and_via(self):
        """Reasons contêm source e via, não apenas string."""
        # Verificar que cada reason é dict com source + via
    
    def test_priority_ordering(self):
        """must_update > likely_update > declared_only
        na ordenação."""
        # Verificar ordenação por priority desc
    
    def test_depth_adaptive(self):
        """Arquivos .md usam depth-docs, .py usam depth."""
        # Seed com .md e .py, verificar depths diferentes
    
    def test_wildcard_edge_activation(self):
        """RULES.md wildcard ativa condicionalmente."""
        # Seed com arquivo na layer constitucional:
        #   RULES.md em must_update
        # Seed com arquivo na layer metabolica:
        #   RULES.md em declared_only ou ausente
    
    def test_glossary_validation(self):
        """Arquivos desconhecidos aparecem em
        glossary_gaps."""
        # --glossary-validate com arquivo não no glossário
        # Esperado: glossary_gaps contém o arquivo
    
    def test_audit_mode(self):
        """Modo audit gera drift_report em vez de
        buckets."""
        # --mode audit
        # Esperado: saída contém drift_report com
        #   aligned, graph_only, governance_only, summary
```

### 6.2 Teste de Integração (Dry Run)

Após implementar tudo, rodar cenário real:

```bash
# 1. Simular alteração em um script
touch .context/_scripts/harness_runner.py

# 2. Rodar blast radius
python .context/_scripts/blast_radius.py \
  --changed .context/_scripts/harness_runner.py \
  --mode propagate \
  --glossary-validate

# 3. Verificar saída
# - must_update: HARNESS_LOG.md, SCRIPT_GLOSSARY.md, etc.
# - likely_update: arquivos que graphify vê mas governance não
# - declared_only: arquivos que governance declara mas graph não vê
# - warnings: [] (ou graph_stale se graphify não atualizado)
# - glossary_gaps: [] (ou arquivos novos)

# 4. Modo audit
python .context/_scripts/blast_radius.py \
  --changed .context/_scripts/harness_runner.py \
  --mode audit

# 5. Verificar drift report
# - aligned: arquivos que ambos concordam
# - graph_only: edges que graph vê mas governance não
# - governance_only: edges que governance declara mas graph não vê
```

### 6.3 Critérios de Aceite da Fase 5

- [ ] Todos os 12 testes passam
- [ ] Saída JSON é parseável e estável
- [ ] Modo degrade funciona (graph ausente, governance ausente)
- [ ] `--glossary-validate` identifica gaps corretamente
- [ ] `--mode audit` gera relatório de drift coerente
- [ ] `post-commit` hook executa sem travar commit
- [ ] `journal-sync` consome a saída sem precisar ler rx-communications manualmente

---

## 7. FASE 6 — Handoff e Fechamento

### 7.1 Checklist de Fechamento

```
□ governance_edges.json criado e válido
□ blast_radius.py implementado e testado
□ journal-sync SKILL.md atualizado
□ post-commit hook criado e executável
□ FLOW_PROPAGATION.md criado
□ FILE_GLOSSARY.md atualizado
□ SCRIPT_GLOSSARY.md atualizado
□ rx-communications.md atualizado com nota + novos componentes
□ package.json com novos scripts
□ tests/test_blast_radius.py com 12 cenários passando
□ Dry run executado com sucesso
□ JOURNAL.md atualizado com registro da mudança
```

### 7.2 O que NÃO fazer nesta fase

| Não fazer | Por quê |
|-----------|---------|
| Alterar JOURNAL_SYNAPSE.md | SAM não deve ser afetado agora |
| Alterar regras do SAM | Enforcement é para o lançamento |
| Integrar affinity_lite no fluxo ativo | É retrospectivo, não preditivo |
| Substituir rx-communications.md como SSOT | Ele continua como documentação narrativa |
| Implementar script_edges no governance_edges.json | Fase 2 do roadmap |

---

## 8. Cronograma Sugerido

| Fase | Dependência | Esforço Estimado |
|------|-------------|-----------------|
| Fase 1: governance_edges.json | Nenhuma | ~1 sessão (manual + schema) |
| Fase 2: blast_radius.py | Fase 1 | ~2-3 sessões (150-200 linhas) |
| Fase 3: Integração | Fase 2 | ~1 sessão |
| Fase 4: Documentação | Fase 1+2+3 | ~1-2 sessões |
| Fase 5: Validação | Fase 2+3 | ~1 sessão |
| Fase 6: Handoff | Todas | ~0.5 sessão |

**Total estimado: 6-8 sessões**

---

## 9. Mapa de Risco

| Risco | Probabilidade | Impacto | Mitigação |
|-------|--------------|---------|-----------|
| Parse de rx-communications.md frágil | Alta | Médio | governance_edges.json como fonte primária; .md como fallback |
| graph.json stale entre commits | Média | Baixo | Post-commit hook + warning no blast_radius.py |
| journal-sync não consome JSON corretamente | Baixa | Alto | Fallback para leitura manual do rx-communications.md |
| governance_edges.json desatualizado | Média | Médio | Modo audit para detectar drift periodicamente |
| blast_radius.py lento em repositórios grandes | Baixa | Médio | BFS com depth limitado; profiling se necessário |

---
