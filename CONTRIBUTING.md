# Contributing to Star Wars Name Generator

**IMPERIAL ENGINEERING CORPS - CONTRIBUTION PROTOCOLS**

We welcome contributions from tactical engineers across the galaxy. This document outlines the operational procedures for contributing to the Star Wars Name Generator weapon platform.

## Development Environment Setup

### Prerequisites
- Python 3.9 or higher
- uv package manager (`curl -LsSf https://astral.sh/uv/install.sh | sh`)
- Git

### Clone and Setup
```bash
# Clone the imperial archives
git clone https://github.com/anthropics/starwars-namegen.git
cd starwars-namegen

# Initialize tactical environment
uv sync

# Verify systems operational
uv run starwars-namegen --help
```

## Development Workflow

### 1. Create Feature Branch
```bash
git checkout -b feature/your-feature-name
```

### 2. Make Changes
- Edit code in `src/starwars_namegen/`
- Update tests if applicable
- Update documentation if needed

### 3. Test Locally
```bash
# Run the tool
uv run starwars-namegen -c 3 -f snake

# Test all formats
uv run starwars-namegen -c 2 -f kebab
uv run starwars-namegen -c 2 -f snake
uv run starwars-namegen -c 2 -f camel
uv run starwars-namegen -c 2 -f pascal
uv run starwars-namegen -c 2 -f space

# Test suffix types
uv run starwars-namegen --random digits
uv run starwars-namegen --random hex
uv run starwars-namegen --random symbol
uv run starwars-namegen --random uuid
```

### 4. Build and Verify
```bash
# Build distribution packages
uv build

# Test wheel installation
uv tool install dist/starwars_namegen-*.whl --force
starwars-namegen --version
```

### 5. Commit Changes
```bash
git add .
git commit -m "feat: Add your feature description"
```

## Code Style

- Follow PEP 8 guidelines
- Use type hints for all functions
- Add docstrings to all public methods
- Keep the "Death Star" theme in documentation

## Commit Message Convention

Follow conventional commits format:

```
feat: Add new feature
fix: Bug fix
docs: Documentation update
refactor: Code refactoring
test: Add tests
chore: Maintenance tasks
```

## Pull Request Process

1. Push your branch to GitHub
2. Create a pull request with clear description
3. Ensure all checks pass
4. Wait for review from maintainers

## Adding New Features

### Adding Vocabulary
Edit `src/starwars_namegen/cli.py`:
```python
self.nouns = [
    # Add your Star Wars nouns here
]
```

### Adding New Output Formats
Add format handling in `_format_output` method.

### Adding New Suffix Types
Add suffix logic in `_generate_suffix` method.

## Questions?

Open an issue on GitHub for questions or discussions.

---

**May the Force guide your contributions!**
