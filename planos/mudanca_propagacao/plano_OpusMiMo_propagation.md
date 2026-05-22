## Plano OpusMiMo — Blast Radius Inteligente (Lean MVP)

> **Autor:** Claude Opus 4.6 · **Data:** 2026-05-21 · **Rev:** 1.1 (incorpora feedback V2 MiMo)
> **Filosofia:** Ship → Validate → Expand. Nenhuma linha de documentação
> antes de código rodando. Nenhum JSON intermediário antes de provar
> que o parsing .md falha.
>
> **Nota Rev 1.1:** O V2 MiMo aceitou 100% da arquitetura OpusMiMo e
> produziu código funcional. Esta revisão incorpora 3 melhorias do V2:
> paths Windows-safe nos testes, localização exata no SCRIPT_GLOSSARY,
> e exemplo atualizado no journal-sync diff.

---

## 0. Visão Executiva

```
ESTADO ATUAL                          ESTADO ALVO (MVP)
─────────────                         ──────────────────
journal-sync lê 348 linhas de         journal-sync recebe lista JSON
rx-communications.md manualmente      priorizada de ~5 arquivos

IA raciocina sobre 30+ edges          IA raciocina sobre 3 buckets
por vez                               focados

graphify-out é GPS passivo            graphify-out alimenta blast radius
                                      estrutural via graph.json

rx-communications.md é SSOT           rx-communications.md CONTINUA
manual e único                        sendo SSOT (parseado direto)
```

**Entregáveis (6 arquivos):**

| # | Arquivo | Ação |
|---|---------|------|
| 1 | `.context/_scripts/blast_radius.py` | **CRIAR** (~120 linhas) |
| 2 | `.agent/skills/journal-sync/SKILL.md` | **ATUALIZAR** Step 2 |
| 3 | `.husky/post-commit` | **CRIAR** (~10 linhas) |
| 4 | `package.json` | **ATUALIZAR** (1 script) |
| 5 | `.context/brain/SCRIPT_GLOSSARY.md` | **ATUALIZAR** (1 entrada) |
| 6 | `tests/test_blast_radius.py` | **CRIAR** (6 testes) |

**Esforço total: 4-5 sessões.**

---

## 1. Fases

| Fase | O que | Sessões |
|------|-------|---------|
| **1. Motor** | `blast_radius.py` — o script core | ~2 |
| **2. Integração** | journal-sync + hook + package.json | ~1 |
| **3. Validação** | 6 testes + dry-run + glossário | ~1 |
| **4. Commit** | Journal + commit atômico | ~0.5 |

---

## 2. FASE 1 — Motor (`blast_radius.py`)

### 2.1 Premissas Validadas (contra o graph.json real)

Antes de escrever código, estas premissas foram verificadas:

```
✅ graph.json top-level keys: directed, multigraph, graph, nodes,
   links, hyperedges, built_at_commit
✅ nodes é uma LISTA (não dict) — requer pré-indexação
✅ cada node tem: id, label, source_file, file_type, community
✅ links usam: source, target (node IDs normalizados),
   relation, confidence, source_file, weight
✅ node IDs NÃO são file paths — são slugs normalizados
   ex: "init_ai_project_sh", não "init_ai_project.sh"
✅ 458 nós, 128 source_files únicos, 549 links
✅ freshness key: built_at_commit (raiz), NÃO meta.built_from_commit
✅ relation types: calls, references, implements, contains,
   defines, conceptually_related_to, semantically_similar_to,
   rationale_for, method
```

### 2.2 Interface CLI (Mínima)

```
python .context/_scripts/blast_radius.py \
  --changed fileA.py fileB.md \
  [--graph graphify-out/graph.json] \
  [--rx .context/maintenance/rx-communications.md] \
  [--format json|text]
```

Sem `--mode`, sem `--depth`, sem `--glossary-validate`.
Depth é fixo em 1. Modo é sempre propagate.

### 2.3 Exit Codes

| Code | Significado |
|------|------------|
| `0` | Sucesso — blast radius calculado |
| `2` | Input inválido — `--changed` vazio |
| `4` | Nenhuma fonte disponível (nem graph nem rx) |

Três exit codes. Não cinco.

### 2.4 Degradação

```
graph.json + rx-communications.md  →  MODO PLENO
graph.json sem rx                  →  structural only + warning
rx sem graph.json                  →  governance only + warning
nenhum                             →  exit 4
```

### 2.5 Algoritmo (Implementação Real, Não Pseudo)

A diferença principal vs. o plano MiMo: **o BFS opera no nível
de source_file, não de node_id.** Isso resolve os problemas 2.1
e 2.2 da revisão crítica.

```python
#!/usr/bin/env python3
"""
blast_radius.py — Hybrid Blast Radius Calculator
Combines graphify structural edges with rx-communications
governance edges to produce prioritized propagation buckets.

Usage:
  python blast_radius.py --changed file1.py file2.md
"""
import argparse
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

# ─── CONFIGURAÇÃO ───────────────────────────────────────
DEFAULT_GRAPH = "graphify-out/graph.json"
DEFAULT_RX = ".context/maintenance/rx-communications.md"
CROSS_FILE_RELATIONS = {
    "calls", "references", "implements",
    "rationale_for", "semantically_similar_to"
}
# Relações internas (defines, contains, method) não
# indicam propagação cross-file.


def load_graph_as_file_adjacency(graph_path: str) -> dict:
    """
    Carrega graph.json e projeta um grafo FILE→FILE.

    Estratégia: em vez de fazer BFS nos nós (que inclui
    funções, classes, conceitos), colapsa todos os nós
    para seus source_files e cria edges diretas entre
    arquivos.

    Resultado: dict[str, set[str]]
      {"fileA.py": {"fileB.py", "fileC.md"}, ...}
    """
    data = json.loads(Path(graph_path).read_text("utf-8"))

    # 1. Mapear node_id → source_file
    id_to_file = {}
    for node in data["nodes"]:
        id_to_file[node["id"]] = node.get("source_file", "")

    # 2. Projetar links em edges file→file
    file_adj = defaultdict(set)
    for link in data["links"]:
        rel = link.get("relation", "")
        if rel not in CROSS_FILE_RELATIONS:
            continue

        src_file = id_to_file.get(link["source"], "")
        tgt_file = id_to_file.get(link["target"], "")

        if src_file and tgt_file and src_file != tgt_file:
            file_adj[src_file].add(tgt_file)
            file_adj[tgt_file].add(src_file)  # bidirecional

    return dict(file_adj), data.get("built_at_commit", "")


def parse_rx_communications(rx_path: str) -> dict:
    """
    Parseia a Seção 4 do rx-communications.md.
    Extrai pares source → [targets] a partir de linhas
    contendo 'Afeta:' e 'É Afetado Por:'.

    Retorna: dict[str, set[str]]
    """
    text = Path(rx_path).read_text("utf-8")
    adjacency = defaultdict(set)
    current_file = None

    for line in text.splitlines():
        # Detectar header de arquivo: **`FILENAME`** ou ### FILENAME
        header = re.search(
            r'\*\*`([^`]+)`\*\*|^###\s+.*?`([^`]+)`', line
        )
        if header:
            current_file = header.group(1) or header.group(2)
            # Normalizar: extrair apenas o basename
            current_file = Path(current_file).name
            continue

        if not current_file:
            continue

        # Detectar "Afeta:" ou "Escreve em:"
        afeta = re.search(
            r'(?:Afeta|Escreve em)\s*:\s*(.+)', line,
            re.IGNORECASE
        )
        if afeta:
            targets = [
                t.strip().strip('`').strip()
                for t in afeta.group(1).split(',')
                if t.strip()
                and not t.strip().startswith('[')  # skip [CRÍTICO]
            ]
            for t in targets:
                clean = re.sub(r'\[.*?\]\s*', '', t).strip()
                if clean:
                    adjacency[current_file].add(Path(clean).name)

    return dict(adjacency)


def check_freshness(commit_hash: str) -> tuple:
    """Retorna (commits_behind, is_stale)."""
    if not commit_hash:
        return 999, True
    try:
        r = subprocess.run(
            ["git", "rev-list", "--count",
             f"{commit_hash[:8]}..HEAD"],
            capture_output=True, text=True, timeout=5
        )
        behind = int(r.stdout.strip())
        return behind, behind > 10
    except Exception:
        return 999, True


def normalize_seed(files: list) -> list:
    """Normaliza paths do seed para caminhos relativos."""
    result = []
    for f in files:
        p = Path(f)
        # Se absoluto, tornar relativo ao cwd
        if p.is_absolute():
            try:
                p = p.relative_to(Path.cwd())
            except ValueError:
                pass
        result.append(str(p).replace("\\", "/"))
    return result


def classify(seed, structural, governance):
    """Classifica em 3 buckets."""
    seed_basenames = {Path(s).name for s in seed}

    # Converter structural para basenames (para comparação)
    struct_set = set()
    for s in seed:
        basename = Path(s).name
        neighbors = structural.get(s, set()) | \
                    structural.get(basename, set())
        struct_set.update(neighbors)
    struct_set -= seed_basenames

    # Converter governance para basenames
    gov_set = set()
    for s in seed:
        basename = Path(s).name
        neighbors = governance.get(basename, set())
        gov_set.update(neighbors)
    gov_set -= seed_basenames

    must = struct_set & gov_set
    likely = struct_set - gov_set
    declared = gov_set - struct_set

    return {
        "must_update": sorted(must),
        "likely_update": sorted(likely),
        "declared_only": sorted(declared)
    }


def main():
    parser = argparse.ArgumentParser(
        description="Hybrid Blast Radius Calculator"
    )
    parser.add_argument(
        "--changed", nargs="+", required=True,
        help="Files in the propagation seed"
    )
    parser.add_argument(
        "--graph", default=DEFAULT_GRAPH,
        help="Path to graphify graph.json"
    )
    parser.add_argument(
        "--rx", default=DEFAULT_RX,
        help="Path to rx-communications.md"
    )
    parser.add_argument(
        "--format", choices=["json", "text"],
        default="json", help="Output format"
    )
    args = parser.parse_args()

    seed = normalize_seed(args.changed)
    if not seed:
        print("Error: --changed is empty", file=sys.stderr)
        sys.exit(2)

    warnings = []
    structural = {}
    governance = {}

    # ── Graph ──
    graph_path = Path(args.graph)
    graph_commit = ""
    if graph_path.exists():
        try:
            structural, graph_commit = \
                load_graph_as_file_adjacency(str(graph_path))
            behind, stale = check_freshness(graph_commit)
            if stale:
                warnings.append(
                    f"graph_stale_{behind}_commits_behind"
                )
        except Exception as e:
            warnings.append(f"graph_load_error: {e}")
    else:
        warnings.append("graph_unavailable")

    # ── Governance ──
    rx_path = Path(args.rx)
    if rx_path.exists():
        try:
            governance = parse_rx_communications(str(rx_path))
        except Exception as e:
            warnings.append(f"rx_parse_error: {e}")
    else:
        warnings.append("governance_unavailable")

    # ── Nenhum disponível ──
    if not structural and not governance:
        print(json.dumps({
            "error": "No data sources available",
            "recovery": [
                "Run: graphify extract . && graphify update .",
                "Verify: .context/maintenance/"
                "rx-communications.md exists"
            ]
        }, indent=2))
        sys.exit(4)

    # ── Classificação ──
    buckets = classify(seed, structural, governance)

    output = {
        "seed": seed,
        **buckets,
        "meta": {
            "graph_available": bool(structural),
            "governance_available": bool(governance),
            "graph_commit": graph_commit[:8] if graph_commit
                           else None,
            "warnings": warnings
        }
    }

    if args.format == "json":
        print(json.dumps(output, indent=2, ensure_ascii=False))
    else:
        print("═══ BLAST RADIUS ═══")
        print(f"Seed: {', '.join(seed)}")
        print()
        for bucket, emoji in [
            ("must_update", "🔴"),
            ("likely_update", "🟡"),
            ("declared_only", "🔵")
        ]:
            items = buckets[bucket]
            print(f"{emoji} {bucket.upper()} ({len(items)})")
            for f in items:
                print(f"   {f}")
            if not items:
                print("   (none)")
            print()
        if warnings:
            print(f"⚠ WARNINGS: {', '.join(warnings)}")

    sys.exit(0)


if __name__ == "__main__":
    main()
```

### 2.6 Decisões de Design Explicadas

| Decisão | Justificativa |
|---------|---------------|
| **Projetar grafo para FILE→FILE** em vez de BFS nos nós | Resolve o "Elefante na Sala" (file_to_node_id). Elimina a explosão combinatória de nós de funções. O BFS de depth=2 no grafo de nós vira uma adjacência direta no grafo de arquivos. |
| **Filtrar relações** (`CROSS_FILE_RELATIONS`) | `defines`, `contains`, `method` são relações internas de um arquivo. Não indicam que outro arquivo precisa ser atualizado. Só `calls`, `references`, `implements`, `rationale_for` e `semantically_similar_to` cruzam fronteiras de arquivo. |
| **Bidirecional** | Se A referencia B e B muda, A pode precisar de atualização. A adjacência é simétrica no nível de arquivo. |
| **Parsear rx-communications.md direto** | Sem `governance_edges.json` intermediário. Se o parsing se mostrar frágil em produção, criamos o JSON depois. YAGNI. |
| **Sem `--mode audit`** | Responsabilidade única. Se precisarmos de auditoria, será `rx_health_check.py` separado. |
| **Sem `--depth`** | No grafo projetado FILE→FILE, depth=1 (adjacência direta) já é o equivalente a depth=2 no grafo de nós. Sem necessidade de configuração. |

### 2.7 Critérios de Aceite da Fase 1

- [ ] `blast_radius.py` executa sem erro com `--changed` de 1+ arquivo
- [ ] Saída JSON é parseável por `json.loads()`
- [ ] Modo pleno: 3 buckets preenchidos quando ambas as fontes existem
- [ ] Modo degradado graph: warning `graph_unavailable`, buckets baseados em governance
- [ ] Modo degradado governance: warning `governance_unavailable`, buckets baseados em graph
- [ ] Nenhuma fonte: exit 4 com mensagem de recuperação

---

## 3. FASE 2 — Integração

### 3.1 Atualização do journal-sync/SKILL.md

**Arquivo:** `.agent/skills/journal-sync/SKILL.md`

**Mudança no Step 2:**

```diff
 ### Step 2: Blast Radius Calculation (Raciocínio Recursivo)
-1. Use `view_file` to read `.context/maintenance/rx-communications.md`.
-2. Use the "Propagation Seed" as search keys in Section 4 and 5 (Adjacency Lists).
-3. Identify all files listed under **"Afeta:"** (or "Escreve em:") for those modified files.
+1. Execute `python .context/_scripts/blast_radius.py --changed <PROPAGATION_SEED_FILES> --format text`
+2. Read the three output buckets:
+   - `must_update`: Both graph and governance agree — OBRIGATÓRIO atualizar ou justificar.
+   - `likely_update`: Graph found connection, governance doesn't declare — revisar com atenção.
+   - `declared_only`: Governance declares, graph doesn't see — validar se edge ainda faz sentido.
+3. If `warnings` is not empty, note them in the Journal entry.
 4. **Raciocínio Recursivo (OBRIGATÓRIO):** Para CADA arquivo listado nos buckets, responda mentalmente:
    > "A natureza específica da minha alteração realmente impacta o CONTEÚDO deste arquivo alvo?"
    - **SIM** → Inclua na propagação e na Matriz `[x]`.
    - **NÃO** → Descarte. Não propague só porque o bucket sugere.
    - **Arquivo não listado, mas detectou impacto real** → Propague mesmo assim.
+5. **Fallback:** Se `blast_radius.py` retornar exit ≠ 0, ler `rx-communications.md`
+   manualmente (fluxo legado) e registrar no Journal que modo degradado foi usado.
```

### 3.2 Hook post-commit

**Arquivo:** `.husky/post-commit` (**CRIAR**)

```bash
#!/bin/sh
# Atualiza graphify após commit. Fire-and-forget.
# Não bloqueia — erro não impede nada.

# Guard: só roda se graphify está instalado
command -v graphify >/dev/null 2>&1 || exit 0

# Guard: só roda se houve mudança em arquivo relevante
CHANGED=$(git diff --name-only HEAD~1 HEAD 2>/dev/null \
  | grep -E '\.(py|ts|js|md|json|sql|yml|yaml)$' \
  | head -1)

[ -z "$CHANGED" ] && exit 0

echo "[graphify] Updating graph..."
graphify update . 2>/dev/null &
# Background — não espera resultado
```

**Nota Windows:** Husky no Windows roda via Git Bash,
então `#!/bin/sh` funciona. Se o user usar PowerShell
diretamente, o hook precisa de adaptação. Documentar
como requisito no SCRIPT_GLOSSARY.

### 3.3 package.json

```json
{
  "scripts": {
    "context:blast-radius": "python .context/_scripts/blast_radius.py",
    "context:affinity": "python .context/_scripts/affinity_lite.py"
  }
}
```

Adicionar ambos. O `context:affinity` estava pendente desde
antes deste plano (marcado como "a ser adicionado" no
SCRIPT_GLOSSARY original).

### 3.4 Critérios de Aceite da Fase 2

- [ ] `journal-sync` SKILL.md atualizado com novo Step 2
- [ ] Fallback documentado no Step 5
- [ ] `.husky/post-commit` criado com guard e nota Windows
- [ ] `package.json` com ambos scripts

---

## 4. FASE 3 — Validação

### 4.1 Testes Unitários (6 Core)

**Arquivo:** `tests/test_blast_radius.py` (**CRIAR**)

```python
"""Tests for blast_radius.py — 6 core scenarios."""
import json
import pytest
import subprocess
import sys
import tempfile
from pathlib import Path
from blast_radius import classify

class TestClassifyBuckets:
    def test_both_agree_gives_must_update(self):
        seed = ["fileA.py"]
        structural = {"fileA.py": {"shared.md"}}
        governance = {"fileA.py": {"shared.md"}}
        result = classify(seed, structural, governance)
        assert "shared.md" in result["must_update"]

    def test_structural_only_gives_likely(self):
        seed = ["fileA.py"]
        structural = {"fileA.py": {"only_graph.md"}}
        governance = {}
        result = classify(seed, structural, governance)
        assert "only_graph.md" in result["likely_update"]

    def test_governance_only_gives_declared(self):
        seed = ["fileA.py"]
        structural = {}
        governance = {"fileA.py": {"only_gov.md"}}
        result = classify(seed, structural, governance)
        assert "only_gov.md" in result["declared_only"]

    def test_no_matches_gives_empty_buckets(self):
        seed = ["unknown.py"]
        structural = {"other.py": {"x.md"}}
        governance = {"other.py": {"y.md"}}
        result = classify(seed, structural, governance)
        assert all(not result[k] for k in ["must_update", "likely_update", "declared_only"])

    def test_seed_excluded_from_buckets(self):
        seed = ["fileA.py"]
        structural = {"fileA.py": {"fileA.py", "fileB.py"}}
        governance = {"fileA.py": {"fileA.py", "fileB.py"}}
        result = classify(seed, structural, governance)
        assert "fileA.py" not in result["must_update"]
        assert "fileB.py" in result["must_update"]

class TestDegradation:
    def test_both_unavailable_exits_4(self):
        SCRIPT = Path(".context/_scripts/blast_radius.py")
        no_exist = Path(tempfile.gettempdir()) / "__no_exist_test"
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--changed", "nonexistent.py",
             "--graph", str(no_exist / "graph.json"), "--rx", str(no_exist / "rx.md")],
            capture_output=True, text=True
        )
        assert result.returncode == 4
```

### 4.2 Dry Run Manual
Validar com: `npm run context:blast-radius -- --changed README.md --format text`.

### 4.3 Atualização do SCRIPT_GLOSSARY.md

Adicionar entrada na seção **"Motores Epistemológicos"**, após `inject_learnings.py`:

```markdown
| `blast_radius.py` | **Radar de Blast Radius** | Calculadora híbrida de impacto de propagação. Combina o grafo estrutural do Graphify (`graph.json`) com o mapa de governança (`rx-communications.md`) para retornar 3 buckets priorizados: `must_update` (ambas concordam), `likely_update` (só estrutural), `declared_only` (só governança). Consumido pelo skill `journal-sync` no Step 2. Degrada graciosamente quando Graphify não está disponível. | `npm run context:blast-radius -- --changed file1.py file2.md` |
```

### 4.4 Critérios de Aceite da Fase 3

- [ ] 6 testes passam
- [ ] Dry run nos 4 cenários produz resultados coerentes
- [ ] SCRIPT_GLOSSARY.md atualizado
- [ ] rx-communications.md atualizado (nota + entrada blast_radius)

---

## 5. FASE 4 — Commit

### 5.1 Journal Entry

```markdown
## Entrada — Blast Radius Inteligente

Ultima Atualizacao: <TIMESTAMP>

### Contexto
Implementação do sistema de blast radius híbrido conforme
`planos/mudanca_propagacao/plano_OpusMiMo_propagation.md`.
Integra graphify-out (estrutural) com rx-communications.md
(governança) para alimentar o journal-sync com listas
priorizadas em vez de leitura manual de 348 linhas.

### Matriz de Propagação
- [x] `.context/_scripts/blast_radius.py` (NOVO)
- [x] `.agent/skills/journal-sync/SKILL.md` (Step 2)
- [x] `.husky/post-commit` (NOVO)
- [x] `package.json` (scripts)
- [x] `.context/brain/SCRIPT_GLOSSARY.md` (entrada)
- [x] `tests/test_blast_radius.py` (NOVO)

executor_context_id: <ID>
validator_context_id: <ID>
status: READY TO COMMIT
```

### 5.2 Commit Message

```
feat(propagation): add blast_radius.py hybrid calculator

- Combines graphify graph.json (structural) with
  rx-communications.md (governance) into 3 prioritized
  buckets: must_update, likely_update, declared_only
- Updates journal-sync SKILL.md Step 2 to consume
  blast_radius output instead of manual 348-line read
- Adds post-commit hook for graphify auto-update
- 6 core tests

Refs: planos/mudanca_propagacao/plano_OpusMiMo_propagation.md
```

---

## 6. O que NÃO fazer (Scope Guard)

| Não fazer agora | Por quê | Quando fazer |
|-----------------|---------|--------------|
| `governance_edges.json` | YAGNI — parsear .md direto funciona | Se parsing falhar 3+ vezes em produção |
| `FLOW_PROPAGATION.md` | Documentação prematura | Após 2-3 sprints com blast_radius rodando |
| `--mode audit` | Mistura responsabilidades | `rx_health_check.py` separado, se necessário |
| `--glossary-validate` | Feature opcional, não core | Sprint seguinte, se glossary gaps forem problema |
| `--depth` configurável | No grafo FILE→FILE, depth é sempre 1 | Nunca (design resolve isso) |
| Alterar JOURNAL_SYNAPSE | SAM não deve ser afetado | Release do template |
| Alterar SAM | Enforcement é para o lançamento | Release do template |
| 12 testes | 6 cobrem o core | Quando expandir features |

---

## 7. Riscos e Mitigações

| Risco | P | I | Mitigação |
|-------|---|---|-----------|
| Parsing de rx-communications.md frágil (regex) | Média | Médio | Se falhar 3+ vezes → criar `governance_edges.json`. O fallback manual no journal-sync garante que nunca é pior que hoje. |
| graph.json stale | Média | Baixo | post-commit hook + warning no output. O blast radius sem graph ainda funciona (governance-only). |
| Saída muito ruidosa (muitos arquivos em buckets) | Média | Médio | Filtrar `CROSS_FILE_RELATIONS` (já feito). Se persistir, adicionar threshold de confiança nos edges. |
| journal-sync IA não consome JSON corretamente | Baixa | Alto | Fallback para leitura manual. Incluir `--format text` no SKILL.md para output humano-legível. |

---

## 8. Evolução Futura (Roadmap Pós-MVP)

Estas são evoluções que **só devem ser implementadas após
validação do MVP em produção:**

```
Sprint N+1: governance_edges.json (se parsing .md frágil)
Sprint N+2: rx_health_check.py (modo audit separado)
Sprint N+3: --glossary-validate (se gaps forem problema)
Sprint N+4: FLOW_PROPAGATION.md (com dados reais de uso)
Sprint N+5: Integrar affinity_lite como validação cruzada
```

---

## 9. Diferenças vs. plano_mimo_propagation.md

| Aspecto | MiMo | OpusMiMo |
|---------|------|----------|
| Fases | 6 | 4 |
| Entregáveis | 10 | 6 |
| Linhas de código | ~400 | ~120 |
| Testes | 12 | 6 |
| Sessões estimadas | 6-8 | 4-5 |
| governance_edges.json | Fase 1 obrigatória | YAGNI — adiado |
| FLOW_PROPAGATION.md | Fase 4 obrigatória | Adiado pós-validação |
| --mode audit | Dentro do blast_radius.py | Script separado (futuro) |
| BFS strategy | Node-level, depth=2 | File-projected, adjacência direta |
| file_to_node_id() | Não especificado | Eliminado pelo design FILE→FILE |
| graph.json freshness key | `meta.built_from_commit` ❌ | `built_at_commit` (raiz) ✅ |
| nodes lookup | `if id in data['nodes']` ❌ | Pré-indexado em dict ✅ |
