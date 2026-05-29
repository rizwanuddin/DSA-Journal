#!/bin/bash

# ============================================================
#   DSA Journal - Mac Setup Script
#   Run this on your macOS laptop to get everything installed
#   Usage: bash setup_mac.sh
# ============================================================

echo ""
echo "=============================="
echo "  DSA Journal - Mac Setup"
echo "=============================="
echo ""

# --- 1. Xcode Command Line Tools (needed for Git + compilers) ---
echo ">>> Installing Xcode Command Line Tools..."
xcode-select --install 2>/dev/null || echo "    Already installed, skipping."
echo ""

# --- 2. Homebrew (Mac package manager) ---
if ! command -v brew &>/dev/null; then
  echo ">>> Installing Homebrew..."
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  # Add brew to PATH for Apple Silicon Macs
  echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
  eval "$(/opt/homebrew/bin/brew shellenv)"
else
  echo ">>> Homebrew already installed. Updating..."
  brew update
fi
echo ""

# --- 3. Git ---
echo ">>> Installing Git..."
brew install git
echo ""

# Prompt for Git identity
echo ">>> Setting up Git identity..."
read -p "    Enter your name for Git (e.g. Ridwan): " git_name
read -p "    Enter your GitHub email: " git_email
git config --global user.name "$git_name"
git config --global user.email "$git_email"
git config --global init.defaultBranch main
echo "    Git identity set!"
echo ""

# --- 4. Python 3 ---
echo ">>> Installing Python 3..."
brew install python
echo ""
echo "    Python version: $(python3 --version)"
echo ""

# --- 5. Java (JDK 21 - LTS) ---
echo ">>> Installing Java (JDK 21)..."
brew install --cask temurin@21
echo ""
echo "    Java version: $(java -version 2>&1 | head -n 1)"
echo ""

# --- 6. VS Code (if not already installed) ---
if ! command -v code &>/dev/null; then
  echo ">>> Installing VS Code..."
  brew install --cask visual-studio-code
else
  echo ">>> VS Code already installed, skipping."
fi
echo ""

# --- 7. Useful Python packages for DSA ---
echo ">>> Installing Python packages..."
pip3 install --upgrade pip
pip3 install pytest          # run Python tests easily
pip3 install ipython         # better interactive Python shell
echo ""

# --- 8. VS Code Extensions ---
echo ">>> Installing VS Code extensions..."
code --install-extension ms-python.python              # Python support
code --install-extension ms-python.debugpy             # Python debugger
code --install-extension redhat.java                   # Java support
code --install-extension vscjava.vscode-java-pack      # Java full pack
code --install-extension eamodio.gitlens               # Git superpowers
code --install-extension streetsidesoftware.code-spell-checker  # typo checker
echo ""

# --- 9. Done ---
echo "=============================="
echo "  Setup Complete!"
echo "=============================="
echo ""
echo "  Next steps:"
echo "  1. Restart your terminal"
echo "  2. Run: git clone https://github.com/rizwanuddin/DSA-Journal.git"
echo "  3. cd DSA-Journal && code ."
echo ""
echo "  Verify installs:"
echo "  - git --version"
echo "  - python3 --version"
echo "  - java -version"
echo ""