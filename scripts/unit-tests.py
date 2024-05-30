#!/usr/bin/env python

import os
import subprocess
import sys

def set_env_variables():
    os.environ["ENV"] = "unit-tests"
    print("[INFO] STEP 1: Setting environment variable for unit tests... DONE")

def run_local_tests():
    try:
        print("[INFO] STEP 2: Running local tests...\n")
        subprocess.run(['python', 'manage.py', 'test'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] STEP 2: Failed to run some unit test: {e}")
        sys.exit(1)

def main():
    print("\n🚀 Starting BanQuest Django App unit tests...\n")
    set_env_variables()
    run_local_tests()
    print("[INFO] Running tests complete!\n")

if __name__ == "__main__":
    main()
