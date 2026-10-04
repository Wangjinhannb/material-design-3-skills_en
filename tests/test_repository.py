import unittest, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class RepositoryTests(unittest.TestCase):
    def test_validator(self):
        subprocess.run([sys.executable,str(ROOT/'tools/validators/validate_repo.py')],check=True)
if __name__=='__main__': unittest.main()
