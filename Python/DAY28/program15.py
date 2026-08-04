import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'Department': ['IT', 'HR', 'IT', 'HR', 'Finance', 'Finance'],
    'Salary': [85000, 60000, 95000, 52000, 90000, 75000]
}

df = pd.DataFrame(data)

# Sort by Department (A-Z) and Salary (High to Low)
sorted_df = df.sort_values(
    by=['Department', 'Salary'], 
    ascending=[True, False]
)

print(sorted_df)