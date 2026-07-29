import numpy as np

# Input Data
ages = np.array([25, 34, 42, 18, 65, 52, 39, 71])

# ======================================================
# NumPy Calculations
# ======================================================

# 1. Total Patients
total_patients = ages.size

# 2. Average Age
average_age = np.mean(ages)

# 3. Youngest Patient
youngest_patient = np.min(ages)

# 4. Oldest Patient
oldest_patient = np.max(ages)

# 5. Patients Above Average Age (Count)
above_average_count = np.sum(ages > average_age)

# 6. Patients Below Average Age (Count)
below_average_count = np.sum(ages < average_age)

# 7. Patients Above 60 (Count)
above_60_count = np.sum(ages > 60)

# 8. Patients Below 30 (Count)
below_30_count = np.sum(ages < 30)


# ======================================================
# Display Summary Report
# ======================================================

print("====== HOSPITAL PATIENT AGE ANALYSIS ======")
print()
print(f"Total Patients: {total_patients}")
print(f"Average Age: {average_age:.2f}")
print(f"Youngest Patient: {youngest_patient}")
print(f"Oldest Patient: {oldest_patient}")
print(f"Patients Above Average Age: {above_average_count}")
print(f"Patients Below Average Age: {below_average_count}")
print(f"Patients Above 60: {above_60_count}")
print(f"Patients Below 30: {below_30_count}")