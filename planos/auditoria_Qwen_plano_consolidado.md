# 🔎 Auditoria do Plano Consolidado Oracle v3 (Qwen)

> **Autor:** Qwen (Auditor)
> **Alvo:** `plano_consolidado_Oracle_v3.md`
> **Data:** 2026-04-28
> **Nota atribuída:** 9.2/10

---

## ✅ Por que a Fusão Funciona (Pontos Fortes)
1. **Faseamento Lógico Impecável:** `Corrigir → Calibrar → Integrar` é a única sequência válida. Muitos frameworks falham ao tentar otimizar scoring antes de garantir que o índice aponta para arquivos que existem.
2. **Transparência nos Descartes:** A tabela de "O Que Foi Descartado" é tão valiosa quanto o plano em si. Eliminar multiplicadores por role e chunking genérico evita viés declarativo e complexidade desnecessária.
3. **Respeito à Restrição Operacional:** A decisão de iniciar o Gate Epistemológico em `Modo Light` e adiar o fallback NotebookLM mostra maturidade. O humano nunca é refém do pipeline.
4. **Feedback Loop Nativo:** `oracle_analytics.py` transforma o Oracle de ferramenta estática em sistema que **aprende com falhas**. Isso é raro em soluções `stdlib-only`.

---

## ⚠️ Riscos Críticos & Ajustes Táticos (Antes de Codar)

| Item do Plano | Risco na Prática | Ajuste Recomendado |
|---------------|------------------|---------------------|
| **0.1 Regenerar `_index.md`** | Se o `ingest_wiki_guard.py` falhar no meio, o índice fica corrompido. | Usar escrita atômica: gerar `_index.md.tmp` → `os.replace()`. Adicionar backup `_index.md.bak`. |
| **1.1 Stemming pt-BR** | Regex puro de sufixos em português causa *over-stemming* (ex: `cartão` → `cart`, `carro` → `car`). | Limitar a sufixos seguros (`-ção`, `-mente`, `-ar/er/ir` no infinitivo, `-s`/`-es` plural). Manter match exato como fallback prioritário. |
| **1.3 Top-N + Graduado** | Resumos longos nos resultados 2 e 3 reintroduzem `Context Bloat`. | Fixar limite rígido: `## Resumo` máximo de **300 chars** ou até a próxima `##`. Truncar com `[...]`. |
| **2.4 Cache mtime** | CLI scripts morrem após execução. Cache in-memory é inútil entre chamadas. | Persistir em `.context/market/.wiki_index.cache.json`. Invalidar apenas se `max(mtime(WIKI/*.md)) > cache_built_at`. |
| **2.6 Gate Epistemológico Light** | Risco de "virar permanente" por comodidade. | Definir gatilho: após `>5` warns consecutivos na mesma tag/conceito, gerar `gate_upgrade.proposed.md` exigindo decisão do `@vision-architect`. |

---

## 🔍 Pontos Cegos (O que não está no plano, mas deveria)

### 1. Normalização Pré-Query
O plano foca em indexação e scoring, mas ignora a **higiene da query** antes do `Counter`.
- **Problema:** Queries com markdown (`**CI**`, `` `DB` ``), aspas ou acentos mal tratados geram tokens fantasmas.
- **Solução:** Adicionar `normalize_query()` na Fase 0:
  ```python
  def normalize_query(q):
      q = re.sub(r'[`*#\[\](){}]', '', q)  # Limpa markdown
      q = unicodedata.normalize('NFKD', q).encode('ASCII', 'ignore').decode()  # Remove acentos
      return q.lower().strip()
  ```

### 2. Escopo de Invalidação do Cache
`max(os.path.getmtime(f))` é perigoso se varrer o repo inteiro.
- **Solução:** Restringir explicitamente a `CONTEXT_DIR / "market/WIKI/**/*.md"` e `_index.md`. Ignorar `RAW/`, `compliance/`, logs.

### 3. Validação do `oracle_analytics.py`
Se o formato do `wiki_log.md` mudar (ex: nova coluna), o parser quebra silenciosamente.
- **Solução:** Usar regex estrito para extrair `confidence` e `status`. Se falhar, logar `[WARN] Formato do wiki_log.md alterado. Analytics pausado.`

---

## 🛠️ Recomendações de Execução

1. **Fase 0 Primeiro:** Não pule para scoring. Um índice quebrado + aliases ignorados invalida qualquer calibração.
2. **Teste com `tests/test_oracle.py`:** Crie um sandbox com 3 artigos reais (com aliases, sem aliases, siglas). Valide confidence antes/depois da calibração.
3. **Implementar Cache com Persistência:** É o único ganho de performance realista em CLI. Use `json.load()`/`json.dump()` com `mtime` check.
4. **Monitorar `oracle_analytics.py` nas 50 primeiras queries:** Se >30% das queries falharem, há gap no `_index.md`. Se <10% falharem mas confidence média for 0.55, a calibração está muito agressiva.
5. **Manter `outside_role_scope` como `info-only`:** Nunca use para filtrar resultados. O agente pode precisar de contexto transversal. A flag serve apenas para o `PROMPT_LIBRARY` decidir se adiciona um disclaimer.

---

## 🏁 Conclusão
Este plano é **o padrão ouro para evolução de módulos em frameworks AI-Ready**. Ele sintetiza visão estratégica (MiMo), rigor técnico (Opus), pragmatismo de schema (Qwen) e realidade operacional (Flash/Usuário) sem cair em contradições ou over-engineering.
