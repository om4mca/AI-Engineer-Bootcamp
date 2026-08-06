import pandas as pd

# Sample Dataset
data = {
    'EmployeeID': ['EMP01', 'EMP02', 'EMP03', 'EMP04', 'EMP05'],
    'Department': ['Engineering', 'Sales', 'Engineering', 'HR', 'Sales'],
    'Salary': [120000, 75000, 140000, 65000, 85000]
}

df = pd.DataFrame(data)

# 1. Calculate overall average salary
overall_avg = df['Salary'].mean()

# 2. Calculate average salary per department
dept_summary = df.groupby('Department', as_index=False).agg(
    Average_Salary=('Salary', 'mean')
)

print(f"Overall Average Salary: ${overall_avg:,.2f}\n")
print("--- Department Average Salary ---")
print(dept_summary)