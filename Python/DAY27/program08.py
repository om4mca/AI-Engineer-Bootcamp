import pandas as pd

# Create a DataFrame with 4 rows and 3 columns (Total 12 elements)
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'London', 'Paris', 'Tokyo']
}

df = pd.DataFrame(data)

# 1. Display total size (elements count)
print("df.size:", df.size)

# 2. Compare with shape for context
print("df.shape:", df.shape)
print(f"Calculation: {df.shape[0]} rows * {df.shape[1]} columns = {df.size}")