import csv
import os.path
from io import StringIO
from typing import List, Union, Dict, Any, Callable
import pytest
from unittest.mock import patch

class TestCSVUtilities:
    """Test class for CSVUtilities"""

    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        """Automatically cleanup after each test method"""
        yield
        try:
            os.remove('sample.csv')
        except FileNotFoundError:
            pass

    def test_generate_sample_csv_normal(self):
        """Test generate_sample_csv with valid inputs and default values"""
        CSVUtilities.generate_sample_csv()
        with open('sample.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            assert list(reader) == [['Sample Data', 'Col 1', 'Col 2', 'Col 3'],
                                    ['Row 1, Col 1', 'Row 1, Col 2', 'Row 1, Col 3', ''],
                                    ['Row 2, Col 1', 'Row 2, Col 2', 'Row 2, Col 3', ''],
                                    # Add more rows as needed, keep the structure intact
                                    ]

    def test_generate_sample_csv_with_args(self):
        """Test generate_sample_csv with custom number of rows and columns"""
        CSVUtilities.generate_sample_csv(10, 5)
        with open('sample.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            assert list(reader) == [['Sample Data', 'Col 1', 'Col 2', 'Col 3', 'Col 4'],
                                    ['Row 1, Col 1', 'Row 1, Col 2', 'Row 1, Col 3', 'Row 1, Col 4', ''],
                                    # Add more rows here as needed, keep the structure intact
                                    ]

    def test_generate_sample_csv_invalid_input(self):
        """Test generate_sample_csv with invalid inputs"""
        with pytest.raises(ValueError) as excinfo:
            CSVUtilities.generate_sample_csv(-1, 5)
        assert str(excinfo.value) == "Number of rows must be greater than or equal to 1."

        with pytest.raises(ValueError) as excinfo:
            CSVUtilities.generate_sample_csv(1, -1)
        assert str(excinfo.value) == "Number of columns must be greater than or equal to 1."

    @patch('csv_utilities.CSVUtilities.merge_csvs')
    def test_main_normal(self, mock_merge_csvs):
        """Test main function with valid input files and output file"""
        CSVUtilities.main()
        mock_merge_csvs.assert_called_once()
        assert os.path.isfile('merged.csv')

    @patch('csv_utilities.CSVUtilities.merge_csvs', side_effect=FileNotFoundError)
    def test_main_input_files_not_found(self, mock_merge_csvs):
        """Test main function with input files not found"""
        with pytest.raises(SystemExit) as excinfo:
            CSVUtilities.main()
        assert str(excinfo.value.code) == "1"

    @patch('csv_utilities.CSVUtilities.split_csv')
    def test_main_normal_output_files(self, mock_split_csv):
        """Test main function with valid input file and output files"""
        CSVUtilities.main()
        mock_split_csv.assert_called_once()
        assert os.path.isfile('output1.csv')
        assert os.path.isfile('output2.csv')

    @patch('csv_utilities.CSVUtilities.split_csv', side_effect=FileNotFoundError)
    def test_main_output_files_not_found(self, mock_split_csv):
        """Test main function with output files not found"""
        with pytest.raises(SystemExit) as excinfo:
            CSVUtilities.main()
        assert str(excinfo.value.code) == "1"

    @patch('csv_utilities.CSVUtilities.split_csv')
    def test_split_csv_normal(self, mock_split_csv):
        """Test split_csv with valid input file and output files"""
        CSVUtilities.split_csv('sample.csv', {'column_name': 'output1.csv', 'another_column_name': 'output2.csv'})
        mock_split_csv.assert_called_once()
        assert os.path.isfile('output1.csv')
        assert os.path.isfile('output2.csv')

    @patch('csv_utilities.CSVUtilities.split_csv', side_effect=FileNotFoundError)
    def test_split_csv_output_files_not_found(self, mock_split_csv):
        """Test split_csv with output files not found"""
        with pytest.raises(SystemExit) as excinfo:
            CSVUtilities.split_csv('sample.csv', {'column_name': 'output1.csv', 'another_column_name': 'output2.csv'})
        assert str(excinfo.value.code) == "1"