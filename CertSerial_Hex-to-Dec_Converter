#A simple Python script used with CMD or Powershell to convert serial numbers from HEX format to DEC format
import argparse

def convert_hex_to_decimal(hex_serial):
    try:
        # Convert hex to decimal
        decimal_serial = int(hex_serial, 16)
        return decimal_serial
    except ValueError:
        return "Invalid hexadecimal input."

def handle_single_serial(hex_serial, save_to_txt=False):
    decimal_serial = convert_hex_to_decimal(hex_serial)
    print(f"Decimal equivalent of {hex_serial} is {decimal_serial}")
    
    if save_to_txt:
        with open("serial_number.txt", "w") as file:
            file.write(f"Hex: {hex_serial}\nDecimal: {decimal_serial}\n")
        print("The serial number has been saved to 'serial_number.txt'.")

def handle_list_of_serials_from_file(input_file):
    output_file = "serial_numbers.txt"
    try:
        with open(input_file, "r") as file:
            hex_serial_list = [line.strip() for line in file.readlines()]
        
        with open(output_file, "w") as file:
            for hex_serial in hex_serial_list:
                decimal_serial = convert_hex_to_decimal(hex_serial)
                file.write(f"Hex: {hex_serial}\nDecimal: {decimal_serial}\n\n")
        
        print(f"The list of serial numbers has been saved to '{output_file}'.")
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Convert hexadecimal serials to decimal.")
    parser.add_argument('-hex-serial', type=str, help="Single hexadecimal serial number to convert.")
    parser.add_argument('-input_file', type=str, help="Path to the input file containing hexadecimal serial numbers.")
    parser.add_argument('-save_single', action='store_true', help="Save single serial conversion to a TXT file.")
    
    # Parse the command-line arguments
    args = parser.parse_args()
    
    if args.hex_serial:
        handle_single_serial(args.hex_serial, args.save_single)
    elif args.input_file:
        handle_list_of_serials_from_file(args.input_file)
    else:
        print("Please provide either a hexadecimal serial number or an input file.")

# Run the main function if executed from command line
if __name__ == "__main__":
    main()
