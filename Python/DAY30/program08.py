import pandas as pd

# Sample Dataset
data = {
    'EmployeeID': ['EMP01', 'EMP02', 'EMP03', 'EMP04', 'EMP05', 'EMP06'],
    'Department': ['Engineering', 'Sales', 'Engineering', 'HR', 'Sales', 'Engineering'],
    'Age': [28, 45, 34, 24, 52, 31],
    'Salary': [120000, 75000, 140000, 65000, 85000, 110000]
}

df = pd.DataFrame(data)

# 1. Overall Average Age
overall_age = df['Age'].mean()

# 2. Department-Wise Average Age
dept_summary = df.groupby('Department', as_index=False).agg(
    Average_Age=('Age', 'mean')
)

print(f"Overall Average Age: {overall_age:.1f} years\n")
print("--- Department Average Age ---")
print(dept_summary)