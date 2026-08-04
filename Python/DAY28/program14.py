import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Department': ['HR', 'IT', 'Sales', 'IT', 'Finance'],
    'Salary': [60000, 85000, 70000, 45000, 90000]
}

df = pd.DataFrame(data)

# Sort by Salary descending
sorted_df = df.sort_values(by='Salary', ascending=False)
print(sorted_df)