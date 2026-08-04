import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Anna', 'Bob', 'Charlie', 'Daniel', None],
    'Department': ['HR', 'IT', 'Sales', 'Finance', 'IT', 'Marketing']
}

df = pd.DataFrame(data)

# Find all names containing 'an' (case-insensitive, ignoring NaN values)
matching_names = df[df['Name'].str.contains('an', case=False, na=False)]
print(matching_names)