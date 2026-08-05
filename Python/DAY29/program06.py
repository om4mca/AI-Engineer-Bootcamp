import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Score1': [85, np.nan, 90],
    'Score2': [np.nan, 78, 88]
})

print("--- Original DataFrame ---")
print(df)

df_zero = df.fillna(0)
print(df_zero)