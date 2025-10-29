# The Complete UV Guide: Modern Python Packaging

**Learn UV through a working example: The Star Wars Name Generator**

This guide uses `starwars-namegen` as a real-world example to teach you everything about UV, the blazingly fast Python package manager and project manager.

---

## Table of Contents

1. [What is UV?](#what-is-uv)
2. [Why UV Over pip/poetry/pipenv?](#why-uv)
3. [UV vs UVX: Understanding the Difference](#uv-vs-uvx)
4. [Installation & Setup](#installation--setup)
5. [Project Structure: The UV Way](#project-structure)
6. [Understanding pyproject.toml](#understanding-pyprojecttoml)
7. [The uv.lock File: Reproducible Builds](#the-uvlock-file)
8. [Development Workflow](#development-workflow)
9. [Building & Publishing](#building--publishing)
10. [Best Practices](#best-practices)

---

## What is UV?

**UV** is an extremely fast Python package and project manager written in Rust. It's designed to replace pip, pip-tools, pipx, poetry, pyenv, twine, and virtualenv with a single, fast tool.

### Key Features

- **10-100x faster** than pip
- **Zero Python installation required** - UV manages Python for you
- **Universal lock files** for reproducible builds
- **Drop-in replacement** for pip commands
- **Built-in virtual environment management**
- **Project scaffolding** and dependency management
- **Package publishing** to PyPI

---

## Why UV Over pip/poetry/pipenv?

### The Old Way (pip)

```bash
# Install Python 3.9-3.12
python3 -m venv .venv
source .venv/bin/activate
pip install click inflect
pip freeze > requirements.txt
python -m build
python -m twine upload dist/*
```

**Problems:**
- Multiple tools (venv, pip, build, twine)
- Slow dependency resolution
- No lock files (requirements.txt isn't deterministic)
- Manual Python version management
- Dependency conflicts are common

### The Poetry Way

```bash
poetry init
poetry add click inflect
poetry build
poetry publish
```

**Problems:**
- Still relatively slow
- Heavy dependency (Poetry itself)
- Lock file can be massive
- Sometimes conflicts with pip

### The UV Way

```bash
uv init
uv add click inflect
uv build
uv publish
```

**Advantages:**
- **Single command** for everything
- **10-100x faster** than pip
- **Universal lock files** that work everywhere
- **No Python required** to start
- **Zero configuration** needed

---

## UV vs UVX: Understanding the Difference

This is **critical** to understand - UV and UVX serve different purposes:

### UV (Package/Project Manager)

**Use when:** You're developing a project or installing tools globally

```bash
# Project management
uv sync                    # Install project dependencies
uv add requests            # Add a dependency
uv run pytest              # Run command in project venv
uv build                   # Build your package

# Global tool installation
uv tool install starwars-namegen
starwars-namegen           # Use the installed tool
```

**UV creates**: Persistent installations in `~/.local/share/uv/tools`

### UVX (Zero-Install Runner)

**Use when:** You want to run a tool WITHOUT installing it

```bash
# Run WITHOUT installing (zero-install)
uvx starwars-namegen -c 3 -f snake

# Every uvx invocation:
# 1. Downloads package (if not cached)
# 2. Creates temporary venv
# 3. Runs the command
# 4. Cleans up

# Perfect for:
uvx black .                # Format code once
uvx pytest                 # Run tests without installing
uvx mkdocs serve           # Preview docs temporarily
```

**UVX creates**: Temporary environments (cached for speed)

### Decision Matrix

| Scenario | Use | Why |
|----------|-----|-----|
| Developing starwars-namegen | `uv sync` + `uv run` | Need persistent dev environment |
| Using starwars-namegen occasionally | `uvx starwars-namegen` | No installation needed |
| Using starwars-namegen frequently | `uv tool install` | Persistent, faster startup |
| CI/CD pipeline | `uvx starwars-namegen` | Clean, reproducible |
| Trying out a new tool | `uvx tool-name` | No commitment |

---

## Installation & Setup

### Installing UV

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# With Homebrew
brew install uv

# Verify installation
uv --version
```

### Your First UV Project

```bash
# Create new project
uv init my-project
cd my-project

# UV automatically creates:
# my-project/
# ├── pyproject.toml
# ├── .python-version
# ├── src/
# │   └── my_project/
# │       └── __init__.py
# └── README.md

# Add dependencies
uv add click requests

# Create virtual environment and install deps
uv sync

# Run your code
uv run python -m my_project
```

---

## Project Structure: The UV Way

Let's examine `starwars-namegen` structure:

```
starwars-namegen/
├── pyproject.toml          # Project metadata & dependencies
├── uv.lock                 # Lock file (committed to git)
├── .python-version         # Python version for project
├── src/
│   └── starwars_namegen/   # Source code (note underscore)
│       ├── __init__.py
│       └── cli.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_cli.py
│   └── test_generator.py
├── examples/               # Usage examples
├── docs/                   # Documentation
└── README.md
```

### Key Points

1. **src-layout**: Code in `src/` prevents accidental imports
2. **Underscores in package name**: `starwars_namegen` (Python), not `starwars-namegen` (PyPI)
3. **uv.lock committed**: Ensures reproducible installs
4. **.python-version**: Specifies exact Python version

---

## Understanding pyproject.toml

The `pyproject.toml` is your project's configuration hub. Let's break down `starwars-namegen`:

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```
**Explanation**: Tells UV how to build your package. Hatchling is fast and simple.

```toml
[project]
name = "starwars-namegen"
version = "0.1.0"
description = "Generate Star Wars-themed names"
readme = "README.md"
requires-python = ">=3.9"
```
**Explanation**: Basic metadata. PyPI uses this for the package page.

```toml
dependencies = [
    "click>=8.0.0",
    "inflect>=7.0.0",
]
```
**Explanation**: Runtime dependencies. UV resolves these automatically.

```toml
[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "pytest-cov>=4.0.0",
    "mypy>=1.0.0",
]
```
**Explanation**: Development dependencies. Install with `uv sync --all-extras`.

```toml
[project.scripts]
starwars-namegen = "starwars_namegen.cli:main"
```
**Explanation**: Creates CLI command. **This is how uvx knows what to run!**

When you run `uvx starwars-namegen`, UV:
1. Finds `starwars_namegen.cli` module
2. Calls the `main()` function
3. Passes CLI arguments

---

## The uv.lock File: Reproducible Builds

The `uv.lock` file is UV's secret weapon for reproducibility.

### What's in uv.lock?

```
# Direct dependencies
click==8.1.0
inflect==7.0.0

# Transitive dependencies (dependencies of dependencies)
importlib-metadata==6.8.0
zipp==3.17.0

# With exact versions and hashes
click==8.1.0 --hash=sha256:xyz123...
```

### Why Lock Files Matter

```bash
# Without lock file (pip)
pip install click  # Gets click 8.1.0 today, 8.2.0 tomorrow
# Result: "Works on my machine" syndrome

# With lock file (uv)
uv sync           # Everyone gets EXACT same versions
# Result: True reproducibility
```

### Lock File Workflow

```bash
# First time: Create lock file
uv sync           # Generates uv.lock

# Commit lock file
git add uv.lock pyproject.toml
git commit -m "feat: add dependencies"

# Team member clones repo
git clone repo
uv sync           # Gets EXACT same versions

# Update dependencies
uv add requests@latest  # Updates uv.lock
uv lock --upgrade       # Upgrade all deps
```

---

## Development Workflow

### Day-to-Day Development

```bash
# Start new feature
git checkout -b feature/new-thing

# Add dependency
uv add httpx

# Run tests
uv run pytest

# Run your CLI (development mode)
uv run starwars-namegen -c 3 -f snake

# Run with specific Python
uv run --python 3.12 pytest

# Add dev dependency
uv add --dev ruff

# Sync after pulling changes
git pull
uv sync
```

### Testing Different Python Versions

```bash
# Test on Python 3.9
uv run --python 3.9 pytest

# Test on Python 3.12
uv run --python 3.12 pytest

# UV downloads Python automatically if needed!
```

### Type Checking & Linting

```bash
# Add dev tools
uv add --dev mypy ruff

# Run type checking
uv run mypy src/

# Run linting
uv run ruff check src/

# Auto-format
uv run ruff format src/
```

---

## Building & Publishing

### Building Your Package

```bash
# Build distribution packages
uv build

# Creates:
# dist/
# ├── starwars_namegen-0.1.0-py3-none-any.whl  (wheel)
# └── starwars_namegen-0.1.0.tar.gz            (source)
```

### Publishing to PyPI

```bash
# Get API token from https://pypi.org/manage/account/token/

# Set token
export UV_PUBLISH_TOKEN="pypi-YOUR_TOKEN_HERE"

# Publish
uv publish

# Now anyone can:
uvx starwars-namegen  # Zero-install usage!
```

### Testing Your Package Locally

```bash
# Build and install globally
uv build
uv tool install dist/starwars_namegen-0.1.0-py3-none-any.whl

# Test it
starwars-namegen --help

# Uninstall
uv tool uninstall starwars-namegen
```

---

## Best Practices

### 1. Always Commit uv.lock

```bash
# .gitignore should NOT include:
# uv.lock        # ❌ Never ignore this!

# .gitignore SHOULD include:
.venv/
__pycache__/
dist/
*.pyc
```

### 2. Use src-layout

```
✅ GOOD:
src/
  starwars_namegen/
    __init__.py
    cli.py

❌ BAD:
starwars_namegen/
  __init__.py
  cli.py
```

**Why?** Prevents accidental imports from working directory.

### 3. Pin Python Version

```toml
# pyproject.toml
requires-python = ">=3.9"  # Minimum version

# .python-version
3.11                       # Exact version for dev
```

### 4. Use Scripts Entry Points

```toml
[project.scripts]
my-tool = "my_package.cli:main"  # Enables uvx!
```

### 5. Separate Dev Dependencies

```toml
[project.optional-dependencies]
dev = ["pytest", "mypy", "ruff"]
```

```bash
# Production install
uv sync

# Development install
uv sync --all-extras
```

### 6. Document UV Commands

In your README:

```markdown
## Development

# Setup
uv sync --all-extras

# Run tests
uv run pytest

# Run CLI
uv run my-tool [OPTIONS]

## Usage

# Zero-install (recommended)
uvx my-tool [OPTIONS]

# Or install globally
uv tool install my-tool
my-tool [OPTIONS]
```

---

## Common Patterns

### CLI Tool (like starwars-namegen)

```toml
[project.scripts]
my-tool = "my_package.cli:main"

dependencies = ["click", "rich"]
```

### Library Package

```toml
[project]
name = "my-library"
# No [project.scripts] needed

dependencies = ["requests", "pydantic"]
```

### Application

```toml
[project]
name = "my-app"

dependencies = [
    "fastapi",
    "uvicorn",
    "sqlalchemy",
]

[project.optional-dependencies]
dev = ["pytest", "httpx", "mypy"]
prod = ["gunicorn", "psycopg2"]
```

---

## Troubleshooting

### Issue: "No module named 'my_package'"

```bash
# Ensure you're in project directory
cd /path/to/project

# Sync dependencies
uv sync

# Run with uv run
uv run python -c "import my_package"
```

### Issue: "Command not found: my-tool"

```bash
# If using uvx, ensure package is published
uvx my-tool  # Must be on PyPI

# If using uv tool install
uv tool install my-tool
# Check: ~/.local/share/uv/tools/
```

### Issue: Dependencies not updating

```bash
# Force update lock file
uv lock --upgrade

# Sync to install updates
uv sync
```

---

## Conclusion

UV represents a major leap forward in Python packaging. By studying `starwars-namegen`, you've learned:

- ✅ Project structure and organization
- ✅ How pyproject.toml works
- ✅ Lock files for reproducibility
- ✅ Development workflows
- ✅ Building and publishing
- ✅ UVX for zero-install execution

**Next Steps:**
1. Create your own UV project: `uv init my-project`
2. Add dependencies: `uv add package-name`
3. Build and publish: `uv build && uv publish`

**May the Force (and UV) be with you!**

---

## Additional Resources

- **UV Documentation**: https://docs.astral.sh/uv/
- **PyPA Packaging Guide**: https://packaging.python.org/
- **PEP 621**: https://peps.python.org/pep-0621/ (pyproject.toml spec)
- **Star Wars Name Generator**: https://gitlab.com/hackur/starwars-namegen

**Author**: Jeremy Sarda (jeremy@hackur.io)
