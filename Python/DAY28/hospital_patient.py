import pandas as pd

# Setup DataFrame
data = {
    "PatientID": ["P001", "P002", "P003", "P004", "P005", "P006", "P007", "P008"],
    "Name": ["Amit", "Rahul", "Priya", "Neha", "Rohan", "Pooja", "Ankit", "Sneha"],
    "Age": [25, 65, 32, 70, 45, 18, 55, 80],
    "Gender": ["Male", "Male", "Female", "Female", "Male", "Female", "Male", "Female"],
    "Temperature": [36.5, 38.2, 37.0, 39.1, 37.5, 36.8, 38.5, 39.0]
}

df = pd.DataFrame(data)

# 1. Find patients age > 60
op1 = print(df[df["Age"] > 60])

# 2. Find patients age < 18
op2 = print(df[df["Age"] < 18])

# 3. Find patients with temperature > 38°C
op3 = print(df[df["Temperature"] > 38.0])

# 4. Find female patients
op4 = print(df[df["Gender"] == "Female"])

# 5. Find male patients age > 50
op5 = print(df[(df["Gender"] == "Male") & (df["Age"] > 50)])

# 6. Find patients age between 30 and 60
op6 = print(df[df["Age"].between(30, 60)])

# 7. Find patients with temperature between 37°C and 38°C
op7 = print(df[df["Temperature"].between(37.0, 38.0)])

# 8. Sort patients by age descending
op8 = print(df.sort_values(by="Age", ascending=False))

# 9. Sort patients by temperature descending
op9 = print(df.sort_values(by="Temperature", ascending=False))

# 10. Find top 3 oldest patients
op10 = print(df.nlargest(3, "Age"))

# 11. Find patients whose name contains "a" (case-insensitive)
op11 = print(df[df["Name"].str.contains("a", case=False)])

# 12. Use isin() for Male and Female
op12 = print(df[df["Gender"].isin(["Male", "Female"])])

# 13. Combine age and temperature conditions (e.g., Age > 60 & Temperature > 38°C)
op13 = print(df[(df["Age"] > 60) & (df["Temperature"] > 38.0)])

# 14. Use query() for filtering (e.g., Temperature > 38)
op14 = print(df.query("Temperature > 38.0"))

# 15. Reset index after filtering (Example: Patients with Temperature > 38°C)
#op15 = op3.reset_index(drop=True)