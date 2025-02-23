import pandas as pd
from collections import defaultdict

# Load the CSV files
sales_data = pd.read_csv('sales_data.csv')
new_sales_data = pd.read_csv('new_sales_data.csv')

# Standardize column names
new_sales_data.rename(columns={
    'TransID': 'OrderID',
    'CustNam': 'CustomerName',
    'Item': 'Product',
    'Qty': 'Quantity'
}, inplace=True)

# Combine the data
combined_data = pd.concat([sales_data, new_sales_data])

# Calculate total sales per item
combined_data['Total'] = combined_data['Quantity'] * combined_data['Price']
item_sales = combined_data.groupby('Product')['Total'].sum().sort_values(ascending=False)

# Top 5 highest-grossing items
top_items = item_sales.head(5)

# Calculate total sales per customer
customer_sales = combined_data.groupby('CustomerName')['Total'].sum().sort_values(ascending=False)

# Top 3 revenue customers
top_customers = customer_sales.head(3)

# Generate recommendations
recommendations = """
Recommendations:
1. Focus on promoting the top-selling items: {}.
2. Offer loyalty programs to top customers: {}.
3. Consider bundling products that are often purchased together.
""".format(", ".join(top_items.index), ", ".join(top_customers.index))

# Generate the markdown report
report_content = f"""
# Processed Sales Report

## Combined Sales Data
Total sales across all items: ${{combined_data['Total'].sum():.2f}}

## Top 5 Highest-Grossing Items
{{top_items.to_string()}}

## Top 3 Revenue Customers
{{top_customers.to_string()}}

## Recommendations
{{recommendations}}
"""

# Write the report to a markdown file
with open('ProcessedSales.md', 'w') as f:
    f.write(report_content)