---
name: harness-context
description: Architectural context of the H.O.K. Validation Harness, including SAM, Karpathy Layer, SDD, and the physical flexibilization rules (Modo Light).
license: MIT
metadata:
  author: AI
  version: 2.0.0
---

# Harness Context Skill

Esta skill fornece o contexto arquitetural e operacional abrangente do sistema de validação H.O.K. (Harness Layer) e do Sistema Anti-Migué (SAM). Ela serve como guia de boot para entender os gates físicos, as restrições epistemológicas e as regras de flexibilização do **Modo Light** implementadas no repositório.

## 🏗️ Architectural Overview

O ecossistema de governança opera sob três camadas de controle e acoplamento:

1. **Camada Estratégica (`brain/`)**: Contém a Visão, Inception e PRD. Dita as fronteiras de escopo ("NUNCA" e "SEMPRE").
2. **Camada de Execução (`.specs/features/`)**: A bancada de desenvolvimento do Spec-Driven (SDD). Controla modificações via `scope_allow` e `max_impact_radius`.
3. **Camada de Validação (`_scripts/`)**: Enforces de qualidade de código, segurança e integridade criptográfica aplicados ativamente no pre-commit (Husky).

---

## 🛡️ The Validation Gates

### 1. SAM (Sistema Anti-Migué)
*   **Finalidade**: Auditar a correspondência entre a Matriz de Propagação do `JOURNAL.md` e os arquivos modificados no Git.
*   **Fraude Narrativa**: Bloqueia se você declarar modificações no diário em arquivos que o Git não viu.
*   **Modificação Silenciosa**: Bloqueia se você alterar arquivos governados sem relatá-los na matriz de diário.
*   **Exceções**: `SHADOW_FILES` (logs automáticos, dashboards e índices de projeto) e caminhos imunes definidos em `IGNORED_PREFIXES` (ex: `planos/`, `scratch/`, `temp/`, `.context/maintenance/_archive_context/`).

### 2. Karpathy Layer (Linter Epistemológico)
*   **Finalidade**: Exigir que claims técnicos na Wiki de Mercado possuam citação e procedência (`> Fonte: RAW/...`).
*   **Exceção**: Se a página contiver a palavra-chave `SSOT` (Single Source of Truth), a checagem é ignorada.

---

## 📅 Decisões de Flexibilização (Modo Light)

Para evitar atritos e travamentos de pipeline durante o desenvolvimento cotidiano, o repositório opera em Modo Light:

1. **SAM Tolerante (WARNING local)**: Em branches secundárias (`feature/*`, `bugfix/*`), o SAM vira apenas consultivo (`Exit 0`), permitindo commits ágeis enquanto exibe o painel visual com a dívida de governança a ser sanada antes do merge. Em branches estáveis (`main`, `master`), o modo STRICT (`Exit 1`) é imposto fisicamente.
2. **Complexity Gate Consultivo**: Análise ciclomática e tamanho de arquivo geram avisos educacionais no terminal sem bloquear o commit.
3. **Cobertura Semântica Light**: Checklist pedagógico que valida se novas declarações de funções possuem referências de teste escritas nos arquivos correspondentes.

---

## 🔧 Implementação Física dos Harnesses locais

Os validadores físicos estão implementados como scripts Python autônomos sob `.context/_scripts/` e integrados no orquestrador mestre `harness_runner.py`:

### A. SAM Dinâmico (`workflow_journal_auditor.py`)
*   **Mecânica**: Executa `git rev-parse --abbrev-ref HEAD` para descobrir a branch git ativa. Se a branch for diferente de `main` e `master`, define dinamicamente `mode = "assist"`. 
*   **Aviso Visual**: Imprime no terminal o sumário de inconsistências e retorna `0` de forma não-bloqueante em branches secundárias.

### B. Env Drift Gate (`env_drift_gate.py`)
*   **Mecânica**: Varre recursivamente arquivos de código JS e TS (exceto pastas ignoradas como `node_modules`, `.context/`, `scratch/`, `planos/`) procurando pelo padrão `process.env.VAR_NAME` ou `process.env['VAR_NAME']`.
*   **Enforcement**: Cruza o conjunto de variáveis descobertas com as chaves declaradas em `.env.example`. Bloqueia fisicamente o commit (Exit Code 1) caso novas variáveis de ambiente não estejam listadas no template.

### C. Detector de Exaustão de Loop (`loop_exhaustion_harness.py`)
*   **Mecânica**: Projetado para evitar o consumo infinito de tokens por teimosia de IA. Monitora falhas consecutivas de testes locais e as armazena no log efêmero `scratch/loop_state.json`.
*   **Git Hash Reset**: Calcula o hash SHA256 do diff de `git diff HEAD`. Se o hash mudar (o que indica que a IA alterou fisicamente o código para tentar corrigir a falha), o contador de erros consecutivos é reiniciado para 1. Se o hash for idêntico, incrementa o contador.
*   **Bloqueio Físico**: Ao atingir 5/5 falhas sem alteração de diff, o script aborta com Exit Code 1, travando a esteira subsequente e exigindo escalação obrigatória para validação humana (Bandeira Branca).
*   **Reset de Sucesso**: Ao rodar com o status pass (`--status pass`), o contador é zerado.

### D. Complexidade & Cobertura Semântica (`complexity_coverage_gate.py`)
*   **Verificação de Linhas**: Analisa se arquivos JS alterados ultrapassam 250 linhas, recomendando subdivisões de arquivos grandes.
*   **Aninhamento Estrutural**: Alerta se o recuo de chaves `{` e `}` exceder 4 níveis, indicando complexidade ciclomática exagerada.
*   **Semantic Coverage**: Procura por definições de funções (ex: `function minhaFuncao(...)` ou `const minhaFuncao = ...`) em arquivos JS alterados e verifica se a string nominal da função aparece no arquivo `.test.js` associado na pasta `tests/`. Emite avisos educacionais em caso de testes ausentes.
*   **Enforcement**: Opera sempre de forma consultiva (Exit Code 0), servindo como checklist orientador de boas práticas.
