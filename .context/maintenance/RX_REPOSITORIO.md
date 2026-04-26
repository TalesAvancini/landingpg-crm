---
Criado em: 2026-04-26
Ultima Atualizacao: 2026-04-26
Status: Ativo (v2.5.2)
---

# 🔬 RX: Raio-X do Repositório `Antigravity-Template` (v2.5.2)

> Mapeamento funcional e arquitetural do ecossistema de governança. Este documento serve como bússola para humanos e IAs navegarem na estrutura Autobuilder e compreenderem a topologia do Zero Trust.

---

## 1) Visão Geral Rápida

*   **O Produto:** Este repositório é um **Framework de Governança**. O "produto" principal é a automação da integridade do contexto e a garantia de qualidade por IA.
*   **Camada de Comando:** Centralizada no `run_context.py` e mapeada via `package.json`.
*   **Orquestração Zero Trust:** A execução de código e a auditoria de qualidade (QA) são obrigatoriamente separadas entre a IA Executora e Subagentes Validadores isolados.
*   **Memória:** Distribuída entre `.context/` (Sempre Ativo) e `.specs/` (Efêmero/Execução).

---

## 2) Mapa Estrutural da Raiz

| Pasta / Arquivo | Função no Projeto | Status | Evidências-chave |
| :--- | :--- | :--- | :--- |
| **`.context/`** | Memória de longo prazo, regras de arquitetura e logs de manutenção. | **Ativo (Crítico)** | `brain/`, `maintenance/`, `_scripts/` |
| **`.specs/`** | Bancada de execução (Workshop). Onde os contratos de código nascem. | **Ativo (Workshop)** | `features/`, `_template.md` |
| **`.agent/`** | Infraestrutura de Subagentes Nativos. Prompts isolados de roles. | **Ativo (QA/Autonomia)** | `subagents/qa-validator.md` |
| **`.husky/`** | Cão de guarda git. Aciona o `run_context.py` no pre-commit. | **Ativo (Gatekeeper)** | `pre-commit` |
| **`planos/`** | Área de rascunhos, pesquisas e ideias fora do contexto core. | **Suporte (Lab)** | `_arquivo_planos/` |
| **`tests/`** | Testes de integridade da própria infraestrutura de governança. | **Ativo (QA)** | `test_context.py` |
| **`captura_projeto/`** | Ferramentas de bundling e ingestão de contexto para LLMs. | **Suporte (Ingestão)** | `captura_projeto.py` |
| **`run_context.py`** | O "Maestro". Orquestra todos os scripts Python do framework. | **Ativo (Core)** | `all`, `validate`, `harness` |

---

## 3) Detalhamento das Pastas Críticas

### 🧠 `.context/` (Governança e Memória)
A "Caixa Preta" e o "Cérebro" do projeto.
*   **`brain/`**: A **Constituição** (`RULES.md`), a **Visão** e o **Registro de Agentes** (`AGENT_REGISTRY.md`). Define as leis da física da IA.
*   **`maintenance/`**: Contém o **Diário** (`JOURNAL.md`), a **Anatomia** e a **Biologia**. É o registro histórico e a saúde técnica.
*   **`_scripts/`**: O motor lógico. Contém scripts pesados como `harness_runner.py` (validador de contratos) e `workflow_journal_auditor.py` (auditor Anti-Migué).

### 🤖 `.agent/` (Subagentes e Autonomia)
Onde residem os avatares especializados do projeto (Padrão B).
*   **`subagents/`**: Guarda prompts isolados (ex: `qa-validator.md`) que são invocados automaticamente pela IA Orquestradora para realizar tarefas de confiança zero, como a auditoria do SAM sem intervenção humana.

### 🧪 `.specs/` (Workshop de Execução)
Onde o trabalho prático (features, fixes, refactors) acontece.
*   **`features/`**: Cada subpasta aqui é uma tarefa atômica. Contém o `spec.md` (o contrato) e o `STATE.md` (o sinalizador do gate).

---

## 4) Pontos de Atenção e Diagnóstico

*   **Saneamento Recente:** As pastas obsoletas `.context/specs` e `.context/planos` foram eliminadas e o histórico consolidado. O sistema usa *Ordem Cronológica Reversa* no Journal.
*   **SAM Gate & Zero Trust:** Nunca edite arquivos em `.context/` sem atualizar o `JOURNAL.md`. O commit será bloqueado pelo SAM. A aprovação da spec agora é validada proativamente pelo `@qa-validator`.
*   **Fuso Horário:** O sistema opera nativamente em **Brasília (-3h)**.

---

## 5) Hierarquia Funcional de Verdade

O repositório obedece a uma rigorosa hierarquia de abstração:
1.  **Nível 0 (Leis Fundamentais):** `RULES.md`, `INCEPTION.md`, `AGENT_REGISTRY.md`.
2.  **Nível 1 (Estratégia e Planos):** `PRD.md`, `ROADMAP.md`.
3.  **Nível 2 (Ação Tática):** `.specs/features/`.
4.  **Nível 3 (Evidência Física):** `JOURNAL.md`, `.agent/subagents/`, `HARNESS_LOG.md`.

**Veredito:** O repositório está em estado **Hardened (Endurecido) com Zero Trust**. Toda mudança é rastreável, cada linha de código exige um contrato prévio, e a IA orquestradora delega a auditoria de qualidade para um subagente autônomo, blindando o pipeline contra burla e eliminando o humano como gargalo mecânico.
