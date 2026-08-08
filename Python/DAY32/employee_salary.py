import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Sample Dataset
data = {
    'EmployeeID': [f'EMP{i:03d}' for i in range(1, 16)],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ian', 'Jack', 'Karen', 'Leo', 'Mia', 'Nathan', 'Olivia'],
    'Department': ['IT', 'Sales', 'IT', 'HR', 'Sales', 'IT', 'HR', 'Finance', 'Finance', 'Sales', 'IT', 'HR', 'Finance', 'IT', 'Sales'],
    'Age': [28, 45, 34, 24, 52, 31, 29, 38, 41, 33, 26, 47, 30, 36, 50],
    'Salary': [120000, 75000, 140000, 65000, 85000, 110000, 68000, 95000, 105000, 80000, 115000, 72000, 92000, 135000, 88000],
    'Experience': [5, 12, 8, 2, 14, 6, 3, 9, 11, 7, 3, 15, 4, 10, 16]
}

df = pd.DataFrame(data)

# Chart 1: Department-wise Employee Count
plt.figure(figsize=(8, 5))
dept_counts = df['Department'].value_counts()
colors = ['#1f77b4', '#aec7e8', '#ff7f0e', '#ffbb78']
bars = plt.bar(dept_counts.index, dept_counts.values, color='#2b5c8f', edgecolor='black', width=0.55)
plt.title('Department-wise Employee Count', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Department', fontweight='bold')
plt.ylabel('Number of Employees', fontweight='bold')
plt.grid(axis='y', linestyle='--', alpha=0.7)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 0.1, int(yval), ha='center', va='bottom', fontweight='bold')

plt.ylim(0, max(dept_counts.values) + 1)
plt.tight_layout()
plt.savefig('employee_count.png', dpi=300)
plt.close()

# Chart 2: Department-wise Average Salary
plt.figure(figsize=(8, 5))
avg_salary = df.groupby('Department')['Salary'].mean()
bars = plt.bar(avg_salary.index, avg_salary.values, color='#2ca02c', edgecolor='black', width=0.55)
plt.title('Department-wise Average Salary', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Department', fontweight='bold')
plt.ylabel('Average Salary ($)', fontweight='bold')
plt.grid(axis='y', linestyle='--', alpha=0.7)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 2000, f'${yval:,.0f}', ha='center', va='bottom', fontweight='bold')

plt.ylim(0, max(avg_salary.values) * 1.15)
plt.tight_layout()
plt.savefig('average_salary.png', dpi=300)
plt.close()

# Chart 3: Age Distribution
plt.figure(figsize=(8, 5))
plt.hist(df['Age'], bins=6, color='#9467bd', edgecolor='black', alpha=0.85)
plt.title('Age Distribution of Employees', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Age', fontweight='bold')
plt.ylabel('Frequency', fontweight='bold')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('age_distribution.png', dpi=300)
plt.close()

# Chart 4: Age vs Salary
plt.figure(figsize=(8, 5))
departments = df['Department'].unique()
dept_colors = {'IT': '#1f77b4', 'Sales': '#ff7f0e', 'HR': '#2ca02c', 'Finance': '#d62728'}

for dept in departments:
    sub_df = df[df['Department'] == dept]
    plt.scatter(sub_df['Age'], sub_df['Salary'], label=dept, color=dept_colors.get(dept, 'blue'), s=100, edgecolors='black', alpha=0.8)

plt.title('Age vs Salary by Department', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Age (Years)', fontweight='bold')
plt.ylabel('Salary ($)', fontweight='bold')
plt.legend(title='Department')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('age_salary.png', dpi=300)
plt.close()

# Chart 5: Experience vs Salary
plt.figure(figsize=(8, 5))
plt.scatter(df['Experience'], df['Salary'], color='#008080', s=100, edgecolors='black', label='Data Points', zorder=3)

# Calculate linear regression line using numpy
m, b = np.polyfit(df['Experience'], df['Salary'], 1)
x_line = np.linspace(df['Experience'].min(), df['Experience'].max(), 100)
plt.plot(x_line, m*x_line + b, color='#d62728', linewidth=2.5, label=f'Trendline (y = {m:.0f}x + {b:,.0f})')

plt.title('Experience vs Salary (Trend Line)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Experience (Years)', fontweight='bold')
plt.ylabel('Salary ($)', fontweight='bold')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('experience_salary.png', dpi=300)
plt.close()

print("All 5 charts successfully generated and saved using pure Matplotlib.")