# Contributing to Star Wars Name Generator

Thank you for your interest in contributing to this project! This is a demonstration tool showcasing professional Python packaging with `uv`, but we welcome improvements and enhancements.

## Development Setup

### Prerequisites

- Python 3.9 or higher
- `uv` package manager ([installation guide](https://docs.astral.sh/uv/))
- Git

### Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/anthropics/claude-code.git
   cd star-wars-name-generator-uvx
   ```

2. **Install dependencies:**
   ```bash
   uv sync
   ```

3. **Run the tool locally:**
   ```bash
   uv run starwars-namegen
   ```

## Development Workflow

### Making Changes

1. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes to the code

3. Test your changes:
   ```bash
   # Run the CLI
   uv run starwars-namegen --help

   # Test specific functionality
   uv run starwars-namegen -c 3 -f snake
   ```

4. Build and test the package:
   ```bash
   # Build distribution
   uv build

   # Install locally
   uv tool install dist/starwars_namegen-*.whl

   # Test installed version
   starwars-namegen
   ```

### Code Style

- Follow PEP 8 guidelines
- Use type hints for all function parameters and return values
- Add docstrings to all public functions and classes
- Keep lines under 100 characters when possible
- Use meaningful variable and function names

### Adding New Features

If you're adding a new feature, please:

1. Update the documentation in README.md
2. Add examples to the examples/ directory if applicable
3. Update CHANGELOG.md with your changes
4. Ensure the feature works with all output formats
5. Test with different Python versions if possible (3.9, 3.10, 3.11, 3.12, 3.13)

### Common Enhancement Areas

- **Vocabulary expansion:** Add more Star Wars themed words
- **New formats:** Additional output format styles
- **New themes:** Non-Star Wars vocabularies (Marvel, LOTR, etc.)
- **Grammar improvements:** More sophisticated sentence patterns
- **Performance:** Optimization for large batch generations
- **Testing:** Add automated tests

## Submitting Changes

1. **Commit your changes:**
   ```bash
   git add .
   git commit -m "feat: add awesome new feature"
   ```

2. **Push to your fork:**
   ```bash
   git push origin feature/your-feature-name
   ```

3. **Create a Pull Request:**
   - Go to the repository on GitHub
   - Click "New Pull Request"
   - Select your branch
   - Describe your changes
   - Submit the PR

## Pull Request Guidelines

- **Title:** Use a clear, descriptive title
- **Description:** Explain what your changes do and why
- **Testing:** Describe how you tested your changes
- **Documentation:** Update relevant documentation
- **Changelog:** Add entry to CHANGELOG.md under [Unreleased]

## Commit Message Convention

We follow Conventional Commits:

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes (formatting, etc.)
- `refactor:` Code refactoring
- `test:` Adding or updating tests
- `chore:` Maintenance tasks

Examples:
```
feat: add Marvel theme vocabulary
fix: correct past tense conversion for irregular verbs
docs: update README with new examples
```

## Reporting Issues

Found a bug or have a feature request?

1. Check if the issue already exists
2. Create a new issue with:
   - Clear title
   - Detailed description
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior
   - Environment details (OS, Python version, uv version)

## Questions?

Feel free to open an issue for questions or discussion!

## Code of Conduct

- Be respectful and constructive
- Help others learn
- Keep discussions on topic
- Report inappropriate behavior

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing! May the Force be with you.
