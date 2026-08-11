import pandas as pd

# Sample Dataset with duplicates
data = {
    'PatientID': [101, 102, 103, 103, 104, 105, 101],
    'Name': ['Alice', 'Bob', 'Charlie', 'Charlie', 'David', 'Eva', 'Alice'],
    'Department': ['Cardiology', 'Neurology', 'Orthopedics', 'Orthopedics', 'ICU', 'Pediatrics', 'Cardiology'],
    'Bill': [1200, 850, 3100, 3100, 950, 2100, 1200]
}

df = pd.DataFrame(data)

# 1. Total duplicate rows count
duplicate_count = df.duplicated().sum()
print(f"Total Duplicate Rows: {duplicate_count}")

# 2. View all duplicate rows (including original records for comparison)
duplicates_df = df[df.duplicated(keep=False)].sort_values(by='PatientID')
print("\n--- Duplicate Records Preview ---")
print(duplicates_df)