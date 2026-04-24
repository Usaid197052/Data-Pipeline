import pandas as pd

print("Starting cleaning process...")

df = pd.read_csv("data/processed/merged_data.csv")

print("Data loaded.")

df.columns = df.columns.str.strip()

# ---------------------------
# STEP 2: Remove duplicates
# ---------------------------
df.drop_duplicates(inplace=True)

# ---------------------------
# STEP 3: Handle missing values
# ---------------------------
df.fillna("Unknown", inplace=True)

# ---------------------------
# STEP 4: Create new feature (total revenue)
# ---------------------------
df['total'] = df['price'] * df['quantity']

# ---------------------------
# STEP 5: Convert date column
# ---------------------------
df['order_date'] = pd.to_datetime(df['order_date'])

# ---------------------------
# STEP 6: Extract month
# ---------------------------
df['month'] = df['order_date'].dt.month

print("Feature engineering complete.")

# ---------------------------
# STEP 7: Save cleaned data
# ---------------------------
df.to_csv("data/processed/cleaned_data.csv", index=False)

print("Cleaned data saved successfully.")
