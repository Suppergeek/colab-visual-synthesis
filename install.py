# install.py

import os
import subprocess
import sys

# Define repo link and target directory
repo_link = "https://github.com/yourusername/colab-visual-synthesis.git"
install_path = "/content/colab-visual-synthesis"

# Clone the repo if not already present
if not os.path.exists(install_path):
    print("Cloning colab-visual-synthesis repo...")
    subprocess.run(["git", "clone", repo_link, install_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Change to repo directory
os.chdir(install_path)

# Pull the latest changes in case repo is already cloned
print("Pulling latest changes from GitHub...")
subprocess.run(["git", "pull"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Install dependencies from TATAprog's requirements.txt
tata_prog_path = "/content/.program/TATAprog"
req_file = os.path.join(tata_prog_path, "requirements.txt")
if os.path.exists(req_file):
    print("Installing dependencies from TATAprog...")
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", req_file])
else:
    print("No requirements.txt found in TATAprog; skipping dependency installation.")

print("Installation complete.")
