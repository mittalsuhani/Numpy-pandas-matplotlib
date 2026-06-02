import os
import pandas as pd
base_dir = os.path.dirname(__file__)
csv_path = os.path.join(base_dir, "data.csv") 
df = pd.read_csv(csv_path)
print("Original DataFrame:")
#print(df)

# sorting values
print(df.sort_values("IMDb"))  # Sort by IMDb rating
print(df.sort_values("Year", ascending=False))  # Sort by Year in descending order
df.reset_index(drop=True)  # Reset index after sorting

df2=df.sort_values(["Year","IMDb"]).copy()
df2.reset_index(drop=True,inplace=True)
df2["Rank"]=df2["IMDb"].rank(ascending=False,method='dense')
print(df2)