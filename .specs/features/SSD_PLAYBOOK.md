# 📜 SSD-Chain Playbook (Spec-Driven Discipline Chain) - V3.0
> Manual definitivo para execução de features com Governança Blindada e Anti-Loop.

## 🎯 Objetivo
Eliminar a afobação do executor e garantir que toda mudança de código seja precedida por carregamento de contexto e validação de restrições.

## ⛓️ O Ciclo das 9 Skills (Obrigatório)
Toda feature deve progredir através destas skills no `STATE.md`:

### Fase A: Preparação (Skills 1-3)
*   **MIMO_MEMORY**: (Automático) Injeção de cicatrizes estratégicas via `inject_learnings.py` para prevenir reincidência de erros.
1.  **CONTEXT_LOADED**: Ler as regras mestras (`RULES.md`) e a Spec enriquecida (`.enriched.md`).
2.  **CONSTRAINTS_EXTRACTED**: Identificar o que NÃO pode ser feito (escopo negativo).
3.  **TECHNICAL_APPROACH**: Definir o plano de implementação ANTES de tocar no código.

### Fase B: Blindagem (Skills 4-5)
4.  **SCRATCHPAD_SYNCED**: Inicializar o `AGENT_SCRATCHPAD.md` com a estratégia atual.
5.  **SCOPE_LOCKED**: Trancar a `allow_list` na Spec da sprint.

### Fase C: Execução (Skills 6-7)
6.  **EVIDENCE_GENERATION**: Escrita física de código via `write_with_validation.py`.
7.  **SELF_AUDIT**: O próprio executor roda o Harness para validar sua entrega.

### Fase D: Fechamento (Skills 8-9)
8.  **REMEDIATION**: Sincronizar o `JOURNAL.md` e limpar rastros de "Modificação Silenciosa".
9.  **HANDOFF**: Gerar o relatório final para o QA-Validator.

---

## 🧠 O Rito do Córtex (MiMo)
O MiMo (Memory Injection Module) insere *Scars* (Cicatrizes de erros passados) no topo do arquivo `.enriched.md`.
- **Injeção Obrigatória:** A Spec só inicia após o comando `npm run context:inject`.
- **Leitura Exclusiva:** Agentes executores devem ler **APENAS** o `.enriched.md` e ignorar o `spec.md` limpo.
- **Score Elevado (>200):** Se uma Scar possuir pontuação acima de 200 (gravidade alta ou recorrência crônica), o Executor DEVE registrar no seu `STRATEGY_LOG` (Skill 3) o plano de mitigação específico para evitar a repetição daquele erro durante a sprint.

## 🛡️ Protocolo Anti-Loop e Escalation
Sempre que o Gatekeeper ou o Harness retornar um erro `[BLOCKED]` ou `[FATAL]`, a IA (Executor) entrará em bloqueio cognitivo:
1.  Ela **NÃO** repetirá a ação.
2.  Ela documentará o erro na seção `INBOX` do `AGENT_SCRATCHPAD.md`.
3.  Ela ejetará o controle com o comando `[HANDOFF: ESCALATION]`.

## 👑 O Papel do Orquestrador (Desbloqueio e Sistema Imunológico)
O Orquestrador (Humano ou IA Master) é o único autorizado a destravar o Executor após um Escalation.
1. **Resolução de Diretiva:** Abra o Scratchpad, leia o INBOX e escreva a solução na seção `DIRECTIVES`.
2. **Gatilho de Despertar (Invocação Explícita):** Não responda com comandos genéricos. Para evitar a Amnésia de Persona, invoque o agente explicitamente:
   > `@spec-driver [RESUME] Diretiva injetada no Scratchpad. Leia a seção DIRECTIVES e retome a execução de onde parou no STATE.md.`
3. **O Sistema Imunológico (Faxina Cognitiva):** Se o mesmo erro for escalado em múltiplas sprints, o Orquestrador deve limpar o Scratchpad e **promover a regra permanentemente** adicionando-a ao `SSD_ERRORS_LEDGER.md` ou atualizando as restrições da Spec.

## 🚫 Regras Proibidas (Zero-Trust)
- Proibido editar arquivos de regras (`RULES.md`, `MASTER_FLOW.md`) sem autorização de intervenção nível 3.
- Proibido marcar tarefas como concluídas `[x]` ANTES de validar a escrita física.
- Proibido ignorar erros do Harness (SAM). O pre-commit VAI barrar.

---

## 📅 Rito de Selagem
Uma feature só é considerada "CLOSED" quando o `JOURNAL.md` reflete o Git e o `STATE.md` exibe as 9 Skills com status `[x]`.

🚀 **Siga a Cadeia. Confie no Gatekeeper.**
