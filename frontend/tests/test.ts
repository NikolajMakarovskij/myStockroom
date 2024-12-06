import { expect, test } from '@playwright/test'

test('home page has expected components in header', async ({ page }) => {
  await page.goto('/')
})
