# SDD Errors Ledger

Registro continuo de erros recorrentes em execucao spec-driven.

## Como usar
- Adicionar uma entrada por incidente.
- Nao apagar historico.
- Vincular correcoes a regras do playbook quando aplicavel.

---

## Template de Entrada
- Data:
- Feature:
- Sprint:
- Erro:
- Sintoma observado:
- Causa raiz:
- Como foi detectado:
- Correcao aplicada:
- Regra adicionada/ajustada:
- Evidencia (arquivo/commit/log):

---

## Entradas Iniciais

### 2026-04-30 | governance_rules_hardening | bootstrap
- Erro: Mistura de `type: standard` com `contract_mode: sprint_based`.
- Sintoma observado: spec inconsistente para harness de sprint.
- Causa raiz: Uso de template inadequado (`_template_operacional` standard-only).
- Como foi detectado: Auditoria de contrato no bootstrap.
- Correcao aplicada: Criacao de `_template_operacional_sprint` separado e ajuste da spec.
- Regra adicionada/ajustada: Rito 0 do `SDD_PLAYBOOK.md` (proibicao de mistura de modos).
- Evidencia (arquivo/commit/log): `.specs/features/_template_operacional_sprint/spec.md`.

### 2026-04-30 | governance_rules_hardening | baseline
- Erro: `start_hash` desatualizado apos novos commits de ajuste.
- Sintoma observado: diff de sprint poluido e telemetria imprecisa.
- Causa raiz: Recaptura de baseline nao executada apos mudanca de HEAD.
- Como foi detectado: Auditoria de coerencia Git vs STATE.
- Correcao aplicada: Recaptura oficial de `start_hash` e registro no JOURNAL.
- Regra adicionada/ajustada: Rito 1 do `SDD_PLAYBOOK.md` (baseline e recaptura quando necessario).
- Evidencia (arquivo/commit/log): `.specs/features/governance_rules_hardening/STATE.md`, `.context/maintenance/JOURNAL.md`.

### 2026-04-30 | contract_sprints_v2_safe | onda_04
- Erro: Atualizacao destrutiva de `STATE.md` por regex agressivo.
- Sintoma observado: Perda de campos obrigatorios da sprint.
- Causa raiz: Substituicao ampla de bloco sem preservacao estrutural.
- Como foi detectado: Auditoria tecnica em diff + leitura de estado.
- Correcao aplicada: Parser cirurgico focado em `impact_snapshot`.
- Regra adicionada/ajustada: `MIMO_STATE_INTEGRITY` e politica de edicao cirurgica.
- Evidencia (arquivo/commit/log): `.context/_scripts/harness_runner.py`.

### 2026-04-30 | governance_rules_hardening | sprint_01_close
- Erro: tasks marcadas como concluidas com `acceptance` ainda pendente no `spec.md`.
- Sintoma observado: narrativa de conclusao adiantada sem espelhamento total no contrato.
- Causa raiz: fechamento focado em checklist de tasks sem sincronizar bloco de aceite da sprint.
- Como foi detectado: auditoria cruzada spec/tasks/state.
- Correcao aplicada: regra de sincronizacao adicionada no playbook/checklist e check automatizado no `validate_context.py`.
- Regra adicionada/ajustada: Rito 4 (self-audit) e validação "Sprint Acceptance Sync".
- Evidencia (arquivo/commit/log): `.specs/features/SDD_PLAYBOOK.md`, `.specs/features/_template_operacional_sprint/CHECKLIST.md`, `.context/_scripts/validate_context.py`.
