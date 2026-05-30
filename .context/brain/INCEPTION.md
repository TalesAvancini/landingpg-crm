---
version: 2.5.2
mode: STRATEGIC
status: ACTIVE  # [DRAFT | ACTIVE | TRANSLATION_LOCK]
---

<!-- 🚨 SYSTEM TRIGGER: IA, NÃO PROSSIGA PARA GERAÇÃO DE CÓDIGO SE OS CAMPOS ABAIXO CONTIVEREM "[TODO]" OU PERGUNTAS. INTERROGUE O HUMANO PRIMEIRO. -->
> 🤖 **INSTRUÇÃO DE FLUXO:** Antes de propor specs ou código, preencha os campos estratégicos. Se `[TODO]` persistir, retorne ao humano com: `"⚠️ Contexto incompleto em INCEPTION.md. Preciso de: [lista]"`.

# 🧭 INCEPTION - Fronteiras Estratégicas (SSOT)

> 🛡️ **HARNESS PREVENTIVO (PARA MÁQUINAS)** 
> Este arquivo dita a Estratégia de Negócio e Limites Arquiteturais (O que NUNCA e SEMPRE fazer).
> - **NÃO** insira UUIDs, IDs de nuvem, mapeamento de pastas, nem configurações de ferramentas.
> - Dependências externas devem ir pro `market/SSOT_MAP.md`.
> - Somente a role `@vision-architect` deve alterar significativamente este arquivo.

*Ratificado a partir da tradução cognitiva do `VISION.md`.*

## 🎯 Visão Mestra
Desenvolvimento de uma Landing Page focada em conversão B2B que acopla um formulário conversacional (Typebot) a um endpoint de API Node.js serverless na Vercel. A API consome o SDK oficial do Notion para popular e gerenciar um CRM comercial estruturado de forma 100% automatizada (com script de auto-setup do banco no Notion). O fluxo garante custo fixo de infraestrutura zero e redirecionamento para agendamento controlado via Calendly.

## 🛑 NUNCA (Boundaries)
> *Limites inegociáveis. Se a IA tentar cruzar estas linhas, o Harness aplicará o fail-fast.*
- **NUNCA** utilizar bancos de dados relacionais ou NoSQL clássicos (como PostgreSQL, MongoDB) para persistência de leads, mantendo o Notion como o banco exclusivo de dados comerciais (SSOT).
- **NUNCA** utilizar ferramentas de middleware pagas (Make, Zapier) para a transmissão ou mapeamento de dados. Toda a integração de webhook e consumo do SDK Notion deve ser feita via código na API Node.js.
- **NUNCA** expor tokens de API do Notion, links sensíveis ou chaves de webhook no código do lado do cliente (client-side/Landing Page).
- **NUNCA** criar rotas de navegação tradicionais (como "Sobre", "Contato") na Landing Page pública, preservando a estrutura de conversão de funil de página única sem rotas de fuga.

## 🛡️ Checklist Estratégico (Preenchimento Obrigatório)
- [x] **Transações DB?** Sim (Notion API via SDK oficial `@notionhq/client` atuando como banco de dados).
- [x] **APIs Externas?** Sim (Notion API, Webhook intake do Typebot, redirecionamento Calendly).
- [x] **Compliance Obrigatório?** Sim (LGPD - Coleta de dados pessoais como nome, e-mail e WhatsApp via formulário de triagem).

## 🟢 SEMPRE (Restrições de Processo)
> *Processos que a IA deve invocar obrigatoriamente durante o ciclo de vida.*
- **SEMPRE** utilizar variáveis de ambiente estruturadas (`.env`) para gerenciar as credenciais da API do Notion (`NOTION_TOKEN`, `NOTION_DATABASE_ID`).
- **SEMPRE** estruturar a Landing Page em HTML5/CSS3 sem frameworks JS pesados (como NextJS ou React se não solicitados), mantendo-a minimalista, responsiva e performática.
- **SEMPRE** validar os campos de payload (`name`, `company`, `whatsapp`, `email`, `budget`) no webhook do Express antes de tentar a inserção no Notion.
- **SEMPRE** formatar a propriedade de telefone no Notion de forma a gerar um link direto clicável para o WhatsApp (`https://wa.me/{numero}`).
