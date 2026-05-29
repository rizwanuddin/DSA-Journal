# 🍎 Mac Setup Guide — DSA Journal

Everything you need to get this repo running on a fresh Mac from scratch.

---

## ⚡ Quick Install (Recommended)

Just run the setup script — it installs everything automatically:

```bash
bash setup_mac.sh
```

Then restart Terminal and you're good. Skip to **Step 4** below.

---

## 🔧 Manual Install (Step by Step)

### Step 1: Install Homebrew
Homebrew is Mac's package manager — like an app store for the terminal.

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

After it installs, restart Terminal.

---

### Step 2: Install Git, Python, Java

```bash
brew install git
brew install python
brew install --cask temurin@21
```

Verify they all installed:
```bash
git --version
python3 --version
java -version
```

---

### Step 3: Install VS Code

```bash
brew install --cask visual-studio-code
```

Or download manually from **code.visualstudio.com**

---

### Step 4: Set Git Identity (do this once)

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

Use the same email as your GitHub account.

---

### Step 5: Clone the Repo

```bash
cd ~
git clone https://github.com/rizwanuddin/DSA-Journal.git
cd DSA-Journal
code .
```

---

### Step 6: Install VS Code Extensions

```bash
code --install-extension ms-python.python
code --install-extension ms-python.debugpy
code --install-extension redhat.java
code --install-extension vscjava.vscode-java-pack
code --install-extension eamodio.gitlens
```

---

## 📅 Daily Workflow

```bash
# Before you start
cd ~/DSA-Journal
git pull

# After you're done
git add .
git commit -m "what you did"
git push
```

---

## ⌨️ Shortcuts

### Terminal (Mac)

| What it does | Shortcut |
|---|---|
| Clear screen | `Cmd + K` or `clear` |
| Cancel running command | `Ctrl + C` |
| Previous command | `Up Arrow` |
| Search command history | `Ctrl + R` |
| Go to start of line | `Ctrl + A` |
| Go to end of line | `Ctrl + E` |
| Go back a folder | `cd ..` |
| See files in folder | `ls` |
| See current folder path | `pwd` |
| Open folder in VS Code | `code .` |

---

### VS Code (Mac)

| What it does | Shortcut |
|---|---|
| Open terminal inside VS Code | `` Ctrl + ` `` |
| Command palette | `Cmd + Shift + P` |
| Quick open file | `Cmd + P` |
| Comment / uncomment line | `Cmd + /` |
| Move line up / down | `Option + Up/Down` |
| Duplicate line | `Option + Shift + Down` |
| Find in file | `Cmd + F` |
| Find across all files | `Cmd + Shift + F` |
| Format / auto-indent code | `Option + Shift + F` |
| Go to definition | `F12` |
| Rename variable everywhere | `F2` |
| Split editor | `Cmd + \` |
| Multi-cursor | `Option + Click` |
| Select all occurrences | `Cmd + Shift + L` |
| Zen mode | `Cmd + K Z` |
| Save file | `Cmd + S` |
| Close tab | `Cmd + W` |
| Undo | `Cmd + Z` |

---

### VS Code (Windows) — for reference

| What it does | Shortcut |
|---|---|
| Open terminal inside VS Code | `` Ctrl + ` `` |
| Command palette | `Ctrl + Shift + P` |
| Quick open file | `Ctrl + P` |
| Comment / uncomment line | `Ctrl + /` |
| Move line up / down | `Alt + Up/Down` |
| Duplicate line | `Alt + Shift + Down` |
| Find in file | `Ctrl + F` |
| Find across all files | `Ctrl + Shift + F` |
| Format / auto-indent code | `Alt + Shift + F` |
| Go to definition | `F12` |
| Rename variable everywhere | `F2` |
| Split editor | `Ctrl + \` |
| Multi-cursor | `Alt + Click` |
| Select all occurrences | `Ctrl + Shift + L` |
| Zen mode | `Ctrl + K Z` |
| Save file | `Ctrl + S` |
| Close tab | `Ctrl + W` |
| Undo | `Ctrl + Z` |

---

## 🐍 Running Code

```bash
# Python
python3 filename.py

# Java
javac filename.java   # compile
java filename         # run
```

---

*Drop this file in your DSA-Journal folder so it syncs to both laptops.*