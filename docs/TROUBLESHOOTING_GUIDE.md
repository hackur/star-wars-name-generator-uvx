# UV Tools: Comprehensive Troubleshooting and Debugging Guide

A complete guide to debugging UV tools based on real-world issues, research, and best practices for 2025.

---

## Table of Contents

1. [Common Development Pitfalls](#common-development-pitfalls)
2. [Debugging Techniques for UV Tools](#debugging-techniques-for-uv-tools)
3. [PATH Issues and Resolution](#path-issues-and-resolution)
4. [Dependency Conflicts and Resolution](#dependency-conflicts-and-resolution)
5. [Version Pinning Strategies](#version-pinning-strategies)
6. [Testing in Different Environments](#testing-in-different-environments)
7. [Cross-Platform Compatibility Issues](#cross-platform-compatibility-issues)
8. [Build Failures](#build-failures)
9. [Lockfile Issues](#lockfile-issues)
10. [Performance Debugging](#performance-debugging)
11. [CI/CD Troubleshooting](#cicd-troubleshooting)

---

## Common Development Pitfalls

### 1. Confusion Between `uv pip` and `uv add`

**Problem:** Developers mix legacy pip workflows with modern UV project management.

**Explanation:**
- `uv pip` is a compatibility layer for users transitioning from pip
- `uv add` is the project-centric approach that manages `pyproject.toml` and `uv.lock`

**Anti-Pattern:**
```bash
# Don't mix workflows
uv pip install requests
uv add click
# This creates inconsistent dependency management
```

**Best Practice:**
```bash
# Choose one workflow and stick with it

# Project-centric (recommended):
uv add requests click
uv sync

# Pip-compatible (for migration):
uv pip install requests click
```

**When to use each:**
- Use `uv add` for new projects
- Use `uv pip` only when migrating from pip or for quick scripts
- Never mix both in the same project

### 2. Not Using `uv run` in Development

**Problem:** Running Python scripts directly instead of through UV.

**Symptoms:**
```bash
$ python -m my_package
ModuleNotFoundError: No module named 'my_package'

$ pytest tests/
# Uses wrong Python/environment
```

**Root Cause:**
- Python isn't running in the project's virtual environment
- Dependencies aren't available
- Wrong Python version being used

**Solution:**
```bash
# Always use uv run in development
uv run python -m my_package
uv run pytest tests/
uv run mypy src/

# Or activate the environment
uv sync
source .venv/bin/activate
python -m my_package
```

### 3. Manually Mutating Tool Environments

**Problem:** Using pip directly on UV-managed tool environments.

**Why it's bad:**
```bash
# Install a tool
uv tool install black

# Don't do this!
~/.local/share/uv/tools/black/bin/pip install some-plugin
```

**What happens:**
- UV doesn't track these changes
- Updates may break
- No reproducibility
- Can cause dependency conflicts

**Correct approach:**
```bash
# If you need plugins/extras:
uv tool install "black[plugin]"

# Or create a project with it as a dependency:
uv init my-formatter
uv add black some-plugin
uv run black .
```

### 4. Ignoring `uv.lock` in Version Control

**Problem:** Adding `uv.lock` to `.gitignore`.

**Why it's wrong:**
```gitignore
# DON'T DO THIS
uv.lock
```

**Impact:**
- No reproducible builds
- Team members get different versions
- CI/CD may fail randomly
- "Works on my machine" syndrome

**Correct practice:**
```gitignore
# .gitignore
.venv/
__pycache__/
dist/
*.pyc
.pytest_cache/
# uv.lock should NOT be here!
```

**Commit the lock file:**
```bash
git add uv.lock pyproject.toml
git commit -m "feat: add dependencies with lock file"
```

### 5. Wrong Working Directory

**Problem:** Running UV commands from incorrect location.

**Symptoms:**
```bash
$ uv sync
error: No project found in current directory or parents
```

**Debugging:**
```bash
# Check current directory
pwd

# Find pyproject.toml
find . -name pyproject.toml -maxdepth 3

# Move to project root
cd /path/to/project

# Verify
ls pyproject.toml
```

**Alternative - specify directory:**
```bash
uv sync --directory /path/to/project
# or
UV_PROJECT=/path/to/project uv sync
```

### 6. Installing UV with pip

**Problem:** Installing UV using pip creates a dependency loop.

**Why it's problematic:**
```bash
# DON'T DO THIS
pip install uv
```

**Issues:**
- UV becomes dependent on that specific Python version
- Updates are complicated
- May break when Python version changes
- Not the intended installation method

**Correct installation:**
```bash
# macOS/Linux - standalone installer
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Homebrew (macOS)
brew install uv

# Verify it's standalone
which uv  # Should be in ~/.cargo/bin or /usr/local/bin
uv --version
```

---

## Debugging Techniques for UV Tools

### 1. Verbose Output

**Basic debugging:**
```bash
# Increase verbosity
uv -v sync
uv -vv add requests  # Very verbose
uv -vvv build        # Maximum verbosity

# See what UV is doing
uv --verbose tool install black
```

**What you'll see:**
- Dependency resolution steps
- Network requests
- File operations
- Cache hits/misses
- Environment variables being used

### 2. Environment Inspection

**Check UV configuration:**
```bash
# Show all environment variables UV respects
env | grep UV_

# Key variables to check
echo $UV_CACHE_DIR
echo $UV_TOOL_DIR
echo $UV_PYTHON_INSTALL_DIR
echo $UV_CONFIG_FILE
```

**Inspect tool directories:**
```bash
# Where are tools installed?
uv tool dir

# List installed tools
uv tool list

# Check tool environment
ls -la ~/.local/share/uv/tools/
ls -la ~/.local/share/uv/tools/my-tool/
```

### 3. Cache Debugging

**Understanding the cache:**
```bash
# Show cache directory
uv cache dir

# See what's cached
ls -lh "$(uv cache dir)/"

# Cache size
du -sh "$(uv cache dir)"

# Clean specific package
uv cache clean package-name

# Clean all cache (nuclear option)
uv cache clean

# Prune old entries
uv cache prune
```

**When to clean cache:**
- After package updates not being recognized
- Disk space issues
- Corrupted downloads
- Testing fresh installs

### 4. Python Version Debugging

**Check Python discovery:**
```bash
# List all Python versions UV can find
uv python list

# Show which Python will be used
uv run python --version

# Check project's Python
cat .python-version

# Check requirements
grep requires-python pyproject.toml

# Force specific Python
uv run --python 3.12 python --version
uv sync --python 3.11
```

**Python discovery order:**
1. Virtual environment (if VIRTUAL_ENV set)
2. `.venv` in current or parent directories
3. `.python-version` file
4. `requires-python` in pyproject.toml
5. System PATH
6. UV-managed Python installations

### 5. Dependency Tree Analysis

**Understand dependency relationships:**
```bash
# Show dependency tree
uv tree

# Show dependencies for specific package
uv tree package-name

# Check for conflicts
uv sync --dry-run

# Explain why a package is installed
uv tree --invert package-name

# Check for outdated packages
uv lock --upgrade --dry-run
```

### 6. Lock File Inspection

**Debug lock file issues:**
```bash
# Verify lock file is in sync
uv lock --check

# See what would change
uv lock --upgrade --dry-run

# Force regenerate lock file
rm uv.lock
uv lock

# Check specific package version in lock
grep "name = \"package-name\"" uv.lock -A 5
```

### 7. Build Isolation Debugging

**When builds fail:**
```bash
# Show build output
uv pip install package-name --verbose

# Disable build isolation (advanced)
uv pip install --no-build-isolation package-name

# Check build dependencies
uv pip install --dry-run package-name
```

### 8. Network Debugging

**Diagnose download issues:**
```bash
# Check if PyPI is reachable
curl -I https://pypi.org/

# Use different index
uv add --index-url https://pypi.org/simple/ package-name

# Check for proxy issues
echo $HTTP_PROXY
echo $HTTPS_PROXY

# Disable proxy temporarily
unset HTTP_PROXY HTTPS_PROXY
uv sync
```

---

## PATH Issues and Resolution

### Understanding the Problem

**How UV tools work:**
1. `uv tool install` places executables in the bin directory
2. The bin directory must be in your PATH
3. Shell needs to find executables by name

**Common locations:**
- Linux: `~/.local/bin`
- macOS: `~/.local/bin` or `~/.cargo/bin`
- Windows: `%USERPROFILE%\.local\bin`

### Diagnostic Commands

```bash
# 1. Check if tool is installed
uv tool list | grep my-tool

# 2. Check where executable is
which my-tool
# or
command -v my-tool

# 3. Check your PATH
echo $PATH

# 4. Check if bin directory exists
ls -la ~/.local/bin/

# 5. Check if executable has permissions
ls -l ~/.local/bin/my-tool

# 6. Test PATH entry manually
~/.local/bin/my-tool --help
```

### Fix PATH Issues

**Automatic fix (recommended):**
```bash
uv tool update-shell
```

This adds UV's bin directory to your shell configuration.

**Manual fix:**

```bash
# For bash (~/.bashrc or ~/.bash_profile)
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# For zsh (~/.zshrc)
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# For fish (~/.config/fish/config.fish)
echo 'set -gx PATH $HOME/.local/bin $PATH' >> ~/.config/fish/config.fish
source ~/.config/fish/config.fish

# For Windows (PowerShell)
$env:PATH = "$env:USERPROFILE\.local\bin;$env:PATH"
# Make permanent:
[Environment]::SetEnvironmentVariable("PATH", "$env:USERPROFILE\.local\bin;$env:PATH", "User")
```

**Verify fix:**
```bash
# Reload shell
exec $SHELL

# Check PATH
echo $PATH | grep -o "[^:]*\.local/bin[^:]*"

# Test command
which my-tool
my-tool --version
```

### Advanced PATH Issues

**Issue 1: Multiple installations**
```bash
# Find all installations
which -a my-tool

# Shows multiple locations:
# /usr/local/bin/my-tool
# ~/.local/bin/my-tool
# ~/venv/bin/my-tool

# Solution: Control PATH order
export PATH="$HOME/.local/bin:/usr/local/bin:$PATH"
```

**Issue 2: Shell-specific configuration**
```bash
# Check which shell you're using
echo $SHELL

# Common mistake: editing wrong config file
# - Login shell vs interactive shell
# - ~/.bashrc vs ~/.bash_profile
# - System-wide vs user-specific

# Debug: Which config is loaded?
echo $BASH_SOURCE
# or for zsh:
echo $ZDOTDIR
```

**Issue 3: Permission problems**
```bash
# Check permissions
ls -l ~/.local/bin/my-tool

# Fix if needed
chmod +x ~/.local/bin/my-tool

# Check directory permissions
ls -ld ~/.local/bin/
# Should be: drwxr-xr-x (755 or 700)
```

### Environment Variables for PATH Control

```bash
# Override bin directory
export UV_TOOL_BIN_DIR="$HOME/bin"
uv tool install my-tool

# Override tool directory
export UV_TOOL_DIR="$HOME/.tools"
uv tool install my-tool

# Use XDG standard directories
export XDG_BIN_HOME="$HOME/.local/bin"
export XDG_CONFIG_HOME="$HOME/.config"
```

---

## Dependency Conflicts and Resolution

### Understanding Resolution

**How UV resolves dependencies:**
1. Parses all requirements
2. Finds compatible versions recursively
3. Uses PubGrub algorithm (same as Poetry)
4. Creates universal resolution (cross-platform)
5. Locks exact versions with hashes

### Common Conflict Scenarios

**Scenario 1: Version range conflicts**
```toml
# Package A requires: requests>=2.30,<3.0
# Package B requires: requests>=2.25,<2.28

# Conflict: No version satisfies both!
```

**Resolution strategies:**
```bash
# 1. Try updating packages
uv lock --upgrade

# 2. Check for newer versions
uv add package-a@latest package-b@latest

# 3. Use overrides (force specific version)
# In pyproject.toml:
[tool.uv]
override-dependencies = [
    "requests==2.31.0"  # Force this version
]

# 4. Exclude problematic package
uv remove package-b
# Find alternative
```

**Scenario 2: Python version conflicts**
```toml
# Your project: requires-python = ">=3.12"
# Dependency: requires Python <3.11

# Incompatible!
```

**Resolution:**
```bash
# Option 1: Widen your Python range
requires-python = ">=3.10"

# Option 2: Find alternative package
uv add alternative-package

# Option 3: Use older package version
uv add "problematic-package<2.0"
```

### Dependency Overrides

**When to use overrides:**
- Force specific version across all dependencies
- Work around incorrect package metadata
- Resolve security issues

**Example:**
```toml
[tool.uv]
override-dependencies = [
    "urllib3==1.26.18",  # Security fix
    "certifi>=2023.7.22", # Certificate update
]
```

**Difference from constraints:**
```toml
# Constraints: Additive (combines with other requirements)
[tool.uv]
constraint-dependencies = [
    "numpy<2.0",  # Adds to existing requirements
]

# Overrides: Absolute (replaces all requirements)
[tool.uv]
override-dependencies = [
    "numpy==1.24.0",  # Forces this exact version
]
```

### Conflicting Optional Dependencies

**Problem:**
```toml
[project.optional-dependencies]
cuda = ["torch==2.0.0+cu118"]
rocm = ["torch==2.0.0+rocm5.4"]
# These conflict with each other!
```

**Solution:**
```toml
[tool.uv]
conflicts = [
    [
        {extra = "cuda"},
        {extra = "rocm"}
    ]
]
```

Now UV resolves them separately:
```bash
# Can install one at a time
uv sync --extra cuda
# or
uv sync --extra rocm

# But not together (will error)
uv sync --extra cuda --extra rocm  # ❌
```

### Resolution Strategies

**Lowest version testing:**
```bash
# Test with minimum versions
uv sync --resolution lowest

# Test with lowest direct dependencies only
uv sync --resolution lowest-direct
```

**Why this matters:**
- Ensures your lower bounds are correct
- Prevents users from getting incompatible old versions
- Important for library maintainers

**Platform-specific resolution:**
```bash
# Resolve for specific platform
uv lock --python-platform linux
uv lock --python-platform darwin
uv lock --python-platform windows

# Resolve for specific Python version
uv lock --python-version 3.11
```

### Debugging Resolution Failures

**Step 1: Increase verbosity**
```bash
uv add problem-package -vv
```

**Step 2: Check dependency tree**
```bash
# Why was this package selected?
uv tree problem-package

# What depends on it?
uv tree --invert problem-package
```

**Step 3: Try different versions**
```bash
# Try older version
uv add "problem-package<2.0"

# Try specific version
uv add problem-package==1.5.0

# Try pre-release
uv add problem-package --prerelease allow
```

**Step 4: Check for updates**
```bash
# See if newer versions are available
uv lock --upgrade --dry-run
```

**Step 5: Use constraints**
```bash
# Constrain problematic dependencies
echo "problematic-dep<2.0" > constraints.txt
uv add package-name --constraint constraints.txt
```

---

## Version Pinning Strategies

### Philosophy: Ranges vs Pins

**Use version ranges (recommended):**
```toml
dependencies = [
    "click>=8.0,<9.0",      # Major version range
    "requests>=2.28,<3.0",  # Minor version flexibility
]
```

**Benefits:**
- Allows security updates
- More compatible with other packages
- Easier to maintain

**Use exact pins (sparingly):**
```toml
dependencies = [
    "critical-package==1.2.3",  # Exact version
]
```

**When to pin exactly:**
- Known breaking changes in newer versions
- Security-critical packages with CVEs in other versions
- Temporary workaround for bugs

### Lock File vs Version Ranges

**Understand the difference:**

```toml
# pyproject.toml (version ranges)
dependencies = ["requests>=2.28,<3.0"]
```

```toml
# uv.lock (exact versions)
[[package]]
name = "requests"
version = "2.31.0"
source = { registry = "https://pypi.org/simple" }
```

**Why both?**
- `pyproject.toml`: Specifies what's compatible
- `uv.lock`: Locks what's actually used
- Consumers get exact versions (reproducible)
- Library authors can update within range

### Pinning Strategies by Project Type

**CLI Tools (like starwars-namegen):**
```toml
dependencies = [
    "click>=8.0,<9.0",
    "inflect>=7.0,<8.0",
]
```
- Use ranges for flexibility
- Lock file ensures reproducibility
- Users always get tested combination

**Libraries:**
```toml
dependencies = [
    "requests>=2.25",  # Wide compatibility
]
```
- Minimal lower bounds
- No upper bounds (unless known incompatibility)
- Let users control versions

**Applications:**
```toml
dependencies = [
    "fastapi>=0.104.0,<0.105.0",  # Tighter ranges
    "sqlalchemy>=2.0,<2.1",
]
```
- More specific ranges
- Control environment closely
- Balance updates vs stability

### Testing Version Compatibility

**Test lower bounds:**
```bash
# Install minimum versions
uv sync --resolution lowest

# Run tests
uv run pytest

# Update lower bounds if tests fail
uv add "package>=newer-version"
```

**Test upper bounds:**
```bash
# Try upgrading all packages
uv lock --upgrade

# Run tests
uv sync
uv run pytest

# Add upper bound if broken
uv add "package>=2.0,<3.0"
```

### Update Strategies

**Conservative updates:**
```bash
# Update specific package
uv lock --upgrade-package requests

# Update within existing ranges
uv lock --upgrade
```

**Aggressive updates:**
```bash
# Update to latest, ignoring current ranges
uv add requests@latest

# Update all packages
for pkg in $(uv tree --depth 0 | cut -d' ' -f1); do
    uv add "$pkg@latest"
done
```

**Controlled updates:**
```bash
# Create update branch
git checkout -b update-dependencies

# Update lock file
uv lock --upgrade

# Review changes
git diff uv.lock

# Test thoroughly
uv run pytest
uv run mypy src/

# Only merge if all tests pass
```

### Version Pinning Best Practices

**1. Use semantic versioning understanding:**
```toml
# Compatible changes (patches, minor)
"package>=1.2,<2.0"

# Only patch updates
"package>=1.2.0,<1.3.0"

# Exact version (rarely needed)
"package==1.2.3"
```

**2. Document why you pin:**
```toml
dependencies = [
    # Pin due to breaking change in 3.0
    "requests>=2.28,<3.0",

    # Pin due to CVE-2023-12345 in older versions
    "urllib3>=2.0.7",
]
```

**3. Regular update schedule:**
```bash
# Monthly: Check for updates
uv lock --upgrade --dry-run

# Review changes
git diff uv.lock

# Update and test
uv lock --upgrade
uv run pytest
```

**4. Security updates:**
```bash
# Check for security issues
pip-audit  # or similar tool

# Update specific CVE-affected package
uv lock --upgrade-package vulnerable-package
```

---

## Testing in Different Environments

### Multi-Python Version Testing

**Using UV's Python management:**
```bash
# Install multiple Python versions
uv python install 3.9 3.10 3.11 3.12

# Test on each version
for version in 3.9 3.10 3.11 3.12; do
    echo "Testing Python $version"
    uv run --python $version pytest tests/
done
```

**Using tox with UV:**
```toml
# pyproject.toml
[tool.tox]
env_list = ["py39", "py310", "py311", "py312"]

[tool.tox.env_run_base]
runner = "uv-venv-lock-runner"
```

```bash
# Install tox with UV
uv tool install tox

# Run tests across Python versions
tox
```

### Docker Testing

**Multi-stage Dockerfile:**
```dockerfile
# Dockerfile.test
FROM python:3.12-slim as base
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.cargo/bin:$PATH"

# Test stage
FROM base as test
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev
COPY . .
RUN uv run pytest tests/

# Run stage
FROM base as run
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev
COPY src/ ./src/
CMD ["uv", "run", "starwars-namegen"]
```

**Test on multiple platforms:**
```bash
# Build for different platforms
docker buildx build --platform linux/amd64,linux/arm64 \
    -t my-app:test \
    --target test \
    .
```

### CI/CD Matrix Testing

**GitHub Actions example:**
```yaml
name: Test

on: [push, pull_request]

jobs:
  test:
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
        python-version: ["3.9", "3.10", "3.11", "3.12"]

    runs-on: ${{ matrix.os }}

    steps:
      - uses: actions/checkout@v4

      - uses: astral-sh/setup-uv@v1
        with:
          enable-cache: true
          cache-dependency-glob: "uv.lock"

      - name: Install Python
        run: uv python install ${{ matrix.python-version }}

      - name: Install dependencies
        run: uv sync --frozen

      - name: Run tests
        run: uv run pytest tests/

      - name: Run type checks
        run: uv run mypy src/
```

**GitLab CI example:**
```yaml
# .gitlab-ci.yml
.test-template:
  before_script:
    - curl -LsSf https://astral.sh/uv/install.sh | sh
    - export PATH="$HOME/.cargo/bin:$PATH"
    - uv sync --frozen

  script:
    - uv run pytest tests/

  cache:
    paths:
      - .cache/uv/

test-python-3.9:
  extends: .test-template
  image: python:3.9-slim

test-python-3.10:
  extends: .test-template
  image: python:3.10-slim

test-python-3.11:
  extends: .test-template
  image: python:3.11-slim

test-python-3.12:
  extends: .test-template
  image: python:3.12-slim
```

### Local Testing Best Practices

**Test in fresh environment:**
```bash
# Remove existing environment
rm -rf .venv

# Create fresh environment
uv sync

# Run tests
uv run pytest
```

**Test with minimal dependencies:**
```bash
# Without dev dependencies
uv sync --no-dev

# Ensure main functionality works
uv run starwars-namegen --help
```

**Test installation:**
```bash
# Build package
uv build

# Install in isolated environment
uv venv test-env
source test-env/bin/activate
uv pip install dist/*.whl

# Test installation
starwars-namegen --help

# Cleanup
deactivate
rm -rf test-env
```

### Environment Variables Testing

**Test with different configurations:**
```bash
# Test with no cache
UV_NO_CACHE=1 uv sync

# Test with different tool directory
UV_TOOL_DIR=/tmp/test-tools uv tool install starwars-namegen

# Test with offline mode
UV_OFFLINE=1 uv sync  # Should use cache only

# Test with different Python
UV_PYTHON=3.11 uv run pytest
```

---

## Cross-Platform Compatibility Issues

### Platform Detection and Resolution

**How UV handles platforms:**
```bash
# Universal resolution (default for projects)
uv lock  # Creates cross-platform lock file

# Platform-specific resolution
uv lock --python-platform linux
uv lock --python-platform darwin
uv lock --python-platform windows
```

**Check what platforms are supported:**
```bash
# Inspect lock file for platform markers
grep "marker" uv.lock

# Example markers:
# sys_platform == "win32"
# sys_platform == "linux"
# sys_platform == "darwin"
```

### Common Cross-Platform Issues

**Issue 1: Line endings**
```bash
# Problem: Git converts line endings
# Windows (CRLF) ↔ Linux/Mac (LF)

# Solution: Configure Git
git config --global core.autocrlf input  # Mac/Linux
git config --global core.autocrlf true   # Windows

# Or use .gitattributes
echo "* text=auto" > .gitattributes
echo "*.py text eol=lf" >> .gitattributes
```

**Issue 2: Path separators**
```python
# ❌ Wrong: Hardcoded separator
path = "src/starwars_namegen/cli.py"

# ✅ Correct: Use pathlib
from pathlib import Path
path = Path("src") / "starwars_namegen" / "cli.py"

# ✅ Or os.path
import os
path = os.path.join("src", "starwars_namegen", "cli.py")
```

**Issue 3: File linking methods**
```bash
# UV defaults differ by platform:
# - macOS: clone (Copy-on-Write)
# - Linux: hardlink
# - Windows: hardlink

# Override if needed
UV_LINK_MODE=copy uv sync      # Slower but more compatible
UV_LINK_MODE=hardlink uv sync  # Faster but requires same filesystem
UV_LINK_MODE=symlink uv sync   # Fast but may not work on Windows
```

**Issue 4: Executable permissions**
```bash
# Linux/Mac: Need execute bit
chmod +x script.sh

# Windows: No execute bit
# But UV handles this automatically for entry points

# In pyproject.toml:
[project.scripts]
my-tool = "my_package.cli:main"
# UV creates .exe on Windows, shell script on Unix
```

### Platform-Specific Dependencies

**Scenario:** Different dependencies per platform

```toml
# pyproject.toml
dependencies = [
    "click>=8.0",
    # Unix-only
    "python-daemon>=3.0 ; sys_platform != 'win32'",
    # Windows-only
    "pywin32>=305 ; sys_platform == 'win32'",
    # macOS-only
    "pyobjc-framework-Cocoa>=9.0 ; sys_platform == 'darwin'",
]
```

**Environment markers:**
```toml
dependencies = [
    # Python version specific
    "importlib-metadata>=6.0 ; python_version < '3.10'",
    "typing-extensions>=4.0 ; python_version < '3.11'",

    # Platform specific
    "colorama>=0.4 ; platform_system == 'Windows'",
]
```

### Virtual Environment Activation

**Problem:** Different activation commands per platform/shell

```bash
# Bash/Zsh (Linux/Mac)
source .venv/bin/activate

# Fish shell
source .venv/bin/activate.fish

# Windows CMD
.venv\Scripts\activate.bat

# Windows PowerShell
.venv\Scripts\Activate.ps1

# Windows Git Bash
source .venv/Scripts/activate
```

**UV solution: Just use `uv run`**
```bash
# Works everywhere!
uv run pytest
uv run python script.py
uv run my-tool
```

### Testing Cross-Platform Compatibility

**Use CI/CD matrix:**
```yaml
# GitHub Actions
strategy:
  matrix:
    os: [ubuntu-latest, macos-latest, windows-latest]

runs-on: ${{ matrix.os }}
```

**Local testing with Docker:**
```bash
# Test Linux
docker run -it --rm -v $(pwd):/app python:3.12-slim bash
cd /app && curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.cargo/bin:$PATH"
uv sync && uv run pytest

# Test Windows (if on Windows/WSL)
# Use Windows containers
```

**Local testing with VMs:**
- Use VirtualBox, VMware, or Parallels
- Test on actual target OS
- Especially important for binary dependencies

### Windows-Specific Issues

**Issue 1: Long path support**
```bash
# Enable long paths on Windows
# Run as Administrator:
Set-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem' -Name 'LongPathsEnabled' -Value 1

# Or use shorter project paths
C:\p\my-project  # Instead of C:\Users\Username\Documents\Projects\my-project
```

**Issue 2: PowerShell execution policy**
```powershell
# Check policy
Get-ExecutionPolicy

# Allow scripts
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Issue 3: Windows Defender**
```bash
# UV may be slow due to real-time scanning
# Add exclusions for:
# - UV cache directory
# - Project .venv directory
# - Python installations

# Check with:
UV_CACHE_DIR=$(uv cache dir)
echo $UV_CACHE_DIR
```

### macOS-Specific Issues

**Issue 1: Rosetta on Apple Silicon**
```bash
# Check architecture
uname -m  # arm64 or x86_64

# Some packages may not have ARM wheels
# UV will build from source (requires Xcode tools)
xcode-select --install

# Or use x86_64 Python
arch -x86_64 uv python install 3.12
```

**Issue 2: System Integrity Protection (SIP)**
```bash
# Can't install to system directories
# Always use user directories
# UV handles this automatically
```

### Linux Distribution Differences

**Issue 1: System dependencies**
```bash
# Debian/Ubuntu
apt-get install build-essential python3-dev

# Fedora/CentOS/RHEL
dnf install gcc python3-devel

# Alpine (Docker)
apk add build-base python3-dev
```

**Issue 2: SSL/TLS certificates**
```bash
# Debian/Ubuntu
apt-get install ca-certificates

# Fedora/CentOS
dnf install ca-certificates

# Alpine
apk add ca-certificates
```

---

## Build Failures

### Recognizing Build Failures

**What it looks like:**
```
error: The build backend returned an error
--- stderr
gcc: error: Python.h: No such file or directory
```

**When builds happen:**
- No compatible wheel for your platform
- Building from source distribution
- Package has C extensions

### Confirming UV-Specific Issues

**Test with pip:**
```bash
# Create test environment
python -m venv test-venv
source test-venv/bin/activate

# Try with pip
pip install --use-pep517 --no-cache --force-reinstall problematic-package

# If it fails with pip too, it's not UV's fault
```

### Common Build Failures

**Failure 1: Missing compiler**

**Symptom:**
```
error: command 'gcc' not found
# or
error: command 'clang' not found
```

**Solution by platform:**
```bash
# Debian/Ubuntu
sudo apt-get install build-essential

# Fedora/CentOS
sudo dnf install gcc gcc-c++

# macOS
xcode-select --install

# Alpine (Docker)
apk add gcc musl-dev

# Note: UV-managed Python often needs clang
# macOS
brew install llvm
# Linux
sudo apt-get install clang
```

**Failure 2: Missing Python headers**

**Symptom:**
```
fatal error: Python.h: No such file or directory
```

**Solution:**
```bash
# Debian/Ubuntu
sudo apt-get install python3-dev

# Fedora/CentOS
sudo dnf install python3-devel

# Alpine
apk add python3-dev

# macOS (usually included with python)
# If not: brew install python@3.12
```

**Failure 3: Missing library headers**

**Symptom:**
```
fatal error: libxml/tree.h: No such file or directory
```

**Solution: Install development packages**
```bash
# Find the package name
apt-cache search libxml | grep dev

# Install
sudo apt-get install libxml2-dev libxslt1-dev

# Common packages needed:
sudo apt-get install \
    libffi-dev \          # For cryptography
    libssl-dev \          # For OpenSSL bindings
    libjpeg-dev \         # For Pillow
    zlib1g-dev \          # For compression
    libpq-dev \           # For psycopg2
    default-libmysqlclient-dev  # For mysqlclient
```

**Failure 4: Import errors during build**

**Symptom:**
```
ModuleNotFoundError: No module named 'setuptools'
```

**Solution: Disable build isolation**
```bash
# Pre-install build dependencies
uv add --dev setuptools wheel

# Install without isolation
uv pip install --no-build-isolation problematic-package
```

**Failure 5: Old package versions**

**Problem:** Old packages use deprecated build methods

**Solution: Add constraints**
```toml
# pyproject.toml
[tool.uv]
constraint-dependencies = [
    "numpy>=1.17",  # Minimum version with working build
]
```

**Or update:**
```bash
uv add "problematic-package>=2.0"
```

### Advanced Build Configuration

**Override dependency metadata:**
```toml
# pyproject.toml
[tool.uv.dependency-metadata]
"problematic-package" = [
    { version = "1.2.3", requires = ["numpy>=1.20"] }
]
```

**Use build constraints:**
```toml
[tool.uv]
build-constraint-dependencies = [
    "setuptools<65",  # Old package needs old setuptools
]
```

### Build Failure Debugging Process

**Step 1: Increase verbosity**
```bash
uv pip install problematic-package -vvv
```

**Step 2: Check build log**
```bash
# Look for specific errors in output
# Common keywords:
# - "fatal error"
# - "ModuleNotFoundError"
# - "command not found"
# - "error:"
```

**Step 3: Search for solutions**
```bash
# Package might have system dependencies
# Check package documentation:
# - README
# - Installation instructions
# - System requirements

# Search for similar issues
# Google: "uv install [package-name] build error"
# GitHub issues: [package-name] repository
```

**Step 4: Try alternative**
```bash
# Use pre-built wheel
uv pip install --only-binary :all: problematic-package

# Or find alternative package
uv add alternative-package
```

---

## Lockfile Issues

### Understanding uv.lock

**What's in the lock file:**
- Exact package versions
- Package hashes for verification
- Platform markers
- Dependency relationships
- Source URLs

**Why it matters:**
- Reproducible builds
- Security verification
- Cross-platform compatibility

### Common Lockfile Problems

**Problem 1: Lock file out of sync**

**Symptom:**
```bash
$ uv sync --frozen
error: The lockfile is out of sync with pyproject.toml
```

**Cause:**
- Modified `pyproject.toml` without updating lock
- Git merge conflict
- Manual edit to lock file

**Solution:**
```bash
# Update lock file
uv lock

# Verify sync
uv sync --frozen

# Commit both
git add pyproject.toml uv.lock
git commit -m "chore: update dependencies"
```

**Problem 2: Lock file needs updating but `uv lock` does nothing**

**Symptom:**
```bash
$ uv lock
# No output, no changes

$ uv sync --locked
error: Lock file is out of date
```

**Cause:** Cache issue

**Solution:**
```bash
# Clear cache
uv cache clean

# Force regenerate lock
rm uv.lock
uv lock

# Or use --upgrade
uv lock --upgrade
```

**Problem 3: Corrupted lock file**

**Symptom:**
```bash
$ uv sync
error: Failed to parse lockfile
```

**Solution:**
```bash
# Validate lock file
cat uv.lock | head -20  # Check if it's valid TOML

# If corrupted, regenerate
rm uv.lock
uv lock

# Restore from git if needed
git checkout HEAD -- uv.lock
uv lock --upgrade
```

**Problem 4: Git conflicts in lock file**

**Symptom:**
```
<<<<<<< HEAD
name = "package"
version = "1.0.0"
=======
name = "package"
version = "1.1.0"
>>>>>>> branch
```

**Solution:**
```bash
# Don't manually resolve lock file conflicts!
# Regenerate instead:

# Take one side (e.g., main branch)
git checkout main -- uv.lock

# Update lock file
uv lock

# Or regenerate from scratch
rm uv.lock
uv lock

# Complete merge
git add uv.lock
git commit
```

**Problem 5: SSH dependencies in lock file**

**Issue:** Lock file obfuscates SSH usernames
```toml
# In uv.lock
source = { git = "ssh://****@github.com/user/repo" }
```

**Symptom:**
```bash
$ uv sync --locked
error: Lock file must be updated
```

**Workaround:**
```bash
# Use HTTPS instead
uv add "package @ git+https://github.com/user/repo"

# Or use token authentication
uv add "package @ git+https://TOKEN@github.com/user/repo"
```

### Lockfile Best Practices

**1. Always commit lock files**
```bash
git add uv.lock
git commit -m "chore: update dependencies"
```

**2. Update lock file after any dependency change**
```bash
uv add new-package
# uv automatically updates uv.lock

uv remove old-package
# uv automatically updates uv.lock

# Manual pyproject.toml edit:
uv lock  # Update lock file
```

**3. Use --frozen in CI/CD**
```bash
# CI should never modify lock file
uv sync --frozen

# This ensures:
# - Exact versions from lock file
# - Fast installation (no resolution)
# - Fails if lock is out of date
```

**4. Verify lock file integrity**
```bash
# Check lock file is in sync
uv lock --check

# Use in CI:
jobs:
  verify:
    - run: uv lock --check
```

**5. Update regularly**
```bash
# Weekly: Update and test
uv lock --upgrade
uv run pytest

# Review changes
git diff uv.lock

# Commit if tests pass
git add uv.lock
git commit -m "chore: update dependencies"
```

### Lock File Debugging Commands

```bash
# Check if lock file is in sync
uv lock --check

# See what would change without updating
uv lock --upgrade --dry-run

# Update specific package
uv lock --upgrade-package requests

# Regenerate from scratch
rm uv.lock && uv lock

# Verify lock file is valid TOML
python -c "import tomllib; tomllib.load(open('uv.lock', 'rb'))"

# Check lock file size (should be reasonable)
ls -lh uv.lock

# See packages in lock file
grep '^name = ' uv.lock | sort | uniq
```

---

## Performance Debugging

### Cache Performance

**Check cache efficiency:**
```bash
# Cache directory location
uv cache dir

# Cache size
du -sh "$(uv cache dir)"

# Number of cached items
find "$(uv cache dir)" -type f | wc -l

# Clear cache and measure impact
time uv sync
uv cache clean
time uv sync  # Will be slower without cache
```

**Optimize cache:**
```bash
# Prune old entries
uv cache prune

# Set cache location on fast disk
export UV_CACHE_DIR=/path/to/fast/disk/cache
```

### Installation Speed

**Measure installation time:**
```bash
# Cold start (no cache)
uv cache clean
time uv sync

# Warm start (with cache)
time uv sync

# Compare with pip
time pip install -r requirements.txt
```

**Optimize installation:**
```bash
# Use wheels (avoid source builds)
uv sync --only-binary :all:

# Parallel downloads (default)
# UV automatically parallelizes

# Use local network cache
uv sync --index-url http://local-pypi-mirror/
```

### Build Performance

**Profile builds:**
```bash
# Time build process
time uv build

# Verbose output to see slow steps
uv build -v
```

**Optimize builds:**
```bash
# Use faster build backend
# pyproject.toml:
[build-system]
requires = ["hatchling"]  # Fast
# Instead of:
requires = ["setuptools>=61.0"]  # Slower
```

### Resolution Performance

**Measure resolution time:**
```bash
# Time dependency resolution
rm uv.lock
time uv lock

# With verbose output
time uv lock -vv
```

**Optimize resolution:**
```bash
# Use tighter version ranges
# Slower:
dependencies = ["requests"]

# Faster:
dependencies = ["requests>=2.31,<3.0"]

# Use --resolution lowest for faster resolution
uv lock --resolution lowest
```

### Tool Invocation Performance

**Measure tool startup:**
```bash
# Cold start
uv cache clean
time uvx starwars-namegen

# Warm start
time uvx starwars-namegen

# Installed tool
uv tool install starwars-namegen
time starwars-namegen
```

**Results (typical):**
- uvx cold start: 2-3 seconds
- uvx warm start: 0.05 seconds
- uv tool install: 0.005 seconds

**Optimization:**
```bash
# For frequent use: install permanently
uv tool install starwars-namegen

# For CI/CD: cache UV's cache directory
```

### Network Performance

**Diagnose slow downloads:**
```bash
# Check connection to PyPI
time curl -I https://pypi.org/

# Use fast mirror
uv sync --index-url https://fast-mirror.example.com/simple/

# Multiple package indices
uv sync \
    --index-url https://pypi.org/simple/ \
    --extra-index-url https://mirror.example.com/simple/
```

**Monitor network usage:**
```bash
# During installation
uv sync -v | grep -i "download"

# Check total downloaded
du -sh "$(uv cache dir)"
```

---

## CI/CD Troubleshooting

### Cache Configuration

**GitHub Actions:**
```yaml
- uses: astral-sh/setup-uv@v1
  with:
    enable-cache: true
    cache-dependency-glob: |
      **/uv.lock
      **/pyproject.toml
```

**GitLab CI:**
```yaml
cache:
  key:
    files:
      - uv.lock
      - pyproject.toml
  paths:
    - .cache/uv/

before_script:
  - export UV_CACHE_DIR="$CI_PROJECT_DIR/.cache/uv"
```

**Docker:**
```dockerfile
# Use BuildKit cache mounts
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen
```

### Reproducible Builds

**Problem: Different versions in CI vs local**

**Solution:**
```bash
# Always use --frozen in CI
uv sync --frozen

# This ensures:
# - Exact versions from lock file
# - No dependency resolution
# - Fails if lock is out of date
```

**Verify reproducibility:**
```bash
# Local
uv sync
uv run python -c "import requests; print(requests.__version__)"

# CI should print same version
```

### Environment Variables in CI

**Set up properly:**
```yaml
# GitHub Actions
env:
  UV_CACHE_DIR: ${{ github.workspace }}/.cache/uv
  UV_PYTHON_INSTALL_DIR: ${{ github.workspace }}/.python

# GitLab CI
variables:
  UV_CACHE_DIR: "$CI_PROJECT_DIR/.cache/uv"
  UV_PYTHON_INSTALL_DIR: "$CI_PROJECT_DIR/.python"
```

### Common CI Errors

**Error 1: uv not found**

**Solution:**
```yaml
# Install UV in CI
- name: Install UV
  run: curl -LsSf https://astral.sh/uv/install.sh | sh

- name: Add UV to PATH
  run: echo "$HOME/.cargo/bin" >> $GITHUB_PATH

# Or use action
- uses: astral-sh/setup-uv@v1
```

**Error 2: Python version mismatch**

**Solution:**
```yaml
# Explicitly install Python
- name: Install Python
  run: uv python install 3.12

# Or use specific version
- name: Sync with specific Python
  run: uv sync --python 3.12
```

**Error 3: Permission errors**

**Solution:**
```yaml
# Don't use sudo with UV
- run: uv sync  # ✅ Correct

# Not:
- run: sudo uv sync  # ❌ Wrong

# If you need system packages:
- run: sudo apt-get install build-essential
- run: uv sync  # Run UV without sudo
```

**Error 4: Disk space issues**

**Solution:**
```yaml
# Clean up before installation
- run: uv cache prune

# Or use smaller cache
- run: uv sync --no-cache
```

### Docker-Specific Issues

**Multi-stage builds:**
```dockerfile
# Builder stage
FROM python:3.12-slim as builder
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.cargo/bin:$PATH"
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

# Runtime stage
FROM python:3.12-slim
COPY --from=builder /app/.venv /app/.venv
COPY src/ /app/src/
ENV PATH="/app/.venv/bin:$PATH"
CMD ["starwars-namegen"]
```

**Optimize Docker builds:**
```dockerfile
# Use cache mounts (BuildKit)
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen

# Separate dependency and code layers
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen
COPY . .  # Code changes don't invalidate dependency layer
```

---

## Quick Reference

### Diagnostic Commands

```bash
# Check UV installation
uv --version
which uv

# Check Python versions
uv python list
uv python dir

# Check cache
uv cache dir
uv cache prune

# Check tools
uv tool list
uv tool dir

# Check project
uv tree
uv lock --check

# Environment info
env | grep UV_
echo $PATH
```

### Emergency Fixes

```bash
# Nuclear option: Start fresh
uv cache clean
rm -rf .venv uv.lock
uv sync

# Reinstall tool
uv tool uninstall tool-name
uv cache clean
uv tool install tool-name

# Fix PATH
uv tool update-shell
exec $SHELL

# Update everything
uv lock --upgrade
uv sync
```

### Getting Help

1. **Read error messages** - UV provides helpful hints
2. **Check documentation** - https://docs.astral.sh/uv/
3. **Search GitHub issues** - https://github.com/astral-sh/uv/issues
4. **Increase verbosity** - Add `-v`, `-vv`, or `-vvv`
5. **Ask community** - UV Discord, Reddit, Stack Overflow

---

## Conclusion

UV is a powerful tool that requires understanding of:
- Dependency resolution
- Virtual environments
- Python version management
- Package distribution
- Cross-platform considerations

When things go wrong:
1. Read the error message carefully
2. Check the basics (PATH, Python version, cache)
3. Increase verbosity to see what's happening
4. Search for similar issues
5. Try the nuclear option (clean cache, start fresh)

Most issues have simple solutions once you understand UV's mental model.

**Happy debugging!**
