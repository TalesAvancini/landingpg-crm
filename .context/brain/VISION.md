<!-- SSOT -->
# Visão do Projeto: Sistema de Captação e CRM Automatizado (Agência MVP)

Framework Version: v2.5.2

Este documento define a visão estratégica, os objetivos de negócio e as funcionalidades planejadas para o MVP do sistema de captação e triagem de leads, integrado ao Notion CRM.

## 🎯 O "Porquê" (Essência)
Agências e profissionais liberais enfrentam altos custos e esforço manual recorrente para capturar, qualificar e gerenciar potenciais clientes comerciais. Este sistema substitui VPSs caros e automações pagas (como Make ou Zapier) por uma arquitetura Serverless híbrida (Typebot + API Node.js + Notion CRM), garantindo 100% de leads capturados, triados e organizados de forma automática com custo fixo zero.

## 🚀 O "O Quê" (Objetivos)
1. **Custo Fixo Zero**: Utilizar camadas gratuitas das ferramentas (Vercel, Notion, Typebot e Calendly).
2. **Esforço Manual Zero**: Automação ponta a ponta na criação da tabela (setup do banco) e na inserção dos novos leads.
3. **Filtro de Curiosos (Triagem)**: Impedir o agendamento direto na agenda sem que os dados mínimos de qualificação do lead tenham sido validados.
4. **Entrega Profissional**: Criação automática de cards no Notion para controle comercial em formato Kanban e propostas geradas no corpo dos cards.

## 🎭 Tom de Voz & Estilo
* Minimalista, de alta conversão, enxuto e profissional.

## 🛑 O que o projeto NÃO é
* Não é um produto SaaS multi-tenant.
* Não é um CRM com servidores próprios ou painéis proprietários complexos.
* Não depende de softwares de middleware pagos (Make, Zapier, etc.).

---

### 📄 PRD: Detalhes das Integrações e Módulos

#### 1. Arquitetura Técnica
* **Hospedagem & API**: Vercel (Gratuito/Serverless).
* **Linguagem & Backend**: Node.js com Express.
* **Banco de Dados & CRM**: Notion (Integração oficial via `@notionhq/client`).
* **Qualificação**: Typebot (Conversacional incorporado).
* **Agendamento**: Calendly (Redirecionamento).

#### 2. Requisitos Funcionais
* **Módulo 1: Landing Page Pública**
  * HTML5/CSS3 minimalista focado em conversão de leads B2B (frameworks de copy PAS/BAB, Headline de Impacto, CTA Único e sem rotas de fuga/links desnecessários).
  * Widget do Typebot integrado (chat conversacional).
* **Módulo 2: Formulário de Triagem (Typebot)**
  * Coleta de: Nome, Empresa, WhatsApp, E-mail corporativo, Orçamento estimado.
  * Dispara webhook POST JSON para a API Node.js ao finalizar o formulário.
  * Redireciona o usuário qualificado para a agenda do Calendly.
* **Módulo 3: API Serverless Node.js**
  * `setup-crm.js`: Script executado via terminal que se conecta ao Notion e monta a tabela de CRM com suas colunas, tags e cores de forma automatizada.
  * `/api/webhook-intake`: Endpoint que recebe os dados do Typebot, valida e insere como card no Notion.
* **Módulo 4: Painel de CRM (Notion)**
  * Funil Kanban: Triagem, Reunião Agendada, Proposta Enviada, Contrato Fechado, Perdido.
  * Link direto do WhatsApp (`wa.me`) clicável para o contato do lead.
  * Proposta Comercial editável dentro do corpo do card com "Share to Web".
* **Módulo 5: Agendamento Controlado (Calendly)**
  * Bloqueio por etapa (acesso à agenda condicionado à triagem).
  * Sincronização e convite do Google Meet/Zoom automático.
