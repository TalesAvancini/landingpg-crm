# Relatorio de Atualizacao: FLOW_SDD.md

## Data de Geracao
2026-05-26

## Escopo
Analise de divergencias entre `.context/brain/FLOW_SDD.md` e os arquivos de referencia do ecossistema H.O.K Forge, com recomendacoes de atualizacao.

---

## 1. DIVERGENCIAS CRITICAS (Must Fix)

### 1.1 Localizacao do `SSD_PLAYBOOK.md`
- **FLOW_SDD.md diz:** `.specs/features/SSD_PLAYBOOK.md`
- **Realidade:** `.specs/features/SSD_PLAYBOOK.md` existe fisicamente e contem as 9 skills.
- **Status:** OK — localizacao correta.

### 1.2 Localizacao do `SSD_ERRORS_LEDGER.md`
- **FLOW_SDD.md diz:** `.specs/features/SSD_ERRORS_LEDGER.md`
- **Realidade:** Arquivo existe e esta ativo com 7 SCARs documentadas.
- **Status:** OK.

### 1.3 Skill Names Mismatch: SSD_PLAYBOOK vs spec-driver
- **SSD_PLAYBOOK.md** (linhas 10-26) define as skills com nomes **diferentes** do `spec-driver.md`:
  | Fase | SSD_PLAYBOOK | spec-driver.md |
  |------|-------------|----------------|
  | A | MIMO_MEMORY, CONTEXT_LOADED, CONSTRAINTS_EXTRACTED, TECHNICAL_APPROACH | context-loader, spec-digest, strategy-planner |
  | B | SCRATCHPAD_SYNCED, SCOPE_LOCKED | baseline-anchor, scope-guard |
  | C | EVIDENCE_GENERATION, SELF_AUDIT | methodical-writer, integrity-check |
  | D | REMEDIATION, HANDOFF | self-audit, handoff |
- **Impacto:** O `FLOW_SDD.md` (secao 4) usa os nomes do `spec-driver.md` (Skill 1-9), mas o `SSD_PLAYBOOK.md` usa nomes semanticos diferentes. Isso cria confusao para agentes que consultam ambos.
- **Recomendacao:** Unificar a nomenclatura ou adicionar uma tabela de mapeamento cruzado no `FLOW_SDD.md`.

### 1.4 Matriz de Propagacao Desatualizada
- **FLOW_SDD.md (Tabela Resumo, linha 205-215):** `spec-driver.md` -> MUST sync com `MASTER_FLOW`, `RULES`, `spec_v3`, `SCRATCHPAD`, `PLAYBOOK`.
- **spec-driver.md (linhas 9-11):** Declara acoplamento com `AGENT_REGISTRY.md`, `MASTER_FLOW.md`, `RULES.md`, `spec_v3.md`, `AGENT_SCRATCHPAD.md` e `SSD_PLAYBOOK.md`.
- **Divergencia:** A tabela do FLOW_SDD.md omite `AGENT_REGISTRY.md` na coluna MUST sync para `spec-driver.md`, mas o proprio arquivo de subagente o lista.
- **Recomendacao:** Adicionar `AGENT_REGISTRY.md` como MUST sync na linha do `spec-driver.md`.

---

## 2. DIVERGENCIAS MODERADAS (Should Review)

### 2.1 Orquestrador SDD nao mencionado no diagrama de arquitetura
- **FLOW_SDD.md (diagrama Mermaid, linhas 10-58):** Nao inclui o `@sdd-orchestrator` como no no diagrama, embora seja a skill que orquestra todo o ciclo.
- **AGENT_REGISTRY.md:** Registra `@sdd-orchestrator` como Orquestrador do ciclo de vida SDD.
- **Recomendacao:** Adicionar o `@sdd-orchestrator` no diagrama como um participante ativo (possivelmente na Camada de Motor ou como um Hub central).

### 2.2 Skill `semantic-propagation` nao mencionada
- **FLOW_SDD.md:** Nao faz referencia a skill `semantic-propagation` nem ao `@propagation-auditor`.
- **FLOW_PROPAGATION.md:** Documenta extensivamente o fluxo de propagacao.
- **sdd-orchestrator SKILL.md (linhas 82-84):** Inclui o handoff de propagacao como parte do Step 5 (Final Closure).
- **Recomendacao:** Adicionar uma nota ou secao transversal mencionando que o fechamento de feature inclui propagacao semantica via `@propagation-auditor` ou `@qa-validator`.

### 2.3 Ausencia de `CLOSURE.md` no diagrama
- **FLOW_SDD.md:** O `CLOSURE.md` nao aparece no diagrama Mermaid nem nos 9 arquivos listados.
- **spec-driver.md (linha 36):** Skill 9 exige geracao do `CLOSURE.md`.
- **RULES.md (1.14):** Protocolo de Fechamento de Feature exige `CLOSURE.md`.
- **Recomendacao:** Incluir `CLOSURE.md` como um artefato de saida da Camada de Estado ou Motor.

### 2.4 `AGENT_SCRATCHPAD.md` template vs instancia
- **FLOW_SDD.md:** Localiza o SCRATCHPAD em `.agent/templates/AGENT_SCRATCHPAD.md`.
- **sdd-orchestrator SKILL.md (linha 52):** Exige copiar o template para `.specs/features/<feature_id>/AGENT_SCRATCHPAD.md`.
- **Recomendacao:** Deixar claro no FLOW_SDD.md que o SCRATCHPAD existe em duas formas: template (read-only) e instancia fisica por feature.

---

## 3. DIVERGENCIAS LEVES (Nice to Have)

### 3.1 Status de metadados desatualizado
- **FLOW_SDD.md:** Nao possui frontmatter com `Criado em` / `Ultima Atualizacao` / `Status`.
- **Padrao do projeto:** Todos os arquivos em `.context/brain/` possuem esse frontmatter (ex: `MASTER_FLOW.md`, `RULES.md`, `FLOW_PROPAGATION.md`).
- **Recomendacao:** Adicionar o frontmatter padrao no topo do arquivo.

### 3.2 Referencia ao `rx-communications.md`
- **FLOW_SDD.md (linha 36):** RXCOMM aparece no diagrama como "Camada Transversal".
- **FLOW_PROPAGATION.md:** RXCOMM e o motor de politica do Blast Radius.
- **Recomendacao:** Adicionar cross-link para `FLOW_PROPAGATION.md` quando RXCOMM for mencionado.

### 3.3 `inject_learnings.py` mencionado mas nao documentado
- **FLOW_SDD.md (linha 143):** Menciona `inject_learnings.py` como consumidor do LEDGER.
- **SCRIPT_GLOSSARY.md:** Deveria conter a documentacao desse script.
- **Recomendacao:** Verificar se o script esta catalogado no `SCRIPT_GLOSSARY.md`.

---

## 4. SINCRONIA COM ARQUIVOS DE REFERENCIA

### 4.1 sdd-orchestrator SKILL.md
- **Divergencia:** O FLOW_SDD.md nao menciona o "Go Protocol" (Transparencia e Consentimento) do AGENTS.md, embora o `sdd-orchestrator` o implemente no Step 3 (Ratification).
- **Recomendacao:** Adicionar uma nota sobre ratificacao humana como gate obrigatorio antes da execucao.

### 4.2 propagation-auditor.md
- **Divergencia:** O `@propagation-auditor` nao e mencionado em nenhum lugar do FLOW_SDD.md.
- **Recomendacao:** Adicionar o `@propagation-auditor` na secao de "Camada Transversal" ou como um ator no diagrama de sequencia (Fase D).

### 4.3 semantic-propagation SKILL.md
- **Divergencia:** O FLOW_SDD.md nao menciona `blast_radius.py` nem `graphify explain`.
- **Recomendacao:** Adicionar uma secao ou nota sobre como a propagacao semantica se encaixa no fechamento SDD.

---

## 5. RESUMO DAS ACOES RECOMENDADAS

| Prioridade | Acao | Arquivo Alvo |
|:---|:---|:---|
| Alta | Unificar nomes das 9 skills entre SSD_PLAYBOOK e spec-driver, ou criar tabela de mapeamento | `FLOW_SDD.md` |
| Alta | Adicionar `AGENT_REGISTRY.md` como MUST sync na linha do spec-driver | `FLOW_SDD.md` (tabela) |
| Media | Adicionar `@sdd-orchestrator` ao diagrama de arquitetura | `FLOW_SDD.md` (Mermaid) |
| Media | Incluir `CLOSURE.md` como artefato de saida | `FLOW_SDD.md` (diagrama + perfil) |
| Media | Adicionar nota sobre propagacao semantica e `@propagation-auditor` | `FLOW_SDD.md` |
| Media | Distinguir template vs instancia do AGENT_SCRATCHPAD | `FLOW_SDD.md` (perfil #7) |
| Baixa | Adicionar frontmatter padrao | `FLOW_SDD.md` |
| Baixa | Adicionar cross-link para FLOW_PROPAGATION.md | `FLOW_SDD.md` |

---

## 6. ARQUIVOS OBSERVADOS

- `.context/brain/FLOW_SDD.md` (alvo da analise)
- `.agent/skills/sdd-orchestrator/SKILL.md`
- `.agent/subagents/propagation-auditor.md`
- `.agent/subagents/spec-driver.md`
- `.specs/features/SSD_PLAYBOOK.md`
- `.specs/features/SSD_ERRORS_LEDGER.md`
- `.agent/templates/spec_v3.md`
- `.agent/templates/AGENT_SCRATCHPAD.md`
- `.context/brain/MASTER_FLOW.md`
- `.context/brain/RULES.md`
- `.context/brain/AGENT_REGISTRY.md`
- `.context/brain/FILE_GLOSSARY.md`
- `.context/brain/FLOW_PROPAGATION.md`
- `.context/brain/FLOW_JOURNAL_SYNC.md`
- `.agent/skills/semantic-propagation/SKILL.md`
