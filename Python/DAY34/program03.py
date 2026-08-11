import pandas as pd

# Load dataset
df = pd.read_csv('dataset.csv')

# 1. Get a list of all column names
print("Column Names:", df.columns.tolist())

# 2. Check Data Types of each column
print("\nData Types:\n", df.dtypes)

# 3. Comprehensive Summary (Non-null count + Data Types + Memory Usage)
df.info()