import pandas as pd

# Sample employee dataset with Age values
data = {
    'EmployeeID': ['EMP01', 'EMP02', 'EMP03', 'EMP04', 'EMP05', 'EMP06', 'EMP07', 'EMP08'],
    'Department': ['Engineering', 'Engineering', 'Engineering', 'Sales', 'Sales', 'Sales', 'HR', 'HR'],
    'Age': [28, 28, 34, 45, 45, 29, 24, 24],
    'Salary': [120000, 115000, 140000, 75000, 85000, 70000, 65000, 62000],
    'Experience': [5, 4, 8, 12, 14, 3, 2, 1]
}

df = pd.DataFrame(data)

# Method 1: Exact Age GroupBy using Named Aggregation
dept_exact_age = df.groupby(['Department', 'Age'], as_index=False).agg(
    Total_Employees=('EmployeeID', 'count'),
    Average_Salary=('Salary', 'mean'),
    Average_Experience=('Experience', 'mean')
)

# Method 2: Age Bracket GroupBy (Binned Age Groups)
df['Age_Group'] = pd.cut(df['Age'], bins=[20, 30, 40, 50, 65], labels=['20-30', '31-40', '41-50', '51+'])
dept_age_bracket = df.groupby(['Department', 'Age_Group'], as_index=False, observed=False).agg(
    Total_Employees=('EmployeeID', 'count'),
    Average_Salary=('Salary', 'mean')
)

print("--- Exact Age GroupBy ---")
print(dept_exact_age.to_string(index=False))

print("\n--- Age Group / Bracket GroupBy ---")
print(dept_age_bracket[dept_age_bracket['Total_Employees'] > 0].to_string(index=False))