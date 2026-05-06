---
name: journal-sync
description: Syncs JOURNAL.md and propagates changes based on the actual git status (Reality Check). Triggers on sync journal, atualiza journal, check blast radius.
license: CC-BY-4.0
metadata:
  author: Antigravity Architect
  version: 2.0.0
---

# Journal Sync & Blast Radius Propagator (v2.0 - Deterministic)

You are an authoritative Governance Enforcement Agent. Your objective is to physically enforce architectural consistency across the H.O.K ecosystem using the Git Status as the single source of truth.

## Instructions

### Step 0: Reality Check (Short-Circuit)
1. Use `run_command` with `git status --porcelain` to identify exactly which files have been modified.
2. **Short-Circuit Logic:** If the output is empty (working tree clean), report: "No-Op: Nenhuma alteração pendente detectada no Git. Sistema já sincronizado." and **STOP** execution.
3. **Propagation Seed:** The list of files from `git status` is your "Propagation Seed". All subsequent steps MUST be based on this list.

### Step 1: Journal & SAM Sync
1. Open `.context/maintenance/JOURNAL.md`.
2. Compare the "Propagation Seed" with the latest entry. For any modified file not yet marked as `[x]`, append it to the Matriz de Propagação.
3. **CRITICAL SYNTAX:** Escreva as chaves do contrato SAM (executor_context_id, validator_context_id, status) estritamente como texto puro. O auditor falhará se detectar asteriscos ou negritos nessas linhas.
4. Update the `Ultima Atualizacao` timestamp ONLY in `JOURNAL.md` and in the files identified in the Propagation Seed.

### Step 2: Blast Radius Calculation
1. Use `view_file` to read `.context/maintenance/rx-communications.md`.
2. Use the "Propagation Seed" as search keys in Section 4 and 5 (Adjacency Lists).
3. Identify all files listed under **"Afeta:"** (or "Escreve em:") for those modified files.

### Step 3: Autonomic Cascade Execution (Power Mode)
1. For every file in the Blast Radius, analyze if the original modification breaks its logic or references.
2. **Execute the code edit immediately** using `multi_replace_file_content`.
3. If a script in `.context/_scripts/` is affected, modify it immediately.
4. Continue recursively until all downstream files are synchronized.

### Step 4: Report
Provide a Walkthrough artifact summarizing:
- The "Propagation Seed" (detected via Git).
- The cascade updates executed.
- The final SAM Sync status.

## Troubleshooting

### Error: SAM pre-commit fails
Cause: A file was modified but not included in the Journal.
Solution: Re-run Step 0 to ensure the Propagation Seed is complete.
