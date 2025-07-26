import csv
import os

DATA_FOLDER = "data"
INPUT_CSV = os.path.join(DATA_FOLDER, "customers.csv")

def write_sample_csv():
    """
    Creates a sample customer CSV file with 10 fields.
    """
    os.makedirs(DATA_FOLDER, exist_ok=True)
    sample_data = [
        ['CustomerID', 'FirstName', 'LastName', 'Email', 'Phone', 'Address', 'City', 'State', 'ZipCode', 'Country'],
        ['1', 'John', 'Doe', 'john.doe@example.com', '1234567890', '123 Elm St', 'New York', 'NY', '10001', 'USA'],
        ['3', 'Alice', 'Brown', 'alice.brown@example.com', '3456789012', '789 Pine St', 'Chicago', 'IL', '60601', 'USA'],
        ['4', 'Bob', 'Wilson', 'bob.wilson@example.com', '4567890123', '321 Maple St', 'Houston', 'TX', '77001', 'USA'],
        ['5', 'Fiona', 'Martinez', 'fiona.martinez@example.com', '4555555555', '150 Main St', 'San Diego', 'CA', '92101', 'USA'],
        ['5', 'Fiona', 'Martinez', 'fiona.martinez@example.com', '4555555555', '150 Main St', 'San Diego', 'CA', '92101', 'USA'],
        ['7', 'Hannah', 'Taylor', 'hannah.taylor@example.com', '4777777777', '170 Main St', 'San Jose', 'CA', '95101', 'USA'],
        ['9', 'Julia', 'Jackson', 'julia.jackson@example.com', '4999999999', '190 Main St', 'Jacksonville', 'FL', '32099', 'USA'],
        ['11', 'Lisa', 'Harris', 'lisa.harris@example.com', '5222222221', '210 Main St', 'Houston', 'TX', '77001', 'USA'],
        ['13', 'Bob', 'Wilson', 'bob.wilson@example.com', '5444444443', '230 Main St', 'Philadelphia', 'PA', '19101', 'USA'],
        ['10', 'Kevin', 'White', 'kevin.white@example.com', '5111111110', '200 Main St', 'Fort Worth', 'TX', '76101', 'USA'],
        ['12', 'Michael', 'Clark', 'michael.clark@example.com', '5333333332', '220 Main St', 'Phoenix', 'AZ', '85001', 'USA']
    ]
    with open(INPUT_CSV, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(sample_data)
    print(f"Sample CSV file created at {INPUT_CSV}")
    
