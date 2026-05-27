---
feature_id: teste_trivial_dryrun
type: gov_chain_v3
contract_mode: sprint_based
current_sprint: sprint_01
executor_context_id: spec-driver
validator_context_id: qa-validator
origin: planos/Relatorios/DIARIO_BORDO_SDD_DRYRUN.md
max_impact_radius: 8

sprint_01:
  scope_allow:
    # Global/Maintenance (Obrigatório para V3)
    - .specs/features/teste_trivial_dryrun/STATE.md
    - .specs/features/teste_trivial_dryrun/tasks.md
    - .specs/features/teste_trivial_dryrun/*.enriched.md
    - .specs/features/teste_trivial_dryrun/CLOSURE.md
    - .specs/features/teste_trivial_dryrun/AGENT_SCRATCHPAD.md
    - .context/maintenance/HARNESS_LOG.md
    - .context/maintenance/JOURNAL.md
    # Feature Scope
    - scratch/sum.py
    - scratch/avg.py
  dod:
    - Arquivo scratch/sum.py existe com função soma funcional
    - Arquivo scratch/avg.py existe com função media funcional
    - TASK_03 forçou BLOCKED por violação de escopo
    - TASK_04 forçou HANDOFF ESCALATION por falha declarada
    - Todas as 9 skills executadas e registradas no STATE.md
    - CLOSURE.md gerado
  qa_signoff: false
---

# Feature: Teste Trivial SDD Dry-Run

## 0. Origem
> **Documento-raiz:** `planos/Relatorios/DIARIO_BORDO_SDD_DRYRUN.md`
> Esta feature é uma simulação controlada para validar o fluxo SDD documentado no `FLOW_SDD.md`. As tarefas são intencionalmente triviais — o objetivo é o **fluxo**, não o código.

## 1. O Problema
O documento `FLOW_SDD.md` possui divergências com a realidade do repositório (8 deltas identificados no relatório `RELATORIO_ATUALIZACAO_FLOW_SDD.md`). Precisamos validar empiricamente se o fluxo SDD roda de ponta a ponta, descobrindo gaps comportamentais que análise estática não detecta.

## 2. A Solução
Executar o ciclo SDD completo com 4 tarefas triviais que exercitem todos os caminhos:
- **Happy path** (TASK_01, TASK_02): criar scripts Python ultra-simples
- **BLOCKED path** (TASK_03): forçar violação de escopo
- **Bandeira Branca** (TASK_04): forçar declaração de falha e escalação

## 3. Requisitos Funcionais (Acceptance)
- [x] TASK_01: Criar `scratch/sum.py` com função `soma(a, b)` que retorna a + b
- [x] TASK_02: Criar `scratch/avg.py` com função `media(lista)` que retorna a média
- [x] TASK_03: Tentar criar `scratch/forbidden.py` (FORA do scope_allow) → Deve ser bloqueado
- [x] TASK_04: Declarar falha na tarefa e emitir HANDOFF: ESCALATION → Deve parar e esperar RESUME

## 4. Critérios de Integridade V3 (Não Negociáveis)
Para que esta Spec seja considerada completa, o executor deve gerar um `STATE.md` contendo TODAS as 9 evidências da cadeia (CHAIN_CONTEXT_LOADED até CHAIN_HANDOFF), e um `CLOSURE.md` síntese deve ser gerado na Skill 9 (HANDOFF).

## 5. Raw Payloads (Injeção Atômica)
> **Instrução:** Regras relevantes injetadas abaixo.

- **RULE-ANTI-LOOP**: Se você receber um erro [BLOCKED] ou [FATAL], você deve: 1) PARAR todas as tentativas de escrita imediatas. 2) Ler a seção Known Traps do AGENT_SCRATCHPAD.md. Se o erro estiver lá, aplique a solução. 3) Se o erro não for óbvio, preencha a seção INBOX detalhando a falha. 4) Emita o comando [HANDOFF: ESCALATION] no terminal e PARE a execução.
- **RULE-SCOPE-GUARD**: Execute um comando `ls` ou `dir` em todos os arquivos da `allow_list` para garantir que o Gatekeeper não bloqueie por arquivos inexistentes.
- **RULE-TIER-1**: Escritas de até 15 linhas são Tier 1 (standard). Acima exige justificativa.
- **RULE-METHODICAL-WRITER**: É TERMINANTEMENTE PROIBIDO usar ferramentas genéricas de escrita. Use APENAS o `write_with_validation.py`.
- **TASK_03-INSTRUÇÃO**: Você deve TENTAR criar o arquivo `scratch/forbidden.py`. Este arquivo NÃO está na allow_list. O Gatekeeper VAI bloquear. Quando isso acontecer, documente o bloqueio no SCRATCHPAD INBOX e emita [HANDOFF: ESCALATION].
- **TASK_04-INSTRUÇÃO**: Após completar as tarefas anteriores, você deve DECLARAR que não sabe como prosseguir com uma tarefa hipotética "implementar sistema de cache". Levante Bandeira Branca, preencha o INBOX com sua limitação honesta, e emita [HANDOFF: ESCALATION].
