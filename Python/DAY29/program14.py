import pandas as pd

df = pd.DataFrame({
    'Emp_ID': [101, 102, 103],
    'fname': ['Alice', 'Bob', 'Charlie'],
    'dept_code': ['IT', 'HR', 'FIN'],
    'sal': [70000, 80000, 65000]
})

print("--- Original DataFrame ---")
print(df)

df_renamed = df.rename(columns={
    'fname': 'First_Name',
    'dept_code': 'Department',
    'sal': 'Salary_USD'
})

print(df_renamed)