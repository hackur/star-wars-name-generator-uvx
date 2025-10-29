#!/usr/bin/env bash
# dev.sh - Death Star Command Console
# Your mission control for developing with UV
#
# May the Force be with your development workflow!

set -euo pipefail

# Colors (HUD Interface)
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Death Star ASCII Art
show_banner() {
    echo -e "${CYAN}"
    cat << 'EOF'
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀
    ⠀⠀⣰⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀
    ⠀⣰⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀
    ⢠⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⡄⠀
    ⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠀
    ⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠀
    ⢿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⡿⠀
    ⠸⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⠇⠀
    ⠀⢹⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀
    ⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀
    ⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣤⣤⣤⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀
    ⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀

    ╔═══════════════════════════════════════════════════════════╗
    ║    DEATH STAR COMMAND CONSOLE - UV Development Suite     ║
    ║                   May the Force be with you              ║
    ╚═══════════════════════════════════════════════════════════╝
EOF
    echo -e "${NC}"
}

# Logging functions
log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[✓]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[!]${NC} $1"
}

log_error() {
    echo -e "${RED}[✗]${NC} $1"
}

log_section() {
    echo -e "\n${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${CYAN}  $1${NC}"
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}\n"
}

# Check if UV is installed
check_uv() {
    if ! command -v uv &> /dev/null; then
        log_error "UV not found! Installing..."
        curl -LsSf https://astral.sh/uv/install.sh | sh
        log_success "UV installed successfully!"
    else
        log_success "UV is operational ($(uv --version))"
    fi
}

# Main commands

cmd_setup() {
    log_section "🚀 Initializing Death Star Systems"
    check_uv
    log_info "Syncing project dependencies..."
    uv sync --all-extras
    log_success "All systems operational!"
}

cmd_test() {
    log_section "🎯 Running Tactical Simulations (Tests)"
    log_info "Executing test suite..."
    uv run pytest "${@:2}" || {
        log_error "Tests failed! The rebellion has caused problems!"
        exit 1
    }
    log_success "All systems passing! Ready for deployment!"
}

cmd_test_all() {
    log_section "🔬 Full Spectrum Analysis (All Python Versions)"
    local versions=("3.9" "3.10" "3.11" "3.12" "3.13")

    for version in "${versions[@]}"; do
        log_info "Testing with Python ${version}..."
        uv run --python "${version}" pytest || {
            log_warning "Tests failed for Python ${version}"
        }
    done
    log_success "Multi-version testing complete!"
}

cmd_lint() {
    log_section "🔍 Code Analysis (Scanning for Rebels)"
    log_info "Running Ruff linter..."
    uv run ruff check src tests
    log_success "Code analysis complete!"
}

cmd_format() {
    log_section "✨ Code Formatting (Aligning TIE Fighters)"
    log_info "Formatting code with Ruff..."
    uv run ruff format src tests
    log_success "Code formatted to Imperial standards!"
}

cmd_typecheck() {
    log_section "🔬 Type Analysis (Verifying Schematics)"
    log_info "Running MyPy type checker..."
    uv run mypy src
    log_success "Type checking complete!"
}

cmd_coverage() {
    log_section "📊 Coverage Report (Shield Integrity)"
    log_info "Generating coverage report..."
    uv run pytest --cov=starwars_namegen --cov-report=html --cov-report=term
    log_success "Coverage report generated at: htmlcov/index.html"
    log_info "Opening coverage report..."
    open htmlcov/index.html 2>/dev/null || xdg-open htmlcov/index.html 2>/dev/null || true
}

cmd_run() {
    log_section "⚡ Execute Command"
    log_info "Running: starwars-namegen ${*:2}"
    uv run starwars-namegen "${@:2}"
}

cmd_demo() {
    log_section "🎬 Death Star Demonstration"
    log_info "Generating name examples..."

    echo -e "${CYAN}Single Name:${NC}"
    uv run starwars-namegen

    echo -e "\n${CYAN}5-Word Story Names:${NC}"
    uv run starwars-namegen -c 5 -m 10

    echo -e "\n${CYAN}With UUID Suffix:${NC}"
    uv run starwars-namegen -c 3 --random uuid -m 5

    echo -e "\n${CYAN}Different Formats:${NC}"
    uv run starwars-namegen -c 3 -f snake
    uv run starwars-namegen -c 3 -f camel
    uv run starwars-namegen -c 3 -f pascal

    log_success "Demonstration complete!"
}

cmd_build() {
    log_section "🏗️  Building Death Star (Package Build)"
    log_info "Cleaning previous builds..."
    rm -rf dist/ build/ *.egg-info

    log_info "Building package..."
    uv build

    log_success "Package built successfully!"
    echo -e "${CYAN}Artifacts:${NC}"
    ls -lh dist/
}

cmd_publish_test() {
    log_section "🧪 Test Deployment (TestPyPI)"
    log_info "Publishing to TestPyPI..."
    log_warning "Make sure UV_PUBLISH_TOKEN is set!"

    uv publish --index-url https://test.pypi.org/legacy/

    log_success "Published to TestPyPI!"
    log_info "Test with: uvx --index-url https://test.pypi.org/simple/ starwars-namegen"
}

cmd_publish() {
    log_section "🚀 Production Deployment (PyPI)"
    log_warning "This will publish to production PyPI!"
    read -p "Are you sure? (yes/no): " confirm

    if [[ "$confirm" != "yes" ]]; then
        log_error "Deployment aborted!"
        exit 1
    fi

    log_info "Publishing to PyPI..."
    uv publish

    log_success "Successfully deployed to PyPI!"
    log_info "Test with: uvx starwars-namegen"
}

cmd_version() {
    log_section "📦 Version Management"

    if [[ -z "${2:-}" ]]; then
        log_error "Usage: ./dev.sh version <bump-type>"
        log_info "Bump types: patch, minor, major, alpha, beta, rc"
        exit 1
    fi

    local bump_type="$2"
    log_info "Bumping $bump_type version..."

    uv version --bump "$bump_type"

    local new_version=$(grep '^version = ' pyproject.toml | cut -d'"' -f2)
    log_success "Version bumped to: $new_version"
}

cmd_clean() {
    log_section "🧹 Cleaning Build Artifacts"
    log_info "Removing build artifacts..."

    rm -rf dist/ build/ *.egg-info
    rm -rf .pytest_cache .ruff_cache .mypy_cache
    rm -rf htmlcov .coverage
    find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true

    log_success "Workspace cleaned!"
}

cmd_docs() {
    log_section "📚 Documentation"
    log_info "Opening documentation..."

    local docs=(
        "docs/JEDI_TRAINING.md"
        "docs/FORCE_POWERS.md"
        "docs/HOLOCRON.md"
        "docs/MISSION_BRIEFINGS.md"
        "README.md"
    )

    for doc in "${docs[@]}"; do
        if [[ -f "$doc" ]]; then
            echo -e "${CYAN}  • $doc${NC}"
        fi
    done
}

cmd_status() {
    log_section "📊 Death Star Status Report"

    echo -e "${CYAN}UV Version:${NC}"
    uv --version

    echo -e "\n${CYAN}Python Versions Available:${NC}"
    uv python list | head -5

    echo -e "\n${CYAN}Project Dependencies:${NC}"
    uv tree --depth 1

    echo -e "\n${CYAN}Git Status:${NC}"
    git status --short

    echo -e "\n${CYAN}Package Version:${NC}"
    grep '^version = ' pyproject.toml

    log_success "Status report complete!"
}

cmd_help() {
    show_banner
    cat << EOF
${CYAN}AVAILABLE COMMANDS:${NC}

  ${GREEN}Development:${NC}
    setup           Initialize project and install dependencies
    run [args]      Run the CLI tool
    demo            Show demonstration of features

  ${GREEN}Testing:${NC}
    test [args]     Run tests (pass pytest args)
    test-all        Test against all Python versions (3.9-3.13)
    coverage        Generate coverage report

  ${GREEN}Code Quality:${NC}
    lint            Run linter (Ruff)
    format          Format code with Ruff
    typecheck       Run type checker (MyPy)

  ${GREEN}Build & Deploy:${NC}
    build           Build package distributions
    version <type>  Bump version (patch|minor|major|alpha|beta|rc)
    publish-test    Publish to TestPyPI
    publish         Publish to production PyPI

  ${GREEN}Utilities:${NC}
    clean           Remove build artifacts
    status          Show project status
    docs            List documentation files
    help            Show this help message

${YELLOW}Examples:${NC}
  ./dev.sh setup                    # First-time setup
  ./dev.sh test                     # Run all tests
  ./dev.sh test tests/test_cli.py   # Run specific test file
  ./dev.sh run -c 5 -m 10           # Generate 10 5-word names
  ./dev.sh version patch            # Bump patch version (0.1.0 -> 0.1.1)
  ./dev.sh build                    # Build package
  ./dev.sh publish-test             # Test on TestPyPI

${CYAN}May the Force be with your development!${NC}
EOF
}

# Main dispatcher
main() {
    local command="${1:-help}"

    case "$command" in
        setup)        cmd_setup ;;
        test)         cmd_test "$@" ;;
        test-all)     cmd_test_all ;;
        lint)         cmd_lint ;;
        format)       cmd_format ;;
        typecheck)    cmd_typecheck ;;
        coverage)     cmd_coverage ;;
        run)          cmd_run "$@" ;;
        demo)         cmd_demo ;;
        build)        cmd_build ;;
        publish-test) cmd_publish_test ;;
        publish)      cmd_publish ;;
        version)      cmd_version "$@" ;;
        clean)        cmd_clean ;;
        status)       cmd_status ;;
        docs)         cmd_docs ;;
        help|--help|-h) cmd_help ;;
        *)
            log_error "Unknown command: $command"
            log_info "Run './dev.sh help' for available commands"
            exit 1
            ;;
    esac
}

# Run main
main "$@"
