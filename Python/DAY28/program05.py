import pandas as pd

# DataFrame with custom index labels
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Department': ['HR', 'Engineering', 'Sales', 'Finance'],
    'Salary': [60000, 85000, 70000, 90000]
}

df = pd.DataFrame(data, index=['emp1', 'emp2', 'emp3', 'emp4'])

# Select rows using string labels
print(df.loc[['emp1', 'emp3']])