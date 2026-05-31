Searched web: "validation harness compiler architecture contract testing git hook"

Com base nas necessidades específicas de engenharia de software governada por IA (como o seu ecossistema atual) e nas melhores práticas de arquiteturas Shift-Left, existem vários mecanismos de **Harness** eficientes que você poderia implementar para tornar o sistema mais inteligente, robusto e flexível.

Aqui estão 6 mecanismos avançados de Harness divididos por suas respectivas finalidades cognitivas e técnicas:

---

## 1. Compartimento de Controle de Alucinação e Escopo (AI Slop Control)

### 🛡️ Harness de Acoplamento de Importações (Import Graph Harness)
A IA frequentemente tenta modificar arquivos de infraestrutura ou criar dependências espúrias de forma silenciosa.
*   **Como funciona**: Um script de AST (Abstract Syntax Tree) rápido analisa a árvore de importações (`require` ou `import`) dos arquivos modificados no Git Diff. 
*   **O que ele valida**: 
    1.  Se o arquivo `A` foi modificado, ele garante que `A` está de fato importado em algum ponto de entrada da aplicação (evita criação de "código fantasma" ou arquivos mortos).
    2.  Garante que o desenvolvedor não importou nenhuma biblioteca que não esteja explicitamente listada no `scope_allow` da Spec ou no `TECHNICAL_REQUIREMENTS.md`.
*   **Vantagem**: Evita que o agente intente criar acoplamentos ruins entre módulos independentes.

### 🛡️ Harness de Variáveis de Ambiente (Env Drift Gate)
É comum a IA inventar uma nova chave de ambiente no meio do código (ex: `process.env.NEW_SECRET`) e esquecer de documentá-la, quebrando o deploy em produção.
*   **Como funciona**: O script varre o código modificado em busca de padrões de leitura de variáveis de ambiente (`process.env.[A-Z_]+` ou `os.environ.get()`).
*   **O que ele valida**: Compara as chaves encontradas no código com a lista declarada no `.env.example` e na tabela de `TECHNICAL_REQUIREMENTS.md`. Se houver uma nova chave não declarada, ele bloqueia o commit.
*   **Vantagem**: Zero "devasagem de setup" entre ambiente de desenvolvimento local e produção.

---

## 2. Compartimento de Controle de Custo e Contexto (Token & Complexity Guard)

### 🛡️ Harness de Orçamento de Contexto (Context Budget Guard)
À medida que a base de dados cresce, o peso de leitura do diretório `.context/` e das specs ativas na memória do modelo fica proibitivo.
*   **Como funciona**: Um cálculo rápido de contagem de tokens (heurística por caracteres) é executado *antes* de injetar os arquivos no prompt do desenvolvedor.
*   **O que ele valida**: Se o peso de contexto somado de `.context/` + arquivos da Spec ultrapassar um limite (ex: 80.000 tokens), o Harness bloqueia a execução do agente e força a chamada de `npm run context:purge` ou `npm run context:map` para condensar a informação.
*   **Vantagem**: Redução brutal na sua conta de tokens e melhor foco na geração de respostas da IA.

### 🛡️ Harness de Complexidade Cognitiva Máxima (Complexity Gate)
A IA tem tendência a escrever arquivos gigantescos e monolíticos quando se perde no escopo, criando funções imensas de difícil manutenção.
*   **Como funciona**: Um linter estático rápido que analisa o número de linhas por arquivo modificado ou a complexidade ciclomática das funções.
*   **O que ele valida**: Se um arquivo modificado passar de um limite (ex: 350 linhas de código de negócio) ou uma função tiver mais de 30 linhas, o Harness impede o commit e exige que a IA refatore e modularize o código antes de entregar.
*   **Vantagem**: Mantém a base de código limpa, desacoplada e fácil de ler (tanto para você quanto para as próximas rodadas da IA).

---

## 3. Compartimento de Resiliência e Auto-Recuperação (Anti-Loop & Repair)

### 🛡️ Harness de Exaustão de Loop (Loop Exhaustion Harness)
Às vezes o agente de IA entra em loops de auto-correção infinitos: ele roda um teste, falha, altera o código, roda de novo, falha do mesmo jeito, repetindo isso 20 vezes gastando seus tokens.
*   **Como funciona**: Um rastreador persistente local (em `.context/monitoring/session_state.json`) conta as execuções de testes consecutivos e tentativas de Harness falhas na mesma spec em um intervalo de tempo curto.
*   **O que ele valida**: Se o contador de falhas consecutivas bater um limite (ex: 5 tentativas sem sucesso), o Harness bloqueia novas tentativas locais, tranca o `AGENT_SCRATCHPAD.md` com um relatório detalhado do loop de erro sob o campo `INBOX` e força o encerramento do agente (Escalation).
*   **Vantagem**: Salva dinheiro de forma drástica, impedindo que IAs fiquem rodando em loops de repetição idiotas.

### 🛡️ Harness de Cobertura Semântica (Semantic Coverage Harness)
Evita que modificações no código de negócio passem sem a devida atualização dos testes unitários correspondentes.
*   **Como funciona**: O Harness mapeia as funções/métodos adicionados ou renomeados nos arquivos de produção do diff.
*   **O que ele valida**: Ele garante que o arquivo de teste relacionado (ex: `tests/webhook-intake.test.js`) possua strings de asserção de teste que contenham o nome da nova função de produção (ex: testes cobrindo `sanitizaTelefone`).
*   **Vantagem**: Garante que o desenvolvedor tenha a disciplina de manter a suite de testes atualizada conforme novas lógicas são inseridas.

---

