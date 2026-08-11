import pandas as pd
import numpy as np

# Sample Dataset
data = {
    'Age': [25, 30, 35, 40, 45, 50, 85], # 85 is an outlier
    'Salary': [45000, 52000, 58000, 64000, 71000, 80000, 120000],
    'Department': ['IT', 'HR', 'IT', 'Sales', 'Sales', 'IT', 'HR']
}
df = pd.DataFrame(data)

# Numerical Statistical Summary
print("--- Numerical Summary ---")
print(df.describe().round(2))