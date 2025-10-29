# PUBLISHING TO PYPI: The Complete Guide

> *"This is where the fun begins."* - Anakin Skywalker

**Project**: Star Wars Name Generator
**Author**: Jeremy Sarda (jeremy@hackur.io)
**Current Version**: 0.3.0
**PyPI Package**: `starwars-namegen`

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [PyPI Account Setup](#pypi-account-setup)
3. [Publishing Methods](#publishing-methods)
4. [Step-by-Step: First Publication](#step-by-step-first-publication)
5. [Step-by-Step: Subsequent Releases](#step-by-step-subsequent-releases)
6. [Verification & Testing](#verification--testing)
7. [Troubleshooting](#troubleshooting)
8. [Automation with GitHub Actions](#automation-with-github-actions)

---

## Prerequisites

### What You Need

- [x] PyPI account (https://pypi.org)
- [x] 2FA enabled on PyPI account
- [x] Package built locally (`uv build`)
- [x] All tests passing (`uv run pytest`)
- [x] Version bumped in `pyproject.toml` and `__init__.py`
- [x] Git changes committed

### Check Your Build

```bash
# Verify package is built
ls -lh dist/
# Should show:
# starwars_namegen-0.3.0-py3-none-any.whl
# starwars_namegen-0.3.0.tar.gz

# Verify version
grep 'version = ' pyproject.toml
grep '__version__ = ' src/starwars_namegen/__init__.py
# Both should show: 0.3.0

# Verify tests pass
uv run pytest
# Should show: 95 passed
```

---

## PyPI Account Setup

### Your Account Details

- **Username**: `sarda` (or your PyPI username)
- **Email**: `jeremy@hackur.io`
- **2FA**: ✅ Enabled (recommended!)
- **Account URL**: https://pypi.org/user/sarda/

### Security: Why API Tokens > Passwords

**DON'T** use your password for publishing! Use API tokens instead:

- ✅ Tokens can be revoked without changing password
- ✅ Tokens can be scoped to specific projects
- ✅ Tokens work with 2FA enabled accounts
- ✅ Tokens can be rotated regularly for security

---

## Publishing Methods

### Method 1: Manual Publishing with API Token (Recommended for First Time)

**Best for**: First publication, testing, one-off releases

**Steps**:
1. Create API token on PyPI
2. Set token as environment variable
3. Run `uv publish`

### Method 2: Trusted Publishing with GitHub Actions (Best for Production)

**Best for**: Automated releases, team projects, ongoing maintenance

**Steps**:
1. Configure trusted publisher on PyPI
2. Create GitHub Actions workflow
3. Push git tag to trigger release

### Method 3: Using dev.sh Script

**Best for**: Quick releases after initial setup

**Steps**:
```bash
./dev.sh publish
```

---

## Step-by-Step: First Publication

### Step 1: Create API Token

1. **Go to PyPI Token Management**
   ```
   https://pypi.org/manage/account/token/
   ```

2. **Click "Add API token"**

3. **Configure Token**:
   - **Token name**: `starwars-namegen-publish`
   - **Scope**:
     - For first publication: "Entire account" (required - project doesn't exist yet)
     - For updates: "Project: starwars-namegen" (more secure)

   ![Token Scope](https://i.imgur.com/pypi-token-scope.png)

4. **Copy the Token**
   ```
   pypi-AgEIcHlwaS5vcmcCJDAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDAwMDAwMDAwMAACKlszLCJmNWY...
   ```

   ⚠️ **IMPORTANT**: Copy it now! You can't see it again!

5. **Save Token Securely**
   ```bash
   # Option A: Save to password manager (recommended)
   # 1Password, Bitwarden, LastPass, etc.

   # Option B: Save to file (for this session only)
   echo "export UV_PUBLISH_TOKEN='pypi-YOUR_TOKEN_HERE'" > ~/.pypi-token
   chmod 600 ~/.pypi-token  # Protect the file
   ```

### Step 2: Set Environment Variable

```bash
# Load token from secure storage
export UV_PUBLISH_TOKEN="pypi-AgEIcHlwaS5vcmcCJDAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDAwMDAwMDAwMAACKlszLCJmNWY..."

# Verify it's set (shows first few chars only for safety)
echo ${UV_PUBLISH_TOKEN:0:20}...
# Should show: pypi-AgEIcHlwaS5vcmc...
```

### Step 3: Pre-Publication Checklist

```bash
# ✅ Clean build directory
rm -rf dist/
uv build

# ✅ Verify package contents
tar -tzf dist/starwars_namegen-0.3.0.tar.gz | head -20

# ✅ Test installation locally
uv tool install dist/starwars_namegen-0.3.0-py3-none-any.whl --force
starwars-namegen --version
# Should show: 0.3.0

# ✅ Run full test suite
uv run pytest

# ✅ Check package metadata
python -c "import tomli; print(tomli.load(open('pyproject.toml', 'rb'))['project'])"
```

### Step 4: Publish to PyPI

```bash
# Publish!
uv publish

# You should see:
# Uploading starwars_namegen-0.3.0-py3-none-any.whl
# Uploading starwars_namegen-0.3.0.tar.gz
# ✓ Successfully published to https://pypi.org/project/starwars-namegen/0.3.0/
```

### Step 5: Verify Publication

```bash
# Check on PyPI
open https://pypi.org/project/starwars-namegen/

# Test installation with uvx (the whole point!)
uvx starwars-namegen --version
# Should show: 0.3.0

# Test functionality
uvx starwars-namegen -c 5 -m 10
# Should generate 10 5-word Star Wars names!
```

### Step 6: Create More Secure Token (After First Publish)

Now that the project exists on PyPI, create a project-scoped token:

1. Go to https://pypi.org/manage/account/token/
2. Create new token:
   - **Name**: `starwars-namegen-updates`
   - **Scope**: "Project: starwars-namegen" ✅ (more secure!)
3. Update your environment variable with the new token
4. Delete the old "entire account" token

---

## Step-by-Step: Subsequent Releases

For releases after the first publication:

### Quick Release Process

```bash
# 1. Update code and tests
# ... make your changes ...

# 2. Run tests
uv run pytest

# 3. Update version
# Edit pyproject.toml: version = "0.3.1"
# Edit src/starwars_namegen/__init__.py: __version__ = "0.3.1"

# 4. Update CHANGELOG
cat >> CHANGELOG.md << EOF

## [0.3.1] - $(date +%Y-%m-%d)

### Added
- New feature X
- Improved Y

### Fixed
- Bug Z
EOF

# 5. Commit changes
git add .
git commit -m "chore: bump version to 0.3.1"
git tag v0.3.1
git push origin main --tags

# 6. Build
rm -rf dist/
uv build

# 7. Publish
export UV_PUBLISH_TOKEN="pypi-YOUR_PROJECT_SCOPED_TOKEN"
uv publish

# 8. Verify
uvx starwars-namegen@latest --version
```

### Using dev.sh for Releases

```bash
# Build
./dev.sh build

# Publish (will prompt for confirmation)
./dev.sh publish
```

---

## Verification & Testing

### Immediate Checks After Publishing

```bash
# 1. Check PyPI page
open https://pypi.org/project/starwars-namegen/

# 2. Test with uvx (ephemeral)
uvx starwars-namegen --version
uvx starwars-namegen -c 3 -m 5

# 3. Test with uv tool install (persistent)
uv tool install starwars-namegen
starwars-namegen --help

# 4. Test specific version
uvx starwars-namegen==0.3.0 --version

# 5. Check package metadata
pip show starwars-namegen  # If you have pip installed
```

### Integration Testing

```bash
# Test in a fresh environment
docker run --rm -it python:3.13-slim bash
# Inside container:
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.cargo/bin:$PATH"
uvx starwars-namegen -c 5 -m 10
```

---

## Troubleshooting

### Issue: "Missing credentials"

```bash
# Error
error: Failed to publish to https://upload.pypi.org/legacy/
  Caused by: Missing credentials

# Solution
export UV_PUBLISH_TOKEN="pypi-YOUR_TOKEN_HERE"
# Make sure no extra quotes or spaces!
```

### Issue: "File already exists"

```bash
# Error
error: File already exists: starwars_namegen-0.3.0-py3-none-any.whl

# Cause: You can't re-upload the same version

# Solution: Bump version
# Edit pyproject.toml: version = "0.3.1"
# Edit __init__.py: __version__ = "0.3.1"
uv build
uv publish
```

### Issue: "Invalid token"

```bash
# Error
error: 403 Client Error: Invalid or non-existent authentication information

# Solutions:
# 1. Check token is complete (they're very long!)
echo $UV_PUBLISH_TOKEN | wc -c  # Should be 200+ characters

# 2. Check for extra quotes
export UV_PUBLISH_TOKEN=pypi-...  # ✅ No quotes
export UV_PUBLISH_TOKEN="pypi-..." # ✅ Double quotes ok
export UV_PUBLISH_TOKEN='pypi-...' # ✅ Single quotes ok
export UV_PUBLISH_TOKEN='pypi-...'  # ❌ Extra space before!

# 3. Generate new token if expired
```

### Issue: Package not appearing immediately

```bash
# PyPI can take 1-2 minutes to index new packages

# Check status
curl -I https://pypi.org/project/starwars-namegen/

# If 404, wait a minute and try again
# If 200, it's published!
```

---

## Automation with GitHub Actions

### Setup Trusted Publishing (Most Secure - 2025 Recommended)

**Why Trusted Publishing?**
- ✅ No API tokens to manage
- ✅ No secrets to store
- ✅ Uses OpenID Connect (OIDC)
- ✅ Automatic authentication
- ✅ Audit trail built-in

### Step 1: Configure PyPI Trusted Publisher

1. **Go to PyPI Publishing Settings**
   ```
   https://pypi.org/manage/project/starwars-namegen/settings/publishing/
   ```

2. **Add Trusted Publisher**
   - **Owner**: `your-github-username` (or `hackur` if org)
   - **Repository**: `starwars-namegen`
   - **Workflow name**: `publish.yml`
   - **Environment name**: `pypi` (optional but recommended)

3. **Save**

### Step 2: Create GitHub Actions Workflow

```yaml
# .github/workflows/publish.yml
name: Publish to PyPI

on:
  push:
    tags:
      - 'v*.*.*'  # Trigger on version tags like v0.3.0

jobs:
  publish:
    name: Publish to PyPI
    runs-on: ubuntu-latest

    # If you configured environment in PyPI
    environment:
      name: pypi
      url: https://pypi.org/project/starwars-namegen/

    # Required for trusted publishing
    permissions:
      id-token: write
      contents: read

    steps:
      - name: Checkout code
        uses: actions/checkout@v5

      - name: Install UV
        uses: astral-sh/setup-uv@v7

      - name: Set up Python
        run: uv python install 3.13

      - name: Install dependencies
        run: uv sync --all-extras

      - name: Run tests
        run: uv run pytest

      - name: Build package
        run: uv build

      - name: Publish to PyPI
        run: uv publish
        # No token needed! Trusted publishing handles it!
```

### Step 3: Release Process with GitHub Actions

```bash
# 1. Make your changes, commit
git add .
git commit -m "feat: add awesome feature"

# 2. Bump version in pyproject.toml and __init__.py
# version = "0.3.1"

# 3. Commit version bump
git add .
git commit -m "chore: bump version to 0.3.1"

# 4. Create and push tag
git tag v0.3.1
git push origin main
git push origin v0.3.1

# 5. GitHub Actions automatically:
#    - Runs tests
#    - Builds package
#    - Publishes to PyPI
#
# Check progress at:
# https://github.com/your-username/starwars-namegen/actions
```

---

## Security Best Practices

### DO ✅

- Use API tokens, not passwords
- Use project-scoped tokens (after first publish)
- Store tokens in password manager
- Use trusted publishing for automation
- Rotate tokens every 6-12 months
- Enable 2FA on PyPI account
- Use GitHub secrets for CI/CD

### DON'T ❌

- Commit tokens to git
- Share tokens in chat/email
- Use same token for multiple projects
- Use "entire account" tokens in production
- Store tokens in plain text files
- Disable 2FA

---

## Current Status

### Your Package Information

- **Package Name**: `starwars-namegen`
- **Latest Version**: `0.3.0`
- **PyPI URL**: https://pypi.org/project/starwars-namegen/ (after publishing)
- **Install Command**: `uvx starwars-namegen`
- **Repository**: https://gitlab.com/hackur/starwars-namegen

### Publication Checklist

Before publishing v0.3.0:

- [x] Version bumped to 0.3.0
- [x] All tests passing (95/95)
- [x] Package built (`dist/` contains .whl and .tar.gz)
- [x] Git changes committed
- [ ] API token created on PyPI
- [ ] Token set as UV_PUBLISH_TOKEN
- [ ] `uv publish` executed
- [ ] Package verified on PyPI
- [ ] `uvx starwars-namegen` tested

### Next Steps

1. **Create PyPI API token** (5 minutes)
   - Visit https://pypi.org/manage/account/token/
   - Create token named `starwars-namegen-publish`
   - Scope: "Entire account" (for first publish)
   - Copy token immediately

2. **Publish** (2 minutes)
   ```bash
   export UV_PUBLISH_TOKEN="pypi-YOUR_TOKEN_HERE"
   uv publish
   ```

3. **Verify** (1 minute)
   ```bash
   uvx starwars-namegen -c 5 -m 10
   ```

4. **Celebrate!** 🎉
   Your package is now available to the entire Python community!

---

## Quick Reference

### Environment Variables

```bash
# Required for publishing
export UV_PUBLISH_TOKEN="pypi-..."

# Optional: specify different index
export UV_INDEX_URL="https://test.pypi.org/legacy/"
```

### Common Commands

```bash
# Build package
uv build

# Publish to PyPI
uv publish

# Publish to Test PyPI (for testing)
uv publish --index-url https://test.pypi.org/legacy/

# Test installation
uvx starwars-namegen
uvx --from starwars-namegen starwars-namegen --help

# Install globally
uv tool install starwars-namegen
```

---

## Support

### Getting Help

- **UV Documentation**: https://docs.astral.sh/uv/
- **PyPI Help**: https://pypi.org/help/
- **Issue Tracker**: https://gitlab.com/hackur/starwars-namegen/-/issues

### Contact

- **Author**: Jeremy Sarda
- **Email**: jeremy@hackur.io
- **GitLab**: https://gitlab.com/hackur

---

**May the Force be with your publishing!** 🚀

*Last Updated*: 2025
*Document Version*: 1.0
*Status*: Ready for Publication
