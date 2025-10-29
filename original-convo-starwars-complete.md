# Star Wars Name Generator: Complete uv Tool Development & Publishing Guide

A comprehensive guide to building, testing, and publishing the Star Wars Name Generator as a professional `uv` tool for macOS, including use as both a CLI application and an installable package.

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Project Setup](#project-setup)
3. [Implementation](#implementation)
4. [Local Development & Testing](#local-development--testing)
5. [Publishing to PyPI](#publishing-to-pypi)
6. [Installation & Usage](#installation--usage)
7. [Advanced Usage](#advanced-usage)
8. [Troubleshooting](#troubleshooting)

---

## Prerequisites

### Required Tools

Ensure you have the following installed on your macOS machine:

- **macOS**: 10.13 or later (M3 Max compatible)
- **Xcode Command Line Tools**: Required for building packages
- **Python 3.9+**: uv will manage Python versions, but you need at least one to bootstrap
- **uv**: The universal Python package and project manager

### Installing uv on macOS

The recommended way to install uv on macOS is using the standalone installer:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Or, if you prefer Homebrew:

```bash
brew install uv
```

Verify installation:

```bash
uv --version
```

You should see output like: `uv 0.9.5 (e4e03833f 2025-04-02)`

### Python Version Management

uv can automatically download and manage Python versions. Ensure you have at least Python 3.9 by checking:

```bash
python3 --version
```

If you need to specify a Python version for your project, uv will handle downloading it automatically during project setup.

---

## Project Setup

### Step 1: Create the Project Directory Structure

Create a new project directory for the Star Wars Name Generator:

```bash
mkdir starwars-namegen
cd starwars-namegen
```

Create the source package directory:

```bash
mkdir -p src/starwars_namegen
```

Your directory structure should now be:

```
starwars-namegen/
├── src/
│   └── starwars_namegen/
│       ├── __init__.py
│       └── cli.py
├── pyproject.toml
├── README.md
└── .gitignore
```

### Step 2: Initialize with uv (Optional but Recommended)

If you'd like uv to help initialize the project with recommended defaults:

```bash
uv init --name starwars-namegen
```

This creates a basic `pyproject.toml` that you'll customize in the next step. If you skip this, we'll create the full `pyproject.toml` manually below.

### Step 3: Create pyproject.toml

Create a `pyproject.toml` file in the root directory with the following content:

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "starwars-namegen"
version = "0.1.0"
description = "Generate Star Wars-themed multi-word names for servers, instances, and resources"
readme = "README.md"
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]
license = {text = "MIT"}
requires-python = ">=3.9"
dependencies = [
    "click>=8.0.0",
    "inflect>=7.0.0",
]
classifiers = [
    "Development Status :: 4 - Beta",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Topic :: System :: Systems Administration",
    "Topic :: Utilities",
]
keywords = ["star-wars", "naming", "generator", "cli", "devops"]

[project.urls]
Homepage = "https://github.com/yourusername/starwars-namegen"
Documentation = "https://github.com/yourusername/starwars-namegen#readme"
Repository = "https://github.com/yourusername/starwars-namegen.git"
Issues = "https://github.com/yourusername/starwars-namegen/issues"

[project.scripts]
starwars-namegen = "starwars_namegen.cli:main"

[tool.uv]
managed = true

[tool.hatch.build.targets.wheel]
packages = ["src/starwars_namegen"]

[tool.hatch.build.targets.sdist]
include = [
    "/src",
    "/README.md",
    "/LICENSE",
]
```

**Important notes:**
- Replace `your.email@example.com` and `Your Name` with your actual details
- Replace `yourusername` with your GitHub username (or the URL where you'll host the repository)
- The `[project.scripts]` section defines `starwars-namegen` as the CLI command name
- The `requires-python` specifies the minimum Python version supported

### Step 4: Create .gitignore

Create a `.gitignore` file to exclude generated and temporary files:

```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# uv
.venv/
.uv/
uv.lock

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~
.DS_Store

# Testing
.pytest_cache/
.coverage
htmlcov/

# Project-specific
*.pyc
.env
.env.local
```

### Step 5: Create README.md

Create a `README.md` file for documentation:

```markdown
# Star Wars Name Generator

A CLI tool for generating Star Wars-themed multi-word names for servers, instances, and other resources.

## Features

- Generates 1-5 word names using Star Wars vocabulary
- Applies grammar rules to create sentence-like names
- Multiple output formats: kebab-case, snake_case, camelCase, PascalCase, space-separated
- Optional random suffixes: digits, hex, UUID, symbols
- Reproducible results with seed option
- Generate multiple names at once

## Installation

### Using uv (Recommended)

```bash
uv tool install starwars-namegen
```

### Using pip

```bash
pip install starwars-namegen
```

## Quick Start

```bash
# Generate a random name
starwars-namegen

# Generate 3-word name in snake_case
starwars-namegen -c 3 -f snake

# Generate 5 names with digit suffixes
starwars-namegen -m 5 --random digits

# Reproducible results with seed
starwars-namegen --seed 42
```

## CLI Options

- `-c, --count`: Number of words (1-5). If not specified, randomly chosen.
- `-f, --format`: Output format (kebab, snake, camel, pascal, space). Default: kebab
- `-m, --multiple`: Generate multiple names. Default: 1
- `-r, --random`: Random suffix type (none, digits, hex, symbol, uuid). Default: none
- `-s, --seed`: Random seed for reproducible results

## Output Examples

### Default (no random suffix)

```bash
$ starwars-namegen -c 3
swift-jedi-deployed

$ starwars-namegen -c 4 -f snake
stealthily_dark_sith_infiltrated
```

### With Random Suffixes

```bash
$ starwars-namegen -c 2 --random digits
galactic-trooper-347

$ starwars-namegen -c 3 --random hex
swift-jedi-deployed-a3f

$ starwars-namegen -c 2 --random uuid
rogue-falcon-b7f9d1
```

## Use Cases

Perfect for naming:
- Docker containers
- Kubernetes pods
- Server instances
- AWS EC2 instances
- Temporary directories
- Test environments
- Git branches (use kebab case)

## Development

### Clone the Repository

```bash
git clone https://github.com/yourusername/starwars-namegen.git
cd starwars-namegen
```

### Set Up Development Environment

```bash
# Install development dependencies
uv sync

# Run tests
uv run pytest

# Run the CLI
uv run starwars-namegen --help
```

### Build and Test Locally

```bash
# Build distribution
uv build

# Install locally for testing
uv tool install ./dist/starwars_namegen-0.1.0-py3-none-any.whl
```

## License

MIT License - see LICENSE file for details

## Contributing

Contributions welcome! Please feel free to submit pull requests or open issues.
```

---

## Implementation

### Step 1: Create src/starwars_namegen/__init__.py

```python
"""
Star Wars Name Generator

A CLI tool for generating Star Wars-themed multi-word names for servers,
instances, and other resources.
"""

__version__ = "0.1.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

from .cli import StarWarsNameGenerator

__all__ = ["StarWarsNameGenerator"]
```

### Step 2: Create src/starwars_namegen/cli.py

This is the main implementation file with grammar support and random suffix options:

```python
#!/usr/bin/env python3
"""
Star Wars Name Generator CLI Tool

Generates multi-word (1-5 words) unique name strings using Star Wars-themed
verbs, adverbs, nouns, etc. for use with servers, instances, and other resources.
"""

import random
import string
import click
import inflect
from typing import List


class StarWarsNameGenerator:
    """Generate Star Wars-themed names with proper grammar."""
    
    def __init__(self):
        self.p = inflect.engine()
        
        # Star Wars vocabulary categorized by part of speech
        self.nouns = [
            "jedi", "sith", "droid", "falcon", "wookiee", "empire", "rebel", 
            "force", "trooper", "saber", "cantina", "speeder", "blaster", 
            "fighter", "destroyer", "cruiser", "squadron", "legion", "padawan",
            "master", "youngling", "senator", "admiral", "general", "commander",
            "pilot", "smuggler", "bounty", "hunter", "scavenger", "princess",
            "queen", "emperor", "chancellor", "council", "temple", "academy",
            "outpost", "station", "base", "fleet", "armada", "garrison"
        ]
        
        self.verbs = [
            "blast", "strike", "charge", "hover", "spin", "deploy", "ignite",
            "wield", "pilot", "command", "defend", "attack", "pursue", "escape",
            "smuggle", "negotiate", "meditate", "train", "duel", "sabotage",
            "infiltrate", "scout", "patrol", "guard", "monitor", "scan",
            "transmit", "receive", "intercept", "decode", "encrypt", "hack"
        ]
        
        self.adjectives = [
            "galactic", "imperial", "rebel", "dark", "light", "swift", "silent", 
            "rogue", "elite", "stealth", "tactical", "advanced", "ancient",
            "mysterious", "powerful", "legendary", "heroic", "cunning", "brave",
            "fierce", "noble", "shadowy", "crimson", "azure", "emerald",
            "chrome", "plasma", "quantum", "hyper", "ultra", "mega"
        ]
        
        self.adverbs = [
            "swiftly", "silently", "fiercely", "boldly", "cunningly", "stealthily",
            "rapidly", "precisely", "efficiently", "strategically", "tactically",
            "aggressively", "defensively", "mysteriously", "heroically", "nobly"
        ]
        
        self.symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "-", "_", "~"]
    
    def _get_random_word(self, word_type: str) -> str:
        """Get a random word from specified category."""
        word_lists = {
            "noun": self.nouns,
            "verb": self.verbs,
            "adjective": self.adjectives,
            "adverb": self.adverbs,
            "any": self.nouns + self.verbs + self.adjectives + self.adverbs
        }
        return random.choice(word_lists.get(word_type, word_lists["any"]))
    
    def _apply_grammar(self, word_count: int) -> List[str]:
        """Apply basic grammar rules to make the name more sentence-like."""
        if word_count == 1:
            return [self._get_random_word("noun")]
        elif word_count == 2:
            adj = self._get_random_word("adjective")
            noun = self._get_random_word("noun")
            return [adj, noun]
        elif word_count == 3:
            adj = self._get_random_word("adjective")
            noun = self._get_random_word("noun")
            verb = self._get_random_word("verb")
            past_verb = self._to_past_tense(verb)
            return [adj, noun, past_verb]
        elif word_count == 4:
            adverb = self._get_random_word("adverb")
            adj = self._get_random_word("adjective")
            noun = self._get_random_word("noun")
            verb = self._get_random_word("verb")
            past_verb = self._to_past_tense(verb)
            return [adverb, adj, noun, past_verb]
        else:  # 5 words
            adj = self._get_random_word("adjective")
            noun = self._get_random_word("noun")
            adverb = self._get_random_word("adverb")
            verb = self._get_random_word("verb")
            past_verb = self._to_past_tense(verb)
            return ["the", adj, noun, adverb, past_verb]
    
    def _to_past_tense(self, verb: str) -> str:
        """Convert a verb to past tense (simple rules)."""
        if verb.endswith("e"):
            return verb + "d"
        elif verb.endswith("y"):
            return verb[:-1] + "ied"
        else:
            return verb + "ed"
    
    def _generate_suffix(self, suffix_type: str) -> str:
        """Generate a random suffix based on type."""
        if suffix_type == "none":
            return ""
        elif suffix_type == "digits":
            return str(random.randint(100, 999))
        elif suffix_type == "hex":
            return format(random.randint(0, 4095), "03x")
        elif suffix_type == "symbol":
            return random.choice(self.symbols)
        elif suffix_type == "uuid":
            # Generate a short UUID-like string
            return "".join(random.choices(string.hexdigits[:16], k=6))
        else:
            return ""
    
    def generate_name(
        self, 
        word_count: int = None, 
        output_format: str = "kebab",
        suffix_type: str = "none"
    ) -> str:
        """
        Generate a Star Wars-themed name.
        
        Args:
            word_count: Number of words (1-5). If None, randomly chosen.
            output_format: Output format - 'kebab', 'snake', 'camel', 'pascal', 'space'
            suffix_type: Type of random suffix - 'none', 'digits', 'hex', 'symbol', 'uuid'
        
        Returns:
            Generated name string
        """
        if word_count is None:
            word_count = random.randint(1, 5)
        
        word_count = max(1, min(5, word_count))  # Clamp to 1-5 range
        
        # Generate words with grammar applied
        words = self._apply_grammar(word_count)
        
        # Generate suffix
        suffix = self._generate_suffix(suffix_type)
        
        return self._format_output(words, output_format, suffix)
    
    def _format_output(self, words: List[str], format_type: str, suffix: str) -> str:
        """Format the output according to the specified format."""
        if format_type == "kebab":
            base = "-".join(words).lower()
        elif format_type == "snake":
            base = "_".join(words).lower()
        elif format_type == "camel":
            base = words[0].lower()
            for word in words[1:]:
                base += word.capitalize()
        elif format_type == "pascal":
            base = "".join(word.capitalize() for word in words)
        elif format_type == "space":
            base = " ".join(words).title()
        else:
            base = "-".join(words).lower()
        
        if suffix:
            return f"{base}-{suffix}" if format_type != "space" else f"{base} {suffix}"
        return base


@click.command()
@click.option(
    "--count", "-c", 
    type=int, 
    help="Number of words in the name (1-5). If not specified, randomly chosen."
)
@click.option(
    "--format", "-f", "output_format",
    type=click.Choice(["kebab", "snake", "camel", "pascal", "space"]),
    default="kebab",
    help="Output format for the generated name."
)
@click.option(
    "--multiple", "-m",
    type=int,
    default=1,
    help="Generate multiple names at once."
)
@click.option(
    "--random", "-r", "suffix_type",
    type=click.Choice(["none", "digits", "hex", "symbol", "uuid"]),
    default="none",
    help="Type of random suffix to append (default: none)."
)
@click.option(
    "--seed", "-s",
    type=int,
    help="Random seed for reproducible results."
)
@click.version_option()
def main(count, output_format, multiple, suffix_type, seed):
    """
    Generate Star Wars-themed multi-word names for servers, instances, and other resources.
    
    Examples:
    
        starwars-namegen                               # Generate one random name
        
        starwars-namegen -c 3 -f snake                 # Generate 3-word name in snake_case
        
        starwars-namegen -m 5 --random digits          # Generate 5 names with digit suffixes
        
        starwars-namegen --seed 42                     # Generate reproducible name
    """
    if seed is not None:
        random.seed(seed)
    
    generator = StarWarsNameGenerator()
    
    for i in range(multiple):
        name = generator.generate_name(count, output_format, suffix_type)
        click.echo(name)


if __name__ == "__main__":
    main()
```

---

## Local Development & Testing

### Step 1: Install Development Dependencies

Navigate to your project directory and set up the development environment:

```bash
cd starwars-namegen
uv sync
```

This command:
- Creates a `.venv` virtual environment
- Installs all dependencies from `pyproject.toml`
- Creates a `uv.lock` file for reproducible environments

### Step 2: Run the CLI During Development

Test the CLI tool locally:

```bash
# Run with uv run
uv run starwars-namegen

# View help
uv run starwars-namegen --help

# Generate specific formats
uv run starwars-namegen -c 3 -f snake
uv run starwars-namegen -m 5 --random digits
```

### Step 3: Install the Package in Editable Mode (Optional)

For a more convenient development experience, install the package in editable mode:

```bash
uv pip install -e .
```

This allows you to run the command directly:

```bash
starwars-namegen -c 2
```

### Step 4: Set Up Git Repository

Initialize a Git repository for version control:

```bash
git init
git add .
git commit -m "Initial commit: Star Wars Name Generator"
```

Create a `.python-version` file to pin the Python version (optional but recommended):

```bash
echo "3.11" > .python-version
```

---

## Publishing to PyPI

### Step 1: Create PyPI Account

1. Go to https://pypi.org/account/register/
2. Create a new account or sign in if you already have one
3. Save your username and password securely

### Step 2: Create PyPI API Token (Recommended)

This is more secure than using your password:

1. Log in to PyPI: https://pypi.org/
2. Navigate to Account Settings → API tokens
3. Click "Add API token"
4. Name the token (e.g., "starwars-namegen")
5. Select scope: "Entire Account" (for your first package)
6. Click "Create token"
7. **Copy the token immediately** - you won't see it again!

The token format should look like: `pypi-AgEIcHlwaS5vcmc...`

### Step 3: Test on TestPyPI (Optional but Recommended)

Before publishing to the real PyPI, test on TestPyPI:

1. Register on TestPyPI: https://test.pypi.org/account/register/
2. Create an API token on TestPyPI
3. Build the distribution:

```bash
uv build
```

This creates a `dist/` directory with two files:
- `starwars_namegen-0.1.0-py3-none-any.whl` (wheel - binary distribution)
- `starwars_namegen-0.1.0.tar.gz` (source distribution)

4. Publish to TestPyPI:

```bash
uv publish --publish-url https://test.pypi.org/legacy/ --token pypi-YOUR_TEST_TOKEN_HERE
```

5. Verify on TestPyPI: https://test.pypi.org/project/starwars-namegen/

6. Test installation from TestPyPI:

```bash
uv tool install --from https://test.pypi.org/simple/ starwars-namegen
```

### Step 4: Publish to Production PyPI

Once you've verified everything works on TestPyPI, publish to the real PyPI:

```bash
uv publish --token pypi-YOUR_REAL_TOKEN_HERE
```

Or, if you prefer to use environment variables (more secure):

```bash
export UV_PUBLISH_TOKEN="pypi-YOUR_REAL_TOKEN_HERE"
uv publish
```

### Step 5: Verify Publication

Check that your package is on PyPI:

- PyPI page: https://pypi.org/project/starwars-namegen/
- Verify metadata and version number are correct

---

## Installation & Usage

### For End Users

#### Installation with uv (Recommended)

```bash
uv tool install starwars-namegen
```

This installs the tool globally and makes it available in any directory.

#### Installation with pip

```bash
pip install starwars-namegen
```

#### Installation with pipx (Alternative)

```bash
pipx install starwars-namegen
```

### CLI Usage Examples

```bash
# Basic usage - single random name with no suffix
starwars-namegen
# Output: galactic-trooper

# Generate 3-word name
starwars-namegen -c 3
# Output: swift-jedi-deployed

# Generate name in snake_case format
starwars-namegen -c 3 -f snake
# Output: dark_sith_infiltrated

# Generate name in PascalCase format
starwars-namegen -c 2 -f pascal
# Output: GalacticTrooper

# Generate with digit suffix
starwars-namegen --random digits
# Output: galactic-trooper-347

# Generate with hex suffix
starwars-namegen -c 3 --random hex
# Output: swift-jedi-deployed-a3f

# Generate with UUID suffix
starwars-namegen -c 2 --random uuid
# Output: rogue-falcon-b7f9d1

# Generate with symbol suffix
starwars-namegen --random symbol
# Output: galactic-trooper-$

# Generate 5 names at once
starwars-namegen -m 5 -f kebab
# Output multiple names:
# rogue-falcon-piloted
# imperial-destroyer-attacked
# silent-padawan-trained
# cunning-smuggler-negotiated
# elite-squadron-deployed

# Use seed for reproducible results
starwars-namegen --seed 42
# Always generates the same name with seed 42
```

### Real-World Use Cases

#### Docker Container Naming

```bash
# Generate a name for your container
docker run --name $(starwars-namegen --random digits) -d myimage:latest
```

#### Kubernetes Pod Naming

```bash
kubectl create deployment $(starwars-namegen) --image=myimage:latest
```

#### AWS EC2 Instance Tagging

```bash
aws ec2 run-instances \
  --image-id ami-0c55b159cbfafe1f0 \
  --count 1 \
  --instance-type t2.micro \
  --tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=$(starwars-namegen)}]"
```

#### Temporary Directory Creation

```bash
mkdir /tmp/$(starwars-namegen -c 3 -f snake)
```

---

## Advanced Usage

### Using in Python Scripts

You can also use the generator programmatically in your own Python projects:

```bash
# Install as a dependency in your project
uv add starwars-namegen
```

Then in your Python code:

```python
from starwars_namegen.cli import StarWarsNameGenerator

generator = StarWarsNameGenerator()

# Generate a single name
name = generator.generate_name(word_count=3, output_format="kebab", suffix_type="digits")
print(name)  # Example: dark-sith-infiltrated-842

# Generate multiple names
names = [generator.generate_name() for _ in range(5)]
for name in names:
    print(name)
```

### Integration with Other Tools

#### Shell Aliases

Add to your `.zshrc` or `.bashrc`:

```bash
# Create an alias for quick access
alias swname='starwars-namegen'

# With specific formatting
alias swname-snake='starwars-namegen -f snake'
alias swname-pascal='starwars-namegen -f pascal'
alias swname-rand='starwars-namegen --random digits'
```

Then use:

```bash
swname -c 3
swname-snake -m 5
```

#### Git Branch Naming

```bash
# Create a feature branch with a generated name
git checkout -b feature/$(starwars-namegen --random digits)
```

#### Terraform Naming

```hcl
# In your Terraform code
locals {
  random_suffix = var.use_random_suffix ? "-${data.external.random_name.result.output}" : ""
}

data "external" "random_name" {
  program = ["starwars-namegen", "--random", "hex"]
}
```

---

## Troubleshooting

### Issue: Command not found after installation

**Solution:**
The tool might not be in your PATH. Run:

```bash
uv tool update-shell
```

This updates your shell configuration to include the uv tool directory in PATH. Restart your terminal or source your shell config:

```bash
source ~/.zshrc  # For zsh
source ~/.bashrc # For bash
```

### Issue: Permission denied when running uv publish

**Solution:**
Make sure your PyPI token is correctly set and has the right permissions:

```bash
export UV_PUBLISH_TOKEN="pypi-YOUR_TOKEN"
uv publish
```

Or explicitly pass the token:

```bash
uv publish --token pypi-YOUR_TOKEN
```

### Issue: "Module not found" when running locally

**Solution:**
Ensure you're using `uv run` or have the package installed in editable mode:

```bash
uv sync
uv run starwars-namegen

# OR

uv pip install -e .
starwars-namegen
```

### Issue: Version conflict with dependencies

**Solution:**
Update your `uv.lock` file:

```bash
uv lock --upgrade
uv sync
```

### Issue: Building fails with "build-system" error

**Solution:**
Ensure your `pyproject.toml` has a valid `[build-system]` section:

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

### Issue: TestPyPI vs PyPI confusion

**Solution:**
Remember:
- **TestPyPI**: https://test.pypi.org/ (for testing)
- **Production PyPI**: https://pypi.org/ (for real releases)

When publishing to TestPyPI, use:

```bash
uv publish --publish-url https://test.pypi.org/legacy/ --token pypi-TEST_TOKEN
```

When publishing to production PyPI, use:

```bash
uv publish --token pypi-PROD_TOKEN
```

Or just use the default:

```bash
uv publish --token pypi-YOUR_TOKEN
```

### Issue: macOS-specific Path issues

**Solution:**
On macOS, ensure your shell is properly configured. If using zsh (default on modern macOS):

1. Check your `.zshrc`:

```bash
cat ~/.zshrc | grep -i uv
```

2. If uv is not in PATH, add it manually to `.zshrc`:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

3. Reload your shell:

```bash
source ~/.zshrc
exec zsh
```

### Issue: Python version compatibility

**Solution:**
Ensure your project's `requires-python` in `pyproject.toml` matches your environment:

```bash
# Check your Python version
python3 --version

# Update requires-python if needed
# In pyproject.toml:
requires-python = ">=3.9"

# Sync with uv
uv sync
```

---

## Updating Your Package

### Publishing a New Version

1. Update the version in `pyproject.toml`:

```toml
version = "0.2.0"
```

2. Update `__init__.py` to match:

```python
__version__ = "0.2.0"
```

3. Commit your changes:

```bash
git add .
git commit -m "Release version 0.2.0"
git tag v0.2.0
git push --tags
```

4. Build the new distribution:

```bash
uv build
```

5. Publish to PyPI:

```bash
uv publish --token pypi-YOUR_TOKEN
```

### Automating Releases with GitHub Actions (Optional)

Create `.github/workflows/publish.yml`:

```yaml
name: Publish to PyPI

on:
  push:
    tags:
      - "v*"

permissions:
  contents: read

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: release
    permissions:
      id-token: write
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v2
      - run: uv build
      - uses: pypa/gh-action-pypi-publish@release/v1
```

---

## Summary of Key Commands

### Development

```bash
# Set up environment
uv sync

# Run CLI
uv run starwars-namegen

# Install editable
uv pip install -e .

# View help
uv run starwars-namegen --help
```

### Building & Publishing

```bash
# Build distributions
uv build

# Test on TestPyPI
uv publish --publish-url https://test.pypi.org/legacy/ --token pypi-TOKEN

# Publish to PyPI
uv publish --token pypi-TOKEN

# Install globally
uv tool install starwars-namegen
```

### Updating

```bash
# Update the tool
uv tool upgrade starwars-namegen

# Remove the tool
uv tool uninstall starwars-namegen
```

---

## Final Notes

- **Security**: Never commit PyPI tokens to version control. Use environment variables or GitHub secrets.
- **Documentation**: Keep your README.md updated with examples and use cases.
- **Testing**: Consider adding pytest for unit tests as your project grows.
- **CI/CD**: Set up GitHub Actions for automated testing and publishing.
- **Versioning**: Use semantic versioning (major.minor.patch) for your releases.
- **Maintenance**: Monitor GitHub issues and PyPI for user feedback and update accordingly.

Congratulations! You now have a professional, published Python CLI tool available for the world to use via `uv`!