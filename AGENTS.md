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

Para preservar sua janela de contexto, os fluxos específicos de governança estão modularizados. Você **DEVE** ler os arquivos abaixo sob demanda, dependendo da tarefa que for executar:

- **Vai modificar arquivos, atualizar o status ou realizar um commit?**
  👉 LEIA: `.context/brain/FLOW_JOURNAL_SYNC.md` (A Constituição do Diário. Errar aqui é bloqueio na certa).
- **Vai criar uma nova funcionalidade do zero?**
  👉 LEIA: `.context/brain/FLOW_SDD.md` (Spec-Driven Development).
- **A tarefa envolve dependências ou afeta a arquitetura?**
  👉 LEIA: `.context/brain/FLOW_PROPAGATION.md` e o `FILE_GLOSSARY.md`.
- **Precisa buscar documentação ou contexto histórico do projeto?**
  👉 LEIA: `.context/brain/FLOW_WIKI_ORACLE.md`.

---

## ⚖️ O SAM ESTÁ OBSERVANDO

O **Sistema Anti-Migué (SAM)** opera fisicamente no `pre-commit` hook do Git.
- Ele sabe se você tocou num arquivo e não relatou no Diário.
- Ele sabe se você relatou algo no Diário mas não tocou no arquivo.
- Se o seu commit for bloqueado, **NÃO TENTE CONTORNAR OU HACKEAR O HUSKY.** Assuma seu erro arquitetural, leia a documentação e reescreva o `JOURNAL.md` corretamente.

**Bem-vindo ao Antigravity. A verdade é binária: ou está no diff do Git, ou é ficção.**
