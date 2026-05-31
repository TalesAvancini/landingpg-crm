<!-- SSOT -->
# 📜 A Constituição do Journal: Flow, Governança e Meandros (H.O.K Forge)

> **⚠️ AVISO AOS AGENTES E HUMANOS:** 
> Se você errou o Journal duas vezes e tomou bloqueio consecutivo do pipeline (SAM FATAL ERROR), **PARE O QUE ESTÁ FAZENDO E ESTUDE ESTE DOCUMENTO.** O pipeline não é quebrado, ele é intolerante a migués.

O `JOURNAL.md` é o **coração epistemológico** do projeto. Ele não é apenas um log de texto; ele é um contrato legal auditado criptograficamente contra o Git. Este documento é a visão "Ultra-Completa" (A Constituição) de como esse ecossistema funciona.

---

## 🧭 1. A Mecânica do Journal (O Diário de Bordo)

O Journal opera sob regras não-negociáveis para evitar a saturação de contexto do LLM e manter a rastreabilidade da governança.

### 1.1 Ordem Cronológica Reversa
Ao contrário de logs tradicionais, o `JOURNAL.md` **sempre cresce para cima**.
- A entrada mais recente é SEMPRE a primeira do arquivo (logo abaixo do cabeçalho).
- Isso garante que o agente/LLM que estiver lendo o arquivo veja primeiro o contexto mais quente e atual, sem precisar ler 600 linhas de histórico antigo.

### 1.2 O Limite Heurístico e o `purge_journal.py`
Para impedir que o contexto estoure, o arquivo tem um limite estrito (ex: 600 linhas).
- Quando o limite é violado, o script `.context/_scripts/purge_journal.py` é acionado.
- **A Lógica de Poda:** Como a ordem é reversa, o script corta a "base" do arquivo. Ele **arquiva os 70% mais antigos** e preserva intactos os 30% do topo (as entradas mais recentes).
- O arquivo morto recebe um timestamp e é jogado em `.context/maintenance/_archive_context/journals/`.

### 1.3 Anatomia de uma Entrada Perfeita
Toda entrada criada deve seguir este exato formato Markdown. Um erro de sintaxe aqui causará a ira do SAM.

```markdown
## 📅 2026-05-22 14:55 | 🛠️ Feat: Título Breve #Tag1 #Tag2
**Estado Atual:**
- [x] O que foi feito (em linguagem natural).
- [x] O porquê foi feito.

**Matriz de Propagação:**
- [x] caminho/absoluto/do/arquivo.py -> [Motivo da alteração]
- [x] outro/arquivo.md -> [Motivo]

executor_context_id: nome-do-agente-que-codou
validator_context_id: nome-do-agente-auditor
status: READY TO COMMIT
```
*(Importante: Os três últimos campos devem ser texto puro, sem formatação markdown `**`).*

---

## 🤖 2. SAM (Auditoria Anti-Migué) e a Regra do Jogo

O **SAM** (`workflow_journal_auditor.py`) atua como o promotor de justiça no hook de `pre-commit` do Husky. Se ele disser não, o commit morre. Ele audita o `JOURNAL.md` lendo a **primeira entrada** (a mais recente) e comparando com o output do `git status --porcelain`.

### 2.1 Tolerância Dinâmica (Modos de Operação)
O SAM possui dois modos de execução baseados na branch git atual:
- **Modo ASSIST (WARNING - Feature Branches):** Se a branch ativa for uma branch de feature ou bugfix (diferente de `main` e `master`), o SAM aponta todas as violações de diário de forma pedagógica, mas retorna exit code `0`, permitindo o commit local rápido para incentivar o desenvolvimento sem fricção.
- **Modo STRICT (LOCK - Branches Estritas):** Se a branch atual for `main` ou `master`, o SAM falha com exit code `1`, exigindo 100% de consistência antes do merge/push.

### 2.2 As 4 Leis Absolutas
Ele implementa 4 leis:

#### Lei 1: O Contrato Deve Ser Assinado
- Falha se faltar `executor_context_id` ou `validator_context_id`.
- Falha se o status não contiver `READY TO COMMIT` ou `🟢`.

#### Lei 2: Segregação de Deveres (Conflito de Interesse)
- Falha se `executor_context_id == validator_context_id`. Quem programa não pode assinar a própria QA.

#### Lei 3: Proibição de Fraude Narrativa
- **O Crime:** O agente escreve na Matriz de Propagação que alterou o arquivo `X`, mas o `git status` mostra que `X` não foi tocado. (Mentiu no diário).
- **A Punição:** Bloqueio do pipeline.

#### Lei 4: Proibição de Modificação Silenciosa
- **O Crime:** O `git status` acusa que o arquivo `Y` foi modificado, mas o agente "esqueceu" de listá-lo na Matriz de Propagação do Journal. (Tentou contrabandear código).
- **A Punição:** Bloqueio do pipeline.

---

## 🛡️ 3. O "Catch-22" e as Zonas de Imunidade

Se o SAM é tão estrito, como lidamos com scripts que geram arquivos automaticamente (como relatórios de saúde) ou com arquivos mortos que o Git nem olha? Nós usamos o conceito de **Imunidade**.

### 3.1 Zonas Ignoradas (`IGNORED_PREFIXES`)
- **Problema:** Se um agente diz que arquivou um arquivo jogando-o na pasta `.context/maintenance/_archive_context/`, o Git não vai trackear (pois está no `.gitignore`). O SAM gritaria "Fraude Narrativa!" porque o arquivo não está no diff.
- **Solução:** O SAM perdoa Fraude Narrativa se o caminho começar com `planos/`, `scratch/`, `temp/`, `.agents/`, ou `_archive_context/`. Você pode listar essas alterações no Journal sem medo.

### 3.2 Os Shadow Files (`SHADOW_FILES`)
- **Problema:** Quando você comita, o pipeline roda o `sync_project.py` ou o `harness_runner.py`, que geram ou modificam arquivos automáticos (ex: `CONTEXT_HEALTH.md`, `PROJECT_INDEX_01.md`, `LEARNINGS.md`). Como esses arquivos mudam *no meio* do pipeline, eles entram no Git Diff. O SAM gritaria "Modificação Silenciosa!" exigindo que você os adivinhasse e colocasse na matriz antes do commit. É o paradoxo "Catch-22".
- **Solução:** O arquivo `workflow_journal_auditor.py` possui uma lista `SHADOW_FILES`. Arquivos nesta lista **estão totalmente isentos da regra de Modificação Silenciosa e de Fraude Narrativa**. Eles vivem nas sombras, operados unicamente pelos oráculos mecânicos do pipeline.

> **💡 Regra de Ouro:** Criou um novo relatório auto-gerado que vai rodar no pre-commit? **Adicione-o na lista `SHADOW_FILES` do SAM**, caso contrário, prepare-se para o bloqueio de Modificação Silenciosa.

### 3.3 O Curto-Circuito do Diário (Gatilho de Estado)
- **Problema:** O SAM costumava ler a entrada velha do Journal e reclamar de Fraude Narrativa se você esquecesse de fazer uma entrada nova (pois os arquivos antigos já estavam commitados e sumiam do Git). Além disso, era chato ter que preencher o Journal só para atualizar logs automáticos e regras de IA.
- **Solução:** O SAM ganhou inteligência de estado. Se você não alterou o `JOURNAL.md`, o SAM vasculha seu Git procurando se você tocou em algum arquivo *governado* (não-sombra e não-ignorado). 
  - Se **NÃO** tocou (apenas mexeu em `.agents/` ou Shadow Files): O SAM te libera sem pedir entrada no Journal. 
  - Se **TOCOU** na arquitetura: O SAM bloqueia com erro fatal IMEDIATO de "Modificação Silenciosa", antes mesmo de ler matriz velha, alertando que você modificou código sem abrir uma ata no diário.

---

## ⛓️ 4. A Arquitetura do Ecossistema

O Journal não vive isolado. Ele é sustentado por outros 3 pilares:

### O Orquestrador (`journal-sync/SKILL.md`)
O agente executor roda essa skill para gerar a entrada perfeita. A skill calcula o impacto ("Blast Radius") lendo o `rx-communications.md` e preenche a Matriz de Propagação automaticamente.

### O Synapse (`JOURNAL_SYNAPSE.md`)
O cérebro complementar do SAM. É um JSON que diz: *"Se o `schema.sql` for tocado na Matriz, exija que o `TECHNICAL_REQUIREMENTS.md` também esteja"*. Ele injeta regras dinâmicas no SAM sem que precisemos alterar código Python.

### O Glossário (`FILE_GLOSSARY.md`)
Dicionário de todos os arquivos. O SAM valida se novos arquivos criados (e listados na matriz) foram corretamente registrados aqui (via regra do Synapse).

---

## 🏁 5. Troubleshooting: "Meu Commit Falhou, O Que Eu Faço?"

1. **"Fraude Narrativa: Arquivo X ausente no Git"**
   *Causa:* Você listou `X` na matriz, mas não o modificou de fato.
   *Solução:* Remova `X` da matriz do Journal, OU de fato altere e salve o arquivo `X`.

2. **"Modificação Silenciosa: Arquivo Y ausente na Matriz"**
   *Causa:* Você alterou `Y`, mas não colocou no Journal.
   *Solução:* Abra o Journal e adicione `- [x] Y -> [motivo]` na primeira entrada.
   *(Se `Y` for um arquivo auto-gerado pelo pipeline, a solução correta é adicioná-lo à lista `SHADOW_FILES` no script do SAM, não na matriz do Journal).*

3. **Ficou preso no Catch-22 de um `STATE.md` de feature (ex: `.specs/features/xyz/STATE.md`)?**
   Lembre-se: Ele não é um *Shadow File* por padrão, pois cada spec tem o seu. Se o pipeline o atualiza automaticamente no encerramento, simplesmente *adicione-o à sua Matriz de Propagação* antes de commitar, que o SAM vai aceitá-lo amigavelmente.
