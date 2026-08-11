import pandas as pd
import numpy as np

# Sample Dataset with missing values
data = {
    'PatientID': [101, 102, 103, 104, 105, 106],
    'Age': [25, np.nan, 35, 42, np.nan, 50],
    'Income': [50000, 62000, np.nan, np.nan, 75000, 90000],
    'Gender': ['M', 'F', 'F', np.nan, 'M', 'F']
}
df = pd.DataFrame(data)

# Check missing values boolean matrix
print(df.isnull())  # or df.isna()