# Star Wars Name Generator - Feature Guide

**A Deep Dive into Every Feature and Why It Exists**

This document explains every feature of `starwars-namegen`, the design decisions behind them, and how they demonstrate modern Python packaging patterns with UV.

---

## Table of Contents

1. [Core Concept: Linguistic Name Generation](#core-concept)
2. [Word Count Control](#word-count-control)
3. [Output Formats](#output-formats)
4. [Suffix Strategies](#suffix-strategies)
5. [Batch Generation](#batch-generation)
6. [Seed-Based Reproducibility](#seed-based-reproducibility)
7. [Star Wars Vocabulary](#star-wars-vocabulary)
8. [Grammar Rules](#grammar-rules)
9. [CLI Design Philosophy](#cli-design-philosophy)
10. [Package Design Patterns](#package-design-patterns)

---

## Core Concept: Linguistic Name Generation

### The Problem We Solve

Developers need memorable, unique identifiers for:
- Docker containers
- Database instances
- Test servers
- CI/CD builds
- Kubernetes pods
- Feature branches

**Bad naming leads to:**
- `obvious-open-duct-007` - Security through obscurity violated
- `prod-db-main-backup-2` - Boring and error-prone
- `temp-server-1` - Not memorable, will multiply

**Good naming provides:**
- Memorability: "The falcon-executor crashed" is easier than "Container ID: a3f2b9c"
- Uniqueness: Suffixes prevent collisions
- Security: Non-descriptive names don't reveal architecture
- Fun: Star Wars theme makes DevOps more enjoyable

### Our Solution

Generate linguistically correct, Star Wars-themed names:
```
covert-padawan-infiltrated-a3f
legendary-millennium-falcon-hyperspaceed-2b9
swift-jedi-temple-defended
```

---

## Word Count Control

### Feature: `-c, --count INTEGER`

Control name complexity from 1-5 words.

```bash
# Simple (1 word)
starwars-namegen -c 1
# Output: destroyer

# Moderate (2-3 words)
starwars-namegen -c 2
# Output: stealth-cruiser

# Complex (4-5 words)
starwars-namegen -c 5
# Output: the-legendary-falcon-swiftly-escaped
```

### Why This Exists

Different use cases need different complexity:

| Word Count | Use Case | Example |
|------------|----------|---------|
| 1 word | Internal variables | `falcon = new_server()` |
| 2 words | Container names | `docker run --name stealth-cruiser` |
| 3 words | Database instances | `postgres-rebel-base-secured` |
| 4 words | Feature branches | `feat/ancient-jedi-temple-discovered` |
| 5 words | Descriptive builds | `the-experimental-xwing-successfully-deployed` |

### Grammar Rules by Word Count

1. **1 word**: `NOUN`
   - `destroyer`, `falcon`, `jedi`

2. **2 words**: `ADJECTIVE NOUN`
   - `stealth cruiser`, `dark lord`, `ancient temple`

3. **3 words**: `ADJECTIVE NOUN PAST_VERB`
   - `rebel base secured`, `imperial fleet deployed`

4. **4 words**: `ADVERB ADJECTIVE NOUN PAST_VERB`
   - `swiftly ancient temple discovered`

5. **5 words**: `the ADJECTIVE NOUN ADVERB PAST_VERB`
   - `the legendary falcon rapidly escaped`

### Implementation Pattern (Teaching UV)

```python
def generate_name(self, word_count: Optional[int] = None):
    # Random if not specified
    if word_count is None:
        word_count = random.randint(1, 5)

    # Clamp to valid range
    word_count = max(1, min(5, word_count))

    # Apply grammar rules
    return self._apply_grammar(word_count)
```

**What This Teaches:**
- Type hints (`Optional[int]`)
- Default parameters
- Input validation
- Separation of concerns (grammar rules separate)

---

## Output Formats

### Feature: `-f, --format CHOICE`

Five output formats for different use cases.

```bash
# kebab-case (default)
starwars-namegen -f kebab
# Output: rebel-alliance-mobilized-a3f
# Perfect for: URLs, hostnames, Docker, K8s

# snake_case
starwars-namegen -f snake
# Output: imperial_destroyer_deployed_2b9
# Perfect for: Files, DB tables, Python variables

# camelCase
starwars-namegen -f camel
# Output: jediTempleMeditated
# Perfect for: JavaScript, Java variables

# PascalCase
starwars-namegen -f pascal
# Output: SithLordDominated
# Perfect for: Classes, types, components

# Space separated
starwars-namegen -f space
# Output: Stealth Fighter Engaged
# Perfect for: Human-readable displays
```

### Why Multiple Formats?

Different ecosystems have different naming conventions:

**Web/DevOps** (kebab-case):
```bash
# DNS-safe, URL-safe
https://api.example.com/rebel-fleet-deployed-a3f
docker run --name imperial-destroyer-2b9
```

**Python/Databases** (snake_case):
```python
# PEP 8 compliant
rebel_base_connection = connect('postgresql://rebel_base_secured')
table_name = 'jedi_temple_archives'
```

**JavaScript/Java** (camelCase/PascalCase):
```javascript
// JavaScript
const rebelAllianceApi = new Api();

// Java
public class ImperialDestroyer extends Ship {
    private String jediTemplePilot;
}
```

### Format Implementation (Teaching UV)

```python
def _format_output(self, words: List[str], format: str, suffix: str):
    if format == "kebab":
        base = "-".join(word.lower() for word in words)
        return f"{base}-{suffix}" if suffix else base

    elif format == "snake":
        base = "_".join(word.lower() for word in words)
        return f"{base}_{suffix}" if suffix else base

    elif format == "camel":
        base = words[0].lower() + "".join(w.capitalize() for w in words[1:])
        return base + suffix.capitalize() if suffix else base

    # ... more formats
```

**What This Teaches:**
- String manipulation
- List comprehensions
- Conditional logic
- Clean code patterns (each format is clear)

---

## Suffix Strategies

### Feature: `--random, -r CHOICE`

Five suffix types to prevent name collisions.

```bash
# No suffix
starwars-namegen --random none
# Output: rebel-alliance

# 3-digit number (1/1000 collision)
starwars-namegen --random digits
# Output: imperial-fleet-847

# 3-character hex (1/4096 collision)
starwars-namegen --random hex
# Output: jedi-temple-a3f

# Random symbol
starwars-namegen --random symbol
# Output: sith-lord-@

# 6-character UUID-like (1/16M collision)
starwars-namegen --random uuid
# Output: millennium-falcon-9a4f2c
```

### Collision Risk Analysis

| Suffix Type | Characters | Combinations | Collision Risk | Use Case |
|-------------|------------|--------------|----------------|----------|
| none | - | ~1.4M | Medium | Local dev |
| digits | 3 | 1,000 | Low | Small clusters |
| hex | 3 | 4,096 | Low | Medium clusters |
| symbol | 1 | 12 | High | Visual markers |
| uuid | 6 | 16,777,216 | Very Low | Large scale |

### Real-World Example

**Docker Swarm with 100 containers:**

```bash
# Using digits suffix
for i in {1..100}; do
    name=$(starwars-namegen -c 2 --random digits)
    docker run -d --name $name nginx:alpine
done

# Results:
# rebel-base-001
# imperial-fleet-473
# jedi-temple-892
# ... (0% collision chance with 1000 possible suffixes)
```

**Kubernetes with 10,000 pods:**

```bash
# Use UUID suffix for near-zero collision
kubectl run $(starwars-namegen -c 2 --random uuid) --image=nginx

# Results:
# rebel-base-a3f2b9
# imperial-fleet-c7dc6c
# ... (0.0006% collision chance)
```

### Implementation (Teaching UV)

```python
def _generate_suffix(self, suffix_type: str) -> str:
    if suffix_type == "none":
        return ""
    elif suffix_type == "digits":
        return f"{random.randint(0, 999):03d}"
    elif suffix_type == "hex":
        return f"{random.randint(0, 4095):03x}"
    elif suffix_type == "symbol":
        return f"{random.choice(self.symbols)}"
    elif suffix_type == "uuid":
        return ''.join(random.choices('0123456789abcdef', k=6))
```

**What This Teaches:**
- String formatting (`f"{value:03d}"`)
- Random number generation
- Hexadecimal formatting
- Trade-offs in system design

---

## Batch Generation

### Feature: `-m, --multiple INTEGER`

Generate multiple names in one command.

```bash
# Generate 10 names for Docker swarm
starwars-namegen -m 10 -c 2 -f kebab --random hex

# Output:
# rebel-fleet-a3f
# imperial-destroyer-2b9
# jedi-temple-f14
# sith-academy-8c2
# millennium-falcon-5d7
# ... (10 total)
```

### Why Batch Generation?

**DevOps Automation:**
```bash
# Create 20 test environments
for name in $(starwars-namegen -m 20 -c 2 --random uuid); do
    terraform apply -var="instance_name=$name"
done
```

**CI/CD Pipelines:**
```yaml
# .gitlab-ci.yml
deploy:
  script:
    - NAMES=$(starwars-namegen -m $INSTANCE_COUNT -c 2 -f snake)
    - for name in $NAMES; do deploy_instance $name; done
```

**Kubernetes Manifests:**
```bash
# Generate 5 pod names for manifest
starwars-namegen -m 5 -c 2 --random hex | \
  while read name; do
    cat > "pod-$name.yaml" <<EOF
apiVersion: v1
kind: Pod
metadata:
  name: $name
EOF
  done
```

### Implementation (Teaching UV)

```python
@click.option('--multiple', '-m', default=1, help="Generate multiple names")
def main(count, format, multiple, random, seed):
    for _ in range(multiple):
        name = generator.generate_name(...)
        click.echo(name)
```

**What This Teaches:**
- Click options
- Loop patterns
- Output formatting
- CLI design

---

## Seed-Based Reproducibility

### Feature: `--seed, -s INTEGER`

Generate reproducible names for testing and CI/CD.

```bash
# Same seed = same name
starwars-namegen --seed 42 -c 3
# Output: cowardly-council-patroled

# Run again with seed 42
starwars-namegen --seed 42 -c 3
# Output: cowardly-council-patroled (identical!)
```

### Why Reproducibility Matters

**CI/CD Pipelines:**
```yaml
# Always use the same name for a given build
deploy:
  script:
    - NAME=$(starwars-namegen --seed ${CI_PIPELINE_ID} -c 2)
    - deploy_to $NAME
```

**Testing:**
```python
def test_deployment():
    # Use seed for reproducible test names
    name = generate_name(seed=12345, word_count=2)
    deploy(name)
    assert check_deployment(name)
    cleanup(name)  # Easy to find and clean up
```

**Debugging:**
```bash
# Production issue with "rebel-base-secured-a3f"
# Reproduce locally:
starwars-namegen --seed 12345 -c 3 --random hex
# Get same name to investigate
```

### Implementation (Teaching UV)

```python
@click.option('--seed', '-s', type=int, help="Random seed")
def main(seed, ...):
    if seed is not None:
        random.seed(seed)

    generator = StarWarsNameGenerator()
    name = generator.generate_name(...)
```

**What This Teaches:**
- Random seeding
- Reproducibility in software
- Testing patterns
- CI/CD best practices

---

## Star Wars Vocabulary

### Feature: 500+ Star Wars Terms

The generator uses an extensive vocabulary of Star Wars terms organized by category.

#### Vocabulary Breakdown

**Nouns (200+):**
- Ships: falcon, destroyer, xwing, tiefighter, millennium-falcon
- Planets: tatooine, hoth, endor, coruscant, naboo
- Ranks: jedi, sith, padawan, master, knight
- Creatures: wookiee, rancor, wampa, bantha
- Locations: temple, base, cantina, hangar
- Characters: skywalker, vader, kenobi, palpatine (easter eggs!)

**Verbs (200+):**
- Combat: strike, attack, defend, assault, duel
- Force Powers: levitate, push, grip, sense, meditate
- Technical: pilot, navigate, hack, repair, scan
- Stealth: cloak, infiltrate, evade, smuggle

**Adjectives (280+):**
- Factions: imperial, rebel, jedi, sith, mandalorian
- Force: light-side, dark-side, force-sensitive
- Combat: tactical, stealth, elite, veteran
- Appearance: crimson, azure, emerald, obsidian

**Adverbs (90+):**
- Speed: swiftly, rapidly, slowly
- Stealth: covertly, secretly, silently
- Force: heroically, cunningly, wisely

### Easter Eggs

Subtle character references (legally safe, no trademark issues):
```bash
# These combinations might appear:
legendary-skywalker-defended
dark-vader-dominated
wise-kenobi-meditated
cunning-palpatine-manipulated
swift-fett-hunted
```

### Why So Many Words?

**Combinatorial Explosion:**
- 200 nouns × 280 adjectives = 56,000 2-word combinations
- Add verbs: 56,000 × 200 = 11,200,000 3-word combinations
- Add suffixes: 11,200,000 × 4,096 (hex) = 45 BILLION+ unique names

**Reduces Collisions:**
```bash
# Small vocabulary = frequent duplicates
with 10 nouns: 10 × 10 = 100 combinations

# Large vocabulary = rare duplicates
with 200 nouns: 200 × 280 = 56,000 combinations
```

---

## Grammar Rules

### Feature: Linguistically Correct Names

Names follow proper English grammar rules.

#### Past Tense Conversion

```python
def _to_past_tense(self, verb: str) -> str:
    # Rule 1: Verbs ending in 'e' add 'd'
    if verb.endswith('e'):
        return verb + 'd'  # escape → escaped

    # Rule 2: Verbs ending in consonant+y become 'ied'
    elif verb.endswith('y') and verb[-2] not in 'aeiou':
        return verb[:-1] + 'ied'  # spy → spied

    # Rule 3: Default add 'ed'
    else:
        return verb + 'ed'  # attack → attacked
```

**Results:**
- `rebel-base-secured` (not "rebel-base-secure")
- `jedi-temple-defended` (not "jedi-temple-defend")
- `imperial-fleet-deployed` (not "imperial-fleet-deploy")

### Why Grammar Matters

**Readability:**
```
✅ GOOD: swift-falcon-escaped
❌ BAD:  swift-falcon-escape

✅ GOOD: dark-lord-dominated
❌ BAD:  dark-lord-dominate
```

**Professionalism:**
Using correct grammar shows attention to detail.

---

## CLI Design Philosophy

### Feature: Click-Based CLI

Built with Click for modern CLI patterns.

```python
import click

@click.command()
@click.option('--count', '-c', type=click.IntRange(1, 5))
@click.option('--format', '-f', type=click.Choice(['kebab', 'snake', ...]))
@click.option('--multiple', '-m', default=1)
@click.option('--random', '-r', type=click.Choice(['none', 'digits', ...]))
@click.option('--seed', '-s', type=int)
@click.version_option(version="0.1.0")
def main(count, format, multiple, random, seed):
    """Generate Star Wars-themed names for your infrastructure."""
    # ... implementation
```

### Design Principles

1. **Short and Long Options:** `-c` and `--count`
2. **Type Validation:** `click.IntRange(1, 5)`
3. **Choices:** `click.Choice(['kebab', 'snake', ...])`
4. **Help Text:** Automatic `--help` generation
5. **Version:** `--version` flag included

### Why Click?

**Before Click (argparse):**
```python
import argparse

parser = argparse.ArgumentParser(description="Generate names")
parser.add_argument('--count', '-c', type=int, choices=range(1,6))
parser.add_argument('--format', '-f', choices=['kebab', 'snake'])
# ... 50+ lines of boilerplate
```

**With Click:**
```python
import click

@click.command()
@click.option('--count', '-c', type=click.IntRange(1,5))
@click.option('--format', '-f', type=click.Choice(['kebab', 'snake']))
def main(count, format):
    pass  # Clean and simple!
```

---

## Package Design Patterns

### Feature: Clean Package Architecture

The package demonstrates modern Python patterns.

#### Src-Layout

```
✅ GOOD (src-layout):
src/
  starwars_namegen/
    __init__.py
    cli.py

❌ BAD (flat layout):
starwars_namegen/
  __init__.py
  cli.py
```

**Why?** Prevents accidental imports during development.

#### Type Hints

```python
from typing import List, Optional

def generate_name(
    self,
    word_count: Optional[int] = None,
    output_format: str = "kebab",
    suffix_type: str = "none"
) -> str:
    """Generate a name with full type safety."""
    pass
```

**Benefits:**
- IDE autocomplete
- mypy type checking
- Self-documenting code

#### Dependency Injection

```python
class StarWarsNameGenerator:
    def __init__(self):
        self.inflect_engine = inflect.engine()
```

**Benefits:**
- Testability
- Flexibility
- Clear dependencies

#### Separation of Concerns

```python
# Each method does ONE thing
def _get_random_word(self, word_type: str) -> str: ...
def _apply_grammar(self, word_count: int) -> List[str]: ...
def _generate_suffix(self, suffix_type: str) -> str: ...
def _format_output(self, words: List[str], ...) -> str: ...
def generate_name(self, ...) -> str: ...  # Orchestrates above
```

---

## Conclusion

Every feature in `starwars-namegen` serves multiple purposes:

1. **Solves a real problem** (memorable, unique names)
2. **Demonstrates best practices** (UV, Click, type hints)
3. **Is fun to use** (Star Wars theme)

**Learn by doing:**
```bash
# Try each feature
uvx starwars-namegen -c 3 -f snake --random hex -m 5 --seed 42
```

**Then build your own:**
```bash
uv init my-awesome-tool
# Apply what you learned!
```

**Author**: Jeremy Sarda (jeremy@hackur.io)
**May the Force be with your infrastructure!**
