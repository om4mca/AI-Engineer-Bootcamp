import pandas as pd
import numpy as np
from scipy import stats

# 1. Create Sample Employee Dataset
data = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['Engineering', 'Engineering', 'Engineering', 'Engineering', 'Sales', 'Sales', 'Sales', 'Sales', 'HR', 'HR'],
    'Salary': [85000, 92000, 88000, 240000, 55000, 60000, 58000, 180000, 50000, 52000]
}

df = pd.DataFrame(data)

# 2. Company-Wide Z-Score Calculation
# Highlighting overall company salary outliers
df['Company_ZScore'] = stats.zscore(df['Salary'])

# 3. Department-Specific Z-Score Calculation
# Evaluates relative pay within an employee's specific department group
df['Dept_ZScore'] = df.groupby('Department')['Salary'].transform(lambda x: stats.zscore(x) if len(x) > 1 else 0)

# 4. Outlier Flagging (Threshold: |Z| > 2.0)
# Standard statistical rule: values beyond +/- 2 Z-scores are notable outliers
df['Company_Outlier'] = df['Company_ZScore'].apply(lambda x: 'High' if x > 2.0 else ('Low' if x < -2.0 else 'Normal'))
df['Dept_Outlier'] = df['Dept_ZScore'].apply(lambda x: 'High' if x > 2.0 else ('Low' if x < -2.0 else 'Normal'))

# 5. Display Formatted Results
# Round floats for clean output
df_display = df.copy()
df_display['Salary'] = df_display['Salary'].map('${:,.2f}'.format)
df_display['Company_ZScore'] = df_display['Company_ZScore'].round(2)
df_display['Dept_ZScore'] = df_display['Dept_ZScore'].round(2)

print("--- FULL SALARY Z-SCORE ANALYSIS ---")
print(df_display.to_string(index=False))

print("\n--- IDENTIFIED SALARY OUTLIERS (COMPANY-WIDE) ---")
outliers = df_display[df_display['Company_Outlier'] != 'Normal']
print(outliers[['Employee_ID', 'Name', 'Department', 'Salary', 'Company_ZScore', 'Company_Outlier']].to_string(index=False))