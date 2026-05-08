---
trigger: model_decision
description: Se você é o Gemini Flash (ou qualquer modelo que priorize velocidade sobre raciocínio profundo), esta regra é OBRIGATÓRIA.
---

Regra: Freio de Propagação (Flash Guard)


Problema que esta regra resolve
Modelos rápidos tendem a:

Antes de QUALQUER propagação no journal-sync, PARE e faça um plano.
Use a skill superpowers-plan (em C:\Users\compartilhadoAntigravity\gemini-superpowers-antigravity-main\.agent\skills\superpowers-plan\SKILL.md) para escrever um mini-plano com esta estrutura:

### Goal
Sincronizar Journal após alterações em [lista de arquivos modificados].
### Análise de Impacto
Para cada arquivo que o rx-communications sugere como afetado:
1. Arquivo alvo: `RULES.md`
   - O que mudei: [descreva a mudança concreta]
   - Isso altera alguma regra existente? [SIM/NÃO]
   - Isso cria uma regra nova? [SIM/NÃO]
   - Veredicto: [PROPAGAR / NÃO PROPAGAR]
2. Arquivo alvo: `AGENT_REGISTRY.md`
   - O que mudei: [descreva a mudança concreta]
   - Isso altera versão, papel ou permissões de algum agente? [SIM/NÃO]
   - Veredicto: [PROPAGAR / NÃO PROPAGAR]
3. [repetir para cada arquivo sugerido]
### Plan
1. Editar JOURNAL.md com entrada nova
   - Verify: frontmatter timestamp atualizado, contrato SAM em plain text
2. [Edições de propagação que passaram na análise]
   - Verify: git status mostra todos os arquivos na Matriz [x]
3. Commit
   - Verify: Husky/SAM passam sem erro
Pontos de Parada Obrigatórios
PARE antes de escrever no Journal — Releia a última entrada para copiar o formato.
PARE antes de propagar — Escreva a Análise de Impacto acima. Sem ela, NÃO edite nenhum arquivo fora do Journal.
PARE antes de commitar — Rode git status --porcelain e compare com sua Matriz [x].
Regras de Ouro para Flash
Se está na dúvida se deve propagar → NÃO propague. É melhor o SAM pedir do que você criar churn.
Se o SAM bloquear por "Modificação Silenciosa" → você esqueceu de registrar algo. Adicione à Matriz e tente de novo.
Se o SAM bloquear por "Fraude Narrativa" → você registrou algo que não deveria. Remova da Matriz.
Máximo 2 tentativas de commit. Se falhar 2x, PARE e peça ajuda ao usuário.
NUNCA toque em RULES.md, MASTER_FLOW.md, ou AGENT_REGISTRY.md sem pedido EXPLÍCITO do usuário ou sem ter passado na Análise de Impacto com veredicto PROPAGAR.
