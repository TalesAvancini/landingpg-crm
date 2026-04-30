---
contract_version: 2.5.2
parties: ["@antigravity-agent", "@user"]
type: standard
executor_context_id: "CTX_FIX_SAM_01"
validator_context_id: "CTX_AI_QA_AUDIT"
definition_of_done:
  - [x] Alterar `get_latest_journal_entry` no script do auditor para ler o topo do arquivo.
  - [x] Garantir que o parser ignore o cabeçalho do JOURNAL.md.
  - [x] Validar se o pipeline aprova um commit usando apenas o contrato da entrada mais recente.
qa_signoff: true

signed_by: "@qa-validator"
---

# 📄 Spec: Correção da Cronologia do SAM (Sistema Anti-Migué)

## 🎯 Objetivo
Corrigir o "Drift de Leitura" no validador do SAM (`workflow_journal_auditor.py`). Atualmente, o script procura o Contrato de Validação na **última entrada do arquivo (rodapé)**. No entanto, o padrão arquitetural do projeto exige que o `JOURNAL.md` siga a **Ordem Cronológica Reversa (mais recente no topo)**. O objetivo é sincronizar o auditor com a arquitetura.

## 🔍 O Bug (Raio-X Técnico)
No arquivo `workflow_journal_auditor.py`, a função `get_latest_journal_entry()` contém o seguinte código:

```python
entries = re.split(r"(?m)^## 📅", content)
valid_entries = [e for e in entries if e.strip()]
return "## 📅" + valid_entries[-1] if valid_entries else ""
```

O uso do índice `[-1]` faz com que o parser extraia o último elemento da lista, que fisicamente é o bloco mais antigo do arquivo.

## 🛠️ Solução Proposta
Modificar a função para extrair o primeiro bloco válido após o cabeçalho do arquivo (geralmente no índice `[1]`, dependendo de como o `re.split` tratar o texto inicial).

```python
# Pseudo-código da correção:
# 1. Separar as entradas
# 2. O primeiro bloco (índice 0) é o cabeçalho do arquivo.
# 3. O primeiro bloco de data válido é o índice 1 (se existir).
return "## 📅" + valid_entries[1] if len(valid_entries) > 1 else ("## 📅" + valid_entries[0] if valid_entries else "")
```
*(Nota: Precisamos testar o comportamento exato do regex no array antes de commitar).*

## ✅ Critérios de Aceite
- [x] O script `workflow_journal_auditor.py` foi atualizado.
- [x] Ao rodar `npm run context:all`, o SAM valida com sucesso a entrada que está no **TOPO** do `JOURNAL.md`.
- [x] Nenhuma quebra em regex secundários (como os que checam os checkboxes da matriz de propagação).
- [x] Resultado registrado no `STATE.md`.

## 🔎 Regra de Segregação
- Sendo `type: standard`, a correção precisará ser revisada pelo `@user` (como validator) antes do fechamento do contrato, comprovando o rigor do Zero Trust.
