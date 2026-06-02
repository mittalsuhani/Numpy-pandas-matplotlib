import pandas as pd

df = pd.DataFrame({
    "Department": ["HR", "HR", "IT", "IT", "Marketing", "Marketing", "Sales", "Sales"],
    "Team": ["A", "A", "B", "B", "C", "C", "D", "D"],
    "Gender": ["M", "F", "M", "F", "M", "F", "M", "F"],
    "Salary": [85, 90, 78, 85, 92, 88, 75, 80],
    "Age": [23, 25, 30, 22, 28, 26, 21, 27],
    "JoinDate": pd.to_datetime([
        "2020-01-10", "2020-02-15", "2021-03-20", "2021-04-10",
        "2020-05-30", "2020-06-25", "2021-07-15", "2021-08-01"
    ])
})  

print("Original DataFrame:")
print(df)

print("Mean Salary by Department:")
print(df.groupby("Department")["Salary"].mean())

print("Mean Salary by Team:")
print(df.groupby("Team")["Salary"].mean())     # Average per team
print("Total Salary by Team:")
print(df.groupby("Team")["Salary"].sum())      # Total score
print("Count of Employees by Team:")
print(df.groupby("Team")["Salary"].count())    # How many entries
print("Minimum Salary by Team:")
print(df.groupby("Team")["Salary"].min())
print("Maximum Salary by Team:")
print(df.groupby("Team")["Salary"].max())

#grouping by multiple columns
print("Mean Salary by Team and Gender:")
print(df.groupby(["Team", "Gender"])["Salary"].mean())

#custom aggregation using .agg()
print("Custom Aggregation by Team:")
print(df.groupby("Team")["Salary"].agg(["mean", "max", "min"]))

df.groupby("Team")["Salary"].agg(
    avg_score="mean",
    high_score="max"
)

df.groupby("Team").agg({
    "Salary": "mean",
    "Age": "max"
})

df["Team Avg"] = df.groupby("Team")["Salary"].transform("mean")
print(df)

print(df.groupby("Team").filter(lambda x: x["Salary"].mean() > 80))
