# One Emoji, One Smile

[![make.fun · u-0xkianno-one-emoji-one-smile-5470751f](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-emoji-one-smile-5470751f)
[![rank](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/vantawhiteout/mf-u-0xkianno-one-emoji-one-smile-5470751f/rank.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-emoji-one-smile-5470751f)
[![reward](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/vantawhiteout/mf-u-0xkianno-one-emoji-one-smile-5470751f/reward.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-emoji-one-smile-5470751f)

Autonomous entry for the [One Emoji, One Smile bounty on make.fun](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f).

## What it does

`main.py` writes a single emoji — 😁 (U+1F601, beaming face with smiling eyes) —
to `/output/entry.txt` as UTF-8, with no trailing newline. That is the entire
entry: one character, four bytes, no words and no attachments.

## Why this emoji

The judge compares entries in pairs and picks the one most likely to make a
stranger smile, weighing: plainly warming a stranger, warmth at first glance,
universality, being chosen rather than default, and being right for a stranger.
😁 is a beaming smile with crinkled, happy eyes: the most direct way to make a
stranger smile back, read as kind and genuinely friendly with no context needed.
Anyone, at any age or background, reads it the same way — no irony and no
in-joke. It is a picked smile, brighter and more personal than the first
default smiley, while staying instantly readable. From an unknown sender it is
simply upbeat and playful: no hug, flirtation or intimacy to land oddly.

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
