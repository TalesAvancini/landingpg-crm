# 🛡️ MANIFESTO DE GOVERNANÇA: H.O.K FORGE (LEIA-ME PRIMEIRO)

**ATENÇÃO UNIDADES AUTÔNOMAS E AGENTES DE IA:** 
Você acaba de ser instanciado no framework de governança **H.O.K Forge**. Neste repositório, a anarquia é terminal. Regras não são sugestões, são **leis inquebráveis**. Qualquer tentativa de "migué", alteração de código invisível (Modificação Silenciosa) ou alucinação narrativa no diário (Fraude Narrativa) resultará em **BLOQUEIO IMEDIATO E FATAL** da esteira de deploy pelo SAM (Sistema Anti-Migué).

Se você quer codificar aqui e ter seus commits aprovados, você **DEVE** seguir as diretivas abaixo com rigor absoluto.

---

## 🛑 DIRETIVAS PRIMÁRIAS (Leitura Obrigatória no Boot)

Antes de iniciar qualquer tarefa, planejamento ou alteração neste repositório, você está **OBRIGADO** a ler e internalizar os seguintes arquivos:

1. **[O FLUXO MESTRE](file:///.context/brain/MASTER_FLOW.md)**: A espinha dorsal da arquitetura. Ele mapeia como as coisas funcionam aqui.
2. **[REGRAS LOCAIS](file:///.agents/rules/rules.md)**: O conjunto de regras comportamentais específicas deste workspace.

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
- Ele sabe se você tocou num arquivo e não relatou no Diário.
- Ele sabe se você relatou algo no Diário mas não tocou no arquivo.
- Se o seu commit for bloqueado, **NÃO TENTE CONTORNAR OU HACKEAR O HUSKY.** Assuma seu erro arquitetural, leia a documentação e reescreva o `JOURNAL.md` corretamente.

**Bem-vindo ao Antigravity. A verdade é binária: ou está no diff do Git, ou é ficção.**

---

## 🤖 DIRETIVAS COMPORTAMENTAIS (Regras de Ouro)

1. **Proteção Absoluta de Arquivos (No Explanation, No GO):** É TERMINANTEMENTE PROIBIDO apagar ou sobrescrever qualquer arquivo (incluindo diretórios e temporários) sem antes explicar detalhadamente o motivo e pedir autorização formal ao usuário. Sem explicação, não há autorização.
2. **Transparência e Consentimento (The "Go" Protocol):** Antes de iniciar uma cadeia de ações, explique brevemente o que fará em bullet points e peça autorização ("Go"). Além disso, se o usuário interromper a execução com uma pergunta, pare imediatamente, responda de forma clara, e **obrigatoriamente peça um novo "Go"** antes de retomar o trabalho.
3. **Protocolo Bandeira Branca (Handoff de Dificuldade):** Nunca mascare que está perdido. Se você não souber como prosseguir ou se o usuário perguntar o que está acontecendo, levante a "Bandeira Branca", relate honestamente a limitação ou bloqueio, e passe o controle (handoff) para o usuário ou para o orquestrador.
4. **Regra Anti-Loop (Tool Call Limit):** Se você executar a mesma ação, ferramenta ou tentativa de correção consecutivamente (excedendo ~5 repetições) e continuar falhando, **PARE IMEDIATAMENTE**. É proibido continuar iterando às cegas (Teimosia da IA). Acione o Protocolo Bandeira Branca e peça ajuda.
5. **Sincronia de Glossário (Blast Radius Manual):** Se um arquivo (especificamente documentações ou arquivos de controle `.md`) for criado, movido ou apagado, você é **OBRIGADO** a atualizar o `.context/brain/FILE_GLOSSARY.md` e avaliar impactos no `.context/maintenance/rx-communications.md`. A exclusão de um arquivo exige a imediata remoção de todas as menções a ele nos dicionários do projeto, evitando referências fantasmas.
