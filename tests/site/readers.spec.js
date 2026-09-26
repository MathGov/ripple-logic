const { test, expect } = require('@playwright/test');
const AxeBuilder = require('@axe-core/playwright').default;
const manifest = require('../../releases/v13.0-release-i/VERSION_MANIFEST.json');
for (const component of manifest.components.filter(item => item.path.endsWith('.docx'))) {
  const filename = component.path.split('/').pop().replace('.docx', '.html');
  test(`reader: ${component.component}`, async ({ page }) => {
    test.setTimeout(90000);
    await page.goto('/read/' + filename);
    await expect(page.getByRole('link', {name:'Original frozen HTML'})).toHaveAttribute('href', '../Reading_HTML/' + filename);
    if (component.component === 'RippleLogic Canon') {
      for (const id of ['p-3404','p-3405']) {
        await expect(page.locator(`#${id} a`)).toHaveCount(1);
        await expect(page.locator(`#${id} a`)).toHaveAttribute('href', /clang=_en$/);
      }
    }
    for (const width of [320, 390, 768, 1280]) {
      await page.setViewportSize({width, height:844});
      expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), `page overflow at ${width}px`).toBe(true);
    }
    await page.setViewportSize({width:390, height:844});
    const table = page.locator('.table-wrap').first();
    if (await table.count()) {
      await table.focus();
      await page.keyboard.press('ArrowRight');
      await expect.poll(() => table.evaluate(node => node.scrollLeft)).toBeGreaterThan(0);
    }
    const results = await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21aa']).analyze();
    expect(results.violations).toEqual([]);
    await page.locator('details.historical').evaluateAll(nodes => nodes.forEach(node => node.open = true));
    expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), 'historical appendix overflow').toBe(true);
  });
}
test('installation is formatted and accessible on mobile', async ({page}) => {
  await page.setViewportSize({width:390,height:844});
  await page.goto('/installation.html');
  await expect(page.getByRole('heading', {level:1})).toHaveText('Reproduce Release I');
  await expect(page.locator('pre').first()).toContainText('git clone');
  expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)).toBe(true);
  expect((await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21aa']).analyze()).violations).toEqual([]);
});
test('full-text search opens the exact passage and handles empty results', async ({page}) => {
  await page.setViewportSize({width:390,height:844});
  await page.goto('/search.html');
  await page.getByLabel('Words to find').fill('ranking cannot rescue');
  await page.getByRole('button', {name:'Search',exact:true}).click();
  await expect(page.locator('.search-result').first()).toBeVisible();
  await page.getByLabel('Document', {exact:true}).selectOption({label:'Public Introduction'});
  const link = page.locator('.search-result a').first();
  await expect(link).toHaveAttribute('href', /read\/MATHGOV_3R_1_2_PUBLIC_INTRO_v13.0.html#p-/);
  expect((await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21aa']).analyze()).violations).toEqual([]);
  expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)).toBe(true);
  await link.click();
  await expect(page.locator(':target')).toContainText(/ranking cannot rescue/i);
  await page.goto('/search.html?q=nonexistentterm987654');
  await expect(page.getByRole('status')).toContainText('No matching passages');
});
test('search reports download failure and retries successfully', async ({page}) => {
  await page.route('**/search-index.json', route => route.abort());
  await page.goto('/search.html?q=ranking');
  await expect(page.getByRole('status')).toContainText('could not load');
  await page.unroute('**/search-index.json');
  await page.getByRole('button', {name:'Search',exact:true}).click();
  await expect(page.locator('.search-result').first()).toBeVisible();
});
