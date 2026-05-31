---
name: harness-context
description: Architectural context of the H.O.K. Validation Harness, including SAM, Karpathy Layer, SDD, and the flexibilization rules (Modo Light).
license: MIT
metadata:
  author: AI
  version: 1.0.0
---

# Harness Context Skill

This skill provides the comprehensive context of the H.O.K. Validation Harness system. It defines the components, the rules of reality checks, and the decisions made during the brainstorm to prevent rigid lockups.

## 🏗️ Architectural Overview

The governance ecosystem is structured into three layers:

1. **Camada Estratégica (PRD, VISION, INCEPTION)**: Defines the boundaries, real-world constraints ("NUNCA" and "SEMPRE"), and business requirements.
2. **Camada de Execução (SDD/TLC)**: Feature workbench located in `.specs/features/`. Manages file access via `scope_allow` and `max_impact_radius`.
3. **Camada de Validação (SAM, Harness, Karpathy)**: Enforces quality, reality, and traceability via git hooks (Husky).

---

## 🛡️ The Validation Gates

### 1. SAM (Sistema Anti-Migué)
*   **Purpose**: Audits that Git status corresponds to the latest `JOURNAL.md` entry.
*   **Rules**:
    *   **Fraude Narrativa**: Blocks if the journal matrix lists a file that is not modified in Git.
    *   **Modificação Silenciosa**: Blocks if a file is modified in Git but not listed in the latest journal entry matrix.
    *   **Exemptions**: `SHADOW_FILES` (automatic logs and indexes) and ignored prefixes (e.g. `scratch/`, `planos/`, `temp/`).

### 2. Harness
*   **Purpose**: Validates schema contracts (`schema.sql` vs specs), handoff completeness (`Dev -> QA`), and strategic constraints alignment.

### 3. Karpathy Layer (Linter Epistemológico)
*   **Purpose**: Verifies that technical claims in wiki pages cite their source (`> Fonte: RAW/...`).
*   **Exemption**: If the file contains `SSOT` (Single Source of Truth) in its text, the check is skipped.

---

## 📅 Decisões de Flexibilização (Modo Light)

To avoid developer lockups, the following rules apply:

1. **SAM Tolerante (WARNING local)**:
   *   On non-stable branches (e.g., `feature/*`, `bugfix/*`), SAM outputs warnings instead of failing the build (`Exit 0`).
   *   It prints an explicit report of the accumulated "governance debt" to encourage continuous self-remediation before the PR.
   *   Strict mode (`Exit 1`) remains active for `main` and `develop` branches (enforced at the CI/CD level).
2. **Escopo Flexível via Scratchpad**:
   *   If the developer (`spec-driver`) needs to touch files outside the `scope_allow`, they must log the request under the `INBOX` of the `AGENT_SCRATCHPAD.md` and pause.
   *   The `sdd-orchestrator` updates the Spec scope and resumes the driver, avoiding hard file-lock errors.
3. **Complexity Gate Consultivo**:
   *   Warnings about high file complexity are strictly advisory (`WARNING`) to prevent deadlocks with file-creation locks (SDD).
4. **Loop Exhaustion Automático**:
   *   Tracks consecutive execution failures. Locks the Scratchpad and triggers Escalation automatically after 5 consecutive failures.
5. **Cobertura Semântica Light**:
   *   Checks test files for references to new functions added in diffs. Acts as an advisory checklist, not a hard build blocker.
