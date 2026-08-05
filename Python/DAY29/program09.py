import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Patient_ID': [101, 102, 103, 104],
    'Name': ['Alice', None, 'Charlie', 'Diana'],
    'Department': ['IT', 'HR', np.nan, 'Finance'],
    'Gender': ['Female', 'Male', np.nan, None]
})

print("--- Original DataFrame ---")
print(df)

# Fill missing values in 'Department' column
df['Department'] = df['Department'].fillna('Unknown')

print(df[['Patient_ID', 'Department']])