# Tasks: api_notion_crm

## Sprint 01

- [ ] **TASK_01: Configuração de dependências e variáveis de ambiente**
  - **Arquivo**: `package.json`, `.env.example`
  - **Escopo**: Adicionar `@notionhq/client` e `dotenv` às dependências de produção do projeto no `package.json`. Criar o arquivo `.env.example` mapeando as credenciais necessárias (`NOTION_TOKEN`, `NOTION_DATABASE_ID`, `TYPEBOT_WEBHOOK_SECRET`).
  - **Acceptance**: RNF3.2

- [ ] **TASK_02: Script de Auto-Setup do Notion CRM**
  - **Arquivo**: `scripts/setup-crm.js`
  - **Escopo**: Desenvolver o script CLI Node.js que consome o SDK do Notion para criar uma base de dados estruturada no Notion (ou configurar uma base existente) com as colunas Nome (Title), Empresa (Text), WhatsApp (Phone), WhatsApp Link (URL), E-mail (Email), Orçamento Estimado (Select), Status (Select com cores) e data de criação.
  - **Acceptance**: RF3.1, RF4.1

- [ ] **TASK_03: Endpoint Serverless de Ingestão de Webhook**
  - **Arquivo**: `api/webhook-intake.js`
  - **Escopo**: Criar a rota de API Node.js compatível com o formato Serverless da Vercel. O endpoint deve validar o payload JSON de entrada recebido do Typebot, formatar o telefone para gerar o link WhatsApp clicável (`https://wa.me/{numero}`) e realizar a chamada da Notion API para criar o lead como um novo item.
  - **Acceptance**: RF3.2, RF3.2.1, RF4.2, RNF3.1
