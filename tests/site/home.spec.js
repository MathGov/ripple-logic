const { test, expect } = require('@playwright/test');
const AxeBuilder = require('@axe-core/playwright').default;

for (const width of [390, 1280]) {
  test(`readable, accessible library at ${width}px`, async ({ page }) => {
    await page.setViewportSize({ width, height: 844 });
    await page.goto('/');
    await expect(page.locator('.document:visible')).toHaveCount(15);
    expect(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth)).toBe(true);
    const results = await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21aa']).analyze();
    expect(results.violations).toEqual([]);
    await page.getByLabel('Find a component by name or edition').fill('sentience');
    await expect(page.locator('.document:visible')).toHaveCount(1);
    await expect(page.getByRole('status')).toHaveText('1 of 15 components');
    await page.getByLabel('Find a component by name or edition').fill('does-not-exist');
    await expect(page.locator('#no-results')).toBeVisible();
    await page.getByRole('button', { name: 'Clear', exact: true }).click();
    await expect(page.locator('.document:visible')).toHaveCount(15);
    await expect(page.getByLabel('Find a component by name or edition')).toBeFocused();
    await page.getByRole('link', {name: 'Read the introduction'}).click();
    await expect(page).toHaveURL(/MATHGOV_3R_1_2_PUBLIC_INTRO_v13.0.html$/);
    expect((await page.textContent('body')).length).toBeGreaterThan(1000);
  });
}
test('library remains usable without JavaScript', async ({ browser }) => {
  const context = await browser.newContext({javaScriptEnabled:false});
  const page = await context.newPage();
  await page.goto('http://127.0.0.1:4173/');
  await expect(page.locator('.document')).toHaveCount(15);
  await expect(page.locator('#search-controls')).toBeHidden();
  await expect(page.getByRole('link', {name: 'Read the introduction'})).toBeVisible();
  await context.close();
});
