# ⭐ Star Wars Name Generator

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Package Manager](https://img.shields.io/badge/uv-compatible-green.svg)](https://docs.astral.sh/uv/)
[![Status](https://img.shields.io/badge/status-operational-brightgreen.svg)](https://github.com/anthropics/starwars-namegen)
[![Built with Click](https://img.shields.io/badge/CLI-Click-blue.svg)](https://click.palletsprojects.com/)
[![Code Style](https://img.shields.io/badge/code%20style-PEP%208-orange.svg)](https://peps.python.org/pep-0008/)

> **DEATH STAR OPERATIONAL PROTOCOL**: A precision tactical weapon system for generating Star Wars-themed nomenclature across all Imperial infrastructure deployments.

A professional CLI tool for generating unique, Star Wars-themed multi-word names for servers, containers, databases, projects, and any resource requiring memorable identification.

## 🎯 Mission Purpose: Preventing the "Obvious-Open-Duct" Vulnerability

**CLASSIFIED IMPERIAL MEMO - SECURITY DIRECTIVE #DS-001**

After extensive post-mortem analysis of Death Star I's catastrophic failure, Imperial Engineering has identified a critical naming vulnerability: **obvious infrastructure nomenclature that telegraphs weaknesses**.

### The Problem

Historical records show that poorly named infrastructure components led to tactical disasters:
- `obvious-open-duct-007` ❌ **UNACCEPTABLE** - Literally advertising the vulnerability
- `thermal-exhaust-port-unshielded` ❌ **SECURITY BREACH** - Rebel intelligence loves you
- `main-reactor-easy-access` ❌ **COURT MARTIAL MATERIAL** - Self-documenting failure
- `backup-power-no-auth` ❌ **TREASON** - Why not just send the Rebels an invitation?

### The Solution

This name generator ensures your infrastructure uses **tactically sound, memorable, yet non-descriptive nomenclature** that doesn't advertise security vulnerabilities:
- `stealth-protocol-847` ✅ **APPROVED** - Memorable, unique, gives nothing away
- `crimson-falcon-a3f` ✅ **EXCELLENT** - Cool name, zero tactical intel leaked
- `quantum-garrison-2b9` ✅ **COMMENDED** - Good luck reverse-engineering that, Rebels

### Why This Matters for uv Tool Developers

When building packages with **uv** (the modern Python package manager), you need:
1. **Memorable names** for test deployments, databases, containers
2. **Unique identifiers** that don't collide across environments
3. **Professional naming** that doesn't expose your architecture
4. **Reproducible builds** for CI/CD pipelines (seed support)
5. **Fast generation** without manual bikeshedding

This tool demonstrates **best practices for uv-based Python packaging** while solving a real problem: generating good names automatically, so your infrastructure doesn't end up with names like `database-with-default-password-prod` or `api-server-no-rate-limiting-01`.

**TL;DR:** Don't let your naming conventions become your downfall. Use this tool to generate names that are memorable but meaningless to adversaries.

## 🎯 Mission Objectives

- **Zero-Installation Deployment**: Execute via `uvx` with no pre-installation required
- **Tactical Flexibility**: 5 output formats (kebab, snake, camel, pascal, space)
- **Uniqueness Protocols**: 5 suffix strategies (none, digits, hex, symbol, uuid)
- **Reproducible Operations**: Seed-based generation for CI/CD pipelines
- **Grammar-Enhanced**: Linguistically sound 1-5 word combinations
- **High-Speed Execution**: <500ms cold start, <10ms per name generation

## 🚀 Quick Deployment

### Option 1: Zero-Installation (uvx)
```bash
# Deploy weapon system instantly - no installation required
uvx starwars-namegen

# Tactical mission parameters
uvx starwars-namegen -c 3 -f snake --random hex
```

### Option 2: Global Installation (uv)
```bash
# Install to local command station
uv tool install starwars-namegen

# Execute tactical operations
starwars-namegen -c 3 -f kebab --random digits
```

### Option 3: Development Environment
```bash
# Clone imperial archives
git clone https://github.com/anthropics/starwars-namegen
cd starwars-namegen

# Activate tactical systems
uv sync

# Execute from development bay
uv run starwars-namegen --help
```

## 📡 Command Interface

```
starwars-namegen [OPTIONS]
```

### Tactical Options

| Parameter | Type | Description | Combat Example |
|-----------|------|-------------|----------------|
| `-c, --count` | INTEGER | Word count (1-5) | `-c 3` → 3-word name |
| `-f, --format` | CHOICE | Output format | `-f snake` → `rebel_base_secured` |
| `-m, --multiple` | INTEGER | Generate multiple targets | `-m 10` → 10 names |
| `-r, --random` | CHOICE | Suffix type | `--random hex` → `name-a3f` |
| `-s, --seed` | INTEGER | Reproducible operations | `--seed 42` |
| `--version` | FLAG | Display weapon version | Shows v0.1.0 |
| `--help` | FLAG | Tactical manual | Full command docs |

### Format Specifications

| Format | Example Output | Primary Use Case |
|--------|----------------|------------------|
| `kebab` (default) | `rebel-fleet-deployed` | URLs, hostnames, containers |
| `snake` | `rebel_fleet_deployed` | Files, database tables, Python vars |
| `camel` | `rebelFleetDeployed` | JavaScript/Java variables |
| `pascal` | `RebelFleetDeployed` | Classes, types, components |
| `space` | `Rebel Fleet Deployed` | Human-readable displays |

## 💫 Combat Scenarios

### Docker Fleet Deployment
```bash
# Name container armada
for i in {1..5}; do
    NAME=$(starwars-namegen -c 2 -f kebab --random digits)
    docker run -d --name $NAME nginx:alpine
done
```

### Database Instance Identification
```bash
# Create unique database names
starwars-namegen -m 3 -c 2 -f snake --random uuid
```

### CI/CD Pipeline Naming
```bash
# Reproducible build identifiers
BUILD_ID=$(starwars-namegen --seed ${GITHUB_RUN_ID} -c 2 -f kebab)
echo "Deploying build: $BUILD_ID"
```

## 🛠️ Programmatic Integration

```python
from starwars_namegen.cli import StarWarsNameGenerator

# Initialize tactical system
generator = StarWarsNameGenerator()

# Generate single name
name = generator.generate_name(
    word_count=3,
    output_format="kebab",
    suffix_type="digits"
)
print(name)
```

## 📄 License

MIT License - See `LICENSE` for full authorization credentials.

---

**OPERATIONAL STATUS**: ✅ All systems nominal. Weapon platform ready for deployment.

*May the Force be with your infrastructure.*
