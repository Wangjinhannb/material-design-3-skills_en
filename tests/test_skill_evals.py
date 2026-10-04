import unittest, yaml
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class SkillEvalTests(unittest.TestCase):
    def test_required_platform_coverage(self):
        d=yaml.safe_load((ROOT/'tests/skill/eval-cases.yaml').read_text(encoding='utf-8'))
        plats={x['expected_platform'] for x in d['cases']}
        self.assertTrue({'web','android','harmonyos','ios','windows'}.issubset(plats))
    def test_no_empty_forbidden_lists(self):
        d=yaml.safe_load((ROOT/'tests/skill/eval-cases.yaml').read_text(encoding='utf-8'))
        self.assertTrue(all(x['forbidden'] for x in d['cases']))
if __name__=='__main__': unittest.main()
