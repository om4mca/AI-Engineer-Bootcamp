import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 32, 28, 40, 22],
    'Department': ['HR', 'Engineering', 'Sales', 'Marketing', 'Finance']
}

df = pd.DataFrame(data)

# Filter employees with Age < 30
young_employees = df[df['Age'] < 30]
print(young_employees)