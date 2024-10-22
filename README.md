----------------
Python_Pinger.py
----------------

This simple script takes in input a TXT file containing a set of IPs (one for each line), and sends one ICMP packet to test reachability.


The script takes 2 parameters, one input TXT file, and one for the output log file name.


Example Usage:

python Python_Pinger.py input_IPs.txt ping_results.txt

Example result:


192.168.1.1 responded to ping.

8.8.8.8 responded to ping.

8.8.4.4 did not respond to ping.


Log written to ping_results.txt

----------------
CSV_Splitter.py
----------------

This simple script splits an input CSV file with a maximum number of lines. 

This script may be useful if you need to split a CSV file for specific and different needs, in my case for example I used it during a migration to ease the load on the device where I needed to import the data.

Example Usage:

Python CSV_Splitter.py -i test.csv -m 500

The above command takes in input the "test.csv" file and splits it with a maximum of 500 lines per file.

Options/Arguments:

-i (input): input CSV file

-m (max-lines): maximum number of lines to be used for splitting the input CSV file

----------------
Bulk_Rename.py
----------------

This simple script renames files within the folder it's in, by removing what is specified in a regex you provide.

This script may be useful if names that follow a specific naming convention need to be renamed for specific purposes.

Example usage:

python Bulk_Rename.py -r "_test-txt"

In this case, within the same folder where the script is run, if one or more files matches the "_test-txt" string, such string will be removed from the filename.

Options/Arguments:

-r (regex): Regex to compare which is removed, if matched.


----------------
CertSerial_Hex-to-Dec_Converter.py
----------------
This Python script converts hexadecimal serial numbers into decimal format. It supports both single serial numbers and lists of serial numbers from a text file. The script can be executed via the command line using arguments such as -hex-serial for a single serial number and -input_file for a file containing multiple serial numbers.

Features
- Converts hexadecimal serial numbers to decimal format.
- Accepts either a single serial number or a list of serial numbers from a TXT file.
- Saves the conversion result to a text file when requested.

Usage:
1. Convert a single hexadecimal serial number and optionally save the result to a text file:

python script.py -hex-serial 730000430415085efbcfa39eaa00000004304

To save the result to a serial_number.txt file:

python script.py -hex-serial 730000430415085efbcfa39eaa00000004304 -save_single

2. You can convert a list of hexadecimal serial numbers by providing a TXT file:

python script.py -input_file serial_list.txt

The result will be saved to serial_numbers.txt.

3. Excel Usage
FYI, if you plan to use the results in Excel, it's important to prevent Excel from converting large decimal numbers into scientific notation or appending additional digits. To ensure serial numbers display correctly:

Option 1: Before importing data, format the column as "Text".
Option 2: Use the Excel import wizard and specify the column format as "Text".
Option 3: If you're generating a CSV, wrap large numbers in double quotes.

Command-Line Options:

-hex-serial	Single hexadecimal serial number to be converted.
-input_file	Path to a TXT file containing a list of hexadecimal serial numbers.
-save_single	(Optional) Save the result of the single conversion to a text file.

Examples:
To convert a single serial number and save it:

python script.py -hex-serial 730000430415085efbcfa39eaa00000004304 -save_single

To convert a list of serial numbers from serial_list.txt:

python script.py -input_file serial_list.txt
