---
name: closure-thinker
description: Specialized skill to generate, audit, or refactor Closure Reports (CLOSURE.md). Ensures high-fidelity narrative of what was actually delivered vs planned.
---

# Closure Thinker — O Protocolo de Síntese

Esta skill deve ser acionada na **Skill 9 (HANDOFF)** do Spec-Driver ou a qualquer momento para auditar a história de uma feature.

## Instruções de Execução

### Step 1: Mapeamento de Realidade (Audit)
1. **Leia a Spec Original:** Identifique o "O Quê" e o "Porquê" iniciais. Verifique o campo `origin` para rastrear a ideia-raiz.
2. **Consulte o JOURNAL.md:** Filtre todas as entradas relacionadas ao `executor_context_id` desta feature. Isso reconstrói a cronologia real.
3. **Reality Check (Git):** Use `git log -p -- .specs/features/<id>/` para ver o diff exato do que entrou no repositório.

### Step 2: Análise de Delta (Plano vs. Entrega)
Responda mentalmente antes de escrever:
- "O que a spec pedia que NÃO foi feito?"
- "O que foi feito que NÃO estava na spec (escopo emergente)?"
- "A solução técnica final divergiu do `TECHNICAL_APPROACH` (Skill 3) do `STATE.md`?"

### Step 3: Extração de Cicatrizes (The Scar Tissue)
Analise o `AGENT_SCRATCHPAD.md` (seção INBOX) e o `HARNESS_LOG.md`.
- Identifique erros que bloquearam a execução.
- Transforme-os em lições aprendidas (formato SCAR) para o `LEARNINGS.md`.

### Step 4: Redação do CLOSURE.md
Use o template em `.agent/templates/CLOSURE.md`.

**Regras de Redação:**
1. **Factualidade:** Não use "eu acho" ou "provavelmente". Use "Arquivos X e Y foram modificados para implementar a lógica Z".
2. **Rastreabilidade:** Garanta que os hashes de commit e datas estejam precisos.
3. **Backlog:** Se algo ficou de fora por restrição de tempo ou complexidade, registre como item de backlog acionável.

## Protocolo de Refatoração (Para Closures mal feitos)
Se o usuário pedir para "refazer um closure":
1. Trate o `CLOSURE.md` atual como uma "alucinação potencial".
2. Ignore o texto atual e repita o **Step 1** (Mapeamento de Realidade) do zero.
3. Compare sua nova descoberta com o closure antigo.
4. Sobrescreva o arquivo com a verdade factual baseada no Git e Journal.

## Checklist Final
- [ ] O problema original está claro?
- [ ] O delta (o que mudou) está 100% mapeado na tabela de modificações?
- [ ] O Blast Radius real (propagação) está coerente com o Journal?
- [ ] Existem cicatrizes úteis para o futuro do projeto?
