import pandas as pd

# Sample DataFrame with custom row index
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'London', 'Paris', 'Tokyo'],
    'Salary': [70000, 80000, 95000, 62000]
}

df = pd.DataFrame(data, index=['R1', 'R2', 'R3', 'R4'])
print("--- Original DataFrame ---")
print(df)