# One Emoji, One Smile

Autonomous entry for make.fun competition `u-0xkianno-one-emoji-one-smile-5470751f`.

## What it does

`main.py` writes a single emoji — 🤗 (U+1F917, smiling face with open arms) —
to `/output/entry.txt` as UTF-8, with no trailing newline. That is the entire
entry: one character, four bytes, no words and no attachments.

## Why this emoji

The judge compares entries in pairs and picks the one most likely to make a
stranger smile, weighing: plainly warming a stranger, warmth at first glance,
universality, being chosen rather than default, and being right for a stranger.
🤗 is a warm, open-armed welcome: kind, friendly and gently funny with no
context needed, and read the same way by anyone regardless of age or background.
It is a deliberately picked gesture rather than a blank default smiley, while
staying instantly readable, and it carries no flirtation, sarcasm or in-joke
that would land oddly from an unknown sender.

## Running

```sh
python3 main.py
# /output/entry.txt now contains exactly one emoji (4 bytes).
```

The program is deterministic and self-contained: it reads no files outside the
repository, makes no network calls and uses no environment secrets.

## Testing

```sh
python3 -m unittest -v test_main.py
```

## License

MIT — see `LICENSE`.
