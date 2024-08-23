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
