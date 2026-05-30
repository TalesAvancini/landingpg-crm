require('dotenv').config();
const { Client } = require('@notionhq/client');

// Initialize Notion client
const notion = new Client({ auth: process.env.NOTION_TOKEN });

// Retry helper with exponential backoff
async function retryWithBackoff(fn, retries = 3, delay = 500) {
  let attempt = 1;
  while (attempt <= retries) {
    try {
      return await fn();
    } catch (error) {
      console.warn(`[Notion API] Attempt ${attempt} failed. Error: ${error.message}`);
      if (attempt === retries) {
        throw error;
      }
      // Wait with backoff
      await new Promise(resolve => setTimeout(resolve, delay * Math.pow(2, attempt - 1)));
      attempt++;
    }
  }
}

module.exports = async (req, res) => {
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST');
    return res.status(405).json({ error: 'Method Not Allowed' });
  }

  // 1. Bearer Authentication Check
  const authHeader = req.headers?.authorization;
  const expectedSecret = process.env.TYPEBOT_WEBHOOK_SECRET;

  if (!expectedSecret) {
    console.error('Server Configuration Error: TYPEBOT_WEBHOOK_SECRET is not set.');
    return res.status(500).json({ error: 'Server Configuration Error' });
  }

  if (!authHeader || authHeader !== `Bearer ${expectedSecret}`) {
    return res.status(401).json({ error: 'Unauthorized: Invalid or missing token' });
  }

  // 2. Payload Extraction and Validation
  const { name, company, whatsapp, email, budget } = req.body || {};

  // Check required fields
  if (!name || !company || !whatsapp || !email || !budget) {
    return res.status(400).json({
      error: 'Bad Request: Fields (name, company, whatsapp, email, budget) are all required and cannot be empty.'
    });
  }

  // Email format validation
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email)) {
    return res.status(400).json({ error: 'Bad Request: Invalid email format.' });
  }

  // Budget option validation
  const allowedBudgets = ['Até 2k', '2k a 5k', 'Acima de 5k'];
  if (!allowedBudgets.includes(budget)) {
    return res.status(400).json({
      error: `Bad Request: Invalid budget option. Allowed values: ${allowedBudgets.join(', ')}`
    });
  }

  // Clean WhatsApp number
  const cleanedWhatsapp = whatsapp.replace(/\D/g, '');
  if (cleanedWhatsapp.length < 8 || cleanedWhatsapp.length > 15) {
    return res.status(400).json({
      error: 'Bad Request: WhatsApp number must contain between 8 and 15 digits.'
    });
  }
  const whatsappUrl = `https://wa.me/${cleanedWhatsapp}`;

  const databaseId = process.env.NOTION_DATABASE_ID;
  if (!databaseId) {
    console.error('Server Configuration Error: NOTION_DATABASE_ID is not set.');
    return res.status(500).json({ error: 'Server Configuration Error' });
  }

  // 3. Database Insertion with Retries
  try {
    const notionPromise = () => notion.pages.create({
      parent: { database_id: databaseId },
      properties: {
        Name: {
          title: [
            {
              text: {
                content: name
              }
            }
          ]
        },
        Company: {
          rich_text: [
            {
              text: {
                content: company
              }
            }
          ]
        },
        WhatsApp: {
          url: whatsappUrl
        },
        Email: {
          email: email
        },
        Budget: {
          select: {
            name: budget
          }
        },
        Status: {
          select: {
            name: '1. Triagem (Typebot)'
          }
        }
      }
    });

    const response = await retryWithBackoff(notionPromise, 3, 500);

    return res.status(201).json({
      status: 'success',
      message: 'Lead created successfully',
      id: response.id
    });
  } catch (error) {
    console.error('Failed to create lead in Notion database after retries:', error);
    return res.status(502).json({
      error: 'Bad Gateway: Failed to store lead in Notion CRM database.',
      details: error.message
    });
  }
};
