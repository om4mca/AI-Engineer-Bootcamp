import pandas as pd

# Create DataFrame
data = {
    "PatientID": ["P001", "P002", "P003", "P004", "P005"],
    "Name": ["Amit", "Rahul", "Priya", "Neha", "Rohan"],
    "Age": [25, 40, 32, 65, 50],
    "Gender": ["Male", "Male", "Female", "Female", "Male"],
    "Temperature": [36.5, 38.2, 37.0, 39.1, 37.5]
}

df = pd.DataFrame(data)

# --- Perform Operations ---

# 1. Display complete patient data
print("1. Complete Patient Data:\n", df)

# 2. Display columns
print("\n2. Columns:", df.columns.tolist())

# 3. Display shape
print("\n3. Shape:", df.shape)

# 4. Display patient names
print("\n4. Patient Names:\n", df["Name"])

# 5. Display Name and Age
print("\n5. Name and Age:\n", df[["Name", "Age"]])

# 6. Display first 3 patients
print("\n6. First 3 Patients:\n", df.head(3))

# 7. Display last 2 patients
print("\n7. Last 2 Patients:\n", df.tail(2))

# 8. Display patient information
print("\n8. Patient Information:")
df.info()

# 9. Generate statistical summary
print("\n9. Statistical Summary:\n", df.describe())

# 10. Calculate average patient age
avg_age = df["Age"].mean()
print(f"\n10. Average Patient Age: {avg_age:.1f}")

# 11. Calculate average temperature
avg_temp = df["Temperature"].mean()
print(f"\n11. Average Temperature: {avg_temp:.2f}°C")

# 12. Find minimum age
min_age = df["Age"].min()
print(f"\n12. Minimum Age: {min_age}")

# 13. Find maximum age
max_age = df["Age"].max()
print(f"\n13. Maximum Age: {max_age}")

# 14. Find minimum temperature
min_temp = df["Temperature"].min()
print(f"\n14. Minimum Temperature: {min_temp}°C")

# 15. Find maximum temperature
max_temp = df["Temperature"].max()
print(f"\n15. Maximum Temperature: {max_temp}°C")

print("\n" + "="*40)

# --- Output Summary Report ---

print("====== HOSPITAL PATIENT ANALYSIS ======")
print(f"Total Patients      : {len(df)}")
print(f"Columns             : {', '.join(df.columns)}")
print(f"DataFrame Shape     : {df.shape}")
print(f"Average Patient Age : {avg_age:.1f} years")
print(f"Average Temperature : {avg_temp:.2f}°C")
print(f"Youngest Patient    : {min_age} years ({df.loc[df['Age'].idxmin(), 'Name']})")
print(f"Oldest Patient      : {max_age} years ({df.loc[df['Age'].idxmax(), 'Name']})")
print(f"Lowest Temperature  : {min_temp}°C ({df.loc[df['Temperature'].idxmin(), 'Name']})")
print(f"Highest Temperature : {max_temp}°C ({df.loc[df['Temperature'].idxmax(), 'Name']})")