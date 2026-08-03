import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'London', 'Paris', 'Tokyo'],
    'Salary': [70000, 80000, 95000, 62000]
}

df = pd.DataFrame(data)

# 1. Select two columns ('Name' and 'Salary')
subset = df[['Name', 'Salary']]

print("--- Subset DataFrame ---")
print(subset)

print("\nData Type:")
print(type(subset))