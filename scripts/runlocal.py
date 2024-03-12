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

def install_requirements():
    try:
        subprocess.run(['pip', 'install', '-r', 'requirements.txt'], check=True, stdout=subprocess.DEVNULL)
        print("[INFO] STEP 2: Installing dependencies... DONE")
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] STEP 2: Failed to install dependencies: {e}")
        sys.exit(1)

def run_local_server():
    try:
        print("[INFO] STEP 3: Running local server...\n")
        subprocess.run(['python', 'manage.py', 'runserver', '0.0.0.0:8000'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] STEP 3: Failed to run local app: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n[INFO] KeyboardInterrupt: BanQuest app stopped.")
        sys.exit(0)

def main():
    print("\n🚀 Starting BanQuest Django App Setup...\n")
    set_env_variables()
    install_requirements()
    run_local_server()

if __name__ == "__main__":
    main()
