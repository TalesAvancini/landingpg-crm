---
feature_id: blast_radius_mvp
type: standard
contract_mode: sprint_based
current_sprint: sprint_01
executor_context_id: spec-driver
validator_context_id: qa-validator
origin: planos/mudanca_propagacao/PLANO_FINAL_blast_radius.md

sprint_01:
  scope_allow: 
    # Global/Maintenance (Obrigatório para V3)
    - .specs/features/blast_radius_mvp/STATE.md
    - .specs/features/blast_radius_mvp/tasks.md
    - .specs/features/blast_radius_mvp/*.enriched.md
    - .specs/features/blast_radius_mvp/CLOSURE.md
    - .context/maintenance/HARNESS_LOG.md
    - .context/maintenance/JOURNAL.md
    - .specs/features/blast_radius_mvp/AGENT_SCRATCHPAD.md
    - .context/brain/FILE_GLOSSARY.md
    # Feature Scope
    - .context/_scripts/blast_radius.py
    - .agent/skills/journal-sync/SKILL.md
    - .husky/post-commit
    - package.json
    - .context/brain/SCRIPT_GLOSSARY.md
    - .context/maintenance/rx-communications.md
    - tests/test_blast_radius.py
  dod:
    - O script `blast_radius.py` executa com sucesso (--changed) com 3 exit codes mapeados.
    - Os 6 testes unitários em `tests/test_blast_radius.py` passam.
    - O Hook post-commit do Husky foi criado com guard fail-safe.
    - A skill `journal-sync` e os docs (GLOSSARY e rx-communications) foram atualizados de acordo com o plano.
  qa_signoff: true
  signed_by: "@qa-validator"
---

# Feature: Blast Radius Inteligente (Lean MVP)

## 0. Origem
> **Documento-raiz:** `planos/mudanca_propagacao/PLANO_FINAL_blast_radius.md`
> Esta feature nasceu do plano final validado (Opus MiMo Rev 1.1) para automatizar e criar uma calculadora híbrida de propagação.

## 1. O Problema
Atualmente, o script `journal-sync` lê o `rx-communications.md` de forma manual/frágil, o grafo estrutural não está integrado com o grafo de governança, e a propagação de mudanças exige esforço mental excessivo e pouco guiado, dependendo de 348 linhas manuais.

## 2. A Solução
Criar uma calculadora híbrida de Blast Radius (`.context/_scripts/blast_radius.py`) que combina o arquivo estrutural `graph.json` do Graphify com as arestas de governança definidas em `rx-communications.md`, produzindo 3 buckets priorizados (`must_update`, `likely_update`, `declared_only`).

## 3. Requisitos Funcionais (Acceptance)
- [ ] Criar o script `.context/_scripts/blast_radius.py`
- [ ] Atualizar `.agent/skills/journal-sync/SKILL.md` (Step 2 reescrito para consumir output)
- [ ] Criar `.husky/post-commit` para rodar `graphify update`
- [ ] Atualizar `package.json` adicionando os scripts npm `context:blast-radius` e `context:affinity`
- [ ] Adicionar entrada em `.context/brain/SCRIPT_GLOSSARY.md` (Motores Epistemológicos)
- [ ] Adicionar entrada em `.context/maintenance/rx-communications.md` (Seção 5 - scripts)
- [ ] Criar `tests/test_blast_radius.py` com os 6 cenários mapeados e executá-los com sucesso.
- [ ] Inserir registro final em `.context/maintenance/JOURNAL.md` com a Matriz de Propagação.

## 4. Critérios de Integridade V3 (Não Negociáveis)
Para que esta Spec seja considerada completa, o executor deve gerar um `STATE.md` contendo TODAS as 9 evidências da cadeia (CHAIN_CONTEXT_LOADED até CHAIN_HANDOFF), e um `CLOSURE.md` síntese deve ser gerado na Skill 9 (HANDOFF).
**max_impact_radius:** Limite absoluto de 10 arquivos modificados nesta sprint (Circuit Breaker).

## 5. Raw Payloads (Injeção Atômica)
> **Instrução:** Se a Spec referenciar IDs de regras ou erros, o texto bruto DEVE ser injetado abaixo.
- **[REGRA 1.14 Protocolo de Fechamento de Feature]**: Toda feature concluída deve obrigatoriamente gerar um arquivo `CLOSURE.md` na pasta da feature. O relatório deve conter o delta entre o plano original (`origin`) e a entrega, o Blast Radius real e as cicatrizes extraídas.
- **[REGRA MIMO_STATE_INTEGRITY]**: Toda automação que altere o STATE.md deve preservar campos obrigatórios e ter edição cirúrgica.
- **[INJEÇÃO DE CÓDIGO]**: Todo o código estrutural para o `blast_radius.py` e os 6 testes em `tests/test_blast_radius.py` encontram-se descritos integralmente no documento raiz `planos/mudanca_propagacao/PLANO_FINAL_blast_radius.md`. NÃO ALUCINE O SCRIPT. Copie a base que já foi homologada lá.
