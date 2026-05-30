---
Criado em: 2026-05-29 22:57
Ultima Atualizacao: 2026-05-29 22:57
Status: Ativo
SSOT: true
---

# 📦 Product Requirements Document (PRD)
> **CRM & Sistema de Captação Automatizado (Agência MVP)**

---

## 📌 1. Visão Geral do Produto
Este documento define as especificações funcionais e a arquitetura do MVP de captação e CRM automatizado para agência. O objetivo principal é rodar uma estrutura de qualificação e centralização de leads B2B 100% autônoma, sem intervenções manuais ou custos fixos de plataformas de automação (como Make ou Zapier).

---

## 🚀 2. Requisitos Funcionais (Módulos do Sistema)

### Módulo 1: Landing Page Pública (O Site Comercial)
*   **RF1.1 — Design Minimalista**: Página única responsiva (HTML5/CSS3) focada em conversão B2B, sem links de fuga ou navegação superior.
*   **RF1.2 — Widget de Conversação**: Incorporação do script ou botão flutuante de chat do Typebot.
*   **Diretrizes de Copywriting**:
    *   *Headline Hero*: Focada em valor e corte de tempo (Ex: "Economize 20 Horas de Trabalho Manual por Semana em 14 Dias — Sem Contratar Pessoas").
    *   *Subheadline*: Explicar o que resolve (Ex: "Ajudamos agências e empresas B2B a automatizar o acompanhamento de leads usando inteligência artificial e CRMs invisíveis").
    *   *Estrutura de Copy*: Aplicar frameworks PAS (Problem, Agitation, Solution) ou BAB (Before, After, Bridge).
    *   *CTA*: Botão de ação único apontando para o benefício (Ex: "Fazer Diagnóstico Gratuito").

### Módulo 2: Formulário de Qualificação e Triagem (Typebot)
*   **RF2.1 — Roteiro de Captura Obrigatório**: Coleta em etapas lógicas:
    *   Nome completo
    *   Nome da Empresa
    *   WhatsApp de contato
    *   E-mail corporativo
    *   Orçamento Estimado (Até 2k, 2k a 5k, Acima de 5k)
*   **RF2.2 — Gatilho de Envio (Webhook)**: Disparar um POST JSON com os dados do lead para a API Node.js assim que o usuário responder a última pergunta.
*   **RF2.3 — Redirecionamento**: Redirecionar o usuário para a página de agenda do Calendly imediatamente após o disparo do webhook.

### Módulo 3: API Serverless Node.js (O Encanador de Dados)
*   **RF3.1 — Rota de Configuração (`setup-crm.js`)**: Script executado via terminal CLI para criar e estruturar automaticamente o banco de dados do Notion com as colunas, tags e cores necessárias.
*   **RF3.2 — Endpoint de Ingestão (`/api/webhook-intake`)**: Receber e validar o payload JSON do Typebot e inserir o lead como um novo card no Notion CRM.

### Módulo 4: Painel de CRM Comercial (Notion Automático)
*   **RF4.1 — Visualização Kanban**:
    *   1. Triagem (Typebot) (Entrada padrão)
    *   2. Reunião Agendada (Movido após agendamento no Calendly)
    *   3. Proposta Enviada
    *   4. Contrato Fechado
    *   5. Perdido
*   **RF4.2 — Link Direto de WhatsApp**: Propriedade de telefone deve conter um link clicável formatado (`https://wa.me/{numero}`) para abrir o WhatsApp Web.
*   **RF4.3 — Proposta Comercial Nativa**: Cada card permite escrever propostas no seu corpo interno e compartilhar o link público via "Share to Web".

### Módulo 5: Agendamento Controlado (Calendly)
*   **RF5.1 — Bloqueio por Etapa**: Acesso à agenda condicionado ao preenchimento do formulário no Typebot.
*   **RF5.2 — Sincronização**: Enviar e-mails com links do Google Meet/Zoom automaticamente ao agendar.

---

## 🛡️ 3. Requisitos Não-Funcionais
*   **RNF3.1 — Latência de Ingestão**: O lead deve aparecer no Notion em menos de 3 segundos após o clique final.
*   **RNF3.2 — Segurança**: API Keys e tokens devem ficar em variáveis de ambiente `.env`.
*   **RNF3.3 — Custo Fixo Zero**: O sistema deve rodar inteiramente no plano gratuito das ferramentas (Vercel, Notion, Typebot e Calendly).

## Critical Dependencies
- Notion Client SDK for Node.js (Fonte: market/notionhq-client)
- Dotenv Environment Variable Config (Fonte: market/dotenv)
