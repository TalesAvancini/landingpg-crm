# 🔎 Avaliação Final do Plano Consolidado Oracle v3 (MiMo — 3ª Rodada)

> **Autor:** MiMo (Auditor)
> **Alvo:** `plano_consolidado_Oracle_v3.md` (versão atualizada com auditorias incorporadas)
> **Data:** 2026-04-28
> **Nota:** 9/10 direção, 8/10 execução (subiu de 8/10 e 6/10)

---

## O Problema dos Testes que Não Podem Passar

Os testes listados incluem cenários que **não existem no Oracle atual**:

- `test_stem_converges()` — vai falhar (stemming não existe)
- `test_top_n_returns_multiple()` — vai falhar (Oracle retorna top-1)
- `test_aliases_indexed()` — vai falhar (aliases não são lidos)
- `test_siglas_2_chars()` — vai falhar (filtro de 3+ mata QA)

**Solução:** Dividir a suíte em duas categorias:

```python
# === BASELINE: devem passar no Oracle ATUAL ===
def test_basic_query_returns_result(): ...
def test_empty_query_returns_missing(): ...
def test_known_term_finds_correct_file(): ...
def test_index_file_is_read(): ...
def test_json_output_is_valid(): ...

# === TARGET: devem passar APÓS a fase correspondente ===
@pytest.mark.phase(1.1)
def test_stem_converges(): ...
# etc.
```

## Detalhe Menor

Itens 10-16 do roadmap têm a coluna "Critério de Sucesso" vazia.

## Posição Final

Com a separação baseline/target, o plano fica **executável de verdade**. Pode executar.
