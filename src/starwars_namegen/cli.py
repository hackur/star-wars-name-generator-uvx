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
        
        # VOCABULARY ARSENAL - Expanded Star Wars Universe
        # Over 200 nouns covering characters, ships, planets, creatures, and more!
        self.nouns = [
            # Iconic Ships & Vehicles
            "falcon", "destroyer", "xwing", "tiefighter", "awing", "bwing", "ywing",
            "interceptor", "bomber", "starfighter", "cruiser", "frigate", "corvette",
            "dreadnought", "walker", "speeder", "transport", "shuttle", "gunship",
            "blockade-runner", "star-destroyer", "super-destroyer", "executor",
            "millennium-falcon", "slave-one", "outrider", "ebon-hawk", "razor-crest",

            # Factions & Organizations
            "empire", "rebel", "alliance", "republic", "confederacy", "resistance",
            "first-order", "new-order", "separatist", "federation", "syndicate",

            # Force Users & Ranks
            "jedi", "sith", "force", "padawan", "knight", "master", "lord",
            "apprentice", "inquisitor", "guardian", "consular", "sentinel",
            "grey-jedi", "dark-jedi", "acolyte", "initiate", "youngling",

            # Military Ranks & Roles
            "commander", "admiral", "general", "captain", "lieutenant", "sergeant",
            "major", "colonel", "marshal", "moff", "grand-moff", "warlord",
            "trooper", "soldier", "pilot", "navigator", "gunner", "engineer",
            "scout", "ranger", "commando", "operative", "agent", "spy",

            # Planets & Moons (Major Locations)
            "tatooine", "hoth", "endor", "dagobah", "coruscant", "naboo",
            "alderaan", "yavin", "bespin", "kamino", "geonosis", "mustafar",
            "kashyyyk", "mandalore", "dathomir", "ryloth", "mon-cala", "corellia",
            "jakku", "scarif", "jedha", "eadu", "crait", "ahch-to", "exegol",
            "korriban", "moraband", "dantooine", "ord-mantell", "nar-shaddaa",

            # Creatures & Species
            "wookiee", "ewok", "hutt", "rodian", "twilek", "togruta", "zabrak",
            "rancor", "wampa", "tauntaun", "bantha", "dewback", "nexu", "reek",
            "acklay", "sarlacc", "krayt-dragon", "mynock", "porg", "loth-cat",
            "purrgil", "exogorth", "zillo-beast", "rathtar", "varactyl",

            # Droids & Tech
            "droid", "astromech", "protocol", "battle-droid", "probe-droid",
            "assassin-droid", "medical-droid", "gonk-droid", "mouse-droid",
            "r2unit", "bb-unit", "c-unit", "ig-unit", "hk-unit",

            # Weapons & Equipment
            "lightsaber", "blaster", "bowcaster", "vibroblade", "electrostaff",
            "thermal-detonator", "ion-cannon", "turbolaser", "photon-torpedo",
            "proton-torpedo", "seismic-charge", "disruptor", "slugthrower",

            # Structures & Locations
            "temple", "citadel", "fortress", "stronghold", "bastion", "sanctuary",
            "academy", "enclave", "monastery", "palace", "cathedral",
            "base", "outpost", "station", "garrison", "bunker", "depot",
            "cantina", "hangar", "bay", "dock", "spaceport", "starport",
            "arena", "colosseum", "pit", "chamber", "throne-room", "council-chamber",

            # Force & Mysticism
            "holocron", "kyber-crystal", "focusing-crystal", "adegan-crystal",
            "meditation-chamber", "vergence", "nexus", "wellspring",

            # Misc Star Wars Elements
            "fleet", "armada", "squadron", "wing", "flight", "battalion",
            "legion", "company", "platoon", "squad", "cell", "sector",
            "system", "cluster", "expanse", "nebula", "hyperspace", "parsec",
            "senate", "council", "tribunal", "assembly", "conclave",
            "chancellor", "senator", "emperor", "queen", "king", "prince",
            "princess", "duchess", "viceroy", "governor", "prefect",
            "smuggler", "scavenger", "hunter", "bounty-hunter", "mercenary",
            "pirate", "raider", "marauder", "scoundrel", "rogue",

            # Easter Egg References (subtle - no direct character names per licensing)
            "skywalker", "solo", "organa", "kenobi", "vader", "palpatine",
            "maul", "dooku", "grievous", "tarkin", "thrawn", "veers",
            "binks", "fett", "calrissian", "antilles", "ackbar", "mothma",
        ]
        
        # Expanded Verbs - Combat, Force Powers, Technical Actions
        self.verbs = [
            # Combat Actions
            "strike", "attack", "defend", "assault", "charge", "rush", "blitz",
            "flank", "ambush", "raid", "siege", "blockade", "bombard", "strafe",
            "dogfight", "duel", "parry", "riposte", "counter", "feint",
            "pierce", "cut", "slash", "stab", "thrust", "cleave", "sever",

            # Tactical Maneuvers
            "patrol", "scout", "reconnoiter", "surveil", "observe", "monitor",
            "hunt", "pursue", "chase", "track", "trail", "follow", "tail",
            "evade", "escape", "flee", "withdraw", "retreat", "disengage",
            "infiltrate", "penetrate", "breach", "invade", "occupy", "secure",
            "sabotage", "disrupt", "undermine", "subvert", "corrupt",
            "deploy", "mobilize", "position", "station", "garrison",
            "engage", "encounter", "confront", "challenge", "oppose",
            "advance", "progress", "push", "drive", "surge", "storm",

            # Force Powers & Jedi/Sith Abilities
            "levitate", "lift", "push", "pull", "throw", "grip", "choke",
            "persuade", "influence", "dominate", "control", "manipulate",
            "foresee", "predict", "sense", "perceive", "detect", "discern",
            "meditate", "commune", "attune", "harmonize", "balance",
            "heal", "restore", "revitalize", "rejuvenate", "mend",
            "absorb", "dissipate", "nullify", "negate", "resist",
            "channel", "focus", "concentrate", "amplify", "project",
            "deflect", "reflect", "redirect", "parry", "block",
            "augment", "enhance", "empower", "strengthen", "fortify",

            # Command & Leadership
            "command", "order", "direct", "coordinate", "organize",
            "lead", "guide", "spearhead", "rally", "inspire", "motivate",
            "obey", "follow", "serve", "submit", "comply",
            "rebel", "resist", "defy", "oppose", "challenge",
            "surrender", "yield", "capitulate", "concede",
            "negotiate", "bargain", "parley", "treat", "arbitrate",

            # Technical & Engineering
            "pilot", "navigate", "steer", "maneuver", "helm",
            "fly", "soar", "glide", "dive", "climb", "barrel-roll",
            "land", "dock", "berth", "anchor", "ground",
            "launch", "takeoff", "liftoff", "ascend",
            "jump", "warp", "hyperspace", "lightspeed",
            "hack", "slice", "crack", "bypass", "override",
            "decode", "decrypt", "decipher", "translate",
            "encrypt", "encode", "scramble", "cipher",
            "repair", "fix", "mend", "patch", "restore",
            "construct", "build", "assemble", "fabricate", "engineer",
            "calibrate", "tune", "adjust", "optimize", "configure",

            # Scanning & Detection
            "scan", "probe", "sweep", "search", "survey",
            "detect", "identify", "recognize", "pinpoint",
            "track", "trace", "locate", "find", "discover",
            "analyze", "examine", "inspect", "investigate", "study",
            "calculate", "compute", "process", "determine",
            "transmit", "broadcast", "signal", "relay", "communicate",

            # Weapons & Combat Tech
            "fire", "shoot", "blast", "discharge", "volley",
            "zap", "electrify", "shock", "jolt", "stun",
            "freeze", "immobilize", "paralyze", "disable",
            "burn", "scorch", "incinerate", "vaporize",
            "explode", "detonate", "burst", "rupture",
            "implode", "collapse", "crush", "compress",
            "shatter", "fragment", "splinter", "break",
            "ignite", "kindle", "spark", "light",
            "extinguish", "quench", "douse", "snuff",
            "activate", "engage", "trigger", "initiate",
            "deactivate", "disengage", "shutdown", "terminate",

            # Stealth & Subterfuge
            "cloak", "conceal", "hide", "mask", "shroud",
            "phase", "shift", "warp", "bend", "distort",
            "smuggle", "traffic", "bootleg", "run",
            "scavenge", "salvage", "reclaim", "recover", "retrieve",
            "trade", "barter", "exchange", "deal", "transact",

            # Defensive Actions
            "shield", "protect", "guard", "defend", "safeguard",
            "armor", "reinforce", "strengthen", "harden",
            "fortify", "entrench", "barricade", "secure",
            "warn", "alert", "notify", "signal", "advise",
        ]
        
        # Expanded Adjectives - Force-aligned, Ship types, Character traits
        self.adjectives = [
            # Faction & Alignment
            "imperial", "rebel", "republic", "separatist", "resistance",
            "first-order", "mandalorian", "jedi", "sith", "grey",
            "light-side", "dark-side", "balanced", "neutral", "independent",

            # Force & Mystical
            "force-sensitive", "force-strong", "force-attuned", "prescient",
            "telepathic", "empathic", "clairvoyant", "prophetic",
            "enlightened", "corrupted", "tempted", "fallen", "redeemed",
            "meditative", "contemplative", "mindful", "aware",

            # Scale & Scope
            "galactic", "planetary", "stellar", "cosmic", "universal",
            "sector-wide", "system-wide", "quadrant", "regional", "local",
            "solar", "lunar", "orbital", "atmospheric", "stratospheric",

            # Technology Level
            "quantum", "hyper", "ultra", "mega", "super", "turbo",
            "advanced", "cutting-edge", "state-of-art", "next-gen",
            "primitive", "ancient", "archaic", "obsolete", "deprecated",
            "prototype", "experimental", "beta", "alpha", "production",
            "standard", "regulation", "mil-spec", "civilian", "commercial",

            # Stealth & Visibility
            "stealth", "cloaked", "invisible", "phased", "shadow",
            "covert", "classified", "black-ops", "secret", "confidential",
            "hidden", "concealed", "masked", "shrouded", "veiled",
            "overt", "visible", "exposed", "revealed", "obvious",

            # Color & Appearance
            "dark", "light", "bright", "dim", "luminous", "radiant",
            "crimson", "scarlet", "ruby", "blood-red",
            "azure", "cobalt", "sapphire", "cerulean",
            "emerald", "jade", "verdant", "viridian",
            "golden", "amber", "aureate", "gilt",
            "silver", "argent", "platinum", "chrome",
            "bronze", "copper", "brass", "rust",
            "iron", "steel", "titanium", "durasteel", "beskar",
            "obsidian", "onyx", "ebon", "jet-black",

            # Historical & Legendary
            "ancient", "primordial", "prehistoric", "antediluvian",
            "legendary", "mythical", "fabled", "storied",
            "epic", "saga-worthy", "monumental", "historic",
            "forgotten", "lost", "rediscovered", "unearthed",

            # Character Traits - Heroic
            "heroic", "valiant", "gallant", "courageous", "brave",
            "noble", "honorable", "virtuous", "righteous", "just",
            "loyal", "faithful", "devoted", "steadfast", "unwavering",
            "wise", "sage", "learned", "enlightened", "astute",
            "compassionate", "merciful", "benevolent", "kind", "gentle",

            # Character Traits - Villainous
            "ruthless", "merciless", "cruel", "vicious", "brutal",
            "savage", "barbaric", "feral", "bestial", "monstrous",
            "cunning", "devious", "scheming", "manipulative", "treacherous",
            "sly", "crafty", "wily", "shrewd", "calculating",
            "traitorous", "perfidious", "disloyal", "faithless",
            "infamous", "notorious", "feared", "dreaded", "terrible",

            # Combat & Military
            "tactical", "strategic", "operational", "logistical",
            "aggressive", "offensive", "defensive", "fortified",
            "elite", "crack", "special-forces", "commando",
            "veteran", "seasoned", "battle-hardened", "war-torn",
            "rookie", "green", "untested", "raw", "fresh",

            # Speed & Motion
            "swift", "rapid", "quick", "fast", "lightning",
            "blazing", "supersonic", "hypersonic", "light-speed",
            "slow", "plodding", "lumbering", "sluggish", "ponderous",
            "agile", "nimble", "acrobatic", "dexterous", "lithe",

            # Power & Strength
            "powerful", "mighty", "potent", "formidable", "imposing",
            "strong", "robust", "sturdy", "solid", "stalwart",
            "weak", "feeble", "frail", "fragile", "delicate",
            "overwhelming", "crushing", "devastating", "cataclysmic",

            # Size & Mass
            "massive", "colossal", "gigantic", "enormous", "titanic",
            "heavy", "weighty", "ponderous", "bulky", "hefty",
            "light", "lightweight", "feather", "gossamer",
            "tiny", "minuscule", "diminutive", "compact", "pocket",

            # Mystery & Knowledge
            "mysterious", "enigmatic", "cryptic", "inscrutable", "arcane",
            "esoteric", "occult", "mystical", "supernatural", "paranormal",
            "unknown", "unexplored", "uncharted", "undiscovered",

            # Moral Alignment
            "lawful", "orderly", "disciplined", "regulated", "controlled",
            "chaotic", "anarchic", "wild", "untamed", "rogue",
            "rogue", "maverick", "independent", "free", "unbound",
            "outlaw", "criminal", "illicit", "illegal", "banned",
        ]

        # Expanded Adverbs - Combat styles, Force techniques, Manner of action
        self.adverbs = [
            # Speed & Tempo
            "swiftly", "rapidly", "quickly", "speedily", "hastily",
            "slowly", "gradually", "steadily", "patiently", "methodically",
            "instantly", "immediately", "suddenly", "abruptly", "spontaneously",

            # Stealth & Subtlety
            "stealthily", "silently", "quietly", "noiselessly", "soundlessly",
            "covertly", "secretly", "clandestinely", "surreptitiously",
            "subtly", "discreetly", "inconspicuously", "unobtrusively",

            # Volume & Intensity
            "loudly", "thunderously", "deafeningly", "resoundingly",
            "softly", "gently", "delicately", "tenderly", "lightly",
            "intensely", "fervently", "passionately", "zealously", "ardently",

            # Force & Violence
            "fiercely", "ferociously", "savagely", "viciously", "violently",
            "brutally", "ruthlessly", "mercilessly", "remorselessly",
            "aggressively", "belligerently", "combatively", "militantly",

            # Intelligence & Cunning
            "cunningly", "cleverly", "shrewdly", "astutely", "sagaciously",
            "slyly", "craftily", "artfully", "deceptively", "deviously",
            "wisely", "prudently", "judiciously", "sensibly", "rationally",

            # Morality & Honor
            "heroically", "valiantly", "courageously", "bravely", "gallantly",
            "nobly", "honorably", "virtuously", "righteously", "justly",
            "shamefully", "dishonorably", "ignominiously", "disgracefully",

            # Mystery & Enigma
            "mysteriously", "enigmatically", "cryptically", "inscrutably",
            "eerily", "uncannily", "strangely", "oddly", "peculiarly",

            # Tactical Approach
            "tactically", "strategically", "operationally", "methodically",
            "systematically", "precisely", "accurately", "exactly", "perfectly",
            "carelessly", "haphazardly", "recklessly", "rashly", "impulsively",

            # Visibility & Openness
            "openly", "overtly", "publicly", "blatantly", "flagrantly",
            "privately", "discreetly", "confidentially", "intimately",

            # Effectiveness & Efficiency
            "efficiently", "effectively", "productively", "optimally",
            "masterfully", "expertly", "skillfully", "adeptly", "deftly",
            "clumsily", "awkwardly", "ineptly", "incompetently",

            # Power & Force
            "powerfully", "mightily", "forcefully", "vigorously", "energetically",
            "strongly", "robustly", "stoutly", "heartily",
            "weakly", "feebly", "limply", "languidly",

            # Determination & Will
            "determinedly", "resolutely", "steadfastly", "unwaveringly",
            "persistently", "doggedly", "tenaciously", "stubbornly",
            "reluctantly", "hesitantly", "tentatively", "uncertainly",
        ]
        
        self.symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '+', '-', '=', '~']
    
    def _get_random_word(self, word_type: str) -> List[str]:
        """
        Retrieve random word from tactical vocabulary database.

        Hyphenated vocabulary words (like "millennium-falcon" or "ig-unit")
        are split into components, with each component counting as a word.
        This allows compound terms to fill multiple word slots naturally.

        Args:
            word_type: Type of word ("noun", "verb", "adjective", "adverb")

        Returns:
            List of word components (single word or split hyphenated compound)
        """
        if word_type == "noun":
            word = random.choice(self.nouns)
        elif word_type == "verb":
            word = random.choice(self.verbs)
        elif word_type == "adjective":
            word = random.choice(self.adjectives)
        elif word_type == "adverb":
            word = random.choice(self.adverbs)
        else:
            word = random.choice(self.nouns)

        # Split hyphenated compounds into components
        # "millennium-falcon" becomes ["millennium", "falcon"] (2 words)
        return word.split("-")
    
    def _apply_grammar(self, word_count: int) -> List[str]:
        """
        Apply narrative grammar patterns that tell Star Wars stories.

        Creates storytelling patterns like:
        - Character actions: "vader-pursued-rebels"
        - Ship events: "falcon-escaped-empire"
        - Location events: "hoth-base-evacuated"
        - Faction actions: "empire-blockaded-naboo"

        Randomly selects from multiple narrative patterns for variety.

        Args:
            word_count: Target number of words (1-5)

        Returns:
            List of words forming a narrative name
        """
        words = []

        # 1-word: Just a noun (character, ship, or location)
        if word_count == 1:
            words.extend(self._get_random_word("noun"))
            return words[:word_count]

        # 2-word: Adjective + Noun OR Noun + Verb
        elif word_count == 2:
            # 50% chance of descriptive (adjective-noun) vs action (noun-verb)
            if random.random() < 0.5:
                # Descriptive: "imperial-fleet"
                words.extend(self._get_random_word("adjective"))
                words.extend(self._get_random_word("noun"))
            else:
                # Action: "fleet-attacked"
                words.extend(self._get_random_word("noun"))
                verb = self._get_random_word("verb")[0]
                words.append(self._to_past_tense(verb))
            return words[:word_count]

        # 3-word: Subject-Verb-Object pattern
        elif word_count == 3:
            # Pattern: "vader-pursued-rebels" or "empire-blockaded-naboo"
            # Subject (may be 1-2 words if compound)
            subject = self._get_random_word("noun")
            if len(subject) >= word_count:
                return subject[:word_count]
            words.extend(subject)

            # Verb (always 1 word after past tense)
            if len(words) < word_count:
                verb = self._get_random_word("verb")[0]
                words.append(self._to_past_tense(verb))

            # Object (fill remaining slots)
            if len(words) < word_count:
                obj = self._get_random_word("noun")
                words.extend(obj)

            return words[:word_count]

        # 4-word: Adjective + Subject + Verb + Object
        elif word_count == 4:
            # Pattern: "ancient-empire-conquered-galaxy" or "rebel-fleet-escaped-hoth"
            # Adjective (1-2 words)
            adj = self._get_random_word("adjective")
            if len(adj) >= word_count:
                return adj[:word_count]
            words.extend(adj)

            # Subject (fill more slots)
            if len(words) < word_count:
                subj = self._get_random_word("noun")
                words.extend(subj)

            # Verb (1 word)
            if len(words) < word_count:
                verb = self._get_random_word("verb")[0]
                words.append(self._to_past_tense(verb))

            # Object (fill remaining)
            if len(words) < word_count:
                obj = self._get_random_word("noun")
                words.extend(obj)

            return words[:word_count]

        # 5-word: Adverb + Adjective + Subject + Verb + Object
        else:  # word_count == 5
            # Pattern: "swiftly-imperial-fleet-blockaded-naboo"
            # Adverb (1-2 words)
            adv = self._get_random_word("adverb")
            if len(adv) >= word_count:
                return adv[:word_count]
            words.extend(adv)

            # Adjective (1-2 words)
            if len(words) < word_count:
                adj = self._get_random_word("adjective")
                words.extend(adj)

            # Subject (1-2 words)
            if len(words) < word_count:
                subj = self._get_random_word("noun")
                words.extend(subj)

            # Verb (1 word)
            if len(words) < word_count:
                verb = self._get_random_word("verb")[0]
                words.append(self._to_past_tense(verb))

            # Object (fill remaining)
            if len(words) < word_count:
                obj = self._get_random_word("noun")
                words.extend(obj)

            return words[:word_count]
    
    def _to_past_tense(self, verb: str) -> str:
        """
        Convert verb to past tense using simplified rules.

        Args:
            verb: Base verb form (single word, no hyphens)

        Returns:
            Past tense form of verb
        """
        # Simple past tense rules
        if verb.endswith('e'):
            return verb + 'd'
        elif verb.endswith('y') and len(verb) > 1 and verb[-2] not in 'aeiou':
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
            Generated suffix string (empty if none, without leading separator)
        """
        if suffix_type == "none":
            return ""
        elif suffix_type == "digits":
            return f"{random.randint(0, 999):03d}"
        elif suffix_type == "hex":
            return f"{random.randint(0, 4095):03x}"
        elif suffix_type == "symbol":
            return f"{random.choice(self.symbols)}"
        elif suffix_type == "uuid":
            return ''.join(random.choices('0123456789abcdef', k=6))
        else:
            return ""
    
    def _normalize_word_for_format(self, word: str, output_format: str) -> str:
        """
        Normalize individual word components for the target output format.

        Since compound words are already split into components by _get_random_word(),
        this only needs to handle basic case formatting for each individual word.

        Args:
            word: Single word component (no hyphens)
            output_format: Target format

        Returns:
            Normalized word with proper casing
        """
        # Simple case handling for individual word components
        if output_format in ("camel", "pascal", "space"):
            return word.capitalize()
        else:
            return word.lower()

    def _format_output(self, words: List[str], output_format: str, suffix: str) -> str:
        """
        Format words into specified output format.

        Args:
            words: List of words to format
            output_format: Desired format (kebab, snake, camel, pascal, space)
            suffix: Suffix to append (without separator)

        Returns:
            Formatted name string
        """
        # Normalize words first to handle hyphenated vocabulary items
        normalized_words = [self._normalize_word_for_format(word, output_format) for word in words]

        if output_format == "kebab":
            base = "-".join(normalized_words)
            return f"{base}-{suffix}" if suffix else base

        elif output_format == "snake":
            base = "_".join(normalized_words)
            return f"{base}_{suffix}" if suffix else base

        elif output_format == "camel":
            if not normalized_words:
                return ""
            # First word lowercase, rest capitalized
            base = normalized_words[0].lower() + "".join(word for word in normalized_words[1:])
            # For camelCase, capitalize and append suffix without separator
            suffix_capitalized = suffix.capitalize() if suffix else ""
            return base + suffix_capitalized

        elif output_format == "pascal":
            base = "".join(normalized_words)
            # For PascalCase, capitalize and append suffix without separator
            suffix_capitalized = suffix.capitalize() if suffix else ""
            return base + suffix_capitalized

        elif output_format == "space":
            # normalized_words already have proper capitalization from normalization
            base = " ".join(normalized_words)
            # For space format, append suffix with space
            return f"{base} {suffix}" if suffix else base

        else:
            # Default to kebab
            base = "-".join(word.lower() for word in words)
            return f"{base}-{suffix}" if suffix else base
    
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
