import pandas as pd

# Create a DataFrame with 4 rows and 3 columns
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'London', 'Paris', 'Tokyo']
}

df = pd.DataFrame(data)

# 1. Display shape tuple
print("df.shape:", df.shape)

# 2. Access rows and columns individually
num_rows, num_cols = df.shape
print(f"Number of Rows   : {num_rows}")
print(f"Number of Columns: {num_cols}")