import pandas as pd
import os

def process_sales_data():
    # Load CSV files
    sales_data = pd.read_csv('sales_data.csv')
    new_sales_data = pd.read_csv('new_sales_data.csv')

    # Combine data
    combined_data = pd.concat([sales_data, new_sales_data])

    # Calculate total sales per customer
    total_per_customer = combined_data.groupby('customer_id')['amount'].sum().reset_index()

    # Top 5 highest-grossing items
    top_items = combined_data.groupby('item_id')['amount'].sum().nlargest(5).reset_index()

    # Top 3 revenue customers
    top_customers = total_per_customer.nlargest(3, 'amount')

    # Generate markdown report
    with open('ProcessedSales.md', 'w') as f:
        f.write('# Processed Sales Report\n\n')
        f.write('## Combined Sales Data\n')
        f.write(total_per_customer.to_markdown(index=False))
        f.write('\n\n## Top 5 Highest-Grossing Items\n')
        f.write(top_items.to_markdown(index=False))
        f.write('\n\n## Top 3 Revenue Customers\n')
        f.write(top_customers.to_markdown(index=False))
        f.write('\n\n## Recommendations\n')
        f.write('- Focus on promoting the top 5 highest-grossing items.\n')
        f.write('- Consider offering loyalty programs to the top 3 revenue customers.\n')

if __name__ == '__main__':
    process_sales_data()
