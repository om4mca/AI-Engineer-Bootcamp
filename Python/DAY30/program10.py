import pandas as pd

data = {
    'EmployeeID': ['EMP01', 'EMP02', 'EMP03', 'EMP04', 'EMP05', 'EMP06'],
    'Department': ['Engineering', 'Sales', 'Engineering', 'HR', 'Sales', 'Engineering'],
    'Salary': [120000, 75000, 140000, 65000, 85000, 110000],
    'Experience': [5, 3, 8, 2, 4, 6],
    'Age': [28, 45, 34, 24, 52, 31]
}

df = pd.DataFrame(data)

# Method 1: Multiple functions on a single column
m1 = df.groupby('Department')['Salary'].agg(['sum', 'mean', 'median', 'min', 'max'])

# Method 2: Different functions across multiple columns
m2 = df.groupby('Department').agg({
    'EmployeeID': 'count',
    'Salary': ['mean', 'max'],
    'Experience': 'mean'
})

# Method 3: Named Aggregation (Best Practice)
m3 = df.groupby('Department', as_index=False).agg(
    Total_Employees=('EmployeeID', 'count'),
    Total_Payroll=('Salary', 'sum'),
    Average_Salary=('Salary', 'mean'),
    Highest_Salary=('Salary', 'max'),
    Average_Experience=('Experience', 'mean')
)

print("--- Named Aggregation Result ---")
print(m3.to_string(index=False))