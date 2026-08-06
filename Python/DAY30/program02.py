import pandas as pd
import numpy as np

# Sample Employee Dataset (including a missing value to show count vs. size)
data = {
    'EmployeeID': ['EMP01', 'EMP02', 'EMP03', 'EMP04', 'EMP05', np.nan],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'Department': ['Engineering', 'Sales', 'Engineering', 'Sales', 'Engineering', 'Sales']
}

df = pd.DataFrame(data)

# 1. Total Employee Count (Overall)
total_rows = len(df)                          # Output: 6 (Total rows)
total_valid_ids = df['EmployeeID'].count()    # Output: 5 (Excludes missing ID)

# 2. Department-Wise Employee Count (Named Aggregation)
dept_counts = df.groupby('Department', as_index=False).agg(
    Total_Rows=('Name', 'size'),              # Includes all records
    Valid_IDs=('EmployeeID', 'count')          # Ignores NaN entries
)

print("--- Overall Counts ---")
print(f"Total Rows: {total_rows}")
print(f"Total Valid IDs: {total_valid_ids}\n")

print("--- Department-Wise Breakdown ---")
print(dept_counts)