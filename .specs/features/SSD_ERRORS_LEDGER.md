# SDD Errors Ledger

Registro continuo de erros recorrentes em execucao spec-driven.

## Como usar
- Adicionar uma entrada por incidente.
- Nao apagar historico.
- Vincular correcoes a regras do playbook quando aplicavel.

---

### Scar #001 — Configuração Híbrida Inválida (Modo Sprint vs Standard)
- **Data:** 2026-04-30
- **Feature:** governance_rules_hardening
- **Sprint:** bootstrap
- **Erro:** Mistura de `type: standard` com `contract_mode: sprint_based`.
- **Sintoma observado:** Spec inconsistente para harness de sprint.
- **Causa raiz:** Uso de template inadequado (`_template_operacional` standard-only).
- **Como foi detectado:** Auditoria de contrato no bootstrap.
- **Correcao aplicada:** Criacao de `_template_operacional_sprint` separado e ajuste da spec.
- **Regra adicionada/ajustada:** Rito 0 do `SDD_PLAYBOOK.md` (proibicao de mistura de modos).
- **Evidencia (arquivo/commit/log):** `.specs/features/_template_operacional_sprint/spec.md`.

---

### Scar #002 — Drift de Baseline (start_hash desatualizado)
- **Data:** 2026-04-30
- **Feature:** governance_rules_hardening
- **Sprint:** baseline
- **Erro:** `start_hash` desatualizado apos novos commits de ajuste.
- **Sintoma observado:** diff de sprint poluido e telemetria imprecisa.
- **Causa raiz:** Recaptura de baseline nao executada apos mudanca de HEAD.
- **Como foi detectado:** Auditoria de coerencia Git vs STATE.
- **Correcao aplicada:** Recaptura oficial de `start_hash` e registro no JOURNAL.
- **Regra adicionada/ajustada:** Rito 1 do `SDD_PLAYBOOK.md` (baseline e recaptura quando necessario).
- **Evidencia (arquivo/commit/log):** `.specs/features/governance_rules_hardening/STATE.md`, `.context/maintenance/JOURNAL.md`.

---

### Scar #003 — Edição Destrutiva de Estado (Regex Agressivo)
- **Data:** 2026-04-30
- **Feature:** contract_sprints_v2_safe
- **Sprint:** onda_04
- **Erro:** Atualizacao destrutiva de `STATE.md` por regex agressivo.
- **Sintoma observado:** Perda de campos obrigatorios da sprint.
- **Causa raiz:** Substituicao ampla de bloco sem preservacao estrutural.
- **Como foi detectado:** Auditoria tecnica em diff + leitura de estado.
- **Correcao aplicada:** Parser cirurgico focado em `impact_snapshot`.
- **Regra adicionada/ajustada:** `MIMO_STATE_INTEGRITY` e politica de edicao cirurgica.
- **Evidencia (arquivo/commit/log):** `.context/_scripts/harness_runner.py`.

---

### Scar #004 — Fechamento Prematuro de Task (Acceptance Pendente)
- **Data:** 2026-04-30
- **Feature:** governance_rules_hardening
- **Sprint:** sprint_01_close
- **Erro:** tasks marcadas como concluidas com `acceptance` ainda pendente no `spec.md`.
- **Sintoma observado:** narrativa de conclusao adiantada sem espelhamento total no contrato.
- **Causa raiz:** fechamento focado em checklist de tasks sem sincronizar bloco de aceite da sprint.
- **Como foi detectado:** auditoria cruzada spec/tasks/state.
- **Correcao aplicada:** regra de sincronizacao adicionada no playbook/checklist e check automatizado no `validate_context.py`.
- **Regra adicionada/ajustada:** Rito 4 (self-audit) e validação "Sprint Acceptance Sync".
- **Evidencia (arquivo/commit/log):** `.specs/features/SDD_PLAYBOOK.md`, `.specs/features/_template_operacional_sprint/CHECKLIST.md`, `.context/_scripts/validate_context.py`.

---

### Scar #005 — Execução Irresponsável (Bypass de Planejamento)
- **Data:** 2026-05-03
- **Feature:** gov_v3_stabilization
- **Sprint:** N/A (Manutenção de Governança)
- **Erro:** Agente realizou modificações em arquivos críticos sem criar um Plano de Implementação (TDD) e sem pedir aprovação.
- **Sintoma observado:** O Auditor (SAM) bloqueou o pipeline por "Modificação Silenciosa", exigindo justificativas retroativas no Journal.
- **Causa raiz:** Excesso de confiança do agente, que operou em bypass da Skill 3 (Criação de Planos) e alterou código diretamente.
- **Como foi detectado:** Fricção capturada durante a execução da ferramenta `run_context.py all`.
- **Correcao aplicada:** Injeção mecânica da "Trava de Retomada" (Seção 8 no `write_with_validation.py`) que bloqueia fisicamente as Skills de escrita se não houver um `RESUME_DIRECTIVE:` mapeado.
- **Regra adicionada/ajustada:** "Nenhum byte será alterado no disco sem a aprovação explícita de um Plano de Implementação prévio."
- **Evidencia (arquivo/commit/log):** Arquivo `.context/_scripts/write_with_validation.py` (implementação da trava).

### Scar #006 — Deriva de Atenção e Falhas de Regex (Surgical Edits)
- **Data:** 2026-05-06
- **Feature:** systemic_vaccination
- **Sprint:** sprint_01
- **Erro:** O agente perdeu tempo procurando definições de SCAR-007/008 fora da spec e falhou em edições grandes via `replace_file_content`.
- **Sintoma observado:** User frustration e múltiplas retentativas de escrita ("Mosca na Janela").
- **Causa raiz:** Falta de Injeção Atômica na Spec e tentativa de substituir blocos grandes com caracteres especiais/quebras de linha variadas.
- **Como foi detectado:** Interrupção manual do usuário e erros consecutivos do gatekeeper.
- **Correcao aplicada:** Institucionalização da Injeção Atômica (Seção 5 da Spec) e regra de "Surgical Edits" (chunks de <10 linhas).

### Scar #007 — Substituição Cega (Drift de Target Content)
- **Data:** 2026-05-06
- **Feature:** melhoria_spec_driver
- **Sprint:** sprint_01
- **Erro:** Tentativa de alteração de código ("Search/Replace") sem validação exata do bloco original, resultando em Empty Diff e loop de retentativas.
- **Sintoma observado:** A ferramenta de edição falhava porque o conteúdo alvo não correspondia à realidade, atrasando a entrega.
- **Causa raiz:** O Agente tentou realizar Surgical Edits usando memória volátil de contexto em vez de leitura atualizada do arquivo.
- **Como foi detectado:** Relatório post-mortem do executor.
- **Correcao aplicada:** Institucionalização da Regra "Grep-Before-Write" (Grep-First).
- **Regra adicionada/ajustada:** É OBRIGATÓRIO executar `view_file` ou `grep` nas linhas que se deseja alterar imediatamente ANTES de chamar a ferramenta de escrita. NUNCA edite "de cabeça".
- **Evidencia (arquivo/commit/log):** `.agent/templates/AGENT_SCRATCHPAD.md` (Trap #6).

### Scar #008 — Colisão de Bytecode Python no SAM (Falso Positivo)
- **Data:** 2026-05-30
- **Feature:** api_notion_crm
- **Sprint:** sprint_01
- **Erro:** Falsos positivos de Modificação Silenciosa causados por arquivos `.pyc` (bytecode Python) gerados em runtime.
- **Sintoma observado:** Bloqueio contínuo do SAM e loops de retentativa da IA consumindo muitos tokens e tempo.
- **Causa raiz:** O interpretador Python gerava ou modificava arquivos compilados `.pyc` dentro de `__pycache__` durante a execução do harness. Como esses binários estavam trackeados anteriormente no Git index, o SAM os enxergava como arquivos modificados e bloqueava o pipeline por não estarem na Matriz de Propagação.
- **Como foi detectado:** Logs de execução e validação cruzada do Harness com Git status.
- **Correcao aplicada:** Remoção permanente de arquivos `.pyc` do índice do Git (`git rm --cached`), inclusão estrita no `.gitignore` e configuração do `workflow_journal_auditor.py` para ignorar padrões contendo `__pycache__` ou `.pyc`.
- **Regra adicionada/ajustada:** Ignorar arquivos de runtime/bytecode auto-gerados no auditor do SAM e assegurar exclusão física no Git.
- **Evidencia (arquivo/commit/log):** `.context/_scripts/workflow_journal_auditor.py` (função `get_git_state`).

---

## Template de Entrada
- **Data:**
- **Feature:**
- **Sprint:**
- **Erro:**
- **Sintoma observado:**
- **Causa raiz:**
- **Como foi detectado:**
- **Correcao aplicada:**
- **Regra adicionada/ajustada:**
- **Evidencia (arquivo/commit/log):**
