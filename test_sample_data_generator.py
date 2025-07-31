from typing import List, Dict, IO, Union, Callable
import pytest
from mock import patch
from os import path
from csv import DictWriter
from json import dumps as json_dumps
from sample_data_generator import generate_csv_report

def test_generate_csv_report_normal():
    """
    Test normal functionality of generate_csv_report.
    """
    data = [{"statistic": "test1", "count": 5}, {"statistic": "test2", "count": 3}]
    output_csv = "test_output.csv"
    output_json = "test_output.json"

    generate_csv_report(data, output_csv, output_json)

    assert path.exists(output_csv)
    with open(output_csv, encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        rows = [row for row in reader]
        assert len(rows) == 2
        assert set([r["Summary Statistic"] for r in rows]) == {"test1", "test2"}

    assert path.exists(output_json)
    with open(output_json, encoding="utf-8") as jsonfile:
        json_data = json.load(jsonfile)
        assert json_data == {'summary': {'test1': 5, 'test2': 3}}

def test_generate_csv_report_empty_data():
    """
    Test generate_csv_report with empty data.
    """
    output_csv = "test_output.csv"
    output_json = "test_output.json"

    generate_csv_report([], output_csv, output_json)

    assert path.exists(output_csv)
    with open(output_csv, encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        rows = [row for row in reader]
        assert len(rows) == 0

def test_generate_csv_report_invalid_data():
    """
    Test generate_csv_report with invalid data (not a list of dictionaries).
    """
    output_csv = "test_output.csv"
    output_json = "test_output.json"

    with pytest.raises(ValueError):
        generate_csv_report([1, 2, 3], output_csv, output_json)

def test_generate_csv_report_missing_output_files():
    """
    Test that FileNotFoundError is raised when the directories containing the output files do not exist.
    """
    data = [{"statistic": "test1", "count": 5}]
    non_existing_output_csv = "/non/existing/path/test_output.csv"
    non_existing_output_json = "/non/existing/path/test_output.json"

    with patch('os.makedirs', side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            generate_csv_report(data, non_existing_output_csv, non_existing_output_json)