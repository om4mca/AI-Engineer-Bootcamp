import pandas as pd
import numpy as np

# Sample Dataset
df = pd.DataFrame({
    'PatientID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', np.nan],
    'Age': [25, 34, np.nan, 42, 50],
    'Bill': [1200.5, 850.0, 3100.25, np.nan, 950.0],
    'IsInsured': [True, False, True, True, False]
})

df.info()