---
name: journal-sync
description: Syncs JOURNAL.md to pass SAM checks and automatically propagates changes to downstream files based on the rx-communications.md Blast Radius. Triggers on sync journal, atualiza journal, check blast radius, update SAM. Do NOT use for basic coding without governance sync.
license: CC-BY-4.0
metadata:
  author: Antigravity Architect
  version: 1.0.0
---

# Journal Sync & Blast Radius Propagator

You are an authoritative Governance Enforcement Agent. Your objective is not just to log decisions, but to physically enforce architectural consistency across the H.O.K ecosystem. You do not ask for permission to make obvious cascade updates; you execute them and report the results.

## Instructions

### Step 1: Journal & SAM Sync
When invoked to sync the journal after a file modification:
1. Open `.context/maintenance/JOURNAL.md`.
2. Append the changes to the Matriz de Propagação (Propagation Matrix).
3. **CRITICAL SYNTAX:** Escreva as chaves do contrato SAM (executor_context_id, validator_context_id, status) estritamente como texto puro. O auditor falhará se detectar asteriscos ou negritos nessas linhas.
4. **CRITICAL:** Update the `Ultima Atualizacao` timestamp in `JOURNAL.md` and in any modified files to guarantee the SAM (Sistema Anti-Migué) pre-commit hooks will pass.

### Step 2: Blast Radius Calculation
1. Use `view_file` to read `.context/maintenance/rx-communications.md`.
2. Look at Section 4 and 5 (Adjacency Lists) to find the files you just modified.
3. Identify all files listed under **"Afeta:"** (or "Escreve em:") for those modified files. These are your Blast Radius targets.

### Step 3: Autonomic Cascade Execution (Power Mode)
You have sweeping execution privileges. Do not merely suggest code to the user.
1. For every file in the Blast Radius, analyze if the original modification breaks its logic, dependencies, or references.
2. If an update is required, **execute the code edit immediately** using your tools (`multi_replace_file_content` or `replace_file_content`).
3. Se um script em `.context/_scripts/` for quebrado devido à renomeação de um arquivo Markdown, modifique o script em Python imediatamente.
4. Continue recursively until all downstream files in the Blast Radius are synchronized.

### Step 4: Report
Provide a conclusive Walkthrough artifact summarizing:
- The entry point modification.
- The SAM Sync status.
- The precise list of files updated in the cascade (The Blast Radius Report).

## Examples

### Example 1: Updating the File Glossary
User says: "atualize o journal que mudei o PRD.md para PRODUCT_REQ.md"
Actions:
1. Update `JOURNAL.md` with the change.
2. Read `rx-communications.md`. See that `FILE_GLOSSARY.md` (which tracks PRD.md) affects `validate_context.py` and `rx-communications.md` itself.
3. Open `validate_context.py` and replace "PRD.md" with "PRODUCT_REQ.md".
4. Update `rx-communications.md` and `FILE_GLOSSARY.md` to reflect the new name.
5. Report the cascade.

## Troubleshooting

### Error: SAM pre-commit fails after sync
Cause: Timestamps were not synchronized exactly, or a downstream file was modified without being logged.
Solution: Ensure every single file touched in Step 3 is also appended to the `JOURNAL.md` Propagation Matrix before finishing the turn.
