"""PassForge - a secure password generator and strength checker.

Everything lives in this one file so it's easy to read and upload.
Uses only the Python standard library.
"""

import argparse
import secrets
import string
import sys

__version__ = "1.0.0"

LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase
DIGITS = string.digits
SYMBOLS = "!@#$%^&*()-_=+[]{};:,.<>?/"

# Characters that are easy to confuse visually
AMBIGUOUS = set("l1IO0")


# ---------- password generation ----------

def build_pool(use_symbols=True, no_ambiguous=False):
    """Build the character pool for password generation."""
    pool = LOWER + UPPER + DIGITS + (SYMBOLS if use_symbols else "")
    if no_ambiguous:
        pool = "".join(c for c in pool if c not in AMBIGUOUS)
    return pool


def generate_password(length=16, use_symbols=True, no_ambiguous=False):
    """Generate a cryptographically secure random password.

    Guarantees at least one character from each selected category,
    then shuffles so the guaranteed characters aren't always at the front.
    """
    if length < 4:
        raise ValueError("Length must be at least 4")

    pool = build_pool(use_symbols, no_ambiguous)
    categories = [LOWER, UPPER, DIGITS] + ([SYMBOLS] if use_symbols else [])

    # Guarantee at least one character from each category
    chars = [secrets.choice(c) for c in categories]

    # Fill the rest randomly from the full pool
    chars += [secrets.choice(pool) for _ in range(length - len(chars))]

    # Shuffle so guaranteed characters are in random positions
    for i in range(len(chars) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        chars[i], chars[j] = chars[j], chars[i]

    return "".join(chars)


# ---------- strength checking ----------

def score_password(password):
    """Score a password from 0 to 100 based on length and variety."""
    score = 0
    length = len(password)

    # Length: up to 40 points
    if length >= 20:
        score += 40
    elif length >= 16:
        score += 32
    elif length >= 12:
        score += 24
    elif length >= 8:
        score += 16
    else:
        score += length * 2  # 1-7 chars: 2 points each

    # Character variety: up to 50 points
    if any(c.islower() for c in password):
        score += 10
    if any(c.isupper() for c in password):
        score += 10
    if any(c.isdigit() for c in password):
        score += 15
    if any(not c.isalnum() for c in password):
        score += 15

    # Long-password bonus
    if length >= 20:
        score += 10

    return min(score, 100)


def strength_label(password):
    """Return (label, score) for a password."""
    s = score_password(password)
    if s <= 40:
        return "Weak", s
    if s <= 60:
        return "Fair", s
    if s <= 80:
        return "Strong", s
    return "Very Strong", s


# ---------- command-line interface ----------

def main():
    parser = argparse.ArgumentParser(
        prog="passforge",
        description="Generate strong passwords and check password strength.",
    )
    sub = parser.add_subparsers(dest="command")

    p_gen = sub.add_parser("generate", help="Generate a strong password")
    p_gen.add_argument("--length", "-l", type=int, default=16,
                       help="Password length (default: 16, min: 4)")
    p_gen.add_argument("--no-symbols", action="store_true",
                       help="Use only letters and digits")
    p_gen.add_argument("--no-ambiguous", action="store_true",
                       help="Avoid confusing characters like l, 1, O, 0")

    p_check = sub.add_parser("check", help="Check a password's strength")
    p_check.add_argument("password", help="The password to evaluate")

    args = parser.parse_args()

    try:
        if args.command == "generate":
            pwd = generate_password(
                length=args.length,
                use_symbols=not args.no_symbols,
                no_ambiguous=args.no_ambiguous,
            )
            print(f"Generated password: {pwd}")
        elif args.command == "check":
            label, score = strength_label(args.password)
            print(f"Strength: {label.upper()} (score {score}/100)")
        else:
            parser.print_help()
            sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
