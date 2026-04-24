import pandas as pd

print("Starting cleaning process...")

df = pd.read_csv("data/processed/merged_data.csv")

print("Data loaded.")

df.columns = df.columns.str.strip()

df.drop_duplicates(inplace=True)

df.fillna("Unknown", inplace=True)
df['total'] = df['price'] * df['quantity']
df['order_date'] = pd.to_datetime(df['order_date'])
df['month'] = df['order_date'].dt.month

print("Feature engineering complete.")


df.to_csv("data/processed/cleaned_data.csv", index=False)

print("Cleaned data saved successfully.")
