#!/bin/bash
# Basic Usage Examples for Star Wars Name Generator

echo "================================================"
echo "Star Wars Name Generator - Basic Usage Examples"
echo "================================================"
echo ""

echo "=== 1. Simple Random Name (Default: kebab-case) ==="
starwars-namegen
echo ""

echo "=== 2. Specific Word Count (3 words) ==="
starwars-namegen -c 3
echo ""

echo "=== 3. Different Formats ==="
echo "kebab-case:"
starwars-namegen -c 2 -f kebab

echo "snake_case:"
starwars-namegen -c 2 -f snake

echo "camelCase:"
starwars-namegen -c 2 -f camel

echo "PascalCase:"
starwars-namegen -c 2 -f pascal

echo "space separated:"
starwars-namegen -c 2 -f space
echo ""

echo "=== 4. Random Suffixes for Uniqueness ==="
echo "With digits:"
starwars-namegen --random digits

echo "With hex:"
starwars-namegen --random hex

echo "With symbol:"
starwars-namegen --random symbol

echo "With UUID:"
starwars-namegen --random uuid
echo ""

echo "=== 5. Generate Multiple Names ==="
starwars-namegen -m 5
echo ""

echo "=== 6. Reproducible Results (seed) ==="
echo "First run with seed 42:"
starwars-namegen --seed 42
echo "Second run with seed 42 (should be identical):"
starwars-namegen --seed 42
echo ""

echo "=== 7. Complex Combinations ==="
echo "3-word snake_case with digits:"
starwars-namegen -c 3 -f snake --random digits

echo "4-word PascalCase with hex:"
starwars-namegen -c 4 -f pascal --random hex

echo "5 kebab-case names with UUID:"
starwars-namegen -m 5 -c 2 --random uuid
echo ""

echo "================================================"
echo "All examples completed!"
echo "================================================"
