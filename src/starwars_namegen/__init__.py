"""
Star Wars Name Generator

A CLI tool for generating Star Wars-themed multi-word names for servers,
instances, and other resources.
"""

__version__ = "0.1.0"
__author__ = "Claude Code"
__email__ = "claude@anthropic.com"

from .cli import StarWarsNameGenerator

__all__ = ["StarWarsNameGenerator"]
