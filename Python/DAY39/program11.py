import pandas as pd
import numpy as np
from scipy import stats

# 1. Create Sample Hospital Patient Dataset
data = {
    'Patient_ID': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010],
    'Name': ['Liam', 'Sophia', 'Jackson', 'Olivia', 'Aiden', 'Emma', 'Lucas', 'Ava', 'Ethan', 'Mia'],
    'Ward': ['Cardiology', 'Cardiology', 'Cardiology', 'Cardiology', 'Pediatrics', 'Pediatrics', 'Pediatrics', 'Oncology', 'Oncology', 'Oncology'],
    'Age': [68, 72, 70, 14, 5, 8, 6, 62, 98, 59]
}

df = pd.DataFrame(data)

# 2. Hospital-Wide Z-Score Calculation
# Measures patient age relative to the entire hospital population
df['Hospital_ZScore'] = stats.zscore(df['Age'])

# 3. Ward-Specific Z-Score Calculation
# Measures patient age relative to peers within the same department/ward
# Safe guard handles single-patient or zero-variance wards to avoid division by zero
df['Ward_ZScore'] = df.groupby('Ward')['Age'].transform(
    lambda x: stats.zscore(x) if len(x) > 1 and x.std() != 0 else 0
)

# 4. Outlier Flagging Threshold (|Z| > 2.0)
# Flags patients whose age deviates significantly from the mean
df['Hospital_Outlier'] = df['Hospital_ZScore'].apply(
    lambda x: 'Elderly Outlier' if x > 2.0 else ('Pediatric/Young Outlier' if x < -2.0 else 'Normal')
)

df['Ward_Outlier'] = df['Ward_ZScore'].apply(
    lambda x: 'High Age Outlier' if x > 2.0 else ('Low Age Outlier' if x < -2.0 else 'Normal')
)

# 5. Formatted Display
df_display = df.copy()
df_display['Hospital_ZScore'] = df_display['Hospital_ZScore'].round(2)
df_display['Ward_ZScore'] = df_display['Ward_ZScore'].round(2)

print("--- FULL PATIENT AGE Z-SCORE ANALYSIS ---")
print(df_display.to_string(index=False))

print("\n--- IDENTIFIED WARD-LEVEL AGE ANOMALIES ---")
ward_anomalies = df_display[df_display['Ward_Outlier'] != 'Normal']
print(ward_anomalies[['Patient_ID', 'Name', 'Ward', 'Age', 'Ward_ZScore', 'Ward_Outlier']].to_string(index=False))