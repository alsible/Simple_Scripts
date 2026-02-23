"""File Hasher Utility
=======================

This script computes the cryptographic hash of a file using Python's
``hashlib`` library. Hash functions are commonly used to verify the
integrity of files or to generate a unique fingerprint for data. By
default the script uses SHA ‑256, but other algorithms such as MD5,
SHA–1 and SHA‑512 are available.

Features
--------

* Compute a file hash with a configurable algorithm.
* Read files in chunks to handle large files efficiently.
* List the algorithms guaranteed to be available in the Python ``hashlib``
  module.
* Handle missing files and unsupported algorithms gracefully.

Example usage::

    # Compute the SHA ‑256 hash of example.txt
    python3 File_Hasher.py example.txt

    # Compute the MD5 hash with a custom block size
    python3 File_Hasher.py example.txt -a md5 -b 4096

    # List available algorithms
    python3 File_Hasher.py --list-algorithms

"""

import argparse
import hashlib
import os
from typing import Generator


def compute_file_hash(file_path: str, algorithm: str = "sha256", block_size: int = 8192) -> str:
    """Compute the hash of a file using the specified algorithm.

    Parameters
    ----------
    file_path : str
        Path to the file to hash.
    algorithm : str, optional
        Name of the hashing algorithm. Must be one of the values listed in
        ``hashlib.algorithms_guaranteed``. Defaults to ``"sha256"``.
    block_size : int, optional
        Size of the chunks (in bytes) used when reading the file. Larger
        values may improve performance for large files. Defaults to 8192.

    Returns
    -------
    str
        Hexadecimal digest of the computed hash.

    Raises
    ------
    ValueError
        If the requested algorithm is not available.
    FileNotFoundError
        If the file cannot be found.
    """
    algorithm = algorithm.lower()
    # Validate algorithm
    if algorithm not in hashlib.algorithms_guaranteed:
        raise ValueError(
            f"Unsupported algorithm '{algorithm}'. Available algorithms: {', '.join(sorted(hashlib.algorithms_guaranteed))}"
        )

    # Attempt to open the file
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    hasher = hashlib.new(algorithm)
    with open(file_path, "rb") as file:
        while True:
            chunk = file.read(block_size)
            if not chunk:
                break
            hasher.update(chunk)
    return hasher.hexdigest()


def list_available_algorithms() -> Generator[str, None, None]:
    """Yield the names of hashing algorithms guaranteed to be available.

    Returns
    -------
    Generator[str, None, None]
        An iterator over algorithm names.
    """
    for algo in sorted(hashlib.algorithms_guaranteed):
        yield algo


def parse_args() -> argparse.Namespace:
    """Parse command -line arguments."""
    parser = argparse.ArgumentParser(
        description="Compute the cryptographic hash of a file using a chosen algorithm."
    )
    parser.add_argument(
        "file",
        metavar="FILE",
        nargs="?",
        help="Path to the file whose hash will be computed.",
    )
    parser.add_argument(
        "-a",
        "--algorithm",
        default="sha256",
        help=(
            "Hashing algorithm to use (default: %(default)s). "
            "Use --list-algorithms to see supported algorithms."
        ),
    )
    parser.add_argument(
        "-b",
        "--block-size",
        type=int,
        default=8192,
        help="Block size in bytes for reading the file (default: %(default)s).",
    )
    parser.add_argument(
        "--list-algorithms",
        action="store_true",
        help="List available hashing algorithms and exit.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.list_algorithms:
        print("Available algorithms:")
        for algo in list_available_algorithms():
            print(f"  {algo}")
        return
    if not args.file:
        print("Error: You must specify a file to hash or use --list-algorithms to list available algorithms.")
        return
    try:
        digest = compute_file_hash(args.file, args.algorithm, args.block_size)
        print(f"{args.algorithm.lower()} hash of {args.file}:\n{digest}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
