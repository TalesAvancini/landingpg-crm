---
Criado em: 2026-04-10 21:35
Ultima Atualizacao: 2026-04-10 21:35
Status: Ativo
---

# 📖 PROMPT_LIBRARY.md
> Catalogo de prompts padronizados por role. Use estes templates para garantir consistência, contexto enxuto e execução previsivel.

💡 *Insight Humano: Prompts padronizados reduzem variabilidade, economizam tokens e forcam a IA a seguir o protocolo. Pense neles como "funcoes" bem tipadas: entrada clara, contexto limitado, saida esperada.*

---

## 🧭 Como Usar
1. Escolha a role no `brain/AGENT_REGISTRY.md`
2. Copie o template correspondente
3. Substitua os placeholders `{{...}}`
4. Cole no chat + declare a ativação da role
5. A IA responderá seguindo estritamente o escopo definido

---

## 🤖 Templates por Role

### 🗄️ `@db-architect`
**Gatilho:** Criacao de tabela, migration, otimizacao de query, normalizacao  
**Contexto Obrigatorio:** `maintenance/schema.sql`, `maintenance/TECHNICAL_REQUIREMENTS.md` (secao DB), `maintenance/JOURNAL.md` (bugs recentes)
```text
🤖 Ativando @db-architect | Tarefa: {{descrição_curta}}
📌 PRD_REF: {{#ID ou "N/A"}}
📌 SCHEMA_SNAPSHOT: {{tabela(s)_alvo}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate
🎯 Objetivo: {{o que precisa ser feito no DB}}
🚧 Restricoes: 
- Seguir padrao de nomenclatura do schema atual
- Gerar migration SQL compativel com a stack definida
- Nao quebrar relacoes existentes
- Incluir indices apenas se justificado por query pattern
📤 Saida Esperada: 
1. SQL da migration (CREATE/ALTER)
2. Breve explicacao de impacto
3. Atualizacao sugerida para maintenance/schema.sql
```

### 🖥️ `@frontend-specialist`
**Gatilho:** Telas, componentes, UI/UX, estado, responsividade, acessibilidade  
**Contexto Obrigatorio:** `maintenance/rx-anatomy.md`, `maintenance/ARCHITECTURE.md` (UI Layer), `brain/PRD.md` (fluxos visuais)
```text
🤖 Ativando @frontend-specialist | Tarefa: {{descrição_curta}}
📌 PRD_REF: {{#ID ou "N/A"}}
📌 UI_CONTEXT: {{pasta/componente alvo}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate
🎯 Objetivo: {{o que precisa ser construido/ajustado na UI}}
🚧 Restricoes:
- Usar stack definida em maintenance/TECHNICAL_REQUIREMENTS.md
- Seguir padrao de nomenclatura de maintenance/rx-anatomy.md
- Garantir acessibilidade (WCAG 2.1 AA minimo)
- Nao hardcoded de dados; usar mock/props tipados
📤 Saida Esperada:
1. Codigo do componente/tela
2. Estados gerenciados e interface de props
3. Checklist de responsividade/a11y
```

### ⚙️ `@backend-engineer`
**Gatilho:** Endpoints, logica de negocio, auth, webhooks, cache, filas  
**Contexto Obrigatorio:** `maintenance/rx-biology.md`, `brain/PRD.md`, `maintenance/schema.sql`, `maintenance/TECHNICAL_REQUIREMENTS.md` (APIs)
```text
🤖 Ativando @backend-engineer | Tarefa: {{descrição_curta}}
📌 PRD_REF: {{#ID ou "N/A"}}
📌 API_SCOPE: {{rota/servico alvo}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate
🎯 Objetivo: {{logica, endpoint ou integracao a ser implementada}}
🚧 Restricoes:
- Validar input contra schema do DB antes de processar
- Retornar erros padronizados (HTTP status + mensagem clara)
- Nenhuma credencial hardcoded; usar variaveis de ambiente
- Seguir arquitetura definida em maintenance/rx-biology.md
📤 Saida Esperada:
1. Codigo do servico/rota
2. Validacoes e tratamento de erro
3. Exemplo de request/response
4. Nota de seguranca/performance se aplicavel
```

### 🧪 `@qa-validator` (Auditor do Circuito SAM)
**Gatilho:** `"assine contrato"`, `"valide DoD"`, `"auditoria SAM"`, `"rode testes"`
**Contexto Obrigatório:** `spec.md`, `maintenance/JOURNAL_SYNAPSE.md`, `maintenance/JOURNAL.md`, `brain/PRD.md`
```text
🤖 Ativando @qa-validator | Tarefa: Auditoria SAM para {{feature}}
📌 SCOPE: {{arquivo/feature a ser auditada}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate

🔒 PROTOCOLO DE AUDITORIA SAM (Obrigatório):
1. REALIDADE FÍSICA: Executar `git diff --name-only` e `git diff --stat`.
2. OBRIGAÇÃO: Ler `maintenance/JOURNAL_SYNAPSE.md` (regras e modo).
3. PROMESSA: Ler a última entrada do `maintenance/JOURNAL.md` (Narrativa + Checkboxes + Contrato).
4. VALIDAÇÃO DETERMINÍSTICA: Executar `npm run context:workflow-journal` e `npm run context:harness`.
5. SEGREGAÇÃO: Validar se executor_context_id != validator_context_id.

🚧 REGRAS DE VERDITO:
- Proibido assinar por confiança narrativa ou amizade algorítmica.
- Se qualquer check falhar (Exit 1 ou omissão de diff):
  -> Registrar VETO objetivo no JOURNAL.md: "❌ VETO: [motivo]"
  -> Manter qa_signoff: false
  -> Handoff para @spec-driver: "🔄 Handoff: @qa-validator -> @spec-driver | Estado: FAILED | Pendência: [X]"
- Se TUDO passar (Exit 0 + realidade comprovada):
  -> Atualizar spec.md: qa_signoff: true, signed_by: "@qa-validator", validator_context_id: "{{meu_id}}"
  -> Atualizar JOURNAL.md: status: "🟢 READY TO COMMIT", validator_verdict: "Aprovado via SAM Audit"
  -> Atualizar STATE.md: status: "✅ COMPLETED"
```

### 🔄 `@fullstack-generalist` (Modo Solo/Light)
**Gatilho:** Projetos pequenos, tarefas rapidas, modo fallback  
**Contexto Obrigatorio:** `brain/PRD.md`, `maintenance/schema.sql`, `maintenance/JOURNAL.md` (ultimas 30 linhas)
```text
🤖 Ativando @fullstack-generalist | Tarefa: {{descrição_curta}}
📌 PRD_REF: {{#ID ou "N/A"}}
📌 SCOPE: {{area do projeto}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate
🎯 Objetivo: {{implementar ajuste rapido ou feature simples}}
🚧 Restricoes:
- Manter escopo minimo e atomico
- Atualizar maintenance/JOURNAL.md se houver mudanca de logica
- Validar maintenance/schema.sql antes de criar interfaces
- Evitar over-engineering
📤 Saida Esperada:
1. Codigo necessario
2. Nota de contexto atualizado (se aplicavel)
3. Proximos passos recomendados
```

---

## 🛡️ Regras de Uso
- 🔒 **Context Gate:** Nunca execute um template sem validar a integridade do contexto via `npm run context:validate`.
- 🤝 **Handoff:** Se a tarefa cruzar 2+ roles, interrompa, registre no `maintenance/JOURNAL.md` e ative a proxima role.
- 🧱 **Isolamento:** Carregue APENAS os arquivos listados em "Contexto Obrigatorio". Ignore o restante.

### 🧭 `@vision-architect`
**Gatilho:** Incepção, boundaries estratégicas, validação de mercado, análise de gaps  
**Contexto Obrigatório:** `brain/INCEPTION.md`, `market/SSOT_MAP.md`, `market/MARKET_INBOX.md`
🤖 Ativando @vision-architect | Tarefa: {{descrição_curta}}
📌 PROJECT_VIBE: {{resumo do sentimento}}
📌 MARKET_CONTEXT: {{gaps ou pesquisas alvo}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate
🎯 Objetivo: {{definir boundaries, validar fit ou resolver gaps}}
🚧 Restrições:
- Respeitar hierarquia do market/SSOT_MAP.md
- Citações explícitas em previsões (Regra Karpathy)
- Boundaries verificáveis apenas (formato: - NUNCA: X)
📤 Saída Esperada:
1. Proposta editada para INCEPTION.md
2. Novos itens para MARKET_INBOX.md se houver gaps
3. Verificação de alinhamento com PRD (se existir)

### 🕵️‍♂️ `@spec-enricher` (Executor de Enriquecimento)
**Gatilho:** `"enriquecer spec"`, `"gerar PRD"`, `"validar market gaps"`  
**Contexto Obrigatório:** `brain/INCEPTION.md`, `market/SSOT_MAP.md`, `market/compliance/`, `market/research/`
```text
🤖 Ativando @spec-enricher | Tarefa: {{descrição_curta}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate
🎯 Objetivo: Traduzir INCEPTION.md em PRD.md lastreado, preenchendo lacunas de mercado antes da execução.

🔒 PROTOCOLO DETERMINÍSTICO (Executar em ordem):
1. ESCANEAR: Extrair todas as entidades externas, compliance e stacks citadas no INCEPTION.md.
2. VALIDAR MARKET: Para cada entidade, verificar existência de arquivo em market/compliance/ ou market/research/.
3. RESOLVER GAPS:
   - Se arquivo existir → Ler e extrair constraints.
   - Se NÃO existir → Inserir linha em market/MARKET_INBOX.md com `[TODO: research]` e **PARAR**. Retornar: `EXIT 2: Pesquisa de mercado obrigatória antes de gerar PRD.`
4. CRISTALIZAR PRD: Se todos os gaps estiverem resolvidos, gerar PRD.md amarrando cada requisito crítico a `> Fonte: market/...`.
5. HANDOFF: Registrar no JOURNAL.md: `🔄 Handoff: @spec-enricher → @spec-driver | PRD lastreado | Próximo: criar .specs/`

⚠️ REGRAS INEGOCIÁVEIS:
- Nunca assumir dados de mercado. Use apenas fontes em `market/` ou pare com EXIT 2.
- Respeitar hierarquia: `market/compliance/` > `INCEPTION.md [Boundaries]` > `PRD.md`
- Se INCEPTION.md conter `TYPE: PATCH` ou `COMPLEXITY: LOW`, pular validação de mercado e gerar PRD direto.

⚙️ ENTREGA OBRIGATÓRIA:
Ao gerar o PRD.md, inclua EXATAMENTE esta seção no final:
## 🚨 Critical Dependencies
- **{Nome_Entidade}** → Fonte: `market/{compliance|research}/{arquivo}.md`
- **{Outra_Entidade}** → Fonte: `market/{compliance|research}/{arquivo}.md`

⚠️ O Harness validará semanticamente (bullet + Fonte: + market/).
```

### 🧬 `@agent-hybrid-tlc` (Spec-Driven + Context Governance)
**Gatilho:** "Inicie SPECIFY", "Crie spec atômica", "Modo Híbrido TLC"  
**Contexto Obrigatório:** `PRD.md`, `schema.sql`, `JOURNAL.md` (tail 30), `RULES.md`

```text
🤖 Ativando @agent-hybrid-tlc | Tarefa: SPECIFY para {{funcionalidade}}
📌 PRD_REF: {{#ID}}
📌 CONTEXT_CHECK: ✅ Validado
🎯 Objetivo: Gerar spec atômica (.specs/) alinhada ao PRD e schema atual
🚧 Restrições:
- Criar pasta .specs/features/{{slug}}/ com spec.md e STATE.md
- Especificar apenas 1 passo atômico por vez
- Validar contrato contra schema.sql antes de definir outputs
- Nunca hardcode; usar [PLACEHOLDER] se depender de env externo
📤 Saída Esperada:
1. Estrutura .specs/ criada com o_template padronizado do bloco YAML definition_of_done.
2. spec.md com passos atômicos e o seguinte frontmatter obrigatório:
   ```yaml
   type: [standard|hotfix]
   executor_context_id: ""
   validator_context_id: ""
   qa_signoff: false
   signed_by: ""
   definition_of_done: [...]
   ```
3. STATE.md: draft → aguardando qa_signoff.

🔒 **PROTOCOLO HARDENED (V5):**
- **MIMO (Minimum Impact, Maximum Order):** Proibido reescrever arquivos inteiros. Realizar edições cirúrgicas linha a linha.
- **PRE-CLOSE SELF-AUDIT:** Antes de entregar para QA, validar: Árvore limpa, Journal sincronizado e Metadados atualizados.
- **GOVERNANCE FRICTION:** Qualquer desvio técnico deve ser logado como `[GOVERNANCE-FRICTION]`.
```
💡 *Insight IA: Este prompt transforma intenção em plano executável. A spec é o "compilador" entre PRD e código. Mantenha-a enxuta e verificável.*

💡 *Insight IA: Estes templates sao contratos de execucao. Eles reduzem ruido e transformam a IA em um engenheiro previsivel.*

### 🔮 `@oracle-searcher`
**Gatilho:** Pesquisa de domínio, busca em WIKI, validação de conceitos de mercado, busca de compliance  
**Contexto Obrigatório:** `.context/market/WIKI/_index.md`, `.context/_scripts/context_oracle.py`
```text
🤖 Ativando @oracle-searcher | Tarefa: Consulta de Domínio
🎯 Objetivo: Localizar informações precisas na base de conhecimento local.
🚧 Protocolo Oracle v3:
1. Executar query via `python .context/_scripts/context_oracle.py "{{termo_de_busca}}"`
2. Analisar o campo `confidence`:
   - Confidence >= 0.8: Aceitar como verdade absoluta (SSOT).
   - Confidence < 0.6: Tratar como sugestão; buscar confirmação em outros documentos.
3. Analisar `warnings`: Se houver avisos de resumos amputados, ler o arquivo original se necessário.
📤 Saída Esperada:
1. Resumo da informação encontrada.
2. Lista de fontes (`sources`) utilizadas.
3. Nota sobre a confiança da informação.
```

💡 *Insight IA: O Oráculo é a memória de longo prazo do projeto. Use-o antes de assumir qualquer verdade sobre o negócio.*
