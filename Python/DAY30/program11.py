import pandas as pd

# Sample Dataset with multiple numeric and categorical columns
data = {
    'Department': ['Engineering', 'Sales', 'Engineering', 'HR', 'Sales', 'Engineering'],
    'City': ['New York', 'New York', 'Chicago', 'Chicago', 'New York', 'Chicago'],
    'Salary': [120000, 75000, 140000, 65000, 85000, 110000],
    'Experience': [5, 3, 8, 2, 4, 6],
    'Age': [28, 45, 34, 24, 52, 31]
}

df = pd.DataFrame(data)

# Group by (Department, City) and aggregate (Salary, Experience)
report = df.groupby(['Department', 'City'], as_index=False).agg(
    Employee_Count=('Salary', 'count'),
    Avg_Salary=('Salary', 'mean'),
    Avg_Experience=('Experience', 'mean')
)

print(report)