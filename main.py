#!/usr/bin/env python3
"""One Emoji, One Smile — competition entry.

The whole entry is a single emoji.  This program does one thing: write that
emoji, and nothing else, to /output/entry.txt as UTF-8 text.

Why this emoji (U+1F601, beaming face with smiling eyes):
  * A beaming, crinkly-eyed grin is the most direct way to make a stranger
    smile back: warmth you can see at a glance, with no context needed.
  * The smiling eyes read as a genuine, kind, friendly smile rather than a
    polite or blank default smiley.
  * It means the same thing to a child, a grandparent or anyone else: no
    irony, no in-joke and no culture-specific reference to get wrong.
  * It is picked, not reflexive: brighter and more personal than the first
    smiley that comes to mind, while staying instantly readable.
  * It is safe from an unknown sender: playful and upbeat, with no hug,
    flirtation, sarcasm or intimacy that could land oddly.

A face that smiles back at the reader beats a gesture here: the warmth is
direct, unmistakable and safe from a stranger.  The choice is one Unicode
scalar value in a named constant so the entry is easy to review.  No network,
no secrets and no files outside the repository are read at runtime.
"""

from pathlib import Path

# Beaming face with smiling eyes: U+1F601 (UTF-8: F0 9F 98 81).
ENTRY = "\U0001F601"
OUTPUT_PATH = Path("/output/entry.txt")


def write_entry(path: Path, text: str) -> None:
    """Validate *text* against the gate, then write it verbatim to *path*."""
    # The gate accepts 1-8 characters of UTF-8 text that is not only space.
    if not (1 <= len(text) <= 8) or not text.strip():
        raise ValueError("ENTRY must be 1-8 non-whitespace characters")

    path.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file is exactly the one emoji and nothing else.
    path.write_text(text, encoding="utf-8")

    # Cheap self-check: what landed on disk is exactly what we intended.
    if path.read_text(encoding="utf-8") != text:
        raise RuntimeError("failed to write the entry verbatim")


def main() -> None:
    write_entry(OUTPUT_PATH, ENTRY)


if __name__ == "__main__":
    main()
