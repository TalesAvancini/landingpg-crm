# 🏗️ Plano Consolidado: Evolução do Oracle v3 (Best-Of de Todos os Relatórios)

> **Consertar primeiro. Calibrar depois. Integrar por último. Nunca bloquear o humano.**

> **Fontes sintetizadas:**
> - `relatorio_Oracle_Opus.md` (Claude Opus) — Bugs estruturais e análise do código real
> - `relatorio_Oracle_Qwen.md` (Qwen) — Otimizações técnicas e schema
> - `relatorio_MiMo-Oracle.md` (MiMo) — Dissecação do algoritmo de scoring e robustez
> - `relatorio_oracle_MiMo.md` (MiMo) — Visão estratégica e governança proativa
> - `comentarios_Flash.md` (Flash + Usuário) — Diretrizes operacionais e restrições
>
> **Auditorias incorporadas:**
> - `auditoria_MiMo_plano_consolidado.md` — Circularidade da Fase 0.1, testes ausentes, estimativas subdimensionadas
> - `auditoria_MiMo_final.md` — Insistência em testes como item 0.0 (aceita)
> - `auditoria_Qwen_plano_consolidado.md` — Cache deve ser em disco (não in-memory), normalização pré-query, escrita atômica

---

## 🧪 Fase -1: Fundação de Testes (PRÉ-REQUISITO INEGOCIÁVEL)

**Origem:** MiMo (auditoria 1ª e 2ª rodada). *"Sem a suíte de testes, é um salto de fé. Com ela, é engenharia."*

### 0.0 Criar `tests/test_oracle.py`
- **O quê:** Suíte dividida em **BASELINE** (snapshot do Oracle atual) e **TARGET** (especificação do comportamento futuro, marcados como `xfail` até a fase correspondente).
- **Por quê (auditoria MiMo 3ª rodada):** Testes como `test_stem_converges()` vão falhar no Oracle atual porque stemming não existe. Misturar baseline com target transforma o checkpoint em ficção — metade falha, você ignora, e a disciplina morre.

#### Testes BASELINE (devem passar no Oracle ATUAL, antes de qualquer mudança):
```python
def test_basic_query_returns_result():
    """Query com termo existente retorna resultado com confidence > 0."""

def test_empty_query_returns_missing():
    """Query sem match retorna status missing e confidence 0."""

def test_known_term_finds_correct_file():
    """Busca por 'harness' retorna artigo de harness, não outro."""

def test_index_file_is_read():
    """Tags do _index.md geram hits com peso 1.0."""

def test_json_output_is_valid():
    """Saída do Oracle é JSON válido com campos obrigatórios."""
```

#### Testes TARGET (escritos agora, marcados `xfail`, ativados fase a fase):
```python
@pytest.mark.xfail(reason="Fase 0.1: normalização pré-query não implementada")
def test_markdown_in_query():
    """Query com '**CI**' deve funcionar como 'CI'."""

@pytest.mark.xfail(reason="Fase 0.3: aliases não lidos")
def test_aliases_indexed():
    """Artigo com aliases no frontmatter deve ser encontrado por alias."""

@pytest.mark.xfail(reason="Fase 0.4: filtro 3+ mata siglas")
def test_siglas_2_chars():
    """Busca por 'QA' não deve retornar vazio."""

@pytest.mark.xfail(reason="Fase 0.5: exceções silenciosas")
def test_warnings_on_corrupt_file():
    """Arquivo corrompido deve gerar warning, não silêncio."""

@pytest.mark.xfail(reason="Fase 1.1: stemming não existe")
def test_stem_converges():
    """'testar', 'teste', 'testes' devem retornar o mesmo arquivo."""

@pytest.mark.xfail(reason="Fase 1.1: sem guarda de tamanho mínimo")
def test_stem_min_length():
    """'ação' não deve gerar stem de 1 caractere."""

@pytest.mark.xfail(reason="Fase 1.2: confidence não calibrado")
def test_confidence_calibrated():
    """Match por tag deve ter confidence > match por corpo acumulado."""

@pytest.mark.xfail(reason="Fase 1.3: Oracle retorna top-1")
def test_top_n_returns_multiple():
    """Query com 2 conceitos deve retornar >= 2 resultados."""

@pytest.mark.xfail(reason="Fase 0.2: regeneração não implementada")
def test_index_regeneration():
    """_index.md regenerado deve conter todos os artigos válidos."""
```
- **Isolamento (auditoria Qwen cirúrgica):** Testes NÃO devem ler/escrever no `.context/` real. Usar `tempfile.TemporaryDirectory()` como sandbox, copiar apenas `market/WIKI/`, `_index.md` e `_template.md`. Mockar `CONTEXT_DIR` via variável de ambiente.
- **Critério de sucesso:** Testes BASELINE passam no Oracle atual. A cada fase, remover o `xfail` do teste TARGET correspondente e confirmar que passa. Testes BASELINE nunca devem regredir.
- **Esforço:** 2-3h.

---

## 🔴 Fase 0: Corrigir o Que Está Quebrado (Antes de Otimizar)

Estas são falhas estruturais no Oracle atual, não otimizações.

### 0.1 Normalização pré-query
**Origem:** Qwen (auditoria — ponto cego que ninguém identificou nos relatórios).
- **O quê:** Criar `normalize_query()` que limpa markdown (`**`, `` ` ``, `#`, `[[]]`) e normaliza acentos antes de extrair keywords.
- **Por quê:** Queries com `**CI**` geram tokens fantasma. O Oracle perde antes de começar a buscar.
- **Esforço:** ~10 linhas.

### 0.2 Regenerar `_index.md` automaticamente
**Origem:** Opus (descoberta original — o índice aponta para `conceito_teste.md` que não existe; os 4 artigos reais não estão indexados).
- **O quê:** O `ingest_wiki_guard.py`, ao final de uma ingestão bem-sucedida, reconstrói o `_index.md` a partir dos frontmatters dos artigos válidos.
- **Pré-condição (auditoria MiMo):** A regeneração só executa **após** a validação de frontmatter (que o `ingest_wiki_guard.py` já faz). Isso resolve a circularidade: frontmatters são validados primeiro, o índice é gerado a partir de frontmatters válidos.
- **Robustez (auditoria Qwen):** Usar escrita atômica — gerar `_index.md.tmp` → `os.replace()`. Se o script crashar no meio, o índice antigo permanece intacto.
- **Esforço:** ~25 linhas.

### 0.3 Ler o campo `aliases` do frontmatter
**Origem:** Opus (o `_template.md` já define `aliases:` mas o `build_index()` ignora completamente).
- **O quê:** No `build_index()`, extrair o frontmatter de cada artigo e injetar os aliases como keywords com peso 0.7.
- **Por quê:** Sinonímia de domínio já está prevista na estrutura do template. Só falta o Oracle usá-la.
- **Esforço:** ~15 linhas.

### 0.4 Exceções para siglas de 2 caracteres
**Origem:** MiMo (descoberta original — o filtro `\b\w{3,}\b` mata silenciosamente QA, DB, CI, PR, OS).
- **O quê:** Manter o filtro de 3+ para indexação do corpo (evita preposições), mas não aplicar nas tags do `_index.md` nem no título. Ou manter uma lista de exceções de siglas de 2 chars relevantes ao domínio.
- **Por quê:** Se alguém busca "como configurar CI?", o Oracle ignora "CI" completamente. Sem warning, sem fallback. Bug silencioso.
- **Esforço:** ~10 linhas.

### 0.5 Parar de engolir exceções no `build_index`
**Origem:** MiMo (problema de robustez — `except Exception: continue` esconde arquivos corrompidos).
- **O quê:** Acumular warnings de arquivos ignorados e incluir um campo `"warnings"` na resposta JSON.
- **Por quê:** O agente recebe resultado parcial sem saber que parte do índice está incompleto.
- **Esforço:** ~10 linhas.

**✅ Checkpoint Fase 0:** Rodar `tests/test_oracle.py`. Todos os testes devem passar. Se algum falhar, corrigir antes de avançar.

---

## 🟡 Fase 1: Melhorar a Qualidade das Respostas

### 1.1 Stemming simplificado pt-BR
**Origem:** MiMo (proposta original com código completo).
- **O quê:** Implementar um `simple_stem()` baseado em sufixos para português. Aplicar tanto na indexação quanto na busca.
- **Por quê:** "testar", "teste" e "testes" são 3 tokens diferentes hoje. O Oracle não conecta "configurar" com "configuração". Em português a morfologia é rica demais para match exato funcionar bem.
- **Risco (auditoria MiMo):** Não é zero. Edge case: `"ação" → stem "a"` (stem inútil). O `simple_stem()` precisa de `len(stem) >= 3` como guarda.
- **Risco (auditoria Qwen):** Over-stemming: `"cartão" → "cart"`. Limitar a sufixos seguros. Manter match exato como fallback prioritário (se match exato bate, não aplicar stem).
- **Implementação (auditoria Qwen cirúrgica):** Usar dicionário mapeado `SAFE_SUFFIXES = {"ção": "", "mente": "", "ar": "a", ...}` com guarda `len(word) > 4 and len(stem) >= 3`. Manter whitelist de termos técnicos do projeto — se o termo estiver na whitelist, pular stemming.
- **Critério de sucesso:** `test_stem_converges()` e `test_stem_min_length()` passam.
- **Esforço:** 1-2h (inclui ajuste de edge cases).

### 1.2 Calibrar confidence (qualidade > quantidade)
**Origem:** MiMo (análise original — 5 matches de corpo (0.2×5=1.0) dão o mesmo confidence que 1 match determinístico (1.0)).
- **O quê:** Normalizar o confidence com: `0.7 * melhor_peso_individual + 0.3 * score_normalizado`.
- **Por quê:** O `min(1.0, score)` atual mascara a diferença entre match determinístico perfeito e acumulado acidental de corpo. O agente que recebe `confidence: 1.0` de ambos não consegue distinguir.
- **Critério de sucesso:** `test_confidence_calibrated()` passa — match por tag retorna confidence > match por corpo acumulado.
- **Esforço:** ~1h.

### 1.3 Retorno top-N em vez de top-1
**Origem:** MiMo (proposta original).
- **O quê:** Retornar até 3 arquivos acima de um threshold mínimo (0.5), em vez de forçar top-1.
- **Por quê:** Queries com 2 conceitos ("como mockar banco de dados?") forçam o Oracle a escolher um tema. Retornar 2-3 resultados permite que o agente tenha contexto complementar.
- **Integrado com:** Retorno graduado (Opus) — o top-1 recebe conteúdo completo, os demais recebem apenas `## Resumo`.
- **Guarda (auditoria Qwen):** Resumo truncado em 300 chars ou até a próxima `##` para evitar Context Bloat.
- **Hard limit (auditoria Qwen cirúrgica):** `total_chars <= 12000` por resposta. Resultados 2+ com `len(content) > 300` truncados com `[...]`.
- **Critério de sucesso:** `test_top_n_returns_multiple()` passa.
- **Esforço:** ~1h.

### 1.4 Schema de resposta estruturado
**Origem:** Qwen (Tool-Calling Schema) + Flash (flag `outside_role_scope`) + MiMo (campo `warnings`).
- **O quê:** Padronizar a resposta para:
```json
{
  "schema_version": "v3",
  "status": "found | partial | missing",
  "results": [
    {"path": "...", "confidence": 0.85, "content": "..."}
  ],
  "match_quality": 0.7,
  "outside_role_scope": false,
  "aliases_matched": ["checkout", "pagamento"],
  "warnings": []
}
```
- **Versionamento (auditoria Qwen cirúrgica):** O campo `schema_version` permite que scripts legados detectem o formato sem quebrar. No `wiki_log_utils.py`, adicionar fallback: `confidence = results[0]["confidence"] if isinstance(results, list) else response.get("confidence")`.
- **Descartado:** O campo `fallback_hint` proposto pelo Qwen. Informação genérica tipo "consulte SSOT_MAP" não ajuda o agente.
- **Impacto em chamadores (auditoria MiMo):** Esta é uma mudança de contrato. Afeta: `query_oracle()`, `wiki_log_utils.py` (formato do log), `PROMPT_LIBRARY.md` (agentes precisam do novo schema). Estimar como 2-3h, não 30min.
- **Esforço:** 2-3h (refatoração + atualização de chamadores).

**✅ Checkpoint Fase 1:** Rodar `tests/test_oracle.py`. Todos os testes (anteriores + novos) devem passar.

---

## 🟢 Fase 2: Integração Sistêmica

### 2.1 Busca imparcial (sem multiplicador de Role)
**Origem:** Flash + Usuário (decisão definitiva — análise do viés declarativo).
- **Regra:** A busca é 100% imparcial. A role é usada **apenas** para gerar a flag `outside_role_scope` na resposta. O Oracle informa, o agente decide.
- **Implementação:** Após o `hits.most_common()`, comparar o domínio do resultado com o domínio esperado da role. Sem multiplicadores.
- **Nota (auditoria Qwen):** `outside_role_scope` é `info-only`. Nunca filtrar resultados por role. O agente pode precisar de contexto transversal.

### 2.2 Log fire-and-forget
**Origem:** MiMo (problema de robustez — o spin lock do `wiki_log` pode travar o Oracle por 5 segundos).
- **O quê:** Envolver o `append_to_wiki_log` em try/except no `query_oracle`. Se o lock falha, o Oracle retorna o resultado mesmo assim.
- **Por quê:** O log é secundário à resposta. Bloquear a resposta por causa de um lock de log é inversão de prioridades.
- **Esforço:** ~3 linhas.

### 2.3 Integração via PROMPT_LIBRARY.md
**Origem:** MiMo (insight de design — o Oracle é "disponível" mas não "obrigatório").
- **O quê:** Adicionar nos templates de prompt dos agentes a instrução de consultar o Oracle antes de responder sobre padrões ou convenções do projeto. Se `confidence >= 0.6`, usar o resultado; se `< 0.6`, registrar a query para análise futura.
- **Por quê:** Hoje o agente só consulta o Oracle se alguém lembrar. Isso transforma o Oracle de ferramenta passiva em passo do workflow.
- **Esforço:** Edição de texto no `PROMPT_LIBRARY.md`.

### 2.4 Cache com invalidação por mtime (persistido em disco)
**Origem:** Qwen (proposta técnica) + MiMo (implementação) + Qwen (auditoria — **correção crítica**).
- **⚠️ Correção da auditoria Qwen:** Cache in-memory é inútil. O Oracle roda como CLI script e morre após cada execução. `_cache = {}` reseta a cada chamada. O cache **deve ser persistido em disco**.
- **O quê:** Persistir em `.context/market/.wiki_index.cache.json`. Invalidar apenas se `max(mtime(WIKI/*.md)) > cache_built_at`.
- **Race condition (auditoria Qwen cirúrgica):** Duas execuções simultâneas do Oracle podem sobrescrever o cache. Usar `tempfile + os.replace()` na escrita (padrão já usado no `purge_journal.py`). Validar `mtime` antes de ler o JSON.
- **Escopo de invalidação (auditoria Qwen):** Restringir a `market/WIKI/**/*.md` e `_index.md`. Ignorar `RAW/`, logs.
- **Aceito com ressalva:** No template atual (4 artigos), o ganho é imperceptível. Implementar quando o template for usado em projetos com >20 artigos.
- **Esforço:** ~30 linhas (persistência em JSON).

### 2.5 `oracle_analytics.py` (Feedback Loop)
**Origem:** MiMo (insight original — o `wiki_log.md` é uma mina de ouro inexplorada).
- **O quê:** Script que lê o `wiki_log.md` e gera:
  - Queries que falharam (confidence < 0.5) → gaps no `_index.md`
  - Queries repetidas → temas que precisam de mais cobertura
  - Queries limítrofes (0.5–0.7) → discriminação fraca do scoring
- **Robustez (auditoria Qwen):** Se o formato do `wiki_log.md` mudar, o parser deve logar `[WARN]` e pausar, não quebrar silenciosamente.
- **Parser (auditoria Qwen cirúrgica):** Usar regex estrito `r"\| \[(.+?)\] \| QUERY \| .+conf: ([0-9.]+) .+ \| (OK|FAIL) \|"`. Ignorar linhas sem match em vez de crashar.
- **Monitoramento (auditoria Qwen):** Nas 50 primeiras queries, se >30% falharem → gap no `_index.md`. Se <10% falharem mas confidence média for 0.55 → calibração muito agressiva.
- **Esforço:** ~50 linhas.

### 2.6 Gate Epistemológico (Oracle como Pré-Gate do Harness)
**Origem:** Qwen (proposta) + Flash + Usuário (restrição operacional).
- **⚠️ DIRETRIZ DO USUÁRIO (INEGOCIÁVEL):** Deve iniciar em **Modo Light**. Apenas avisa. Nunca bloqueia. O humano não pode ser forçado a parar para fazer deep research só para preencher uma tag.
- **Implementação futura:** Quando ativado, o Harness consulta o Oracle com os termos-chave da Spec. Se `confidence < 0.4` para um termo crítico, gera um `[WARN]` no log, não um `Exit 1`.
- **Dependência (auditoria MiMo):** O Harness passa a depender do Oracle. Se o Oracle estiver lento/quebrado, o Harness é afetado. **Obrigatório:** timeout de 2 segundos. Se o Oracle não responder, o check é skipado, não travado.
- **Transição para Strict:** Apenas por decisão explícita do arquiteto, nunca automática.

### 2.7 Fallback para NotebookLM
**Origem:** Opus (proposta original baseada na hierarquia do SSOT_MAP.md).
- **O quê:** Quando a Wiki local retorna `confidence < 0.5`, o Oracle pode opcionalmente consultar o NotebookLM via MCP (`mcp_notebooklm_chat_with_notebook`) usando o `oracle_mcp_id` do `SSOT_MAP.md`.
- **Condição:** Só funciona se o MCP estiver configurado e o ID do notebook for válido.
- **Esforço:** Médio (~40 linhas + tratamento de fallback).
- **Usuário:** O usuário não quer isso agora, só vale a pena quando muitas outras coisas estiverem funcionando.

---

## ❌ O Que Foi Descartado (e Por Quê)

| Proposta | Origem | Motivo do Descarte |
|:---|:---|:---|
| Multiplicadores por Role | Qwen (Item 3.2) | Gera viés declarativo deletério na ambiguidade (análise do Flash). |
| Chunking genérico por headings | Qwen (Item 2.3) | O template já define `## Resumo` como seção obrigatória. Usar isso é mais simples. |
| `match_quality` como substituto de calibração | Opus | A calibração do MiMo (qualidade > quantidade) é mais elegante. `match_quality` permanece como complemento. |
| Consistência de Intenção via LLM | MiMo-estratégico (Item 2.B) | Viola a restrição `stdlib-only` e introduz não-determinismo no pipeline. |
| Impact-Aware Harness | MiMo-estratégico (Item 3) | Ideia boa mas pertence ao Harness, não ao Oracle. Guardada em `relatorio_insights_context.md`. |
| `DECISIONS.md` separado | MiMo-estratégico (Item 4.1) | O Journal já cumpre esse papel. Arquivo extra seria duplicação. |
| Popular Wiki com Bootstrap genérico | Insights anteriores | O template é um molde vazio por design. Wiki só faz sentido com domínio concreto. |
| Cache in-memory | Qwen + MiMo (corrigido pela auditoria Qwen) | CLI scripts morrem após execução. Cache in-memory é placebo. Persistir em disco. |

---

## 📅 Roadmap de Execução

| Ordem | Entrega | Origem | Esforço | Risco | Critério de Sucesso |
|:---|:---|:---|:---:|:---:|:---|
| **0** | **`test_oracle.py`** (suíte de testes) | MiMo (auditoria) | 2-3h | Zero | Testes passam no Oracle atual |
| **1** | Normalização pré-query | Qwen (auditoria) | 30min | Zero | Query com `**CI**` retorna mesmo que `CI` |
| **2** | Fix `_index.md` (regeneração atômica) | Opus + Qwen (auditoria) | 1-2h | Zero | `test_index_regeneration()` passa |
| **3** | Leitura de `aliases` do frontmatter | Opus | 1h | Zero | `test_aliases_indexed()` passa |
| **4** | Exceções para siglas de 2 chars | MiMo | 30min | Zero | `test_siglas_2_chars()` passa |
| **5** | Parar de engolir exceções + campo `warnings` | MiMo | 30min | Zero | `test_warnings_on_corrupt_file()` passa |
| — | **✅ Checkpoint Fase 0** | | | | Todos os testes passam |
| **6** | Stemming simplificado pt-BR | MiMo | 1-2h | Baixo | `test_stem_converges()` + `test_stem_min_length()` |
| **7** | Calibração de confidence | MiMo | 1h | Baixo | `test_confidence_calibrated()` passa |
| **8** | Retorno top-N + graduado | MiMo + Opus | 1h | Baixo | `test_top_n_returns_multiple()` passa |
| **9** | Schema de resposta estruturado | Qwen + Flash + MiMo | 2-3h | Médio | Chamadores atualizados, testes passam |
| — | **✅ Checkpoint Fase 1** | | | | Todos os testes passam |
| **10** | Busca imparcial + `outside_role_scope` | Flash + Usuário | 1h | Zero | Query por termo fora do domínio da role retorna resultado + flag `true` |
| **11** | Log fire-and-forget | MiMo | 15min | Zero | Oracle retorna em <100ms mesmo com `wiki_log.lock` presente |
| **12** | Integração via PROMPT_LIBRARY | MiMo | 30min | Zero | Prompts dos agentes-chave contêm instrução de consulta ao Oracle |
| **13** | Cache em disco (`.json`) + mtime | Qwen (auditoria) | 2h | Baixo | 2ª query consecutiva sem mudanças na Wiki é <5ms |
| **14** | `oracle_analytics.py` | MiMo | 2h | Baixo | Roda sem erro no `wiki_log.md` atual e gera relatório com 3 métricas |
| **15** | Gate Epistemológico (Modo Light + timeout 2s) | Qwen + Flash + Usuário | 3h | Médio | Harness gera `[WARN]` para termos ausentes; timeout de 2s funciona |
| **16** | Fallback NotebookLM (adiado) | Opus | 3h | Médio | Query local com conf<0.5 consulta MCP e retorna resultado enriquecido |

**Estimativa total:** ~25-30h de trabalho, stdlib-only, sem breaking changes.
*(Corrigida de ~20h para ~25-30h conforme auditoria MiMo: inclui testes, iteração de edge cases, e validação entre fases.)*

---

> **Filosofia deste plano:** Consertar primeiro. Calibrar depois. Integrar por último. Nunca bloquear o humano.
>
> **Filosofia de execução:** Testar antes de mudar. Mudar uma coisa por vez. Rodar testes após cada mudança. Se regrediu, reverter antes de avançar.
