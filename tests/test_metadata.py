import unittest, yaml, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class MetadataTests(unittest.TestCase):
    def test_component_count_and_unique_ids(self):
        d=yaml.safe_load((ROOT/'metadata/components.yaml').read_text(encoding='utf-8'))
        self.assertGreaterEqual(len(d['components']),31)
        ids=[x['id'] for x in d['components']]
        self.assertEqual(len(ids),len(set(ids)))
    def test_platform_ids(self):
        d=yaml.safe_load((ROOT/'metadata/platforms.yaml').read_text(encoding='utf-8'))
        self.assertEqual({p['id'] for p in d['platforms']},{'web','android','harmonyos','ios','windows','linux-gtk','linux-qt'})
    def test_baseline_excludes_expressive(self):
        d=yaml.safe_load((ROOT/'metadata/md3-baseline.yaml').read_text(encoding='utf-8'))
        self.assertTrue(any('Expressive' in x for x in d['policy']['exclude']))
if __name__=='__main__': unittest.main()
