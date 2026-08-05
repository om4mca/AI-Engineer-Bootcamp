import pandas as pd

df = pd.DataFrame({
    'Emp_ID': [101, 102, 103, 102, 104, 101],
    'Name': ['Alice', 'Bob', 'Charlie', 'Bob', 'Diana', 'Alice'],
    'Department': ['IT', 'HR', 'Finance', 'HR', 'IT', 'IT']
})

print("--- Original DataFrame ---")
print(df)

clean_df = df.drop_duplicates()
print(clean_df)