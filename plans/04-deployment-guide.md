# Deployment Protocol: Weapon Systems Authorization

**Project Designation:** STARWARS-NAMEGEN v0.1.0
**Deployment Classification:** PHASE I - INITIAL STRIKE CAPABILITY
**Authorization:** Imperial High Command
**Deployment Date:** 2025-10-28

---

## Mission Brief

This document outlines the complete deployment sequence for establishing the Star Wars Name Generator as a fully operational uvx-compatible weapon system. This tool is designed for galaxy-wide deployment across all development stations, enabling instant tactical designation of resources without the need for permanent installation in local systems.

**Strategic Objective:** Deploy a zero-configuration, instant-execution naming platform accessible to all forces equipped with the `uv` universal package manager.

---

## Phase I: Local Build & Verification

### Objective: Construct the Battle Station Core

This phase establishes the foundational build artifacts required for all deployment scenarios.

#### Step 1: Activate Build Systems

```bash
# Navigate to command center
cd /Users/sarda/Downloads/star-wars-name-generator-uvx

# Initialize tactical build sequence
uv build
```

**Expected Output:**
```
Building source distribution...
Building wheel...
Successfully built starwars_namegen-0.1.0.tar.gz and starwars_namegen-0.1.0-py3-none-any.whl
```

**Mission-Critical Verification:**
- [ ] Build completes without errors
- [ ] Two artifacts generated in `dist/` directory:
  - `starwars_namegen-0.1.0.tar.gz` (source distribution - sdist)
  - `starwars_namegen-0.1.0-py3-none-any.whl` (wheel distribution - bdist)
- [ ] Wheel is "pure Python" (py3-none-any indicates cross-platform capability)
- [ ] No dependency resolution failures

**Tactical Analysis:**
```bash
# Inspect build artifacts
ls -lh dist/

# Expected structure:
# -rw-r--r--  starwars_namegen-0.1.0-py3-none-any.whl (~ 10-15 KB)
# -rw-r--r--  starwars_namegen-0.1.0.tar.gz (~ 8-12 KB)
```

#### Step 2: Local Installation Testing (Operation Home Base)

**Mission:** Establish weapon system in local command post

```bash
# Deploy to local tool arsenal
uv tool install .

# Alternative: Install from built wheel
uv tool install dist/starwars_namegen-0.1.0-py3-none-any.whl
```

**Expected Outcomes:**
```
Installed starwars-namegen 0.1.0
 + click 8.1.7
 + inflect 7.0.0
```

**Verification Protocol:**
```bash
# Verify command accessibility
which starwars-namegen
# Expected: /Users/[username]/.local/bin/starwars-namegen (or similar)

# Execute weapon test
starwars-namegen
# Expected: Single generated name (e.g., "galactic-trooper")

# Full diagnostic scan
starwars-namegen --help
starwars-namegen --version
starwars-namegen -c 3 -f snake --random hex
```

**Status Check:**
- [ ] Command found in PATH
- [ ] Execution successful (< 500ms response)
- [ ] Help system operational
- [ ] Version reporting accurate
- [ ] All tactical options functional

#### Step 3: Primary Mission Test - uvx Deployment

**Critical Capability:** Execute without installation

```bash
# Uninstall local copy (to simulate clean environment)
uv tool uninstall starwars-namegen

# Execute via uvx (this is the PRIMARY deployment method)
uvx --from . starwars-namegen

# Expected: Immediate execution without prior installation
```

**Why This Matters:**
- uvx is the ultimate deployment vector for maximum reach
- Zero installation friction
- Automatic dependency management
- Isolated execution environment
- Users can run tool instantly without commitment

**Full uvx Battle Test:**
```bash
# Test all combat scenarios
uvx --from . starwars-namegen -c 3
uvx --from . starwars-namegen -f snake
uvx --from . starwars-namegen --random digits
uvx --from . starwars-namegen -m 5 --seed 42
```

---

## Phase II: PyPI Deployment (Galaxy-Wide Distribution)

### Objective: Broadcast Weapon System Across All Star Systems

**Security Clearance Required:** PyPI API Token

### Step 1: Secure Communications Channel (API Token)

**Procedure:**
1. Navigate to PyPI Command Center: https://pypi.org/
2. Authenticate with credentials
3. Access Account Settings → API Tokens
4. Generate new token:
   - Token name: `starwars-namegen-deployment`
   - Scope: `Entire Account` (for first deployment) or `Project: starwars-namegen` (for updates)
5. **IMMEDIATELY** copy token (format: `pypi-AgEIcHlwaS5vcmc...`)
6. Store in secure vault (password manager)

**Token Security Protocol:**
- ❌ NEVER commit to version control
- ❌ NEVER share in communications
- ❌ NEVER hardcode in scripts
- ✅ Store in environment variables
- ✅ Use secure credential management
- ✅ Rotate periodically

### Step 2: Test PyPI Reconnaissance Mission (RECOMMENDED)

**Objective:** Validate deployment procedures in test environment

**Target:** https://test.pypi.org/

**Why Test First:**
- Non-destructive validation
- Catch deployment errors before production
- Verify package metadata rendering
- Confirm README displays correctly
- No risk to production namespace

**Execution:**
```bash
# Establish test communications
export UV_PUBLISH_TOKEN="pypi-YOUR_TEST_PYPI_TOKEN_HERE"

# Deploy to test facility
uv publish --publish-url https://test.pypi.org/legacy/

# Verification scan
# Visit: https://test.pypi.org/project/starwars-namegen/
```

**Inspection Checklist:**
- [ ] Package appears on TestPyPI
- [ ] Version number correct (0.1.0)
- [ ] README renders properly (markdown formatting)
- [ ] All classifiers present
- [ ] Dependencies listed correctly
- [ ] Download files available (wheel + sdist)
- [ ] Project URLs functional

**Test Installation from TestPyPI:**
```bash
# Deploy from test facility to local station
uvx --from https://test.pypi.org/simple/ starwars-namegen

# Full operational test
uvx --from https://test.pypi.org/simple/ starwars-namegen -c 3 -f snake
```

**Abort Criteria:**
- Dependency resolution failures
- Missing/broken imports
- CLI not executable
- Incorrect version display
- Runtime errors

**If Aborted:** Return to Phase I, fix issues, rebuild, retry test deployment.

### Step 3: Production Deployment (The Real Deal)

**⚠️ POINT OF NO RETURN - Once deployed to PyPI, versions are PERMANENT**

**Pre-Flight Checklist:**
- [ ] All tests passing (Phase I complete)
- [ ] TestPyPI deployment successful (if performed)
- [ ] Git repository committed and tagged
- [ ] CHANGELOG.md updated
- [ ] README.md finalized
- [ ] Version number confirmed in pyproject.toml and __init__.py
- [ ] Production PyPI token secured
- [ ] Cleared for deployment by mission command

**Deployment Sequence:**
```bash
# Set production credentials
export UV_PUBLISH_TOKEN="pypi-YOUR_PRODUCTION_TOKEN_HERE"

# Initiate production deployment
uv publish

# Monitor for confirmation
```

**Expected Output:**
```
Uploading starwars_namegen-0.1.0.tar.gz
Uploading starwars_namegen-0.1.0-py3-none-any.whl
Successfully uploaded starwars_namegen-0.1.0
```

**Immediate Post-Deployment Actions:**
1. **Verify on PyPI:**
   - URL: https://pypi.org/project/starwars-namegen/
   - Check version, description, classifiers
   - Verify README rendering
   - Test download links

2. **Test Global Installation:**
```bash
# On clean system or new terminal session
uvx starwars-namegen

# Expected: Automatic download, installation, and execution
```

3. **Announce Deployment:**
   - Update GitHub repository with PyPI badge
   - Tag release in git
   - Notify stakeholders

**Git Tagging Protocol:**
```bash
# Tag the release
git tag -a v0.1.0 -m "Release version 0.1.0 - Initial deployment"

# Push tags to remote
git push origin v0.1.0

# Push all tags
git push --tags
```

---

## Phase III: Field Deployment Scenarios

### Scenario Alpha: Developer Workstation

**Objective:** Enable instant usage without installation

**User Command:**
```bash
uvx starwars-namegen
```

**What Happens:**
1. `uv` checks if package exists in cache
2. If not, downloads from PyPI
3. Creates isolated environment
4. Installs dependencies (click, inflect)
5. Executes starwars-namegen
6. **Total time: 2-5 seconds on first run, < 1 second on subsequent runs**

**User Experience:**
- No manual installation required
- No virtual environment setup needed
- No PATH configuration necessary
- Works immediately
- Cached for speed on repeat usage

### Scenario Bravo: CI/CD Pipeline Integration

**Objective:** Generate resource names in automated workflows

**GitHub Actions Example:**
```yaml
name: Generate Resource Names
on: [push]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Install uv
        run: curl -LsSf https://astral.sh/uv/install.sh | sh

      - name: Generate deployment name
        run: |
          NAME=$(uvx starwars-namegen -c 3 --random hex)
          echo "DEPLOYMENT_NAME=$NAME" >> $GITHUB_ENV

      - name: Deploy with generated name
        run: |
          echo "Deploying to: $DEPLOYMENT_NAME"
          # Actual deployment commands here
```

### Scenario Charlie: Docker Container Naming

**Objective:** Dynamic container naming in scripts

```bash
#!/bin/bash
# deploy-containers.sh

# Generate unique container names
for i in {1..5}; do
    CONTAINER_NAME=$(uvx starwars-namegen --random digits)
    docker run -d --name "$CONTAINER_NAME" myimage:latest
    echo "Deployed container: $CONTAINER_NAME"
done
```

### Scenario Delta: Infrastructure as Code

**Terraform Example:**
```hcl
# Use external data source to generate names
data "external" "server_name" {
  program = ["uvx", "starwars-namegen", "-c", "3", "--random", "hex"]
}

resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  tags = {
    Name = data.external.server_name.result.output
  }
}
```

---

## Phase IV: Maintenance & Updates

### Deploying Version 0.2.0 (Future Operations)

**Procedure:**

1. **Update Version Numbers:**
```toml
# pyproject.toml
version = "0.2.0"
```

```python
# src/starwars_namegen/__init__.py
__version__ = "0.2.0"
```

2. **Update CHANGELOG.md:**
```markdown
## [0.2.0] - 2025-11-15

### Added
- New feature X
- Enhanced feature Y

### Fixed
- Bug in Z

### Changed
- Improved performance of Q
```

3. **Commit and Tag:**
```bash
git add .
git commit -m "Release v0.2.0"
git tag -a v0.2.0 -m "Release version 0.2.0"
git push && git push --tags
```

4. **Rebuild and Deploy:**
```bash
# Clean previous build
rm -rf dist/

# Build new version
uv build

# Test locally
uv tool install --force dist/starwars_namegen-0.2.0-py3-none-any.whl

# Deploy to PyPI
uv publish --token pypi-YOUR_TOKEN
```

### User Upgrade Path

**Automatic (uvx):**
```bash
# uvx always uses latest version by default
uvx starwars-namegen  # Automatically uses 0.2.0 after deployment
```

**Explicit (uv tool):**
```bash
# Upgrade installed tool
uv tool upgrade starwars-namegen

# Or reinstall
uv tool install --force starwars-namegen
```

---

## Phase V: Troubleshooting & Battle Damage Assessment

### Issue Alpha: Command Not Found After Install

**Symptoms:**
```bash
starwars-namegen
# bash: starwars-namegen: command not found
```

**Diagnosis:** PATH misconfiguration

**Solution:**
```bash
# Update shell PATH
uv tool update-shell

# Reload shell configuration
source ~/.zshrc  # or ~/.bashrc

# Verify PATH includes uv tool directory
echo $PATH | grep .local/bin
```

### Issue Bravo: Import Errors on Execution

**Symptoms:**
```
ModuleNotFoundError: No module named 'click'
```

**Diagnosis:** Dependency installation failure

**Solution:**
```bash
# Reinstall with verbose output
uv tool uninstall starwars-namegen
uv tool install starwars-namegen --verbose

# Check dependency resolution
uv pip list
```

### Issue Charlie: Version Mismatch

**Symptoms:**
```bash
starwars-namegen --version
# starwars-namegen, version 0.1.0
# (Expected: 0.2.0)
```

**Diagnosis:** Cached old version

**Solution:**
```bash
# Force upgrade
uv tool upgrade starwars-namegen

# Or clear cache and reinstall
uv cache clean
uv tool install starwars-namegen
```

### Issue Delta: uvx Downloads Every Time

**Symptoms:** Slow execution, downloading dependencies repeatedly

**Diagnosis:** Cache not working properly

**Solution:**
```bash
# Check cache status
uv cache dir

# Verify cached packages
ls -la $(uv cache dir)

# Pre-cache the package
uvx --from starwars-namegen@latest starwars-namegen
```

### Issue Echo: PyPI Upload Fails

**Symptoms:**
```
403 Forbidden: Invalid or insufficient permissions
```

**Diagnosis:** Token authentication failure

**Solutions:**
1. **Verify token is correct:**
```bash
echo $UV_PUBLISH_TOKEN  # Should show token
```

2. **Check token scope:**
   - Must have upload permissions
   - If project-scoped, package must already exist

3. **Regenerate token:**
   - Go to PyPI → Account Settings → API Tokens
   - Delete old token
   - Create new token
   - Update environment variable

---

## Phase VI: Operational Metrics

### Success Indicators

**Deployment Success:**
- [ ] Package available on PyPI
- [ ] `uvx starwars-namegen` works globally
- [ ] Documentation accessible
- [ ] Version correct across all platforms
- [ ] Dependencies auto-install
- [ ] No reported critical bugs

**Adoption Metrics (Monitor Post-Launch):**
- PyPI download statistics
- GitHub stars/forks
- Issue reports
- Pull requests
- Community engagement

### Performance Benchmarks

**Target Metrics:**
- First-time uvx execution: < 5 seconds (includes download)
- Cached uvx execution: < 1 second
- Name generation: < 10ms
- Batch generation (100 names): < 500ms
- Memory footprint: < 30MB
- Package size: < 20KB (wheel)

---

## Phase VII: Decommissioning (Emergency Procedures)

### Package Yanking (EMERGENCY ONLY)

**Use Cases:**
- Critical security vulnerability discovered
- Catastrophic bug causing data loss
- Malicious code detected

**Procedure:**
```bash
# Via PyPI web interface:
# 1. Login to PyPI
# 2. Navigate to Releases
# 3. Select version
# 4. Click "Yank version"
# 5. Provide reason

# Note: Yanked versions are NOT deleted
# They remain visible but with warning
# Users can still explicitly install yanked versions
```

**⚠️ YANKING IS NOT DELETION:**
- Package remains visible on PyPI
- Downloads show "yanked" warning
- Does not affect already-installed copies
- Cannot be undone
- Should be followed by fixed release

---

## Final Deployment Authorization

**Deployment Readiness Certification:**

```
WEAPON SYSTEM: starwars-namegen v0.1.0
DEPLOYMENT STATUS: [ ] AUTHORIZED / [ ] DENIED

PRE-FLIGHT CHECKS:
[ ] Build successful
[ ] Local installation verified
[ ] uvx execution confirmed
[ ] All tests passing
[ ] Documentation complete
[ ] PyPI token secured
[ ] Git repository tagged
[ ] CHANGELOG updated

DEPLOYMENT COMMANDER: ____________________
SIGNATURE: ____________________
DATE: ____________________
TIME: ____________________

AUTHORIZATION CODE: ____________________

---TRANSMISSION ENDS---
```

**May the Force be with our deployment.**

---

**Document Classification:** OPERATIONAL - FOR DEPLOYMENT USE ONLY
**Version:** 1.0
**Last Updated:** 2025-10-28
**Distribution:** All Deployment Engineers
**Security Level:** CONFIDENTIAL

**Remember:** This is not just a simple Python package. This is a precision tool delivery system leveraging the full power of modern Python packaging (`pyproject.toml`), the uv ecosystem (managed dependencies, virtual environments, tool isolation), and instant deployment capabilities (uvx). It demonstrates the complete lifecycle from local development to galaxy-wide distribution.
