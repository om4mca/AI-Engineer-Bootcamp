import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Date': ['2026-08-01', '2026-08-02', '2026-08-03', '2026-08-04', '2026-08-05'],
    'Price': [np.nan, np.nan, 102.5, np.nan, 108.0],
    'Status': [np.nan, 'Pending', np.nan, np.nan, 'Completed']
})

print("--- Original DataFrame ---")
print(df)

df_filled = df.bfill()
print(df_filled)