import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 28, 40],
    'Salary': [70000, 80000, 95000, 62000, 110000],
    'Score': [85.5, 90.0, 92.3, 78.0, 88.5]
}

df = pd.DataFrame(data)

# Generate descriptive statistics
print(df.describe())