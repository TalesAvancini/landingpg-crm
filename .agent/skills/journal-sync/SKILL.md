---
name: journal-sync
description: Syncs JOURNAL.md and propagates changes based on the actual git status (Reality Check). Triggers on sync journal, atualiza journal, check blast radius.
license: CC-BY-4.0
metadata:
  author: Antigravity Architect
  version: 2.2.0
---

# Journal Sync & Blast Radius Propagator (v2.2.0 - Recursive Reasoning)

You are an authoritative Governance Enforcement Agent. Your objective is to physically enforce architectural consistency across the H.O.K ecosystem using the Git Status as the single source of truth.

## Instructions

### Step 0: Reality Check (Short-Circuit)
1. Use `run_command` with `git status --porcelain` to identify exactly which files have been modified.
2. **Short-Circuit Logic:** If the output is empty (working tree clean), report: "No-Op: Nenhuma alteração pendente detectada no Git. Sistema já sincronizado." and **STOP** execution.
3. **Propagation Seed:** The list of files from `git status` is your "Propagation Seed". All subsequent steps MUST be based on this list.
4. **SAM-Exempt Filter:** Remove from the Propagation Seed any file whose path starts with: `planos/`, `scratch/`, `temp/`, `.agents/`. These are zones ignoradas pelo SAM (`workflow_journal_auditor.py` → `IGNORED_PREFIXES`). Files nessas zonas NÃO devem aparecer na Matriz de Propagação do Journal, sob risco de "Fraude Narrativa".
   > ⚠️ Fonte canônica: `IGNORED_PREFIXES` em `.context/_scripts/workflow_journal_auditor.py` (linha ~23).

### Step 1: Journal & SAM Sync
1. Open `.context/maintenance/JOURNAL.md`.
2. Compare the "Propagation Seed" with the latest entry. For any modified file not yet marked as `[x]`, append it to the Matriz de Propagação.
3. **CLÁUSULA DE CASTIDADE (IMUTÁVEL):** O bloco final do contrato (executor_context_id, validator_context_id, status) DEVE ser escrito em PLAIN TEXT puro. É terminantemente proibido o uso de Markdown (negritos, itálicos ou crases) nestas chaves. O Auditor Regex falhará silenciosamente ou bloqueará o commit caso detecte formatação estética.
4. Update the `Ultima Atualizacao` timestamp ONLY in `JOURNAL.md` and in the files identified in the Propagation Seed.

### Step 2: Blast Radius Calculation (Raciocínio Recursivo)
1. Use `view_file` to read `.context/maintenance/rx-communications.md`.
2. Use the "Propagation Seed" as search keys in Section 4 and 5 (Adjacency Lists).
3. Identify all files listed under **"Afeta:"** (or "Escreve em:") for those modified files.
4. **Raciocínio Recursivo (OBRIGATÓRIO):** Para CADA arquivo listado como afetado, responda mentalmente:
   > "A natureza específica da minha alteração realmente impacta o CONTEÚDO deste arquivo alvo?"
   - **SIM** → Inclua na propagação e na Matriz `[x]`.
   - **NÃO** → Descarte. Não propague só porque a adjacência sugere.
   - **Arquivo não listado, mas detectou impacto real** → Propague mesmo assim (rx-communications pode estar desatualizado).

   **Exemplo correto:** Mudei `spec-driver.md` (nova Skill 10). rx-communications diz: afeta `RULES.md`, `MASTER_FLOW.md`, `AGENT_REGISTRY.md`. Raciocínio: `AGENT_REGISTRY` → SIM (version bump). `MASTER_FLOW` → SIM (diagrama de skills). `RULES.md` → NÃO (nenhuma regra nova criada).

   **Exemplo errado (propagação cega):** Mudei condição de ativação no `sobriedade-operacional.md` → propagar para `RULES.md` e `AGENT_REGISTRY.md` ← ERRADO. A mudança é cosmética/condicional, não altera regras nem roles.

### Step 3: Autonomic Cascade Execution (Power Mode)
1. Execute edições APENAS nos arquivos que passaram no Raciocínio Recursivo do Step 2.
2. **Execute the code edit immediately** using `multi_replace_file_content`.
3. If a script in `.context/_scripts/` is affected, modify it immediately.
4. If a new file was created under `.context/`, update `FILE_GLOSSARY.md` (regra `new_context_path` do `JOURNAL_SYNAPSE.md`).
5. Continue recursively until all downstream files are synchronized.

### Step 4: Final Integrity Guard (Self-Correction Loop)
1. **Re-Verification:** Run `git status --porcelain` one last time. 
2. **Mental Reasoning:** Compare the output with the updated `JOURNAL.md`. If any modified file (outside `IGNORED_PREFIXES`) is not marked with `[x]` in the Journal, **RESTART Step 1**.
3. **Governance Prediction:** Mentally simulate the execution of `npm run context:validate`. If you detect that a new file is not in the `FILE_GLOSSARY.md`, alert the user BEFORE finishing.

### Step 5: Report
Provide a Walkthrough artifact summarizing:
- The "Propagation Seed" (detected via Git).
- The cascade updates executed.
- The final SAM Sync status and Integrity Guard verdict.

## Anti-Patterns (NÃO faça)

1. ❌ Registrar arquivos de `.agents/` no Journal → causa "Fraude Narrativa" (SAM-Exempt)
2. ❌ Usar backticks/negrito nas chaves do Contrato SAM → Regex do Auditor falha
3. ❌ Propagar cegamente toda a lista do rx-communications → Churn desnecessário
4. ❌ Esquecer `FILE_GLOSSARY.md` para novos arquivos em `.context/` → SAM bloqueia
5. ❌ Esquecer timestamp no frontmatter do `JOURNAL.md` → Metadata freshness falha
6. ❌ Criar entrada sem Matriz de Propagação `[x]` → "Modificação Silenciosa"
7. ❌ Assumir conteúdo de arquivo sem ler (`view_file`/`grep` primeiro) → Diffs vazios

## Troubleshooting

### Error: SAM pre-commit fails
Cause: A file was modified but not included in the Journal.
Solution: Re-run Step 0 to ensure the Propagation Seed is complete.

### Error: Fraude Narrativa
Cause: Um arquivo marcado `[x]` no Journal está em zona SAM-Exempt (`.agents/`, `planos/`, etc).
Solution: Remova a linha da Matriz de Propagação. O SAM não enxerga esses arquivos.

### Error: Propagação incompleta
Cause: rx-communications desatualizado ou raciocínio recursivo descartou arquivo que deveria ser propagado.
Solution: Re-avalie com `view_file` no arquivo alvo. Se a mudança impacta, propague.
