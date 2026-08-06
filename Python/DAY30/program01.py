import pandas as pd

# Sample Dataset
data = {
    'EmployeeID': ['EMP01', 'EMP02', 'EMP03', 'EMP04', 'EMP05', 'EMP06'],
    'Department': ['Engineering', 'Sales', 'Engineering', 'Human Resources', 'Sales', 'Engineering'],
    'Salary': [120000, 75000, 140000, 65000, 85000, 110000],
    'Experience': [5, 3, 8, 2, 4, 6],
    'Age': [28, 25, 34, 24, 29, 31]
}

df = pd.DataFrame(data)

# Department-wise aggregation using Named Aggregation
dept_summary = df.groupby('Department', as_index=False).agg(
    Total_Employees=('EmployeeID', 'count'),
    Total_Payroll=('Salary', 'sum'),
    Average_Salary=('Salary', 'mean'),
    Max_Salary=('Salary', 'max'),
    Avg_Experience=('Experience', 'mean')
)

print(dept_summary)