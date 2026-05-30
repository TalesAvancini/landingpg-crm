const assert = require('assert');

// Store original environment variables to restore them later
const originalEnv = { ...process.env };

// Mocking @notionhq/client in Node.js require cache
let mockShouldFail = false;
let mockFailAttempts = 0;
let mockPageCreateCallCount = 0;
let lastPageCreatePayload = null;

const mockPagesCreate = {
  create: async (payload) => {
    mockPageCreateCallCount++;
    lastPageCreatePayload = payload;
    if (mockShouldFail) {
      mockFailAttempts--;
      if (mockFailAttempts >= 0) {
        throw new Error('Notion API connection error');
      }
    }
    return { id: 'mock-page-id-12345' };
  }
};

require.cache[require.resolve('@notionhq/client')] = {
  exports: {
    Client: class {
      constructor() {
        this.pages = mockPagesCreate;
      }
    }
  }
};

// Import the endpoint (which imports the mocked client)
const handler = require('../api/webhook-intake');

// Helper to create mocked response object
function createMockResponse() {
  const res = {
    statusCode: 200,
    headers: {},
    body: null,
    status(code) {
      this.statusCode = code;
      return this;
    },
    json(obj) {
      this.body = obj;
      return this;
    },
    setHeader(name, value) {
      this.headers[name] = value;
      return this;
    }
  };
  return res;
}

async function runTests() {
  console.log('🧪 Starting Webhook Intake Unit Tests...');

  // Setup default environment variables for testing
  process.env.TYPEBOT_WEBHOOK_SECRET = 'supersecret';
  process.env.NOTION_DATABASE_ID = 'db-id-abc';

  // --- Test Case 1: Method not allowed (GET) ---
  {
    const req = { method: 'GET' };
    const res = createMockResponse();
    await handler(req, res);
    assert.strictEqual(res.statusCode, 405);
    assert.strictEqual(res.body.error, 'Method Not Allowed');
    assert.strictEqual(res.headers['Allow'], 'POST');
    console.log('✅ Test 1: Method Not Allowed passed.');
  }

  // --- Test Case 2: Config missing secret ---
  {
    delete process.env.TYPEBOT_WEBHOOK_SECRET;
    const req = { method: 'POST' };
    const res = createMockResponse();
    await handler(req, res);
    assert.strictEqual(res.statusCode, 500);
    assert.strictEqual(res.body.error, 'Server Configuration Error');
    process.env.TYPEBOT_WEBHOOK_SECRET = 'supersecret'; // Restore
    console.log('✅ Test 2: Server configuration check passed.');
  }

  // --- Test Case 3: Unauthorized token ---
  {
    const req = {
      method: 'POST',
      headers: { authorization: 'Bearer wrongsecret' }
    };
    const res = createMockResponse();
    await handler(req, res);
    assert.strictEqual(res.statusCode, 401);
    assert.match(res.body.error, /Unauthorized/);
    console.log('✅ Test 3: Unauthorized Bearer validation passed.');
  }

  // --- Test Case 4: Missing required fields ---
  {
    const req = {
      method: 'POST',
      headers: { authorization: 'Bearer supersecret' },
      body: { name: 'John Doe', email: 'john@example.com' } // Missing WhatsApp, Company, Budget
    };
    const res = createMockResponse();
    await handler(req, res);
    assert.strictEqual(res.statusCode, 400);
    assert.match(res.body.error, /Bad Request: Fields.*required/);
    console.log('✅ Test 4: Missing required fields validation passed.');
  }

  // --- Test Case 5: Invalid email format ---
  {
    const req = {
      method: 'POST',
      headers: { authorization: 'Bearer supersecret' },
      body: {
        name: 'John Doe',
        company: 'ACME',
        whatsapp: '11988887777',
        email: 'invalid-email',
        budget: 'Até 2k'
      }
    };
    const res = createMockResponse();
    await handler(req, res);
    assert.strictEqual(res.statusCode, 400);
    assert.strictEqual(res.body.error, 'Bad Request: Invalid email format.');
    console.log('✅ Test 5: Invalid email format check passed.');
  }

  // --- Test Case 6: Invalid budget option ---
  {
    const req = {
      method: 'POST',
      headers: { authorization: 'Bearer supersecret' },
      body: {
        name: 'John Doe',
        company: 'ACME',
        whatsapp: '11988887777',
        email: 'john@example.com',
        budget: '10k a 20k' // Wrong option
      }
    };
    const res = createMockResponse();
    await handler(req, res);
    assert.strictEqual(res.statusCode, 400);
    assert.match(res.body.error, /Bad Request: Invalid budget option/);
    console.log('✅ Test 6: Invalid budget option check passed.');
  }

  // --- Test Case 7: Invalid WhatsApp number (too short) ---
  {
    const req = {
      method: 'POST',
      headers: { authorization: 'Bearer supersecret' },
      body: {
        name: 'John Doe',
        company: 'ACME',
        whatsapp: '12345', // Too short
        email: 'john@example.com',
        budget: 'Até 2k'
      }
    };
    const res = createMockResponse();
    await handler(req, res);
    assert.strictEqual(res.statusCode, 400);
    assert.match(res.body.error, /WhatsApp number must contain between/);
    console.log('✅ Test 7: WhatsApp number length validation passed.');
  }

  // --- Test Case 8: Success Flow with Number Formatting ---
  {
    mockPageCreateCallCount = 0;
    mockShouldFail = false;
    const req = {
      method: 'POST',
      headers: { authorization: 'Bearer supersecret' },
      body: {
        name: 'John Doe',
        company: 'ACME Corp',
        whatsapp: '+55 (11) 98888-7777', // Needs cleaning
        email: 'john@example.com',
        budget: '2k a 5k'
      }
    };
    const res = createMockResponse();
    await handler(req, res);

    assert.strictEqual(res.statusCode, 201);
    assert.strictEqual(res.body.status, 'success');
    assert.strictEqual(res.body.id, 'mock-page-id-12345');
    assert.strictEqual(mockPageCreateCallCount, 1);
    
    // Check formatted properties
    assert.strictEqual(lastPageCreatePayload.parent.database_id, 'db-id-abc');
    assert.strictEqual(lastPageCreatePayload.properties.Name.title[0].text.content, 'John Doe');
    assert.strictEqual(lastPageCreatePayload.properties.Company.rich_text[0].text.content, 'ACME Corp');
    assert.strictEqual(lastPageCreatePayload.properties.WhatsApp.url, 'https://wa.me/5511988887777'); // Sanitized!
    assert.strictEqual(lastPageCreatePayload.properties.Email.email, 'john@example.com');
    assert.strictEqual(lastPageCreatePayload.properties.Budget.select.name, '2k a 5k');
    assert.strictEqual(lastPageCreatePayload.properties.Status.select.name, '1. Triagem (Typebot)');
    console.log('✅ Test 8: Success flow & payload mapping validation passed.');
  }

  // --- Test Case 9: Resilience / Retries success after failure ---
  {
    mockPageCreateCallCount = 0;
    mockShouldFail = true;
    mockFailAttempts = 2; // Fails twice, succeeds on 3rd attempt
    
    const req = {
      method: 'POST',
      headers: { authorization: 'Bearer supersecret' },
      body: {
        name: 'Jane Doe',
        company: 'Globex',
        whatsapp: '5511999998888',
        email: 'jane@globex.com',
        budget: 'Acima de 5k'
      }
    };
    const res = createMockResponse();
    
    const startTime = Date.now();
    await handler(req, res);
    const duration = Date.now() - startTime;

    assert.strictEqual(res.statusCode, 201);
    assert.strictEqual(res.body.status, 'success');
    assert.strictEqual(mockPageCreateCallCount, 3); // 2 failures + 1 success
    assert.ok(duration >= 1500, `Expected delay between backoffs (duration: ${duration}ms)`);
    console.log('✅ Test 9: Resilience with successful exponential backoff passed.');
  }

  // --- Test Case 10: Retries exhausted and failure response ---
  {
    mockPageCreateCallCount = 0;
    mockShouldFail = true;
    mockFailAttempts = 4; // Exceeds limit of 3
    
    const req = {
      method: 'POST',
      headers: { authorization: 'Bearer supersecret' },
      body: {
        name: 'Error Lead',
        company: 'Broken LLC',
        whatsapp: '5511999998888',
        email: 'err@broken.com',
        budget: 'Acima de 5k'
      }
    };
    const res = createMockResponse();
    await handler(req, res);

    assert.strictEqual(res.statusCode, 502);
    assert.strictEqual(res.body.error, 'Bad Gateway: Failed to store lead in Notion CRM database.');
    assert.strictEqual(res.body.details, 'Notion API connection error');
    assert.strictEqual(mockPageCreateCallCount, 3); // 3 attempts and then gave up
    console.log('✅ Test 10: Retry failure exhaustion passed.');
  }

  console.log('\n🎉 ALL WEBHOOK INTAKE TESTS PASSED SUCCESSFULLY! 🎉');
  
  // Restore environment variables
  process.env = { ...originalEnv };
}

runTests().catch(err => {
  console.error('❌ TEST SUITE FAILED:', err);
  process.exit(1);
});
