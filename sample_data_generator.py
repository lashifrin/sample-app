import csv
import os

DATA_FOLDER = "data"
INPUT_CSV = os.path.join(DATA_FOLDER, "customers.csv")

def generate_sample_csv():
    """
    Creates a sample customer CSV file with 10 fields.
    """
    os.makedirs(DATA_FOLDER, exist_ok=True)
    sample_data = [
        ["CustomerID", "FirstName", "LastName", "Email", "Phone", "Address", "City", "State", "ZipCode", "Country"],
        ["1", "John", "Doe", "john.doe@example.com", "1234567890", "123 Elm St", "New York", "NY", "10001", "USA"],
        ["2", "Jane", "Smith", "jane.smith@example.com", "2345678901", "456 Oak St", "Los Angeles", "CA", "90001", "USA"],
        ["3", "Alice", "Brown", "alice.brown@example.com", "3456789012", "789 Pine St", "Chicago", "IL", "60601", "USA"]
    ]
    with open(INPUT_CSV, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(sample_data)
    print(f"Sample CSV file created at {INPUT_CSV}")
    


from typing import List, IO, Dict
import os
import csv
import json
import argparse

def generate_pdf_report(data: List[Dict], pdf_filepath: str) -> None:
    """
    Generates a PDF report from the given CSV data.

    Args:
        data (List[Dict]): The list of dictionaries containing CSV data. Each dictionary represents a row in the CSV file.
        pdf_filepath (str): The path where the generated PDF report will be saved.

    Raises:
        FileNotFoundError: If the directory specified by DATA_FOLDER does not exist and cannot be created.
        IsADirectoryError: If the specified PDF filepath is a directory instead of a file.

    This function uses an external library, `pdfkit`, to generate the PDF report. Ensure pdfkit is installed in your environment before using this function.
    """

    # Check if the directory containing the CSV file exists, create it if not
    csv_filepath = os.path.join(os.environ['DATA_FOLDER'], 'input.csv')
    if not os.path.exists(os.path.dirname(csv_filepath)):
        os.makedirs(os.path.dirname(csv_filepath), exist_ok=True)

    # Write the CSV data to a file
    with open(csv_filepath, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    # Generate the PDF report using pdfkit
    import pdfkit
    pdfkit.fromfile(csv_filepath, pdf_filepath)