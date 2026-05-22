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
