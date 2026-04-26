# Nível 2 Karpathy Wiki – Implementation Plan

**Objetivo**: Implantar a camada WIKI (RAW → WIKI) com roteamento determinístico, guardrail de ingestão, lint incremental e integração no pipeline, tudo executado via spec‑driven na pasta `.specs`.

## User Review Required
> [!IMPORTANT] **Revisão necessária** – Confirme o plano antes de gerar os specs e iniciar a execução.  
> - As alterações são *patches cirúrgicos*; nenhum arquivo será sobrescrito integralmente.  
> - O fluxo será orquestrado pelos specs em `.specs/features/wiki_level2/`.

## Proposed Changes
---
### 1️⃣ Criação de novos arquivos (caminhos completos)
- **[NEW] [.context/market/WIKI/_index.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/market/WIKI/_index.md)**
  - Estrutura mínima do índice raiz da WIKI.
- **[NEW] [.context/market/wiki_log.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/market/wiki_log.md)**
  - Log append‑only de ingestões e lint.
- **[NEW] [.context/_scripts/ingest_wiki_guard.py](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/_scripts/ingest_wiki_guard.py)**
  - Validação de artigo (front‑matter, `> Fonte:`, `## Key Takeaways`, `## Related`/wikilink). Não verifica presença no índice.

---
### 2️⃣ Modificações em arquivos existentes (patches cirúrgicos)
- **[MODIFY] [.context/_scripts/context_oracle.py](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/_scripts/context_oracle.py)**
  - Injetar leitura de `SSOT_MAP.md` e `_index.md` antes de fallback lexical.  
  - Manter fallback lexical existente caso índice falhe ou esteja vazio.
- **[MODIFY] [.context/_scripts/lint_wiki.py](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/_scripts/lint_wiki.py)**
  - Implementar flag `--strict` que aborta (`exit 1`) quando:  
    - Falta `> Fonte:`  
    - Front‑matter incompleto  
    - Wikilink quebrado  
    - Ausência de `## Key Takeaways` ou `## Related`.  
  - Relatório de lint será emitido no console; **não** criar diretório `_lint_reports/`.
- **[MODIFY] [run_context.py](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/run_context.py)**
  - Adicionar sub‑comandos `ingest-guard` e `wiki-health` que chamam os scripts acima.  
  - `ingest-guard` → `python .context/_scripts/ingest_wiki_guard.py`  
  - `wiki-health` → `python .context/_scripts/validate_context.py check_wiki_integrity` (verifica existência/tamanho do índice).
- **[MODIFY] [package.json](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/package.json)**
  - Scripts atualizados:  
    ```json
    "context:ingest-guard": "python run_context.py ingest-guard",
    "context:wiki-health": "python run_context.py wiki-health"
    ```
- **[MODIFY] [.context/_scripts/validate_context.py](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/_scripts/validate_context.py)**
  - Função `check_wiki_integrity()` → verifica apenas existência e tamanho > 50 bytes de `_index.md` (não duplica lint).
- **[MODIFY] [.context/brain/RULES.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/brain/RULES.md)**
  - Inserir bloco de fluxo: `INGEST → LINT → LOG`.
- **[MODIFY] [.context/brain/MASTER_FLOW.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/brain/MASTER_FLOW.md)**
  - Incluir operação de ingestão wiki no diagrama de fluxo.

---
### 3️⃣ Spec‑driven orchestration (`.specs`)
- Criaremos a pasta **`.specs/features/wiki_level2/`** contendo:  
  - `spec.md` – descrição da feature, critérios de aceitação (pipeline verde, fallback lexical, guard‑pass) **e** campos `qa_signoff: true` e `signed_by: "@qa-validator"` para atender ao fail‑closed do harness.
  - `STATE.md` – estado inicial (empty).  
  - `tasks.md` – lista de tarefas atômicas gerada a partir deste plano (será preenchida automaticamente pelo motor spec‑driven).  
  - `README.md` – instruções de execução (`npm run spec wiki_level2`).
- O motor spec‑driven garantirá:  
  1. Cada mudança será um commit atômico **apenas quando o usuário autorizar**.  
  2. Verificação automática dos testes listados na **Definition of Done** (oracle, lint‑strict, ingest‑guard, context:all).

---
## Open Questions
- **Log rotation**: Qual política de retenção deseja para `wiki_log.md` (ex.: 200 linhas ou 10 k chars)?
- **Template de artigo**: Quer um arquivo `_template.md` para novos artigos? (pode ser criado agora ou adicionado depois).

---
## Verification Plan
### Automated Tests
- `npm run context:oracle "termo_inexistente"` → deve retornar **warning + fallback lexical** e **exit 2** (conforme contrato atual do `context_oracle.py`).
- `npm run context:lint‑strict` → falha se houver artigo sem `> Fonte:` ou sem `Key Takeaways`.
- `npm run context:ingest‑guard` → exit 0 quando apenas `_index.md`/`_template.md` existirem; exit 1 caso artigo inválido.
- `npm run context:wiki-health` → verifica existência/tamanho do índice (`check_wiki_integrity`).
- `npm run context:all` → pipeline verde, sem regressão.

### Manual Verification
- Abra o `wiki_log.md` e confirme que cada ingestão aparece com timestamp e status.
- Verifique visualmente o índice raiz (`.context/market/WIKI/_index.md`) e alguns artigos para garantir o schema.
