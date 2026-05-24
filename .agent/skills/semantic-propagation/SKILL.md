---
name: semantic-propagation
description: Analyzes committed changes using blast_radius.py and graphify explain to generate structured propagation plans (via superpowers-plan) and apply doc/index updates.
license: MIT
metadata:
  author: AI
  version: 1.0.0
---

# Semantic Propagation Skill

This skill guides an agent (or developer) through the process of analyzing file changes (seeds), detecting deep semantic and structural dependencies, formulating a structured propagation plan, and executing surgical updates to metadata and documentation.

## Execution Steps

### Step 1: Identify Seeds (Change Diff)

Identify the list of modified files (the Propagation Seeds).
* **If auditing a completed feature/commit:** Run `git diff HEAD~1 --name-only` to get the exact list of changed files.
* **If auditing uncommitted/working tree changes:** Run `git status --porcelain` to identify changed files.
* Filter out files in ignored directories (e.g., `scratch/`, `temp/`, `planos/`).

### Step 2: Physics & Policy Analysis (Blast Radius)

Run the blast radius calculator on the seeds to get the structural and policy dependency buckets:
```bash
python .context/_scripts/blast_radius.py --changed <SPACE_SEPARATED_SEEDS> --format text
```
Analyze the returned buckets:
* **🔴 MUST UPDATE:** Structural dependencies that are also declared in policy maps.
* **🟡 LIKELY UPDATE:** Structural dependencies found via code imports/AST.
* **🔵 DECLARED ONLY:** Policy-declared dependencies (documentation or manual maps).

### Step 3: Semantic Analysis (Graphify Explain)

For each modified file (seed), query the Graphify knowledge base to discover conceptual connections that lack physical code imports:
```powershell
$env:PYTHONUTF8=1; graphify explain "<SEED_FILE_PATH>"
```
Analyze the output:
* Look for connected nodes of type `document` or `markdown` (such as `rx-*.md`, blueprints, READMEs, or architectural specifications).
* If a conceptually related file in `.context/` or `*.md` is found in the semantic neighborhood, add it to your list of target files for propagation.

### Step 4: Create Structured Propagation Plan

Before modifying any file, you MUST write an implementation plan using the **`superpowers-plan`** format. Break down the updates into small, manageable steps:

```markdown
### Goal
[Describe which files need to be updated or stamped based on the Blast Radius and Graphify Semantic output]

### Assumptions
[Describe any context details]

### Plan
1. Update [file_name]
   - Files: `path/to/file.md`
   - Change: [Describe the surgical edit or stamp]
   - Verify: [Describe the exact check command]
2. ...

### Risks & mitigations
### Rollback plan
```

### Step 5: Apply & Verify

1. **Surgical Updates:** Edit manual files (e.g., `FILE_GLOSSARY.md`, `rx-communications.md`) using precise editing tools. Do not overwrite whole files.
2. **Metadata Stamps:** If a file only needs a metadata stamp (Declared Only), update its `Ultima Atualizacao:` date in the frontmatter header. Do not insert empty spaces or comments.
3. **Run Builders:** For auto-generated files (e.g., `PROJECT_INDEX.md`), run the corresponding index builders:
   ```powershell
   npm run context:map
   ```
4. **Final Check:** Run the Husky pre-commit validations locally to verify that no syntax or SAM errors were introduced:
   ```powershell
   python run_context.py check-version; python run_context.py validate; python run_context.py scan-secrets; python run_context.py workflow-journal
   ```
