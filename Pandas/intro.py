import pandas as pd
import os

# creating dataframes
data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "city": ["Delhi", "Mumbai", "Bangalore"]
}
df = pd.DataFrame(data)
print(df)

# from python lists
data = [
    ["Alice", 25],
    ["Bob", 30],
    ["Charlie", 35]
]

df = pd.DataFrame(data, columns=["Name", "Age"])
print(df)

# from dictionary of lists
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35]
}
df = pd.DataFrame(data)
print(df)

# from numpy arrays
import numpy as np
data = np.array([["Alice", 25], ["Bob", 30], ["Charlie", 35]])
df = pd.DataFrame(data, columns=["Name", "Age"])
print(df)

# from csv file (use script directory so path works regardless of CWD)
base_dir = os.path.dirname(__file__)
csv_path = os.path.join(base_dir, "data.csv")
df = pd.read_csv(csv_path)
print(df)