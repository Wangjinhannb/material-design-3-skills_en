import { test, expect } from '@playwright/test';
test('catalog visual baseline',async({page})=>{await page.goto('/examples/component-catalog/web/');await expect(page).toHaveScreenshot('catalog.png',{fullPage:true,animations:'disabled',caret:'hide',maxDiffPixelRatio:0.01});});
