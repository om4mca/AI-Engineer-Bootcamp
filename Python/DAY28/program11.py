import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 25, 28, 30, 35],
    'Department': ['HR', 'IT', 'Sales', 'IT', 'Finance']
}

df = pd.DataFrame(data)

# Filter employees with Age between 25 and 30 (inclusive)
age_filtered = df[df['Age'].between(25, 30)]
print(age_filtered)