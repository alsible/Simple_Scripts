#!/usr/bin/env python3
"""
Simple File Encryptor/Decryptor
================================

This script provides a simple command‑line interface for encrypting and decrypting
files without relying on any third‑party dependencies. It uses a basic XOR
cipher, which is **not suitable for production use** or protecting highly
sensitive data. The goal of this tool is to demonstrate how encryption and
decryption can be implemented using only Python's standard library.

**Disclaimer**
--------------

The XOR cipher implemented here offers minimal security. It can be useful for
obfuscation or educational purposes, but it should not be used to protect
confidential information. If you require strong encryption, use a library like
`cryptography` or OpenSSL instead.

Usage examples:

    # Encrypt a file with a password
    python3 Simple_File_Encryptor.py encrypt -i secrets.txt -o secrets.enc -p mypassword

    # Decrypt the file back to its original contents
    python3 Simple_File_Encryptor.py decrypt -i secrets.enc -o secrets.txt -p mypassword

You can also omit the `-p/--password` argument to be prompted interactively.

```
python3 Simple_File_Encryptor.py encrypt -i secrets.txt -o secrets.enc
```
You will be prompted to enter and confirm the password.

```
python3 Simple_File_Encryptor.py decrypt -i secrets.enc -o secrets.txt
```
You will be prompted to enter the password. If the password does not match
during decryption, the output will be unreadable, so choose and remember your
password carefully.

"""

import argparse
import getpass
import hashlib
import os
import sys


def derive_key(password: str) -> bytes:
    """Derive a 32‑byte key from the password using SHA‑256.

    This function uses the SHA‑256 hash function to derive a fixed‑length key
    from an arbitrary password string. The resulting key is used for XOR
    operations. While SHA‑256 provides a cryptographic hash, the overall
    security of this scheme is limited by the XOR cipher itself.

    Args:
        password: The password string provided by the user.

    Returns:
        A 32‑byte sequence derived from the password.
    """
    return hashlib.sha256(password.encode("utf-8")).digest()


def xor_data(data: bytes, key: bytes) -> bytes:
    """Apply XOR between data and key, repeating the key as needed.

    Args:
        data: The input byte sequence to encrypt or decrypt.
        key: The key byte sequence derived from the password.

    Returns:
        A new byte sequence resulting from XORing each byte of `data` with
        the corresponding byte of `key` (cycled).
    """
    key_len = len(key)
    return bytes(b ^ key[i % key_len] for i, b in enumerate(data))


def encrypt_file(input_path: str, output_path: str, password: str) -> None:
    """Encrypt the contents of `input_path` and write to `output_path`.

    This function reads the entire contents of the input file, derives a key
    from the password, applies XOR encryption, and writes the encrypted
    bytes to the output file. It does not modify the input file.

    Args:
        input_path: Path to the plaintext file to encrypt.
        output_path: Path where the encrypted file will be written.
        password: Password used to derive the encryption key.
    """
    with open(input_path, "rb") as f:
        data = f.read()
    key = derive_key(password)
    encrypted = xor_data(data, key)
    with open(output_path, "wb") as f:
        f.write(encrypted)


def decrypt_file(input_path: str, output_path: str, password: str) -> None:
    """Decrypt the contents of `input_path` and write to `output_path`.

    XOR encryption is symmetric: applying XOR with the same key decrypts
    encrypted data. If the incorrect password is provided, the output will
    be meaningless.

    Args:
        input_path: Path to the encrypted file.
        output_path: Path where the decrypted file will be written.
        password: Password used to derive the decryption key (must match the
            original password used for encryption).
    """
    with open(input_path, "rb") as f:
        encrypted = f.read()
    key = derive_key(password)
    decrypted = xor_data(encrypted, key)
    with open(output_path, "wb") as f:
        f.write(decrypted)


def prompt_for_password(confirm: bool = False) -> str:
    """Prompt the user for a password, optionally confirming it.

    Args:
        confirm: If True, prompt for the password twice and ensure both
            entries match. Useful for encryption to avoid typos.

    Returns:
        The password entered by the user.

    Raises:
        SystemExit: If the passwords do not match when confirmation is
            required.
    """
    password = getpass.getpass("Enter password: ")
    if confirm:
        confirm_pw = getpass.getpass("Confirm password: ")
        if password != confirm_pw:
            sys.exit("Error: passwords do not match. Aborting.")
    return password


def parse_arguments() -> argparse.Namespace:
    """Set up and parse command‑line arguments.

    Returns:
        An argparse.Namespace containing the parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description="Encrypt or decrypt files using a simple XOR cipher.",
        epilog=(
            "Note: This tool provides minimal security and should not be used to "
            "protect confidential data. Use a proper cryptographic library for "
            "strong encryption."
        ),
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Encrypt subcommand
    encrypt_parser = subparsers.add_parser(
        "encrypt", help="Encrypt a plaintext file"
    )
    encrypt_parser.add_argument(
        "-i", "--input", required=True, help="Path to the plaintext input file"
    )
    encrypt_parser.add_argument(
        "-o", "--output", required=True, help="Path to write the encrypted file"
    )
    encrypt_parser.add_argument(
        "-p",
        "--password",
        help=(
            "Password to derive the encryption key. If omitted, you will be "
            "prompted to enter one."
        ),
    )

    # Decrypt subcommand
    decrypt_parser = subparsers.add_parser(
        "decrypt", help="Decrypt an encrypted file"
    )
    decrypt_parser.add_argument(
        "-i", "--input", required=True, help="Path to the encrypted input file"
    )
    decrypt_parser.add_argument(
        "-o", "--output", required=True, help="Path to write the decrypted file"
    )
    decrypt_parser.add_argument(
        "-p",
        "--password",
        help=(
            "Password used for decryption. If omitted, you will be prompted to "
            "enter one."
        ),
    )

    return parser.parse_args()


def main() -> None:
    args = parse_arguments()

    # Expand ~ in file paths
    input_path = os.path.expanduser(args.input)
    output_path = os.path.expanduser(args.output)

    # Ensure input file exists
    if not os.path.isfile(input_path):
        sys.exit(f"Error: input file '{input_path}' does not exist.")

    # Prompt for password if not provided
    if args.password is None:
        if args.command == "encrypt":
            password = prompt_for_password(confirm=True)
        else:
            password = prompt_for_password(confirm=False)
    else:
        password = args.password

    try:
        if args.command == "encrypt":
            encrypt_file(input_path, output_path, password)
            print(f"Encrypted '{input_path}' -> '{output_path}'")
        elif args.command == "decrypt":
            decrypt_file(input_path, output_path, password)
            print(f"Decrypted '{input_path}' -> '{output_path}'")
    except Exception as e:
        sys.exit(f"Error during {args.command}: {e}")


if __name__ == "__main__":
    main()
