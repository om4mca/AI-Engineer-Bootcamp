import pandas as pd

# Sample Dataset
data = {
    'EmployeeID': ['EMP01', 'EMP02', 'EMP03', 'EMP04', 'EMP05'],
    'Department': ['Engineering', 'Sales', 'Engineering', 'HR', 'Sales'],
    'Salary': [120000, 75000, 140000, 65000, 85000]
}

df = pd.DataFrame(data)

# 1. Overall Minimum Salary
min_sal = df['Salary'].min()

# 2. Minimum Salary by Department
dept_min = df.groupby('Department', as_index=False).agg(
    Lowest_Salary=('Salary', 'min')
)

print(f"Overall Lowest Salary: ${min_sal:,.2f}\n")
print("--- Department-Wise Minimum Salary ---")
print(dept_min)