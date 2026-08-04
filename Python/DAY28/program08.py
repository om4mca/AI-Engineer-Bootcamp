import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Department': ['HR', 'IT', 'Sales', 'IT', 'Finance'],
    'Salary': [60000, 85000, 70000, 75000, 90000]
}

df = pd.DataFrame(data)

# Filter employees in the IT department
it_employees = df[df['Department'] == 'IT']
print(it_employees)