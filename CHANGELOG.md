# Changelog

All notable changes to the Star Wars Name Generator will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2025-10-28

### Added
- Initial release of Star Wars Name Generator
- Multi-word name generation (1-5 words) with grammatically coherent patterns
- Grammar rules: noun, adjective+noun, adjective+noun+verb, etc.
- Five output formats: kebab-case, snake_case, camelCase, PascalCase, space-separated
- Five suffix types: none, digits (3-digit), hex (3-char), symbol, uuid (6-char)
- Reproducibility via `--seed` option
- Batch generation via `--multiple` option
- Click-based CLI with comprehensive help
- Full vocabulary database:
  - 43 Star Wars nouns
  - 32 Star Wars verbs
  - 31 Star Wars adjectives
  - 16 Star Wars adverbs
- Type hints throughout codebase
- Comprehensive documentation
- Example scripts for common use cases
- uv-compatible package structure
- uvx instant-execution support
- MIT License

### Technical Details
- Python 3.9+ support
- Dependencies: click>=8.0.0, inflect>=7.0.0
- Build system: hatchling
- Package manager: uv
- Distribution: PyPI-ready wheel and sdist

### Documentation
- Comprehensive README with usage examples
- Detailed planning documents in `plans/` directory
- Example scripts in `examples/` directory
- Inline code documentation with docstrings

## [Unreleased]

### Planned Features
- Custom vocabulary support
- Alternative themes (Marvel, LOTR, etc.)
- Configuration file support
- JSON output mode
- Web interface
- Plugin system

---

**Full Changelog:** https://github.com/anthropics/claude-code/commits/main
