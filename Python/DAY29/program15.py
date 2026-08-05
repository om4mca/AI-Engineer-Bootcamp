import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Employee_ID': [101, 102, 103, 104, 105, 106],
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Evan', 'Fiona'],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'HR', np.nan]
})

print("--- Original DataFrame ---")
print(df)

# Returns total count of distinct non-null departments
unique_count = df['Department'].nunique()
print(f"Total Unique Departments: {unique_count}")
# Output: Total Unique Departments: 3  (IT, HR, Finance)