----------------
Python_Pinger.py
----------------

This script takes in input a TXT file containing a set of IPs (one for each line), and sends one ICMP packet to test reachability.


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
