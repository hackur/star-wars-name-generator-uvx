# Implementation Guide: Star Wars Name Generator

**Version:** 0.1.0
**Phase:** Development
**Last Updated:** 2025-10-28

---

## Table of Contents

1. [Pre-Implementation Checklist](#pre-implementation-checklist)
2. [Phase 1: Project Foundation](#phase-1-project-foundation)
3. [Phase 2: Core Implementation](#phase-2-core-implementation)
4. [Phase 3: Documentation](#phase-3-documentation)
5. [Implementation Best Practices](#implementation-best-practices)

---

## Pre-Implementation Checklist

### Environment Setup

- [ ] `uv` installed and accessible
```bash
uv --version
# Expected: uv 0.x.x or higher
```

- [ ] Python 3.9+ available
```bash
python3 --version
# Expected: Python 3.9.x or higher
```

- [ ] Working directory prepared
```bash
pwd
# Should be in: /Users/sarda/Downloads/star-wars-name-generator-uvx
```

---

## Phase 1: Project Foundation

### Task 1: Create Directory Structure

```bash
# Create source directory
mkdir -p src/starwars_namegen

# Create examples directory
mkdir -p examples

# Verify structure
tree -L 2
```

**Expected Output:**
```
.
├── plans/
├── src/
│   └── starwars_namegen/
└── examples/
```

### Task 2: Create pyproject.toml

**File:** `/Users/sarda/Downloads/star-wars-name-generator-uvx/pyproject.toml`

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

**Key Points:**
- `[project.scripts]` defines the CLI entry point
- `hatchling` as build backend (fast, modern)
- `src/` layout for proper packaging
- Dependencies: click (CLI), inflect (grammar)

### Task 3: Create .gitignore

**File:** `/Users/sarda/Downloads/star-wars-name-generator-uvx/.gitignore`

```gitignore
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

### Task 4: Create LICENSE

**File:** `/Users/sarda/Downloads/star-wars-name-generator-uvx/LICENSE`

```
MIT License

Copyright (c) 2025 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

**Note:** Update [Your Name] with actual name.

### Task 5: Create README.md

(See separate section for full README content)

---

## Phase 2: Core Implementation

### Task 6: Create __init__.py

**File:** `/Users/sarda/Downloads/star-wars-name-generator-uvx/src/starwars_namegen/__init__.py`

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

**Purpose:**
- Package metadata
- Version information
- Public API exports

### Task 7: Create cli.py - Part 1 (Imports & Class)

**File:** `/Users/sarda/Downloads/star-wars-name-generator-uvx/src/starwars_namegen/cli.py`

**Section 1: Imports**
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
```

**Section 2: Class Definition & Init**
```python
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
```

### Task 8: Implement Helper Methods

```python
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

    def _to_past_tense(self, verb: str) -> str:
        """Convert a verb to past tense (simple rules)."""
        if verb.endswith("e"):
            return verb + "d"
        elif verb.endswith("y"):
            return verb[:-1] + "ied"
        else:
            return verb + "ed"
```

### Task 9: Implement Grammar Engine

```python
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
```

### Task 10: Implement Suffix Generator

```python
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
```

### Task 11: Implement Format Engine

```python
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
```

### Task 12: Implement Main Generator Method

```python
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
```

### Task 13: Implement CLI Interface

```python
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

## Phase 3: Documentation

### Task 14: Create Comprehensive README.md

(See plans/03-documentation-guide.md for full content)

### Task 15: Create CONTRIBUTING.md

Brief guide for contributors on:
- Code style
- Pull request process
- Issue reporting
- Development setup

### Task 16: Create CHANGELOG.md

```markdown
# Changelog

All notable changes to this project will be documented in this file.

## [0.1.0] - 2025-10-28

### Added
- Initial release
- Multi-word name generation (1-5 words)
- Grammar rules for sentence-like names
- Five output formats: kebab, snake, camel, pascal, space
- Five suffix types: none, digits, hex, symbol, uuid
- Seed support for reproducibility
- Multiple name generation
- Click-based CLI interface
- Comprehensive documentation
```

### Task 17: Create Example Scripts

**examples/basic_usage.sh**
```bash
#!/bin/bash
# Basic usage examples

echo "=== Basic Name Generation ==="
starwars-namegen

echo -e "\n=== 3-word Snake Case ==="
starwars-namegen -c 3 -f snake

echo -e "\n=== 5 Names with Digits ==="
starwars-namegen -m 5 --random digits

echo -e "\n=== Reproducible (seed=42) ==="
starwars-namegen --seed 42
```

**examples/python_usage.py**
```python
#!/usr/bin/env python3
"""Example of using starwars-namegen programmatically."""

from starwars_namegen.cli import StarWarsNameGenerator

def main():
    generator = StarWarsNameGenerator()

    # Generate different formats
    print("Kebab:", generator.generate_name(3, "kebab"))
    print("Snake:", generator.generate_name(3, "snake"))
    print("Camel:", generator.generate_name(3, "camel"))
    print("Pascal:", generator.generate_name(3, "pascal"))

    # Generate with suffixes
    print("\nWith digits:", generator.generate_name(2, "kebab", "digits"))
    print("With hex:", generator.generate_name(2, "kebab", "hex"))
    print("With UUID:", generator.generate_name(2, "kebab", "uuid"))

if __name__ == "__main__":
    main()
```

---

## Implementation Best Practices

### Code Quality

1. **Type Hints:**
```python
def generate_name(
    self,
    word_count: int = None,  # Type hints for all parameters
    output_format: str = "kebab",
    suffix_type: str = "none"
) -> str:  # Return type hint
```

2. **Docstrings:**
```python
"""
Generate a Star Wars-themed name.

Args:
    word_count: Number of words (1-5). If None, randomly chosen.
    output_format: Output format - 'kebab', 'snake', 'camel', 'pascal', 'space'
    suffix_type: Type of random suffix - 'none', 'digits', 'hex', 'symbol', 'uuid'

Returns:
    Generated name string
"""
```

3. **Error Handling:**
```python
# Clamp word count to valid range
word_count = max(1, min(5, word_count))
```

4. **Consistent Style:**
- Use 4 spaces for indentation
- Follow PEP 8 naming conventions
- Keep lines under 100 characters when possible
- Use meaningful variable names

### Testing During Development

After each major component:
```bash
# Run the CLI
uv run starwars-namegen

# Test specific options
uv run starwars-namegen -c 3 -f snake
uv run starwars-namegen --help
```

### Git Workflow

```bash
# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "feat: initial implementation of Star Wars name generator"
```

---

**Document Version:** 1.0
**Status:** Ready for Implementation
**Next:** Begin Task 1 of Phase 1
