import pandas as pd

df = pd.DataFrame({
    'Department': ['Engineering', 'Sales', 'Engineering', 'HR', 'Sales'],
    'Salary': [120000, 75000, 140000, 65000, 85000]
})

# Method 1: Using as_index=False (Cleanest)
result_1 = df.groupby('Department', as_index=False).agg(
    Avg_Salary=('Salary', 'mean')
)

# Method 2: Equivalent alternative using reset_index()
result_2 = df.groupby('Department').agg(
    Avg_Salary=('Salary', 'mean')
).reset_index()