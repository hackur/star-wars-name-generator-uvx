"""
CLI Integration Tests

TACTICAL CLI TESTING - Validates command-line interface operates correctly
across all operational parameters and edge cases.
"""

import pytest
import re
from click.testing import CliRunner
from starwars_namegen.cli import main


class TestCLIBasicOperation:
    """Test suite for basic CLI functionality."""

    def test_cli_runs_without_args(self, cli_runner):
        """Verify CLI executes successfully with no arguments."""
        result = cli_runner.invoke(main, [])
        assert result.exit_code == 0
        assert len(result.output.strip()) > 0

    def test_help_flag(self, cli_runner):
        """Verify --help displays usage information."""
        result = cli_runner.invoke(main, ['--help'])
        assert result.exit_code == 0
        assert 'Usage:' in result.output
        assert '--count' in result.output
        assert '--format' in result.output
        assert '--multiple' in result.output

    def test_version_flag(self, cli_runner):
        """Verify --version displays version information."""
        result = cli_runner.invoke(main, ['--version'])
        assert result.exit_code == 0
        assert '0.3.0' in result.output


class TestCLIWordCount:
    """Test suite for --count/-c option."""

    def test_count_1_word(self, cli_runner):
        """Verify -c 1 generates single-word name."""
        result = cli_runner.invoke(main, ['-c', '1'])
        assert result.exit_code == 0
        output = result.output.strip()
        assert '-' not in output  # Single word should have no separator

    def test_count_2_words(self, cli_runner):
        """Verify -c 2 generates 2-word name."""
        result = cli_runner.invoke(main, ['-c', '2', '-f', 'kebab'])
        assert result.exit_code == 0
        output = result.output.strip()
        parts = output.split('-')
        # May have suffix, so at least 2 words
        assert len(parts) >= 2

    def test_count_3_words(self, cli_runner):
        """Verify -c 3 generates 3-word name."""
        result = cli_runner.invoke(main, ['-c', '3', '-f', 'kebab', '--random', 'none'])
        assert result.exit_code == 0
        output = result.output.strip()
        parts = output.split('-')
        assert len(parts) == 3

    def test_count_4_words(self, cli_runner):
        """Verify -c 4 generates 4-word name."""
        result = cli_runner.invoke(main, ['-c', '4', '-f', 'kebab', '--random', 'none'])
        assert result.exit_code == 0
        output = result.output.strip()
        parts = output.split('-')
        assert len(parts) == 4

    def test_count_5_words(self, cli_runner):
        """Verify -c 5 generates 5-word name."""
        result = cli_runner.invoke(main, ['-c', '5', '-f', 'kebab', '--random', 'none'])
        assert result.exit_code == 0
        output = result.output.strip()
        parts = output.split('-')
        assert len(parts) == 5

    def test_long_form_count(self, cli_runner):
        """Verify --count long form works."""
        result = cli_runner.invoke(main, ['--count', '3'])
        assert result.exit_code == 0


class TestCLIFormats:
    """Test suite for --format/-f option."""

    def test_format_kebab(self, cli_runner):
        """Verify kebab-case format."""
        result = cli_runner.invoke(main, ['-c', '2', '-f', 'kebab', '--random', 'none'])
        assert result.exit_code == 0
        output = result.output.strip()
        assert '-' in output
        assert output.islower()

    def test_format_snake(self, cli_runner):
        """Verify snake_case format."""
        result = cli_runner.invoke(main, ['-c', '2', '-f', 'snake', '--random', 'none'])
        assert result.exit_code == 0
        output = result.output.strip()
        assert '_' in output
        assert output.islower()

    def test_format_camel(self, cli_runner):
        """Verify camelCase format."""
        result = cli_runner.invoke(main, ['-c', '2', '-f', 'camel', '--random', 'none'])
        assert result.exit_code == 0
        output = result.output.strip()
        # CamelCase starts with lowercase
        assert output[0].islower()
        assert re.match(r'^[a-z][a-zA-Z0-9]*$', output)

    def test_format_pascal(self, cli_runner):
        """Verify PascalCase format."""
        result = cli_runner.invoke(main, ['-c', '2', '-f', 'pascal', '--random', 'none'])
        assert result.exit_code == 0
        output = result.output.strip()
        # PascalCase starts with uppercase
        assert output[0].isupper()
        assert re.match(r'^[A-Z][a-zA-Z0-9]*$', output)

    def test_format_space(self, cli_runner):
        """Verify space-separated format."""
        result = cli_runner.invoke(main, ['-c', '2', '-f', 'space', '--random', 'none'])
        assert result.exit_code == 0
        output = result.output.strip()
        assert ' ' in output
        # Each word should be capitalized
        words = output.split()
        assert all(word[0].isupper() for word in words)

    def test_long_form_format(self, cli_runner):
        """Verify --format long form works."""
        result = cli_runner.invoke(main, ['--format', 'snake'])
        assert result.exit_code == 0


class TestCLISuffixes:
    """Test suite for --random/-r option."""

    def test_suffix_none(self, cli_runner):
        """Verify 'none' suffix generates no suffix."""
        result = cli_runner.invoke(main, ['-c', '2', '-f', 'kebab', '--random', 'none'])
        assert result.exit_code == 0
        output = result.output.strip()
        # Verify it's just words (no digits or hex at end)
        assert re.match(r'^[a-z-]+$', output)

    def test_suffix_digits(self, cli_runner):
        """Verify 'digits' suffix adds 3-digit number."""
        result = cli_runner.invoke(main, ['-c', '2', '-f', 'kebab', '--random', 'digits'])
        assert result.exit_code == 0
        output = result.output.strip()
        # Should end with -NNN
        assert re.search(r'-\d{3}$', output)

    def test_suffix_hex(self, cli_runner):
        """Verify 'hex' suffix adds 3-character hex."""
        result = cli_runner.invoke(main, ['-c', '2', '-f', 'kebab', '--random', 'hex'])
        assert result.exit_code == 0
        output = result.output.strip()
        # Should end with -xxx (hex)
        assert re.search(r'-[0-9a-f]{3}$', output)

    def test_suffix_symbol(self, cli_runner):
        """Verify 'symbol' suffix adds symbol."""
        result = cli_runner.invoke(main, ['-c', '2', '-f', 'kebab', '--random', 'symbol'])
        assert result.exit_code == 0
        output = result.output.strip()
        # Should end with a symbol
        assert re.search(r'-[!@#$%^&*+\-=~]$', output)

    def test_suffix_uuid(self, cli_runner):
        """Verify 'uuid' suffix adds 6-character hex."""
        result = cli_runner.invoke(main, ['-c', '2', '-f', 'kebab', '--random', 'uuid'])
        assert result.exit_code == 0
        output = result.output.strip()
        # Should end with -xxxxxx (6 hex chars)
        assert re.search(r'-[0-9a-f]{6}$', output)


class TestCLIMultipleGeneration:
    """Test suite for --multiple/-m option."""

    def test_multiple_generates_multiple_lines(self, cli_runner):
        """Verify -m generates multiple names."""
        result = cli_runner.invoke(main, ['-m', '5', '-c', '2', '-f', 'kebab'])
        assert result.exit_code == 0
        lines = result.output.strip().split('\n')
        assert len(lines) == 5

    def test_multiple_10(self, cli_runner):
        """Verify -m 10 generates 10 names."""
        result = cli_runner.invoke(main, ['-m', '10'])
        assert result.exit_code == 0
        lines = result.output.strip().split('\n')
        assert len(lines) == 10

    def test_long_form_multiple(self, cli_runner):
        """Verify --multiple long form works."""
        result = cli_runner.invoke(main, ['--multiple', '3'])
        assert result.exit_code == 0
        lines = result.output.strip().split('\n')
        assert len(lines) == 3


class TestCLISeedReproducibility:
    """Test suite for --seed/-s option."""

    def test_seed_produces_reproducible_output(self, cli_runner):
        """Verify same seed generates same name."""
        result1 = cli_runner.invoke(main, ['--seed', '42', '-c', '3'])
        result2 = cli_runner.invoke(main, ['--seed', '42', '-c', '3'])

        assert result1.exit_code == 0
        assert result2.exit_code == 0
        assert result1.output == result2.output

    def test_different_seeds_produce_different_output(self, cli_runner):
        """Verify different seeds generate different names."""
        result1 = cli_runner.invoke(main, ['--seed', '42', '-c', '3'])
        result2 = cli_runner.invoke(main, ['--seed', '123', '-c', '3'])

        assert result1.exit_code == 0
        assert result2.exit_code == 0
        # Very unlikely to be the same
        assert result1.output != result2.output

    def test_seed_with_multiple(self, cli_runner):
        """Verify seed works with multiple generation."""
        result1 = cli_runner.invoke(main, ['--seed', '42', '-m', '5'])
        result2 = cli_runner.invoke(main, ['--seed', '42', '-m', '5'])

        assert result1.output == result2.output

    def test_long_form_seed(self, cli_runner):
        """Verify --seed long form works."""
        result = cli_runner.invoke(main, ['--seed', '999'])
        assert result.exit_code == 0


class TestCLICombinations:
    """Test suite for complex option combinations."""

    def test_all_options_combined(self, cli_runner):
        """Verify all options work together."""
        result = cli_runner.invoke(main, [
            '-c', '3',
            '-f', 'snake',
            '-m', '3',
            '--random', 'hex',
            '--seed', '42'
        ])
        assert result.exit_code == 0
        lines = result.output.strip().split('\n')
        assert len(lines) == 3
        for line in lines:
            assert '_' in line  # snake_case
            assert re.search(r'_[0-9a-f]{3}$', line)  # hex suffix

    def test_count_format_suffix_combo(self, cli_runner):
        """Verify count + format + suffix combination."""
        result = cli_runner.invoke(main, ['-c', '4', '-f', 'pascal', '--random', 'digits'])
        assert result.exit_code == 0
        output = result.output.strip()
        assert output[0].isupper()  # PascalCase
        assert re.search(r'\d{3}$', output)  # digits suffix

    def test_multiple_with_seed_reproducibility(self, cli_runner):
        """Verify multiple names with seed are reproducible."""
        result1 = cli_runner.invoke(main, ['--seed', '999', '-m', '10', '-c', '2'])
        result2 = cli_runner.invoke(main, ['--seed', '999', '-m', '10', '-c', '2'])

        assert result1.output == result2.output
        lines = result1.output.strip().split('\n')
        assert len(lines) == 10


class TestCLIEdgeCases:
    """Test suite for CLI edge cases and error handling."""

    def test_invalid_format_shows_error(self, cli_runner):
        """Verify invalid format value shows helpful error."""
        result = cli_runner.invoke(main, ['-f', 'invalid'])
        assert result.exit_code != 0
        assert 'Invalid value' in result.output or 'Error' in result.output

    def test_invalid_suffix_shows_error(self, cli_runner):
        """Verify invalid suffix value shows helpful error."""
        result = cli_runner.invoke(main, ['--random', 'invalid'])
        assert result.exit_code != 0
        assert 'Invalid value' in result.output or 'Error' in result.output

    def test_negative_count_handled(self, cli_runner):
        """Verify negative count doesn't crash CLI."""
        result = cli_runner.invoke(main, ['-c', '-5'])
        # Should either succeed (clamp to 1) or show helpful error
        assert result.exit_code == 0 or 'Invalid' in result.output

    def test_zero_multiple_handled(self, cli_runner):
        """Verify zero multiple value is handled."""
        result = cli_runner.invoke(main, ['-m', '0'])
        # Should generate no output or show error
        assert result.exit_code == 0 or 'Invalid' in result.output

    def test_very_large_multiple(self, cli_runner):
        """Verify large multiple value works."""
        result = cli_runner.invoke(main, ['-m', '100', '-c', '2'])
        if result.exit_code == 0:
            lines = result.output.strip().split('\n')
            assert len(lines) == 100


class TestCLIOutputQuality:
    """Test suite for CLI output quality and formatting."""

    def test_output_has_no_trailing_whitespace(self, cli_runner):
        """Verify output lines don't have trailing whitespace."""
        result = cli_runner.invoke(main, ['-m', '5'])
        assert result.exit_code == 0
        for line in result.output.split('\n'):
            if line:  # Skip empty lines
                assert line == line.rstrip(), "Line has trailing whitespace"

    def test_output_is_consistent_format(self, cli_runner):
        """Verify all output lines use consistent format."""
        result = cli_runner.invoke(main, ['-m', '10', '-f', 'kebab'])
        assert result.exit_code == 0
        lines = result.output.strip().split('\n')

        # All lines should match kebab-case pattern
        for line in lines:
            assert re.match(r'^[a-z0-9-]+$', line), f"Inconsistent format: {line}"

    def test_output_contains_no_duplicates_with_uuid(self, cli_runner):
        """Verify UUID suffixes ensure no duplicates in batch."""
        result = cli_runner.invoke(main, ['-m', '50', '-c', '2', '--random', 'uuid'])
        assert result.exit_code == 0
        lines = result.output.strip().split('\n')

        # With UUID suffixes, should have no duplicates
        assert len(lines) == len(set(lines)), "Found duplicate names with UUID suffixes"

    def test_names_are_reasonable_length(self, cli_runner):
        """Verify generated names have reasonable length."""
        result = cli_runner.invoke(main, ['-m', '10', '-c', '3'])
        assert result.exit_code == 0
        lines = result.output.strip().split('\n')

        for line in lines:
            # Names should be between 10 and 70 characters
            assert 10 <= len(line) <= 70, f"Name length unusual: {len(line)} chars"


class TestCLIUserExperience:
    """Test suite for user experience and usability."""

    def test_default_behavior_generates_useful_name(self, cli_runner):
        """Verify running with no args generates useful output."""
        result = cli_runner.invoke(main, [])
        assert result.exit_code == 0
        output = result.output.strip()

        # Should be a single, reasonable name
        assert len(output) > 0
        assert '\n' not in output  # Single name
        # Allow shorter names (single words can be as short as 5 chars)
        assert 5 <= len(output) <= 70  # Reasonable length

    def test_help_is_comprehensive(self, cli_runner):
        """Verify help text covers all options."""
        result = cli_runner.invoke(main, ['--help'])
        assert result.exit_code == 0

        # Check all major options are documented
        assert '-c' in result.output or '--count' in result.output
        assert '-f' in result.output or '--format' in result.output
        assert '-m' in result.output or '--multiple' in result.output
        assert '-r' in result.output or '--random' in result.output
        assert '-s' in result.output or '--seed' in result.output
        assert '--version' in result.output

    def test_error_messages_are_helpful(self, cli_runner):
        """Verify error messages provide guidance."""
        result = cli_runner.invoke(main, ['-f', 'bad-format'])
        assert result.exit_code != 0
        # Error should mention the problem and show valid choices
        output = result.output.lower()
        assert 'invalid' in output or 'error' in output
