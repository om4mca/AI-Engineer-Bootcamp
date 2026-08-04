import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Department': ['HR', 'Engineering', 'Sales', 'Marketing', 'Finance'],
    'Salary': [60000, 85000, 70000, 65000, 90000]
}

df = pd.DataFrame(data)

# Select rows at index positions 0, 2, and 4
selected_rows = df.iloc[[0, 2, 4]]
print(selected_rows)