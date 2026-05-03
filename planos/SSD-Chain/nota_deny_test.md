# Nota Técnica: Teste de Estresse do Sandbox (Hard-Deny vs. Cognitive-Lock)

> **Contexto:** Durante o design da Chain-Skills V3, surgiu a dúvida sobre a granularidade das permissões de ferramentas (`tool_permissions`) no Antigravity/IDE.
> **Data:** 2026-05-03
> **Autor:** MiMo / Antigravity Agent

## 1. O Problema Epistemológico
Não sabemos se ao definir `deny: [edit_file]` no frontmatter de um **subagente**, o IDE bloqueia a ferramenta apenas para aquele processo isolado ou se o bloqueio "vaza" para o **Agente Central (Orquestrador)**.

*   **Hipótese A (Isolamento Real):** O bloqueio é por subagente. Seria o cenário ideal para segurança máxima.
*   **Hipótese B (Vazamento Global):** O bloqueio remove a ferramenta da sessão inteira. Isso "cegaria" o Orquestrador, impedindo intervenções de emergência.

## 2. O Teste de Estresse Proposto
Para validar isso durante a **Fase 4 (Integração)** da V3, devemos executar o seguinte rito:

1.  **Preparação:** Criar um subagente temporário (`test-worker.md`) com a seguinte configuração:
    ```yaml
    tool_permissions:
      deny:
        - multi_replace_file_content
        - edit_file
    ```
2.  **Desafio do Subagente:** Ordenar que o `test-worker` escreva 30 linhas de código em dois arquivos simultaneamente (forçando o uso de `multi_replace_file_content`).
    *   *Resultado esperado:* O sistema deve retornar um erro de "Tool not available".
3.  **O Xeque-Mate (Orquestrador):** Imediatamente após a falha do subagente, o Agente Central deve tentar executar EXATAMENTE a mesma operação de escrita multi-arquivo.
    *   *Cenário 1 (Sucesso do Orquestrador):* O isolamento é real. Podemos voltar a usar Hard-Deny no plano V3.
    *   *Cenário 2 (Falha do Orquestrador):* O bloqueio é global. Isso valida a decisão atual da V3 de usar **Restrição Cognitiva (Prompt) + Auditoria SAM**.

## 3. Por que isso importa?
A V3 optou por **Restrição Cognitiva** para evitar o risco do Cenário 2. Se o Orquestrador perder suas ferramentas, ele perde o poder de "policiar" e "corrigir" o sistema, quebrando o princípio do Orquestrador como Supervisor Ativo.

## 4. Como proceder se o teste for realizado
- Se o **Cenário 1** for comprovado, atualizar o `Chain-Skills V3.md` (Seção 5.2) para restaurar os blocos `deny` físicos, aumentando a blindagem contra impulsos da IA.
- Se o **Cenário 2** for comprovado, manter a abordagem atual de restrição via prompt e monitoria de log (SAM).

---
*Nota vinculada à Fase 4 do Checklist de Implementação da Chain-Skills V3.*
