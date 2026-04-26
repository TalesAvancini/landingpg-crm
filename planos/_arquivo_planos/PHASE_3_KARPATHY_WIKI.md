# [Fase 3] Karpathy Wiki Hardening (H.O.K v2.5 - Production Ready)

Plano de engenharia final aprovado para implementação futura. Ele implementa a Wiki de Karpathy no `.context` garantindo **Zero RAG Analytics** com resiliência à prova do modelo Flash.

## Status: SALVO PARA EXECUÇÃO FUTURA (Aguardando GO)

---

## Proposed Changes

### [Componente: Estrutura Física]

#### [NEW] .context/market/RAW/ e .context/market/WIKI/
*   **Aresta:** Serão criados com `.gitkeep`.
*   **Regras:** `RAW/` será blindado contra leitura da IA e ignorado nos pacotes.
*   **Template (`WIKI/_template.md`):** Arquivo mestre injetado contendo o YAML com `entity`, `concept`, `tags` e a exigência mandatória da linha `> Fonte: RAW/...`.

---

### [Componente: Lógica e Consulta]

#### [MODIFY] .context/_scripts/context_oracle.py
O script sofrerá uma refatoração cirúrgica em sua inteligência de busca:
1.  **Limitação (Privileged Isolation):** Pesquisará **apenas** em `market/WIKI` e `market/compliance`.
2.  **Triple-Match Heuristic:** O *score* de confiança considerará 1º Tags/Frontmatter, 2º Nome do arquivo, 3º Início do conteúdo.
3.  **Anti-Bloat Lock:** Retornará **exclusivamente 1 arquivo completo** (o *top match*), impedindo sobrecarga invisível.
4.  **Graceful Fallback:** Se a pesquisa for sobre o código base da aplicação (ex: auth do database), e não houver retorno na WIKI, o script não mais "falha e sai", ele devolverá uma mensagem limpa instruindo a IA: `"[INFO] Termo não encontrado no WIKI (Mercado). Use seu bundle ou busque no schema/PRD."`

---

### [Componente: Automação e Linting]

#### [MODIFY] .context/_scripts/lint_wiki.py
*   **Regra Karpathy Automática:** Injeção de uma checagem que fará o commit falhar se um manifesto na pasta `WIKI/` esquecer a fita de auditoria. Todo arquivo `WIKI/*.md` será escaneado por `> Fonte: RAW/` ou `> Fonte: market/RAW/`.

#### [MODIFY] .context/brain/RULES.md
*   Adição da seção **Protocolo de Destilação (RAW → WIKI)**, formalizando o contrato de que "Humanos lidam com o RAW, Agentes e Lint lidam com WIKI".

#### [MODIFY] .context/_scripts/captura_projeto.py (ou equivalente de bundle)
*   Assegurar que a regra de exclusão (ignore list) bloqueia a pastar `market/RAW/` de ser lida durante a construção do prompt gigantesco do projeto.

---

## Verification Plan

### Automated Tests
1. Script injetará WIKI sem fita de auditoria → O Linter DEVE barrar.
2. Script injetará WIKI com Frontmatter e Tags, testando o `context_oracle.py` contra as tags → DEVE retornar o arquivo inteiro sem erros de JSON.
3. Oráculo consultando termos internos (ex: `postgres`) → DEVE devolver a mensagem de Fallback.
