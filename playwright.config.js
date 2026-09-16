const { defineConfig } = require('@playwright/test');

module.exports = defineConfig({
  testDir: './tests/E2E',
  use: {
    headless: true,
  },
});
