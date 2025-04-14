# colab.py

import os
import subprocess
import sys

# Define the path to the TATAprog folder
# (This must be consistent with the installation; we assume TATAprog is installed in .program/TATAprog)
tata_prog_path = "/content/.program/TATAprog"

def run_app(ngrok_token=None):
    print("Launching TATAprog UI...")
    
    # The launcher uses run.py as the entry point.
    # We use a shell command (colab magic not available in regular Python, so we simulate similar behavior)
    command = f"python3 run.py --N {ngrok_token if ngrok_token else ''}"
    
    # Change directory to tata_prog_path and run the command
    os.chdir(tata_prog_path)
    subprocess.run(command, shell=True)

if __name__ == '__main__':
    # Optionally, you can pass a token via command-line arguments
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--N', type=str, default=None, help='NGROK token (optional)')
    args = parser.parse_args()
    
    run_app(args.N)
