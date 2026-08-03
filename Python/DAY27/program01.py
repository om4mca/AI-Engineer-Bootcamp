import pandas as pd

# 1. Define a dictionary where keys are column names and values are lists of data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'London', 'Paris', 'Tokyo'],
    'Salary': [70000, 80000, 95000, 62000]
}

# 2. Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)