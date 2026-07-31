import numpy as np

# Input Datasets
ages = np.array([12, 18, 25, 32, 45, 52, 60, 65, 70, 80])
temperatures = np.array([36.5, 36.8, 37.0, 37.2, 37.5, 38.0, 38.2, 38.5, 39.0, 39.2])

# Age Calculations
total_patients = len(ages)
avg_age = np.mean(ages)
median_age = np.median(ages)
min_age = np.min(ages)
max_age = np.max(ages)
std_age = np.std(ages)
p25_age = np.percentile(ages, 25)
p75_age = np.percentile(ages, 75)

# Temperature Calculations
avg_temp = np.mean(temperatures)
median_temp = np.median(temperatures)
min_temp = np.min(temperatures)
max_temp = np.max(temperatures)
std_temp = np.std(temperatures)

# Boolean Filters
age_gt_50 = ages[ages > 50]
age_lt_18 = ages[ages < 18]
temp_gt_38 = temperatures[temperatures > 38.0]
temp_lte_375 = temperatures[temperatures <= 37.5]

# Report Formatting
print("============================================================")
print("           HOSPITAL PATIENT & VITAL STATS REPORT            ")
print("============================================================\n")

print("1. AGE STATISTICAL ANALYSIS")
print("------------------------------------------------------------")
print(f"* Total Patients          : {total_patients}")
print(f"* Average Age             : {avg_age:.1f} years")
print(f"* Median Age              : {median_age:.1f} years")
print(f"* Youngest Patient        : {min_age} years old")
print(f"* Oldest Patient          : {max_age} years old")
print(f"* Standard Deviation      : {std_age:.2f} years")
print(f"* 25th Percentile         : {p25_age:.2f} years")
print(f"* 75th Percentile         : {p75_age:.2f} years\n")

print("------------------------------------------------------------")
print("2. TEMPERATURE STATISTICAL ANALYSIS (°C)")
print("------------------------------------------------------------")
print(f"* Average Temperature     : {avg_temp:.2f}°C")
print(f"* Median Temperature      : {median_temp:.2f}°C")
print(f"* Minimum Temperature     : {min_temp:.2f}°C")
print(f"* Maximum Temperature     : {max_temp:.2f}°C")
print(f"* Standard Deviation      : {std_temp:.2f}°C\n")

print("------------------------------------------------------------")
print("3. ADVANCED BOOLEAN FILTERING")
print("------------------------------------------------------------")
print(f"* Patients Age > 50       : {age_gt_50.tolist()} (Count: {len(age_gt_50)})")
print(f"* Patients Age < 18       : {age_lt_18.tolist()} (Count: {len(age_lt_18)})")
print(f"* Temperature > 38.0°C    : {temp_gt_38.tolist()}°C (Count: {len(temp_gt_38)})")
print(f"* Temperature <= 37.5°C   : {temp_lte_375.tolist()}°C (Count: {len(temp_lte_375)})\n")

print("============================================================")