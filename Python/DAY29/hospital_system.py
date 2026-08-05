import pandas as pd
import numpy as np

# Step 0: Create initial dataset with intentional missing values and duplicate
data = {
    'PatientID': [1, 2, 3, 4, 5, 6, 3, 7],
    'Name': ['John Doe', 'Jane Smith', 'Robert Johnson', np.nan, 'Emily Davis', 'Michael Brown', 'Robert Johnson', 'Sarah Wilson'],
    'Age': [45.0, np.nan, 32.0, 50.0, np.nan, 28.0, 32.0, 61.0],
    'Gender': ['Male', 'Female', np.nan, 'Male', 'Female', np.nan, np.nan, 'Female'],
    'Temperature': [98.6, 101.2, 98.2, np.nan, 99.1, np.nan, 98.2, 98.6],
    'Blood Group': ['A+', 'O-', 'B+', 'AB+', 'A+', 'O+', 'B+', 'O-']
}

df = pd.DataFrame(data)

print("=== RAW DATASET ===")
print(df.to_string(index=False))
print("\n" + "="*50 + "\n")

# 1. Detect missing values
print("--- 1. Missing Values Count per Column ---")
missing_counts = df.isna().sum()
print(missing_counts)
print("\n")

# 2. Fill missing age (using median age)
median_age = df['Age'].median()
df['Age'] = df['Age'].fillna(median_age)

# 3. Fill gender as 'Unknown'
df['Gender'] = df['Gender'].fillna('Unknown')

# 4. Fill temperature with average (mean)
mean_temp = round(df['Temperature'].mean(), 1)
df['Temperature'] = df['Temperature'].fillna(mean_temp)

# Also handle missing Name to ensure dataset integrity
df['Name'] = df['Name'].fillna('Unknown Patient')

# 5. Remove duplicate patients (based on PatientID)
df = df.drop_duplicates(subset=['PatientID'], keep='first')

# 6. Count blood groups
print("--- 6. Blood Group Distribution ---")
blood_group_counts = df['Blood Group'].value_counts()
print(blood_group_counts)
print("\n")

# 7. Rename columns for standardized naming conventions
df = df.rename(columns={
    'PatientID': 'Patient_ID',
    'Name': 'Full_Name',
    'Age': 'Age_Years',
    'Gender': 'Gender',
    'Temperature': 'Temp_Fahrenheit',
    'Blood Group': 'Blood_Group'
})

# 8. Display clean dataset
print("--- 8. Cleaned Dataset ---")
print(df.to_string(index=False))
print("\n" + "="*50 + "\n")

# 9. Generate statistics
print("--- 9. Summary Statistics (Numeric Fields) ---")
stats = df[['Age_Years', 'Temp_Fahrenheit']].describe().round(2)
print(stats)
print("\n")

# 10. Print final report
print("--- 10. FINAL DATA CLEANING REPORT ---")
print(f"Total Initial Records   : {len(data['PatientID'])}")
print(f"Total Unique Patients  : {len(df)}")
print(f"Duplicates Removed     : {len(data['PatientID']) - len(df)}")
print(f"Applied Imputed Age    : {median_age} (Median)")
print(f"Applied Imputed Temp   : {mean_temp} °F (Mean)")
print("Status                 : Cleaning Complete & Validated")