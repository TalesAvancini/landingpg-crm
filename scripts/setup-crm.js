require('dotenv').config();
const { Client } = require('@notionhq/client');

const notion = new Client({ auth: process.env.NOTION_TOKEN });

async function main() {
  console.log("Notion setup script initialized.");
  const parentPageId = process.env.NOTION_PAGE_ID;
  if (!parentPageId) {
    console.error("Error: NOTION_PAGE_ID is not defined.");
    process.exit(1);
  }

  try {
    console.log("Creating Kanban database under page:", parentPageId);
    const response = await notion.databases.create({
      parent: {
        type: 'page_id',
        page_id: parentPageId,
      },
      title: [
        {
          type: 'text',
          text: {
            content: 'Lead CRM Pipeline',
          },
        },
      ],
      properties: {
        Name: {
          title: {},
        },
        Company: {
          rich_text: {},
        },
        WhatsApp: {
          url: {},
        },
        Email: {
          email: {},
        },
        Budget: {
          select: {
            options: [
              { name: 'Até 2k', color: 'blue' },
              { name: '2k a 5k', color: 'green' },
              { name: 'Acima de 5k', color: 'purple' },
            ],
          },
        },
        Status: {
          select: {
            options: [
              { name: '1. Triagem (Typebot)', color: 'default' },
              { name: '2. Reunião Agendada', color: 'yellow' },
              { name: '3. Proposta Enviada', color: 'orange' },
              { name: '4. Contrato Fechado', color: 'green' },
              { name: '5. Perdido', color: 'red' },
            ],
          },
        },
      },
    });

    console.log("Database created successfully!");
    console.log("Database ID:", response.id);
  } catch (error) {
    console.error("Error creating Notion database:", error.message);
    process.exit(1);
  }
}

if (require.main === module) {
  main().catch(console.error);
}
