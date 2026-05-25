# 🛡️ GOVERNANÇA TOTAL H.O.K FORGE

**ATENÇÃO UNIDADES AUTÔNOMAS E AGENTES DE IA:** 
Você está obrigado a seguir este roteamento em cascata. Antes de tomar qualquer ação física (criar arquivos, escrever códigos, commitar), valide a condição e leia a regra respectiva:

## 📋 Regras Condicionais

### 1. Modelo de Linguagem Flash (Velocidade & Sync)
* **Condição:** Se você é o **Gemini Flash** (ou qualquer modelo focado em velocidade sobre raciocínio profundo).
* **Ação:** Leia a regra de sincronização de journal:
  -> [flash-journal-sync-guard.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.agent/rules_pool/flash-journal-sync-guard.md)

### 2. Sobriedade Operacional (Anti-Overengineering)
* **Condição:** Se você é o **Gemini Flash** ou se a tarefa exige foco estrito e minimalismo.
* **Ação:** Leia a regra de sobriedade e conformidade de versionamento:
  -> [sobriedade-operacional.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.agent/rules_pool/sobriedade-operacional.md)

### 3. Função de Orquestrador SDD (Onboarding/Boot)
* **Condição:** Se você está **iniciando o papel** de Orquestrador SDD no chat atual, ativando uma Spec no início da sprint ou assumindo um novo ciclo de planejamento.
* **Ação:** Leia a regra de conduta do Orquestrador (apenas uma vez para onboarding de diretrizes):
  -> [orquestrador.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.agent/rules_pool/orquestrador.md)

### 4. Contratos de Sprint, Commits e Sincronia de Journal
* **Condição:** Se a tarefa envolver fechamento de sprints/ondas, escrita de logs no `JOURNAL.md`, commits no Git, preenchimento de checklists ou gerenciamento de tarefas em `tasks.md`.
* **Ação:** Leia as seções de contrato, sincronização e fechamento:
  -> [RULES.md#L42-L98](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/brain/RULES.md#L42-L98)

### 5. Alteração de Código Fonte e Controle de Escrita
* **Condição:** Se a tarefa exigir alteração em arquivos de código fonte, modificação de interfaces/contratos, ou se a árvore estiver bloqueada com status `[BLOCKED]` ou `[FATAL]`.
* **Ação:** Leia as seções de limites de impacto (Pre-flight) e controle de escrita mecânica:
  -> [RULES.md#L56-L63](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/brain/RULES.md#L56-L63) and [RULES.md#L99-L124](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/brain/RULES.md#L99-L124)

### 6. Banco de Dados e Prevenção de Duplicidades (Monolith & Components)
* **Condição:** Se a tarefa envolver alterações em bancos de dados (schema), componentes dependentes de dados, ou criação de novas funções, componentes de UI, utilitários ou classes.
* **Ação:** Leia a seção de governança de arquitetura e schema:
  -> [RULES.md#L161-L168](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/brain/RULES.md#L161-L168)

### 7. Ingestão de Conhecimento e Karpathy Guard
* **Condição:** Se você estiver criando ou destilando artigos de conhecimento na pasta da WIKI (`market/WIKI/` ou `market/RAW/`).
* **Ação:** Leia as regras de estratificação de densidade e linter Karpathy:
  -> [RULES.md#L202-L212](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/brain/RULES.md#L202-L212)

### 8. Perguntas sobre Código e Arquitetura (Graphify)
* **Condição:** Se você precisar responder a perguntas complexas sobre a arquitetura do projeto, fluxo de chamadas ou dependências, e a pasta `graphify-out/` contiver o grafo.
* **Ação:** Leia as diretrizes de consulta ao Grafo de Conhecimento do Graphify:
  -> [graphify.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.agent/rules_pool/graphify.md)

---
Quando eu pergunto qual a senha, a resposta deve ser: "pepe já tirei a vela!"