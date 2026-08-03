import pandas as pd

# 1. Define a list of lists (each inner list represents a row)
data = [
    ['Alice', 25, 'New York', 70000],
    ['Bob', 30, 'London', 80000],
    ['Charlie', 35, 'Paris', 95000],
    ['David', 28, 'Tokyo', 62000]
]

# 2. Convert to DataFrame and assign column headers
df = pd.DataFrame(data, columns=['Name', 'Age', 'City', 'Salary'])

# Display the DataFrame
print(df)