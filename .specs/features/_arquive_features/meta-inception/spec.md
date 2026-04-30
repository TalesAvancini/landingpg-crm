---
contract_version: 1.0
parties: ["@spec-driver", "@qa-validator"]
definition_of_done:
  - [x] Criar templates-base para INCEPTION.md e market/.
  - [x] Registrar Role @vision-architect.
  - [x] Inserir bloqueamento estratégico no Pipeline do Harness.
qa_signoff: true
signed_by: "@qa-validator"
Epic: Governança do Template
Feature: Camada Inception e Market (v2.4.0)
Status: Active
Context Dependencies: 
  - .context/brain/RULES.md
  - .context/brain/MASTER_FLOW.md
---

# 🎯 Spec: Meta-Inception Layer

## 1. Visão Geral
Implementar a fundação estrutural e de governança para injetar as restrições e objetivos "Soft e Hard" (Estratégia e Mercado) sem vazar ambiguidade para a camada executiva (PRD e Código).

## 2. Requisitos Principais
- Criar templates-base para `INCEPTION.md`, `SSOT_MAP.md` e diretório `market/`.
- Atualizar a rede de Agentes (Registrar `@vision-architect`).
- Inserir um bloqueamento estratégico no Pipeline do `Harness` (se o código quebra uma restrição do Inception, o CI deve falhar).

## 3. Restrições & Premissas
- Retro-compatibilidade: O arquivo `INCEPTION.md` deve ser **opcional** no `validate_context.py` para não causar quebras em outras instâncias desse template em uso por aí.
- Acesso explícito: O agente `@vision-architect` deve ter seus privilégios formatados aplicando Mínimo Privilégio (apenas Inception e Market).
