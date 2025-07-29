import pytest
import csv
import os
import tempfile
import shutil
from sample_data_generator import write_sample_csv, DATA_FOLDER, INPUT_CSV


class TestSampleDataGenerator:
    """Test cases for sample_data_generator module."""
    
    def setup_method(self):
        """Set up test environment before each test."""
        # Create a temporary directory for testing
        self.test_dir = tempfile.mkdtemp()
        self.original_data_folder = DATA_FOLDER
        self.original_input_csv = INPUT_CSV
        
        # Patch the global variables to use test directory
        import sample_data_generator
        sample_data_generator.DATA_FOLDER = os.path.join(self.test_dir, "data")
        sample_data_generator.INPUT_CSV = os.path.join(sample_data_generator.DATA_FOLDER, "customers.csv")
    
    def teardown_method(self):
        """Clean up after each test."""
        # Remove test directory
        shutil.rmtree(self.test_dir, ignore_errors=True)
        
        # Restore original values
        import sample_data_generator
        sample_data_generator.DATA_FOLDER = self.original_data_folder
        sample_data_generator.INPUT_CSV = self.original_input_csv
    
    def test_write_sample_csv_creates_file(self):
        """Test that write_sample_csv creates the CSV file."""
        write_sample_csv()
        
        import sample_data_generator
        assert os.path.exists(sample_data_generator.INPUT_CSV)
    
    def test_write_sample_csv_creates_directory(self):
        """Test that write_sample_csv creates the data directory."""
        write_sample_csv()
        
        import sample_data_generator
        assert os.path.exists(sample_data_generator.DATA_FOLDER)
    
    def test_write_sample_csv_file_content(self):
        """Test that the CSV file contains expected content structure."""
        write_sample_csv()
        
        import sample_data_generator
        with open(sample_data_generator.INPUT_CSV, 'r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)
        
        # Check that we have at least header + some data rows
        assert len(rows) >= 12  # Updated to expect 12 rows (header + 11 data rows)
        
        # Check header row
        expected_header = ['CustomerID', 'FirstName', 'LastName', 'Email', 'Phone', 'Address', 'City', 'State', 'ZipCode', 'Country']
        assert rows[0] == expected_header
        
        # Check that all data rows have correct number of columns
        for i, row in enumerate(rows[1:], 1):
            assert len(row) == 10, f"Row {i} should have 10 columns, got {len(row)}"
    
    def test_write_sample_csv_data_integrity(self):
        """Test that the CSV contains valid customer data."""
        write_sample_csv()
        
        import sample_data_generator
        with open(sample_data_generator.INPUT_CSV, 'r', newline='') as file:
            reader = csv.DictReader(file)
            customers = list(reader)
        
        # Check that we have customer data
        assert len(customers) > 0
        
        # Check first customer data structure
        first_customer = customers[0]
        required_fields = ['CustomerID', 'FirstName', 'LastName', 'Email', 'Phone', 'Address', 'City', 'State', 'ZipCode', 'Country']
        
        for field in required_fields:
            assert field in first_customer, f"Missing field: {field}"
            assert first_customer[field], f"Empty value for field: {field}"
    
    def test_write_sample_csv_customer_ids_are_unique(self):
        """Test that all customer IDs are unique."""
        write_sample_csv()
        
        import sample_data_generator
        with open(sample_data_generator.INPUT_CSV, 'r', newline='') as file:
            reader = csv.DictReader(file)
            customer_ids = [row['CustomerID'] for row in reader]
        
        # Check that all customer IDs are unique
        unique_ids = set(customer_ids)
        assert len(customer_ids) == len(unique_ids), f"Customer IDs should be unique. Found duplicates: {[id for id in customer_ids if customer_ids.count(id) > 1]}"
    
    def test_write_sample_csv_email_format(self):
        """Test that email addresses have valid format."""
        write_sample_csv()
        
        import sample_data_generator
        with open(sample_data_generator.INPUT_CSV, 'r', newline='') as file:
            reader = csv.DictReader(file)
            customers = list(reader)
        
        for customer in customers:
            email = customer['Email']
            assert '@' in email, f"Invalid email format: {email}"
            assert '.' in email.split('@')[1], f"Invalid email domain: {email}"
    
    def test_write_sample_csv_multiple_calls_overwrites(self):
        """Test that multiple calls to write_sample_csv overwrites the file."""
        # First call
        write_sample_csv()
        
        import sample_data_generator
        first_mtime = os.path.getmtime(sample_data_generator.INPUT_CSV)
        
        # Small delay to ensure different modification time
        import time
        time.sleep(0.1)
        
        # Second call
        write_sample_csv()
        second_mtime = os.path.getmtime(sample_data_generator.INPUT_CSV)
        
        # File should have been modified
        assert second_mtime > first_mtime, "File should be overwritten on second call"


if __name__ == "__main__":
    pytest.main([__file__])