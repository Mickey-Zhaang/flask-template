"""
Easy Testing: run `python tests/run_tests.py` to get report
"""

import subprocess

subprocess.run(
    ["pytest", "-s", "--cov=website.", "--cov-report=term-missing", "-v"], check=True
)
