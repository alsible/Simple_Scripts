----------------
Python_Pinger.py
----------------

This simple script takes a text file containing IP addresses (one per line) and sends a single ICMP packet to test reachability.  It takes two command‑line arguments: an input file with the IP list and the output log file name.

Example usage:

```bash
python Python_Pinger.py input_IPs.txt ping_results.txt
```

Example result:

```
192.168.1.1 responded to ping.
8.8.8.8 responded to ping.
8.8.4.4 did not respond to ping.

Log written to ping_results.txt
```

----------------
CSV_Splitter.py
----------------

This script splits a CSV file into multiple smaller files based on a maximum number of data lines per output file.  Each output file preserves the header row from the input so that it can be used independently.  You can optionally provide a custom prefix for the generated files; otherwise the script derives one from the input filename.

**Example usage:**

```bash
# Split `test.csv` into chunks with at most 500 data rows per file
python CSV_Splitter.py -i test.csv -m 500

# Split using a custom output prefix (files will be named `custom_001.csv`, `custom_002.csv`, ...)
python CSV_Splitter.py -i test.csv -m 100 -o custom_
```

Options/Arguments:

- `-i` or `--input` : input CSV file to split (required)
- `-m` or `--max-lines` : maximum number of data rows per output file (required)
- `-o` or `--output` : prefix for the output files (optional)

----------------
Bulk_Rename.py
----------------

This script renames files within the specified directory by removing a pattern that you provide as a regular expression.  It is useful when you need to strip a common prefix or suffix from filenames.

Example usage:

```bash
python Bulk_Rename.py -d /path/to/files -r "_test-txt"
```

The above command will iterate through files in `/path/to/files` and remove the string `_test-txt` wherever it appears in a filename.

Options/Arguments:

- `-d` or `--directory` : path to the directory containing the files to rename (defaults to the current working directory)
- `-r` or `--regex` : regular expression pattern to match and remove from filenames (required)

----------------
CertSerial_Hex-to-Dec_Converter.py
----------------

This Python script converts hexadecimal serial numbers into decimal format.  It supports both single serial numbers and lists of serial numbers from a text file.  Use `-hex-serial` to convert a single value or `-input_file` to convert a file containing a list of hexadecimal serial numbers.  Use `-save_single` to save the result to a text file when converting a single serial number.

Features:

- Converts hexadecimal serial numbers to decimal format
- Accepts either a single serial number or a list of serial numbers from a text file
- Saves the conversion result to a text file when requested

**Examples:**

```bash
# Convert a single hexadecimal serial number
python CertSerial_Hex-to-Dec_Converter.py -hex-serial 730000430415085efbcfa39eaa00000004304

# Convert a single serial number and save the result to serial_number.txt
python CertSerial_Hex-to-Dec_Converter.py -hex-serial 730000430415085efbcfa39eaa00000004304 -save_single

# Convert a list of serial numbers from serial_list.txt and save results to serial_numbers.txt
python CertSerial_Hex-to-Dec_Converter.py -input_file serial_list.txt
```

----------------
simple_backup_linux.sh
----------------

This Bash script performs a simple file-system backup on a Linux host.  It creates a compressed archive of a source directory, writes progress and errors to a log file, and automatically deletes backups older than seven days.  Customize `SOURCE_DIR` to point to the folder you want to back up.

Example usage:

1. Edit the `SOURCE_DIR` variable in the script to specify the directory you want to back up.
2. Run the script (ensure it is executable: `chmod +x simple_backup_linux.sh`):

```bash
./simple_backup_linux.sh
```

The script will create a `.tar.gz` archive in `/opt/backup/` with a timestamped filename and log the process to `/opt/backup/backup.log`.  Old backups (older than seven days) will be cleaned up automatically.

----------------
Password_Generator.py
----------------

This Python script generates one or more cryptographically secure random passwords. You can customize the number of passwords, the length of each password, and which character sets to include (lowercase letters, uppercase letters, digits and special characters). Optionally, you can copy the first generated password to the system clipboard if the `pyperclip` library is installed.

**Example usage:**

```bash
# Generate a single 16-character password with all character sets
python Password_Generator.py -l 16

# Generate three 24-character passwords without special characters
python Password_Generator.py -n 3 -l 24 --no-special

# Generate a default password and copy it to the clipboard
python Password_Generator.py --clipboard
```

Options/Arguments:

- `-n` or `--number` : Number of passwords to generate (default: 1)
- `-l` or `--length` : Length of each password (default: 12)
- `--no-lower` : Exclude lowercase letters
- `--no-upper` : Exclude uppercase letters
- `--no-digits` : Exclude digits
- `--no-special` : Exclude punctuation/special characters
- `--clipboard` : Copy the first generated password to the clipboard (requires `pyperclip`)

----------------
