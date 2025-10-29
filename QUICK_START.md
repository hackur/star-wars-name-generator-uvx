# Star Wars Name Generator - Quick Start Guide

**Get started in 30 seconds**

## Instant Usage (Zero Installation)

```bash
# If published to PyPI (future):
uvx starwars-namegen

# For now, use local installation:
uv tool install dist/starwars_namegen-0.1.0-py3-none-any.whl
starwars-namegen
```

## Common Commands

```bash
# Generate random name
starwars-namegen

# 3-word name for servers
starwars-namegen -c 3 -f kebab --random digits
# Output: rebel-fleet-secured-847

# Python variable names
starwars-namegen -c 2 -f snake
# Output: imperial_destroyer

# Class names
starwars-namegen -c 2 -f pascal
# Output: GalacticEmpire

# Generate 5 container names
starwars-namegen -m 5 -c 2 -f kebab --random hex
# Output:
# stealth-trooper-a3f
# quantum-fleet-2b9
# shadow-base-f14
# tactical-saber-8c2
# crimson-falcon-5d7

# Reproducible (same seed = same name)
starwars-namegen --seed 42 -c 3
# Always outputs: cowardly-council-patroled
```

## Quick Examples

### Docker Containers
```bash
for i in {1..5}; do
    docker run -d --name $(starwars-namegen -c 2 -f kebab --random digits) nginx:alpine
done
```

### Python Usage
```python
from starwars_namegen.cli import StarWarsNameGenerator

gen = StarWarsNameGenerator()
name = gen.generate_name(word_count=3, output_format="kebab", suffix_type="hex")
print(name)  # rebel-base-secured-a3f
```

## All Options

| Option | Description | Example |
|--------|-------------|---------|
| `-c, --count` | Word count (1-5) | `-c 3` |
| `-f, --format` | Format type | `-f snake` |
| `-m, --multiple` | Generate multiple | `-m 10` |
| `-r, --random` | Suffix type | `--random hex` |
| `-s, --seed` | Reproducible seed | `--seed 42` |

**Formats**: `kebab`, `snake`, `camel`, `pascal`, `space`
**Suffixes**: `none`, `digits`, `hex`, `symbol`, `uuid`

---

**That's it! May the Force be with your infrastructure.**

Created by Jeremy Sarda - https://gitlab.com/hackur/starwars-namegen
