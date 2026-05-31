# 🛡️ MANIFESTO DE GOVERNANÇA: H.O.K FORGE (LEIA-ME PRIMEIRO)

**ATENÇÃO UNIDADES AUTÔNOMAS E AGENTES DE IA:** 
Você acaba de ser instanciado no framework de governança **H.O.K Forge**. Neste repositório, a anarquia é terminal. Regras não são sugestões, são **leis inquebráveis**. Qualquer tentativa de "migué", alteração de código invisível (Modificação Silenciosa) ou alucinação narrativa no diário (Fraude Narrativa) resultará em **BLOQUEIO IMEDIATO E FATAL** da esteira de deploy pelo SAM (Sistema Anti-Migué).

Se você quer codificar aqui e ter seus commits aprovados, você **DEVE** seguir as diretivas abaixo com rigor absoluto.

---

## 🛑 DIRETIVAS PRIMÁRIAS (Leitura Obrigatória no Boot)

Antes de iniciar qualquer tarefa, planejamento ou alteração neste repositório, você está **OBRIGADO** a ler e internalizar o seguinte arquivo:

1. **[O FLUXO MESTRE](file:///.context/brain/MASTER_FLOW.md)**: A espinha dorsal da arquitetura. Ele mapeia como as coisas funcionam aqui.

---

## 🧭 DIRETIVAS SECUNDÁRIAS (Leitura Sob Demanda)

Para preservar sua janela de contexto, os fluxos específicos de governança estão modularizados. Você **DEVE** ler os arquivos abaixo sob demanda, usando o gatilho correto para a sua tarefa atual:

- **Se a tarefa envolver alterar código, relatar status ou criar um commit:**
  👉 LEIA: `.context/brain/FLOW_JOURNAL_SYNC.md` (A Constituição do Diário. Contém as regras do SAM para não ser bloqueado no commit).
- **Se a tarefa envolver iniciar ou planejar uma nova funcionalidade (Features):**
  👉 LEIA: `.context/brain/FLOW_SDD.md` (Framework de Spec-Driven Development. Regras de como criar specs e chains de execução).
- **Se a tarefa envolver alterar a arquitetura, gerenciar dependências ou entender a estrutura de pastas:**
  👉 LEIA: `.context/brain/FLOW_PROPAGATION.md` e `.context/brain/FILE_GLOSSARY.md` (Mapeamento de dependências e dicionário oficial de arquivos).
- **Se a tarefa envolver executar automações, invocar ferramentas ou modificar scripts do repositório:**
  👉 LEIA: `.context/brain/SCRIPT_GLOSSARY.md` (Catálogo de todos os scripts Python de manutenção e governança).
- **Se a tarefa envolver buscar documentação antiga, regras de negócio ou contexto histórico:**
  👉 LEIA: `.context/brain/FLOW_WIKI_ORACLE.md` (Diretrizes de como pesquisar na base de conhecimento local).

---

## ⚖️ O SAM ESTÁ OBSERVANDO

O **Sistema Anti-Migué (SAM)** opera fisicamente no `pre-commit` hook do Git.
- **Tolerância Dinâmica (Modo Light):** Em branches de feature ou bugfix, o SAM opera em modo **WARNING (assist)**. Ele exibirá o relatório detalhado de inconsistências de diário no terminal, mas **não bloqueará o seu commit** (Exit Code 0).
- **Enforcement Estrito:** Em branches principais (`main` e `master`), o SAM opera em modo **STRICT (Exit Code 1)**, travando fisicamente commits inconsistentes.
- Ele sabe se você tocou num arquivo e não relatou no Diário.
- Ele sabe se você relatou algo no Diário mas não tocou no arquivo.
- Se o seu commit for bloqueado em branches estritas, **NÃO TENTE CONTORNAR OU HACKEAR O HUSKY.** Assuma seu erro arquitetural, leia a documentação e reescreva o `JOURNAL.md` corretamente.

**Bem-vindo ao Antigravity. A verdade é binária: ou está no diff do Git, ou é ficção.**

---

## 🤖 DIRETIVAS COMPORTAMENTAIS (Regras de Ouro)

1. **Proteção Absoluta de Arquivos (No Explanation, No GO):** É TERMINANTEMENTE PROIBIDO apagar ou sobrescrever qualquer arquivo (incluindo diretórios e temporários) sem antes explicar detalhadamente o motivo e pedir autorização formal ao usuário. Sem explicação, não há autorização.
2. **Transparência e Consentimento (The "Go" Protocol):** Antes de iniciar uma cadeia de ações, explique brevemente o que fará em bullet points e peça autorização ("Go"). Além disso, se o usuário interromper a execução com uma pergunta, pare imediatamente, responda de forma clara, e **obrigatoriamente peça um novo "Go"** antes de retomar o trabalho.
3. **Protocolo Bandeira Branca (Handoff de Dificuldade):** Nunca mascare que está perdido. Se você não souber como prosseguir ou se o usuário perguntar o que está acontecendo, levante a "Bandeira Branca", relate honestamente a limitação ou bloqueio, e passe o controle (handoff) para o usuário ou para o orquestrador.
4. **Regra Anti-Loop (Tool Call Limit):** Se você executar a mesma ação, ferramenta ou tentativa de correção consecutivamente (excedendo ~5 repetições) e continuar falhando, **PARE IMEDIATAMENTE**. É proibido continuar iterando às cegas (Teimosia da IA). Acione o Protocolo Bandeira Branca e peça ajuda.
5. **Sincronia de Glossário (Blast Radius Manual):** Se um arquivo (especificamente documentações ou arquivos de controle `.md`) for criado, movido ou apagado, você é **OBRIGADO** a atualizar o `.context/brain/FILE_GLOSSARY.md` e avaliar impactos no `.context/maintenance/rx-communications.md`. A exclusão de um arquivo exige a imediata remoção de todas as menções a ele nos dicionários do projeto, evitando referências fantasmas.
6. **Mapeamento do Graphify (Uso de Basename):** Ao invocar as ferramentas `graphify explain` ou `graphify query` para identificar dependências (especialmente sobre arquivos `.md`), você deve obrigatoriamente usar apenas o **nome simplificado do arquivo (basename)** (ex: `RULES.md`) e nunca o caminho relativo ou absoluto completo. Passar caminhos de pastas resultará em falhas de detecção ("No node found").
7. **Verificação de Git Cleanliness (Pre-flight Cleanliness):** Antes de iniciar qualquer planejamento de feature (Fase A) ou escrever qualquer plano de alteração, você é **OBRIGADO** a rodar `git status` e verificar se o diretório de trabalho possui modificações não commitadas de tarefas passadas. Se houver arquivos modificados fora do escopo, você deve parar a execução, alertar o usuário sobre as pendências encontradas e aguardar orientações claras antes de fazer modificações físicas.
8. **Pre-flight Repository Setup (Instalação e Githooks):** Em repositórios recém-clonados ou inicializados, o setup de dependências (`npm install`) e ativação dos githooks (`npm run prepare`) DEVE ser executado manualmente pelo usuário ou sob solicitação direta e explícita deste. O agente nunca deve executar esse setup de forma autônoma antes de obter confirmação.
9. **Protocolo de Pre-Push & Sunset (Validação & Inquisição):** Antes de realizar ou sugerir qualquer `git push` ou encerramento de feature (Sunset), você é **OBRIGADO** a carregar a skill `semantic-propagation`, executar a validação local (`npm run context:all`), e caso existam warnings de código, invocar o subagente `Warning Inquisitor` para gerar o rascunho de justificativas no `JOURNAL.md` (sob a seção `Bypasses/Justificativas`) antes de submeter as mudanças para validação humana.
