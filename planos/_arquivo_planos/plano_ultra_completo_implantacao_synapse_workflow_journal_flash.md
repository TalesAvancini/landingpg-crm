# Plano Ultra Completo: Implantacao do Synapse + workflow_Journal (para Flash)

## Objetivo
Implementar um circuito anti-migue completo onde:
- o Executor declara promessa no `JOURNAL.md`;
- o sistema calcula obrigacoes por `git + synapse`;
- o Validador autonomo (context_id diferente) audita a evidencia fisica;
- o commit so passa quando o contrato fecha.

Este plano foi escrito para execucao posterior pelo Flash, com rollout seguro e sem criar fragilidade operacional.

## Escopo
- Criar SSOT de regras `JOURNAL_SYNAPSE` em formato hibrido (parseavel + humano).
- Introduzir `journal_mode: strict` no governor (instrucao) e no harness (execucao).
- Implementar comando unico `workflow_Journal` no pipeline (`run_context.py`).
- Definir template obrigatorio de entrada no `JOURNAL.md` (narrativa + checklist + contrato).
- Garantir segregacao executor/validator por `executor_context_id != validator_context_id`.

## Fora de escopo (nesta rodada)
- Watcher em tempo real ao salvar arquivo no editor.
- NLP pesado para interpretar narrativa livre.
- Reescrever historico antigo do Journal.

---

## Arquitetura alvo (simples e robusta)

### 1) Fontes de verdade
- Declaracao: `JOURNAL.md`.
- Regras de obrigacao: `JOURNAL_SYNAPSE`.
- Realidade: `git status --porcelain`, `git diff --name-only`, `git diff --stat`, `git diff`.
- Gate final: `harness_runner.py`.

### 2) Principio central
- O Executor nao define o que e obrigatorio.
- O Synapse define obrigacoes.
- O Harness calcula obrigacoes esperadas pelo que o Git realmente mostra.
- O Validador independente fecha contrato (ou veta).

### 3) Regra de ouro
- Se `git diff` mostrar mudanca sensivel e o Journal nao refletir, bloqueia.
- Se o Journal prometer propagacao e o Git nao provar, bloqueia.

---

## Design do arquivo Synapse (SSOT)

### Caminho sugerido
- `.context/maintenance/JOURNAL_SYNAPSE.md`

### Formato
- Frontmatter YAML parseavel para o script.
- Tabela humana abaixo para manutencao pelo time.

### Exemplo de schema minimo
```yaml
version: 1
mode: strict
rules:
  - id: sql_change
    when_any_changed:
      - ".context/maintenance/schema.sql"
    require_journal_tags:
      - "SQL"
      - "Schema"
    require_files_touched:
      - ".context/maintenance/TECHNICAL_REQUIREMENTS.md"
    require_evidence_in_files:
      - file: ".context/maintenance/TECHNICAL_REQUIREMENTS.md"
        contains_any: ["schema", "migration"]
    severity: critical

  - id: new_context_path
    when_new_path_under:
      - ".context/"
    require_files_touched:
      - ".context/maintenance/rx-anatomy.md"
    require_evidence_in_files:
      - file: ".context/maintenance/rx-anatomy.md"
        contains_path_from_diff: true
    severity: critical
```

### Regras iniciais obrigatorias (MVP)
1. Mudou `schema.sql` -> exige `TECHNICAL_REQUIREMENTS.md`.
2. Criou caminho novo em `.context/` -> exige `rx-anatomy.md`.
3. Mudou regra em `brain/RULES.md` -> exige registro no Journal e possivel bump de versao quando aplicavel.
4. Mudou roteamento de mercado -> exige `SSOT_MAP.md`.

---

## Template obrigatorio do Journal (modo strict)

Cada entrada nova deve usar este bloco:

```markdown
## 📅 YYYY-MM-DD HH:MM | [TIPO]: [TITULO]

### Narrativa
[o que foi feito, por que, impacto]

### Matriz de Propagacao (Sinapse)
- [ ] `arquivo_obrigatorio_1` -> [acao esperada]
- [ ] `arquivo_obrigatorio_2` -> [acao esperada]

### Alteracoes Operacionais (Reality Check)
- Arquivos esperados: `...`
- Arquivos observados (git diff --name-only): `...`
- Resumo (git diff --stat): `...`

### Contrato de Validacao
- executor_context_id: `CTX_EXEC_...`
- validator_context_id: `[PENDENTE]`
- segregation_check: `executor_context_id != validator_context_id`
- status: `🔴 BLOQUEADO`
- validator_verdict: `[PENDENTE]`
```

Observacao:
- Executor abre promessa e preenche pendencias.
- Executor nao fecha o proprio [x].
- Validador preenche `validator_context_id`, veredito e status final.

---

## workflow_Journal (comando unico)

### Nome do comando
- `python run_context.py workflow-journal`
- npm alias: `npm run context:workflow-journal`

### Fluxo interno
1. Ler ultima entrada ativa do `JOURNAL.md`.
2. Validar formato minimo da entrada (campos obrigatorios).
3. Ler `JOURNAL_SYNAPSE` e construir `expected_obligations`.
4. Ler estado do Git e inferir mudancas reais.
5. Cruzar:
   - obrigacoes esperadas vs checkboxes declarados;
   - obrigacoes esperadas vs arquivos realmente tocados;
   - evidencias minimas no conteudo dos arquivos-alvo.
6. Validar segregacao de contexto executor/validator.
7. Emitir resultado deterministico:
   - `HARNESS-PASS` ou
   - `HARNESS-FAIL` com lista exata de pendencias.

### Modos
- `--mode assist`: bloqueia apenas `severity=critical`, resto warning.
- `--mode strict`: bloqueia qualquer violacao de contrato.
- `--fix-suggest`: apenas sugere patch textual no terminal.

---

## Validador autonomo (contexto diferente)

### Contrato de independencia
- `validator_context_id` deve ser diferente de `executor_context_id`.
- Se IDs iguais, nulos, ou ausentes em modo strict -> bloqueio.

### Protocolo do Validador
1. Nao confiar na narrativa.
2. Conferir diff real (`git diff`, `--name-only`, `--stat`).
3. Conferir propagacao obrigatoria por Synapse.
4. Registrar veredito no Journal:
   - `status: 🟢 READY TO COMMIT` quando tudo bate.
   - `status: 🔴 VETO` quando houver divergencia.

### Exemplos de veto
- `schema.sql` mudou sem trilha SQL no Journal.
- `rx-anatomy.md` nao atualizado apos pasta nova.
- Checkbox marcado sem diff correspondente.

---

## Integracao com governanca atual

### Arquivos a atualizar na implementacao
- `run_context.py` (novo comando `workflow-journal`).
- `.context/_scripts/harness_runner.py` (novo check Synapse + Git).
- `.context/brain/RULES.md` (secao `journal_mode: strict`).
- `.context/brain/MASTER_FLOW.md` (ato/etapa do workflow_Journal).
- `package.json` (script npm).
- `.context/maintenance/JOURNAL.md` (template padrao de entrada futura).

### Compatibilidade
- Specs legadas sem metadados novos: manter fallback gracioso em `assist`.
- CI/protected branch: exigir `strict`.

---

## Estrategia anti-fragilidade

1. Evitar hash byte-a-byte como prova primaria.
2. Usar validacao semantica minima (presenca de secao, termos-chave, path novo refletido).
3. Se Synapse estiver malformado:
   - em `assist`: warning + fallback baseline.
   - em `strict`: bloqueio com erro claro e linha/causa.
4. Mensagens de erro sempre acionaveis (o que faltou + onde corrigir).

---

## Rollout em 3 fases

### Fase 1 - Shadow (sem bloqueio)
- Executar `workflow-journal` em modo relatorio.
- Medir falsos positivos/negativos.
- Ajustar Synapse inicial.

### Fase 2 - Critical Gate
- Bloquear apenas regras `critical`.
- Treinar uso do template Journal e rotina do Validador.

### Fase 3 - Strict Gate
- Ativar bloqueio completo em CI e branch protegida.
- Tornar `workflow-journal` obrigatorio no fluxo de commit.

---

## Casos de teste obrigatorios (MVP)

1. **PASS feliz**
- Mudou `schema.sql`, atualizou `TECHNICAL_REQUIREMENTS`, Journal coerente, validador diferente.

2. **FAIL omissao**
- Mudou `schema.sql`, Journal nao citou SQL.

3. **FAIL propagacao**
- Journal citou SQL, mas `TECHNICAL_REQUIREMENTS` nao mudou.

4. **FAIL independencia**
- `executor_context_id == validator_context_id`.

5. **FAIL estrutura nova sem Rx**
- Criou pasta em `.context/`, nao refletiu em `rx-anatomy.md`.

6. **PASS assist com warning**
- Violacao nao critica em modo assist nao bloqueia, apenas reporta.

---

## Definition of Done (DoD)

- Existe `JOURNAL_SYNAPSE` parseavel e versionado.
- `workflow-journal` executa e gera veredito deterministico.
- Harness cruza Journal + Synapse + Git diff.
- Bloqueios criticos funcionam antes do commit.
- Segregacao executor/validator e obrigatoria em strict.
- Documentacao (`RULES` e `MASTER_FLOW`) alinhada ao comportamento real.

---

## Prompt de execucao para Flash (copiar e usar)

```text
Execute este plano por fases sem quebrar o fluxo atual.

Prioridade:
1) Criar JOURNAL_SYNAPSE em formato hibrido com regras MVP.
2) Implementar comando run_context.py workflow-journal.
3) Integrar check no harness_runner.py (git + synapse + journal).
4) Atualizar RULES.md e MASTER_FLOW.md com journal_mode: strict.
5) Adicionar script npm context:workflow-journal.
6) Rodar testes de 6 cenarios (pass/fail) e reportar evidencias.

Regras:
- Nao usar hash rigido como criterio principal.
- Nao quebrar compatibilidade local em modo assist.
- Mensagens de erro devem ser objetivas e acionaveis.
- Segregacao executor/validator obrigatoria em strict.
```

## Resultado esperado
Promessa (Journal) + Prova (Git) + Selo independente (Validador) formando um circuito fechado anti-migue, com baixa burocracia local e alta seguranca no gate final.
