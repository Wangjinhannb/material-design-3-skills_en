import subprocess, sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class CatalogCoverageTests(unittest.TestCase):
    def test_catalog_coverage(self):
        subprocess.run([sys.executable,str(ROOT/'tools/validators/validate_catalog_coverage.py')],cwd=ROOT,check=True)
if __name__=='__main__': unittest.main()
