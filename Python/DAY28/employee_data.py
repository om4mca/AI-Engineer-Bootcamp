import pandas as pd

# Setup DataFrame
data = {
    "EmployeeID": ["E001", "E002", "E003", "E004", "E005", "E006", "E007", "E008"],
    "Name": ["Amit", "Rahul", "Priya", "Neha", "Rohan", "Pooja", "Ankit", "Sneha"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "IT", "Finance", "IT"],
    "Age": [25, 30, 28, 35, 32, 26, 40, 29],
    "Salary": [35000, 45000, 50000, 60000, 40000, 55000, 70000, 48000]
}

df = pd.DataFrame(data)

# 1. Display IT employees
op1 = print(df[df["Department"] == "IT"])



# 2. Display employees with salary > 50000
op2 = print(df[df["Salary"] > 50000])

# 3. Display employees age < 30
op3 = print(df[df["Age"] < 30])

# 4. Display IT employees earning > 45000
op4 = print(df[(df["Department"] == "IT") & (df["Salary"] > 45000)])

# 5. Display HR or Finance employees
op5 = print(df[(df["Department"] == "HR") | (df["Department"] == "Finance")])

# 6. Display employees age between 25 and 35
op6 = print(df[df["Age"].between(25, 35)])

# 7. Find employees with salary between 40000 and 60000
op7 = print(df[df["Salary"].between(40000, 60000)])

# 8. Sort by salary descending
op8 = print(df.sort_values(by="Salary", ascending=False))

# 9. Sort by age ascending
op9 = print(df.sort_values(by="Age", ascending=True))

# 10. Sort by Department and Salary
op10 = print(df.sort_values(by=["Department", "Salary"], ascending=[True, False]))

# 11. Find top 3 highest-paid employees
op11 = print(df.nlargest(3, "Salary"))

# 12. Find employees whose name contains "a" (case-insensitive)
op12 = print(df[df["Name"].str.contains("a", case=False)])

# 13. Use isin() for IT and Finance
op13 = print(df[df["Department"].isin(["IT", "Finance"])])

# 14. Use query() for salary filtering
op14 = print(df.query("Salary > 50000"))

# 15. Reset index after filtering
#op15 =op1.reset_index(drop=True)
