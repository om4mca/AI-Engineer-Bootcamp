import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic dataset
n_employees = 60
departments = ['Engineering', 'Sales', 'Marketing', 'Finance', 'Human Resources']
cities = ['New York', 'San Francisco', 'Chicago', 'Austin', 'Seattle']

data = []
for i in range(1, n_employees + 1):
    emp_id = f"EMP{i:03d}"
    dept = np.random.choice(departments, p=[0.3, 0.25, 0.15, 0.15, 0.15])
    
    # Base age & experience logic
    age = np.random.randint(22, 60)
    exp = max(0, age - 22 - np.random.randint(0, 5))
    
    # Salary logic based on dept & experience
    base_sal = {'Engineering': 85000, 'Finance': 75000, 'Sales': 65000, 'Marketing': 60000, 'Human Resources': 55000}[dept]
    salary = base_sal + (exp * 3500) + np.random.randint(-5000, 10000)
    city = np.random.choice(cities)
    
    data.append({
        'EmployeeID': emp_id,
        'Department': dept,
        'Age': age,
        'Salary': salary,
        'Experience': exp,
        'City': city
    })

df = pd.DataFrame(data)

# Department-wise Analytics
dept_analytics = df.groupby('Department').agg(
    Total_Employees=('EmployeeID', 'count'),
    Total_Salary=('Salary', 'sum'),
    Average_Salary=('Salary', 'mean'),
    Highest_Salary=('Salary', 'max'),
    Lowest_Salary=('Salary', 'min'),
    Median_Salary=('Salary', 'median'),
    Average_Experience=('Experience', 'mean'),
    Average_Age=('Age', 'mean')
).reset_index()

print("Department-Wise Breakdown:")
print(dept_analytics.to_string())

print("\nSummary overall:")
print(f"Total Employees: {len(df)}")
print(f"Total Payroll: ${df['Salary'].sum():,.2f}")