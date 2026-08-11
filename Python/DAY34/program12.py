import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------------------
# 1. Generate Synthetic Department Data
# -------------------------------------------------------------
np.random.seed(42)
n_employees = 400

depts = ['Engineering', 'Sales', 'IT', 'Marketing', 'HR', 'Finance']
probabilities = [0.35, 0.25, 0.15, 0.10, 0.08, 0.07] # Realistic headcount imbalance

df = pd.DataFrame({
    'EmployeeID': [f'EMP-{1000+i}' for i in range(n_employees)],
    'Department': np.random.choice(depts, size=n_employees, p=probabilities),
    'Salary': np.random.lognormal(mean=11.1, sigma=0.4, size=n_employees).round(2)
})

# -------------------------------------------------------------
# 2. Headcount & Percentage Breakdown
# -------------------------------------------------------------
headcount_summary = pd.DataFrame({
    'Headcount': df['Department'].value_counts(),
    'Share (%)': (df['Department'].value_counts(normalize=True) * 100).round(2)
})

print("="*45)
print("📊 DEPARTMENT HEADCOUNT SUMMARY")
print("="*45)
print(headcount_summary)

# -------------------------------------------------------------
# 3. Aggregated Salary Statistics by Department
# -------------------------------------------------------------
dept_stats = df.groupby('Department')['Salary'].agg(
    Headcount='count',
    Mean_Salary='mean',
    Median_Salary='median',
    Min_Salary='min',
    Max_Salary='max',
    Std_Dev='std'
).round(2).sort_values(by='Headcount', ascending=False)


print("💰 SALARY METRICS BY DEPARTMENT")
print("="*65)
print(dept_stats)

# -------------------------------------------------------------
# 4. Visualization Dashboard
# -------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(15, 5))

# Chart 1: Horizontal Bar Plot (Headcount Share)
df['Department'].value_counts().plot(
    kind='barh', 
    ax=axes[0], 
    color='#3498db', 
    edgecolor='black'
)
axes[0].set_title('1. Headcount Distribution by Department', fontweight='bold')
axes[0].set_xlabel('Number of Employees')
axes[0].set_ylabel('Department')
axes[0].invert_yaxis() # Display top department at the top
axes[0].grid(axis='x', linestyle='--', alpha=0.5)

# Chart 2: Box Plot (Salary Distribution & Outliers per Dept)
df.boxplot(column='Salary', by='Department', ax=axes[1], patch_artist=True, grid=False)
axes[1].set_title('2. Salary Spread & Outliers by Department', fontweight='bold')
axes[1].set_xlabel('Department')
axes[1].set_ylabel('Salary ($)')
axes[1].yaxis.set_major_formatter('${x:,.0f}')
plt.suptitle('') # Remove automatic title artifact

plt.tight_layout()
plt.show()