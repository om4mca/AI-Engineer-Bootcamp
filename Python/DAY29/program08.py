import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Evan'],
    'Age': [22.0, np.nan, 28.0, 60.0, np.nan],
    'Salary': [45000, 50000, np.nan, 250000, 55000] # 250,000 is an outlier!
})

print("--- Original DataFrame ---")
print(df)

# Calculate median salary: middle value of [45k, 50k, 55k, 250k] = 52,500
median_salary = df['Salary'].median()

# Fill missing values in 'Salary' column
df['Salary'] = df['Salary'].fillna(median_salary)

print(df)