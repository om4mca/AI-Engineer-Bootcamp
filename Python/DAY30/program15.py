import pandas as pd

# Sample Dataset
data = {
    'EmployeeID': ['EMP01', 'EMP02', 'EMP03', 'EMP04', 'EMP05', 'EMP06'],
    'Department': ['Engineering', 'Sales', 'Engineering', 'HR', 'Sales', 'Engineering'],
    'Salary': [120000, 75000, 140000, 65000, 85000, 110000],
    'Experience': [5, 3, 8, 2, 4, 6]
}

df = pd.DataFrame(data)

# Named Aggregation Report
report = df.groupby('Department', as_index=False).agg(
    Headcount=('EmployeeID', 'count'),
    Total_Payroll=('Salary', 'sum'),
    Average_Salary=('Salary', 'mean'),
    Highest_Salary=('Salary', 'max'),
    Average_Experience=('Experience', 'mean')
)

print(report)