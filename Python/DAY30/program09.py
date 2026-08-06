import pandas as pd
import numpy as np

# Sample Dataset
data = {
    'EmployeeID': ['EMP01', 'EMP02', 'EMP03', 'EMP04', 'EMP05', 'EMP06'],
    'Department': ['Engineering', 'Sales', 'Engineering', 'HR', 'Sales', 'Engineering'],
    'Salary': [120000, 75000, 140000, 65000, 85000, 110000]
}

df = pd.DataFrame(data)

# 1. Overall Total Employees using size
overall_count = df.size  # Total elements in DataFrame (rows * cols)
total_rows = len(df)    # Total employee rows

# 2. Department-Wise Employee Count using size()
dept_counts = df.groupby('Department').size().reset_index(name='Total_Employees')

print(f"Total Rows: {total_rows}\n")
print("--- Employee Count by Department (using size) ---")
print(dept_counts)