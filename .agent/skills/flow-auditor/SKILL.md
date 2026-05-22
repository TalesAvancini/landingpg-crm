---
name: flow-auditor
description: Gatekeeper epistemológico (Zero-Trust) para validar se a orquestração e documentos do tipo FLOW_*.md batem com a realidade física do repositório (Scripts e Glossários).
when_to_use: Sempre que o Agente for ler ou atualizar um mapa arquitetural (FLOW_*.md), antes de orquestrar uma Spec, ou quando o orquestrador exigir uma auditoria de coerência na cadeia de skills.
allowed-tools: view_file, grep_search, list_dir
---

# Flow Auditor - Reality Check de Documentos H.O.K.

> **Objetivo:** Impedir que Agentes alucinem processos ou invoquem scripts e regras que não existem fisicamente no sistema. 

O `flow-auditor` opera com o princípio de **Fail-Closed (Bloqueio Total)**. Se a documentação teórica não bater com os glossários físicos, o processo deve ser interrompido imediatamente para intervenção humana ou correção da mentira.

## Protocolo de Auditoria Rigorosa

### 1. Extração de Entidades (Parsing do FLOW)
Leia o documento `FLOW_*.md` alvo e identifique e liste mentalmente:
- Todos os arquivos `.md` citados (Ex: regras, glossários).
- Todos os scripts `.py` mencionados.
- Qualquer Agente nomeado (Ex: `@spec-driver`).

### 2. Reality Check (O Cruzamento Físico)
Para cada entidade extraída, o Agente DEVE obrigatoriamente usar ferramentas como `view_file` e `grep_search` para cruzar:
- **Glossários Principais:** Os arquivos `.md` e diretórios vitais citados estão devidamente listados no `.context/brain/FILE_GLOSSARY.md`?
- **Scripts Automação:** Os scripts `.py` ou ferramentas mencionados existem fisicamente nas pastas da arquitetura?
- **Raio de Impacto:** A cadeia de fluxo está respeitando os canais listados no `.context/maintenance/rx-communications.md`?

### 3. Veredicto e Execução (Fail-Closed)
- **Tudo Coerente (PASS):** A documentação bate com a realidade física. Prossiga com a execução das tarefas, ou libere a cadeia de orquestração.
- **Incoerência Detectada (FAIL):** **BLOQUEIO IMEDIATO.** O Agente **NÃO** deve tentar consertar o código sozinho ou reescrever o FLOW (exceto se instruído diretamente pelo usuário com uma nova permissão). Ele deve exibir o log do erro detalhado (ex: *"O arquivo FLOW_SDD.md diz para chamar 'validator.py', mas esse script não existe e não consta no glossário"*).

---

## Integração (Cadeia de Skills - Skills Chain)

Para uma orquestração perfeita no framework H.O.K, o `flow-auditor` atua como o **Segurança da Porta** e deve ser combinado com skills de **Fiscais de Saída**. 

Siga esta sequência obrigatória ao orquestrar tarefas complexas:
1. **Pré-Execução (Segurança da Porta):** Invoque o `flow-auditor` primeiro para garantir que a arquitetura teórica que você está seguindo não é uma alucinação. 
2. **Execução:** Codifique a Spec.
3. **Pós-Execução (Fiscais de Saída):** 
   - Acione a skill `lint-and-validate` (se disponível no ambiente) para garantir que a sintaxe recém-escrita não quebrou.
   - Acione a skill `verify-changes` (se aplicável) para testar e provar executando comandos reais que a alteração funciona.
