# Star Wars Name Generator

**Mission Status:** Fully Operational
**Deployment Vector:** uvx-compatible Python CLI tool
**Strategic Purpose:** Generate unique Star Wars-themed designations for infrastructure resources

---

## Overview

A command-line weapon system that generates grammatically coherent, Star Wars-themed multi-word names for servers, containers, instances, and any infrastructure requiring unique identifiers. Built to demonstrate professional `uv`-based Python packaging and instant-deployment capabilities.

### Why This Tool Exists

- **Instant Deployment:** Run via `uvx` without installation
- **Professional Packaging:** Demonstrates modern Python project structure
- **Universal Compatibility:** Works with all major package managers (uv, pip, pipx)
- **Educational Purpose:** Shows complete lifecycle from dev to PyPI

## Features

- ⚡ **Grammar Engine:** Generates sentence-like names with proper word patterns
- 🎯 **Multiple Formats:** kebab-case, snake_case, camelCase, PascalCase, space-separated
- 🎲 **Random Suffixes:** digits, hex, symbols, UUID-like strings
- 🔄 **Reproducible:** Seed support for consistent name generation
- 📦 **Batch Generation:** Create multiple names in one command
- 🚀 **Zero Config:** Works immediately via uvx

## Quick Start

### Using uvx (Recommended - Zero Installation)

```bash
# Single command execution - no installation needed!
uvx starwars-namegen

# Generate with specific options
uvx starwars-namegen -c 3 -f snake --random digits
```

### Using uv tool (Persistent Installation)

```bash
# Install globally
uv tool install starwars-namegen

# Use the command
starwars-namegen -c 3 -f kebab
```

### Using pip (Traditional Method)

```bash
pip install starwars-namegen
starwars-namegen --help
```

## Usage Examples

### Basic Generation

```bash
# Random name (default: kebab-case)
$ starwars-namegen
galactic-trooper

# Specific word count (1-5)
$ starwars-namegen -c 3
swift-jedi-deployed

# Different format
$ starwars-namegen -c 3 -f snake
dark_sith_infiltrated
```

### Output Formats

```bash
# kebab-case (default) - URL-safe, git branches
$ starwars-namegen -c 2
rogue-falcon

# snake_case - Python variables, filenames
$ starwars-namegen -c 2 -f snake
rogue_falcon

# camelCase - JavaScript variables
$ starwars-namegen -c 2 -f camel
rogueFalcon

# PascalCase - Class names, components
$ starwars-namegen -c 2 -f pascal
RogueFalcon

# space - Human-readable display
$ starwars-namegen -c 2 -f space
Rogue Falcon
```

### Random Suffixes for Uniqueness

```bash
# 3-digit number (100-999)
$ starwars-namegen --random digits
galactic-trooper-347

# 3-character hex (000-fff)
$ starwars-namegen --random hex
galactic-trooper-a3f

# Special symbol
$ starwars-namegen --random symbol
galactic-trooper-$

# 6-character UUID-like
$ starwars-namegen --random uuid
galactic-trooper-b7f9d1
```

### Batch Generation

```bash
# Generate 5 names at once
$ starwars-namegen -m 5
imperial-destroyer
swift-jedi
dark-sith-escaped
galactic-fleet-deployed
rogue-squadron-attacked
```

### Reproducible Results

```bash
# Use seed for consistent output
$ starwars-namegen --seed 42
# Always generates the same name with seed 42

# Useful for testing and coordination
$ starwars-namegen --seed 12345 -c 3
```

## Real-World Use Cases

### Docker Container Naming

```bash
# Generate unique container name
docker run -d --name $(starwars-namegen --random digits) nginx:latest
```

### Kubernetes Resources

```bash
# Create deployment with generated name
kubectl create deployment $(starwars-namegen -c 2) --image=myapp:latest
```

### AWS Resource Tags

```bash
# Name EC2 instance
aws ec2 run-instances \
  --image-id ami-12345 \
  --tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=$(starwars-namegen)}]"
```

### File and Directory Creation

```bash
# Create unique temporary directory
mkdir /tmp/$(starwars-namegen -c 3 -f snake)

# Create log file with timestamp concept
touch $(starwars-namegen --random digits).log
```

### Git Branch Naming

```bash
# Create feature branch
git checkout -b feature/$(starwars-namegen -c 2 --random hex)
```

### Python/JavaScript Variable Names

```python
# Generate camelCase variable name
var_name = $(starwars-namegen -c 2 -f camel)
```

## CLI Options Reference

| Option | Short | Type | Default | Description |
|--------|-------|------|---------|-------------|
| `--count` | `-c` | int | random(1-5) | Number of words in name (1-5) |
| `--format` | `-f` | choice | kebab | Output format: kebab, snake, camel, pascal, space |
| `--multiple` | `-m` | int | 1 | Generate N names |
| `--random` | `-r` | choice | none | Suffix type: none, digits, hex, symbol, uuid |
| `--seed` | `-s` | int | None | Random seed for reproducibility |
| `--version` | | flag | | Show version number |
| `--help` | | flag | | Show help message |

## Grammar Patterns

The tool uses linguistically sound patterns:

| Words | Pattern | Example |
|-------|---------|---------|
| 1 | `[NOUN]` | `jedi` |
| 2 | `[ADJ] [NOUN]` | `galactic trooper` |
| 3 | `[ADJ] [NOUN] [VERB_PAST]` | `swift jedi deployed` |
| 4 | `[ADV] [ADJ] [NOUN] [VERB_PAST]` | `stealthily dark sith infiltrated` |
| 5 | `"the" [ADJ] [NOUN] [ADV] [VERB_PAST]` | `the crimson falcon swiftly escaped` |

## Development

### Prerequisites

- Python 3.9+
- uv package manager

### Local Setup

```bash
# Clone repository
git clone https://github.com/yourusername/starwars-namegen.git
cd starwars-namegen

# Install dependencies
uv sync

# Run locally
uv run starwars-namegen
```

### Project Structure

```
starwars-namegen/
├── src/
│   └── starwars_namegen/
│       ├── __init__.py      # Package metadata
│       └── cli.py            # Core implementation
├── plans/                     # Detailed planning docs
├── examples/                  # Usage examples
├── pyproject.toml            # Build configuration
├── README.md                  # This file
└── LICENSE                    # MIT License
```

### Building

```bash
# Build distribution packages
uv build

# Output: dist/starwars_namegen-0.1.0-py3-none-any.whl
#         dist/starwars_namegen-0.1.0.tar.gz
```

### Testing Locally

```bash
# Install in development mode
uv pip install -e .

# Or install from wheel
uv tool install dist/starwars_namegen-0.1.0-py3-none-any.whl

# Test uvx execution
uvx --from . starwars-namegen
```

## Programmatic Usage

```python
from starwars_namegen.cli import StarWarsNameGenerator

# Initialize generator
generator = StarWarsNameGenerator()

# Generate names
name1 = generator.generate_name(word_count=3, output_format="kebab", suffix_type="digits")
print(name1)  # dark-sith-infiltrated-842

name2 = generator.generate_name(word_count=2, output_format="camel", suffix_type="none")
print(name2)  # galacticTrooper

# Batch generation
names = [generator.generate_name() for _ in range(10)]
```

## Why This Demonstrates Excellent uv Usage

This project showcases professional Python packaging with uv:

1. **Modern pyproject.toml:** PEP 621 compliant configuration
2. **src-layout:** Proper package structure avoiding import pitfalls
3. **hatchling build backend:** Fast, modern build system
4. **Managed dependencies:** uv handles everything automatically
5. **uvx compatibility:** Zero-friction deployment to end users
6. **Tool isolation:** Each execution in clean environment
7. **Cross-platform:** Pure Python wheel works everywhere

## Technical Details

- **Dependencies:** click (CLI framework), inflect (grammar engine)
- **Build System:** hatchling
- **Package Manager:** uv
- **Python Support:** 3.9, 3.10, 3.11, 3.12, 3.13
- **License:** MIT
- **Package Size:** ~15KB (wheel)
- **Execution Time:** <500ms cold start, <10ms name generation

## Contributing

Contributions welcome! This is a demonstration project, but improvements are appreciated:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Acknowledgments

Built with:
- [uv](https://docs.astral.sh/uv/) - Universal Python package manager
- [Click](https://click.palletsprojects.com/) - CLI framework
- [inflect](https://inflect.readthedocs.io/) - Grammar engine

---

**May the Force be with your infrastructure naming.**

For detailed planning documents, see the `plans/` directory.
