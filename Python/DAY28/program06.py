import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Department': ['HR', 'Engineering', 'Sales', 'Marketing', 'Finance'],
    'Salary': [45000, 85000, 70000, 48000, 90000]
}

df = pd.DataFrame(data)

# Filter employees with salary > 50000
high_salary = df[df['Salary'] > 50000]
print(high_salary)