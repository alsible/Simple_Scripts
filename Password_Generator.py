#!/usr/bin/env python3
"""
Password_Generator.py

This script generates one or more cryptographically secure random passwords.
Users can specify the number of passwords to generate, the length of each
password, and whether to include uppercase letters, lowercase letters,
digits, and punctuation characters. The generated passwords are printed to
stdout; optionally, the first password can be copied to the clipboard if
`pyperclip` is installed and the `--clipboard` flag is used.

Examples:
    # Generate one 16-character password with all character sets
    python Password_Generator.py -l 16

    # Generate five 20-character passwords without punctuation
    python Password_Generator.py -n 5 -l 20 --no-special

    # Generate a 12-character password and copy it to the clipboard
    python Password_Generator.py --clipboard
"""

import argparse
import string
import secrets
from typing import List

try:
    import pyperclip  # type: ignore
except ImportError:
    pyperclip = None  # clipboard functionality will be disabled if not installed


def build_character_pool(include_lower: bool, include_upper: bool,
                         include_digits: bool, include_special: bool) -> str:
    """Construct the character pool based on selected character types."""
    pool = ''
    if include_lower:
        pool += string.ascii_lowercase
    if include_upper:
        pool += string.ascii_uppercase
    if include_digits:
        pool += string.digits
    if include_special:
        pool += string.punctuation
    return pool


def generate_password(length: int, pool: str) -> str:
    """Generate a single password of given length from the provided pool."""
    if not pool:
        raise ValueError("Character pool is empty; enable at least one character type.")
    return ''.join(secrets.choice(pool) for _ in range(length))


def generate_passwords(count: int, length: int, include_lower: bool,
                        include_upper: bool, include_digits: bool,
                        include_special: bool) -> List[str]:
    """Generate a list of passwords according to the provided parameters."""
    pool = build_character_pool(include_lower, include_upper, include_digits, include_special)
    return [generate_password(length, pool) for _ in range(count)]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate secure random passwords.")
    parser.add_argument('-n', '--number', type=int, default=1,
                        help="Number of passwords to generate (default: 1)")
    parser.add_argument('-l', '--length', type=int, default=12,
                        help="Length of each password (default: 12)")
    parser.add_argument('--no-lower', action='store_true', help="Exclude lowercase letters")
    parser.add_argument('--no-upper', action='store_true', help="Exclude uppercase letters")
    parser.add_argument('--no-digits', action='store_true', help="Exclude digits")
    parser.add_argument('--no-special', action='store_true', help="Exclude punctuation/special characters")
    parser.add_argument('--clipboard', action='store_true',
                        help="Copy the first generated password to the clipboard (requires pyperclip)")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    include_lower = not args.no_lower
    include_upper = not args.no_upper
    include_digits = not args.no_digits
    include_special = not args.no_special

    if args.length <= 0:
        raise ValueError("Password length must be positive.")
    if args.number <= 0:
        raise ValueError("Number of passwords to generate must be positive.")

    passwords = generate_passwords(args.number, args.length,
                                   include_lower, include_upper,
                                   include_digits, include_special)
    for idx, pwd in enumerate(passwords, start=1):
        print(f"Password {idx}: {pwd}")

    if args.clipboard:
        if not pyperclip:
            print("pyperclip is not installed; cannot copy to clipboard.")
        else:
            pyperclip.copy(passwords[0])
            print("First password copied to clipboard.")

if __name__ == '__main__':
    main()
