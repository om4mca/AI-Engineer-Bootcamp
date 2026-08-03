import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'Salary': [70000, 80000, 95000, 62000]
}

df = pd.DataFrame(data)

# 1. Standard approach using square brackets (Returns a Series)
ages = df['Age']

print("--- Extracted 'Age' Column ---")
print(ages)

print("\nData Type:")
print(type(ages))