#!/usr/bin/env python

import os
import subprocess
import sys

def set_env_variables():
    try:
        with open('.env') as f:
            for line in f:
                key, value = line.strip().split('=')
                os.environ[key] = value
        print("[INFO] STEP 1: Setting environment variables... DONE")
    except FileNotFoundError:
        print("[ERROR] STEP 1: Config file not found.")
        sys.exit(1)
    except ValueError:
        print("[ERROR] STEP 1: Invalid format in config file.")
        sys.exit(1)

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
