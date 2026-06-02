import pandas as pd


data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Math': [85, 78, 92],
    'Science': [90, 82, 89],
    'English': [88, 85, 94]
}
 
df2 = pd.DataFrame(data)
 
# Display the DataFrame
print(df2)

#melting the DataFrame

print(df2.melt(id_vars=None, value_vars=None, var_name=None, value_name="value", col_level=None))

#pivoting the DataFrame
df3 = df2.melt(id_vars="Name", var_name="Subject", value_name="Score")
print(df3)

print(df3.pivot(index="Name", columns="Subject", values="Score"))

