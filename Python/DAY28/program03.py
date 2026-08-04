import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Department': ['HR', 'Engineering', 'Sales', 'Marketing', 'Finance'],
    'Salary': [60000, 85000, 70000, 65000, 90000]
}

df = pd.DataFrame(data)

# Select first 3 rows
first_three = df.iloc[:3]
print(first_three)