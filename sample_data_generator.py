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
    


from typing import List, Dict, IO, Union
import os
import csv
import json
import argparse
import sys

def generate_csv_report(data: List[Dict], output_csv: str, output_json: str) -> None:
    """
    Generates a CSV summary report with statistics and counts based on the provided data.
    Writes both the CSV report and JSON summary to the specified file paths.

    Args:
        data (List[Dict]): The data from which to generate the summary report. Each item should be a dictionary.
        output_csv (str): Path to save the generated CSV report.
        output_json (str): Path to save the JSON summary of the report.

    Raises:
        FileNotFoundError: If either the output CSV or JSON files could not be created.
        ValueError: If the data is not in a suitable format for report generation.
    """

    # Ensure the directories containing the output files exist
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)
    os.makedirs(os.path.dirname(output_json), exist_ok=True)

    # Write CSV report to file
    with open(output_csv, 'w', newline='') as csvfile:
        fieldnames = ['Summary Statistic', 'Count']
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames)

        # Add row for each statistic and count in the data
        for stat_name, count in get_statistics_and_counts(data).items():
            writer.writerow([stat_name, str(count)])

    # Write JSON summary to file
    with open(output_json, 'w') as jsonfile:
        json.dump({'summary': get_statistics_and_counts(data)}, jsonfile, indent=4)