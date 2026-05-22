# Auditoria de Execucao + Mini-Spec
## Opcao 5 - Recomendacao (Proposta B + elementos da A)

## 1) Objetivo operacional
Implementar um calculo de blast radius hibrido (estrutural + governanca) para substituir a leitura manual extensa de `rx-communications.md` no Step 2 do `journal-sync`, reduzindo ruido e aumentando precisao da propagacao.

---

## 2) Escopo imediato (MVP)
1. Criar `.context/_scripts/blast_radius.py`
2. Atualizar `.agent/skills/journal-sync/SKILL.md` (Step 2) para usar o script
3. Garantir atualizacao do grafo (`graphify update .`) no fluxo escolhido (hook ou comando explicito)
4. Registrar no glossario e no mapa de comunicacoes

Fora do escopo imediato:
- Integracao ativa do affinity-lite no fluxo de propagacao
- Substituicao completa de `rx-communications.md` como SSOT

---

## 3) Auditoria: lacunas que precisam detalhamento
1. Contrato de I/O do `blast_radius.py` nao definido
2. Regras de classificacao (`must_update`, `likely_update`, `declared_only`) ainda genericas
3. Politica de falha/fallback nao definida (sem graph, graph desatualizado, parse parcial)
4. Estrategia de atualizacao do graphify sem criterio de custo/timeout
5. Criterios de aceite e metricas de sucesso nao formalizados
6. Testes minimos e cenarios de borda nao especificados

---

## 4) Mini-spec do `blast_radius.py`

### 4.1 Interface (CLI)
Exemplo:
`python .context/_scripts/blast_radius.py --changed fileA.py fileB.md --graph graphify-out/graph.json --rx .context/maintenance/rx-communications.md --depth 2 --format json`

Parametros:
- `--changed` (obrigatorio): lista de arquivos alterados (seed)
- `--graph` (opcional, default: `graphify-out/graph.json`)
- `--rx` (opcional, default: `.context/maintenance/rx-communications.md`)
- `--depth` (opcional, default: `2`)
- `--format` (opcional: `json|text`, default: `json`)

Exit codes:
- `0`: sucesso
- `2`: input invalido
- `3`: graph indisponivel
- `4`: parse rx indisponivel
- `5`: erro interno

### 4.2 Saida (JSON canonico)
```json
{
  "seed": ["fileA.py", "fileB.md"],
  "must_update": [
    {"file":"SCRIPT_GLOSSARY.md","reasons":["graph","governance"],"priority":100}
  ],
  "likely_update": [
    {"file":"rx-anatomy.md","reasons":["graph"],"priority":70}
  ],
  "declared_only": [
    {"file":"HARNESS_LOG.md","reasons":["governance"],"priority":60}
  ],
  "meta": {
    "graph_depth": 2,
    "graph_edges_considered": ["calls","references","implements","contains","defines"],
    "warnings": []
  }
}
```

### 4.3 Regras de classificacao
- `must_update`: arquivo presente em ambos os conjuntos (estrutural intersecao governanca)
- `likely_update`: somente estrutural (estrutural - governanca)
- `declared_only`: somente governanca (governanca - estrutural)

### 4.4 Priorizacao (MVP simples)
- Base por bucket:
  - `must_update`: 100
  - `likely_update`: 70
  - `declared_only`: 60
- Ajustes:
  - +10 se distancia no grafo = 1
  - +5 por multiplos caminhos independentes
- Ordenacao final: `priority desc`, depois nome do arquivo

### 4.5 Algoritmo (MVP)
1. Normalizar `seed`
2. Carregar `graph.json`
3. Extrair vizinhos por BFS (depth configuravel), usando edges permitidas
4. Parsear adjacencia relevante de `rx-communications.md`
5. Construir conjuntos `structural` e `governance`
6. Classificar em 3 buckets
7. Atribuir prioridade, deduplicar e emitir saida

---

## 5) Politica de falha e degradacao
1. Sem `graph.json`:
   - modo degradado: usar somente governanca
   - incluir warning: `graph_unavailable`
2. Parse parcial de `rx-communications.md`:
   - usar somente estrutural
   - warning: `rx_parse_partial`
3. Sem ambos:
   - falha hard (exit != 0), com instrucao de recuperacao
4. `journal-sync` deve registrar no log qual modo foi usado

---

## 6) Contrato de integracao com `journal-sync` (Step 2)
Novo fluxo do Step 2:
1. Coletar Propagation Seed (git status)
2. Executar `blast_radius.py`
3. Consumir buckets:
   - `must_update`: obrigatorio revisar/atualizar ou justificar explicitamente
   - `likely_update`: revisao obrigatoria com decisao explicita (atualiza/nao atualiza + motivo)
   - `declared_only`: auditoria de consistencia (validar se edge ainda faz sentido)
4. Prosseguir para raciocinio recursivo apenas sobre os arquivos retornados

---

## 7) Estrategia de atualizacao do graphify
Opcao recomendada (MVP):
- Executar `graphify update .` antes do `blast_radius.py` no fluxo de manutencao
- Se usar hook, aplicar condicoes:
  - executar somente quando houver mudancas em extensoes relevantes (`.py`, `.ts`, `.js`, `.md` de governanca)
  - timeout defensivo
- Se timeout: continuar em modo degradado com warning

---

## 8) Testes minimos (aceite)
Casos:
1. Intersecao clara (gera `must_update`)
2. Apenas estrutural (gera `likely_update`)
3. Apenas governanca (gera `declared_only`)
4. Arquivo novo sem aresta
5. `graph.json` ausente
6. `rx-communications.md` com secao invalida

Criterios de aceite:
- Saida JSON estavel e parseavel
- Buckets corretos nos 6 cenarios
- `journal-sync` consome resultado sem leitura manual extensa do mapa completo
- Warnings e modos degradados explicitos

---

## 9) Metricas de sucesso (primeiro ciclo)
- Reducao do universo analisado no Step 2 (ex.: de 30+ para <= 8 arquivos por execucao tipica)
- Aumento da taxa de atualizacao correta de artefatos de governanca
- Queda de falso positivo (arquivo revisado sem necessidade)
- Tempo medio do Step 2 aceitavel para uso diario

---

## 10) Roadmap apos MVP
1. Adicionar `rx_health_check.py` para drift report periodico (elemento da Proposta A)
2. Integrar sinais do `rx-affinity-lite` ao health check (auditoria cruzada)
3. Evoluir para governanca declarativa dedicada (`governance_edges.json`) quando necessario
