import csv
import os.path
from typing import List, Union, Dict, Any

class CSVUtilities:
    """Advanced CSV processing utility class"""

    def __init__(self):
        pass

    @staticmethod
    def generate_sample_csv(num_rows: int = 10, num_cols: int = 4) -> None:
        """Generates a sample CSV file with the specified number of rows and columns.

        Args:
            num_rows (int): Number of rows in the generated CSV. Default is 10.
            num_cols (int): Number of columns in the generated CSV. Default is 4.

        Raises:
            ValueError: If either `num_rows` or `num_cols` are less than 1.

        """
        if not (1 <= num_rows and num_rows > 0):
            raise ValueError("Number of rows must be greater than or equal to 1.")

        if not (1 <= num_cols and num_cols > 0):
            raise ValueError("Number of columns must be greater than or equal to 1.")

        data = [['Sample Data'] + ['Col {}'.format(i) for i in range(1, num_cols)] for _ in range(num_rows)]
        with open('sample.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for row in data:
                writer.writerow(row)

    @staticmethod
    def merge_csvs(input_files: List[str], output_file: str) -> None:
        """Merges multiple CSV files into a single CSV file.

        Args:
            input_files (List[str]): List of paths to the input CSV files.
            output_file (str): Path to the output merged CSV file.

        Raises:
            FileNotFoundError: If any of the input files are not found.
            IOError: If there's an error while reading or writing files.

        """
        with open(output_file, 'w', newline='') as output:
            reader = csv.reader(output)
            first = True
            for input_file in input_files:
                if not os.path.isfile(input_file):
                    raise FileNotFoundError("Input file {} not found.".format(input_file))

                with open(input_file, 'r') as csvfile:
                    if first:
                        first = False
                        next(csvfile)  # Skip header row if present in the first input file
                    for row in csv.reader(csvfile):
                        reader.writerow(row)

    @staticmethod
    def split_csv(input_file: str, output_files: Dict[str, Any]) -> None:
        """Splits a CSV file into multiple output files based on column values.

        Args:
            input_file (str): Path to the input CSV file.
            output_files (Dict[str, Any]): A dictionary mapping column names to paths for the output files.

        Raises:
            FileNotFoundError: If any of the output files are not found.
            IOError: If there's an error while reading or writing files.

        """
        with open(input_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)

            for file_name, output_path in output_files.items():
                if not os.path.isdir(os.path.dirname(output_path)):
                    raise FileNotFoundError("Output directory for {} not found.".format(file_name))

                with open(output_path, 'w', newline='') as output:
                    writer = csv.DictWriter(output, fieldnames=reader.fieldnames)
                    writer.writeheader()
                    for row in reader:
                        if row[file_name]:
                            writer.writerow(row)

def main():
    """Example usage of CSVUtilities class methods."""
    CSVUtilities.generate_sample_csv(5, 3)
    input_files = ['input1.csv', 'input2.csv']
    output_file = 'merged.csv'
    CSVUtilities.merge_csvs(input_files, output_file)
    input_file = 'sample.csv'
    output_files = {'column_name': 'output1.csv', 'another_column_name': 'output2.csv'}
    CSVUtilities.split_csv(input_file, output_files)

if __name__ == "__main__":
    main()