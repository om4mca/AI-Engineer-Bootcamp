import pandas as pd
import numpy as np

# Sample Hospital Dataset
data = {
    'PatientID': ['P101', 'P102', 'P103', 'P104', 'P105', 'P106'],
    'Department': ['Cardiology', 'Neurology', 'Cardiology', 'Orthopedics', 'Cardiology', 'ICU'],
    'Status': ['Discharged', 'Discharged', 'Admitted', 'Discharged', 'Admitted', 'Discharged'],
    'HospitalBranch': ['Main', 'Main', 'Main', 'Main', 'Main', 'Main'] # Constant feature
}

df = pd.DataFrame(data)

# -------------------------------------------------------------
# 1. unique() -> View distinct values
# -------------------------------------------------------------
print("Unique Departments:", df['Department'].unique())
# Output: ['Cardiology' 'Neurology' 'Orthopedics' 'ICU']

# -------------------------------------------------------------
# 2. nunique() -> Count distinct values
# -------------------------------------------------------------
print("Number of Unique Departments:", df['Department'].nunique())
# Output: 4

# Check cardinality across ALL columns
print("\nUnique count per column:\n", df.nunique())

# -------------------------------------------------------------
# 3. value_counts() -> Frequency Distribution
# -------------------------------------------------------------
print("\nDepartment Counts:\n", df['Department'].value_counts())

# Get percentage share / relative frequencies
print("\nDepartment Percentage Share:\n", df['Department'].value_counts(normalize=True) * 100)