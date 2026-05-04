---
Ultima Atualizacao: 2026-04-30 02:45
Status: 🔥 HARDENED (v2.5.2) - Agnóstico e Técnico
---

# skill mãe: tlc-spec-driven

# 🔗 TLC_INTEGRATION.md: O Córtex de Execução
> Ponte definitiva entre Governança (`.context/`) e Execução Atômica (`.specs/`).
> 💡 *A Fonte de Intenção (Plano/PRD) diz O QUÊ. A Spec TLC diz COMO. O Flash-Harness prova que FOI FEITO.*

---

> **Estrutura Oficial V3.5** para a pasta `.specs`:

.specs/features/[feature]/     <-- O "CANTEIRO DE OBRAS" (O que eu gero para executar)
├── spec.md                    <-- O CONTRATO: Extraído do plano, ou prdzinho, qualquer nome que remeta o arquivo de planejamento que embasa a spec.md .
├── design.md                  <-- O DESENHO: Diagramas/Arquitetura (Se for complexo).
├── tasks.md                   <-- O PASSO-A-PASSO: Checklist atômica com 'Verify'.
└── STATE.md                   <-- A MEMÓRIA VIVA: Decisões, logs e estado da sessão."


## 🔄 Ciclo de Vida Híbrido (v2.5.2)
1. **INTENT:** Documento ativo define a intenção.
2. **SPECIFY:** Hub gera `spec.md` via `specify.md`.
3. **SPRINT PLANNING:** Organização no `tasks.md` via `tasks.md`. **Foco: TDD**.
4. **IMPLEMENT:** Execução mecânica via `@spec-driver` usando `implement.md`.
5. **VERIFY:** Validação técnica via `validate.md`.
6. **SYNC:** Sincronização final via `session-handoff.md`.

## 📏 Regras de Ouro (Zero Migué)
- 🧪 **TDD e Verificação:** Proibido codar sem critério de prova técnica.
- ⚡ **Flash-Harness Mandatório:** Diário de Bordo estruturado visível ANTES de cada ação.
- 📦 **Single-Spec / Multi-Sprint:** Uma Spec por feature, progresso fatiado no `tasks.md`.
- 🛡️ **Execution Gatekeeper:** O `STATE.md` dita fisicamente se você pode ou não escrever no disco (Skill 6 - `write_with_validation.py`). Se bloqueado, exija a vacina `RESUME_DIRECTIVE:` do humano.

---

## 📖 Glossário de Referências (Pasta: `C:\Users\User\.gemini\skills\tlc-spec-driven`)
Abaixo estão as 16 sub-skills que podem ser utilizadas, com base no conteúdo real do diretório global:

1.  **project-init.md:** Protocolo de inicialização e definição de objetivos do projeto.
2.  **roadmap.md:** Criação e gestão do `ROADMAP.md` (Milestones e Capabilites).
3.  **brownfield-mapping.md:** Análise de código existente e mapeamento de stack tecnológica.
4.  **concerns.md:** Registro de dívidas técnicas, riscos e áreas de atenção.
5.  **specify.md:** Transformação de intenção em requisitos atômicos com IDs.
6.  **discuss.md:** Protocolo de conversa para resolução de ambiguidades.
7.  **design.md:** Definição de arquitetura, componentes e lógica técnica.
8.  **tasks.md:** Criação de checklists atômicos com critérios de `Verify`.
9.  **implement.md:** Protocolo de execução técnica e incremento de código.
10. **quick-mode.md:** Modo de execução rápida para tarefas de baixa complexidade (≤3 arquivos).
11. **state-management.md:** Gestão do arquivo `STATE.md` (Estado, decisões e bloqueios).
12. **validate.md:** Protocolo de testes, UAT e verificação de critérios de aceite.
13. **code-analysis.md:** Métodos para auditoria e análise estrutural de código.
14. **session-handoff.md:** Protocolo para pausar e retomar sessões de trabalho.
15. **context-limits.md:** Gestão de limites de contexto e tokens.
16. **coding-principles.md:** Princípios fundamentais de codificação aplicados ao TLC.
> *Este documento garante que o "Cérebro" e o "Músculo" operem em harmonia.*
