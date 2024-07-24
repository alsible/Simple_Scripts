import os
import re
import argparse

def rename_files(directory, regex_pattern):
    # Compile the regular expression pattern
    pattern = re.compile(regex_pattern)

    # Loop through all files in the directory
    for filename in os.listdir(directory):
        # Check if the file name matches the pattern
        if pattern.search(filename):
            # Create the new filename by removing the matched pattern
            new_filename = pattern.sub('', filename)
            # Get the full path for the old and new filenames
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_filename)
            # Rename the file
            os.rename(old_file, new_file)
            print(f'Renamed: {filename} -> {new_filename}')
        else:
            print(f'No match for: {filename}')

def main():
    parser = argparse.ArgumentParser(description='Rename files in a directory based on a regular expression pattern.')
    parser.add_argument('-d', '--directory', default=os.getcwd(), help='Path to the directory containing the files to rename. Default is the current directory.')
    parser.add_argument('-r', '--regex', required=True, help='Regular expression pattern to match filenames.')

    args = parser.parse_args()

    # Debug: Print arguments
    print(f'Directory: {args.directory}')
    print(f'Regex pattern: {args.regex}')

    rename_files(args.directory, args.regex)

if __name__ == "__main__":
    main()
