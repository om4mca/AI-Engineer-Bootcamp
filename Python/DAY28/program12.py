import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'Department': ['HR', 'IT', 'Sales', 'Finance', 'Marketing', 'IT'],
    'Salary': [60000, 85000, 70000, 90000, 65000, 78000]
}

df = pd.DataFrame(data)

# Specify the departments you want to include
target_departments = ['HR', 'IT', 'Finance']

# Filter using isin()
filtered_df = df[df['Department'].isin(target_departments)]
print(filtered_df)