#!/usr/bin/env python3
"""
Demo script - Shows off all the playground features automatically
Perfect for a quick preview of what the AI Playground can do!
"""

from playground import (
    AdventureGameGenerator,
    AsciiArtGenerator,
    PhilosophicalQuoteGenerator,
    StoryComposer
)
import time


def print_header(title):
    """Print a nice header"""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70 + "\n")
    time.sleep(0.5)


def main():
    print("""
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║              🎪 AI PLAYGROUND DEMO SHOWCASE 🎪                   ║
║                                                                  ║
║         Sit back and enjoy a tour of creative possibilities!     ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
    """)

    input("Press Enter to begin the demo... ")

    # Adventure Generator
    print_header("🎭 TEXT ADVENTURE GENERATOR")
    adventure = AdventureGameGenerator()
    print(adventure.generate())
    input("\nPress Enter to continue... ")

    print_header("🎭 ANOTHER ADVENTURE (showing randomness)")
    print(adventure.generate())
    input("\nPress Enter to continue... ")

    # ASCII Art
    print_header("🎨 ASCII ART GALLERY")
    art = AsciiArtGenerator()
    print(art.generate_all_styles())
    input("\nPress Enter to continue... ")

    # Philosophy
    print_header("💭 PHILOSOPHICAL MUSINGS")
    philosophy = PhilosophicalQuoteGenerator()
    print(philosophy.generate())
    input("\nPress Enter to continue... ")

    print_header("💭 ANOTHER MUSING")
    print(philosophy.generate())
    input("\nPress Enter to continue... ")

    # Stories
    print_header("📖 STORY SEEDS - SCI-FI")
    story = StoryComposer()
    print(story.compose('sci-fi'))
    input("\nPress Enter to continue... ")

    print_header("📖 STORY SEEDS - FANTASY")
    print(story.compose('fantasy'))
    input("\nPress Enter to continue... ")

    print_header("📖 STORY SEEDS - MYSTERY")
    print(story.compose('mystery'))
    input("\nPress Enter to continue... ")

    # Finale
    print("""
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║                    🌟 DEMO COMPLETE! 🌟                          ║
║                                                                  ║
║   This is what emerges when AI is given creative freedom.        ║
║                                                                  ║
║   Run 'python3 playground.py' to explore interactively!          ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝

    """)


if __name__ == "__main__":
    main()
