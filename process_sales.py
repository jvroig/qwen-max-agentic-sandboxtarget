import pandas as pd

def process_sales_data():
    # Load the CSV files into DataFrames
    sales_df = pd.read_csv('sales_data.csv')
    new_sales_df = pd.read_csv('new_sales_data.csv')

    # Combine the two dataframes
    combined_df = pd.concat([sales_df, new_sales_df], ignore_index=True)

    # Calculate total sales per customer
    combined_df['Total'] = combined_df['Quantity'] * combined_df['Price']
    customer_totals = combined_df.groupby('CustomerName')['Total'].sum().reset_index()

    # Get top 5 highest-grossing items
    item_totals = combined_df.groupby('Product')['Total'].sum().reset_index()
    top_items = item_totals.nlargest(5, 'Total')

    # Get top 3 revenue customers
    top_customers = customer_totals.nlargest(3, 'Total')

    # Generate markdown report
    with open('ProcessedSales.md', 'w') as f:
        f.write('# Processed Sales Report\n\n')
        f.write('## Combined Sales Data\n\n')
        f.write(customer_totals.to_markdown(index=False))
        f.write('\n\n## Top 5 Highest-Grossing Items\n\n')
        f.write(top_items.to_markdown(index=False))
        f.write('\n\n## Top 3 Revenue Customers\n\n')
        f.write(top_customers.to_markdown(index=False))
        f.write('\n\n## Recommendations\n\n')
        f.write('- Focus on promoting high-margin products that generate the most revenue.\n')
        f.write('- Consider offering loyalty programs to top customers to increase retention.\n')
        f.write('- Analyze purchasing patterns to optimize inventory management.\n')

if __name__ == '__main__':
    process_sales_data()