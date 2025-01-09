import csv
import random
#files name required in this task
sales_data_files = "sales_data.csv"
summary_data_file = "sales_summary.csv"
def create_csv():
    """
    Create a csv file with headers
    """
    headers = ["Product", "City", "Quantity", "Price_per_unit", "Total"]
    with open(sales_data_files, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
    print("CSV file created.")

def add_sale(product, city, quantity, price_per_unit):
    total = quantity * price_per_unit
    with open(sales_data_files, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([product, city, quantity, price_per_unit, total])
    print("Sales record added.")

def generate_random_sales_data(num_records):
    products = ["Laptop", "Smartphone", "Tablet", "Headphones", "Mouse"]
    regions = ["Pokhara", "Kathmandu", "Birjung", "Ilam"]
    for _ in range(num_records):
        product = random.choice(products)
        region = random.choice(regions)
        sales = random.randint(10, 500 )  #random units sold
        price = round(random.uniform(10.0, 2000.0), 2)  #random price
        add_sale(product, region, sales, price)
    print(f"Generated {num_records} random sales records. ")


import numpy as np

def analyze_sales_data():
    sales_data = []
    # read data from the sales CSV
    with open(sales_data_files, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["Sales"] = int(row["Quantity"])
            row["price"] = float(row["Price_per_unit"])
            row["Revenue"] = row["Sales"] * row["price"]
            sales_data.append(row)
    # calculate metrics using numpy
    revenues = np.array([row["Revenue"] for row in sales_data])
    average_revenue = np.mean(revenues)
    product_revenue_map = {row["Product"]: row["Revenue"] for row in sales_data}
    product_with_highest_revenue = max(product_revenue_map, key=product_revenue_map.get)
    region_revenue_map = {}
    for row in sales_data:
        region = row["City"]
        region_revenue_map[region] = region_revenue_map.get(region, 0) + row["Revenue"]
# write the summary to a new CSV    
    with open(summary_data_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Product", "total Revenue", "City"])
        for row in sales_data:
            writer.writerow([row["Product"], row["Revenue"], row["City"]])
# print summary results
    print("\nAnalysis Summary:")
    print(f"Average Revenue: ${average_revenue:.2f}")
    print(f"""Product with Highest Revenue:
        {product_with_highest_revenue} (${product_revenue_map[product_with_highest_revenue]:.2f}""")
    print("Total Revenue by Region:")
    for region, revenue in region_revenue_map.items():
        print(f" - {region}: ${revenue:.2f}")
create_csv() # sales_date.csv create with headers
generate_random_sales_data(10)
analyze_sales_data()








