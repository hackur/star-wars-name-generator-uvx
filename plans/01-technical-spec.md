# Technical Specification: Star Wars Name Generator

**Version:** 0.1.0
**Status:** Design Complete
**Last Updated:** 2025-10-28

---

## 1. System Overview

### 1.1 Purpose
The Star Wars Name Generator is a command-line tool that generates unique, grammatically coherent names using Star Wars-themed vocabulary for use in software development, DevOps workflows, and system administration tasks.

### 1.2 Core Functionality
- Generate 1-5 word names with proper grammar
- Support multiple output formats (kebab-case, snake_case, camelCase, PascalCase, space-separated)
- Optional random suffixes (digits, hex, symbols, UUID-like)
- Reproducible generation via seed parameter
- Batch generation capability

### 1.3 Target Users
- DevOps engineers naming resources (containers, instances, servers)
- Software developers creating test data
- System administrators managing infrastructure
- General users needing unique identifiers

---

## 2. Architecture Design

### 2.1 Component Architecture

```
┌─────────────────────────────────────────────┐
│           CLI Interface (Click)             │
│  - Argument parsing                         │
│  - Option validation                        │
│  - Output formatting                        │
└────────────────┬────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────┐
│      StarWarsNameGenerator (Core)           │
│  - Vocabulary management                    │
│  - Grammar engine                           │
│  - Format engine                            │
│  - Suffix generator                         │
└─────────────────────────────────────────────┘
                 │
                 ├──► Vocabulary Lists
                 │     - Nouns (45+)
                 │     - Verbs (30+)
                 │     - Adjectives (30+)
                 │     - Adverbs (15+)
                 │
                 ├──► Grammar Rules
                 │     - 1-word pattern
                 │     - 2-word pattern
                 │     - 3-word pattern
                 │     - 4-word pattern
                 │     - 5-word pattern
                 │
                 ├──► Format Engine
                 │     - kebab-case
                 │     - snake_case
                 │     - camelCase
                 │     - PascalCase
                 │     - space separated
                 │
                 └──► Suffix Generator
                       - none
                       - digits (3-digit)
                       - hex (3-char)
                       - symbol
                       - uuid (6-char)
```

### 2.2 Class Design

#### StarWarsNameGenerator Class

```python
class StarWarsNameGenerator:
    """Main generator class with grammar and formatting logic."""

    # Attributes
    - p: inflect.engine()          # Grammar engine
    - nouns: List[str]             # 45+ Star Wars nouns
    - verbs: List[str]             # 30+ Star Wars verbs
    - adjectives: List[str]        # 30+ Star Wars adjectives
    - adverbs: List[str]           # 15+ Star Wars adverbs
    - symbols: List[str]           # Special characters

    # Methods
    - __init__() -> None
    - _get_random_word(word_type: str) -> str
    - _apply_grammar(word_count: int) -> List[str]
    - _to_past_tense(verb: str) -> str
    - _generate_suffix(suffix_type: str) -> str
    - generate_name(word_count: int, output_format: str, suffix_type: str) -> str
    - _format_output(words: List[str], format_type: str, suffix: str) -> str
```

---

## 3. Detailed Specifications

### 3.1 Vocabulary Database

#### Nouns (45+ items)
**Categories:**
- Characters: jedi, sith, droid, wookiee, padawan, master, youngling
- Vehicles: falcon, speeder, fighter, destroyer, cruiser
- Military: trooper, squadron, legion, admiral, general, commander
- Roles: pilot, smuggler, bounty hunter, scavenger, senator
- Locations: cantina, temple, academy, outpost, station, base
- Groups: empire, rebel, force, fleet, armada, garrison

**Selection Criteria:**
- Recognizable Star Wars terms
- Single-word (no multi-word phrases)
- Suitable for professional contexts
- No trademarked character names (e.g., "Luke", "Vader")

#### Verbs (30+ items)
**Categories:**
- Combat: blast, strike, charge, attack, defend, duel
- Movement: hover, spin, pilot, escape, patrol, scout
- Technical: deploy, ignite, wield, transmit, intercept, hack
- Strategic: command, pursue, smuggle, negotiate, sabotage

**Grammar Notes:**
- Base form (infinitive) stored
- Past tense generated dynamically via _to_past_tense()
- Compatible with inflect engine rules

#### Adjectives (30+ items)
**Categories:**
- Factions: galactic, imperial, rebel, rogue
- Qualities: dark, light, swift, silent, elite, stealth
- Scale: legendary, ancient, powerful, advanced
- Combat: tactical, fierce, cunning, brave
- Visual: crimson, azure, emerald, chrome

#### Adverbs (15+ items)
**Categories:**
- Speed: swiftly, rapidly, quickly
- Stealth: silently, stealthily, mysteriously
- Manner: fiercely, boldly, cunningly, precisely
- Strategy: strategically, tactically, efficiently

### 3.2 Grammar Rules

#### 1-Word Pattern
```
Structure: [NOUN]
Example: "jedi"
Use Case: Simple identifiers
```

#### 2-Word Pattern
```
Structure: [ADJECTIVE] [NOUN]
Example: "galactic trooper"
Use Case: Descriptive names
Grammar: Standard adjective-noun English pattern
```

#### 3-Word Pattern
```
Structure: [ADJECTIVE] [NOUN] [VERB_PAST]
Example: "swift jedi deployed"
Use Case: Action-oriented names
Grammar: Noun phrase + past participle (like passive voice)
```

#### 4-Word Pattern
```
Structure: [ADVERB] [ADJECTIVE] [NOUN] [VERB_PAST]
Example: "stealthily dark sith infiltrated"
Use Case: Detailed descriptions
Grammar: Adverb modifies adjective + noun phrase + past participle
```

#### 5-Word Pattern
```
Structure: "the" [ADJECTIVE] [NOUN] [ADVERB] [VERB_PAST]
Example: "the crimson falcon swiftly escaped"
Use Case: Full sentence-like names
Grammar: Definite article + noun phrase + adverb + past participle
```

### 3.3 Past Tense Conversion Rules

```python
def _to_past_tense(verb: str) -> str:
    """
    Simple past tense conversion.

    Rules:
    1. Ends with 'e' → add 'd' (escape → escaped)
    2. Ends with 'y' → replace with 'ied' (deploy → deployed)
    3. Default → add 'ed' (blast → blasted)

    Note: Irregular verbs not handled (e.g., "go" → "went")
          since our verb list uses regular verbs only.
    """
```

### 3.4 Output Formats

#### kebab-case (Default)
```
Format: lowercase-words-separated-by-hyphens
Example: "galactic-trooper-deployed"
Use Cases: URLs, Git branches, Docker containers, file names
Characteristics: URL-safe, highly readable
```

#### snake_case
```
Format: lowercase_words_separated_by_underscores
Example: "galactic_trooper_deployed"
Use Cases: Python variables, database columns, file names
Characteristics: Programming convention, file-system safe
```

#### camelCase
```
Format: firstWordLowercaseRestCapitalized
Example: "galacticTrooperDeployed"
Use Cases: JavaScript variables, Java methods
Characteristics: No separators, programming convention
```

#### PascalCase
```
Format: AllWordsCapitalizedNoSeparators
Example: "GalacticTrooperDeployed"
Use Cases: Class names, type names, components
Characteristics: No separators, OOP convention
```

#### space (Title Case)
```
Format: All Words Capitalized With Spaces
Example: "Galactic Trooper Deployed"
Use Cases: Display names, documentation, human-readable output
Characteristics: Most readable, not code-safe
```

### 3.5 Suffix Generation

#### none (Default)
```
Output: Base name only
Example: "galactic-trooper"
```

#### digits
```
Output: Base name + 3-digit random number
Example: "galactic-trooper-347"
Range: 100-999
Use Case: Simple unique identifiers
```

#### hex
```
Output: Base name + 3-character hexadecimal
Example: "galactic-trooper-a3f"
Range: 000-fff (4096 possibilities)
Use Case: Short unique IDs, compact representation
```

#### symbol
```
Output: Base name + random symbol
Example: "galactic-trooper-$"
Symbols: !, @, #, $, %, ^, &, *, -, _, ~
Use Case: Visual distinction, testing special characters
```

#### uuid
```
Output: Base name + 6-character hex string
Example: "galactic-trooper-b7f9d1"
Range: 16^6 = 16,777,216 possibilities
Use Case: High uniqueness, UUID-like identifiers
```

---

## 4. CLI Interface Specification

### 4.1 Command Syntax

```bash
starwars-namegen [OPTIONS]
```

### 4.2 Options

| Option | Short | Type | Default | Description |
|--------|-------|------|---------|-------------|
| --count | -c | int | random(1-5) | Number of words in name |
| --format | -f | choice | kebab | Output format |
| --multiple | -m | int | 1 | Generate N names |
| --random | -r | choice | none | Suffix type |
| --seed | -s | int | None | Random seed |
| --version | | flag | | Show version |
| --help | | flag | | Show help |

### 4.3 Option Details

#### --count / -c
```
Type: Integer
Range: 1-5 (automatically clamped)
Default: Random selection between 1 and 5
Validation: Values < 1 → 1, values > 5 → 5
Examples:
  -c 1  # Single noun
  -c 3  # Adjective + noun + verb
  -c 5  # Full sentence pattern
```

#### --format / -f
```
Type: Choice
Options: kebab, snake, camel, pascal, space
Default: kebab
Validation: Click choice validation
Examples:
  -f kebab   # galactic-trooper
  -f snake   # galactic_trooper
  -f camel   # galacticTrooper
  -f pascal  # GalacticTrooper
  -f space   # Galactic Trooper
```

#### --multiple / -m
```
Type: Integer
Range: 1-∞ (practical limit ~1000)
Default: 1
Behavior: Outputs N names, one per line
Examples:
  -m 1   # Single name
  -m 5   # Five names
  -m 100 # Hundred names
```

#### --random / -r
```
Type: Choice
Options: none, digits, hex, symbol, uuid
Default: none
Validation: Click choice validation
Examples:
  --random none    # No suffix
  --random digits  # -347
  --random hex     # -a3f
  --random symbol  # -$
  --random uuid    # -b7f9d1
```

#### --seed / -s
```
Type: Integer
Range: Any integer
Default: None (true randomness)
Behavior: Sets random.seed() for reproducibility
Examples:
  --seed 42    # Always same output for seed 42
  --seed 12345 # Different deterministic output
```

### 4.4 Usage Examples

```bash
# Basic usage - random name
starwars-namegen
# → galactic-trooper

# Specific word count
starwars-namegen -c 3
# → swift-jedi-deployed

# Different format
starwars-namegen -c 3 -f snake
# → swift_jedi_deployed

# With suffix
starwars-namegen --random digits
# → galactic-trooper-347

# Multiple names
starwars-namegen -m 5
# → (5 names output)

# Reproducible
starwars-namegen --seed 42
# → (always same output)

# Complex combination
starwars-namegen -c 4 -f pascal --random hex -m 3
# → SwiftlyDarkSithInfiltrated-a3f
# → FiercelyGalacticTrooperDeployed-b7c
# → SilentlyRogueJediEscaped-d2e
```

---

## 5. Dependencies

### 5.1 Runtime Dependencies

#### click >= 8.0.0
```
Purpose: CLI framework
Features Used:
  - Command decorator
  - Option decorators with types
  - Choice validation
  - Version option
  - Echo for output

Why Click:
  - Industry standard for Python CLIs
  - Excellent validation and help generation
  - Type-safe option handling
  - Minimal boilerplate

Documentation: https://click.palletsprojects.com/
```

#### inflect >= 7.0.0
```
Purpose: Grammar engine (future-proofing)
Features Used:
  - Potential for pluralization
  - Number to word conversion (future)
  - Grammar utilities

Current Usage:
  - Initialized but basic past tense is manual
  - Reserved for future grammar improvements

Why inflect:
  - Standard Python grammar library
  - Extensible for future features
  - Lightweight

Documentation: https://inflect.readthedocs.io/
```

### 5.2 Build Dependencies

#### hatchling
```
Purpose: Build backend
Why: Recommended by uv, modern, fast
Configuration: pyproject.toml [build-system]
```

### 5.3 Dependency Pinning Strategy

```toml
[project]
dependencies = [
    "click>=8.0.0",    # Allow minor updates
    "inflect>=7.0.0",  # Allow minor updates
]
```

**Rationale:**
- `>=` allows minor version updates for bug fixes
- Major version locked to prevent breaking changes
- Tested with latest versions as of 2025-10-28

---

## 6. Testing Specification

### 6.1 Manual Testing Matrix

| Feature | Test Case | Expected Result |
|---------|-----------|-----------------|
| Basic execution | `starwars-namegen` | Single kebab-case name |
| Help | `--help` | Full help text with all options |
| Version | `--version` | Version number display |
| 1-word | `-c 1` | Single noun |
| 2-word | `-c 2` | Adjective + noun |
| 3-word | `-c 3` | Adj + noun + past verb |
| 4-word | `-c 4` | Adv + adj + noun + past verb |
| 5-word | `-c 5` | "the" + adj + noun + adv + past verb |
| Kebab format | `-f kebab` | lowercase-with-hyphens |
| Snake format | `-f snake` | lowercase_with_underscores |
| Camel format | `-f camel` | camelCaseFormat |
| Pascal format | `-f pascal` | PascalCaseFormat |
| Space format | `-f space` | Title Case Format |
| No suffix | `--random none` | No suffix appended |
| Digits suffix | `--random digits` | name-### |
| Hex suffix | `--random hex` | name-xxx |
| Symbol suffix | `--random symbol` | name-X |
| UUID suffix | `--random uuid` | name-xxxxxx |
| Multiple | `-m 5` | 5 names, one per line |
| Seed reproducibility | `--seed 42` (run twice) | Identical output |
| Combination | `-c 3 -f snake --random hex` | 3-word_snake_case-a3f |

### 6.2 Edge Cases

| Test | Input | Expected Behavior |
|------|-------|-------------------|
| Invalid count low | `-c 0` | Clamped to 1 |
| Invalid count high | `-c 10` | Clamped to 5 |
| Invalid format | `-f invalid` | Click validation error |
| Negative multiple | `-m -1` | Click validation error |
| Large multiple | `-m 1000` | 1000 names output |
| Space format with suffix | `-f space --random digits` | "Name Here 347" |

### 6.3 Integration Tests

| Scenario | Test | Validation |
|----------|------|------------|
| uvx execution | `uvx starwars-namegen` | Runs without install |
| Docker naming | `docker run --name $(starwars-namegen)` | Valid container name |
| File creation | `touch $(starwars-namegen -f snake).txt` | Valid filename |
| Variable naming | Use camelCase output | Valid code identifier |
| Git branch | `git checkout -b $(starwars-namegen)` | Valid branch name |

---

## 7. Performance Specifications

### 7.1 Performance Requirements

| Metric | Target | Rationale |
|--------|--------|-----------|
| Startup time | < 500ms | CLI responsiveness |
| Single generation | < 10ms | Negligible delay |
| 1000 generations | < 1s | Batch efficiency |
| Memory usage | < 50MB | Lightweight tool |
| Package size | < 500KB | Quick download |

### 7.2 Scalability

- **Vocabulary Size:** 120+ total words → O(1) random selection
- **Grammar Rules:** 5 patterns → O(1) selection
- **Format Engine:** 5 formats → O(n) where n = word count (max 5)
- **Suffix Generation:** O(1) for all types

**Overall Complexity:** O(1) per name generation

---

## 8. Security Considerations

### 8.1 Input Validation
- All CLI inputs validated by Click
- Integer ranges enforced (count, multiple, seed)
- Choice options restricted to valid sets
- No user-supplied code execution

### 8.2 Output Safety
- All formats produce safe strings
- No shell command injection vectors
- File-system safe characters only (except symbol suffix)
- URL-safe in kebab mode

### 8.3 Dependency Security
- Using well-maintained packages (click, inflect)
- No known vulnerabilities in specified versions
- Minimal dependency tree

---

## 9. Compatibility Matrix

### 9.1 Python Versions
```
Minimum: Python 3.9
Tested: Python 3.9, 3.10, 3.11, 3.12, 3.13
Reason for 3.9+: Modern type hints, dict ordering
```

### 9.2 Operating Systems
```
Primary: macOS 10.13+
Secondary: Linux (Ubuntu 20.04+, Debian 11+)
Tertiary: Windows 10+ (via WSL or native)
```

### 9.3 Installation Methods
```
✅ uvx starwars-namegen (recommended)
✅ uv tool install starwars-namegen
✅ pip install starwars-namegen
✅ pipx install starwars-namegen
```

---

## 10. Future Enhancements (v0.2.0+)

### Potential Features
1. **Custom Vocabulary:** User-supplied word lists
2. **Themes:** Different theme modes (Marvel, LOTR, etc.)
3. **Grammar Improvements:** More complex patterns
4. **Configuration File:** `.starwars-namegen.toml` for defaults
5. **Output Templates:** Custom format strings
6. **API Mode:** JSON output for programmatic use
7. **Uniqueness Check:** Verify name not already used
8. **Database:** Store previously generated names
9. **Web UI:** Simple web interface
10. **Plugins:** Extensible plugin system

### Not In Scope (v0.1.0)
- Database persistence
- Web interface
- Network calls
- User accounts
- Cloud integration
- AI/ML features

---

**Document Version:** 1.0
**Status:** Final
**Approved By:** Development Team
**Next Review:** Post-v0.1.0 release
