---
feature_id: landing_page_crm
type: standard
contract_mode: sprint_based
current_sprint: sprint_01
executor_context_id: spec-driver
validator_context_id: qa-validator
origin: .context/brain/PRD.md

sprint_01:
  scope_allow: 
    # Global/Maintenance (Obrigatório para V3)
    - .specs/features/landing_page_crm/STATE.md
    - .specs/features/landing_page_crm/tasks.md
    - .specs/features/landing_page_crm/*.enriched.md
    - .specs/features/landing_page_crm/CLOSURE.md
    - .context/maintenance/HARNESS_LOG.md
    - .context/maintenance/JOURNAL.md
    - .specs/features/landing_page_crm/AGENT_SCRATCHPAD.md
    # Feature Scope
    - index.html
    - style.css
  max_impact_radius: 6
  dod:
    - Landing Page renderiza corretamente em desktop e mobile (responsiva)
    - Seção Hero com headline de impacto, subheadline e CTA único visíveis acima da dobra
    - Framework de copy PAS (Problem, Agitation, Solution) aplicado nas seções da página
    - Pilha de benefícios focada em outcomes de negócio (não features técnicas)
    - Container/placeholder do Typebot integrado e funcional na página
    - Nenhum link de navegação ou rota de fuga (sem menu superior)
    - Design premium dark mode com gradientes, micro-animações e tipografia profissional
  qa_signoff: false
---

# Feature: Landing Page de Alta Conversão B2B

## 0. Origem
> **Documento-raiz:** `.context/brain/PRD.md` — Módulo 1 (RF1.1, RF1.2) e Diretrizes de Copywriting.
> Escopo reduzido ao frontend estático da Landing Page. O backend (API Node.js, Módulo 3) e as integrações externas (Typebot config, Calendly) ficam fora desta spec.

## 1. O Problema
A agência precisa de uma presença web pública que capture a atenção de potenciais clientes B2B e os direcione para o fluxo de qualificação (Typebot), sem oferecer rotas de fuga. Atualmente não existe nenhum código de produção no repositório — o frontend precisa ser criado do zero.

## 2. A Solução
Criar uma Landing Page estática em HTML5/CSS3 puro (sem frameworks JS), com design premium focado em conversão B2B. A página segue o framework de copywriting PAS (Problem, Agitation, Solution) e inclui:
- Seção Hero com headline de impacto e CTA único
- Seção de agitação das dores do cliente
- Pilha de benefícios focada em resultados de negócio
- Container do Typebot (widget de chat conversacional)
- Design dark mode moderno com tipografia profissional (Google Fonts), gradientes e micro-animações

## 3. Requisitos Funcionais (Acceptance)
- [ ] RF1.1 — Página única responsiva (HTML5/CSS3) sem links de fuga ou menu de navegação
- [ ] RF1.2 — Widget/container do Typebot incorporado na página (script placeholder configurável)
- [ ] COPY-01 — Headline Hero focada em valor e corte de tempo
- [ ] COPY-02 — Subheadline explicativa do serviço
- [ ] COPY-03 — CTA único com texto de benefício (não genérico)
- [ ] COPY-04 — Seções seguindo framework PAS (Problem, Agitation, Solution)
- [ ] COPY-05 — Pilha de benefícios focada em outcomes (Corte de Custos, Tempo, Escala)
- [ ] DESIGN-01 — Dark mode premium com gradientes sutis e paleta harmoniosa
- [ ] DESIGN-02 — Tipografia profissional via Google Fonts (Inter ou Outfit)
- [ ] DESIGN-03 — Micro-animações em hover/scroll para engajamento
- [ ] DESIGN-04 — Layout 100% responsivo (mobile-first)

## 4. Critérios de Integridade V3 (Não Negociáveis)
Para que esta Spec seja considerada completa, o executor deve gerar um `STATE.md` contendo TODAS as 9 evidências da cadeia (CHAIN_CONTEXT_LOADED até CHAIN_HANDOFF), e um `CLOSURE.md` síntese deve ser gerado na Skill 9 (HANDOFF).

## 5. Raw Payloads (Injeção Atômica)
- INCEPTION-NUNCA-04: "NUNCA criar rotas de navegação tradicionais (como 'Sobre', 'Contato') na Landing Page pública, preservando a estrutura de conversão de funil de página única sem rotas de fuga."
- INCEPTION-SEMPRE-02: "SEMPRE estruturar a Landing Page em HTML5/CSS3 sem frameworks JS pesados (como NextJS ou React se não solicitados), mantendo-a minimalista, responsiva e performática."
- PRD-RF1.1: "Página única responsiva (HTML5/CSS3) focada em conversão B2B, sem links de fuga ou navegação superior."
- PRD-RF1.2: "Incorporação do script ou botão flutuante de chat do Typebot."
- PRD-COPY-HEADLINE: "Headline Hero focada em valor e corte de tempo (Ex: 'Economize 20 Horas de Trabalho Manual por Semana em 14 Dias — Sem Contratar Pessoas')."
- PRD-COPY-CTA: "Botão de ação único apontando para o benefício (Ex: 'Fazer Diagnóstico Gratuito')."
- PRD-COPY-PAS: "Aplicar frameworks PAS (Problem, Agitation, Solution) ou BAB (Before, After, Bridge)."
