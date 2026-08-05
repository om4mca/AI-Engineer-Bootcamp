import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Patient_ID': [101, 102, 103, 104],
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [28, np.nan, 35, 42],        # Has 1 missing value
    'Notes': [np.nan, np.nan, np.nan, np.nan]  # Completely missing
})

print("--- Original DataFrame ---")
print(df)

clean_df = df.dropna(axis=1)
print(clean_df)