import pandas as pd

# 1. Define a list of dictionaries (each dictionary is one row)
data = [
    {'Name': 'Alice', 'Age': 25, 'City': 'New York', 'Salary': 70000},
    {'Name': 'Bob', 'Age': 30, 'City': 'London', 'Salary': 80000},
    {'Name': 'Charlie', 'Age': 35, 'City': 'Paris', 'Salary': 95000},
    {'Name': 'David', 'Age': 28, 'City': 'Tokyo', 'Salary': 62000}
]

# 2. Convert to DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)