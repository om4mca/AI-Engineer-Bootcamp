import pandas as pd
import numpy as np

# Step 0: Create the initial dataset with intentional errors
data = {
    'EmployeeID': [101, 102, 103, 104, 105, 106, 102, 107],
    'Name': ['Alice Smith', None, 'Charlie Brown', 'Diana Prince', 'Evan Wright', 'Fiona Gallagher', None, 'George Clark'],
    'Department': ['IT', 'HR', None, 'Finance', 'IT', 'Marketing', 'HR', 'Finance'],
    'Age': [28, 34, np.nan, 45, 29, np.nan, 34, 52],
    'Salary': [70000, np.nan, 65000, 85000, np.nan, 55000, np.nan, 90000]
}

df = pd.DataFrame(data)

print("--- Original Raw Dataset ---")
print(df)
print("\n" + "="*50 + "\n")

# 1. Detect missing values
print("--- 1. Detect Missing Values (Boolean Mask) ---")
print(df.isna())
print("\n")

# 2. Count missing values per column
print("--- 2. Count Missing Values ---")
missing_counts = df.isna().sum()
print(missing_counts)
print("\n")

# 3. Fill missing Age with mean age
mean_age = round(df['Age'].mean(), 1)
df['Age'] = df['Age'].fillna(mean_age)

# 4. Fill missing Salary with median salary
median_salary = df['Salary'].median()
df['Salary'] = df['Salary'].fillna(median_salary)

# 5. Fill missing Department with 'Unknown'
df['Department'] = df['Department'].fillna('Unknown')

# Note: Filling missing Name to ensure a completely clean dataset
df['Name'] = df['Name'].fillna('Unknown Name')

# 6. Remove duplicate employees (based on EmployeeID)
df = df.drop_duplicates(subset=['EmployeeID'], keep='first')

# 7. Rename columns (for cleaner presentation)
df = df.rename(columns={
    'EmployeeID': 'Emp_ID',
    'Name': 'Full_Name',
    'Department': 'Dept',
    'Age': 'Age_Years',
    'Salary': 'Salary_USD'
})

# 8. Count employees per department
dept_counts = df['Dept'].value_counts()
print("--- 8. Department Distribution ---")
print(dept_counts)
print("\n")

# 9. Display clean dataset
print("--- 9. Cleaned Dataset ---")
print(df.to_string(index=False))
print("\n" + "="*50 + "\n")

# 10. Generate summary report
print("--- 10. Data Cleaning Summary Report ---")
print(f"* Initial Record Count : {len(data['EmployeeID'])}")
print(f"* Clean Record Count   : {len(df)}")
print(f"* Duplicates Removed   : {len(data['EmployeeID']) - len(df)}")
print(f"* Mean Age Applied     : {mean_age}")
print(f"* Median Salary Applied : ${median_salary:,.2f}")
print("\nStatistical Overview of Numeric Fields:")
print(df[['Age_Years', 'Salary_USD']].describe().round(2))