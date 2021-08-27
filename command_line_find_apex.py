import sys
from process_file import process_file

# Usage: $ python command_line_find_apex.py FILENAME
# Optionally set the working data limit: python command_line_find_apex.py FILENAME --working_data_limit=WORKING_DATA_LIMIT

# sys.argv[0] Needs to be command_line_find_apex.py

def run_process_file(arguments):
    filename = arguments[1] # Name of file

    if len(arguments) > 2:
        var_name, value = sys.argv[2].split("=")
        if var_name == "--working_data_limit":
            apex, index = process_file(filename, working_data_limit=int(value))
            print(f"APEX: {apex}, INDEX: {index}, RUN_WITH_WORKING_DATA_LIMIT: {value}")

            return

    apex, index = process_file(filename)
    print(f"APEX: {apex}, INDEX: {index}")

run_process_file(sys.argv)
