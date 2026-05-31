---
Criado em: 2026-04-10 20:50
Ultima Atualizacao: 2026-05-30
Status: Ativo
SSOT: true
---

# 🔧 TECHNICAL REQUIREMENTS: Restrições e Ambiente

Este documento especifica a pilha técnica, dependências de pacotes autorizados e os requisitos de variáveis de ambiente para a integridade técnica da aplicação.

---

## 🚫 Restrições de Infraestrutura (Guerrilha)
> O Antigravity Kit (H.O.K Forge) atua como um sistema para PMEs. Fica expressamente **proibida** a introdução das seguintes tecnologias no core, limitando o AI Slop e a dívida técnica:
- **Kubernetes (K8s)** ou Orquestradores Complexos.
- **Bancos Vetoriais (Vector DBs)** para busca de contexto (usar stdlib-only).
- **Infraestruturas MLOps Pesadas**.
- **Middlewares Pagos (Make/Zapier):** Toda a persistência e transporte devem ser feitos em código nativo.

---

## 🔧 Requisitos Mínimos (Motor)
Para execução segura dos scripts de governança (Harness e Oracle) e da API de produção:
- **Python:** `>= 3.10`
- **Node.js:** `>= 18.x` (para pacotes de pre-commits automáticos e Vercel Serverless)

---

## 📦 Dependências Autorizadas (Node.js)

### Produção (`dependencies`)
- `@notionhq/client`: `^2.2.15` (SDK Oficial da API do Notion)
- `dotenv`: `^16.4.5` (Gerenciador de variáveis de ambiente locais)

### Desenvolvimento (`devDependencies`)
- `husky`: `^9.1.7` (Gerenciador de Git Hooks locais)

---

## 🔑 Variáveis de Ambiente Obrigatórias (`.env`)

Para o funcionamento correto dos endpoints e scripts de automação, o arquivo local `.env` (baseado no `.env.example`) deve obrigatoriamente prever as seguintes chaves:

| Variável | Tipo | Finalidade |
| :--- | :--- | :--- |
| `NOTION_TOKEN` | String (Segredo) | Token de integração secreta (Internal Integration Token) gerado no painel do Notion Developer. |
| `NOTION_PAGE_ID` | String (ID) | ID de 32 caracteres da página pai onde o banco de dados do CRM será criado pelo script. |
| `NOTION_DATABASE_ID` | String (ID) | ID de 32 caracteres do banco de dados Kanban criado no Notion (gerado pelo setup e consumido pela API). |
| `TYPEBOT_WEBHOOK_SECRET` | String (Segredo) | Token estático e estrito de segurança que valida a autenticação Bearer da requisição originária do Typebot. |

<!-- AUTO-SYNC START -->
*🤖 Atualizado automaticamente em 2026-05-30 21:44*

### Dependencias (package.json)
- `@notionhq/client`: `^2.2.15`
- `dotenv`: `^16.4.5`

### DevDependencies
- `husky`: `^9.1.7`

### Tabelas no Schema (schema.sql)
- `orders`

<!-- AUTO-SYNC END -->




