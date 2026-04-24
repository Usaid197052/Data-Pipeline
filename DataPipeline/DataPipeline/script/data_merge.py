import pandas as pd

print("Starting data merge...")

customers = pd.read_csv("data/raw/customers.csv")
orders = pd.read_csv("data/raw/orders.csv")
products = pd.read_csv("data/raw/products.csv")

print("Files loaded successfully.")

df = orders.merge(customers, on="customer_id", how="left")

print("Orders + Customers merged.")

df = df.merge(products, on="product_id", how="left")

print("All datasets merged.")
# Save merged file
df.to_csv("data/processed/merged_data.csv", index=False)

print("Merged data saved successfully.")
