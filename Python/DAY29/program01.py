import pandas as pd
import numpy as np

# Sample DataFrame with missing values (NaN / None)
df = pd.DataFrame({
    'Patient_ID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', None, 'Diana', 'Evan'],
    'Age': [29, np.nan, 35, 42, np.nan],
    'Salary': [70000, 80000, 65000, np.nan, 90000]
})

print(df)