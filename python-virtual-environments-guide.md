# Python Virtual Environment Management Guide

## Table of Contents
- [Introduction](#introduction)
- [Pyenv Installation](#pyenv-installation)
- [Managing Python Versions](#managing-python-versions)
- [Virtual Environments with Pyenv](#virtual-environments-with-pyenv)
- [Common Workflows](#common-workflows)
- [Alternative Tools](#alternative-tools)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)
- [Quick Reference](#quick-reference)

---

## Introduction

### What is Pyenv?

`pyenv` is a powerful Python version management tool that allows you to:
- Install and manage multiple Python versions on the same system
- Switch between Python versions seamlessly
- Create isolated virtual environments per project
- Set Python versions globally, locally (per-directory), or per-shell session

### Why Use Virtual Environments?

Virtual environments provide:
- **Isolation**: Each project has its own dependencies
- **Reproducibility**: Consistent environments across different machines
- **Version Control**: Different projects can use different package versions
- **Clean System**: Avoid polluting system Python installation

---

## Pyenv Installation

### macOS Installation

```bash
# Install using Homebrew
brew update
brew install pyenv

# Add to shell configuration (~/.zshrc for zsh or ~/.bash_profile for bash)
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc

# Reload shell configuration
source ~/.zshrc
```

### Linux Installation

```bash
# Install using pyenv-installer
curl https://pyenv.run | bash

# Add to shell configuration (~/.bashrc or ~/.zshrc)
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc

# Reload shell configuration
source ~/.bashrc

# Install build dependencies (Ubuntu/Debian)
sudo apt-get update
sudo apt-get install -y build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

### Verify Installation

```bash
pyenv --version
```

---

## Managing Python Versions

### Listing Available Versions

```bash
# List all available Python versions
pyenv install --list

# List only stable releases (filter out dev/rc versions)
pyenv install --list | grep "^\s*[0-9]"

# Search for specific version
pyenv install --list | grep "3.11"
pyenv install --list | grep "3.12"
```

### Installing Python Versions

```bash
# Install specific version
pyenv install 3.11.7

# Install latest patch version
pyenv install 3.11

# Install multiple versions
pyenv install 3.9.18
pyenv install 3.10.13
pyenv install 3.11.7
pyenv install 3.12.1

# Install with verbose output (for debugging)
pyenv install -v 3.11.7
```

### Listing Installed Versions

```bash
# Show all installed Python versions
pyenv versions

# Show currently active version
pyenv version

# Example output:
#   system
# * 3.11.7 (set by /Users/username/.pyenv/version)
#   3.10.13
```

### Uninstalling Python Versions

```bash
# Uninstall a specific version
pyenv uninstall 3.9.18

# Force uninstall without confirmation
pyenv uninstall -f 3.9.18
```

### Switching Python Versions

#### Global (System-wide)

```bash
# Set global Python version for all shells
pyenv global 3.11.7

# Set multiple versions (fallback order)
pyenv global 3.11.7 3.10.13

# Check current global version
pyenv global
```

#### Local (Project-specific)

```bash
# Set Python version for current directory and subdirectories
pyenv local 3.11.7

# This creates a .python-version file in the current directory
# Pyenv automatically switches to this version when you cd into the directory

# Check local version
pyenv local

# Remove local version setting
pyenv local --unset
```

#### Shell (Current Session Only)

```bash
# Set Python version for current shell session only
pyenv shell 3.11.7

# Unset shell version
pyenv shell --unset

# Check shell version
pyenv shell
```

#### Version Priority

Pyenv uses the following priority order (highest to lowest):
1. **Shell** - `pyenv shell`
2. **Local** - `.python-version` file in current or parent directories
3. **Global** - `~/.pyenv/version` file

---

## Virtual Environments with Pyenv

### Installing Pyenv-virtualenv Plugin

```bash
# On macOS
brew install pyenv-virtualenv

# On Linux
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv

# Add to shell configuration (~/.zshrc or ~/.bashrc)
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc
source ~/.zshrc
```

### Creating Virtual Environments

```bash
# Create virtualenv with specific Python version
pyenv virtualenv 3.11.7 myproject-env

# Create with current active Python version
pyenv virtualenv myenv

# Create from any installed version
pyenv virtualenv 3.10.13 data-science-env
pyenv virtualenv 3.11.7 django-app-env
```

### Activating Virtual Environments

```bash
# Manual activation
pyenv activate myproject-env

# Deactivate
pyenv deactivate

# Auto-activate when entering directory (recommended)
cd /path/to/project
pyenv local myproject-env
# Now the environment activates automatically when you cd into this directory
```

### Listing Virtual Environments

```bash
# List all virtual environments
pyenv virtualenvs

# List with full paths
pyenv virtualenvs --bare

# Example output:
#   3.11.7/envs/myproject-env (created from /Users/username/.pyenv/versions/3.11.7)
#   myproject-env (created from /Users/username/.pyenv/versions/3.11.7)
```

### Deleting Virtual Environments

```bash
# Delete a virtualenv
pyenv virtualenv-delete myproject-env

# Alternative method
pyenv uninstall myproject-env
```

---

## Common Workflows

### Workflow 1: Starting a New Project

```bash
# 1. Create and navigate to project directory
mkdir my-awesome-project
cd my-awesome-project

# 2. Install desired Python version (if not already installed)
pyenv install 3.11.7

# 3. Create a virtual environment for this project
pyenv virtualenv 3.11.7 my-awesome-project-env

# 4. Set local Python version (creates .python-version file)
pyenv local my-awesome-project-env

# 5. Verify setup
python --version
which python
pip --version

# 6. Upgrade pip and install tools
pip install --upgrade pip setuptools wheel

# 7. Install project dependencies
pip install -r requirements.txt

# 8. Start coding!
```

### Workflow 2: Cloning an Existing Project

```bash
# 1. Clone the repository
git clone https://github.com/username/project.git
cd project

# 2. Check if .python-version exists
cat .python-version
# Output: 3.11.7 or myproject-env

# 3. Install the Python version if needed
pyenv install $(cat .python-version)

# 4. If it specifies a virtualenv name, create it
pyenv virtualenv 3.11.7 $(cat .python-version)

# 5. Environment auto-activates when you cd into directory

# 6. Install dependencies
pip install -r requirements.txt
```

### Workflow 3: Testing Across Multiple Python Versions

```bash
# 1. Install multiple Python versions
pyenv install 3.9.18
pyenv install 3.10.13
pyenv install 3.11.7
pyenv install 3.12.1

# 2. Create separate environments for each version
pyenv virtualenv 3.9.18 test-py39
pyenv virtualenv 3.10.13 test-py310
pyenv virtualenv 3.11.7 test-py311
pyenv virtualenv 3.12.1 test-py312

# 3. Test in each environment
pyenv activate test-py39
pip install -r requirements.txt
pytest
pyenv deactivate

pyenv activate test-py310
pip install -r requirements.txt
pytest
pyenv deactivate

# And so on...
```

### Workflow 4: Managing Dependencies

```bash
# Activate your project environment
cd /path/to/project
# (auto-activates if you used pyenv local)

# Install packages
pip install django requests pandas

# Export dependencies
pip freeze > requirements.txt

# Or use pip-tools for better dependency management
pip install pip-tools

# Create requirements.in with top-level dependencies
echo "django>=4.2" > requirements.in
echo "requests" >> requirements.in

# Compile to requirements.txt with all sub-dependencies
pip-compile requirements.in

# Sync environment
pip-sync requirements.txt
```

---

## Alternative Tools

### Built-in venv Module

```bash
# Create virtual environment
python3 -m venv myenv

# Activate (macOS/Linux)
source myenv/bin/activate

# Activate (Windows)
myenv\Scripts\activate

# Deactivate
deactivate

# Remove
rm -rf myenv
```

**Pros**: Built-in, no installation needed  
**Cons**: Doesn't manage Python versions, manual activation required

### Virtualenv

```bash
# Install
pip install virtualenv

# Create environment
virtualenv myenv

# Specify Python version
virtualenv -p python3.11 myenv

# Activate/deactivate same as venv
```

**Pros**: More features than venv, faster  
**Cons**: Doesn't manage Python versions, requires separate installation

### Conda

```bash
# Create environment
conda create -n myenv python=3.11

# Activate
conda activate myenv

# Deactivate
conda deactivate

# Remove
conda env remove -n myenv
```

**Pros**: Manages Python versions and system packages, great for data science  
**Cons**: Large installation, slower, different package ecosystem

### Comparison Table

| Feature | pyenv + pyenv-virtualenv | venv | virtualenv | conda |
|---------|-------------------------|------|------------|-------|
| Manage Python versions | ✅ | ❌ | ❌ | ✅ |
| Virtual environments | ✅ | ✅ | ✅ | ✅ |
| Auto-activation | ✅ | ❌ | ❌ | ❌ |
| Built-in | ❌ | ✅ | ❌ | ❌ |
| Lightweight | ✅ | ✅ | ✅ | ❌ |
| System packages | ❌ | ❌ | ❌ | ✅ |
| Best for | General Python development | Simple projects | Legacy projects | Data science/ML |

---

## Best Practices

### 1. Project-Specific Environments

Always create a separate virtual environment for each project:

```bash
# Good
pyenv virtualenv 3.11.7 project-a-env
pyenv virtualenv 3.11.7 project-b-env

# Bad - sharing environments between projects
pyenv virtualenv 3.11.7 shared-env  # Don't do this
```

### 2. Descriptive Naming Convention

Use clear, descriptive names for your environments:

```bash
# Good examples
pyenv virtualenv 3.11.7 django-blog-dev
pyenv virtualenv 3.10.13 ml-research-env
pyenv virtualenv 3.11.7 api-production
pyenv virtualenv 3.12.1 fastapi-microservice

# Less clear
pyenv virtualenv 3.11.7 env1
pyenv virtualenv 3.11.7 test
```

### 3. Use .python-version Files

Always create a `.python-version` file in your project root:

```bash
cd /path/to/project
pyenv local myproject-env

# This creates .python-version file
# Commit this file to version control
git add .python-version
git commit -m "Add Python version specification"
```

### 4. Keep Dependencies Updated

```bash
# Regularly update pip
pip install --upgrade pip

# Check for outdated packages
pip list --outdated

# Update specific package
pip install --upgrade package-name

# Update all packages (use with caution)
pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip install -U
```

### 5. Pin Dependencies

Always pin your dependencies in `requirements.txt`:

```txt
# Good - pinned versions
django==4.2.7
requests==2.31.0
pytest==7.4.3

# Acceptable - minimum version with compatible releases
django>=4.2,<5.0
requests~=2.31.0

# Risky - unpinned
django
requests
```

### 6. Separate Development and Production Dependencies

```bash
# requirements.txt (production)
django==4.2.7
psycopg2-binary==2.9.9
gunicorn==21.2.0

# requirements-dev.txt (development)
-r requirements.txt
pytest==7.4.3
black==23.11.0
flake8==6.1.0
ipython==8.17.2
```

Install with:
```bash
# Production
pip install -r requirements.txt

# Development
pip install -r requirements-dev.txt
```

### 7. Add Virtual Environments to .gitignore

Never commit virtual environment directories:

```gitignore
# .gitignore
venv/
env/
.venv/
ENV/
*.pyc
__pycache__/
.pytest_cache/
.python-version  # Optional: commit this if you want to share the Python version
```

### 8. Document Setup Instructions

Include setup instructions in your `README.md`:

```markdown
## Setup

1. Install pyenv and pyenv-virtualenv
2. Install Python version: `pyenv install 3.11.7`
3. Create virtual environment: `pyenv virtualenv 3.11.7 myproject-env`
4. Activate environment: `pyenv local myproject-env`
5. Install dependencies: `pip install -r requirements.txt`
```

---

## Troubleshooting

### Python Version Not Switching

**Problem**: Python version doesn't change when using `pyenv local` or `pyenv global`

**Solutions**:
```bash
# Check current version and source
pyenv version

# Check for shell override
pyenv shell
# If set, unset it
pyenv shell --unset

# Rebuild shim binaries
pyenv rehash

# Verify pyenv is in PATH
echo $PATH | grep pyenv

# Re-initialize pyenv
eval "$(pyenv init -)"
```

### Build Failures During Python Installation

**Problem**: `pyenv install` fails with compilation errors

**Solutions**:

**macOS**:
```bash
# Install build dependencies
brew install openssl readline sqlite3 xz zlib tcl-tk

# Install with specific flags
CFLAGS="-I$(brew --prefix openssl)/include" \
LDFLAGS="-L$(brew --prefix openssl)/lib" \
pyenv install 3.11.7
```

**Ubuntu/Debian**:
```bash
sudo apt-get update
sudo apt-get install -y build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

pyenv install 3.11.7
```

### Virtual Environment Not Auto-Activating

**Problem**: Environment doesn't activate when entering directory

**Solutions**:
```bash
# Ensure virtualenv-init is in shell config
grep "pyenv virtualenv-init" ~/.zshrc

# If not present, add it
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc
source ~/.zshrc

# Verify .python-version file exists
cat .python-version

# Recreate local setting
pyenv local myproject-env
```

### Command Not Found After Installing Package

**Problem**: Installed package command not found

**Solutions**:
```bash
# Rebuild shims
pyenv rehash

# Verify package is installed
pip list | grep package-name

# Check which command
pyenv which command-name

# Ensure you're in correct environment
pyenv version
```

### Permission Denied Errors

**Problem**: Permission errors when installing packages

**Solutions**:
```bash
# Never use sudo with pip in virtual environments
# Bad: sudo pip install package
# Good: pip install package

# If you get permission errors, check you're in virtualenv
pyenv version

# Recreate environment if needed
pyenv virtualenv-delete myenv
pyenv virtualenv 3.11.7 myenv
pyenv local myenv
```

### Slow pyenv Performance

**Problem**: Shell startup is slow due to pyenv

**Solutions**:
```bash
# Use lazy loading in ~/.zshrc
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"

# Lazy load pyenv
if command -v pyenv 1>/dev/null 2>&1; then
  eval "$(pyenv init --path)"
  eval "$(pyenv init -)"
  eval "$(pyenv virtualenv-init -)"
fi
```

---

## Quick Reference

### Essential Commands

| Task | Command |
|------|---------|
| **Installation** | |
| Install pyenv (macOS) | `brew install pyenv` |
| Install pyenv (Linux) | `curl https://pyenv.run \| bash` |
| Install pyenv-virtualenv | `brew install pyenv-virtualenv` |
| **Python Versions** | |
| List available versions | `pyenv install --list` |
| Install Python version | `pyenv install 3.11.7` |
| List installed versions | `pyenv versions` |
| Show current version | `pyenv version` |
| Uninstall version | `pyenv uninstall 3.11.7` |
| **Version Switching** | |
| Set global version | `pyenv global 3.11.7` |
| Set local version | `pyenv local 3.11.7` |
| Set shell version | `pyenv shell 3.11.7` |
| Unset local | `pyenv local --unset` |
| Unset shell | `pyenv shell --unset` |
| **Virtual Environments** | |
| Create virtualenv | `pyenv virtualenv 3.11.7 myenv` |
| Activate virtualenv | `pyenv activate myenv` |
| Deactivate | `pyenv deactivate` |
| Auto-activate in directory | `pyenv local myenv` |
| List virtualenvs | `pyenv virtualenvs` |
| Delete virtualenv | `pyenv virtualenv-delete myenv` |
| **Package Management** | |
| Install package | `pip install package-name` |
| Install from requirements | `pip install -r requirements.txt` |
| List packages | `pip list` |
| Export dependencies | `pip freeze > requirements.txt` |
| Update pip | `pip install --upgrade pip` |
| Uninstall package | `pip uninstall package-name` |
| **Utilities** | |
| Rebuild shims | `pyenv rehash` |
| Show command path | `pyenv which python` |
| Show pyenv root | `echo $PYENV_ROOT` |
| Update pyenv (macOS) | `brew upgrade pyenv` |
| Update pyenv (Linux) | `cd $(pyenv root) && git pull` |

### Common File Locations

| File/Directory | Purpose |
|----------------|---------|
| `~/.pyenv/` | Pyenv root directory |
| `~/.pyenv/versions/` | Installed Python versions |
| `~/.pyenv/version` | Global Python version |
| `.python-version` | Local Python version (project-specific) |
| `$PYENV_VERSION` | Shell Python version (environment variable) |

### Environment Variables

```bash
# Show pyenv root
echo $PYENV_ROOT

# Show current version
echo $PYENV_VERSION

# Show virtualenv name
echo $PYENV_VIRTUAL_ENV
```

---

## Additional Resources

### Official Documentation
- [Pyenv GitHub](https://github.com/pyenv/pyenv)
- [Pyenv-virtualenv GitHub](https://github.com/pyenv/pyenv-virtualenv)
- [Python venv Documentation](https://docs.python.org/3/library/venv.html)

### Useful Tools
- **pip-tools**: Better dependency management
- **poetry**: Modern Python packaging and dependency management
- **pipenv**: Combines pip and virtualenv
- **tox**: Testing across multiple Python versions

### Tips for Specific Use Cases

**Data Science**:
```bash
# Consider using conda for data science projects
# But if using pyenv:
pyenv install 3.11.7
pyenv virtualenv 3.11.7 data-science-env
pyenv activate data-science-env
pip install jupyter pandas numpy scipy scikit-learn matplotlib
```

**Web Development**:
```bash
pyenv install 3.11.7
pyenv virtualenv 3.11.7 django-project
pyenv local django-project
pip install django djangorestframework celery redis
```

**Testing/CI**:
```bash
# Install multiple versions for testing
pyenv install 3.9.18 3.10.13 3.11.7 3.12.1

# Use tox for automated testing
pip install tox
```

---

## Summary

**Pyenv** is the recommended tool for Python version and virtual environment management because it:
- ✅ Manages multiple Python versions effortlessly
- ✅ Provides automatic environment activation
- ✅ Keeps projects isolated and reproducible
- ✅ Works seamlessly with standard Python tools
- ✅ Lightweight and fast
- ✅ Integrates well with development workflows

**Quick Start Reminder**:
```bash
# 1. Install pyenv and pyenv-virtualenv
brew install pyenv pyenv-virtualenv

# 2. Configure shell
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc
source ~/.zshrc

# 3. Install Python and create environment
pyenv install 3.11.7
pyenv virtualenv 3.11.7 myproject-env

# 4. Use in project
cd myproject
pyenv local myproject-env
pip install -r requirements.txt
```

Happy coding! 🐍
