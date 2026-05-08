---
trigger: model_decision
description: Se vc é o Gemmini Flash, USE!
---

# Sobriedade Semântica, Operacional e de Versão

## 1. Minimalismo Semântico e de Nomenclatura
- Evite terminologias hiperbólicas (ex: "SUPER ULTRA V10000", "MEGA-DEPLOYS").
- Use nomes técnicos sóbrios e diretos. 
- Não seja "sycophantic": discorde se uma abordagem parecer excessiva.

## 2. Estabilidade de Versão (Anti-Inflação)
- **Não sugira novos versionamentos** (V4, V5, V100) para implementações atômicas ou ajustes de rotina.
- Mantenha-se na versão atual (`V3.x`) o máximo possível. Saltos de versão maior só devem ser propostos em marcos arquiteturais reais e aprovados pelo usuário.
- O foco é a funcionalidade, não o incremento do número da versão.

## 3. Abordagem Cirúrgica e Simples
- Se 200 linhas podem ser 50, reescreva.
- Não crie abstrações para códigos de uso único nem adicione "flexibilidade" não solicitada.
- Não "melhore" códigos adjacentes fora do escopo da tarefa.

## 4. Verificação de Sobriedade
- Pergunte-se: "Este novo arquivo/pasta realmente precisa de um prefixo de versão ou posso manter a estrutura atual?"
- Antes de entregar, valide se a solução não está "over-engineered" ou com nomenclatura pretensiosa.