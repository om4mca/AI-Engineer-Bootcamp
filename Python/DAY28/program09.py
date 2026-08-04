import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Department': ['HR', 'IT', 'Sales', 'IT', 'Finance'],
    'Salary': [60000, 85000, 70000, 45000, 90000]
}

df = pd.DataFrame(data)

# Filter IT employees with Salary > 50000
it_high_salary = df[(df['Department'] == 'IT') & (df['Salary'] > 50000)]
print(it_high_salary)