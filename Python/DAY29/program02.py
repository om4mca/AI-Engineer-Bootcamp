import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Name': ['Alice', None, 'Charlie', 'Diana', 'Evan'],
    'Age': [28, np.nan, 35, 42, np.nan],
    'Salary': [70000, 80000, np.nan, 85000, 90000]
})

print(df.isna().sum())