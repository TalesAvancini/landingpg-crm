---
feature_id: [nome_da_feature]
type: [gov_chain_v3 | standard]
contract_mode: sprint_based
current_sprint: sprint_01
executor_context_id: spec-driver
validator_context_id: qa-validator
origin: [caminho/do/documento/de/ideação]

sprint_01:
  scope_allow: 
    # Global/Maintenance (Obrigatório para V3)
    - .specs/features/[feature_id]/STATE.md
    - .specs/features/[feature_id]/tasks.md
    - .specs/features/[feature_id]/*.enriched.md
    - .specs/features/[feature_id]/CLOSURE.md
    - .context/maintenance/HARNESS_LOG.md
    - .context/maintenance/JOURNAL.md
    - .specs/features/[feature_id]/AGENT_SCRATCHPAD.md
    # Feature Scope
    - [caminho/do/arquivo/a/ser/modificado]
  dod:
    - [criterio_de_aceite_01]
  qa_signoff: false
---

# Feature: [Nome Amigável]

## 0. Origem
> **Documento-raiz:** `[caminho/do/documento/de/ideação]`
> Se esta feature nasceu de um plano, brainstorm ou ideia documentada, registre aqui para rastreabilidade. Se o escopo foi reduzido em relação ao plano original, descreva o que ficou de fora e por quê.

## 1. O Problema
[Descrição do problema]

## 2. A Solução
[Descrição da solução]

## 3. Requisitos Funcionais (Acceptance)
- [ ] [Requisito 01]

## 4. Critérios de Integridade V3 (Não Negociáveis)
Para que esta Spec seja considerada completa, o executor deve gerar um `STATE.md` contendo TODAS as 9 evidências da cadeia (CHAIN_CONTEXT_LOADED até CHAIN_HANDOFF), e um `CLOSURE.md` síntese deve ser gerado na Skill 9 (HANDOFF).

## 5. Raw Payloads (Injeção Atômica)
> **Instrução:** Se a Spec referenciar IDs de regras ou erros (ex: SCAR-XXX), o texto bruto DEVE ser injetado abaixo para evitar que o agente perca tempo caçando contextos externos.
- [ID]: [Texto Bruto da Regra/Cicatriz]
