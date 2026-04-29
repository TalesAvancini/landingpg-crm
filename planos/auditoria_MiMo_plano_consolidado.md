# 🔎 Auditoria Crítica do Plano Consolidado Oracle v3

> **Autor:** MiMo (Auditor)
> **Alvo:** `plano_consolidado_Oracle_v3.md`
> **Data:** 2026-04-28

---

## O que está bem

**A tabela de descartes é a parte mais valiosa do documento.** Saber o que não fazer e por quê economiza mais tempo do que saber o que fazer. A rejeição do multiplicador por role, do chunking genérico, e da consistência de intenção via LLM mostra discernimento.

**A filosofia final ("Consertar primeiro. Calibrar depois. Integrar por último. Nunca bloquear o humano.")** é excelente e deveria ser o headline do documento, não uma nota no rodapé.

**A ordem do roadmap está correta.** Fase 0 antes da Fase 1, Fase 1 antes da Fase 2. Dependências respeitadas.

---

## O que precisa de crítica

### 1. A Fase 0.1 tem um problema de circularidade

> "O `ingest_wiki_guard.py`, ao final de uma ingestão bem-sucedida, reconstrói o `_index.md` a partir dos frontmatters dos artigos válidos."

Isso assume que os artigos têm frontmatters bem formados com tags. Mas se o `_index.md` está quebrado hoje (apontando para `conceito_teste.md` que não existe), quem garante que os frontmatters dos artigos existentes estão corretos? Se o `ingest_wiki_guard.py` regenerar o `_index.md` a partir de frontmatters incompletos ou mal formatados, ele vai gerar um `_index.md` novo mas igualmente ruim.

**Antes de regenerar automaticamente, precisa validar que os frontmatters de origem estão corretos.** Caso contrário, automatiza a geração de lixo.

### 2. O item 1.1 (stemming) merece um teste antes de confiar

O código de stemming proposto pelo MiMo (que eu mesmo forneci) é heurístico. Funciona para casos comuns, mas tem edge cases reais em português:

- "configuração" → stem "configura" (ok)
- "configurações" → stem "configura" (ok)
- "testagem" → stem "test" (ok)
- "sugestão" → stem "sugest" (ok)
- Mas: "informação" → stem "inform" — e "informar" → stem "inform" (ok, convergem)
- Problema: "ação" → stem "a" (3 chars, mas "a" é meaningless como stem)

O sufixo "ção" corta "ação" para "a", que é um stem inútil. O código precisa de uma verificação de comprimento mínimo do stem resultante (ex: `len(stem) >= 2`).

**Não é um blocker, mas precisa de uma suíte de testes antes de confiar.** O plano trata como "1h, risco zero" — não é zero.

### 3. Fase 1.4 (schema estruturado) é maior que o estimado

> "Refatoração da função `query_oracle()`, ~30 linhas."

Refatorar o retorno de uma função de "dicionário simples" para "schema estruturado com múltiplos resultados, warnings, aliases_matched, outside_role_scope" não são 30 linhas. É uma mudança de contrato que afeta:

- A própria função `query_oracle()`
- Todos os chamadores (scripts que consomem o resultado)
- O `wiki_log_utils.py` (que loga a query — o formato do log muda)
- O PROMPT_LIBRARY.md (agentes precisam saber o novo schema)
- Testes (se existirem)

O esforço real é mais próximo de **2-3 horas** do que 30 minutos. Não é um problema, mas a estimativa está subdimensionada.

### 4. O item 2.6 (Gate Epistemológico) tem uma contradição interna

> "Quando ativado, o Harness consulta o Oracle com os termos-chave da Spec. Se confidence < 0.4 para um termo crítico, gera um [WARN] no log, não um Exit 1."

Mas o Harness já tem 6 checks. Adicionar mais um check (que consulta o Oracle) significa que o `harness_runner.py` agora depende do `context_oracle.py`. Essa dependência não existia antes. Se o Oracle estiver lento, com erro, ou com o índice quebrado, o Harness também é afetado.

O plano diz "Modo Light, apenas avisa" — mas mesmo em modo light, se o Oracle demora 5 segundos por causa do lock do wiki_log (ironicamente, o problema que o item 2.2 resolve), o Harness fica mais lento.

**A dependência precisa ser explícita e com timeout.** Se o Oracle não responder em 2 segundos, o check é skipado, não travado.

### 5. O plano não define critérios de sucesso

Há 15 itens no roadmap. Nenhum tem um critério de "como sei que funcionou". Exemplos:

- **Steming (item 5):** "Melhora o recall" — como mede? Quantas queries que falhavam agora acertam?
- **Top-N (item 7):** "Queries com 2 conceitos recebem contexto complementar" — como valida? Quais queries de teste?
- **Oracle analytics (item 13):** "Revela gaps no _index.md" — como sabe que os gaps revelados são reais e não falsos positivos?

Sem critérios de sucesso, o plano vira uma checklist de "implementei" sem saber se melhorou. E com 15 itens, a probabilidade de implementar algo que não melhora nada é alta.

### 6. A estimativa de ~20h é otimista demais

O roadmap soma os esforços individuais. Mas não conta:

- **Testes entre fases** (validar que Fase 0 não quebrou nada antes de ir para Fase 1)
- **Refatorização de código existente** (o `context_oracle.py` vai mudar significativamente — regressões são prováveis)
- **Iteração** (o primeiro código de stemming vai ter bugs, a primeira calibração de confidence vai precisar de ajuste)

Estimativa realista: **30-35h**. Não é um problema — é um bom investimento. Mas é melhor saber a realidade agora do que descobrir na hora 20 que falta metade.

### 7. Falta o item mais importante de todos

O plano não inclui **testes automatizados para o Oracle**. Há 15 itens de mudança no motor de busca, e nenhum deles menciona uma suíte de validação.

O mínimo necessário:

```python
# test_oracle.py
def test_stem_converges():
    """'testar', 'teste', 'testes' devem retornar o mesmo arquivo."""

def test_siglas_2_chars():
    """Busca por 'QA' não deve retornar vazio."""

def test_top_n_returns_multiple():
    """Query com 2 conceitos deve retornar >= 2 resultados."""

def test_confidence_calibrated():
    """Match por tag deve ter confidence > match por corpo."""

def test_index_regeneration():
    """_index.md regenerado deve conter todos os artigos válidos."""

def test_aliases_indexed():
    """Artigo com aliases no frontmatter deve ser encontrado por alias."""

def test_warnings_on_corrupt_file():
    """Arquivo corrompido deve gerar warning, não silêncio."""
```

Sem isso, cada item do roadmap é um tiro no escuro. Com isso, cada item é uma hipótese testável.

---

## Resumo

| Aspecto | Avaliação |
|---|---|
| Estrutura do plano | Excelente — fases bem separadas, dependências respeitadas |
| Tabela de descartes | A melhor parte — decisões claras e justificadas |
| Estimativas de esforço | Subdimensionadas em ~40% |
| Critérios de sucesso | Ausentes — o maior gap do documento |
| Testes automatizados | Ausentes — risco real de regressão |
| Dependências entre componentes | Subestimadas (Oracle → Harness, schema → chamadores) |
| Filosofia final | Correta e bem articulada |

**Veredicto:** O plano é executável e a direção está certa. Antes de começar, adicione: (1) uma suíte de testes do Oracle com 10-15 queries de validação, (2) critérios de sucesso mensuráveis para os itens 1-8, e (3) revise as estimativas para cima. Com esses três ajustes, o plano fica sólido.
