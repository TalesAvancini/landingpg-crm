# 🔎 Ajustes Cirúrgicos Válidos (Auditoria Qwen — Filtrado pelo MiMo)

> **Autor:** Qwen (Auditor), filtrado pelo MiMo
> **Data:** 2026-04-28

---

## 1. Test Isolation (Sandbox)
Usar `tempfile.TemporaryDirectory()` + copiar `WIKI/`, `_index.md`, `_template.md`. Mockar `CONTEXT_DIR`.

## 2. Stemming com Dicionário de Sufixos Seguros
`SAFE_SUFFIXES` mapeado, guarda `len(word) > 4 and len(stem) >= 3`.

## 3. Campo `schema_version` no Payload
`"schema_version": "v3"` no JSON. Fallback para scripts legados.

## 4. Cache Race Condition (Escrita Atômica)
`tempfile + os.replace()` na escrita do cache (padrão do `purge_journal.py`).

## 5. Stemming: Whitelist de Termos Técnicos
Termos da whitelist pulam o stemming.

## 6. Top-N: Hard Limit de Caracteres
`total_chars <= 12000` por resposta. Resultados 2+ truncados em 300 chars.

## 7. Parser do oracle_analytics.py
Regex estrito + ignorar linhas sem match + `[WARN]` em vez de crash.
