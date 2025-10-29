#!/usr/bin/env python3
"""
Star Wars Name Generator - Python Programmatic Usage Examples
TACTICAL OPERATIONS MANUAL - PYTHON API INTEGRATION
"""

from starwars_namegen.cli import StarWarsNameGenerator

def main():
    print("=" * 60)
    print("Star Wars Name Generator - Python Programmatic Usage")
    print("=" * 60)
    print()
    
    # Initialize the generator
    generator = StarWarsNameGenerator()
    
    # Example 1: Different Word Counts
    print("=== Example 1: Different Word Counts ===")
    for count in range(1, 6):
        name = generator.generate_name(word_count=count, output_format="kebab")
        print(f"{count}-word name: {name}")
    print()
    
    # Example 2: All Output Formats
    print("=== Example 2: All Output Formats ===")
    formats = ["kebab", "snake", "camel", "pascal", "space"]
    for fmt in formats:
        name = generator.generate_name(word_count=3, output_format=fmt)
        print(f"{fmt:10s}: {name}")
    print()
    
    # Example 3: All Suffix Types
    print("=== Example 3: All Suffix Types ===")
    suffixes = ["none", "digits", "hex", "symbol", "uuid"]
    for suffix in suffixes:
        name = generator.generate_name(
            word_count=2,
            output_format="kebab",
            suffix_type=suffix
        )
        print(f"{suffix:10s}: {name}")
    print()
    
    # Example 4: Generate Container Fleet
    print("=== Example 4: Generate Container Fleet (10 containers) ===")
    for i in range(1, 11):
        name = generator.generate_name(
            word_count=2,
            output_format="kebab",
            suffix_type="digits"
        )
        print(f"Container {i:2d}: {name}")
    print()
    
    # Example 5: Infrastructure Naming Convention
    print("=== Example 5: Infrastructure Naming Convention ===")
    
    # Web servers
    print("Web Servers:")
    for _ in range(3):
        name = generator.generate_name(
            word_count=2,
            output_format="snake",
            suffix_type="hex"
        )
        print(f"  server_{name}")
    
    # Database instances
    print("\nDatabase Instances:")
    for _ in range(3):
        name = generator.generate_name(
            word_count=4,
            output_format="kebab",
            suffix_type="uuid"
        )
        print(f"  db-{name}")
    
    # Python class names
    print("\nPython Class Names:")
    for _ in range(3):
        name = generator.generate_name(
            word_count=2,
            output_format="pascal",
            suffix_type="none"
        )
        print(f"  class {name}:")
    print()
    
    # Example 6: Reproducible Names with Seed
    print("=== Example 6: Reproducible Names with Seed ===")
    import random
    
    # First generation
    random.seed(42)
    gen1 = StarWarsNameGenerator()
    name1 = gen1.generate_name(word_count=3, output_format="kebab")
    
    # Second generation with same seed
    random.seed(42)
    gen2 = StarWarsNameGenerator()
    name2 = gen2.generate_name(word_count=3, output_format="kebab")
    
    print(f"First generation  (seed=42): {name1}")
    print(f"Second generation (seed=42): {name2}")
    print(f"Names are identical: {name1 == name2}")
    print()
    
    # Example 7: Paired Resources
    print("=== Example 7: Paired Resources ===")
    for i in range(1, 4):
        base_name = generator.generate_name(
            word_count=2,
            output_format="snake",
            suffix_type="none"
        )
        print(f"Application Suite {i}:")
        print(f"  App:   {base_name}")
        print(f"  DB:    {base_name}_db")
        print(f"  Cache: {base_name}_cache")
    print()
    
    print("=" * 60)
    print("All Python API examples completed successfully!")
    print("=" * 60)

if __name__ == "__main__":
    main()
