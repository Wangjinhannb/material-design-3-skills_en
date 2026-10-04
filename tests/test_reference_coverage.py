import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class ReferenceCoverageTests(unittest.TestCase):
    def test_reference_app_sections(self):
        subprocess.run([sys.executable, str(ROOT / 'tools/validators/validate_reference_coverage.py')], check=True)

if __name__ == '__main__':
    unittest.main()
