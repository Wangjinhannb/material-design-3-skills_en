import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';
test('catalog has no serious WCAG violations',async({page})=>{await page.goto('/examples/component-catalog/web/');const results=await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21a','wcag21aa','wcag22aa']).analyze();expect(results.violations.filter(v=>['serious','critical'].includes(v.impact))).toEqual([]);});
