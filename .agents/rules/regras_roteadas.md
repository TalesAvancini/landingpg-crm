# 🛸 Roteador de Regras (Antigravity Kit)
> **Este é o único ponto de entrada de regras ativas na IDE.**
> Ele despacha a leitura das regras específicas sob demanda (lazy loading) via links absolutos.

Antes de prosseguir com qualquer ação de escrita, commit ou alteração no repositório, avalie as condições abaixo. Se alguma condição for verdadeira, você **DEVE** carregar a regra correspondente usando a ferramenta `view_file`:

## 📋 Regras Condicionais

### 1. Modelo de Linguagem Flash (Velocidade & Sync)
* **Condição:** Se você é o **Gemini Flash** (ou qualquer modelo focado em velocidade sobre raciocínio profundo).
* **Ação:** Leia a regra de sincronização de journal:
  -> [flash-journal-sync-guard.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inicío_de_projeto/.agent/rules_pool/flash-journal-sync-guard.md)

### 2. Sobriedade Operacional (Anti-Overengineering)
* **Condição:** Se você é o **Gemini Flash** ou se a tarefa exige foco estrito e minimalismo.
* **Ação:** Leia a regra de sobriedade e conformidade de versão:
  -> [sobriedade-operacional.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inicío_de_projeto/.agent/rules_pool/sobriedade-operacional.md)

### 3. Função de Orquestrador SDD
* **Condição:** Se você está na função de **Orquestrador SDD** (planejando uma feature, injetando raw payloads em `.specs/`, rotacionando agentes no `AGENT_REGISTRY.md` ou autorizando fechamento de sprint).
* **Ação:** Leia a regra de conduta do Orquestrador:
  -> [orquestrador.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inicío_de_projeto/.agent/rules_pool/orquestrador.md)

### 4. Contratos de Sprint, Commits e Sincronia de Journal
* **Condição:** Se a tarefa envolver fechamento de sprints/ondas, escrita de logs no `JOURNAL.md`, commits no Git, preenchimento de checklists ou gerenciamento de tarefas em `tasks.md`.
* **Ação:** Leia as seções de contrato, sincronização e fechamento:
  -> [RULES.md#L42-L98](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inicío_de_projeto/.context/brain/RULES.md#L42-L98)

### 5. Alteração de Código Fonte e Controle de Escrita
* **Condição:** Se a tarefa exigir alteração em arquivos de código fonte, modificação de interfaces/contratos, ou se a árvore estiver bloqueada com status `[BLOCKED]` ou `[FATAL]`.
* **Ação:** Leia as seções de limites de impacto (Pre-flight) e controle de escrita mecânica:
  -> [RULES.md#L56-L63](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inicío_de_projeto/.context/brain/RULES.md#L56-L63) e [RULES.md#L99-L124](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inicío_de_projeto/.context/brain/RULES.md#L99-L124)

### 6. Banco de Dados e Prevenção de Duplicidades (Monolith & Components)
* **Condição:** Se a tarefa envolver alterações em bancos de dados (schema), componentes dependentes de dados, ou criação de novas funções, componentes de UI, utilitários ou classes.
* **Ação:** Leia a seção de governança de arquitetura e schema:
  -> [RULES.md#L161-L168](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inicío_de_projeto/.context/brain/RULES.md#L161-L168)

### 7. Ingestão de Conhecimento e Karpathy Guard
* **Condição:** Se você estiver criando ou destilando artigos de conhecimento na pasta da WIKI (`market/WIKI/` ou `market/RAW/`).
* **Ação:** Leia as regras de estratificação de densidade e linter Karpathy:
  -> [RULES.md#L202-L212](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inicío_de_projeto/.context/brain/RULES.md#L202-L212)

### 8. Perguntas sobre Código e Arquitetura (Graphify)
* **Condição:** Se você precisar responder a perguntas complexas sobre a arquitetura do projeto, fluxo de chamadas ou dependências, e a pasta `graphify-out/` contiver o grafo.
* **Ação:** Leia as diretrizes de consulta ao Grafo de Conhecimento do Graphify:
  -> [graphify.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inicío_de_projeto/.agent/rules_pool/graphify.md)

---
*Nota: Este arquivo foi consolidado para otimização de tokens (evitando carregar múltiplos blocos de regras grandes a cada turno na thread principal).*
