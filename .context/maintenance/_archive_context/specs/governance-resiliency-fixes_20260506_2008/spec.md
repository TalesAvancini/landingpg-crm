---
feature_id: governance-resiliency-fixes
type: gov_chain_v3
contract_mode: sprint_based
current_sprint: sprint_01
executor_context_id: spec-driver
validator_context_id: qa-validator

sprint_01:
  scope_allow: 
    # Global/Maintenance
    - .specs/features/governance-resiliency-fixes/STATE.md
    - .specs/features/governance-resiliency-fixes/tasks.md
    - .context/maintenance/JOURNAL.md
    - .context/brain/RULES.md
    - .context/brain/LEARNINGS.md
    - .context/_scripts/validate_context.py
    - .context/_scripts/workflow_journal_auditor.py
  dod:
    - Regex de 'updated:' suporta negrito/crase.
    - Pasta 'planos/' ignorada no SAM auditor.
    - Regra 'Governança > Estética' em RULES.md.
    - Aprendizados de Afinidade em LEARNINGS.md.
  qa_signoff: true

---

# Feature: Governance Resiliency Fixs (Gincana Debrief)

## 1. O Problema
A gincana do `affinity-lite` revelou pontos de atrito na governança:
1. O validador de frescor (`updated:`) falha se houver formatação Markdown, causando fricção desnecessária.
2. O SAM audita pastas de rascunho (`planos/`), exigindo burocracia excessiva para ideias voláteis.

## 2. A Solução
Implementar tolerância técnica no código do Harness e SAM, além de legislar sobre a prioridade da consistência mecânica sobre a estética visual.

## 3. Critérios de Integridade V3 (Não Negociáveis)
Completar as 9 Skills da Cadeia de Disciplina.
