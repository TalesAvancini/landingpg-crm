# Relatório Técnico: Otimizações e Insights para o Oracle

Análise focada exclusivamente na **mecânica, performance e qualidade operacional** do `context_oracle.py` como ferramenta de busca.

---

## 1. Diagnóstico do Estado Atual

O Oracle é um motor de busca léxico com dois índices sobrepostos:

```
Índice Determinístico (_index.md) → peso 1.0 por tag
Índice Léxico (dinâmico)          → título: 0.8, título palavra: 0.6,
                                     stem: 0.5, corpo: 0.2
```

O fluxo atual:
1. Recebe uma query como string
2. Extrai keywords com `r'\b\w{3,}\b'`
3. Busca nos dois índices
4. Acumula pesos por arquivo
5. Retorna o top-1 com score >= 0.6

**Funciona.** Mas há pontos cegos importantes.

---

## 2. Problemas Estruturais

### 2.1 O filtro de 3+ caracteres é arbitrário e silencioso

```python
words = re.findall(r'\b\w{3,}\b', text.lower())
```

Isso descarta silenciosamente termos de 1-2 caracteres. Na prática:

| Termo | Caracteres | Capturado? |
|---|---|---|
| QA | 2 | **Não** |
| DB | 2 | **Não** |
| OS | 2 | **Não** |
| API | 3 | Sim |
| TDD | 3 | Sim |
| CI | 2 | **Não** |
| PR | 2 | **Não** |

O problema não é só perder termos — é que o **usuário não sabe que perdeu**. Se alguém busca "como configurar CI?", o Oracle ignora "CI" completamente. Não há warning, não há fallback. Simplesmente não matcheia.

**Solução:** Mantenha o filtro de 3+ para indexação do corpo (evita ruído de artigos e preposições), mas **não aplique** o filtro nas tags do `_index.md` nem no título. Ou, alternativemente, tenha uma lista de exceções de siglas de 2 caracteres que são relevantes ao domínio.

### 2.2 Busca léxica sem normalização morfológica

```python
# Indexação
words = re.findall(r'\b\w{3,}\b', text.lower())

# Busca
keywords = set(re.findall(r'\b\w{3,}\b', question.lower()))
```

A busca é por **match exato de token**. Isso significa:

- "testar" e "teste" e "testes" são tokens diferentes
- "configurar" e "configuração" não se conectam
- "mockar" e "mock" e "mocking" são universos separados

Em português, isso é especialmente problemático porque a morfologia é rica: verbos conjugados, plurais, femininos — todos geram tokens diferentes da forma base.

**Solução prática sem dependências externas:** Implementar um stemming simplificado para português. Não precisa ser perfeito — mesmo uma abordagem baseada em sufixos cobre 80% dos casos:

```python
def simple_stem(word):
    """Stemming heurístico para português (stdlib only)."""
    suffixes = [
        'ando', 'endo', 'indo',  # gerúndio
        'ar', 'er', 'ir',        # infinitivo
        'ou', 'eu', 'iu',        # pretérito
        'ção', 'ções',           # substantivos
        'mente',                  # advérbios
        'dade', 'dades',         # substantivos
        'oso', 'osa', 'osos', 'osas',  # adjetivos
        'ando', 'endo',
        'es', 'as', 'os',        # plurais
        'ado', 'ida',            # particípios
        'mente',
    ]
    for s in sorted(suffixes, key=len, reverse=True):
        if word.endswith(s) and len(word) - len(s) >= 3:
            return word[:-len(s)]
    return word
```

Aplicar isso **tanto na indexação quanto na busca** faz "testar", "teste", "testes" convergirem para o stem "test". Melhora significativamente o recall sem adicionar dependências.

### 2.3 O score de confiança não é calibrado

```python
"confidence": min(1.0, score)
```

O score é a soma bruta dos pesos. Veja os cenários possíveis:

| Cenário | Fontes | Score | Confidence |
|---|---|---|---|
| Match determinístico perfeito | tag (1.0) | 1.0 | 1.0 |
| Match por título + stem | título (0.8) + stem (0.5) | 1.3 | 1.0 (capped) |
| Match por 5 palavras no corpo | 5 × corpo (0.2) | 1.0 | 1.0 |
| Match acidental por 3 palavras | 3 × corpo (0.2) | 0.6 | 0.6 |

O problema: um match por 5 palavras no corpo (relevância baixa) tem o **mesmo confidence** que um match determinístico perfeito. O `min(1.0, score)` mascara a diferença.

**Solução:** Normalizar o confidence com uma função que reflita a **qualidade** do match, não apenas a quantidade:

```python
def calibrate_confidence(hits):
    """Pondera confiança pela qualidade das fontes, não só pelo acumulado."""
    if not hits:
        return 0.0
    
    top_file, raw_score = hits.most_common(1)[0]
    
    # Detectar a melhor fonte individual
    best_source_weight = max(
        (m["weight"] for path, matches in ... for m in matches if path == top_file),
        default=0.0
    )
    
    # Confidence = 70% melhor fonte + 30% score normalizado
    normalized = min(1.0, raw_score / 3.0)  # 3.0 como teto razoável
    confidence = 0.7 * best_source_weight + 0.3 * normalized
    
    return round(confidence, 2)
```

Isso faz com que um match por tag (peso 1.0) sempre tenha confidence alto, e matches por corpo acumulado tenham confidence moderado mesmo com score alto.

### 2.4 Retorno de arquivo único limita queries complexas

```python
top_file, score = hits.most_common(1)[0]
```

Queries que envolvem dois conceitos (ex: "como mockar banco de dados?") forçam o Oracle a escolher **um** dos dois temas. O arquivo sobre mocks e o arquivo sobre banco de dados competem, e apenas um vence.

**Solução:** Retornar top-N com threshold de relevância:

```python
def get_relevant_files(hits, min_score=0.5, max_results=3):
    """Retorna os N arquivos mais relevantes acima do threshold."""
    results = []
    for path, score in hits.most_common():
        if score < min_score:
            break
        results.append({"path": path, "score": score})
        if len(results) >= max_results:
            break
    return results
```

Isso permite que o agente receba **contexto complementar** quando a pergunta é multidimensional.

### 2.5 A heurística de build_index é recalcada a cada query

```python
def query_oracle(question, role="unknown"):
    idx = build_index()       # ← reindexa tudo toda vez
    det_idx = load_index_file()  # ← relê o _index.md toda vez
```

Cada chamada ao Oracle:
1. Varre recursivamente todos os `.md` em `market/WIKI/` e `market/compliance/`
2. Lê cada arquivo inteiro
3. Extrai palavras, stems, títulos
4. Monta o dicionário de índice

Para uma base pequena (5-10 arquivos), isso é imperceptível. Mas se a WIKI crescer para 30-50 arquivos, cada query vai reler tudo.

**Solução:** Cache com invalidação baseada em mtime:

```python
import os

_cache = {"index": None, "mtime": 0}

def get_index():
    """Retorna índice com cache baseado em mtime do diretório WIKI."""
    wiki_dir = CONTEXT_DIR / "market" / "WIKI"
    
    # Mtime do diretório muda quando arquivos são adicionados/modificados
    current_mtime = max(
        os.path.getmtime(f) 
        for f in wiki_dir.rglob("*.md")
    ) if wiki_dir.exists() else 0
    
    if _cache["index"] is not None and _cache["mtime"] == current_mtime:
        return _cache["index"]
    
    _cache["index"] = build_index()
    _cache["mtime"] = current_mtime
    return _cache["index"]
```

Isso mantém a simplicidade (sem Redis, sem SQLite) mas evita reindexação desnecessária.

---

## 3. Problemas de Robustez

### 3.1 Silêncio em caso de erro

```python
except Exception:
    continue
```

O `build_index` engole exceções silenciosamente. Se um arquivo `.md` estiver corrompido, com encoding inválido, ou com permissão negada, o Oracle simplesmente pula sem avisar. O agente recebe um resultado parcial sem saber que parte do índice está incompleto.

**Solução:** Acumular warnings e incluir no resultado:

```python
warnings = []

for p in search_dir.rglob("*.md"):
    try:
        # ... indexação normal ...
    except Exception as e:
        warnings.append(f"Arquivo ignorado: {p.name} ({e})")

# No resultado final:
return {
    "answer": ...,
    "confidence": ...,
    "sources": ...,
    "warnings": warnings  # ← novo campo
}
```

### 3.2 O lock do wiki_log pode bloquear o Oracle

O `append_to_wiki_log` usa spin lock com timeout de 5 segundos. Se outro processo está escrevendo no log, o Oracle **espera até 5 segundos** antes de retornar. Em um fluxo de múltiplos agentes, isso pode gerar latência cumulativa.

**Solução:** Log do Oracle deveria ser **fire-and-forget** — se o lock falha, o Oracle retorna o resultado mesmo assim. O log é secundário à resposta.

```python
# No query_oracle, em vez de:
append_to_wiki_log("QUERY", ...)

# Usar:
try:
    append_to_wiki_log("QUERY", ...)
except:
    pass  # Log é best-effort, não bloqueia a resposta
```

### 3.3 Ausência de validação de integridade do _index.md

O `load_index_file()` assume que o `_index.md` está bem formado. Se alguém editar manualmente e quebrar o padrão de tags:

```markdown
- [[testing/foo]] | tags:     ← tag vazia
- [[testing/bar]] | tags: t1,  ← trailing comma
```

O Oracle vai indexar tags vazias ou criar matches inválidos. Sem validação, isso se manifesta como resultados errados sem explicação.

**Solução:** Um lint simples no `_index.md` (o `lint_wiki.py` já existe — verificar se valida isso).

---

## 4. Insights de Design

### 4.1 O Oracle é RAG sem vetor — e isso é uma feature

Em um mundo obcecado por embeddings e bancos vetoriais, o Oracle faz busca lexical com pesos manuais. Isso parece primitivo, mas tem vantagens reais:

- **Determinístico**: mesma query, mesmo resultado, sempre
- **Auditável**: você pode inspecionar exatamente por que um arquivo foi retornado
- **Zero dependências**: funciona com stdlib Python, sem APIs externas
- **Rápido**: não precisa carregar modelos nem fazer chamadas de rede

O trade-off é recall menor (não captura sinônimos nem semântica). Mas para uma base de conhecimento **curada e pequena** (< 50 arquivos), a abordagem lexical com tags determinísticas é suficiente. O _index.md funciona como um "vetor manual" — alguém decidiu que o termo X mapeia para o arquivo Y.

**Insight:** Não tente transformar o Oracle em algo que ele não é. Em vez de adicionar embeddings, invista em **melhorar a curadoria do _index.md** e o **stemming**. Para o tamanho da base que você tem, isso dá mais retorno.

### 4.2 O _index.md é o ponto de alavancagem máximo

Toda a inteligência do Oracle está concentrada em dois lugares:
1. O algoritmo de scoring (código)
2. As tags no `_index.md` (curadoria humana)

O algoritmo é difícil de mudar sem efeitos colaterais. Mas as tags são **fáceis de ajustar e imediatas no efeito**. Cada tag adicionada ao _index.md é peso 1.0 puro — é o sinal mais forte que o Oracle tem.

**Insight:** Trate o _index.md como um **documento vivo**. Quando perceber que o Oracle está errando, a primeira pergunta não deve ser "como melhoro o algoritmo?" mas sim "que tag está faltando no _index.md?".

### 4.3 O wiki_log é uma mina de ouro inexplorada

O `wiki_log.md` registra toda query que passa pelo Oracle, com timestamp, modo, descrição e status (OK/FAIL). Mas ninguém analisa esse log.

**Insight:** Um script simples `oracle_analytics.py` que lê o wiki_log.md e gera:

- **Queries que falharam** (confidence < 0.5): revelam gaps no _index.md
- **Queries repetidas**: revelam temas que precisam de mais cobertura
- **Queries com confidence limítrofe** (0.5-0.7): revelam onde a discriminação está fraca

Esse feedback loop transforma o Oracle de ferramenta estática em ferramenta que **melhora com o uso**. Cada query falhada é um sinal de que algo está faltando — seja uma tag, um arquivo, ou um ajuste no scoring.

### 4.4 A integração com agentes é o gargalo real

O Oracle funciona bem como script standalone. Mas para ser o "melhor bibliotecário do mundo", ele precisa ser **consultado automaticamente**. Hoje, um agente só consulta o Oracle se alguém lembrar de mandar.

**Insight:** O ponto de integração mais de impacto é o **PROMPT_LIBRARY.md**. Se os prompts dos agentes incluírem algo como:

```
Antes de responder sobre práticas, padrões ou convenções do projeto, 
consulte o Oracle: python context_oracle.py "sua pergunta"
Se confidence >= 0.6, use o resultado como base.
Se confidence < 0.6, responda com seu conhecimento mas registre a query.
```

Isso transforma o Oracle de "ferramenta disponível" em "passo obrigatório do workflow".

---

## 5. Resumo de Prioridades

| Prioridade | Otimização | Esforço | Impacto |
|---|---|---|---|
| **Crítica** | Stemming simplificado pt-BR | Baixo | Alto — resolve o problema de morfologia |
| **Crítica** | Calibrar confidence (qualidade > quantidade) | Baixo | Alto — resultados mais confiáveis |
| **Alta** | Retornar top-N em vez de top-1 | Baixo | Alto — suporta queries complexas |
| **Alta** | Integração via PROMPT_LIBRARY | Baixo | Alto — torna o Oracle parte do fluxo |
| **Alta** | Exceções para siglas de 2 chars (QA, DB, CI) | Baixo | Médio — evita perda silenciosa |
| **Média** | Cache de índice por mtime | Baixo | Médio — performance com WIKI grande |
| **Média** | Log fire-and-forget | Baixo | Médio — evita latência por lock |
| **Média** | Warnings no resultado (erros de arquivo) | Baixo | Médio — transparência |
| **Média** | Analytics do wiki_log | Médio | Médio — feedback loop |
| **Baixa** | Validação do _index.md (lint) | Baixo | Baixo — já tem lint_wiki.py |

O padrão que emerge: **a maioria das otimizações de alto impacto é de baixo esforço**. O Oracle está a poucos ajustes de ser significativamente melhor. O que falta não é arquitetura — é calibração.
