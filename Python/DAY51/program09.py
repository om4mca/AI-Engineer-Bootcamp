import pandas as pd
import numpy as np

# 1. Shape of a Pandas DataFrame
df = pd.DataFrame({
    'Age': [25, 45, 35, 50, 28],
    'BMI': [22.4, 28.1, 24.5, 30.2, 26.1],
    'Income': [50000, 85000, 62000, 95000, 58000],
    'Purchased': [0, 1, 0, 1, 0]
})

# Get shape tuple (rows, columns)
shape = df.shape
rows, cols = df.shape

print(f"Dataset Shape : {shape}")   # Output: (5, 4)
print(f"Total Rows    : {rows}")    # Output: 5 (Samples)
print(f"Total Columns : {cols}")    # Output: 4 (Features + Target)

# 2. Shape of Feature Matrix (X) and Target Vector (y)
X = df.drop(columns=['Purchased'])
y = df['Purchased']

print(f"Features (X) Shape : {X.shape}")  # Output: (5, 3)
print(f"Target (y) Shape   : {y.shape}")  # Output: (5,)

# 3. Shape of a NumPy Array
X_array = X.to_numpy()
print(f"NumPy Array Shape  : {X_array.shape}")  # Output: (5, 3)