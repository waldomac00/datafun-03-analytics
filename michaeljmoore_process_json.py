"""
File: michaeljmoore_process_json.py

Project: DataFun-03-Analytics

Description:
    Process a JSON file (zodiac.json) to count the number of famous people for each zodiac sign
    and save the results to a text file in the 'processed' folder.

Usage:
    - Ensure utils_logger.py is present in the same directory.
    - Run this script directly or import its process_json_file() function.

Author: Michael J Moore
Date: 2025-09
"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import json
import pathlib
import sys

# Ensure project root is in sys.path for local imports
sys.path.append(str(pathlib.Path(__file__).resolve().parent))

# Import local modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

# TODO: Replace with the names of your folders
FETCHED_DATA_DIR: str = "data"
PROCESSED_DIR: str = "processed"

#####################################
# Define Functions
#####################################

def famous_people_by_zodiac(file_path: pathlib.Path) -> dict:
    """
    Reads a zodiac JSON file and returns a dictionary with zodiac sign names as keys
    and the number of famous people for each sign as values.
    """
    
    try:
        with file_path.open('r', encoding='utf-8') as file:
            zodiac_data = json.load(file)
            zodiac_signs = zodiac_data.get("zodiacSigns", [])
            famous_counts = {}
            for sign in zodiac_signs:
                sign_name = sign.get("name", "Unknown")
                famous_list = sign.get("famousPeople", [])
                famous_counts[sign_name] = len(famous_list)
            return famous_counts
    except Exception as e:
        logger.error(f"Error reading or processing JSON file: {e}")
        return {}

def process_json_file():
    """Read a JSON file, count astronauts by spacecraft, and save the result."""

    input_file: pathlib.Path = pathlib.Path(FETCHED_DATA_DIR, "zodiac.json")

    output_file: pathlib.Path = pathlib.Path(PROCESSED_DIR, "json_famous_people_by_zodiac.txt")
    
    
    famous_counts = famous_people_by_zodiac(input_file)

    # Create the output directory if it doesn't exist
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Open the output file in write mode and write the results
    with output_file.open('w') as file:
        # TODO: Update the output to describe your results
        file.write("Famous People by Zodiac:\n")
        for sign, count in famous_counts.items():
            file.write(f"{sign}: {count}\n")
    
    # Log the processing of the JSON file
    logger.info(f"Processed JSON file: {input_file}, Results saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting JSON processing...")
    process_json_file()
    logger.info("JSON processing complete.")