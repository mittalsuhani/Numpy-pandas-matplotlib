import pandas as pd

employees = pd.DataFrame({
    "EmpID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"],
    "DeptID": [10, 20, 30]
})

departments = pd.DataFrame({
    "DeptID": [10, 20, 40],
    "DeptName": ["HR", "Engineering", "Marketing"]
})

print(pd.merge(employees, departments, on="DeptID"))
print(pd.merge(employees, departments, on="DeptID", how="left")) #left join :keeps all employees, fills NaN where no match.

print(pd.merge(employees, departments, on="DeptID", how="right")) #right join :keeps all departments, fills NaN where no match.

print(pd.merge(employees, departments, on="DeptID", how="outer")) #outer join : keeps all records from both tables, fills NaN where no match.

#concatinaing DataFrames
df1 = pd.DataFrame({"Name": ["Alice", "Bob"]})
df2 = pd.DataFrame({"Name": ["Charlie", "David"]})

print(pd.concat([df1, df2]))

df1 = pd.DataFrame({"ID": [1, 2]})
df2 = pd.DataFrame({"Score": [90, 80]})

print(pd.concat([df1, df2], axis=1))

