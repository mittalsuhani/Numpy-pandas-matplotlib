import os
import pandas as pd

base_dir = os.path.dirname(__file__)
csv_path = os.path.join(base_dir, "data.csv")

df = pd.read_csv(csv_path)
print(df)
print(df["Actor"])
print(df[["Actor", "IMDb"]])
print(df.loc[1])  # by index label
print(df.iloc[1])  # by index position
print(df.loc[8, "IMDb"])  # by index label and column name
print(df.loc[0:2, ["Actor", "Film"]])   # Rows 0 to 2, selected columns
print(df.iloc[0:2, 0:2])              # Rows and cols by index position


# fast access using .at and .iat
print(df.at[0, "Actor"])       # Fast label-based access
print(df.iat[0, 1])         # Fast position-based access

#data filtering
print(df[df["IMDb"] > 7.0])  # Filter rows where IMDb is greater than 7.0
print(df[(df["IMDb"] > 7.0) & (df["Year"] > 2020)])  # Filter rows where IMDb is greater than 7.0 and Year is greater than 2020

# querying with .query()
print(df.query("IMDb > 7.0 and Year > 2020"))  # Using query method for filtering
