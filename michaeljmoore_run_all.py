"""
File: michaeljmoore_run_all.py

Purpose:
    Run all data fetching ("get") scripts first, then all data processing ("process") scripts,
    to automate the workflow for the DataFun analytics project.

Instructions:
    - Ensure all the required scripts and their dependencies are in the same directory or in your Python path.
    - This script will import and call the main() function from each module in the correct order.
    - Logs and output files will be created as defined in each individual script.

Author: Michael J Moore
Date: 2025-09-12
"""

#####################################
# Import Modules
#####################################

# Import the main() functions from each "get" script
from michaeljmoore_get_csv import main as get_csv_main
from michaeljmoore_get_excel import main as get_excel_main
from michaeljmoore_get_json import main as get_json_main
from michaeljmoore_get_text import main as get_text_main

# Import the process functions from each "process" script
from michaeljmoore_process_csv import process_csv_file
from michaeljmoore_process_excel import process_excel_file
from michaeljmoore_process_json import process_json_file
from michaeljmoore_process_text import process_text_file

#####################################
# Run All Scripts
#####################################

def run_all():
    """Run all get scripts, then all process scripts."""
    print("=== Running all data fetching scripts ===")
    get_csv_main()
    get_excel_main()
    get_json_main()
    get_text_main()

    print("=== Running all data processing scripts ===")
    process_csv_file()
    process_excel_file()
    process_json_file()
    process_text_file()

if __name__ == "__main__":
    run_all()