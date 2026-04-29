# 🔬 Relatório Original: O Oracle Como Ele Realmente É (Claude Opus)

> **Data:** 2026-04-28
> **Método:** Leitura linha a linha do `context_oracle.py`, `_index.md`, `ingest_wiki_guard.py`, `_wiki_log_utils.py`, `wiki_log.md` e `SSOT_MAP.md`.

---

## 1. O Que o Oracle Realmente Faz (Sem Romantismo)

O Oracle é um buscador de palavras-chave em 134 linhas de Python. Ele:
1. Lê todos os `.md` dentro de `market/WIKI/` e `market/compliance/`.
2. Quebra cada arquivo em palavras de 3+ caracteres.
3. Atribui pesos fixos: corpo (0.2), nome do arquivo (0.5), palavras do título (0.6), título exato (0.8), tags do `_index.md` (1.0).
4. Soma os pesos de cada keyword da query contra esse índice.
5. Se o arquivo top tiver score ≥ 0.6, devolve o **conteúdo inteiro** do arquivo. Senão, devolve um warning.

Isso é tudo. Não há stemming, não há stopwords, não há normalização. A query `"como funciona o harness?"` e `"harness"` produzem resultados diferentes porque `"como"` e `"funciona"` também geram hits (ruído).

---

## 2. Três Problemas Que Ninguém Mencionou

### 2.1 O `_index.md` é um Beco Sem Saída

O `_index.md` atual tem exatamente **1 entrada**:
```markdown
- [[conceito_teste]] | tags: ecommerce, checkout
```

Esse arquivo aponta para `conceito_teste.md`, que **não existe** no disco. Os 4 artigos reais da Wiki (`harness_architecture`, `harness_behavior`, `harness_maintainability`, `ralph_wiggum_loop`) **não estão no índice**. O roteamento determinístico (peso 1.0) — que deveria ser a vantagem competitiva do Oracle — está completamente desconectado do conteúdo real.

Na prática, o Oracle funciona hoje **apenas pela busca léxica** (pesos 0.2–0.8). O canal determinístico é decorativo.

**Implicação para o template:** Quando alguém clonar esse template e começar a popular a Wiki, o `_index.md` vai ficar dessincronizado imediatamente, a menos que exista um mecanismo que o atualize automaticamente. Isso é um problema de **design do template**, não do projeto.

### 2.2 O Retorno é Binário Demais

O Oracle devolve ou o arquivo inteiro (se ≥ 0.6) ou um warning genérico. Não existe meio-termo. Num template que será usado por projetos de tamanhos variados, isso cria dois cenários ruins:
- **Wiki com artigos pequenos (como agora, ~500 tokens):** Funciona bem. O arquivo inteiro é leve.
- **Wiki com artigos grandes (quando o projeto real chegar):** O Oracle vai vomitar 5KB+ de texto num agente que só precisava de uma definição.

O `_template.md` já prevê a seção `## Resumo`. O Oracle poderia retornar **apenas o Resumo** quando `confidence < 0.8`, e o arquivo inteiro quando `confidence ≥ 0.8`. Isso não requer chunking complexo — é um `re.search` a mais.

### 2.3 O Oracle Não Sabe Que Não Sabe

Quando a query não bate com nada, o Oracle retorna:
```json
{"answer": "[INFO] Termo não encontrado na WIKI de Mercado...", "confidence": 0.0}
```

Mas quando a query bate **parcialmente** com lixo (palavras genéricas como "como", "funciona", "modelo"), o Oracle retorna um arquivo com `confidence: 0.4` e um warning vago. O agente que recebe isso não tem como distinguir entre:
- "O conceito existe mas a query foi ruim" (reformule a pergunta)
- "O conceito simplesmente não está na Wiki" (crie o artigo)

**Proposta:** Adicionar um campo `"match_quality"` que indique quantas keywords da query realmente casaram vs quantas eram ruído. Algo como:
```python
matched = len(keywords & set(idx.keys()))
quality = matched / len(keywords) if keywords else 0
```
Se `quality < 0.3`, a resposta muda para: *"A maioria dos termos da sua query não existe na Wiki. Considere reformular ou criar o artigo."*

---

## 3. O Insight do Bootstrap (Corrigido)

Este template é um **molde de governança** que se autoconstrói. A Wiki vazia é correta por design. Mas o `_index.md` desconectado dos artigos reais é um **bug do template**.

A correção não é "popular a Wiki com conteúdo genérico". É garantir que o **mecanismo de sincronização** entre artigos e índice funcione quando o usuário clonar o template e começar a usar.

**Proposta concreta:** O `ingest_wiki_guard.py` já valida frontmatter e fonte. Ele poderia, no final de uma ingestão bem-sucedida, **regenerar o `_index.md`** automaticamente a partir dos frontmatters dos artigos válidos:
```python
def rebuild_index(articles):
    lines = ["# WIKI Index Raiz\n> Fonte: SSOT_MAP.md\n\n## Topicos\n"]
    for art in articles:
        fm = extract_frontmatter(art)
        concept = fm.get("concept", art.stem)
        tags = fm.get("tags", "")
        rel = art.relative_to(WIKI_DIR).with_suffix("").as_posix()
        lines.append(f"- [[{rel}]] | tags: {tags}\n")
    INDEX_FILE.write_text("".join(lines), encoding="utf-8")
```

Isso elimina a dessincronização por design. O `_index.md` deixa de ser um arquivo mantido manualmente e passa a ser um artefato gerado.

---

## 4. O Papel Real do Oracle Neste Template

O Oracle hoje é subutilizado. O `wiki_log.md` mostra que em toda a história do template, houve **exatamente 1 query real** (linha 34: `"Loop"` → `ralph_wiggum_loop.md`, conf 0.80). Todo o resto são logs de INGEST e LINT.

Isso não é um problema — é a realidade de um template em construção. Mas revela que o Oracle foi projetado para um futuro (projetos com domínio rico) que ainda não chegou. A pergunta certa não é "como otimizar o Oracle?" mas sim **"o que ele precisa resolver quando o template for instanciado?"**

Respostas:
1. **Resolver jargão de domínio** — Quando o projeto for um e-commerce, o Oracle precisa saber que "carrinho" = "cart" = "checkout". Isso é o campo `aliases` do `_template.md`, que já existe mas o Oracle **ignora completamente** (ele não lê o frontmatter dos artigos).
2. **Servir como "cola" entre o NotebookLM e o local** — O `SSOT_MAP.md` define uma hierarquia onde o NotebookLM é nível 1 e a Wiki local é nível 2. O Oracle só busca no nível 2. Ele não tem consciência do nível 1. Um fallback para o MCP do NotebookLM quando a Wiki local retorna `confidence < 0.5` fecharia esse gap. 

---

## 5. Resumo das Propostas Originais

| # | Proposta | Esforço | Impacto |
|:---|:---|:---:|:---|
| 1 | Regeneração automática do `_index.md` pelo `ingest_wiki_guard.py` | Baixo | Elimina dessincronização do roteamento determinístico |
| 2 | Leitura de `aliases` do frontmatter no `build_index()` | Baixo | Habilita sinonímia de domínio que já está prevista no template |
| 3 | Retorno graduado (Resumo vs Arquivo Inteiro) baseado em confidence | Baixo | Previne Context Bloat em projetos futuros com Wiki densa |
| 4 | Campo `match_quality` na resposta | Baixo | Permite ao agente distinguir "query ruim" de "conceito ausente" |
| 5 | Fallback para NotebookLM MCP quando Wiki local falha | Médio | Fecha o gap entre nível 1 e nível 2 da hierarquia SSOT |
