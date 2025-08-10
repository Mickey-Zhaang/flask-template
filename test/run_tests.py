"""
Easy Testing
"""

import subprocess

subprocess.run(
    ["pytest", "-s", "--cov=website.", "--cov-report=term-missing", "-v"], check=True
)
