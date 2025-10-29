"""
Pytest Configuration and Fixtures

TACTICAL TESTING INFRASTRUCTURE - Shared test configuration and reusable fixtures
for all Death Star operational testing protocols.
"""

import pytest
from click.testing import CliRunner
from starwars_namegen.cli import StarWarsNameGenerator, main


@pytest.fixture
def generator():
    """
    Provide a fresh StarWarsNameGenerator instance for each test.

    Returns:
        StarWarsNameGenerator: Initialized name generation engine
    """
    return StarWarsNameGenerator()


@pytest.fixture
def cli_runner():
    """
    Provide a Click CLI test runner.

    Returns:
        CliRunner: Click testing utility for CLI invocation
    """
    return CliRunner()


@pytest.fixture
def seeded_generator():
    """
    Provide a generator with predictable random state for reproducibility tests.

    Returns:
        StarWarsNameGenerator: Generator with seed 42 applied
    """
    import random
    random.seed(42)
    return StarWarsNameGenerator()


@pytest.fixture(params=['kebab', 'snake', 'camel', 'pascal', 'space'])
def all_formats(request):
    """
    Parametrized fixture providing all supported output formats.

    Yields:
        str: Each format type (kebab, snake, camel, pascal, space)
    """
    return request.param


@pytest.fixture(params=['none', 'digits', 'hex', 'symbol', 'uuid'])
def all_suffixes(request):
    """
    Parametrized fixture providing all supported suffix types.

    Yields:
        str: Each suffix type (none, digits, hex, symbol, uuid)
    """
    return request.param


@pytest.fixture(params=[1, 2, 3, 4, 5])
def all_word_counts(request):
    """
    Parametrized fixture providing all supported word counts.

    Yields:
        int: Each word count from 1 to 5
    """
    return request.param
