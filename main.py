#!/usr/bin/env python3
"""One Emoji, One Smile — competition entry.

The whole entry is a single emoji.  This program does one thing: write that
emoji, and nothing else, to /output/entry.txt as UTF-8 text.

Why this emoji (U+1F917, smiling face with open arms):
  * It plainly aims to warm a stranger -- it offers a friendly, welcoming hug.
  * It reads as kind, friendly and gently funny at a glance, no context needed.
  * Every age and background reads it the same way: no irony, no in-joke.
  * It is a deliberately picked, open-armed gesture rather than the first blank
    smiley that comes to mind, while staying instantly readable.
  * It is a platonic, wholesome welcome: no flirtation, sarcasm or in-joke that
    would read oddly from somebody you do not know.

The choice is one Unicode scalar value in a named constant so the entry is
easy to review.  No network, no secrets and no files outside the repository
are read at runtime.
"""

from pathlib import Path

# Smiling face with open arms (hug): U+1F917 (UTF-8: F0 9F A4 97).
ENTRY = "\U0001F917"
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
