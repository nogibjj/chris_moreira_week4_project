import os
import sys
import re


def main_function():
    python_version = re.search(r"\d+\.\d+", sys.version).group()
    os_name = os.getenv("RUNNER_OS")
    return python_version, os_name
