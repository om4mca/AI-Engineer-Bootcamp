import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', None, 'Diana', 'Evan'],
    'Age': [25, np.nan, 30, 42, 35],
    'Salary': [50000, 60000, 65000, np.nan, 80000]
})

print("--- Original DataFrame ---")
print(df)

clean_df = df.dropna()
print(clean_df)