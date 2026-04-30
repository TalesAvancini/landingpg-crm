---
id: wiki_level2
status: DRAFT
qa_signoff: true
signed_by: "@qa-validator"
version: 1.0.0
definition_of_done:
  - "npm run context:all verde"
  - "fallback lexical funcional"
  - "artigos sem fonte bloqueados"
---

# Spec: Nível 2 Karpathy Wiki (Market Layer)

## 🎯 Objetivo
Implantar o Nível 2 da Wiki de Mercado (Karpathy Paradigm) focado em roteamento determinístico, guardrails de ingestão e lint incremental sem regressão no pipeline v2.5.0.

## 📋 Requisitos (Rastreabilidade)

### 1. Camada de Roteamento (ORACLE)
- **ORACLE-01**: Implementar cascata de busca: `SSOT_MAP.md` -> `WIKI/_index.md` -> Fallback Lexical.
- **ORACLE-02**: Retorno integral de arquivos MD para evitar truncamento cognitivo.
- **ORACLE-03**: Fallback seguro (exit 2) com warning explícito em caso de baixa confiança.

### 2. Contrato de Ingestão (GUARD)
- **GUARD-01**: Criar `ingest_wiki_guard.py` para validar schema MD (Frontmatter + Fonte + Takeaways).
- **GUARD-02**: Registro obrigatório de toda transação em `market/wiki_log.md`.
- **GUARD-03**: Fast-path (exit 0) se a pasta estiver vazia (pre-onboarding).

### 3. Governança e Qualidade (LINT)
- **LINT-01**: Atualizar `lint_wiki.py` com flag `--strict` bloqueante para diretrizes Karpathy.
- **LINT-02**: Integração no `npm run context:all` como gate obrigatório.
- **LINT-03**: Health check estrutural em `validate_context.py` (check de existência do índice).

## 📐 Design
- **Localização**: `.context/market/WIKI/`
- **Índice Mestre**: `.context/market/WIKI/_index.md`
- **Scripting**: Python 3 (No external dependencies)

## ✅ Critérios de Aceitação
1. `npm run context:all` deve passar com 100% de sucesso.
2. `npm run context:oracle` com termo inexistente deve disparar fallback e aviso.
3. Artigo sem `> Fonte: RAW/...` deve ser bloqueado pelo lint.
