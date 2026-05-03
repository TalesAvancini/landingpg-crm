---
feature_id: gov_chain_v3_phase1
type: standard
contract_mode: sprint_based
status: completed
version: 1.0.0
created_at: "2026-05-03"
---

# Feature: Chain-Skills V3 - Fase 1 (Fundação)

## 1. O Problema
A implementação da governança Chain-Skills V3 requer uma fundação mecânica robusta, especificamente a restrição controlada de edições no disco. Atualmente, o subagente possui liberdade total para editar arquivos, resultando em comportamentos impulsivos que furam o escopo. Precisamos instalar os controles físicos antes de atualizar a cadeia lógica.

## 2. A Solução
Implementar a Fase 1 da V3 através de:
1. Um gatekeeper físico (`write_with_validation.py`) que audita todas as requisições de escrita contra as métricas do "Tier" e o "Scope".
2. Uma nova skill restrita (`methodical_writer.json`) que força o executor a passar pelo gatekeeper.
3. Atualização instrucional do prompt `spec-driver.md` para implementar o bloqueio cognitivo.

## 3. Escopo
- **ALLOW:**
  - Criação do `.agent/skills/methodical_writer.json`.
  - Criação do `.context/_scripts/write_with_validation.py`.
  - Atualização do `spec-driver.md` (frontmatter e prompt base).
- **DENY:**
  - Modificação de outros scripts de governança como SAM ou Harness nesta fase.

## 4. Requisitos Funcionais (Acceptance)
- [ ] `methodical_writer.json` criado e configurado conforme o plano V3.
- [ ] `write_with_validation.py` desenvolvido, validando os 4 parâmetros obrigatórios (`<feature_id> <task_id> <file_path> <line_count>`).
- [ ] Limite de linhas (Tier 1: 15, Tier 2: 50) imposto no script.
- [ ] `spec-driver.md` atualizado com as novas instruções da V3 e bloqueio cognitivo de ferramentas genéricas de edição.

## 5. Estratégia de Deploy
Deploy isolado. Estes artefatos são componentes novos (ou updates limitados a um subagente) e não afetam a validação de segurança global imediatamente. O teste completo da cadeia ocorrerá na Fase 2.
