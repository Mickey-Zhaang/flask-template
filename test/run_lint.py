"""
Easy Linting
"""

import subprocess

subprocess.run(["pylint", "website"], check=True)
