# MISSION BRIEFINGS: Real-World UV Patterns

> *"In my experience, there's no such thing as luck."* - Obi-Wan Kenobi
>
> Success comes from following proven patterns. Here are your mission briefings.

**Classification**: Tactical Operations Manual
**Clearance Level**: Rebel Alliance Command
**Author**: Admiral Ackbar's Strategic Command

---

## Table of Contents

1. [Mission Alpha: Docker Integration](#mission-alpha-docker-integration)
2. [Mission Beta: CI/CD Deployment](#mission-beta-cicd-deployment)
3. [Mission Gamma: Multi-Tool Project](#mission-gamma-multi-tool-project)
4. [Mission Delta: Private Package Registry](#mission-delta-private-package-registry)
5. [Mission Epsilon: Cross-Platform Distribution](#mission-epsilon-cross-platform-distribution)

---

## Mission Alpha: Docker Integration

**Objective**: Deploy your UV tool in containerized environments

### The Rebellion's Docker Strategy

```dockerfile
# Dockerfile - Multi-stage build for optimal performance
FROM python:3.13-slim AS builder

# Install UV
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Set working directory
WORKDIR /app

# Copy project files
COPY pyproject.toml uv.lock ./
COPY src ./src

# Install dependencies and build
RUN uv sync --frozen --no-dev
RUN uv build

# Runtime stage (smaller image)
FROM python:3.13-slim

# Install UV for runtime
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Copy built package
COPY --from=builder /app/dist/*.whl /tmp/

# Install the package globally
RUN uv tool install /tmp/*.whl

# Set entry point
ENTRYPOINT ["starwars-namegen"]
CMD ["--help"]
```

### Usage

```bash
# Build
docker build -t starwars-namegen:latest .

# Run
docker run --rm starwars-namegen:latest -c 5 -m 10

# With volume for output
docker run --rm -v $(pwd)/output:/output starwars-namegen:latest -c 5 -m 1000 > /output/names.txt
```

### Docker Compose for Development

```yaml
# docker-compose.yml
services:
  dev:
    build:
      context: .
      target: builder
    volumes:
      - .:/app
      - uv-cache:/root/.cache/uv
    command: uv run pytest

  tool:
    build: .
    command: ["--help"]

volumes:
  uv-cache:
```

---

## Mission Beta: CI/CD Deployment

**Objective**: Automated testing and deployment pipeline

### GitHub Actions: The Rebellion's Pipeline

```yaml
# .github/workflows/main.yml
name: Death Star Construction Pipeline

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  release:
    types: [created]

jobs:
  # Phase 1: Quality Checks
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v5

      - name: Install UV
        uses: astral-sh/setup-uv@v7

      - name: Lint
        run: uv run ruff check .

      - name: Type Check
        run: uv run mypy src

  # Phase 2: Multi-Platform Testing
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
        python-version: ['3.9', '3.10', '3.11', '3.12', '3.13']

    steps:
      - uses: actions/checkout@v5

      - name: Install UV
        uses: astral-sh/setup-uv@v7
        with:
          enable-cache: true

      - name: Set Python version
        run: uv python install ${{ matrix.python-version }}

      - name: Install dependencies
        run: uv sync --all-extras

      - name: Run tests
        run: uv run pytest --cov --cov-report=xml

      - name: Upload coverage
        uses: codecov/codecov-action@v4
        with:
          file: ./coverage.xml

  # Phase 3: Build Verification
  build:
    needs: [quality, test]
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v5

      - name: Install UV
        uses: astral-sh/setup-uv@v7

      - name: Build package
        run: uv build

      - name: Verify package
        run: |
          uv pip install dist/*.whl
          starwars-namegen --version

      - name: Upload artifacts
        uses: actions/upload-artifact@v4
        with:
          name: dist
          path: dist/

  # Phase 4: Publish (on release only)
  publish:
    if: github.event_name == 'release'
    needs: [quality, test, build]
    runs-on: ubuntu-latest
    environment:
      name: pypi
    permissions:
      id-token: write

    steps:
      - uses: actions/checkout@v5

      - name: Install UV
        uses: astral-sh/setup-uv@v7

      - name: Build
        run: uv build

      - name: Publish to PyPI
        run: uv publish
```

### GitLab CI: Imperial Forces Pipeline

```yaml
# .gitlab-ci.yml
variables:
  UV_CACHE_DIR: "$CI_PROJECT_DIR/.cache/uv"

cache:
  paths:
    - .cache/uv

stages:
  - quality
  - test
  - build
  - deploy

before_script:
  - curl -LsSf https://astral.sh/uv/install.sh | sh
  - export PATH="$HOME/.cargo/bin:$PATH"

# Quality Phase
lint:
  stage: quality
  script:
    - uv run ruff check .

typecheck:
  stage: quality
  script:
    - uv run mypy src

# Test Phase
test:
  stage: test
  parallel:
    matrix:
      - PYTHON_VERSION: ["3.9", "3.10", "3.11", "3.12", "3.13"]
  script:
    - uv python install $PYTHON_VERSION
    - uv sync --all-extras
    - uv run pytest --cov --cov-report=xml
  coverage: '/(?i)total.*? (100(?:\.0+)?\%|[1-9]?\d(?:\.\d+)?\%)$/'
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage.xml

# Build Phase
build:
  stage: build
  script:
    - uv build
  artifacts:
    paths:
      - dist/

# Deploy Phase
deploy:
  stage: deploy
  only:
    - tags
  script:
    - uv publish
  environment:
    name: production
```

---

## Mission Gamma: Multi-Tool Project

**Objective**: Manage multiple CLI tools in one repository

### Monorepo Structure

```
rebel-tools/
├── packages/
│   ├── name-generator/
│   │   ├── src/
│   │   ├── tests/
│   │   └── pyproject.toml
│   ├── config-manager/
│   │   ├── src/
│   │   ├── tests/
│   │   └── pyproject.toml
│   └── deployment-tool/
│       ├── src/
│       ├── tests/
│       └── pyproject.toml
├── shared/
│   └── rebel-common/
│       ├── src/
│       └── pyproject.toml
└── pyproject.toml  # Workspace root
```

### Workspace Configuration

```toml
# pyproject.toml (root)
[tool.uv.workspace]
members = [
    "packages/*",
    "shared/*",
]

[tool.uv]
managed = true
```

### Individual Package Setup

```toml
# packages/name-generator/pyproject.toml
[project]
name = "rebel-name-generator"
version = "0.1.0"
dependencies = [
    "click>=8.1.0",
    "rebel-common",  # Shared workspace dependency
]

[project.scripts]
rebel-gen = "rebel_name_generator.cli:main"
```

### Workspace Commands

```bash
# Install all workspace packages
uv sync

# Run specific package
uv run --package rebel-name-generator pytest

# Build all packages
for pkg in packages/*; do
    (cd "$pkg" && uv build)
done

# Add dependency to specific package
uv add --package rebel-name-generator rich
```

---

## Mission Delta: Private Package Registry

**Objective**: Use UV with private PyPI repositories

### Configuration

```toml
# pyproject.toml
[tool.uv]
index-url = "https://pypi.org/simple"
extra-index-url = [
    "https://artifacts.example.com/pypi/simple",
]

[tool.uv.sources]
# Override specific package source
secret-weapon = { index = "private-registry" }

[[tool.uv.index]]
name = "private-registry"
url = "https://artifacts.example.com/pypi/simple"
```

### Authentication

```bash
# Set credentials via environment
export UV_INDEX_SECRET_WEAPON_USERNAME="rebel-alliance"
export UV_INDEX_SECRET_WEAPON_PASSWORD="use-the-force"

# Or use .netrc
cat > ~/.netrc << EOF
machine artifacts.example.com
login rebel-alliance
password use-the-force
EOF

chmod 600 ~/.netrc
```

### Using in CI/CD

```yaml
# GitHub Actions
- name: Configure private registry
  run: |
    mkdir -p ~/.config/uv
    cat > ~/.config/uv/pip.conf << EOF
    [global]
    extra-index-url = https://${{ secrets.REGISTRY_USER }}:${{ secrets.REGISTRY_PASS }}@artifacts.example.com/pypi/simple
    EOF

- name: Install dependencies
  run: uv sync
```

---

## Mission Epsilon: Cross-Platform Distribution

**Objective**: Build and distribute for multiple platforms

### Universal Wheel Building

```bash
# Build universal wheel (pure Python)
uv build

# Verify wheel is universal
unzip -l dist/*.whl | grep WHEEL
# Should show: Tag: py3-none-any
```

### Platform-Specific Dependencies

```toml
# pyproject.toml
[project]
dependencies = [
    "click>=8.1.0",
    "colorama>=0.4.0; platform_system=='Windows'",
    "pyobjc-framework-Cocoa; platform_system=='Darwin'",
]
```

### Building for Multiple Platforms (GitHub Actions)

```yaml
name: Build Multi-Platform

on: [push]

jobs:
  build:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]

    steps:
      - uses: actions/checkout@v5

      - name: Install UV
        uses: astral-sh/setup-uv@v7

      - name: Build
        run: uv build

      - name: Test built package
        run: |
          uv tool install dist/*.whl
          starwars-namegen --version

      - name: Upload artifacts
        uses: actions/upload-artifact@v4
        with:
          name: dist-${{ matrix.os }}
          path: dist/
```

---

## Bonus Mission: Performance Optimization

### Fast Docker Builds with Layer Caching

```dockerfile
FROM python:3.13-slim

# Layer 1: Install UV (cached unless UV version changes)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Layer 2: Install dependencies (cached unless lock file changes)
WORKDIR /app
COPY uv.lock pyproject.toml ./
RUN uv sync --frozen --no-install-project

# Layer 3: Copy source and install project
COPY . .
RUN uv sync --frozen

ENTRYPOINT ["uv", "run", "starwars-namegen"]
```

### CI Cache Strategy

```yaml
- name: Cache UV dependencies
  uses: actions/cache@v4
  with:
    path: |
      ~/.cache/uv
      .venv
    key: ${{ runner.os }}-uv-${{ hashFiles('uv.lock') }}
    restore-keys: |
      ${{ runner.os }}-uv-

- name: Install dependencies
  run: uv sync
```

---

## Quick Reference: Common Patterns

### Pattern: Global Tools vs Project Dependencies

```bash
# Project dependency (added to pyproject.toml)
uv add requests

# Development tool (testing only)
uv add --group dev pytest

# Global tool (available everywhere)
uv tool install black

# One-off execution (no installation)
uvx ruff check .
```

### Pattern: Version Pinning Strategy

```toml
# Libraries: Minimal constraints (flexible)
[project]
dependencies = [
    "click>=8.0",  # Allow any 8.x version
]

# Applications: Lock file provides reproducibility
# Use ranges, let uv.lock handle exact versions

# Security updates
uv lock --upgrade-package urllib3
```

### Pattern: Testing Matrix

```bash
# Test all Python versions
for ver in 3.9 3.10 3.11 3.12 3.13; do
    uv run --python $ver pytest
done

# Test minimum and maximum versions
uv run --python 3.9 --resolution lowest pytest  # Test lower bounds
uv run --python 3.13 --resolution highest pytest  # Test latest
```

---

## Mission Complete: Deploy Checklist

Before deploying your UV tool to production:

- [ ] All tests pass across Python 3.9-3.13
- [ ] Code passes `ruff check` and `mypy`
- [ ] Coverage is above 80%
- [ ] README has clear usage examples
- [ ] LICENSE file is included
- [ ] CHANGELOG is updated
- [ ] Version is bumped appropriately
- [ ] `uv.lock` is committed
- [ ] CI/CD pipeline is green
- [ ] Built package tested with `uvx`
- [ ] Documentation is complete

---

**Mission Status**: OPERATIONAL

**Commander's Note**: These patterns have been battle-tested across the galaxy. Use them wisely, and may the Force be with your deployments!

*Document Version*: 1.0
*Rebel Alliance Stamp*: ⚔️ APPROVED ⚔️
