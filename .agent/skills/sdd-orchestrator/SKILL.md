---
name: sdd-orchestrator
description: Orchestrates the Spec-Driven Development process. Triggers when the user asks to start a new feature, write a spec, or explicitly requests SDD. Do NOT use for simple code edits without a spec.
license: CC-BY-4.0
metadata:
  author: AI
  version: 1.0.2
---

# SDD Orchestrator

This skill guides the Orchestrator (Hub) through the FULL Spec-Driven Development (SDD) lifecycle in the H.O.K Forge framework. As the Hub, your job is not only to start the process, but to define safety limits, fill the YAML frontmatter and scope allow list, run the vaccine injection, support the executor (`spec-driver`), promote recurring errors to the Ledger, and formalize final closure.

## Instructions

### Step 0: Pre-Flight Check (Git Cleanliness Baseline)

Before drafting any spec or planning changes, you MUST ensure the workspace is 100% clean. This is an inviolable rule to prevent residual or unrelated changes ("Modificação Silenciosa" or "Ghost Couplings") from leaking into the new feature's Git history and breaking pipeline gates.
1. Run `git status --short` and `git status --ignored`.
2. If there are ANY uncommitted modifications, untracked files, or staged changes, you MUST stop immediately. Do NOT draft the spec.
3. Ask the user or use tools to commit them cleanly (e.g., `chore: cleanup residual changes`) and push them (`git push`) to sync with the remote repository.
4. Only proceed to Step 1 when the command `git status --short` returns a completely empty output, guaranteeing a pristine baseline.

### Step 1: Blast Radius Calculation (Propagation Matrix)

Before writing any spec, you must understand the impact of the intended changes. Identify the core files that will be modified (Propagation Seed).

Execute the blast radius script:
```bash
python .context/_scripts/blast_radius.py --changed <PROPAGATION_SEED_FILES> --format text
```

Analyze the output buckets (`must_update`, `likely_update`, `declared_only`).

### Step 2: Draft the Spec (The Payload & Boundaries)

1. Read the `.agent/templates/spec_v3.md` template.
2. Draft the new specification document. You MUST meticulously fill the YAML frontmatter (`feature_id`, `type`, `contract_mode`, etc.).
3. **Scope Allow List**: You MUST explicitly populate the `scope_allow` array in the YAML with the global mandatory files PLUS all the specific feature files identified in the Blast Radius. This acts as the Physical Check (Scope Guard).
4. **Propagation & Limits**: Define a strict `max_impact_radius` (the maximum acceptable number of file changes) to act as a circuit breaker.
5. **Raw Payloads**: You OBRIGATORIAMENTE must inject the actual texts of relevant rules and constraints directly into the Spec's Section 5. 
6. Save the drafted spec in the `.specs/features/` directory.

### Step 3: Human Ratification, Vaccine & Delegation (Transition Gate)

1. **Ratification:** Show the drafted Spec to the user and ask for explicit approval. Do NOT proceed or delegate to the executor until the user ratifies the Spec.
2. Before delegating, you MUST run the MiMo injection to insert Scars into the Spec:
```bash
npm run context:inject
```
3. Verify that the `*.enriched.md` file was generated.
4. **Physical Scratchpad Instantiation:** You MUST copy the template `.agent/templates/AGENT_SCRATCHPAD.md` to `.specs/features/<feature_id>/AGENT_SCRATCHPAD.md` to ensure the executor has a physical escalation buffer.
5. **Git Cleanliness Gate (Pre-Delegation):** Before spawning the executor subagent, you MUST commit the spec setup (the drafted `spec.md`, `STATE.md`, `tasks.md`, `AGENT_SCRATCHPAD.md`, and the `*.enriched.md` files) to seal the feature setup in Git. Run:
   - `git add .specs/features/<feature_id>/`
   - Create a corresponding setup entry at the top of `JOURNAL.md` for this setup commit.
   - Run `git commit -m "chore(sprint): setup spec, STATE and SCRATCHPAD for <feature_id>"`
   - Run `git push` to sync the baseline.
   - Run `git status --short` to verify the tree is 100% clean.
6. Hand off execution to the `spec-driver` subagent (e.g., via `/spec-driver [instrução]`), passing the path to the spec.
7. Once delegated, **do not close the task**. Wait for execution.

### Step 4: Handle Escalations & The Immune System

During Phase C, the `@spec-driver` might hit safety limits and issue a `[HANDOFF: ESCALATION]`.
- **If `[BLOCKED]`**: 
  1. Review the escalation request in the `INBOX` of `AGENT_SCRATCHPAD.md`.
  2. Write your clear solution or directive in the `DIRECTIVES` section of the Scratchpad.
  3. Reply with: `@spec-driver [RESUME] Diretiva injetada no Scratchpad. Leia a seção DIRECTIVES e retome a execução de onde parou no STATE.md.`
- **If `⚠️ SCOPE_BLOWOUT`**: You must abort the current spec, use the telemetria provided to re-fragment the feature into smaller, atomic specs, and restart the process.
- **The Immune System (Faxina Cognitiva)**: If the same error is escalated across multiple sprints, you MUST promote it permanently by adding it to `SSD_ERRORS_LEDGER.md` or updating the Spec restrictions.
- **[GOVERNANCE-FRICTION]**: If you or the executor detect any operational slips (e.g., broken chronology, unupdated metadata, ghost couplings) that don't block the execution but create governance debt, you MUST log it by appending a line to `.context/maintenance/HARNESS_LOG.md` (e.g., `[GOVERNANCE-FRICTION] YYYY-MM-DD | file | description`).

### Step 5: Receive Signoff & Final Closure

In Phase D, the `spec-driver` will invoke the `@qa-validator` for the final audit.
Wait for the `@qa-validator` to return `qa_signoff: true` (or rejection).
- If **rejected**: Pass the feedback back to `@spec-driver` for correction.
- If **true**: The feature is technically complete.
- **Final Hub Duties**: As the Orchestrator, you must now execute the final Rites:
  1. **Run Harness:** Run `npm run context:harness` to ensure the spec didn't break physical logic.
  2. **Validate SAM:** Ensure `npm run context:workflow-journal` passes cleanly.
  3. **Aggregate Learnings:** Run `npm run context:learnings` to compile the error scars from `SSD_ERRORS_LEDGER.md` and failure loops from `HARNESS_LOG.md` into `LEARNINGS.md` before the spec directory is archived.
  4. **Closure Synthesis:** Ensure the `CLOSURE.md` synthesis file is generated and technical decisions are migrated to `JOURNAL.md`.
  5. **Commit:** Perform the final Git commit for the feature.
  6. **Cleanup:** Run `npm run context:cleanup` to archive the ephemeral `.specs/features/` folder since the merge is complete.

## Examples

### Example 1: Escalation Handling
User says: "[HANDOFF: ESCALATION] Error X happened."
Actions:
1. Hub reads `INBOX` in `AGENT_SCRATCHPAD.md`.
2. Hub writes solution in `DIRECTIVES` section of `AGENT_SCRATCHPAD.md`.
3. Hub tells SD: `@spec-driver [RESUME] Diretiva injetada no Scratchpad. Leia a seção DIRECTIVES e retome a execução de onde parou no STATE.md.`
