---
Criado em: 2026-04-10 22:45
Ultima Atualizacao: 2026-04-11 23:30
Status: Ativo (v2.5.2)
---

# 📖 README_CONTEXT.md — Guia de Operação do Framework
> Diretriz oficial para humanos e agentes de IA operarem o diretório `.context/` no dia a dia.

## 🎯 1. Visão Geral
O diretório `.context/` é a **Fonte Unica da Verdade (SSOT)** do projeto. Ele existe para:
- 🧠 Manter a IA alinhada, previsivel e livre de alucinacoes.
- 📐 Garantir rastreabilidade tecnica, de negocio e de decisoes.
- ⚙️ Automatizar validacao, sincronizacao e limpeza de contexto.
- 🛡️ Impedir que codigo e documentacao divirjam ao longo do tempo.

**Regra de Ouro:** `Se nao esta no .context, nao existe. O codigo deve ser o reflexo fiel do contexto.`

## 🧩 Novos Pilares de Operação (v2.5.2+)
- **🛡️ Harness:** O pipeline aborta automaticamente se uma Spec referenciar tabelas/campos inexistentes no `schema.sql` ou se handoffs estiverem incompletos.
- **🔍 Oracle:** Ao detectar ambiguidade, execute `npm run context:oracle "sua pergunta"`. Retorno com `confidence < 0.5` pausa o fluxo e exige `[oracle:uncertain]` no `JOURNAL.md`.
- **📖 Karpathy:** Todo claim técnico adicionado ao `.context/` deve conter `> Fonte: raw/nome-arquivo.md`. O `pre-commit` roda em modo `--strict` e rejeita commits sem citação.

---

## 📂 2. Estrutura em Camadas
| Camada | Arquivos Principais | Função |
|--------|---------------------|--------|
| 🧠 **Cognitiva** | `brain/` (`RULES`, `MASTER_FLOW`, `AGENT_REGISTRY`, `PROMPT_LIBRARY`, `PRD`) | Governanca, roteamento, execucao e requisitos. |
| 💼 **Mercado** | `market/` | Camada Estratégica, limites operacionais e compliance financeiro. |
| 🛠️ **Manutencao** | `maintenance/` (`JOURNAL`, `TECH_REQ`, `rebuild_guide`, `schema.sql`) | Memoria continua, inventario tecnico e recovery. |
| 📊 **Monitoramento** | `monitoring/` (`CONTEXT_HEALTH.md`) | Dashboard de integridade e limites de sessao. |
| ⚙️ **Automacao** | `_scripts/*.py`, `run_context.py` | Validacao, purge, sync, harness e orquestracao. (SSOT de Execucao). |
| 🛡️ **Qualidade** | `tests/test_context.py`, `.husky/` | Testes automaticos e gate de commit. |

---

## 🔄 3. Fluxo de Trabalho Diário (Day-to-Day)

### 🌅 Inicio da Sessao (Sunrise)
1. Verifique a saude do contexto: `npm run context:validate`
2. Leia `brain/RULES.md` + `brain/PRD.md` ativo + ultimas 30 linhas do `maintenance/JOURNAL.md`.
3. Declare a role no chat: `🤖 Ativando @[role] | Escopo: [descricao]`

### 💻 Durante o Desenvolvimento
- Siga estritamente os templates do `brain/PROMPT_LIBRARY.md`.
- Respeite o `Context Gate` antes de gerar codigo.
- Em cruzamentos de dominio, registre handoff no `maintenance/JOURNAL.md`.
- Nunca hardcode segredos; use `[VAR_NAME]` + `.env`.

### 🌙 Fim da Sessao / Pre-Commit (Sunset)
1. Execute `npm run context:sync` se adicionou libs ou mudou schema.
2. Responda ao prompt da IA: `"Deseja que eu atualize o contexto agora?"`
3. Commit normal -> Husky roda `npm run context:all` automaticamente.
4. Se passar: ✅ merge seguro. Se falhar: 🔍 corrija o contexto antes de forcar (Harness, Lint e Oráculo barrarão desvios).

---

## 🤖 4. Operando com Agentes de IA

| Situacao | Acao Recomendada |
|----------|------------------|
| **Ativacao** | Sempre comece com `🤖 Ativando @[role] | Tarefa: [...]` |
| **Isolamento** | A IA so carrega `Global + Role-Specific + Task-Ephemeral`. |
| **Handoff** | Se cruzar 2+ dominios -> pausa -> registra no `maintenance/JOURNAL.md` -> proxima role assume. |
| **Prompt Padronizado** | Use `brain/PROMPT_LIBRARY.md`. Substitua `{{...}}` e cole no chat. |
| **Alucinacao Suspeita** | Execute `npm run context:validate` e peca: `"Valide o contexto antes de prosseguir."` |

---

## ⚙️ 5. Comandos Rápidos (Cheat Sheet v2.5.2)
```bash
# Validar integridade + estimar tokens
npm run context:validate

# Consultar Oráculo antes de assumir ambiguidades
npm run context:oracle "qual regex de validação?"

# Checar citações epistemológicas (modo manual: WARN-ONLY)
npm run context:lint

# Pipeline completo (orquestrado por run_context.py, lint vira STRICT-MODE aqui)
npm run context:all

# Limpar specs inativas / Sincronizar deps / Purge Journal
npm run context:cleanup
npm run context:sync
npm run context:purge
```
**🌎 Fuso Horário:** Por padrão, todos os artefatos temporais usam **Brasília (-3h)**. Exporte `CONTEXT_TIMEZONE="..."` para sobrescrever nativamente.

> 💡 *Nota:* Todos os comandos são roteados pelo `run_context.py`. Isso garante compatibilidade nativa Windows/WSL/Linux no `pre-commit`, sem dependências de shell.

---

## 🛡️ 6. Gate de Qualidade (Husky & CI)
- **Pre-commit:** Bloqueia commits se o `npm run context:all` falhar (Harness aborta, ou Lint em modo Strict acusa falta de fonte crua).
- **CI/CD:** O GitHub Actions roda o pipeline completo (`python run_context.py all`) em cada Pull Request para garantir consistencia remota.

---

## ✅ 7. Checklist de Operacao & Implantacao

### 🆕 Novo Projeto / Onboarding (The Fool's Cut)
- [ ] **Visão Humana:** Crie o arquivo `brain/VISION.md` (veja template).
- [ ] **Enriquecimento:** Execute `npm run context:enrich`. A IA gerará o `INCEPTION.proposed.md`.
- [ ] **Ratificação:** Revise a proposta. Se aprovado, renomeie para `INCEPTION.md` e mude `status` para `ACTIVE`.
- [ ] **Consistência:** Execute `npm run context:validate` para garantir que o projeto está operando em modo governado.

### 🚀 Feature / Desenvolvimento Normal
- [ ] `brain/PRD.md` preenchido com objetivos e criterios de aceite.
- [ ] `Context Gate` validado.
- [ ] Roles mapeadas na tabela de roteamento do PRD.

### ✅ Antes do Commit / PR
- [ ] `npm run context:validate` retorna `[SUCCESS]`.
- [ ] Secrets nao estao no codigo (usar `.env`).
- [ ] Husky pre-commit passou sem bloqueios.

---

> 💡 **Nota para a Equipe:** Este framework e vivo. Revise este guia a cada nova fase do `ROADMAP.md`. Um contexto desatualizado gera falsa sensacao de controle.

🚀 **Pronto para operar.** Mantenha o `.context/` enxuto, valido e atualizado. A IA fara o resto.
