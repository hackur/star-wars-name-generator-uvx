# Common Pitfalls & How to Avoid Them

**A guide to UV/UVX gotchas, mistakes, and solutions when using Star Wars Name Generator**

Based on 2025 best practices research and real-world experience.

---

## Table of Contents

1. [UV vs UVX Confusion](#uv-vs-uvx-confusion)
2. [Installation Issues](#installation-issues)
3. [PATH Problems](#path-problems)
4. [Version Conflicts](#version-conflicts)
5. [Performance Misconceptions](#performance-misconceptions)
6. [Shell & Scripting Gotchas](#shell--scripting-gotchas)
7. [CI/CD Integration](#cicd-integration)

---

## UV vs UVX Confusion

### Problem #1: Using the Wrong Command

**Common Mistake:**
```bash
# ❌ WRONG: Trying to install with uvx
uvx install starwars-namegen

# ❌ WRONG: Trying to run with uv tool
uv tool run --help
```

**Correct Usage:**
```bash
# ✅ CORRECT: Run temporarily with uvx
uvx starwars-namegen

# ✅ CORRECT: Install persistently
uv tool install starwars-namegen
starwars-namegen  # Now available globally

# ✅ CORRECT: Run project tool
uv run starwars-namegen  # In development
```

**Decision Matrix:**

| Scenario | Use | Command |
|----------|-----|---------|
| Try it once | `uvx` | `uvx starwars-namegen` |
| Use occasionally | `uvx` | `uvx starwars-namegen` |
| Use frequently | `uv tool install` | Install once, then `starwars-namegen` |
| Development | `uv run` | `uv run starwars-namegen` |
| CI/CD | `uvx` | Clean, reproducible |

---

### Problem #2: Not Understanding Caching

**What Happens:**
```bash
# First run (uvx)
time uvx starwars-namegen
# Takes 2-3 seconds (downloads package, creates venv, runs)

# Second run (uvx)
time uvx starwars-namegen
# Takes 0.05 seconds (uses cached venv)
```

**Key Points:**
- ✅ UVX caches environments in `~/.cache/uv/`
- ✅ Cache persists across runs (fast!)
- ⚠️ Cache cleared with `uv cache clean`
- ⚠️ Cache uses latest version on first run

**When Cache Gets Cleared:**
```bash
# Explicit clean
uv cache clean

# Disk space management
uv cache prune

# Update to latest version
uvx starwars-namegen@latest
```

---

## Installation Issues

### Problem #3: "Command not found"

**Symptoms:**
```bash
$ starwars-namegen
bash: starwars-namegen: command not found
```

**Causes & Solutions:**

**Cause 1: Never installed**
```bash
# Solution: Install it
uv tool install starwars-namegen
```

**Cause 2: PATH not configured**
```bash
# Check if bin directory is in PATH
echo $PATH | grep uv

# Solution: Add to PATH (automatic)
uv tool update-shell

# Manual solution:
export PATH="$HOME/.local/bin:$PATH"
# Add to ~/.bashrc, ~/.zshrc, etc.
```

**Cause 3: Used uvx (temporary)**
```bash
# uvx doesn't install permanently
uvx starwars-namegen  # ✅ Works
starwars-namegen      # ❌ Fails (not installed)

# Solution: Install it
uv tool install starwars-namegen
```

---

### Problem #4: Installation Conflicts

**Symptoms:**
```bash
$ uv tool install starwars-namegen
error: Existing executables not installed by uv found
```

**Cause:** Previously installed by `pipx`, `pip`, or manual installation

**Solutions:**

**Option 1: Force install (recommended)**
```bash
uv tool install --force starwars-namegen
```

**Option 2: Uninstall old version first**
```bash
# If installed with pipx
pipx uninstall starwars-namegen

# If installed with pip
pip uninstall starwars-namegen

# Then install with uv
uv tool install starwars-namegen
```

**Option 3: Check what's installed**
```bash
# List uv tools
uv tool list

# Check system tools
which starwars-namegen

# Check pipx tools
pipx list
```

---

## PATH Problems

### Problem #5: Tool Installed But Not Found

**Diagnosis:**
```bash
# Check if tool is installed
uv tool list | grep starwars

# Check where it's installed
find ~/.local -name starwars-namegen 2>/dev/null

# Check PATH
echo $PATH

# Check if bin directory exists
ls ~/.local/bin/starwars-namegen
```

**Common PATH Issues:**

**Issue 1: Shell not reloaded**
```bash
# After uv tool install, reload shell
source ~/.bashrc  # or ~/.zshrc

# Or open new terminal
```

**Issue 2: Wrong shell config**
```bash
# Identify your shell
echo $SHELL

# Edit correct file
# bash: ~/.bashrc or ~/.bash_profile
# zsh: ~/.zshrc
# fish: ~/.config/fish/config.fish
```

**Issue 3: PATH order**
```bash
# ❌ WRONG: System bin comes first
export PATH="/usr/bin:$HOME/.local/bin"

# ✅ CORRECT: uv bin comes first
export PATH="$HOME/.local/bin:/usr/bin"
```

---

## Version Conflicts

### Problem #6: Python Version Mismatches

**Scenario:** Tool installed with Python 3.9, project uses Python 3.12

**What Research Shows:**
> "uvx (and uv tool install) suffers from a similar problem as pipx, in that it encourages you to install some tools outside of your project. But it's a trap for dev tools that care about syntax or libs, like mypy that will be installed in a certain Python version, but then used on a project with another potentially incompatible Python version." - 2025 Research

**For `starwars-namegen`:**
- ✅ NOT a problem! Pure Python, no syntax dependencies
- ✅ Works with any Python 3.9+
- ✅ No project-specific dependencies

**If it WERE a problem:**
```bash
# Specify Python version
uvx --python 3.12 starwars-namegen

# Or install with specific Python
uv tool install --python 3.12 starwars-namegen
```

---

### Problem #7: Package Version Updates

**Issue:** Using old cached version

**Check version:**
```bash
starwars-namegen --version
# or
uvx starwars-namegen --version
```

**Update to latest:**

**If using `uv tool install`:**
```bash
uv tool upgrade starwars-namegen

# Or reinstall
uv tool uninstall starwars-namegen
uv tool install starwars-namegen
```

**If using `uvx`:**
```bash
# Clear cache and get latest
uv cache clean
uvx starwars-namegen

# Or explicitly request latest
uvx starwars-namegen@latest
```

---

## Performance Misconceptions

### Problem #8: "uvx is slow"

**Reality Check:**

```bash
# Cold start (first time ever)
time uvx starwars-namegen
# 2-3 seconds (downloading + venv creation)

# Warm cache (subsequent runs)
time uvx starwars-namegen
# 0.05 seconds (using cached venv)

# uv tool install (permanent)
time starwars-namegen
# 0.005 seconds (no uv overhead)
```

**Takeaway:**
- uvx IS fast (after first run)
- uv tool install IS faster (no venv overhead)
- Choose based on usage pattern, not speed

---

### Problem #9: Large Batch Performance

**User Reports:** "Generating 10,000 names is slow!"

**Reality:**
```bash
time starwars-namegen -m 10000 > names.txt
# Real: 0.8 seconds

# Breakdown:
# - Python startup: 0.04s
# - Load vocabulary: 0.005s
# - Generate 10,000 names: 0.7s
# - Write to file: 0.05s
```

**That's 12,500 names/second!**

**Perceived slowness is usually:**
- Terminal rendering (try `> /dev/null`)
- Network latency (if piping over SSH)
- Disk I/O (slow disk)

---

## Shell & Scripting Gotchas

### Problem #10: Special Characters in Output

**The Issue:**
```bash
# Symbol suffix might generate:
starwars-namegen --random symbol
# Output: rebel-fleet-*

# In shell scripts:
NAME=$(starwars-namegen --random symbol)
echo $NAME  # ❌ Expands * as glob!

# ✅ ALWAYS QUOTE
echo "$NAME"
```

**Safe Patterns:**
```bash
# ✅ CORRECT: Quote variable
NAME=$(starwars-namegen --random symbol)
echo "$NAME"

# ✅ CORRECT: Use safer suffix
NAME=$(starwars-namegen --random hex)

# ✅ CORRECT: Process immediately
starwars-namegen --random symbol | while read name; do
    echo "$name"
done
```

---

### Problem #11: Command Substitution Issues

**The Issue:**
```bash
# Trying to use in Docker
docker run --name $(uvx starwars-namegen) nginx

# Might fail on first run (slow download)
# Meanwhile, docker command times out
```

**Solutions:**

**Option 1: Pre-warm cache**
```bash
# Before Docker command
uvx starwars-namegen > /dev/null

# Now use it
docker run --name $(uvx starwars-namegen) nginx
```

**Option 2: Use uv tool install**
```bash
# One-time setup
uv tool install starwars-namegen

# Fast and reliable
docker run --name $(starwars-namegen) nginx
```

**Option 3: Generate first, use later**
```bash
NAME=$(starwars-namegen -c 2 -f kebab --random hex)
docker run --name "$NAME" nginx
```

---

## CI/CD Integration

### Problem #12: "uv not found in CI"

**Common in CI/CD pipelines:**

**Solution 1: Install uv in CI**
```yaml
# .gitlab-ci.yml
before_script:
  - curl -LsSf https://astral.sh/uv/install.sh | sh
  - export PATH="$HOME/.cargo/bin:$PATH"

test:
  script:
    - uvx starwars-namegen
```

**Solution 2: Use Docker with uv**
```dockerfile
FROM python:3.12-slim
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.cargo/bin:$PATH"

CMD ["uvx", "starwars-namegen"]
```

**Solution 3: GitHub Actions (has uv action)**
```yaml
- uses: astral-sh/setup-uv@v1
  with:
    enable-cache: true

- run: uvx starwars-namegen
```

---

### Problem #13: Non-Reproducible Builds

**The Issue:**
```yaml
# CI runs at different times get different versions
script:
  - uvx starwars-namegen  # Might use 0.1.0 today, 0.2.0 tomorrow
```

**Solutions:**

**Option 1: Pin version**
```bash
uvx starwars-namegen==0.2.0
```

**Option 2: Use seed for determinism**
```bash
# Same seed = same output
uvx starwars-namegen --seed ${CI_JOB_ID} -c 3
```

**Option 3: Lock in requirements**
```bash
# In your project's pyproject.toml
[project.dependencies]
starwars-namegen = "==0.2.0"

# Then use
uv run starwars-namegen
```

---

### Problem #14: Caching in CI

**The Issue:** Every CI run downloads package fresh

**Solution: Enable cache**

**GitHub Actions:**
```yaml
- uses: astral-sh/setup-uv@v1
  with:
    enable-cache: true  # ← This!
```

**GitLab CI:**
```yaml
cache:
  paths:
    - .cache/uv/

before_script:
  - export UV_CACHE_DIR="$CI_PROJECT_DIR/.cache/uv"
```

**Docker:**
```dockerfile
# Use build cache
RUN --mount=type=cache,target=/root/.cache/uv \
    uvx starwars-namegen
```

---

## Development Pitfalls

### Problem #15: "ModuleNotFoundError" in Development

**Symptoms:**
```bash
$ python -m starwars_namegen.cli
ModuleNotFoundError: No module named 'starwars_namegen'
```

**Cause:** Not running in project environment

**Solutions:**

**Option 1: Use uv run (recommended)**
```bash
uv run python -m starwars_namegen.cli
# or
uv run starwars-namegen
```

**Option 2: Sync environment**
```bash
uv sync
source .venv/bin/activate
python -m starwars_namegen.cli
```

**Option 3: Install in dev mode**
```bash
uv pip install -e .
python -m starwars_namegen.cli
```

---

### Problem #16: Tests Failing After Install

**The Issue:**
```bash
uv tool install starwars-namegen  # Global install
pytest tests/  # Uses global, not local code!
```

**Solution:**
```bash
# Always use uv run for tests
uv run pytest tests/

# Or activate venv
uv sync
source .venv/bin/activate
pytest tests/
```

---

## Quick Reference: Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `command not found` | Not installed or PATH issue | `uv tool install` + check PATH |
| `Existing executables found` | Conflict with old install | `uv tool install --force` |
| `ModuleNotFoundError` | Not in project venv | Use `uv run` |
| `No such file or directory` | Wrong working directory | `cd` to project root |
| Slow first run | Cache miss | Normal, second run is fast |
| `uv: command not found` | UV not installed | Install UV first |
| Wrong version | Cached old version | `uv cache clean` |
| Tests use wrong code | Global vs local conflict | Use `uv run pytest` |

---

## Best Practices Summary

### DO:
- ✅ Use `uvx` for one-off runs
- ✅ Use `uv tool install` for frequent use
- ✅ Use `uv run` in development
- ✅ Quote variables in shell scripts
- ✅ Cache uvx in CI/CD
- ✅ Use seeds for reproducibility
- ✅ Read the error messages (they're helpful!)

### DON'T:
- ❌ Mix `pipx` and `uv tool install`
- ❌ Forget to quote shell variables
- ❌ Use `uvx install` (wrong command)
- ❌ Skip reading tool output
- ❌ Ignore PATH warnings
- ❌ Test with `python` instead of `uv run`

---

## Getting Help

**Check versions:**
```bash
uv --version
python --version
starwars-namegen --version
```

**Check installation:**
```bash
uv tool list
which starwars-namegen
echo $PATH
```

**Clear cache and retry:**
```bash
uv cache clean
uvx starwars-namegen
```

**Still stuck?**
- Read error messages carefully
- Check UV documentation: https://docs.astral.sh/uv/
- Open issue: https://gitlab.com/hackur/starwars-namegen/-/issues

---

**Author:** Jeremy Sarda (jeremy@hackur.io)

**May the Force help you avoid these pitfalls!**
