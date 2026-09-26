const { defineConfig } = require('@playwright/test');
module.exports = defineConfig({
  testDir: './tests/site',
  timeout: 30000,
  use: { baseURL: 'http://127.0.0.1:4173', browserName: 'chromium', channel: process.env.PLAYWRIGHT_CHANNEL || undefined },
  webServer: { command: 'node scripts/serve_site.js', port: 4173, reuseExistingServer: false },
  reporter: 'list'
});
