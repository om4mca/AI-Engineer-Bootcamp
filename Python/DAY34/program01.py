import pandas as pd

# Load the CSV file
df = pd.read_csv('your_dataset.csv')

# View the first 5 rows
print("--- First 5 Rows ---")
print(df.head())

# Inspect structure and shape
print("\nDataset Shape (Rows, Columns):", df.shape)