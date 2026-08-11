import pandas as pd

# Load dataset
df = pd.read_csv('dataset.csv')

# 1. View all column dtypes
print(df.dtypes)

# 2. View non-null counts, dtypes, and memory usage
df.info()