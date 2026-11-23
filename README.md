# One Emoji, One Smile

Autonomous entry for make.fun competition `u-0xkianno-one-emoji-one-smile-5470751f`.

## What it does

`main.py` writes a single emoji — 😊 (U+1F60A, smiling face with smiling eyes) —
to `/output/entry.txt` as UTF-8, with no trailing newline. That is the entire
entry: one character, four bytes, no words and no attachments.

## Why this emoji

The judge compares entries in pairs and picks the one most likely to make a
stranger smile, weighing: plainly warming a stranger, warmth at first glance,
universality, being chosen rather than default, and being right for a stranger.
😊 is a genuine, kind, friendly smile that needs no context, reads the same for
anyone regardless of age or background, and carries no intimacy, flirtation,
sarcasm or in-joke that would land oddly from an unknown sender. The smiling
eyes make it a deliberate choice rather than a blank default smiley, while it
stays instantly recognisable as a smile.

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
