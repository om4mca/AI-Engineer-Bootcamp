import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Department': ['IT', 'Sales', 'HR'],
    'Salary': [120000, 75000, 140000]
}
df = pd.DataFrame(data)

# Save to CSV (excluding row numbers/index)
df.to_csv("output.csv", index=False)