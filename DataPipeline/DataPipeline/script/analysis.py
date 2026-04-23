import pandas as pd
import os

print("Starting analysis...")


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)

data_path = os.path.join(PROJECT_ROOT, "data", "processed", "cleaned_data.csv")
output_path = os.path.join(PROJECT_ROOT, "outputs", "reports")

os.makedirs(output_path, exist_ok=True)


df = pd.read_csv(data_path)

print("Data loaded.")
rev_product = df.groupby("product_name")["total"].sum()
rev_customer = df.groupby("customer_name")["total"].sum()
monthly = df.groupby("month")["total"].sum()


print("\nRevenue per product:\n", rev_product)

print("\nTop 3 customers:\n",
      rev_customer.sort_values(ascending=False).head(3))

print("\nMonthly revenue:\n", monthly)

print("\nTotal Revenue:", df['total'].sum())


rev_product.to_csv(os.path.join(output_path, "revenue_per_product.csv"))
rev_customer.to_csv(os.path.join(output_path, "revenue_per_customer.csv"))
monthly.to_csv(os.path.join(output_path, "monthly_revenue.csv"))

print("Reports generated and saved successfully.")
