import unittest, json, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class TokenTests(unittest.TestCase):
    def test_color_roles(self):
        for fn in ['color-light.tokens.json','color-dark.tokens.json']:
            d=json.loads((ROOT/'tokens/source'/fn).read_text(encoding='utf-8'))
            for role in ['primary','onPrimary','surface','onSurface','surfaceContainer','outline','error','onError']:
                self.assertIn(role,d['color'])
    def test_generator_runs(self):
        subprocess.run([sys.executable,str(ROOT/'tools/token_generator/generate.py')],check=True)
        self.assertTrue((ROOT/'tokens/generated/web/tokens.css').exists())
if __name__=='__main__': unittest.main()
