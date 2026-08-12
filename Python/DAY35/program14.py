import pandas as pd
import numpy as np

# Sample Patient Dataset
df = pd.DataFrame({
    'Patient_ID': [101, 102, 103, 104, 105, 106, 107, 108],
    'Age': [12, 28, 45, 52, 61, 78, 35, 115],  # 115 is an outlier
    'Blood_Pressure': [110, 120, 125, 130, 140, 135, 122, 160],
    'Department': ['Pediatrics', 'ER', 'Cardiology', 'Cardiology', 'ER', 'Cardiology', 'ER', 'ER']
})

# Basic statistical summary for numeric columns
numeric_summary = df[['Age', 'Blood_Pressure']].describe()
print("--- Standard Numeric Summary ---")
print(numeric_summary.round(2))