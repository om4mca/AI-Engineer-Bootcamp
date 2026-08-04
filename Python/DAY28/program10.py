import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Department': ['HR', 'IT', 'Sales', 'IT', 'Finance'],
    'Salary': [60000, 85000, 70000, 75000, 90000]
}

df = pd.DataFrame(data)

# Filter employees in IT or HR
it_or_hr = df[df['Department'].isin(['IT', 'HR'])]
print(it_or_hr)