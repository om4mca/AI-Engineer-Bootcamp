import pandas as pd

# Load or create a dataset
df = pd.read_csv('dataset.csv')

# Check shape
shape_tuple = df.shape
print(f"Dataset Shape: {shape_tuple}")

# Unpack rows and columns
rows, cols = df.shape
print(f"Total Rows (Records)    : {rows}")
print(f"Total Columns (Features): {cols}")