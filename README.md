# PassForge 🔐

A simple, secure command-line tool to **generate strong passwords** and **check password strength** — built with Python's standard library only. No dependencies, no tracking, everything runs locally on your machine.

## Why PassForge?

Weak passwords are one of the biggest causes of hacked accounts. PassForge helps you create random, strong passwords and tells you how strong (or weak) your existing ones are — useful for everyone, not just developers.

## Features

- 🔑 Generate strong random passwords (customizable length & character types)
- 📊 Check the strength of any password (Weak / Fair / Strong / Very Strong)
- 🚫 Exclude ambiguous characters (like `l`, `1`, `O`, `0`) for easy typing
- 🔒 Uses Python's `secrets` module — cryptographically secure randomness
- 📁 Single-file design — the whole tool is one `passforge.py` file
- 🧪 Fully tested

## Installation

```bash
git clone https://github.com/ekramul-bd/passforge.git
cd passforge
pip install -e .
```

## Usage

Generate a password (default: 16 characters):

```bash
passforge generate
passforge generate --length 24
passforge generate --no-symbols     # letters and digits only
passforge generate --no-ambiguous   # avoids confusing characters
```

Check a password's strength:

```bash
passforge check "myP@ssw0rd123"
# Output: Strength: STRONG (score 75/100)
```

Or run it directly without installing:

```bash
python passforge.py generate
python passforge.py check "myP@ssw0rd123"
```

## How the strength score works

Passwords are scored out of 100 based on:

| Factor | Points |
|---|---|
| Length (8+ / 12+ / 16+ / 20+ chars) | up to 40 |
| Lowercase + uppercase letters | 20 |
| Digits | 15 |
| Symbols | 15 |
| Bonus for length 20+ | 10 |

- **0–40: Weak** — don't use this anywhere
- **41–60: Fair** — okay for throwaway accounts
- **61–80: Strong** — good for most accounts
- **81–100: Very Strong** — ideal for important accounts

## Running tests

```bash
python -m pytest test_passforge.py -v
```

## License

MIT License — see [LICENSE](LICENSE). Copyright (c) 2026 Ekramul Islam.

Made with ❤️ by [ekramul-bd](https://github.com/ekramul-bd).
