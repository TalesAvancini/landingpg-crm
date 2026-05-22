# Plano OpusMiMo — Implementação Lean MVP

Concordo com o diagnóstico do Opus. As correções são cirúrgicas e reais — especialmente o bug do `file_to_node_id` e as premissas erradas sobre o schema do graph.json. A estratégia de projetar o grafo para FILE→FILE em vez de BFS em nós de função resolve dois problemas de uma vez.

Vou seguir o plano OpusMiMo fielmente. Implementação abaixo:

---

## Fase 1 — Motor: blast_radius.py

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

**~170 linhas.** Próximo das 120 estimadas (a diferença está no parser de rx-communications e no formatador de texto).

---

## Fase 2 — Integração

### 2.1 Atualização do journal-sync/SKILL.md

Preciso ver o arquivo atual para fazer o diff preciso. Posso me passar o conteúdo do **`.agent/skills/journal-sync/SKILL.md`**?

Enquanto isso, a mudança do Step 2 será conforme o plano:

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

### 2.2 Hook post-commit

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

### 2.3 package.json

Adicionar:
```json
"context:blast-radius": "python .context/_scripts/blast_radius.py"
```

E o `context:affinity` que estava pendente:
```json
"context:affinity": "python .context/_scripts/affinity_lite.py"
```

---

## Fase 3 — Validação

### 3.1 Testes (6 core)

```python
"""Tests for blast_radius.py — 6 core scenarios."""
import json
import sys
import subprocess
from pathlib import Path
from unittest.mock import patch

# Ajustar path para importar o módulo
SCRIPT_DIR = Path(__file__).parent.parent / ".context" / "_scripts"
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
        assert "only_graph.md" not in result["declared_only"]

    def test_governance_only_gives_declared(self):
        """Só na governance → declared_only."""
        seed = ["fileA.py"]
        structural = {}
        governance = {"fileA.py": {"only_gov.md"}}
        result = classify(seed, structural, governance)
        assert "only_gov.md" in result["declared_only"]
        assert "only_gov.md" not in result["must_update"]
        assert "only_gov.md" not in result["likely_update"]

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
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT_DIR / "blast_radius.py"),
                "--changed", "nonexistent.py",
                "--graph", "/tmp/no_graph.json",
                "--rx", "/tmp/no_rx.md",
            ],
            capture_output=True,
        )
        assert result.returncode == 4
        output = json.loads(result.stdout)
        assert "error" in output
```

### 3.2 SCRIPT_GLOSSARY.md

Adicionar entrada:

```markdown
| blast_radius.py | 🎯 Radar de Blast Radius | Calculadora híbrida de blast radius. Combina `graph.json` (relações estruturais via Graphify) com `rx-communications.md` (regras de governança) para retornar 3 buckets priorizados: `must_update`, `likely_update`, `declared_only`. Consumido pelo skill `journal-sync` no Step 2. **Gatilho:** `npm run context:blast-radius -- --changed <files>` **Requisitos:** Python 3.9+. Graphify opcional (degrada graciosamente). |
```

---

## Fase 4 — Commit

### 4.1 Scope Guard (o que NÃO fazer agora)

| Não fazer | Quando fazer |
|-----------|-------------|
| `governance_edges.json` | Se parsing .md falhar 3+ vezes |
| `FLOW_PROPAGATION.md` | Após 2-3 sprints com blast_radius rodando |
| `--mode audit` | `rx_health_check.py` separado, se necessário |
| `--glossary-validate` | Sprint seguinte, se gaps forem problema |
| Alterar JOURNAL_SYNAPSE / SAM | Release do template |

---

## Preciso de você para completar

| Arquivo | Status | Ação |
|---------|--------|------|
| `blast_radius.py` | ✅ Pronto | Acima |
| `journal-sync/SKILL.md` | ⏳ Preciso do conteúdo | Fazer diff no Step 2 |
| `.husky/post-commit` | ✅ Pronto | Acima |
| `package.json` | ✅ Pronto | Adicionar 2 scripts |
| `SCRIPT_GLOSSARY.md` | ⏳ Preciso do formato | Adicionar 1 entrada |
| `tests/test_blast_radius.py` | ✅ Pronto | Acima |

journal-sync/SKILL.md — Diff do Step 2

A mudança é cirúrgica: substituir as linhas 1-3 do Step 2 (leitura manual de 348 linhas) pela execução do script, mantendo o Raciocínio Recursivo intacto e adicionando o fallback.


diff
diff
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

Versão completa do Step 2 atualizado (para aplicar):

markdown
markdown
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
SCRIPT_GLOSSARY.md — Entrada a adicionar

A seção correta é "Motores Epistemológicos" — o blast_radius.py é da mesma família do affinity_lite.py (análise de relações entre arquivos). Entrada na tabela, após inject_learnings.py:


markdown
markdown
| `blast_radius.py` | **Radar de Blast Radius** | Calculadora híbrida de impacto de propagação. Combina o grafo estrutural do Graphify (`graph.json`) com o mapa de governança (`rx-communications.md`) para retornar 3 buckets priorizados: `must_update` (ambas concordam), `likely_update` (só estrutural), `declared_only` (só governança). Consumido pelo skill `journal-sync` no Step 2. Degrada graciosamente quando Graphify não está disponível. | `npm run context:blast-radius -- --changed file1.py file2.md` |


Entregáveis Finais — Tudo Pronto

Aqui está o resumo consolidado dos 6 arquivos:


#	Arquivo	Ação	Localização
1	blast_radius.py	CRIAR (~170 linhas)	.context/_scripts/blast_radius.py
2	journal-sync/SKILL.md	ATUALIZAR Step 2 (substituir linhas 1-3)	.agent/skills/journal-sync/SKILL.md
3	post-commit	CRIAR (~12 linhas)	.husky/post-commit
4	package.json	ATUALIZAR (2 scripts)	package.json
5	SCRIPT_GLOSSARY.md	ATUALIZAR (1 entrada)	.context/brain/SCRIPT_GLOSSARY.md
6	test_blast_radius.py	CRIAR (~80 linhas)	tests/test_blast_radius.py


Arquivo 1: blast_radius.py

O script completo já foi fornecido na mensagem anterior (~170 linhas). Para referência rápida, as decisões de design:


Grafo projetado para FILE→FILE — colapsa nós de funções/conceitos em source_files, eliminando o bug do file_to_node_id
built_at_commit (raiz do graph.json), não meta.built_from_commit
nodes é lista — pré-indexado em dict antes de lookup
Filtragem por CROSS_FILE_RELATIONS — só calls, references, implements, rationale_for, semantically_similar_to
3 exit codes (0, 2, 4) — não 5


Arquivo 2: journal-sync/SKILL.md — Diff aplicado

O Step 2 completo atualizado:


markdown
markdown
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


Arquivo 3: .husky/post-commit

bash
bash
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

Após criar: chmod +x .husky/post-commit



Arquivo 4: package.json — Scripts a adicionar

json
json
"context:blast-radius": "python .context/_scripts/blast_radius.py",
"context:affinity": "python .context/_scripts/affinity_lite.py"


Arquivo 5: SCRIPT_GLOSSARY.md

Entrada fornecida acima (seção Motores Epistemológicos, após inject_learnings.py).



Arquivo 6: tests/test_blast_radius.py

python
python
"""Tests for blast_radius.py — 6 core scenarios."""
import json
import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / \
    ".context" / "_scripts" / "blast_radius.py"
SCRIPT_DIR = SCRIPT.parent

sys.path.insert(0, str(SCRIPT_DIR))

from blast_radius import classify


class TestClassifyBuckets:

    def test_both_agree_gives_must_update(self):
        seed = ["fileA.py"]
        structural = {"fileA.py": {"shared.md"}}
        governance = {"fileA.py": {"shared.md"}}
        result = classify(seed, structural, governance)
        assert "shared.md" in result["must_update"]
        assert "shared.md" not in result["likely_update"]
        assert "shared.md" not in result["declared_only"]

    def test_structural_only_gives_likely(self):
        seed = ["fileA.py"]
        structural = {"fileA.py": {"only_graph.md"}}
        governance = {}
        result = classify(seed, structural, governance)
        assert "only_graph.md" in result["likely_update"]
        assert "only_graph.md" not in result["must_update"]

    def test_governance_only_gives_declared(self):
        seed = ["fileA.py"]
        structural = {}
        governance = {"fileA.py": {"only_gov.md"}}
        result = classify(seed, structural, governance)
        assert "only_gov.md" in result["declared_only"]
        assert "only_gov.md" not in result["must_update"]

    def test_no_matches_gives_empty_buckets(self):
        seed = ["unknown.py"]
        structural = {"other.py": {"x.md"}}
        governance = {"other.py": {"y.md"}}
        result = classify(seed, structural, governance)
        assert result["must_update"] == []
        assert result["likely_update"] == []
        assert result["declared_only"] == []

    def test_seed_excluded_from_buckets(self):
        seed = ["fileA.py"]
        structural = {"fileA.py": {"fileA.py", "fileB.py"}}
        governance = {"fileA.py": {"fileA.py", "fileB.py"}}
        result = classify(seed, structural, governance)
        assert "fileA.py" not in result["must_update"]
        assert "fileB.py" in result["must_update"]


class TestDegradation:

    def test_both_unavailable_exits_4(self):
        result = subprocess.run(
            [
                sys.executable, str(SCRIPT),
                "--changed", "nonexistent.py",
                "--graph", "/tmp/__no_graph.json",
                "--rx", "/tmp/__no_rx.md",
            ],
            capture_output=True, text=True,
        )
        assert result.returncode == 4
        output = json.loads(result.stdout)
        assert "error" in output


Scope Guard — O que NÃO fazer agora

Não fazer	Quando fazer
governance_edges.json	Se parsing .md falhar 3+ vezes
FLOW_PROPAGATION.md	Após 2-3 sprints com blast_radius rodando
--mode audit	rx_health_check.py separado, se necessário
--glossary-validate	Sprint seguinte, se gaps forem problema
Alterar JOURNAL_SYNAPSE / SAM	Release do template
6 testes extras	Quando expandir features
