"""
Star Wars Name Generator

A CLI tool for generating Star Wars-themed multi-word names for servers,
instances, and other resources. Educational tool demonstrating modern
Python packaging with UV/UVX.
"""

__version__ = "0.3.0"
__author__ = "Jeremy Sarda"
__email__ = "jeremy@hackur.io"

from .cli import StarWarsNameGenerator

__all__ = ["StarWarsNameGenerator"]
