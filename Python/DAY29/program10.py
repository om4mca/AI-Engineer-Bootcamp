import pandas as pd
import numpy as np

# Sample time-series dataset (e.g., daily stock prices)
df = pd.DataFrame({
    'Date': ['2026-08-01', '2026-08-02', '2026-08-03', '2026-08-04', '2026-08-05'],
    'Price': [100.0, np.nan, np.nan, 105.5, np.nan],
    'Status': ['Active', np.nan, 'Pending', np.nan, np.nan]
})

print("--- Original DataFrame ---")
print(df)

df_filled = df.ffill()
print(df_filled)