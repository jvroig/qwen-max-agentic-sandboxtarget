import pandas as pd
from collections import defaultdict

# Load the CSV files
sales_data = pd.read_csv('sales_data.csv')
new_sales_data = pd.read_csv('new_sales_data.csv')

# Standardize column names for new_sales_data
new_sales_data.columns = ['OrderID', 'CustomerName', 'Product', 'Quantity', 'Price', 'OrderDate']

# Combine the data
combined_data = pd.concat([sales_data, new_sales_data], ignore_index=True)

# Calculate total sales per customer
customer_totals = combined_data.groupby('CustomerName')['Price'].sum().reset_index()
top_customers = customer_totals.nlargest(3, 'Price')

# Calculate total revenue per product
product_totals = combined_data.groupby('Product')['Price'].sum().reset_index()
top_products = product_totals.nlargest(5, 'Price')

# Generate recommendations
recommendations = """
Recommendations:
1. Focus on promoting the top-selling products: {}, {}, and {}.
2. Consider offering discounts or loyalty programs to top customers: {}, {}, and {}.
3. Explore bundling products that are frequently purchased together.
""".format(*top_products['Product'].head(3), *top_customers['CustomerName'].head(3))

# Generate the markdown report
report_content = f"""
# Processed Sales Report

## Combined Sales Data
Total Combined Revenue: ${{combined_data['Price'].sum():.2f}}

## Top 5 Highest-Grossing Items
{{top_products.to_markdown(index=False)}}

## Top 3 Revenue Customers
{{top_customers.to_markdown(index=False)}}

## Recommendations
{{recommendations}}
"""

# Write the report to a file
with open('ProcessedSales.md', 'w') as f:
    f.write(report_content)