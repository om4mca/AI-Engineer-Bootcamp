import pandas as pd

# Data dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'Salary': [70000, 80000, 95000, 62000]
}

# Define custom index labels (e.g., Employee IDs)
custom_index = ['E101', 'E102', 'E103', 'E104']

# Create DataFrame with custom index
df = pd.DataFrame(data, index=custom_index)

print(df)