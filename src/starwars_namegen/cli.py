"""
Star Wars Name Generator CLI

Main command-line interface and name generation engine.
"""

import random
import string
from typing import List, Optional

import click
import inflect


class StarWarsNameGenerator:
    """
    TACTICAL NAME GENERATION ENGINE
    
    Generates Star Wars-themed multi-word names using linguistically sound
    grammar patterns and tactical suffix protocols.
    """
    
    def __init__(self):
        """Initialize the name generation tactical systems."""
        self.inflect_engine = inflect.engine()
        
        # VOCABULARY ARSENAL - Star Wars Themed Terms
        self.nouns = [
            "falcon", "destroyer", "empire", "rebel", "jedi", "sith", "force",
            "lightsaber", "blaster", "droid", "trooper", "clone", "republic",
            "senate", "council", "temple", "base", "outpost", "station", "fleet",
            "squadron", "legion", "battalion", "cruiser", "fighter", "speeder",
            "walker", "dreadnought", "frigate", "corvette", "starfighter",
            "interceptor", "bomber", "transport", "shuttle", "gunship", "academy",
            "garrison", "armada", "patrol", "scout", "hunter", "bounty",
            "smuggler", "scavenger", "pilot", "commander", "admiral", "general",
            "captain", "lieutenant", "sergeant", "trooper", "guard", "sentinel",
            "wookiee", "ewok", "hutt", "naboo", "tatooine", "hoth", "endor",
            "dagobah", "coruscant", "alderaan", "yavin", "bespin", "kamino",
            "geonosis", "mustafar", "kashyyyk", "mandalore", "dathomir",
            "holocron", "kyber", "crystal", "saber", "chancellor", "senator",
            "emperor", "lord", "master", "knight", "padawan", "youngling",
            "apprentice", "queen", "king", "prince", "princess", "duchess",
            "protocol", "astromech", "battle", "medical", "probe", "assassin",
            "cantina", "hangar", "bay", "chamber", "throne", "pit", "arena"
        ]
        
        self.verbs = [
            "strike", "attack", "defend", "patrol", "scout", "hunt", "pursue",
            "evade", "escape", "infiltrate", "sabotage", "destroy", "construct",
            "deploy", "engage", "retreat", "advance", "flank", "ambush", "raid",
            "siege", "blockade", "bombard", "strafe", "dogfight", "duel",
            "train", "meditate", "commune", "sense", "predict", "foresee",
            "command", "lead", "follow", "obey", "rebel", "resist", "surrender",
            "negotiate", "trade", "smuggle", "scavenge", "salvage", "repair",
            "hack", "slice", "decode", "encrypt", "transmit", "broadcast",
            "scan", "detect", "track", "locate", "identify", "analyze",
            "calculate", "navigate", "pilot", "fly", "land", "launch", "jump",
            "warp", "teleport", "phase", "cloak", "shield", "armor", "fortify",
            "charge", "fire", "shoot", "blast", "zap", "stun", "freeze",
            "burn", "melt", "explode", "implode", "collapse", "shatter",
            "pierce", "cut", "slash", "stab", "thrust", "parry", "block",
            "deflect", "reflect", "absorb", "channel", "focus", "concentrate",
            "ignite", "extinguish", "activate", "deactivate", "power", "fuel"
        ]
        
        self.adjectives = [
            "imperial", "rebel", "galactic", "cosmic", "stellar", "lunar",
            "solar", "quantum", "hyper", "ultra", "mega", "super", "turbo",
            "stealth", "shadow", "dark", "light", "crimson", "azure", "emerald",
            "chrome", "golden", "silver", "bronze", "iron", "steel", "titanium",
            "ancient", "legendary", "mythical", "epic", "heroic", "noble",
            "fierce", "savage", "brutal", "ruthless", "cunning", "sly",
            "swift", "rapid", "quick", "fast", "slow", "heavy", "light",
            "powerful", "mighty", "strong", "weak", "feeble", "fragile",
            "tactical", "strategic", "operative", "covert", "classified",
            "secret", "hidden", "mysterious", "enigmatic", "cryptic", "arcane",
            "advanced", "primitive", "prototype", "experimental", "standard",
            "elite", "veteran", "rookie", "seasoned", "experienced", "green",
            "rogue", "outlaw", "lawful", "chaos", "order", "neutral",
            "brave", "cowardly", "loyal", "traitorous", "honorable", "infamous"
        ]
        
        self.adverbs = [
            "swiftly", "quickly", "rapidly", "slowly", "stealthily", "silently",
            "loudly", "fiercely", "savagely", "brutally", "cunningly", "slyly",
            "heroically", "nobly", "honorably", "shamefully", "mysteriously",
            "enigmatically", "tactically", "strategically", "operationally",
            "covertly", "secretly", "openly", "publicly", "privately",
            "efficiently", "effectively", "powerfully", "mightily", "strongly",
            "weakly", "precisely", "accurately", "carefully", "recklessly"
        ]
        
        self.symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '+', '-', '=', '~']
    
    def _get_random_word(self, word_type: str) -> str:
        """
        Retrieve random word from tactical vocabulary database.
        
        Args:
            word_type: Type of word ("noun", "verb", "adjective", "adverb")
        
        Returns:
            Random word from specified category
        """
        if word_type == "noun":
            return random.choice(self.nouns)
        elif word_type == "verb":
            return random.choice(self.verbs)
        elif word_type == "adjective":
            return random.choice(self.adjectives)
        elif word_type == "adverb":
            return random.choice(self.adverbs)
        else:
            return random.choice(self.nouns)
    
    def _apply_grammar(self, word_count: int) -> List[str]:
        """
        Apply tactical grammar rules to generate name components.
        
        Grammar Protocols:
        - 1-word: {noun}
        - 2-word: {adjective} {noun}
        - 3-word: {adjective} {noun} {verb-past}
        - 4-word: {adverb} {adjective} {noun} {verb-past}
        - 5-word: the {adjective} {noun} {adverb} {verb-past}
        
        Args:
            word_count: Number of words to generate (1-5)
        
        Returns:
            List of words forming the name
        """
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
            adv = self._get_random_word("adverb")
            adj = self._get_random_word("adjective")
            noun = self._get_random_word("noun")
            verb = self._get_random_word("verb")
            past_verb = self._to_past_tense(verb)
            return [adv, adj, noun, past_verb]
        
        else:  # 5 words
            adj = self._get_random_word("adjective")
            noun = self._get_random_word("noun")
            adv = self._get_random_word("adverb")
            verb = self._get_random_word("verb")
            past_verb = self._to_past_tense(verb)
            return ["the", adj, noun, adv, past_verb]
    
    def _to_past_tense(self, verb: str) -> str:
        """
        Convert verb to past tense using simplified rules.
        
        Args:
            verb: Base verb form
        
        Returns:
            Past tense form of verb
        """
        # Simple past tense rules (good enough for our tactical purposes)
        if verb.endswith('e'):
            return verb + 'd'
        elif verb.endswith('y') and verb[-2] not in 'aeiou':
            return verb[:-1] + 'ied'
        else:
            return verb + 'ed'
    
    def _generate_suffix(self, suffix_type: str) -> str:
        """
        Generate tactical identifier suffix.
        
        Suffix Protocols:
        - none: No suffix
        - digits: 3-digit number (000-999)
        - hex: 3-character hexadecimal (000-fff)
        - symbol: Random symbol
        - uuid: 6-character hex (UUID-like)
        
        Args:
            suffix_type: Type of suffix to generate
        
        Returns:
            Generated suffix string (empty if none)
        """
        if suffix_type == "none":
            return ""
        elif suffix_type == "digits":
            return f"-{random.randint(0, 999):03d}"
        elif suffix_type == "hex":
            return f"-{random.randint(0, 4095):03x}"
        elif suffix_type == "symbol":
            return f"-{random.choice(self.symbols)}"
        elif suffix_type == "uuid":
            hex_chars = ''.join(random.choices('0123456789abcdef', k=6))
            return f"-{hex_chars}"
        else:
            return ""
    
    def _format_output(self, words: List[str], output_format: str, suffix: str) -> str:
        """
        Format words into specified output format.
        
        Args:
            words: List of words to format
            output_format: Desired format (kebab, snake, camel, pascal, space)
            suffix: Suffix to append
        
        Returns:
            Formatted name string
        """
        if output_format == "kebab":
            base = "-".join(word.lower() for word in words)
            return base + suffix
        
        elif output_format == "snake":
            base = "_".join(word.lower() for word in words)
            # Replace dash with underscore in suffix for consistency
            suffix_clean = suffix.replace("-", "_")
            return base + suffix_clean
        
        elif output_format == "camel":
            if not words:
                return ""
            base = words[0].lower() + "".join(word.capitalize() for word in words[1:])
            # For camelCase, append suffix without separator
            suffix_clean = suffix.replace("-", "")
            return base + suffix_clean
        
        elif output_format == "pascal":
            base = "".join(word.capitalize() for word in words)
            # For PascalCase, append suffix without separator
            suffix_clean = suffix.replace("-", "")
            return base + suffix_clean
        
        elif output_format == "space":
            base = " ".join(word.capitalize() for word in words)
            # For space format, append suffix with space
            if suffix:
                return base + " " + suffix.lstrip("-")
            return base
        
        else:
            # Default to kebab
            base = "-".join(word.lower() for word in words)
            return base + suffix
    
    def generate_name(
        self,
        word_count: Optional[int] = None,
        output_format: str = "kebab",
        suffix_type: str = "none"
    ) -> str:
        """
        Generate a Star Wars themed name.
        
        Args:
            word_count: Number of words (1-5). If None, randomly chosen.
            output_format: Output format (kebab, snake, camel, pascal, space)
            suffix_type: Suffix type (none, digits, hex, symbol, uuid)
        
        Returns:
            Generated name string
        
        Examples:
            >>> generator = StarWarsNameGenerator()
            >>> generator.generate_name(word_count=2, output_format="kebab")
            'imperial-destroyer'
            >>> generator.generate_name(word_count=3, output_format="snake", suffix_type="digits")
            'rebel_base_secured_847'
        """
        # Determine word count
        if word_count is None:
            word_count = random.randint(1, 5)
        else:
            word_count = max(1, min(5, word_count))
        
        # Generate words using grammar rules
        words = self._apply_grammar(word_count)
        
        # Generate suffix
        suffix = self._generate_suffix(suffix_type)
        
        # Format output
        name = self._format_output(words, output_format, suffix)
        
        return name


@click.command()
@click.option(
    "-c", "--count",
    type=int,
    default=None,
    help="Number of words in the name (1-5). If not specified, randomly chosen."
)
@click.option(
    "-f", "--format",
    type=click.Choice(["kebab", "snake", "camel", "pascal", "space"], case_sensitive=False),
    default="kebab",
    help="Output format for the generated name."
)
@click.option(
    "-m", "--multiple",
    type=int,
    default=1,
    help="Generate multiple names at once."
)
@click.option(
    "-r", "--random",
    "suffix_type",
    type=click.Choice(["none", "digits", "hex", "symbol", "uuid"], case_sensitive=False),
    default="none",
    help="Type of random suffix to append (default: none)."
)
@click.option(
    "-s", "--seed",
    type=int,
    default=None,
    help="Random seed for reproducible results."
)
@click.version_option(version="0.1.0", prog_name="starwars-namegen")
def main(count, format, multiple, suffix_type, seed):
    """
    Generate Star Wars-themed multi-word names for servers, instances, and other resources.
    
    Examples:
    
        starwars-namegen                               # Generate one random name
        
        starwars-namegen -c 3 -f snake                 # Generate 3-word name in snake_case
        
        starwars-namegen -m 5 --random digits          # Generate 5 names with digit suffixes
        
        starwars-namegen --seed 42                     # Generate reproducible name
    """
    # Set seed if provided
    if seed is not None:
        random.seed(seed)
    
    # Initialize generator
    generator = StarWarsNameGenerator()
    
    # Generate names
    for _ in range(multiple):
        name = generator.generate_name(
            word_count=count,
            output_format=format,
            suffix_type=suffix_type
        )
        click.echo(name)


if __name__ == "__main__":
    main()
