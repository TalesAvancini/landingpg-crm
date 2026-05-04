---
Criado em: 2026-05-04
Ultima Atualizacao: 2026-05-04 00:09
Status: Ativo
---

# 🧠 LEARNINGS.md (Memória Estratégica MiMo)

> "Aquele que não lembra o passado está condenado a repeti-lo."
> Gerado automaticamente por `learnings_aggregator.py`.

## 🚨 Top Cicatrizes Ativas (Scars)
*(Erros que custaram caro e NÃO devem ser repetidos)*

### [SCAR-001] Configuração Híbrida Inválida (Modo Sprint vs Standard) (Score: 50)
- **Última vez:** governance_rules_hardening (2026-04-30)
- **O que aconteceu:** Mistura de `type: standard` com `contract_mode: sprint_based`. -> Uso de template inadequado (`_template_operacional` standard-only).
- **A Regra:** Rito 0 do `SDD_PLAYBOOK.md` (proibicao de mistura de modos).

### [SCAR-002] Drift de Baseline (start_hash desatualizado) (Score: 50)
- **Última vez:** governance_rules_hardening (2026-04-30)
- **O que aconteceu:** `start_hash` desatualizado apos novos commits de ajuste. -> Recaptura de baseline nao executada apos mudanca de HEAD.
- **A Regra:** Rito 1 do `SDD_PLAYBOOK.md` (baseline e recaptura quando necessario).

### [SCAR-003] Edição Destrutiva de Estado (Regex Agressivo) (Score: 50)
- **Última vez:** contract_sprints_v2_safe (2026-04-30)
- **O que aconteceu:** Atualizacao destrutiva de `STATE.md` por regex agressivo. -> Substituicao ampla de bloco sem preservacao estrutural.
- **A Regra:** `MIMO_STATE_INTEGRITY` e politica de edicao cirurgica.

### [SCAR-004] Fechamento Prematuro de Task (Acceptance Pendente) (Score: 50)
- **Última vez:** governance_rules_hardening (2026-04-30)
- **O que aconteceu:** tasks marcadas como concluidas com `acceptance` ainda pendente no `spec.md`. -> fechamento focado em checklist de tasks sem sincronizar bloco de aceite da sprint.
- **A Regra:** Rito 4 (self-audit) e validação "Sprint Acceptance Sync".

### [SCAR-005] Execução Irresponsável (Bypass de Planejamento) (Score: 50)
- **Última vez:** gov_v3_stabilization (2026-05-03)
- **O que aconteceu:** Agente realizou modificações em arquivos críticos sem criar um Plano de Implementação (TDD) e sem pedir aprovação. -> Excesso de confiança do agente, que operou em bypass da Skill 3 (Criação de Planos) e alterou código diretamente.
- **A Regra:** "Nenhum byte será alterado no disco sem a aprovação explícita de um Plano de Implementação prévio."

---

## ⚠️ Propostas de Novas Regras
*(Nenhuma regra nova consolidada neste ciclo)*
