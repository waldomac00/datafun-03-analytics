"""
Process a CSV file on 2020 Happiness ratings by country to analyze the `Ladder score` column and save statistics.
"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import csv
import statistics
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

# TODO: Add or replace this with a function that reads and processes your CSV file

def analyze_running_time(file_path: pathlib.Path) -> dict:
    """Analyze the Running Time column to calculate min, max, mean, and stdev."""
    try:
        # initialize an empty list to store the scores
        run_list = []
        with file_path.open('r', encoding='utf-8') as file:
            # csv.DictReader() methods to read into a DictReader so we can access named columns in the csv file
            dict_reader = csv.DictReader(file)  
            for row in dict_reader:
                try:
                    time = float(row["Running time"])  # Extract and convert to float
                    # append the score to the list
                    run_list.append(time)
                except ValueError as e:
                    logger.warning(f"Skipping invalid row: {row} ({e})")
        
        # Calculate statistics
        stats = {
            "min": min(run_list),
            "max": max(run_list),
            "mean": statistics.mean(run_list),
            "stdev": statistics.stdev(run_list) if len(run_list) > 1 else 0,
        }
        return stats
    except Exception as e:
        logger.error(f"Error processing CSV file: {e}")
        return {}

def process_csv_file():
    """Read a CSV file, analyze Running Time, and save the results."""
    
    input_file = pathlib.Path(FETCHED_DATA_DIR, "DisneyMovies_cleaned_data.csv")
    
    output_file = pathlib.Path(PROCESSED_DIR, "disney_running_time_stats.txt")
    
    # TODO: Call your new function to process YOUR CSV file
    # TODO: Create a new local variable to store the result of the function call
    stats = analyze_running_time(input_file)

    # Create the output directory if it doesn't exist
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Open the output file in write mode and write the results
    with output_file.open('w') as file:

        file.write("Running Time Statistics:\n") #
        file.write(f"Minimum: {stats['min']:.2f}\n") 
        file.write(f"Maximum: {stats['max']:.2f}\n")
        file.write(f"Mean: {stats['mean']:.2f}\n")
        file.write(f"Standard Deviation: {stats['stdev']:.2f}\n")
    
    # Log the processing of the CSV file
    logger.info(f"Processed CSV file: {input_file}, Statistics saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting CSV processing...")
    process_csv_file()
    logger.info("CSV processing complete.")