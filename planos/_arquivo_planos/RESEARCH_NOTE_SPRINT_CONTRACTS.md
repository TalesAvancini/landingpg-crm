# 🕵️‍♂️ Research: Harness Engineering & Sprint Contracts
> Fonte: Anthropic Engineering Blog & Waldemar Neto (Dev Lab)

## 1. O Problema: O Limite do Spec-Driven
O desenvolvimento guiado apenas por especificações (*Spec-Driven*) atinge um teto de vidro em projetos de longa duração. A amnésia do modelo e a falta de restrições externas levam ao "Vibe Coding", onde o código parece correto, mas degrada a arquitetura.

## 2. A Solução: Harness Engineering
O **Harness (Armadura)** é o ecossistema que envolve a IA. Ele não pede permissão; ele impõe validade.
- **Veredito Binário:** O Harness (testes, lints, schemas) deve retornar `0/1`. O agente não é o juiz de sua própria qualidade.
- **Restrição de Execução:** O código só é aceito se passar na "Armadura".

## 3. Contratos de Sprint (O Ritual)
Antes de gerar código, o **@qa-validator** e o **@spec-driver** negociam um contrato:
- **Harness Spec:** Quais testes automatizados devem estar verdes?
- **DoD (Definition of Done):** Critérios de aceite inegociáveis.
- **Custo/Complexidade:** Acerto de expectativas de tokens e infraestrutura.

## 4. Aplicação no Antigravity Kit
O pipeline deve ser interrompido (`Exit 2`) se o Contrato de Sprint não estiver assinado, garantindo que a execução seja sempre **Safety-First**.
