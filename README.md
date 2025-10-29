# ⭐ Star Wars Name Generator

> **DEATH STAR OPERATIONAL PROTOCOL**: A precision tactical weapon system for generating Star Wars-themed nomenclature across all Imperial infrastructure deployments.

A professional CLI tool for generating unique, Star Wars-themed multi-word names for servers, containers, databases, projects, and any resource requiring memorable identification.

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
