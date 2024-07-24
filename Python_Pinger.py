import os
import platform
import subprocess
import sys

def ping_ip(ip):
    """
    Ping the given IP address once and return True if it responds, otherwise False.
    """
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", ip]
    
    return subprocess.call(command) == 0

def read_ips_from_file(file_path):
    """
    Read IP addresses from a given file and return them as a list.
    """
    with open(file_path, "r") as file:
        return [line.strip() for line in file if line.strip()]

def write_log_file(file_path, log_data):
    """
    Write the log data to a specified file.
    """
    with open(file_path, "w") as file:
        file.write(log_data)

def main(input_file, output_file):
    """
    Main function to read IPs, ping them, and log the results.
    """
    ips = read_ips_from_file(input_file)
    log_data = ""
    
    for ip in ips:
        if ping_ip(ip):
            result = f"{ip} responded to ping.\n"
        else:
            result = f"{ip} did not respond to ping.\n"
        
        log_data += result
        print(result.strip())

    write_log_file(output_file, log_data)
    print(f"\nLog written to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)
