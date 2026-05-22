---
Criado em: 2026-05-04
Ultima Atualizacao: 2026-05-22 13:50
Status: Ativo
---

# 🧠 LEARNINGS.md (Memória Estratégica MiMo)

> "Aquele que não lembra o passado está condenado a repeti-lo."
> Gerado automaticamente por `learnings_aggregator.py`.

## 🚨 Top Cicatrizes Ativas (Scars)
*(Erros que custaram caro e NÃO devem ser repetidos)*

### [SCAR-001] Edição Destrutiva de Estado (Regex Agressivo) (Score: 324)
- **Última vez:** contract_sprints_v2_safe (2026-04-30)
- **O que aconteceu:** Atualizacao destrutiva de `STATE.md` por regex agressivo. -> Substituicao ampla de bloco sem preservacao estrutural.
- **A Regra:** `MIMO_STATE_INTEGRITY` e politica de edicao cirurgica.

### [SCAR-002] Execução Irresponsável (Bypass de Planejamento) (Score: 171)
- **Última vez:** gov_v3_stabilization (2026-05-03)
- **O que aconteceu:** Agente realizou modificações em arquivos críticos sem criar um Plano de Implementação (TDD) e sem pedir aprovação. -> Excesso de confiança do agente, que operou em bypass da Skill 3 (Criação de Planos) e alterou código diretamente.
- **A Regra:** "Nenhum byte será alterado no disco sem a aprovação explícita de um Plano de Implementação prévio."

### [SCAR-003] Configuração Híbrida Inválida (Modo Sprint vs Standard) (Score: 108)
- **Última vez:** governance_rules_hardening (2026-04-30)
- **O que aconteceu:** Mistura de `type: standard` com `contract_mode: sprint_based`. -> Uso de template inadequado (`_template_operacional` standard-only).
- **A Regra:** Rito 0 do `SDD_PLAYBOOK.md` (proibicao de mistura de modos).

### [SCAR-004] Drift de Baseline (start_hash desatualizado) (Score: 108)
- **Última vez:** governance_rules_hardening (2026-04-30)
- **O que aconteceu:** `start_hash` desatualizado apos novos commits de ajuste. -> Recaptura de baseline nao executada apos mudanca de HEAD.
- **A Regra:** Rito 1 do `SDD_PLAYBOOK.md` (baseline e recaptura quando necessario).

### [SCAR-005] Fechamento Prematuro de Task (Acceptance Pendente) (Score: 108)
- **Última vez:** governance_rules_hardening (2026-04-30)
- **O que aconteceu:** tasks marcadas como concluidas com `acceptance` ainda pendente no `spec.md`. -> fechamento focado em checklist de tasks sem sincronizar bloco de aceite da sprint.
- **A Regra:** Rito 4 (self-audit) e validação "Sprint Acceptance Sync".

### [SCAR-006] Deriva de Atenção e Falhas de Regex (Surgical Edits) (Score: 90)
- **Última vez:** systemic_vaccination (2026-05-06)
- **O que aconteceu:** O agente perdeu tempo procurando definições de SCAR-007/008 fora da spec e falhou em edições grandes via `replace_file_content`. -> Falta de Injeção Atômica na Spec e tentativa de substituir blocos grandes com caracteres especiais/quebras de linha variadas.
- **A Regra:** 

### [SCAR-007] Substituição Cega (Drift de Target Content) (Score: 90)
- **Última vez:** melhoria_spec_driver (2026-05-06)
- **O que aconteceu:** Tentativa de alteração de código ("Search/Replace") sem validação exata do bloco original, resultando em Empty Diff e loop de retentativas. -> O Agente tentou realizar Surgical Edits usando memória volátil de contexto em vez de leitura atualizada do arquivo.
- **A Regra:** É OBRIGATÓRIO executar `view_file` ou `grep` nas linhas que se deseja alterar imediatamente ANTES de chamar a ferramenta de escrita. NUNCA edite "de cabeça".

---

## ⚠️ Alertas Automáticos (Harness Log)
- **[LOOP DETECTADO]** Spec `synapse_workflow` falhou 6 vezes recentemente. Requer análise estratégica.
- **[LOOP DETECTADO]** Spec `oracle_v3` falhou 5 vezes recentemente. Requer análise estratégica.
- **[LOOP DETECTADO]** Spec `gov_chain_v3_phase2_dryrun` falhou 12 vezes recentemente. Requer análise estratégica.
- **[LOOP DETECTADO]** Spec `gov_v3_stress_test` falhou 3 vezes recentemente. Requer análise estratégica.
- **[LOOP DETECTADO]** Spec `manual` falhou 5 vezes recentemente. Requer análise estratégica.
- **[LOOP DETECTADO]** Spec `blast_radius_mvp` falhou 3 vezes recentemente. Requer análise estratégica.
