# Plano Final — Blast Radius Inteligente (Lean MVP)

> **Consolidado por:** Claude Opus 4.6 · **Data:** 2026-05-21
> **Fontes:** OpusMiMo Rev 1.1 (arquitetura + premissas validadas) +
> V2 MiMo (código funcional + localização exata no GLOSSARY) +
> Revisão crítica (formato real do JOURNAL.md)
>
> **Filosofia:** Ship → Validate → Expand.
> Nenhuma documentação antes de código rodando.
> Nenhum JSON intermediário antes de provar que o parsing .md falha.

---

## 0. Visão Executiva

```
ESTADO ATUAL                          ESTADO ALVO (MVP)
─────────────                         ──────────────────
journal-sync lê 348 linhas de         journal-sync recebe lista
rx-communications.md manualmente      priorizada de ~5 arquivos

IA raciocina sobre 30+ edges          IA raciocina sobre 3 buckets
por vez                               focados

graphify-out é GPS passivo            graphify-out alimenta blast
                                      radius estrutural via graph.json

rx-communications.md é SSOT           rx-communications.md CONTINUA
manual e único                        sendo SSOT (parseado direto)
```

**Entregáveis (7 arquivos — inclui o próprio JOURNAL):**

| # | Arquivo | Ação |
|---|---------|------|
| 1 | `.context/_scripts/blast_radius.py` | **CRIAR** (~170 linhas) |
| 2 | `.agent/skills/journal-sync/SKILL.md` | **ATUALIZAR** Step 2 |
| 3 | `.husky/post-commit` | **CRIAR** (~12 linhas) |
| 4 | `package.json` | **ATUALIZAR** (2 scripts) |
| 5 | `.context/brain/SCRIPT_GLOSSARY.md` | **ATUALIZAR** (1 entrada) |
| 6 | `tests/test_blast_radius.py` | **CRIAR** (6 testes) |
| 7 | `.context/maintenance/JOURNAL.md` | **ATUALIZAR** (1 entrada) |

**Esforço total: 4-5 sessões.**

---

## 1. Fases

| Fase | O que | Sessões |
|------|-------|---------|
| **1. Motor** | `blast_radius.py` — o script core | ~2 |
| **2. Integração** | journal-sync + hook + package.json | ~1 |
| **3. Validação** | 6 testes + dry-run + glossário | ~1 |
| **4. Commit** | Journal entry + commit atômico | ~0.5 |

---

## 2. FASE 1 — Motor (`blast_radius.py`)

### 2.1 Premissas Validadas (contra o graph.json real)

Antes de escrever código, estas premissas foram verificadas
executando queries diretas no `graph.json` do repositório:

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
Depth é fixo em 1 (adjacência direta no grafo FILE→FILE).
Modo é sempre propagate.

### 2.3 Exit Codes

| Code | Significado |
|------|------------|
| `0` | Sucesso — blast radius calculado |
| `2` | Input inválido — `--changed` vazio |
| `4` | Nenhuma fonte disponível (nem graph nem rx) |

Três exit codes. Não cinco.

### 2.4 Degradação

```
graph.json + rx-communications.md  →  MODO PLENO (3 buckets)
graph.json sem rx                  →  structural only + warning
rx sem graph.json                  →  governance only + warning
nenhum                             →  exit 4 + mensagem de recovery
```

### 2.5 Decisões de Design

| Decisão | Justificativa |
|---------|---------------|
| **Projetar grafo para FILE→FILE** em vez de BFS nos nós | Resolve o "Elefante na Sala" (`file_to_node_id`). Elimina a explosão combinatória de nós de funções. O BFS de depth=2 no grafo de nós vira uma adjacência direta no grafo de arquivos. |
| **Filtrar relações** (`CROSS_FILE_RELATIONS`) | `defines`, `contains`, `method` são relações internas de um arquivo. Não indicam que outro arquivo precisa ser atualizado. Só `calls`, `references`, `implements`, `rationale_for` e `semantically_similar_to` cruzam fronteiras de arquivo. |
| **Bidirecional** | Se A referencia B e B muda, A pode precisar de atualização. A adjacência é simétrica no nível de arquivo. |
| **Parsear rx-communications.md direto** | Sem `governance_edges.json` intermediário. Se o parsing se mostrar frágil em produção, criamos o JSON depois. YAGNI. |
| **Sem `--mode audit`** | Responsabilidade única. Se precisarmos de auditoria, será `rx_health_check.py` separado. |
| **Sem `--depth`** | No grafo projetado FILE→FILE, depth=1 (adjacência direta) já é o equivalente a depth=2 no grafo de nós. Sem necessidade de configuração. |

### 2.6 Código Completo

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


def load_graph_as_file_adjacency(graph_path: str) -> tuple:
    """
    Carrega graph.json e projeta um grafo FILE→FILE.
    Colapsa nós (funções, classes, conceitos) em seus
    source_files, criando edges diretas entre arquivos.
    """
    data = json.loads(
        Path(graph_path).read_text(encoding="utf-8")
    )

    # nodes é uma LISTA — pré-indexar
    id_to_file: dict[str, str] = {}
    for node in data.get("nodes", []):
        id_to_file[node["id"]] = node.get("source_file", "")

    # Projetar links em edges file→file
    file_adj: dict[str, set[str]] = defaultdict(set)
    for link in data.get("links", []):
        rel = link.get("relation", "")
        if rel not in CROSS_FILE_RELATIONS:
            continue
        src_file = id_to_file.get(link.get("source", ""), "")
        tgt_file = id_to_file.get(link.get("target", ""), "")
        if src_file and tgt_file and src_file != tgt_file:
            file_adj[src_file].add(tgt_file)
            file_adj[tgt_file].add(src_file)

    return dict(file_adj), data.get("built_at_commit", "")


def parse_rx_communications(rx_path: str) -> dict:
    """
    Parseia a Seção 4 do rx-communications.md.
    Extrai pares source → [targets] a partir das linhas
    'Afeta:' e 'Escreve em:'.
    """
    text = Path(rx_path).read_text(encoding="utf-8")
    adjacency: dict[str, set[str]] = defaultdict(set)
    current_file = None

    for line in text.splitlines():
        # Header de arquivo: **`FILENAME`** ou ### FILENAME
        header = re.search(
            r'\*\*`([^`]+)`\*\*|^###\s+.*?`([^`]+)`',
            line
        )
        if header:
            current_file = header.group(1) or header.group(2)
            current_file = Path(current_file).name
            continue

        if not current_file:
            continue

        # Linhas "Afeta:" ou "Escreve em:"
        afeta = re.search(
            r'(?:Afeta|Escreve em)\s*:\s*(.+)',
            line, re.IGNORECASE
        )
        if afeta:
            raw_targets = afeta.group(1).split(",")
            for t in raw_targets:
                # Limpar: remover [CRÍTICO], backticks, etc.
                clean = re.sub(
                    r'\[.*?\]\s*', '', t
                ).strip().strip('`').strip()
                if clean:
                    adjacency[current_file].add(
                        Path(clean).name
                    )

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
    """Normaliza paths do seed."""
    result = []
    for f in files:
        p = Path(f)
        if p.is_absolute():
            try:
                p = p.relative_to(Path.cwd())
            except ValueError:
                pass
        result.append(str(p).replace("\\", "/"))
    return result


def classify(
    seed: list,
    structural: dict[str, set[str]],
    governance: dict[str, set[str]]
) -> dict:
    """Classifica em 3 buckets."""
    seed_basenames = {Path(s).name for s in seed}

    # Structural → basenames
    struct_set: set[str] = set()
    for s in seed:
        basename = Path(s).name
        neighbors = (
            structural.get(s, set()) |
            structural.get(basename, set())
        )
        struct_set.update(neighbors)
    struct_set -= seed_basenames

    # Governance → basenames
    gov_set: set[str] = set()
    for s in seed:
        basename = Path(s).name
        neighbors = governance.get(basename, set())
        gov_set.update(neighbors)
    gov_set -= seed_basenames

    # Classificar
    must = struct_set & gov_set
    likely = struct_set - gov_set
    declared = gov_set - struct_set

    return {
        "must_update": sorted(must),
        "likely_update": sorted(likely),
        "declared_only": sorted(declared),
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
        default="json",
        help="Output format"
    )
    args = parser.parse_args()

    seed = normalize_seed(args.changed)
    if not seed:
        print("Error: --changed is empty",
              file=sys.stderr)
        sys.exit(2)

    warnings: list[str] = []
    structural: dict[str, set[str]] = {}
    governance: dict[str, set[str]] = {}
    graph_commit = ""

    # ── Graph ──
    graph_path = Path(args.graph)
    if graph_path.exists():
        try:
            structural, graph_commit = \
                load_graph_as_file_adjacency(
                    str(graph_path)
                )
            behind, stale = check_freshness(graph_commit)
            if stale:
                warnings.append(
                    f"graph_stale_{behind}_commits"
                )
        except Exception as e:
            warnings.append(f"graph_load_error: {e}")
    else:
        warnings.append("graph_unavailable")

    # ── Governance ──
    rx_path = Path(args.rx)
    if rx_path.exists():
        try:
            governance = parse_rx_communications(
                str(rx_path)
            )
        except Exception as e:
            warnings.append(f"rx_parse_error: {e}")
    else:
        warnings.append("governance_unavailable")

    # ── Nenhuma fonte ──
    if not structural and not governance:
        print(json.dumps({
            "error": "No data sources available",
            "recovery": [
                "Run: graphify extract . "
                "&& graphify update .",
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
            "graph_commit": (
                graph_commit[:8]
                if graph_commit else None
            ),
            "warnings": warnings,
        },
    }

    if args.format == "json":
        print(json.dumps(
            output, indent=2, ensure_ascii=False
        ))
    else:
        print("═" * 50)
        print("  BLAST RADIUS")
        print("═" * 50)
        print(f"Seed: {', '.join(seed)}")
        print()
        for bucket, emoji in [
            ("must_update", "🔴"),
            ("likely_update", "🟡"),
            ("declared_only", "🔵"),
        ]:
            items = buckets[bucket]
            print(
                f"{emoji} {bucket.upper()} ({len(items)})"
            )
            for f in items:
                print(f"   {f}")
            if not items:
                print("   (none)")
            print()
        if warnings:
            print(
                f"⚠ WARNINGS: {', '.join(warnings)}"
            )

    sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nAborted.", file=sys.stderr)
        sys.exit(130)
    except Exception as e:
        print(f"Internal error: {e}", file=sys.stderr)
        sys.exit(5)
```

### 2.7 Critérios de Aceite da Fase 1

- [ ] `blast_radius.py` executa sem erro com `--changed` de 1+ arquivo
- [ ] Saída JSON é parseável por `json.loads()`
- [ ] Modo pleno: 3 buckets preenchidos quando ambas as fontes existem
- [ ] Modo degradado graph: warning `graph_unavailable`, buckets governance-only
- [ ] Modo degradado governance: warning `governance_unavailable`, buckets structural-only
- [ ] Nenhuma fonte: exit 4 com mensagem de recuperação

---

## 3. FASE 2 — Integração

### 3.1 Atualização do journal-sync/SKILL.md

**Arquivo:** `.agent/skills/journal-sync/SKILL.md`

**Diff do Step 2** (substituir as linhas 1-4 do Step atual, manter Raciocínio Recursivo, atualizar exemplo):

```diff
 ### Step 2: Blast Radius Calculation (Raciocínio Recursivo)
-1. Use `view_file` to read `.context/maintenance/rx-communications.md`.
-2. Use the "Propagation Seed" as search keys in Section 4 and 5 (Adjacency Lists).
-3. Identify all files listed under **"Afeta:"** (or "Escreve em:") for those modified files.
-4. **Raciocínio Recursivo (OBRIGATÓRIO):** Para CADA arquivo listado como afetado, responda mentalmente:
+1. Execute `python .context/_scripts/blast_radius.py --changed <PROPAGATION_SEED_FILES> --format text`
+2. Read the three output buckets:
+   - `must_update`: Both graph and governance agree — OBRIGATÓRIO atualizar ou justificar.
+   - `likely_update`: Graph found connection, governance doesn't declare — revisar com atenção.
+   - `declared_only`: Governance declares, graph doesn't see — validar se edge ainda faz sentido.
+3. If `warnings` is not empty, note them in the Journal entry.
+4. **Raciocínio Recursivo (OBRIGATÓRIO):** Para CADA arquivo listado nos buckets, responda mentalmente:
    > "A natureza específica da minha alteração realmente impacta o CONTEÚDO deste arquivo alvo?"
    - **SIM** → Inclua na propagação e na Matriz `[x]`.
    - **NÃO** → Descarte. Não propague só porque o bucket sugere.
-   - **Arquivo não listado, mas detectou impacto real** → Propague mesmo assim (rx-communications pode estar desatualizado).
+   - **Arquivo não listado, mas detectou impacto real** → Propague mesmo assim.

-   **Exemplo correto:** Mudei `spec-driver.md` (nova Skill 10). rx-communications diz: afeta `RULES.md`, `MASTER_FLOW.md`, `AGENT_REGISTRY.md`. Raciocínio: `AGENT_REGISTRY` → SIM (version bump). `MASTER_FLOW` → SIM (diagrama de skills). `RULES.md` → NÃO (nenhuma regra nova criada).
+   **Exemplo correto:** Mudei `spec-driver.md` (nova Skill 10). blast_radius retorna: `must_update: [MASTER_FLOW.md, AGENT_REGISTRY.md]`, `declared_only: [RULES.md]`. Raciocínio: `AGENT_REGISTRY` → SIM (version bump). `MASTER_FLOW` → SIM (diagrama de skills). `RULES.md` → NÃO (nenhuma regra nova criada).

    **Exemplo errado (propagação cega):** Mudei condição de ativação no `sobriedade-operacional.md` → propagar para `RULES.md` e `AGENT_REGISTRY.md` ← ERRADO. A mudança é cosmética/condicional, não altera regras nem roles.
+5. **Fallback:** Se `blast_radius.py` retornar exit ≠ 0, ler `rx-communications.md` manualmente (fluxo legado) e registrar no Journal que modo degradado foi usado.
```

**Versão completa do Step 2 atualizado (para aplicar):**

```markdown
### Step 2: Blast Radius Calculation (Raciocínio Recursivo)
1. Execute `python .context/_scripts/blast_radius.py --changed <PROPAGATION_SEED_FILES> --format text`
2. Read the three output buckets:
   - `must_update`: Both graph and governance agree — OBRIGATÓRIO atualizar ou justificar.
   - `likely_update`: Graph found connection, governance doesn't declare — revisar com atenção.
   - `declared_only`: Governance declares, graph doesn't see — validar se edge ainda faz sentido.
3. If `warnings` is not empty, note them in the Journal entry.
4. **Raciocínio Recursivo (OBRIGATÓRIO):** Para CADA arquivo listado nos buckets, responda mentalmente:
   > "A natureza específica da minha alteração realmente impacta o CONTEÚDO deste arquivo alvo?"
   - **SIM** → Inclua na propagação e na Matriz `[x]`.
   - **NÃO** → Descarte. Não propague só porque o bucket sugere.
   - **Arquivo não listado, mas detectou impacto real** → Propague mesmo assim.

   **Exemplo correto:** Mudei `spec-driver.md` (nova Skill 10). blast_radius retorna: `must_update: [MASTER_FLOW.md, AGENT_REGISTRY.md]`, `declared_only: [RULES.md]`. Raciocínio: `AGENT_REGISTRY` → SIM (version bump). `MASTER_FLOW` → SIM (diagrama de skills). `RULES.md` → NÃO (nenhuma regra nova criada).

   **Exemplo errado (propagação cega):** Mudei condição de ativação no `sobriedade-operacional.md` → propagar para `RULES.md` e `AGENT_REGISTRY.md` ← ERRADO. A mudança é cosmética/condicional, não altera regras nem roles.
5. **Fallback:** Se `blast_radius.py` retornar exit ≠ 0, ler `rx-communications.md` manualmente (fluxo legado) e registrar no Journal que modo degradado foi usado.
```

### 3.2 Hook post-commit

**Arquivo:** `.husky/post-commit` (**CRIAR**)

```bash
#!/bin/sh
# Atualiza graphify após commit. Fire-and-forget.
# Não bloqueia — erro não impede nada.
# Nota: requer Git Bash no Windows (Husky roda via sh).

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

Após criar: `chmod +x .husky/post-commit`

**Nota Windows:** Husky no Windows roda via Git Bash,
então `#!/bin/sh` funciona. Se alguém usar PowerShell
diretamente, o hook precisa de adaptação.

### 3.3 package.json

Adicionar 2 scripts na seção `"scripts"`:

```json
"context:blast-radius": "python .context/_scripts/blast_radius.py",
"context:affinity": "python .context/_scripts/affinity_lite.py"
```

O `context:affinity` estava pendente desde antes deste plano
(marcado como "a ser adicionado" no SCRIPT_GLOSSARY original).

### 3.4 Critérios de Aceite da Fase 2

- [ ] `journal-sync` SKILL.md atualizado com novo Step 2 (diff acima)
- [ ] Fallback documentado no Step 5
- [ ] `.husky/post-commit` criado com guard para graphify ausente
- [ ] `package.json` com ambos scripts (`context:blast-radius` + `context:affinity`)

---

## 4. FASE 3 — Validação

### 4.1 Testes Unitários (6 Core)

**Arquivo:** `tests/test_blast_radius.py` (**CRIAR**)

```python
"""Tests for blast_radius.py — 6 core scenarios."""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / \
    ".context" / "_scripts" / "blast_radius.py"
SCRIPT_DIR = SCRIPT.parent

sys.path.insert(0, str(SCRIPT_DIR))

from blast_radius import classify


class TestClassifyBuckets:

    def test_both_agree_gives_must_update(self):
        """Arquivo em ambos → must_update."""
        seed = ["fileA.py"]
        structural = {"fileA.py": {"shared.md"}}
        governance = {"fileA.py": {"shared.md"}}
        result = classify(seed, structural, governance)
        assert "shared.md" in result["must_update"]
        assert "shared.md" not in result["likely_update"]
        assert "shared.md" not in result["declared_only"]

    def test_structural_only_gives_likely(self):
        """Só no graph → likely_update."""
        seed = ["fileA.py"]
        structural = {"fileA.py": {"only_graph.md"}}
        governance = {}
        result = classify(seed, structural, governance)
        assert "only_graph.md" in result["likely_update"]
        assert "only_graph.md" not in result["must_update"]

    def test_governance_only_gives_declared(self):
        """Só na governance → declared_only."""
        seed = ["fileA.py"]
        structural = {}
        governance = {"fileA.py": {"only_gov.md"}}
        result = classify(seed, structural, governance)
        assert "only_gov.md" in result["declared_only"]
        assert "only_gov.md" not in result["must_update"]

    def test_no_matches_gives_empty_buckets(self):
        """Seed sem edges → buckets vazios."""
        seed = ["unknown.py"]
        structural = {"other.py": {"x.md"}}
        governance = {"other.py": {"y.md"}}
        result = classify(seed, structural, governance)
        assert result["must_update"] == []
        assert result["likely_update"] == []
        assert result["declared_only"] == []

    def test_seed_excluded_from_buckets(self):
        """Seed não aparece nos buckets."""
        seed = ["fileA.py"]
        structural = {"fileA.py": {"fileA.py", "fileB.py"}}
        governance = {"fileA.py": {"fileA.py", "fileB.py"}}
        result = classify(seed, structural, governance)
        assert "fileA.py" not in result["must_update"]
        assert "fileB.py" in result["must_update"]


class TestDegradation:

    def test_both_unavailable_exits_4(self):
        """Sem nenhuma fonte → exit 4."""
        no_exist = Path(tempfile.gettempdir()) / \
            "__blast_radius_test_no_exist"
        result = subprocess.run(
            [
                sys.executable, str(SCRIPT),
                "--changed", "nonexistent.py",
                "--graph", str(no_exist / "graph.json"),
                "--rx", str(no_exist / "rx.md"),
            ],
            capture_output=True, text=True,
        )
        assert result.returncode == 4
        output = json.loads(result.stdout)
        assert "error" in output
```

### 4.2 Dry Run Manual

Após implementar, executar com seeds reais:

```bash
# Cenário 1: Script central
python .context/_scripts/blast_radius.py \
  --changed .context/_scripts/harness_runner.py \
  --format text

# Cenário 2: Documento de governança
python .context/_scripts/blast_radius.py \
  --changed .context/brain/RULES.md \
  --format text

# Cenário 3: Arquivo sem edges (esperar buckets vazios)
python .context/_scripts/blast_radius.py \
  --changed README.md \
  --format text

# Cenário 4: Múltiplos seeds
python .context/_scripts/blast_radius.py \
  --changed .context/_scripts/affinity_lite.py \
            .context/maintenance/JOURNAL.md \
  --format json
```

**Validação humana:** O resultado dos cenários 1 e 2 deve
ser comparado manualmente com a Seção 4 do
`rx-communications.md` para confirmar coerência.

### 4.3 Atualização do SCRIPT_GLOSSARY.md

Adicionar entrada na seção **"Motores Epistemológicos"**, após `inject_learnings.py`:

```markdown
| `blast_radius.py` | **Radar de Blast Radius** | Calculadora híbrida de impacto de propagação. Combina o grafo estrutural do Graphify (`graph.json`) com o mapa de governança (`rx-communications.md`) para retornar 3 buckets priorizados: `must_update` (ambas concordam), `likely_update` (só estrutural), `declared_only` (só governança). Consumido pelo skill `journal-sync` no Step 2. Degrada graciosamente quando Graphify não está disponível. | `npm run context:blast-radius -- --changed file1.py file2.md` |
```

### 4.4 Atualização do rx-communications.md

Adicionar entrada para `blast_radius.py` na Seção 5 (Scripts), com:

```markdown
**`blast_radius.py`**
- **Lê:** `graphify-out/graph.json`, `.context/maintenance/rx-communications.md`
- **Escreve em:** stdout (JSON ou text)
- **Afeta:** `journal-sync` (consumido no Step 2)
- **Gatilho:** Manual via `npm run context:blast-radius` ou invocado pelo journal-sync
```

### 4.5 Critérios de Aceite da Fase 3

- [ ] 6 testes passam (5 unitários `classify` + 1 integração `exit 4`)
- [ ] Dry run nos 4 cenários produz resultados coerentes
- [ ] SCRIPT_GLOSSARY.md atualizado (seção Motores Epistemológicos)
- [ ] rx-communications.md atualizado (Seção 5 — scripts)

---

## 5. FASE 4 — Commit

### 5.1 Journal Entry

Formato validado contra o JOURNAL.md real do projeto (frontmatter
no topo do arquivo, entradas com `## 📅`, `**Estado Atual:**`,
`**Matriz de Propagação:**`, metadados no final).

**Posição:** A nova entry vai no **TOPO** do arquivo (abaixo do
frontmatter). O JOURNAL é cronológico inverso — mais recente primeiro.

```markdown
## 📅 YYYY-MM-DD HH:MM | ⚙️ Feature: Blast Radius Inteligente (Lean MVP) #Propagation #BlastRadius #Tooling #Graphify
**Estado Atual:**
- [x] **Script Core:** Criado `blast_radius.py` (~170 linhas) — calculadora híbrida FILE→FILE que combina `graph.json` + `rx-communications.md` em 3 buckets priorizados.
- [x] **Integração journal-sync:** Step 2 reescrito para consumir output do `blast_radius.py` com fallback para leitura manual (Step 5).
- [x] **Hook:** Criado `.husky/post-commit` para `graphify update .` em background (fire-and-forget).
- [x] **Scripts npm:** Adicionados `context:blast-radius` e `context:affinity` no `package.json`.
- [x] **Glossário:** Entrada para `blast_radius.py` em Motores Epistemológicos do `SCRIPT_GLOSSARY.md`.
- [x] **Testes:** 6 cenários core em `tests/test_blast_radius.py`.

**Matriz de Propagação:**
- [x] .context/_scripts/blast_radius.py -> [NOVO — calculadora híbrida, 3 exit codes, degradação graceful]
- [x] .agent/skills/journal-sync/SKILL.md -> [Step 2 reescrito — consume blast_radius.py]
- [x] .husky/post-commit -> [NOVO — graphify auto-update, guard para ausência]
- [x] package.json -> [2 scripts: context:blast-radius, context:affinity]
- [x] .context/brain/SCRIPT_GLOSSARY.md -> [Entrada blast_radius.py]
- [x] .context/maintenance/rx-communications.md -> [Entrada blast_radius.py na Seção 5]
- [x] tests/test_blast_radius.py -> [NOVO — 6 testes core]
- [x] .context/maintenance/JOURNAL.md -> [Esta entrada]

Ref: planos/mudanca_propagacao/PLANO_FINAL_blast_radius.md
executor_context_id: blast-radius-mvp
validator_context_id: pending
status: READY TO COMMIT
```

### 5.2 Commit Message

```
feat(propagation): add blast_radius.py hybrid calculator

Combines graphify graph.json (structural) with
rx-communications.md (governance) to produce 3 prioritized
propagation buckets: must_update, likely_update, declared_only.

Changes:
- NEW: .context/_scripts/blast_radius.py (FILE→FILE projection, ~170 lines)
- NEW: .husky/post-commit (graphify auto-update hook)
- NEW: tests/test_blast_radius.py (6 core tests)
- UPDATE: journal-sync SKILL.md Step 2 (consume script output)
- UPDATE: package.json (context:blast-radius, context:affinity)
- UPDATE: SCRIPT_GLOSSARY.md (blast_radius.py entry)
- UPDATE: rx-communications.md (blast_radius.py in Section 5)

Refs: planos/mudanca_propagacao/PLANO_FINAL_blast_radius.md
```

### 5.3 Ordem de Execução Recomendada

```
1. Criar blast_radius.py e test_blast_radius.py
2. Rodar os testes para validar o core
3. Dry-run com seeds reais (harness_runner.py, RULES.md)
4. Atualizar journal-sync/SKILL.md e SCRIPT_GLOSSARY.md
5. Atualizar rx-communications.md (Seção 5)
6. Criar .husky/post-commit e atualizar package.json
7. Escrever Journal entry
8. Commit com a mensagem acima
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
| graph.json stale entre commits | Média | Baixo | post-commit hook + warning no output. Blast radius sem graph ainda funciona (governance-only). |
| Saída muito ruidosa (muitos arquivos em buckets) | Média | Médio | Filtrar `CROSS_FILE_RELATIONS` (já feito). Se persistir, adicionar threshold de confiança nos edges. |
| journal-sync IA não consome output corretamente | Baixa | Alto | Fallback para leitura manual. `--format text` no SKILL.md gera output humano-legível. |

---

## 8. Evolução Futura (Roadmap Pós-MVP)

Estas evoluções **só devem ser implementadas após
validação do MVP em produção:**

```
Sprint N+1: governance_edges.json (se parsing .md frágil)
Sprint N+2: rx_health_check.py (modo audit separado)
Sprint N+3: --glossary-validate (se gaps forem problema)
Sprint N+4: FLOW_PROPAGATION.md (com dados reais de uso)
Sprint N+5: Integrar affinity_lite como validação cruzada
```

**Nota:** O `plano_fase1.md` contém um `governance_edges.json`
completo com 39 edges + 3 wildcards que pode ser usado como
template se/quando chegar o Sprint N+1.

---

## 9. Genealogia deste Plano

| Documento | O que é | Status |
|-----------|---------|--------|
| `propagation_analysis.md` | Análise original das 3 camadas + 4 propostas (A-D) | ✅ Base teórica |
| `plano_mimo_propagation.md` | Plano MiMo v1 — 6 fases, 10 entregáveis, ~400 linhas | ⚠️ Over-engineered |
| `critica_plano_mimo.md` | Revisão crítica Opus — 3 bugs, 5 over-engineering, scorecard 5.2/10 | ✅ Diagnóstico |
| `plano_OpusMiMo_propagation.md` | OpusMiMo Rev 1.1 — arquitetura lean + premissas validadas | ✅ Arquitetura |
| `V2plano_mimo_propagation.md` | V2 MiMo — implementação funcional seguindo OpusMiMo | ✅ Código funcional |
| `plano_fase1.md` | governance_edges.json completo (39 edges) — ref futura | 📦 Arquivado |
| `plano_fase2.md` | blast_radius.py v1 (780 linhas, 3 bugs) — obsoleto | ❌ Substituído |
| **`PLANO_FINAL_blast_radius.md`** | **Este documento — consolidação definitiva** | **🎯 ATIVO** |

---

## 10. Checklist Final de Completude

```
✅ blast_radius.py              (§2.6 — código completo, ~170 linhas)
✅ journal-sync SKILL.md        (§3.1 — diff + versão completa do Step 2)
✅ .husky/post-commit           (§3.2 — com guard graphify + nota Windows)
✅ package.json                 (§3.3 — 2 scripts: blast-radius + affinity)
✅ SCRIPT_GLOSSARY.md           (§4.3 — seção Motores Epistemológicos, após inject_learnings)
✅ rx-communications.md         (§4.4 — Seção 5, entrada de script)
✅ test_blast_radius.py         (§4.1 — 6 cenários, paths Windows-safe)
✅ Dry Run                      (§4.2 — 4 cenários com seeds reais)
✅ Journal Entry                (§5.1 — formato real do JOURNAL.md validado)
✅ Commit Message               (§5.2 — conventional commits)
✅ Ordem de Execução            (§5.3 — 8 passos sequenciais)
✅ Scope Guard                  (§6 — 8 itens explicitamente adiados)
✅ Riscos                       (§7 — 4 riscos com mitigação)
✅ Roadmap Pós-MVP              (§8 — 5 sprints futuros)
✅ Genealogia                   (§9 — rastreabilidade completa)
```
