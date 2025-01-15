# Write a CSV Parser for Totals in Python Task Details
#Write a Python program that reads a CSV file containing numerical data.
#The file has multiple rows and columns. Each row represents a category, and each column contains numeric values.
#Your parser should calculate:
#The total for each row.
#The total for each column.
#Output the results clearly in the console.
#Sample Input File (data.csv)
#Category,Value1,Value2,Value3
#A,10,20,30
#B,5,15,25
#C,8,18,28
#D,12,22,32


import csv

def parse_csv_and_calculate_totals(file_name):
    """Parse a CSV file and calculate row and column totals."""
    row_totals = {}
    column_totals = {}

    with open(file_name, mode="r") as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames[1:]  # Exclude the "Category" column
        column_totals = {header: 0 for header in headers}  # Initialize column totals

        for row in reader:
            category = row["Category"]
            row_total = 0

            for header in headers:
                value = int(row[header])
                row_total += value
                column_totals[header] += value

            row_totals[category] = row_total

    # Output the results
    print("Row Totals:")
    for category, total in row_totals.items():
        print(f"{category}: {total}")

    print("\nColumn Totals:")
    for column, total in column_totals.items():
        print(f"{column}: {total}")

# Create sample data.csv file
def create_sample_csv():
    data = [
        ["Category", "Value1", "Value2", "Value3"],
        ["A", 10, 20, 30],
        ["B", 5, 15, 25],
        ["C", 8, 18, 28],
        ["D", 12, 22, 32],
    ]
    with open("data.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print("Sample data.csv file created.")

# Create and parse the CSV file
create_sample_csv()
parse_csv_and_calculate_totals("data.csv")
