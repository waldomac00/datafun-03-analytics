"""
Process an Excel file to count occurrences of a specific word in a column.

"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import sys

# Import from external packages
import openpyxl

# Ensure project root is in sys.path for local imports
sys.path.append(str(pathlib.Path(__file__).resolve().parent))

# Import local modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

# TODO: Replace with the names of your folders
FETCHED_DATA_DIR: str = "example_data"
PROCESSED_DIR: str = "example_processed"

#####################################
# Define Functions
#####################################

def count_word_in_column(file_path: pathlib.Path, column_letter: str, word: str) -> int:
    """Count the occurrences of a specific word in a given column of an Excel file."""
    try:
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active
        count = 0
        for cell in sheet[column_letter]:
            if cell.value and isinstance(cell.value, str):
                count += cell.value.lower().count(word.lower())
        return count
    except Exception as e:
        logger.error(f"Error reading Excel file: {e}")
        return 0

def process_excel_file():
    """Read an Excel file, count occurrences of 'GitHub' in a specific column, and save the result."""
    
    # TODO: Replace with path to your Excel data file
    input_file = pathlib.Path(FETCHED_DATA_DIR, "Feedback.xlsx")

    # TODO: Replace with path to your Excel processed file
    output_file = pathlib.Path(PROCESSED_DIR, "excel_feedback_github_count.txt")

    # TODO: Replace with the appropriate column letter for your Excel data file
    column_to_check = "A"  

    # TODO: Replace with the word you want to count from your Excel file
    word_to_count = "GitHub"

    # Call the function to count occurrences of the word in the specified column
    word_count = count_word_in_column(input_file, column_to_check, word_to_count)
    
    # Write the results to the output file    
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Open the output file in write mode and write the results
    with output_file.open('w') as file:
        # TODO: Update the output to describe your results
        file.write(f"Occurrences of '{word_to_count}' in column {column_to_check}: {word_count}\n")
    
    # Log the processing of the Excel file    
    logger.info(f"Processed Excel file: {input_file}, Word count saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting Excel processing...")
    process_excel_file()
    logger.info("Excel processing complete.")