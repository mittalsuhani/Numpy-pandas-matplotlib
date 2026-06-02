import pandas as pd
import os

# Load data from CSV
base_dir = os.path.dirname(__file__)
csv_path = os.path.join(base_dir, "data_cleaning_sample.csv")
df = pd.read_csv(csv_path)
print("Original DataFrame:")
print(df)

# Handling missing values
print(df.isnull())  # Check for missing values
print(df.isnull().sum())  # Count missing values in each column

df.dropna()              # Drop rows with *any* missing values
df.dropna(axis=1)        # Drop columns with missing values

df.fillna(0)                     # Replace NaN with 0
df["Age"].fillna(df["Age"].mean())  # Replace with mean
df.ffill()      # Forward fill
df.bfill()      # Backward fill

# Handling duplicates
print(df.duplicated())  # Check for duplicate rows
print(df.duplicated().sum())  # Count duplicate rows
df.drop_duplicates()  # Drop duplicate rows
print("DataFrame after removing duplicates:")
print(df)

df.duplicated(subset=["Name", "Age"])  # Check for duplicates based on specific columns
df.drop_duplicates(subset=["Name", "Age"])  # Drop duplicates based on specific columns 