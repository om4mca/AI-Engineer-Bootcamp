import pandas as pd

# Sample Dataset
data = {
    'EmployeeID': ['EMP01', 'EMP02', 'EMP03', 'EMP04', 'EMP05'],
    'Department': ['Engineering', 'Sales', 'Engineering', 'HR', 'Sales'],
    'Salary': [120000, 75000, 140000, 65000, 85000]
}

df = pd.DataFrame(data)

# 1. Total Overall Salary
total_payroll = df['Salary'].sum()

# 2. Department-Wise Total Salary
dept_summary = df.groupby('Department', as_index=False).agg(
    Total_Salary=('Salary', 'sum')
)

print(f"Overall Payroll: ${total_payroll:,.2f}\n")
print("--- Department Salary Sum ---")
print(dept_summary)