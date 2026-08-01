import pandas as pd

# Create the Series
ages = pd.Series(
    [12, 18, 25, 32, 45, 52, 60, 65, 70, 80],
    index=[
        "P001",
        "P002",
        "P003",
        "P004",
        "P005",
        "P006",
        "P007",
        "P008",
        "P009",
        "P010"
    ]
)

# 1. Total Patients
total_patients = len(ages)

# 2. Average Age
avg_age = ages.mean()

# 3. Median Age
median_age = ages.median()

# 4. Minimum Age
min_age = ages.min()

# 5. Maximum Age
max_age = ages.max()

# 6. Standard Deviation
std_age = ages.std()

# 7. Patients above age 50
above_50 = ages[ages > 50]

# 8. Patients below age 18
below_18 = ages[ages < 18]

# 9. Sort patient ages
sorted_ages = ages.sort_values()

# 10. Display patient IDs and ages
# (Included in the printable summary below)

# Format listings for the report
above_50_str = "\n".join([f"- {pid}: {age} years" for pid, age in above_50.items()])
below_18_str = "\n".join([f"- {pid}: {age} years" for pid, age in below_18.items()])

# Output Report
report = f"""====== HOSPITAL PATIENT AGE ANALYSIS ======

Total Patients: {total_patients}

Average Age: {avg_age:.1f}

Median Age: {median_age:.1f}

Youngest Patient: {min_age} years

Oldest Patient: {max_age} years

Standard Deviation: {std_age:.2f}

Patients Above 50:
{above_50_str}

Patients Below 18:
{below_18_str}
"""

print(report)