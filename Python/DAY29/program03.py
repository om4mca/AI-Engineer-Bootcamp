import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, np.nan, 30],
    'Salary': [50000, 60000, 70000]
})
has_missing = df.isna().values.any()
print("Has missing values:", has_missing)