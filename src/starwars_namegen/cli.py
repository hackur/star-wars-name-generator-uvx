#!/usr/bin/env python3
"""
Star Wars Name Generator CLI Tool

Generates multi-word (1-5 words) unique name strings using Star Wars-themed
verbs, adverbs, nouns, etc. for use with servers, instances, and other resources.
"""

import random
import string
import click
import inflect
from typing import List


class StarWarsNameGenerator:
    """Generate Star Wars-themed names with proper grammar."""

    def __init__(self):
        self.p = inflect.engine()

        # Star Wars vocabulary categorized by part of speech
        self.nouns = [
            "jedi", "sith", "droid", "falcon", "wookiee", "empire", "rebel",
            "force", "trooper", "saber", "cantina", "speeder", "blaster",
            "fighter", "destroyer", "cruiser", "squadron", "legion", "padawan",
            "master", "youngling", "senator", "admiral", "general", "commander",
            "pilot", "smuggler", "bounty", "hunter", "scavenger", "princess",
            "queen", "emperor", "chancellor", "council", "temple", "academy",
            "outpost", "station", "base", "fleet", "armada", "garrison"
        ]

        self.verbs = [
            "blast", "strike", "charge", "hover", "spin", "deploy", "ignite",
            "wield", "pilot", "command", "defend", "attack", "pursue", "escape",
            "smuggle", "negotiate", "meditate", "train", "duel", "sabotage",
            "infiltrate", "scout", "patrol", "guard", "monitor", "scan",
            "transmit", "receive", "intercept", "decode", "encrypt", "hack"
        ]

        self.adjectives = [
            "galactic", "imperial", "rebel", "dark", "light", "swift", "silent",
            "rogue", "elite", "stealth", "tactical", "advanced", "ancient",
            "mysterious", "powerful", "legendary", "heroic", "cunning", "brave",
            "fierce", "noble", "shadowy", "crimson", "azure", "emerald",
            "chrome", "plasma", "quantum", "hyper", "ultra", "mega"
        ]

        self.adverbs = [
            "swiftly", "silently", "fiercely", "boldly", "cunningly", "stealthily",
            "rapidly", "precisely", "efficiently", "strategically", "tactically",
            "aggressively", "defensively", "mysteriously", "heroically", "nobly"
        ]

        self.symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "-", "_", "~"]

    def _get_random_word(self, word_type: str) -> str:
        """Get a random word from specified category."""
        word_lists = {
            "noun": self.nouns,
            "verb": self.verbs,
            "adjective": self.adjectives,
            "adverb": self.adverbs,
            "any": self.nouns + self.verbs + self.adjectives + self.adverbs
        }
        return random.choice(word_lists.get(word_type, word_lists["any"]))

    def _apply_grammar(self, word_count: int) -> List[str]:
        """Apply basic grammar rules to make the name more sentence-like."""
        if word_count == 1:
            return [self._get_random_word("noun")]
        elif word_count == 2:
            adj = self._get_random_word("adjective")
            noun = self._get_random_word("noun")
            return [adj, noun]
        elif word_count == 3:
            adj = self._get_random_word("adjective")
            noun = self._get_random_word("noun")
            verb = self._get_random_word("verb")
            past_verb = self._to_past_tense(verb)
            return [adj, noun, past_verb]
        elif word_count == 4:
            adverb = self._get_random_word("adverb")
            adj = self._get_random_word("adjective")
            noun = self._get_random_word("noun")
            verb = self._get_random_word("verb")
            past_verb = self._to_past_tense(verb)
            return [adverb, adj, noun, past_verb]
        else:  # 5 words
            adj = self._get_random_word("adjective")
            noun = self._get_random_word("noun")
            adverb = self._get_random_word("adverb")
            verb = self._get_random_word("verb")
            past_verb = self._to_past_tense(verb)
            return ["the", adj, noun, adverb, past_verb]

    def _to_past_tense(self, verb: str) -> str:
        """Convert a verb to past tense (simple rules)."""
        if verb.endswith("e"):
            return verb + "d"
        elif verb.endswith("y"):
            return verb[:-1] + "ied"
        else:
            return verb + "ed"

    def _generate_suffix(self, suffix_type: str) -> str:
        """Generate a random suffix based on type."""
        if suffix_type == "none":
            return ""
        elif suffix_type == "digits":
            return str(random.randint(100, 999))
        elif suffix_type == "hex":
            return format(random.randint(0, 4095), "03x")
        elif suffix_type == "symbol":
            return random.choice(self.symbols)
        elif suffix_type == "uuid":
            # Generate a short UUID-like string
            return "".join(random.choices(string.hexdigits[:16], k=6))
        else:
            return ""

    def generate_name(
        self,
        word_count: int = None,
        output_format: str = "kebab",
        suffix_type: str = "none"
    ) -> str:
        """
        Generate a Star Wars-themed name.

        Args:
            word_count: Number of words (1-5). If None, randomly chosen.
            output_format: Output format - 'kebab', 'snake', 'camel', 'pascal', 'space'
            suffix_type: Type of random suffix - 'none', 'digits', 'hex', 'symbol', 'uuid'

        Returns:
            Generated name string
        """
        if word_count is None:
            word_count = random.randint(1, 5)

        word_count = max(1, min(5, word_count))  # Clamp to 1-5 range

        # Generate words with grammar applied
        words = self._apply_grammar(word_count)

        # Generate suffix
        suffix = self._generate_suffix(suffix_type)

        return self._format_output(words, output_format, suffix)

    def _format_output(self, words: List[str], format_type: str, suffix: str) -> str:
        """Format the output according to the specified format."""
        if format_type == "kebab":
            base = "-".join(words).lower()
        elif format_type == "snake":
            base = "_".join(words).lower()
        elif format_type == "camel":
            base = words[0].lower()
            for word in words[1:]:
                base += word.capitalize()
        elif format_type == "pascal":
            base = "".join(word.capitalize() for word in words)
        elif format_type == "space":
            base = " ".join(words).title()
        else:
            base = "-".join(words).lower()

        if suffix:
            return f"{base}-{suffix}" if format_type != "space" else f"{base} {suffix}"
        return base


@click.command()
@click.option(
    "--count", "-c",
    type=int,
    help="Number of words in the name (1-5). If not specified, randomly chosen."
)
@click.option(
    "--format", "-f", "output_format",
    type=click.Choice(["kebab", "snake", "camel", "pascal", "space"]),
    default="kebab",
    help="Output format for the generated name."
)
@click.option(
    "--multiple", "-m",
    type=int,
    default=1,
    help="Generate multiple names at once."
)
@click.option(
    "--random", "-r", "suffix_type",
    type=click.Choice(["none", "digits", "hex", "symbol", "uuid"]),
    default="none",
    help="Type of random suffix to append (default: none)."
)
@click.option(
    "--seed", "-s",
    type=int,
    help="Random seed for reproducible results."
)
@click.version_option()
def main(count, output_format, multiple, suffix_type, seed):
    """
    Generate Star Wars-themed multi-word names for servers, instances, and other resources.

    Examples:

        starwars-namegen                               # Generate one random name

        starwars-namegen -c 3 -f snake                 # Generate 3-word name in snake_case

        starwars-namegen -m 5 --random digits          # Generate 5 names with digit suffixes

        starwars-namegen --seed 42                     # Generate reproducible name
    """
    if seed is not None:
        random.seed(seed)

    generator = StarWarsNameGenerator()

    for i in range(multiple):
        name = generator.generate_name(count, output_format, suffix_type)
        click.echo(name)


if __name__ == "__main__":
    main()
