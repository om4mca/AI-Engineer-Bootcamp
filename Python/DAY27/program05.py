import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris'],
    'Salary': [70000, 80000, 95000]
}

df = pd.DataFrame(data)

# 1. Get the Index object containing all column names
print("df.columns:\n", df.columns)

print("-" * 40)

# 2. Convert column names to a Python list
column_list = df.columns.tolist()
print("As a Python List:", column_list)

# 3. Print each column name line-by-line
print("\nIterating through columns:")
for col in df.columns:
    print(f"- {col}")