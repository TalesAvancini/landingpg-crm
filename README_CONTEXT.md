---
Criado em: 2026-04-10 22:45
Ultima Atualizacao: 2026-05-03 01:54
Status: Ativo (v3.0.0 - Chain-Skills)
---

# 📖 README_CONTEXT.md — Guia de Operação Chain-Skills V3
> Diretriz oficial para humanos e agentes de IA operarem o ecossistema Antigravity com Governança Blindada.

## 🎯 1. Visão Geral
O diretório `.context/` é a **Fonte Única da Verdade (SSOT)**, mas a partir da v3.0, a execução é governada pela pasta `.agent/` e pelo protocolo **Chain-Skills**.
- 🛡️ **Zero-Trust**: Nenhuma escrita é permitida fora do escopo definido na Spec.
- 🧠 **Anti-Loop**: Falhas são documentadas no Scratchpad para evitar repetição de erros.
- ⛓️ **9 Skills**: Todo desenvolvimento segue uma cadeia determinística de 9 passos.

## 🧩 Pilares de Operação (v3.0.0+)
- **🛡️ Physical Gatekeeper**: O script `write_with_validation.py` é a única forma autorizada de alterar arquivos, garantindo que a IA não saia do escopo.
- **🧠 Metacognição**: O arquivo `AGENT_SCRATCHPAD.md` atua como a "memória de trabalho" da IA, impedindo loops infinitos em erros fatais.
- **✅ SAM Enforcement**: O Auditor Anti-Migué no pre-commit garante que o que está no Journal é EXATAMENTE o que está no Git.

---

## 📂 2. Estrutura em Camadas
| Camada | Pasta | Função |
|--------|-------|--------|
| 🧠 **Cognitiva** | `.context/brain/` | Regras mestras, Master Flow e Glossários. |
| 🤖 **Agenciamento** | `.agent/` | Templates de Spec V3, Scratchpads e Prompts de Subagentes. |
| 🛠️ **Manutenção** | `.context/maintenance/` | Memória contínua (Journal) e logs do Harness. |
| ⚙️ **Automação** | `.context/_scripts/` | Motores Python de validação, purge e gatekeeping. |
| 🛡️ **Qualidade** | `.husky/` | Gate de commit (Strict Mode). |

---

## 🔄 3. O Fluxo Chain-Skills (9 Skills)
Todo desenvolvimento deve seguir esta sequência:
1. **Skill 1-3**: Carregar contexto, extrair restrições e definir abordagem técnica.
2. **Skill 4-5**: Sincronizar Scratchpad e Trancar o Escopo na Spec.
3. **Skill 6**: Geração de Evidência (Escrita de código via Gatekeeper).
4. **Skill 7-9**: Auto-auditoria, Remediação (Journal Sync) e Handoff final.

---

## 🤖 4. Operando com o Anti-Loop
Se você receber um erro `[BLOCKED]` ou `[FATAL]`:
1. **PAUSE**: Não tente o mesmo comando novamente.
2. **SCRATCHPAD**: Abra o `AGENT_SCRATCHPAD.md` da feature.
3. **LOG**: Registre o Erro, a Hipótese do porquê falhou e o Novo Plano.
4. **EXECUTE**: Só então tente a correção.

---

## ⚙️ 5. Comandos Rápidos (v3.0.0)
```bash
# Validar integridade e conformidade SAM
npm run context:harness

# Sincronizar Journal e limpar specs antigas
npm run context:cleanup
npm run context:purge

# Mapear o projeto para a IA (Baixo consumo de tokens)
npm run context:map
```

> 💡 **Nota Final:** A governança V3 não é uma sugestão, é uma restrição física. Se o gatekeeper bloquear, a IA não passa. Respeite o fluxo.
