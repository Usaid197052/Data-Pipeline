import pandas as pd
import os
from sklearn.model_selection import train_test_split

print("Starting ML preparation...")


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)

data_path = os.path.join(PROJECT_ROOT, "data", "processed", "cleaned_data.csv")

# ---------------------------
# LOAD DATA
# ---------------------------
df = pd.read_csv(data_path)

print("Data loaded.")

# ---------------------------
# CREATE TARGET VARIABLE
# ---------------------------
# High value customer if total > 100
df['high_value_customer'] = df['total'] > 100

# ---------------------------
# SELECT FEATURES
# ---------------------------
X = df[['price', 'quantity']]
y = df['high_value_customer']

# ---------------------------
# TRAIN TEST SPLIT
# ---------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Train/Test split completed.")

# ---------------------------
# PRINT RESULTS
# ---------------------------
print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))

print("\nSample training data:")
print(X_train.head())

print("\nSample target values:")
print(y_train.head())

print("ML preparation complete.")