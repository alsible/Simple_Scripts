#!/usr/bin/env python3
"""
CSV_Splitter.py

This script splits a CSV file into multiple smaller files based on a maximum
number of data lines per output file. Each output file preserves the header
row from the input file so that downstream processing can treat the split
files as standalone CSV files.

Usage:

    python CSV_Splitter.py -i input.csv -m 500 [-o output_prefix]

Arguments:
    -i / --input      Path to the input CSV file to split (required).
    -m / --max-lines  Maximum number of data lines per output file (required).
    -o / --output     Prefix for the output files (optional). If not provided,
                      the script derives a prefix from the input filename.

Examples:
    # Split "large_file.csv" into chunks of at most 1,000 lines each:
    python CSV_Splitter.py -i large_file.csv -m 1000

    # Split and use a custom output prefix
    python CSV_Splitter.py -i test.csv -m 200 -o split_part_

This script prints the names of generated files upon completion.
"""

import argparse
import csv
import os
from typing import Iterator, Iterable, List


def generate_chunks(rows: Iterable[List[str]], max_lines: int) -> Iterator[List[List[str]]]:
    """Yield successive chunks of rows, each containing at most max_lines entries."""
    chunk: List[List[str]] = []
    for row in rows:
        chunk.append(row)
        if len(chunk) >= max_lines:
            yield chunk
            chunk = []
    # yield any remaining rows
    if chunk:
        yield chunk


def split_csv(input_file: str, max_lines: int, output_prefix: str) -> List[str]:
    """
    Split the CSV at `input_file` into multiple files with at most `max_lines`
    data rows each. Returns a list of generated file names.

    :param input_file: Path to the CSV file to split
    :param max_lines: Maximum number of data rows per output file
    :param output_prefix: Prefix for the generated output file names
    :return: List of output file names
    """
    if max_lines <= 0:
        raise ValueError("max_lines must be a positive integer")

    generated_files: List[str] = []
    base_dir = os.path.dirname(os.path.abspath(input_file))
    with open(input_file, newline='', encoding='utf-8') as csv_in:
        reader = csv.reader(csv_in)
        # Read header
        header = next(reader, None)
        if header is None:
            raise ValueError("Input CSV file appears to be empty.")

        for index, chunk in enumerate(generate_chunks(reader, max_lines), start=1):
            file_number = f"{index:03d}"  # zero-padded numbering for ordering
            out_filename = f"{output_prefix}{file_number}.csv"
            out_path = os.path.join(base_dir, out_filename)
            with open(out_path, 'w', newline='', encoding='utf-8') as csv_out:
                writer = csv.writer(csv_out)
                # write header then chunk rows
                writer.writerow(header)
                writer.writerows(chunk)
            generated_files.append(out_path)
    return generated_files


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Split a CSV file into smaller chunks.")
    parser.add_argument('-i', '--input', required=True, help="Path to the input CSV file.")
    parser.add_argument('-m', '--max-lines', type=int, required=True,
                        help="Maximum number of data rows per output file.")
    parser.add_argument('-o', '--output', default=None,
                        help="Prefix for the output files (optional).")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = args.input
    max_lines = args.max_lines
    output_prefix = args.output

    # Determine output prefix if not provided
    if output_prefix is None:
        input_base = os.path.splitext(os.path.basename(input_path))[0]
        output_prefix = f"{input_base}_part_"

    try:
        generated_files = split_csv(input_path, max_lines, output_prefix)
        print(f"Generated {len(generated_files)} file(s):")
        for filename in generated_files:
            print(f"  {filename}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()
