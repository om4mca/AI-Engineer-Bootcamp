import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Department': ['HR', 'Engineering', 'Sales'],
    'Salary': [60000, 85000, 70000],
    'Age': [25, 30, 35]
}

df = pd.DataFrame(data)

# Select multiple columns
subset = df[['Name', 'Department', 'Salary']]
print(subset)