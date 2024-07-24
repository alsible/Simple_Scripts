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

----------------
