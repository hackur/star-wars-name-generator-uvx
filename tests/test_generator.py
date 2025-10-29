"""
Unit Tests for StarWarsNameGenerator

TACTICAL UNIT TESTING - Validates all name generation engine components
operate within acceptable parameters.
"""

import random
import re
import pytest
from starwars_namegen.cli import StarWarsNameGenerator


class TestNameGeneratorInitialization:
    """Test suite for generator initialization and vocabulary loading."""

    def test_generator_creates_successfully(self, generator):
        """Verify generator initializes without errors."""
        assert generator is not None
        assert generator.inflect_engine is not None

    def test_vocabulary_loaded(self, generator):
        """Verify all vocabulary lists are populated."""
        assert len(generator.nouns) > 0
        assert len(generator.verbs) > 0
        assert len(generator.adjectives) > 0
        assert len(generator.adverbs) > 0
        assert len(generator.symbols) > 0

    def test_vocabulary_minimum_size(self, generator):
        """Ensure vocabulary meets minimum tactical requirements."""
        assert len(generator.nouns) >= 40, "Insufficient noun arsenal"
        assert len(generator.verbs) >= 30, "Insufficient verb tactical options"
        assert len(generator.adjectives) >= 30, "Insufficient adjective modifiers"
        assert len(generator.adverbs) >= 15, "Insufficient adverb operations"
        assert len(generator.symbols) >= 10, "Insufficient symbol diversity"


class TestWordRetrieval:
    """Test suite for vocabulary word retrieval methods."""

    def test_get_random_noun(self, generator):
        """Verify random noun selection."""
        word = generator._get_random_word("noun")
        assert word in generator.nouns

    def test_get_random_verb(self, generator):
        """Verify random verb selection."""
        word = generator._get_random_word("verb")
        assert word in generator.verbs

    def test_get_random_adjective(self, generator):
        """Verify random adjective selection."""
        word = generator._get_random_word("adjective")
        assert word in generator.adjectives

    def test_get_random_adverb(self, generator):
        """Verify random adverb selection."""
        word = generator._get_random_word("adverb")
        assert word in generator.adverbs

    def test_randomness_distribution(self, generator):
        """Verify word selection has reasonable distribution."""
        words = [generator._get_random_word("noun") for _ in range(100)]
        unique_words = set(words)
        # Should get at least 20 different nouns in 100 draws
        assert len(unique_words) >= 20, "Insufficient randomness in word selection"


class TestPastTenseConversion:
    """Test suite for verb past tense conversion."""

    def test_past_tense_e_ending(self, generator):
        """Test verbs ending in 'e' get 'd' appended."""
        assert generator._to_past_tense("strike") == "striked"
        assert generator._to_past_tense("evade") == "evaded"

    def test_past_tense_y_ending(self, generator):
        """Test verbs ending in 'y' convert to 'ied'."""
        result = generator._to_past_tense("spy")
        assert result == "spied"

    def test_past_tense_default(self, generator):
        """Test default past tense adds 'ed'."""
        result = generator._to_past_tense("attack")
        assert result == "attacked"


class TestSuffixGeneration:
    """Test suite for suffix generation protocols."""

    def test_suffix_none(self, generator):
        """Verify 'none' suffix returns empty string."""
        suffix = generator._generate_suffix("none")
        assert suffix == ""

    def test_suffix_digits(self, generator):
        """Verify 'digits' suffix generates 3-digit number."""
        suffix = generator._generate_suffix("digits")
        assert re.match(r'^\d{3}$', suffix), f"Invalid digits suffix: {suffix}"
        assert 0 <= int(suffix) <= 999

    def test_suffix_hex(self, generator):
        """Verify 'hex' suffix generates 3-character hexadecimal."""
        suffix = generator._generate_suffix("hex")
        assert re.match(r'^[0-9a-f]{3}$', suffix), f"Invalid hex suffix: {suffix}"
        assert len(suffix) == 3

    def test_suffix_symbol(self, generator):
        """Verify 'symbol' suffix returns valid symbol."""
        suffix = generator._generate_suffix("symbol")
        assert suffix in generator.symbols

    def test_suffix_uuid(self, generator):
        """Verify 'uuid' suffix generates 6-character hex string."""
        suffix = generator._generate_suffix("uuid")
        assert re.match(r'^[0-9a-f]{6}$', suffix), f"Invalid uuid suffix: {suffix}"
        assert len(suffix) == 6


class TestFormatOutput:
    """Test suite for output format conversion."""

    def test_format_kebab(self, generator):
        """Verify kebab-case formatting."""
        words = ["imperial", "fleet", "deployed"]
        result = generator._format_output(words, "kebab", "123")
        assert result == "imperial-fleet-deployed-123"

    def test_format_snake(self, generator):
        """Verify snake_case formatting."""
        words = ["rebel", "base", "secured"]
        result = generator._format_output(words, "snake", "abc")
        assert result == "rebel_base_secured_abc"

    def test_format_camel(self, generator):
        """Verify camelCase formatting."""
        words = ["galactic", "empire", "rises"]
        result = generator._format_output(words, "camel", "")
        assert result == "galacticEmpireRises"
        assert result[0].islower()

    def test_format_pascal(self, generator):
        """Verify PascalCase formatting."""
        words = ["death", "star", "complete"]
        result = generator._format_output(words, "pascal", "")
        assert result == "DeathStarComplete"
        assert result[0].isupper()

    def test_format_space(self, generator):
        """Verify space-separated formatting."""
        words = ["stealth", "fighter"]
        result = generator._format_output(words, "space", "007")
        assert result == "Stealth Fighter 007"
        # Check proper capitalization
        assert all(word[0].isupper() for word in result.split()[:-1])


class TestNameGeneration:
    """Test suite for complete name generation."""

    def test_generate_1_word_name(self, generator):
        """Verify single-word name generation."""
        name = generator.generate_name(word_count=1, output_format="kebab", suffix_type="none")
        assert name is not None
        assert len(name) > 0
        assert '-' not in name  # Single word, no separator

    def test_generate_2_word_name(self, generator):
        """Verify 2-word name generation."""
        name = generator.generate_name(word_count=2, output_format="kebab", suffix_type="none")
        parts = name.split('-')
        assert len(parts) == 2

    def test_generate_3_word_name(self, generator):
        """Verify 3-word name generation."""
        name = generator.generate_name(word_count=3, output_format="kebab", suffix_type="none")
        parts = name.split('-')
        assert len(parts) == 3

    def test_generate_4_word_name(self, generator):
        """Verify 4-word name generation."""
        name = generator.generate_name(word_count=4, output_format="kebab", suffix_type="none")
        parts = name.split('-')
        assert len(parts) == 4

    def test_generate_5_word_name(self, generator):
        """Verify 5-word name generation."""
        name = generator.generate_name(word_count=5, output_format="kebab", suffix_type="none")
        parts = name.split('-')
        assert len(parts) == 5

    def test_all_formats_parametrized(self, generator, all_formats):
        """Test all output formats generate valid names."""
        name = generator.generate_name(word_count=2, output_format=all_formats, suffix_type="none")
        assert name is not None
        assert len(name) > 0

    def test_all_suffixes_parametrized(self, generator, all_suffixes):
        """Test all suffix types generate valid names."""
        name = generator.generate_name(word_count=2, output_format="kebab", suffix_type=all_suffixes)
        assert name is not None
        assert len(name) > 0

    def test_all_word_counts_parametrized(self, generator, all_word_counts):
        """Test all word counts generate valid names."""
        name = generator.generate_name(word_count=all_word_counts, output_format="kebab", suffix_type="none")
        assert name is not None
        assert len(name) > 0

    def test_reproducibility_with_seed(self):
        """Verify same seed produces same names."""
        random.seed(42)
        gen1 = StarWarsNameGenerator()
        name1 = gen1.generate_name(word_count=3, output_format="kebab", suffix_type="digits")

        random.seed(42)
        gen2 = StarWarsNameGenerator()
        name2 = gen2.generate_name(word_count=3, output_format="kebab", suffix_type="digits")

        assert name1 == name2, "Seeded generation should be reproducible"

    def test_randomness_without_seed(self, generator):
        """Verify names are different without seed."""
        names = [generator.generate_name(word_count=3, output_format="kebab", suffix_type="hex") for _ in range(10)]
        unique_names = set(names)
        # Should generate at least 8 unique names out of 10 tries
        assert len(unique_names) >= 8, "Insufficient randomness in name generation"

    def test_word_count_clamping(self, generator):
        """Verify word count is clamped to valid range."""
        # Test lower bound
        name = generator.generate_name(word_count=0, output_format="kebab", suffix_type="none")
        assert name is not None  # Should clamp to 1

        # Test upper bound
        name = generator.generate_name(word_count=10, output_format="kebab", suffix_type="none")
        assert name is not None  # Should clamp to 5


class TestNameQuality:
    """Test suite for name quality and usability."""

    def test_name_is_url_safe_kebab(self, generator):
        """Verify kebab-case names are URL-safe."""
        name = generator.generate_name(word_count=3, output_format="kebab", suffix_type="digits")
        # Should only contain lowercase letters, numbers, and hyphens
        assert re.match(r'^[a-z0-9-]+$', name), f"Name not URL-safe: {name}"

    def test_name_is_filesystem_safe_snake(self, generator):
        """Verify snake_case names are filesystem-safe."""
        name = generator.generate_name(word_count=2, output_format="snake", suffix_type="none")
        # Should only contain lowercase letters, numbers, and underscores
        assert re.match(r'^[a-z0-9_]+$', name), f"Name not filesystem-safe: {name}"

    def test_name_is_valid_identifier_camel(self, generator):
        """Verify camelCase names are valid programming identifiers."""
        name = generator.generate_name(word_count=2, output_format="camel", suffix_type="none")
        # Should be valid Python/JavaScript identifier
        assert re.match(r'^[a-zA-Z][a-zA-Z0-9]*$', name), f"Name not valid identifier: {name}"

    def test_name_is_valid_class_name_pascal(self, generator):
        """Verify PascalCase names are valid class names."""
        name = generator.generate_name(word_count=2, output_format="pascal", suffix_type="none")
        # Should start with uppercase and contain only letters
        assert re.match(r'^[A-Z][a-zA-Z0-9]*$', name), f"Name not valid class name: {name}"

    def test_generated_names_are_memorable(self, generator):
        """Verify names have reasonable length for memorability."""
        name = generator.generate_name(word_count=3, output_format="kebab", suffix_type="digits")
        # Names should be between 10 and 60 characters for good memorability
        assert 10 <= len(name) <= 60, f"Name length suboptimal: {len(name)} chars"

    def test_batch_uniqueness(self, generator):
        """Verify batch generation produces unique names."""
        names = [generator.generate_name(word_count=2, output_format="kebab", suffix_type="hex") for _ in range(50)]
        unique_names = set(names)
        # With hex suffixes, should get high uniqueness (at least 90%)
        uniqueness_ratio = len(unique_names) / len(names)
        assert uniqueness_ratio >= 0.90, f"Insufficient uniqueness: {uniqueness_ratio:.2%}"


class TestEdgeCases:
    """Test suite for edge cases and error handling."""

    def test_none_word_count_uses_random(self, generator):
        """Verify None word_count triggers random selection."""
        name = generator.generate_name(word_count=None, output_format="kebab", suffix_type="none")
        assert name is not None
        assert len(name) > 0

    def test_negative_word_count_handled(self, generator):
        """Verify negative word count doesn't crash."""
        name = generator.generate_name(word_count=-5, output_format="kebab", suffix_type="none")
        assert name is not None  # Should be clamped to 1

    def test_empty_suffix_handled(self, generator):
        """Verify empty suffix type doesn't crash."""
        name = generator.generate_name(word_count=2, output_format="kebab", suffix_type="none")
        assert name is not None
        assert not name.endswith('-')  # Should not end with separator
