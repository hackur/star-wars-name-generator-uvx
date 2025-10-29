#!/usr/bin/env python3
"""
Python Programmatic Usage Examples for Star Wars Name Generator

This demonstrates how to use the starwars-namegen package
programmatically in your own Python applications.
"""

from starwars_namegen.cli import StarWarsNameGenerator


def main():
    print("=" * 60)
    print("Star Wars Name Generator - Python Programmatic Usage")
    print("=" * 60)
    print()

    # Initialize the generator
    generator = StarWarsNameGenerator()

    # Example 1: Generate names with different word counts
    print("=== Example 1: Different Word Counts ===")
    for count in range(1, 6):
        name = generator.generate_name(word_count=count)
        print(f"{count}-word name: {name}")
    print()

    # Example 2: Generate names in all formats
    print("=== Example 2: All Output Formats ===")
    formats = ["kebab", "snake", "camel", "pascal", "space"]
    for fmt in formats:
        name = generator.generate_name(word_count=3, output_format=fmt)
        print(f"{fmt:10s}: {name}")
    print()

    # Example 3: Generate names with all suffix types
    print("=== Example 3: All Suffix Types ===")
    suffixes = ["none", "digits", "hex", "symbol", "uuid"]
    for suffix in suffixes:
        name = generator.generate_name(word_count=2, suffix_type=suffix)
        print(f"{suffix:10s}: {name}")
    print()

    # Example 4: Batch generation for resource naming
    print("=== Example 4: Generate Container Fleet (10 containers) ===")
    containers = []
    for i in range(10):
        name = generator.generate_name(
            word_count=2,
            output_format="kebab",
            suffix_type="digits"
        )
        containers.append(name)
        print(f"Container {i+1:2d}: {name}")
    print()

    # Example 5: Generate names for different infrastructure types
    print("=== Example 5: Infrastructure Naming Convention ===")

    # Web servers (snake_case for Python/configs)
    print("Web Servers:")
    for i in range(3):
        name = generator.generate_name(
            word_count=2,
            output_format="snake",
            suffix_type="hex"
        )
        print(f"  server_{name}")

    # Database instances (kebab-case with UUID)
    print("\nDatabase Instances:")
    for i in range(3):
        name = generator.generate_name(
            word_count=3,
            output_format="kebab",
            suffix_type="uuid"
        )
        print(f"  db-{name}")

    # Python classes (PascalCase)
    print("\nPython Class Names:")
    for i in range(3):
        name = generator.generate_name(
            word_count=2,
            output_format="pascal",
            suffix_type="none"
        )
        print(f"  class {name}:")
    print()

    # Example 6: Using seed for reproducible results
    print("=== Example 6: Reproducible Names with Seed ===")
    import random

    seed_value = 42
    random.seed(seed_value)
    name1 = generator.generate_name(word_count=3)

    # Reset seed to get same result
    random.seed(seed_value)
    name2 = generator.generate_name(word_count=3)

    print(f"First generation  (seed={seed_value}): {name1}")
    print(f"Second generation (seed={seed_value}): {name2}")
    print(f"Names are identical: {name1 == name2}")
    print()

    # Example 7: Generate name pairs for related resources
    print("=== Example 7: Paired Resources ===")
    for i in range(3):
        app_name = generator.generate_name(word_count=2, output_format="snake")
        db_name = f"{app_name}_db"
        cache_name = f"{app_name}_cache"

        print(f"Application Suite {i+1}:")
        print(f"  App:   {app_name}")
        print(f"  DB:    {db_name}")
        print(f"  Cache: {cache_name}")
    print()

    print("=" * 60)
    print("All examples completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
