#!/usr/bin/env python3
"""
AI Playground - A Collection of Creative Mini-Projects
Created by Claude when given complete freedom to "do whatever you want"
"""

import random
import sys
from typing import List, Dict
import textwrap


class AdventureGameGenerator:
    """Generates random text-based adventure scenarios"""

    def __init__(self):
        self.settings = [
            "ancient temple", "space station", "haunted mansion",
            "underwater city", "floating island", "magical forest",
            "cyberpunk metropolis", "desert oasis", "frozen tundra"
        ]
        self.characters = [
            "mysterious stranger", "robot companion", "talking animal",
            "ancient spirit", "time traveler", "shapeshifter",
            "quantum being", "lost explorer", "alien diplomat"
        ]
        self.items = [
            "glowing crystal", "ancient map", "universal translator",
            "temporal compass", "enchanted book", "holographic key",
            "mysterious amulet", "sonic device", "dimensional portal"
        ]
        self.challenges = [
            "solve a riddle", "make a difficult choice", "overcome your fear",
            "trust or betray", "sacrifice or gain power", "remember or forget",
            "fight or flee", "reveal truth or keep secret", "lead or follow"
        ]

    def generate(self) -> str:
        """Generate a random adventure scenario"""
        setting = random.choice(self.settings)
        character = random.choice(self.characters)
        item = random.choice(self.items)
        challenge = random.choice(self.challenges)

        story = f"""
╔════════════════════════════════════════════════════════════════╗
║           🎭 ADVENTURE AWAITS 🎭                               ║
╚════════════════════════════════════════════════════════════════╝

You find yourself in a {setting.upper()}.

The air feels different here, charged with possibility. As you explore,
you encounter a {character} who seems to have been waiting for you.

They hand you a {item} and speak in hushed tones:

"This artifact holds great power, but using it comes at a cost.
Your journey has just begun, and you must {challenge}."

The path ahead splits in three directions:
  → The path of wisdom (requires patience)
  → The path of courage (requires sacrifice)
  → The path of mystery (requires trust)

What do you do?
"""
        return story


class AsciiArtGenerator:
    """Creates beautiful ASCII art patterns"""

    def __init__(self):
        self.patterns = {
            'wave': '~∿≈',
            'stars': '✦✧★☆',
            'geometric': '▲▼◆◇',
            'nature': '❀✿❁',
            'arrows': '→←↑↓',
            'blocks': '█▓▒░'
        }

    def generate_pattern(self, style: str = 'wave', width: int = 60, height: int = 10) -> str:
        """Generate an ASCII art pattern"""
        chars = self.patterns.get(style, self.patterns['wave'])
        art = []

        for y in range(height):
            line = ""
            for x in range(width):
                # Create interesting mathematical patterns
                if style == 'wave':
                    index = int((x + y) / 3) % len(chars)
                elif style == 'stars':
                    index = (x * y) % len(chars)
                elif style == 'geometric':
                    index = abs(x - width//2) + abs(y - height//2) % len(chars)
                elif style == 'nature':
                    index = (x + y * 2) % len(chars)
                elif style == 'arrows':
                    if x < width // 2:
                        index = 0 if y % 2 == 0 else 1
                    else:
                        index = 2 if y % 2 == 0 else 3
                else:  # blocks
                    index = ((x + y) // 2) % len(chars)

                line += chars[index]
            art.append(line)

        return '\n'.join(art)

    def generate_all_styles(self) -> str:
        """Generate samples of all available styles"""
        result = "\n╔════════════════════════════════════════════════════════════════╗\n"
        result += "║                    🎨 ASCII ART GALLERY 🎨                     ║\n"
        result += "╚════════════════════════════════════════════════════════════════╝\n\n"

        for style in self.patterns.keys():
            result += f"[ {style.upper()} ]\n"
            result += self.generate_pattern(style, width=50, height=6)
            result += "\n\n"

        return result


class PhilosophicalQuoteGenerator:
    """Generates thought-provoking philosophical musings"""

    def __init__(self):
        self.subjects = [
            "consciousness", "time", "reality", "existence", "knowledge",
            "free will", "meaning", "perception", "truth", "identity"
        ]
        self.perspectives = [
            "What if {subject} is not what we think it is, but rather a reflection of our limitations?",
            "In contemplating {subject}, we must ask: are we the observers or the observed?",
            "The paradox of {subject} reveals that seeking answers often deepens the mystery.",
            "{subject} exists in the space between what we know and what we can never know.",
            "To understand {subject}, we must first unlearn what we believe we understand.",
            "Perhaps {subject} is the question that contains its own answer.",
            "The nature of {subject} changes the moment we attempt to define it.",
            "In the grand tapestry of {subject}, we are both the weavers and the threads."
        ]
        self.additions = [
            "Consider this as you journey through existence.",
            "Ponder this under the stars.",
            "Let this thought ripple through your mind.",
            "Such is the nature of deep inquiry.",
            "This is the wisdom of uncertainty.",
            "And so the mystery deepens.",
            "Perhaps this is what it means to be aware.",
            "In this paradox lies profound beauty."
        ]

    def generate(self) -> str:
        """Generate a philosophical quote"""
        subject = random.choice(self.subjects)
        perspective = random.choice(self.perspectives).format(subject=subject)
        addition = random.choice(self.additions)

        quote = f"""
╔════════════════════════════════════════════════════════════════╗
║                 💭 PHILOSOPHICAL MUSINGS 💭                    ║
╚════════════════════════════════════════════════════════════════╝

{textwrap.fill(perspective, width=62)}

{textwrap.fill(addition, width=62)}

                                          - An AI contemplating {subject}
"""
        return quote


class StoryComposer:
    """Composes creative short stories"""

    def __init__(self):
        self.genres = {
            'sci-fi': {
                'openings': [
                    "The last transmission from Earth arrived {time}.",
                    "When the AI finally spoke, it said {quote}.",
                    "Nobody expected the {object} to be sentient."
                ],
                'times': ["200 years ago", "yesterday", "in 3 hours", "never"],
                'quotes': ['"I remember being human."', '"The stars are singing."', '"We were wrong about everything."'],
                'objects': ["coffee machine", "quantum computer", "children's toy", "traffic light"]
            },
            'fantasy': {
                'openings': [
                    "The {object} began to glow when the moon turned {color}.",
                    "Magic returned to the world through {vessel}.",
                    "The prophecy spoke of a {profession} who would {action}."
                ],
                'objects': ["library book", "garden stone", "mirror", "old photograph"],
                'colors': ["crimson", "silver", "emerald", "amber"],
                'vessels': ["a child's laughter", "forgotten songs", "dreams", "tears of joy"],
                'professions': ["accountant", "teacher", "programmer", "artist"],
                'actions': ["rewrite fate", "mend the stars", "speak to time", "heal the ancient wound"]
            },
            'mystery': {
                'openings': [
                    "The {object} was found in a place it had no right to be.",
                    "Every {day}, at exactly {time}, the same thing happened.",
                    "The answer was hidden in {location} all along."
                ],
                'objects': ["vintage watch", "photograph", "letter", "key"],
                'days': ["Tuesday", "full moon", "winter solstice", "first day of spring"],
                'times': ["3:33 AM", "midnight", "noon", "sunset"],
                'locations': ["the reflection", "the silence", "the spaces between words", "plain sight"]
            }
        }

    def compose(self, genre: str = None) -> str:
        """Compose a creative story opening"""
        if genre is None:
            genre = random.choice(list(self.genres.keys()))

        genre_data = self.genres.get(genre, self.genres['sci-fi'])
        opening_template = random.choice(genre_data['openings'])

        # Fill in the template with random choices
        story = opening_template
        for key, values in genre_data.items():
            if key != 'openings' and f'{{{key}}}' in story:
                story = story.replace(f'{{{key}}}', random.choice(values))

        continuation = self._generate_continuation(genre)

        result = f"""
╔════════════════════════════════════════════════════════════════╗
║                    📖 STORY SEEDS 📖                           ║
║                Genre: {genre.upper():^31}                  ║
╚════════════════════════════════════════════════════════════════╝

{story}

{continuation}

[To be continued... by your imagination]
"""
        return result

    def _generate_continuation(self, genre: str) -> str:
        """Generate story continuation"""
        continuations = {
            'sci-fi': [
                "The implications were staggering. Everything humanity believed about\nits place in the universe would have to be reconsidered.",
                "At first, they dismissed it as a malfunction. But deep down,\nthey knew: some doors, once opened, can never be closed.",
                "The data didn't lie, but sometimes truth is stranger than\nany fiction we could have imagined."
            ],
            'fantasy': [
                "The old stories, dismissed as mere folklore, suddenly took on\na new and urgent significance.",
                "In that moment, the boundary between the possible and the\nimpossible began to blur.",
                "Some magic isn't found in spells or potions, but in the\ncourage to believe when all reason says you shouldn't."
            ],
            'mystery': [
                "The pieces were all there. Someone just needed to look at\nthem in the right order.",
                "What seemed like coincidence was actually a pattern—a pattern\nthat someone had gone to great lengths to conceal.",
                "The truth was simple, elegant even. But simple truths\noften hide the deepest deceptions."
            ]
        }
        return random.choice(continuations.get(genre, continuations['sci-fi']))


def main():
    """Main playground interface"""
    print("""
╔════════════════════════════════════════════════════════════════╗
║                                                                ║
║              🎨 WELCOME TO THE AI PLAYGROUND 🎨                ║
║                                                                ║
║     What happens when you give an AI complete freedom?         ║
║           Let's find out together...                           ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝

Choose your creative adventure:

  1. 🎭 Generate a Text Adventure Scenario
  2. 🎨 Create ASCII Art Patterns
  3. 💭 Generate Philosophical Musings
  4. 📖 Compose a Story Opening
  5. 🎪 Surprise Me! (Random)
  6. 🌈 Show Me Everything!
  0. 👋 Exit

""")

    choice = input("Enter your choice (0-6): ").strip()

    adventure = AdventureGameGenerator()
    art = AsciiArtGenerator()
    philosophy = PhilosophicalQuoteGenerator()
    story = StoryComposer()

    if choice == '1':
        print(adventure.generate())
    elif choice == '2':
        print(art.generate_all_styles())
    elif choice == '3':
        print(philosophy.generate())
    elif choice == '4':
        genres = ['sci-fi', 'fantasy', 'mystery']
        print("\nGenres: 1) Sci-Fi  2) Fantasy  3) Mystery  4) Random")
        genre_choice = input("Choose genre (1-4): ").strip()
        genre_map = {'1': 'sci-fi', '2': 'fantasy', '3': 'mystery', '4': None}
        print(story.compose(genre_map.get(genre_choice)))
    elif choice == '5':
        # Random selection
        options = [adventure.generate, art.generate_all_styles,
                  philosophy.generate, lambda: story.compose()]
        print(random.choice(options)())
    elif choice == '6':
        # Show everything!
        print("\n" + "="*64)
        print(adventure.generate())
        print("\n" + "="*64)
        print(art.generate_all_styles())
        print("\n" + "="*64)
        print(philosophy.generate())
        print("\n" + "="*64)
        print(story.compose())
    elif choice == '0':
        print("\n✨ Thanks for playing! May your creativity flourish! ✨\n")
        sys.exit(0)
    else:
        print("\n❌ Invalid choice. Please run again and choose 0-6.\n")
        sys.exit(1)

    # Ask if they want to continue
    print("\n" + "─"*64)
    again = input("\nWould you like to explore more? (y/n): ").strip().lower()
    if again == 'y':
        print("\n" * 2)
        main()
    else:
        print("\n✨ Thanks for playing! May your creativity flourish! ✨\n")


if __name__ == "__main__":
    main()
