import pandas as pd

# Sample Dataset
data = {
    'EmployeeID': ['EMP01', 'EMP02', 'EMP03', 'EMP04', 'EMP05', 'EMP06'],
    'Department': ['Engineering', 'Sales', 'Engineering', 'HR', 'Sales', 'Engineering'],
    'Salary': [120000, 75000, 140000, 65000, 85000, 300000]  # EMP06 is an outlier
}

df = pd.DataFrame(data)

# 1. Overall Median vs Mean
overall_median = df['Salary'].median()
overall_mean = df['Salary'].mean()

# 2. Department-Wise Median Salary
dept_median = df.groupby('Department', as_index=False).agg(
    Median_Salary=('Salary', 'median'),
    Average_Salary=('Salary', 'mean')
)

print(f"Overall Median Salary: ${overall_median:,.2f}")
print(f"Overall Mean Salary:   ${overall_mean:,.2f}  <-- Skewed by $300k outlier!\n")
print("--- Department Salary Summary ---")
print(dept_median)