# CHECKLIST Chain-Skills V3 (The 9 Skills)

## Fase A: Preparação (Skills 1-3)
- [ ] **Skill 1 (Context Loader):** `RULES.md` lido e regras citadas no `STATE.md`.
- [ ] **Skill 2 (Spec Reader):** Contrato da sprint atual validado sem ambiguidades.
- [ ] **Skill 3 (Strategy Planner):** `AGENT_SCRATCHPAD.md` inicializado com a estratégia técnica.

## Fase B: Blindagem (Skills 4-5)
- [ ] **Skill 4 (Baseline Anchor):** `git status` limpo e `start_hash` capturado.
- [ ] **Skill 5 (Scope Guard):** `allow_list` trancada na Spec e copiada para o `STATE.md`.

## Fase C: Execução (Skill 6)
- [ ] **Skill 6 (Evidence Generation):** Código escrito exclusivamente via `write_with_validation.py`.
- [ ] Nenhuma edição fora do escopo (`SCOPE_BLOWOUT` evitado).
- [ ] Tasks atualizadas imediatamente após cada alteração.

## Fase D: Fechamento (Skills 7-9)
- [ ] **Skill 7 (Self Audit):** Cópia exata entre `Git Diff` e `Matriz de Propagação` do Journal.
- [ ] **Skill 8 (Remediation):** Erros bloqueados foram corrigidos e logados no Scratchpad.
- [ ] **Skill 9 (Handoff):** `npm run context:harness` rodado com sucesso (PASS).

Se o Harness falhar, volte para a Skill 8 e corrija no Scratchpad antes de tentar novamente.
