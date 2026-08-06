import pandas as pd

# Sample Dataset
data = {
    'EmployeeID': ['EMP01', 'EMP02', 'EMP03', 'EMP04', 'EMP05'],
    'Department': ['Engineering', 'Sales', 'Engineering', 'HR', 'Sales'],
    'Salary': [120000, 75000, 140000, 65000, 85000]
}

df = pd.DataFrame(data)

# 1. Overall Maximum Salary
max_sal = df['Salary'].max()

# 2. Maximum Salary by Department
dept_max = df.groupby('Department', as_index=False).agg(
    Highest_Salary=('Salary', 'max')
)

print(f"Overall Highest Salary: ${max_sal:,.2f}\n")
print("--- Department-Wise Maximum Salary ---")
print(dept_max)