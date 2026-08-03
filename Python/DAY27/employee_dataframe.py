import pandas as pd

# Create DataFrame
data = {
    "EmployeeID": ["E001", "E002", "E003", "E004", "E005"],
    "Name": ["Amit", "Rahul", "Priya", "Neha", "Rohan"],
    "Department": ["IT", "HR", "Finance", "IT", "Sales"],
    "Age": [25, 30, 28, 35, 32],
    "Salary": [35000, 45000, 50000, 60000, 40000]
}

df = pd.DataFrame(data)

# --- Perform Operations ---

print("1. Complete DataFrame:\n", df)
print("\n2. Columns:", df.columns.tolist())
print("\n3. Index:", df.index)
print("\n4. Shape:", df.shape)
print("\n5. Size:", df.size)
print("\n6. Data Types:\n", df.dtypes)
print("\n7. First 3 employees:\n", df.head(3))
print("\n8. Last 2 employees:\n", df.tail(2))
print("\n9. Employee Names:\n", df["Name"])
print("\n10. Name and Salary:\n", df[["Name", "Salary"]])
print("\n11. First employee:\n", df.iloc[0])

# Setting EmployeeID as index for operation 12 slicing
df_id = df.set_index("EmployeeID")
print("\n12. Employees E001 to E003:\n", df_id.loc["E001":"E003"])

print("\n13. Statistical Summary:\n", df.describe())

print("\n14. DataFrame Information:")
df.info()

avg_salary = df["Salary"].mean()
print(f"\n15. Average Salary: {avg_salary}")

print("\n" + "="*36)

# --- Output Summary Report ---

print("====== EMPLOYEE DATA ANALYSIS ======")
print(f"Total Employees: {len(df)}")
print(f"Columns: {', '.join(df.columns)}")
print(f"DataFrame Shape: {df.shape}")
print(f"Average Age: {df['Age'].mean():.1f} years")
print(f"Average Salary: ₹{avg_salary:,.2f}")
print(f"Highest Salary: ₹{df['Salary'].max():,.2f} ({df.loc[df['Salary'].idxmax(), 'Name']})")
print(f"Lowest Salary: ₹{df['Salary'].min():,.2f} ({df.loc[df['Salary'].idxmin(), 'Name']})")