from typing import List, Dict, IO, Callable, Any
import pytest
import os
import tempfile
import csv
import json
import argparse
from pdfkit import PDFKit

def _get_temp_csv_path() -> str:
    """
    Returns a temporary CSV file path.
    """
    with tempfile.TemporaryFile(mode='w', newline='') as tmp_file:
        writer = csv.DictWriter(tmp_file, fieldnames=[])
        return tmp_file.name

def _get_temp_pdf_path() -> str:
    """
    Returns a temporary PDF file path.
    """
    with tempfile.TemporaryFile(mode='wb') as tmp_file:
        return tmp_file.name

@pytest.fixture
def pdfkit_module():
    """
    A fixture to wrap the pdfkit module and ensure it is imported only once per test session.
    """
    # Importing pdfkit here avoids the circular import issue.
    from sample_data_generator import pdfkit  # noqa: F401,F403,F821
    return pdfkit

def _check_csv_content(csv_filepath: str, expected_data: List[Dict]) -> None:
    """
    Checks the content of a CSV file against an expected list of dictionaries.
    """
    with open(csv_filepath, 'r', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        assert [row for row in reader] == expected_data

def test_generate_pdf_report_normal_functionality():
    """
    Test the normal functionality of generate_pdf_report function.
    """
    data = [{"key1": "val1", "key2": "val2"}, {"key1": "val3", "key2": "val4"}]
    temp_csv_path = _get_temp_csv_path()
    temp_pdf_path = _get_temp_pdf_path()

    generate_pdf_report(data, temp_pdf_path)

    # Check if the CSV file was written correctly.
    _check_csv_content(temp_csv_path, data)

    # Check if the PDF report was generated correctly.
    assert os.path.exists(temp_pdf_path)

def test_generate_pdf_report_empty_data():
    """
    Test the behavior of generate_pdf_report function when given empty data.
    """
    data = []
    temp_csv_path = _get_temp_csv_path()
    temp_pdf_path = _get_temp_pdf_path()

    with pytest.raises(FileNotFoundError):
        generate_pdf_report(data, temp_pdf_path)

def test_generate_pdf_report_missing_fieldnames():
    """
    Test the behavior of generate_pdf_report function when the CSV data has missing fieldnames.
    """
    data = [{"key1": "val1"}]
    temp_csv_path = _get_temp_csv_path()
    temp_pdf_path = _get_temp_pdf_path()

    with pytest.raises(ValueError):
        generate_pdf_report(data, temp_pdf_path)

def test_generate_pdf_report_invalid_filepath():
    """
    Test the behavior of generate_pdf_report function when given an invalid filepath.
    """
    data = [{"key1": "val1", "key2": "val2"}]
    temp_csv_path = _get_temp_csv_path()
    temp_pdf_path = "/non/existing/path"

    with pytest.raises(FileNotFoundError):
        generate_pdf_report(data, temp_pdf_path)

def test_generate_pdf_report_directory_instead_of_file():
    """
    Test the behavior of generate_pdf_report function when the specified PDF filepath is a directory.
    """
    data = [{"key1": "val1", "key2": "val2"}]
    temp_csv_path = _get_temp_csv_path()
    temp_pdf_path = os.path.join(os.environ['DATA_FOLDER'], 'mydir')

    with pytest.raises(IsADirectoryError):
        generate_pdf_report(data, temp_pdf_path)