from typing import List, IO, Tuple, Callable, Dict, Any, Optional
import csv
import os
import pytest
from io import StringIO
from data_validator import CsvFormatValidator

def generate_sample_csv(data_folder: str) -> None:
    """
    Generate a sample CSV file with test data for validation testing.

    Args:
        data_folder (str): Directory to save the generated CSV file.
    """
    if not os.path.exists(data_folder):
        os.makedirs(data_folder, exist_ok=True)

    sample_data = [
        ["CustomerID", "FirstName", "LastName", "Email", "Phone", "Address", "City", "State", "ZipCode", "Country"],
        ["1", "John", "Doe", "john.doe@example.com", "123-456-7890", "123 Main St", "Anytown", "CA", "12345", "USA"],
        # Add more sample customer data here if needed
    ]

    custom_generator = generate_sample_csv_with_error(sample_data, index=2)
    with open(os.path.join(data_folder, 'sample.csv'), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows((row for row in sample_data if custom_generator is None or not custom_generator(row)))

    print(f"Sample CSV file has been created at {os.path.join(data_folder, 'sample.csv')}")

def generate_sample_csv_with_error(data: List[List[Any]], index: Optional[int] = None) -> Callable[[List[Any]], bool]:
    """
    A generator function that returns True for rows beyond a specific index to simulate errors.

    Args:
        data (List[List[Any]]): Sample customer data.
        index (Optional[int]): Index beyond which the rows will be considered invalid. Default is None, meaning no error simulation.

    Returns:
        A callable function that checks if a row should be skipped based on the given index.
    """
    if index is not None:
        for i, _ in enumerate(data):
            if i >= index:
                def skip_row(row: List[Any]):
                    return True
                yield skip_row

class TestCsvFormatValidator:
    """
    Test cases for the CsvFormatValidator class.
    """

    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        """
        Setup and teardown for test cases.
        """
        yield
        os.remove("test_csv.csv") if os.path.exists("test_csv.csv") else None

    @pytest.mark.parametrize(
        "input_content, expected_exception",
        [
            ("header1, column1\nheader2, column2\nrow1, missing_column, row3", ValueError),
            (StringIO("invalid data"), ValueError),
            (StringIO(""), ValueError),
        ],
    )
    def test_validate_csv_format_invalid(self, input_content: Union[str, IO], expected_exception: type):
        """
        Test validate_csv_format with invalid CSV content.
        """
        csv_validator = CsvFormatValidator()

        if isinstance(input_content, StringIO):
            csv_file = input_content
        else:
            csv_content = input_content
            csv_file = StringIO(csv_content)

        with pytest.raises(expected_exception):
            csv_validator.validate_csv_format(csv_file)

    @pytest.mark.parametrize(
        "input_csv_file, expected_exception",
        [
            (os.path.join("test_data", "valid_csv.csv"), None),
            (os.path.join("test_data", "missing_column_csv.csv"), ValueError),
            (os.path.join("test_data", "sample_csv_with_error.csv"), ValueError),  # New test case to handle the generated CSV file with errors
        ],
    )
    def test_validate_csv_format(self, input_csv_file: str, expected_exception: Union[type, None]):
        """
        Test validate_csv_format with valid and invalid CSV files.
        """
        csv_validator = CsvFormatValidator()

        if expected_exception is not None:
            with pytest.raises(expected_exception):
                csv_validator.validate_csv_format(open(input_csv_file, "r"))
        else:
            # Generate a sample CSV file with errors and validate it
            generate_sample_csv("temp_data")  # Use a temporary directory to ensure no existing files are overwritten
            with open("temp_data/sample.csv", "r") as csv_file:
                csv_validator.validate_csv_format(csv_file)