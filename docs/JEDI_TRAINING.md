# JEDI TRAINING: Path to UV Mastery

> *"A Jedi uses the Force for knowledge and defense, never for attack."* - Master Yoda
> *Similarly, a developer uses UV for speed and reliability, never for complexity.*

**Status**: Jedi Archive - Complete Training Program
**Classification**: Educational Holocron
**Author**: Jedi Council of Python Development

---

## Table of Contents

1. [**Youngling Training**: First Steps with UV](#youngling-training-first-steps-with-uv)
2. [**Padawan Path**: Building Your First CLI Tool](#padawan-path-building-your-first-cli-tool)
3. [**Knight Trials**: Testing & Quality](#knight-trials-testing--quality)
4. [**Master Techniques**: Publishing & Distribution](#master-techniques-publishing--distribution)
5. [**Council Wisdom**: Best Practices](#council-wisdom-best-practices)

---

## Youngling Training: First Steps with UV

### The Force Awakens: What is UV?

UV is to Python what a lightsaber is to a Jedi - an elegant weapon for a more civilized age. It replaces the clunky blaster of `pip` with something far more powerful:

```bash
# The Old Way (Slow, Like a Podrace on Tatooine)
pip install package-name      # 5-10 seconds
virtualenv venv              # 2-3 seconds
source venv/bin/activate     # Manual activation

# The New Way (Fast, Like the Millennium Falcon)
uv add package-name          # 0.1 seconds (50-100x faster!)
uv run your-script.py       # Auto-activates environment
```

### Why UV is Your Lightsaber

| Feature | pip/venv | UV | Advantage |
|---------|----------|-----|-----------|
| Speed | Pod racer | Millennium Falcon | **10-100x faster** |
| Dependency Resolution | Manually pilot | Autopilot | Automatic conflict resolution |
| Virtual Environments | Manual creation | Auto-managed | No activation needed |
| Lock Files | Separate tools | Built-in | Reproducible builds |
| Python Versions | pyenv | Built-in | Install any version |

### Your First Mission: Installing UV

```bash
# MacOS / Linux (One-liner, Like a Jedi Mind Trick)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps3 | iex"

# Verify Installation (Check Your Lightsaber Works)
uv --version
# Output: uv 0.6.14 (or later)
```

### Training Exercise 1: Create Your First Project

```bash
# Initialize a new CLI tool project (Build Your Lightsaber)
uv init --package rebel-tool
cd rebel-tool

# Project structure created:
# rebel-tool/
#   ├── src/
#   │   └── rebel_tool/
#   │       ├── __init__.py
#   │       └── cli.py
#   ├── tests/
#   ├── pyproject.toml
#   └── uv.lock

# Add dependencies (Gather Your Allies)
uv add click rich

# Add dev dependencies (Get Training Gear)
uv add --group dev pytest pytest-cov ruff mypy

# Install everything (Assemble Your Squadron)
uv sync

# Run your tool (Ignite Your Lightsaber!)
uv run rebel-tool --help
```

### Understanding the Force: UV vs UVX

```bash
# UV: For Project Dependencies (Your Personal Ship)
cd my-project
uv add requests  # Adds to pyproject.toml, installs in .venv
uv run python script.py  # Runs in project environment

# UVX: For One-Off Tools (Hyperspace Jump - Ephemeral)
uvx black .  # Formats code without installing
uvx ruff check  # Lints without polluting project
uvx starwars-namegen -m 10  # Use tool without commitment

# UV Tool Install: For Frequent Tools (Your Arsenal)
uv tool install black  # Install globally
black .  # Now available everywhere
```

**Jedi Wisdom**:
- Use `uv` for projects you're developing
- Use `uvx` for tools you use occasionally
- Use `uv tool install` for tools you use daily

---

## Padawan Path: Building Your First CLI Tool

### Mission Briefing: Create a Holocron Reader

We'll build a CLI tool that reads and displays Star Wars quotes - perfect for learning UV patterns.

### Step 1: Project Structure (The Temple Layout)

```bash
uv init --package holocron-reader
cd holocron-reader

# Your temple structure:
holocron-reader/
├── src/
│   └── holocron_reader/
│       ├── __init__.py      # The Force binds the galaxy together
│       ├── cli.py           # Jedi Council Chamber (CLI interface)
│       ├── quotes.py        # Holocron Archives (Data)
│       └── display.py       # Holoprojector (Output formatting)
├── tests/
│   ├── test_cli.py          # Test your Jedi skills
│   └── conftest.py          # Training scenarios
├── pyproject.toml           # The Jedi Code
└── uv.lock                  # The Sacred Texts (COMMIT THIS!)
```

### Step 2: Configure Your Holocron (pyproject.toml)

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "holocron-reader"
version = "0.1.0"
description = "Read wisdom from the Jedi Archives"
readme = "README.md"
requires-python = ">=3.9"
license = {text = "MIT"}
authors = [
    {name = "Obi-Wan Kenobi", email = "obiwan@jediorder.org"}
]
keywords = ["star-wars", "quotes", "cli", "holocron"]
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Jedi Order",
    "Topic :: Philosophy :: Force",
]

# The Lightsaber Ignition Sequence (Entry Point)
[project.scripts]
holocron = "holocron_reader.cli:main"
hr = "holocron_reader.cli:main"  # Short form for quick draws

# Your Jedi Arsenal (Dependencies)
dependencies = [
    "click>=8.1.0",     # Command interface
    "rich>=13.0.0",     # Beautiful output
]

# Training Equipment (Dev Dependencies)
[dependency-groups]
dev = [
    "pytest>=8.0.0",
    "pytest-cov>=4.1.0",
    "ruff>=0.8.0",
    "mypy>=1.8.0",
]

[tool.uv]
managed = true  # Let UV be your Jedi Master
```

### Step 3: The Holocron Archives (quotes.py)

```python
# src/holocron_reader/quotes.py
"""The Sacred Jedi Archives - Wisdom Preserved"""

JEDI_WISDOM = [
    {
        "quote": "Do or do not. There is no try.",
        "speaker": "Yoda",
        "location": "Dagobah",
        "philosophy": "Commitment",
    },
    {
        "quote": "The Force will be with you, always.",
        "speaker": "Obi-Wan Kenobi",
        "location": "Death Star",
        "philosophy": "Faith",
    },
    {
        "quote": "Fear is the path to the dark side.",
        "speaker": "Yoda",
        "location": "Jedi Temple",
        "philosophy": "Wisdom",
    },
    {
        "quote": "In my experience, there's no such thing as luck.",
        "speaker": "Obi-Wan Kenobi",
        "location": "Millennium Falcon",
        "philosophy": "Preparation",
    },
]

SITH_MAXIMS = [
    {
        "quote": "Power! Unlimited power!",
        "speaker": "Darth Sidious",
        "location": "Senate Chamber",
        "philosophy": "Domination",
    },
    {
        "quote": "I find your lack of faith disturbing.",
        "speaker": "Darth Vader",
        "location": "Death Star",
        "philosophy": "Fear",
    },
]

def get_random_quote(side="jedi"):
    """Retrieve wisdom from the archives."""
    import random
    source = JEDI_WISDOM if side == "jedi" else SITH_MAXIMS
    return random.choice(source)

def get_all_quotes():
    """Access all archived wisdom."""
    return JEDI_WISDOM + SITH_MAXIMS
```

### Step 4: The Holoprojector (display.py)

```python
# src/holocron_reader/display.py
"""Holoprojector - Display wisdom in beautiful formats"""
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

console = Console()

def display_quote(quote_data, show_meta=True):
    """Project a quote holographically."""
    quote_text = Text(quote_data["quote"], style="bold cyan")

    if show_meta:
        meta = f"\n\n— {quote_data['speaker']}"
        if 'location' in quote_data:
            meta += f", {quote_data['location']}"
        quote_text.append(meta, style="italic yellow")

    panel = Panel(
        quote_text,
        title="[bold blue]⚔️  Holocron Archive  ⚔️[/bold blue]",
        border_style="blue",
        padding=(1, 2)
    )

    console.print(panel)

def display_quote_table(quotes):
    """Display multiple quotes in archive format."""
    table = Table(title="Jedi Archives - Compiled Wisdom")

    table.add_column("Speaker", style="cyan", width=20)
    table.add_column("Quote", style="green", width=50)
    table.add_column("Philosophy", style="magenta", width=15)

    for q in quotes:
        table.add_row(
            q["speaker"],
            q["quote"],
            q["philosophy"]
        )

    console.print(table)
```

### Step 5: The Council Chamber (cli.py)

```python
# src/holocron_reader/cli.py
"""Command-line interface - The Jedi Council Chamber"""
import click
from rich.console import Console
from . import __version__
from .quotes import get_random_quote, get_all_quotes
from .display import display_quote, display_quote_table

console = Console()

@click.group()
@click.version_option(version=__version__)
def cli():
    """
    🌌 Holocron Reader - Access wisdom from the Star Wars universe

    May the Force be with you!
    """
    pass

@cli.command()
@click.option('--side', type=click.Choice(['jedi', 'sith']),
              default='jedi', help='Choose your path')
@click.option('--plain', is_flag=True, help='Plain text output')
def random(side, plain):
    """Display a random quote from the archives."""
    quote = get_random_quote(side)

    if plain:
        console.print(f'"{quote["quote"]}" - {quote["speaker"]}')
    else:
        display_quote(quote)

@cli.command()
@click.option('--format', type=click.Choice(['table', 'list']),
              default='table', help='Display format')
def all(format):
    """Display all quotes from the archives."""
    quotes = get_all_quotes()

    if format == 'table':
        display_quote_table(quotes)
    else:
        for quote in quotes:
            display_quote(quote, show_meta=True)
            console.print()

@cli.command()
@click.argument('search_term')
def search(search_term):
    """Search the archives for specific wisdom."""
    quotes = get_all_quotes()
    results = [
        q for q in quotes
        if search_term.lower() in q['quote'].lower() or
           search_term.lower() in q['speaker'].lower()
    ]

    if results:
        console.print(f"\n[green]Found {len(results)} results:[/green]\n")
        for quote in results:
            display_quote(quote)
            console.print()
    else:
        console.print(f"[red]No wisdom found matching '{search_term}'[/red]")

@cli.command()
def about():
    """Learn about this holocron."""
    console.print("""
    [bold cyan]Holocron Reader v{__version__}[/bold cyan]

    This tool accesses the Jedi Archives to retrieve ancient wisdom
    and philosophy from the Star Wars universe.

    [yellow]Usage Examples:[/yellow]

      # Display random Jedi wisdom
      [green]$ holocron random[/green]

      # Display Sith philosophy
      [green]$ holocron random --side sith[/green]

      # Search for specific wisdom
      [green]$ holocron search force[/green]

      # View all archived quotes
      [green]$ holocron all[/green]

    [italic]May the Force be with you![/italic]
    """)

def main():
    """Entry point - Activate the holocron."""
    cli()

if __name__ == '__main__':
    main()
```

### Step 6: Test Your Jedi Skills (tests/test_cli.py)

```python
# tests/test_cli.py
"""Test your mastery of the Force"""
import pytest
from click.testing import CliRunner
from holocron_reader.cli import cli

@pytest.fixture
def runner():
    """Prepare the training ground."""
    return CliRunner()

def test_random_quote_jedi(runner):
    """Test retrieving Jedi wisdom."""
    result = runner.invoke(cli, ['random'])
    assert result.exit_code == 0
    assert 'Holocron Archive' in result.output or 'quote' in result.output.lower()

def test_random_quote_sith(runner):
    """Test retrieving Sith philosophy."""
    result = runner.invoke(cli, ['random', '--side', 'sith'])
    assert result.exit_code == 0

def test_search_found(runner):
    """Test searching archives successfully."""
    result = runner.invoke(cli, ['search', 'force'])
    assert result.exit_code == 0
    assert 'Found' in result.output or 'force' in result.output.lower()

def test_search_not_found(runner):
    """Test searching for nonexistent wisdom."""
    result = runner.invoke(cli, ['search', 'zzzznonexistent'])
    assert result.exit_code == 0
    assert 'No wisdom found' in result.output

def test_all_quotes(runner):
    """Test displaying all archived wisdom."""
    result = runner.invoke(cli, ['all'])
    assert result.exit_code == 0

def test_about(runner):
    """Test about information."""
    result = runner.invoke(cli, ['about'])
    assert result.exit_code == 0
    assert 'Holocron Reader' in result.output
```

### Step 7: Train and Deploy (Development Workflow)

```bash
# 1. Install your project in development mode
uv sync

# 2. Run during development (The Training Begins)
uv run holocron random
uv run holocron random --side sith
uv run holocron search force
uv run holocron all --format table

# 3. Run tests (Prove Your Worth)
uv run pytest
uv run pytest --cov=holocron_reader --cov-report=html

# 4. Check code quality (Maintain the Code)
uv run ruff check src tests
uv run mypy src

# 5. Build the holocron (Prepare for Distribution)
uv build

# 6. Test the built package locally
uv pip install dist/*.whl
holocron random

# 7. Test with uvx (Ephemeral Trial)
uvx --from . holocron random

# Success! You've built your first UV-powered CLI tool! 🎉
```

---

## Knight Trials: Testing & Quality

### The Path of the Jedi: Comprehensive Testing

A Jedi's strength flows from testing. Testing leads to confidence. Confidence leads to deployment. Deployment leads to... success!

```bash
# Install testing arsenal
uv add --group dev pytest pytest-cov pytest-mock mypy ruff

# Configure in pyproject.toml
```

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
addopts = [
    "--strict-markers",
    "--cov=holocron_reader",
    "--cov-report=term-missing",
    "--cov-report=html",
    "--cov-fail-under=80",  # Require 80% coverage (Jedi Standard)
]

[tool.ruff]
line-length = 100
target-version = "py39"

[tool.ruff.lint]
select = ["E", "F", "I", "B", "C4", "UP"]
ignore = ["E501"]  # Line length handled by formatter

[tool.mypy]
python_version = "3.9"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
```

### Testing Patterns (Jedi Combat Forms)

**Form I: Basic Command Testing**
```python
def test_command_works(runner):
    """Shii-Cho - Basic lightsaber form"""
    result = runner.invoke(cli, ['command'])
    assert result.exit_code == 0
```

**Form II: Parametrized Testing**
```python
@pytest.mark.parametrize("side,expected", [
    ("jedi", "Force"),
    ("sith", "power"),
])
def test_multiple_scenarios(runner, side, expected):
    """Makashi - Elegant dueling form"""
    result = runner.invoke(cli, ['random', '--side', side])
    assert expected.lower() in result.output.lower()
```

**Form III: Mock Testing**
```python
def test_with_mocking(monkeypatch):
    """Soresu - Defensive form"""
    def mock_api_call(*args):
        return {"data": "test"}

    monkeypatch.setattr("my_module.api_call", mock_api_call)
    # Test with mocked dependency
```

### The Trial: Run All Tests

```bash
# Run all tests
uv run pytest

# Run with coverage report
uv run pytest --cov=holocron_reader --cov-report=html

# Run specific test file
uv run pytest tests/test_cli.py

# Run specific test function
uv run pytest tests/test_cli.py::test_random_quote_jedi

# Run with verbose output
uv run pytest -vv

# Run and stop at first failure
uv run pytest -x

# Run only failed tests from last run
uv run pytest --lf
```

---

## Master Techniques: Publishing & Distribution

### Preparing for the Galaxy (Pre-Publish Checklist)

Before sharing your holocron with the galaxy:

```bash
# ✅ 1. All tests pass
uv run pytest

# ✅ 2. Code quality check
uv run ruff check src tests
uv run mypy src

# ✅ 3. Documentation is complete
# - README.md with examples
# - LICENSE file
# - CHANGELOG.md

# ✅ 4. Version is set correctly
# In pyproject.toml: version = "0.1.0"

# ✅ 5. Build succeeds
uv build

# ✅ 6. Local installation works
uv pip install dist/*.whl
holocron --version
```

### The Publishing Ritual (Deploy to PyPI)

**Method 1: Trusted Publishing (Jedi Council Approved - 2025)**

1. **Configure PyPI Trusted Publisher**:
   - Go to https://pypi.org/manage/account/publishing/
   - Add publisher:
     - Owner: your-github-username
     - Repository: holocron-reader
     - Workflow: publish.yml
     - Environment: pypi

2. **Create GitHub Action**:

```yaml
# .github/workflows/publish.yml
name: Publish to PyPI

on:
  push:
    tags:
      - 'v*'  # Trigger on version tags

jobs:
  publish:
    runs-on: ubuntu-latest
    environment:
      name: pypi
    permissions:
      id-token: write  # Required for trusted publishing
      contents: read

    steps:
      - uses: actions/checkout@v5

      - name: Install uv
        uses: astral-sh/setup-uv@v7

      - name: Set up Python
        run: uv python install 3.13

      - name: Install dependencies
        run: uv sync --all-extras --dev

      - name: Run tests
        run: uv run pytest

      - name: Build package
        run: uv build

      - name: Publish to PyPI
        run: uv publish
```

3. **Release**:
```bash
# Update version
uv version --bump minor

# Commit and tag
git add pyproject.toml
git commit -m "chore: bump version to 0.2.0"
git tag v0.2.0
git push origin main
git push origin v0.2.0

# GitHub Actions handles the rest!
```

**Method 2: Manual Publishing (For Quick Releases)**

```bash
# Create PyPI API token at https://pypi.org/manage/account/token/
export UV_PUBLISH_TOKEN="pypi-..."

# Build and publish
uv build
uv publish

# Or publish to Test PyPI first
uv publish --index-url https://test.pypi.org/legacy/
```

### After Publishing: Verification

```bash
# Install from PyPI
uvx holocron-reader random

# Or install globally
uv tool install holocron-reader
holocron random

# Check on PyPI
open https://pypi.org/project/holocron-reader/
```

---

## Council Wisdom: Best Practices

### The Jedi Code of UV Development

```python
# DO: Use uv for everything in 2025
uv add package-name           # ✅ Correct
uv run pytest                 # ✅ Correct

# DON'T: Mix old and new ways
pip install package-name      # ❌ Wrong (in UV projects)
python -m pytest              # ❌ Wrong (use 'uv run')

# DO: Commit lock files
git add uv.lock               # ✅ Reproducible builds

# DON'T: Gitignore lock files
echo "uv.lock" >> .gitignore  # ❌ Breaks reproducibility

# DO: Use src/ layout for packages
my-tool/
  src/
    my_tool/              # ✅ Prevents import accidents

# DON'T: Use flat layout for packages
my-tool/
  my_tool/              # ❌ Can import from wrong location

# DO: Separate CLI from logic
cli.py    # Click commands only
core.py   # Business logic (easy to test)

# DON'T: Mix CLI and logic
cli.py    # Everything in one file ❌
```

### Common Padawan Mistakes (And How to Avoid Them)

**Mistake 1: Using `python` instead of `uv run`**
```bash
# ❌ Wrong
python my_script.py

# ✅ Correct
uv run python my_script.py
uv run my-tool
```

**Mistake 2: Not committing uv.lock**
```bash
# ❌ Wrong
echo "uv.lock" >> .gitignore

# ✅ Correct
git add uv.lock
git commit -m "chore: add lockfile for reproducibility"
```

**Mistake 3: Manual venv activation**
```bash
# ❌ Wrong (The old way)
source .venv/bin/activate
python script.py

# ✅ Correct (The UV way)
uv run python script.py  # Auto-activates environment
```

**Mistake 4: Installing UV with pip**
```bash
# ❌ Wrong (Creates dependency loops)
pip install uv

# ✅ Correct (Official installer)
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Mistake 5: Using uv pip in projects**
```bash
# ❌ Wrong (Bypasses project management)
uv pip install requests

# ✅ Correct (Adds to pyproject.toml)
uv add requests
```

### The Master's Workflow (Daily Development)

```bash
# Morning: Sync project (Update from lock file)
cd my-project
uv sync

# Add new feature dependency
uv add new-package

# Add new dev tool
uv add --group dev new-dev-tool

# Run during development
uv run my-tool --option value

# Run tests
uv run pytest

# Check code quality
uv run ruff check .
uv run mypy src

# Before committing
uv run pytest --cov
git add .
git commit -m "feat: add new feature"

# Afternoon: Update dependencies
uv lock --upgrade      # Update lock file
uv sync               # Apply updates
uv run pytest         # Verify still works

# Evening: Publish new version
uv version --bump patch
git add pyproject.toml
git commit -m "chore: bump version"
git tag v0.1.1
git push origin main --tags
```

---

## Graduation: You Are Now a Jedi Knight

Congratulations, Padawan! You have completed your training in the ways of UV. You now know:

✅ How to create UV projects with proper structure
✅ How to configure pyproject.toml like a master
✅ How to build beautiful CLI tools with Click and Rich
✅ How to test comprehensively with pytest
✅ How to publish to PyPI with trusted publishing
✅ How to follow Jedi best practices

**Your Next Missions**:
1. Read [FORCE_POWERS.md](./FORCE_POWERS.md) for advanced UV techniques
2. Study [HOLOCRON.md](./HOLOCRON.md) for deep technical reference
3. Review [MISSION_BRIEFINGS.md](./MISSION_BRIEFINGS.md) for real-world patterns

**Remember**:
> "The Force will be with you, always." - Obi-Wan Kenobi

And UV will be with your Python projects, always. 🌌

---

**May the Force (and fast package management) be with you!**

*Document Version*: 1.0
*Last Updated*: 2025
*Jedi Council Seal*: ⚔️ Approved for training ⚔️
