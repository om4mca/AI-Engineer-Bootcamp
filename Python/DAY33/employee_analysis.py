import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set random seed for reproducible synthetic dataset
np.random.seed(42)

# 1. Generate Synthetic Dataset
n_employees = 120
departments = ['Engineering', 'Sales', 'Marketing', 'HR', 'Finance', 'Product']

df = pd.DataFrame({
    'EmployeeID': [f'EMP{1000 + i}' for i in range(n_employees)],
    'Name': [f'Employee_{i}' for i in range(n_employees)],
    'Department': np.random.choice(departments, size=n_employees, p=[0.3, 0.25, 0.15, 0.1, 0.1, 0.1]),
    'Age': np.random.randint(22, 60, size=n_employees),
    'Experience': np.random.randint(1, 25, size=n_employees)
})

# Calculate Salary based on Department baseline + Experience depth
dept_salary_base = {
    'Engineering': 75000, 'Sales': 60000, 'Marketing': 58000, 
    'HR': 52000, 'Finance': 68000, 'Product': 72000
}

df['Salary'] = df.apply(
    lambda row: dept_salary_base[row['Department']] + (row['Experience'] * 3200) + np.random.normal(0, 5000), 
    axis=1
).round(-2)

# Assign Performance Scores (1 to 5)
df['PerformanceScore'] = np.random.choice([1, 2, 3, 4, 5], size=n_employees, p=[0.05, 0.15, 0.45, 0.25, 0.10])

# 2. Setup Figure Grid (3 rows x 2 columns)
fig, axes = plt.subplots(3, 2, figsize=(14, 15))
fig.suptitle('Employee Performance & Organizational Dashboard', fontsize=18, fontweight='bold', y=0.98)

# -------------------------------------------------------------
# Chart 1: Department-wise Employee Count
# -------------------------------------------------------------
dept_counts = df['Department'].value_counts()
bars1 = axes[0, 0].bar(dept_counts.index, dept_counts.values, color='#2b5c8f', edgecolor='#1a334e', width=0.55)
axes[0, 0].set_title('Chart 1: Department-wise Employee Count', fontsize=12, fontweight='bold')
axes[0, 0].set_ylabel('Number of Employees')
axes[0, 0].tick_params(axis='x', rotation=15)
axes[0, 0].grid(axis='y', linestyle='--', alpha=0.5)

for bar in bars1:
    yval = bar.get_height()
    axes[0, 0].text(bar.get_x() + bar.get_width()/2, yval + 0.5, f'{int(yval)}', ha='center', va='bottom', fontweight='bold')

# -------------------------------------------------------------
# Chart 2: Average Salary by Department
# -------------------------------------------------------------
avg_sal = df.groupby('Department')['Salary'].mean().sort_values(ascending=False)
bars2 = axes[0, 1].bar(avg_sal.index, avg_sal.values, color='#27ae60', edgecolor='#1e8449', width=0.55)
axes[0, 1].set_title('Chart 2: Average Salary by Department', fontsize=12, fontweight='bold')
axes[0, 1].set_ylabel('Average Salary ($)')
axes[0, 1].yaxis.set_major_formatter('${x:,.0f}')
axes[0, 1].tick_params(axis='x', rotation=15)
axes[0, 1].grid(axis='y', linestyle='--', alpha=0.5)

for bar in bars2:
    yval = bar.get_height()
    axes[0, 1].text(bar.get_x() + bar.get_width()/2, yval + 1000, f'${yval:,.0f}', ha='center', va='bottom', fontweight='bold', fontsize=9)

# -------------------------------------------------------------
# Chart 3: Experience vs Salary
# -------------------------------------------------------------
axes[1, 0].scatter(df['Experience'], df['Salary'], color='#e67e22', edgecolor='#d35400', alpha=0.8, s=50)
z = np.polyfit(df['Experience'], df['Salary'], 1)
p = np.poly1d(z)
axes[1, 0].plot(df['Experience'], p(df['Experience']), color='#c0392b', linestyle='--', linewidth=2, label='Trendline')
axes[1, 0].set_title('Chart 3: Experience vs. Salary', fontsize=12, fontweight='bold')
axes[1, 0].set_xlabel('Experience (Years)')
axes[1, 0].set_ylabel('Salary ($)')
axes[1, 0].yaxis.set_major_formatter('${x:,.0f}')
axes[1, 0].grid(True, linestyle='--', alpha=0.5)
axes[1, 0].legend()

# -------------------------------------------------------------
# Chart 4: Age Distribution
# -------------------------------------------------------------
counts, bins, _ = axes[1, 1].hist(df['Age'], bins=8, color='#8e44ad', edgecolor='#4a235a', alpha=0.85)
axes[1, 1].set_title('Chart 4: Age Distribution', fontsize=12, fontweight='bold')
axes[1, 1].set_xlabel('Age (Years)')
axes[1, 1].set_ylabel('Employee Frequency')
axes[1, 1].grid(axis='y', linestyle='--', alpha=0.5)

for count, bin_left, bin_right in zip(counts, bins[:-1], bins[1:]):
    if count > 0:
        axes[1, 1].text((bin_left + bin_right)/2, count + 0.3, f'{int(count)}', ha='center', va='bottom', fontweight='bold')

# -------------------------------------------------------------
# Chart 5: Performance Score Distribution
# -------------------------------------------------------------
perf_counts = df['PerformanceScore'].value_counts().sort_index()
bars5 = axes[2, 0].bar(perf_counts.index.astype(str), perf_counts.values, color='#16a085', edgecolor='#0e6251', width=0.5)
axes[2, 0].set_title('Chart 5: Performance Score Distribution', fontsize=12, fontweight='bold')
axes[2, 0].set_xlabel('Performance Score (1 = Low, 5 = High)')
axes[2, 0].set_ylabel('Number of Employees')
axes[2, 0].grid(axis='y', linestyle='--', alpha=0.5)

for bar in bars5:
    yval = bar.get_height()
    axes[2, 0].text(bar.get_x() + bar.get_width()/2, yval + 0.5, f'{int(yval)}', ha='center', va='bottom', fontweight='bold')

# -------------------------------------------------------------
# Chart 6: Performance Score vs Salary (Pure Matplotlib Boxplot)
# -------------------------------------------------------------
# Group salary arrays by score for standard matplotlib boxplot
salary_by_score = [df[df['PerformanceScore'] == score]['Salary'] for score in sorted(df['PerformanceScore'].unique())]

box = axes[2, 1].boxplot(
    salary_by_score, 
    patch_artist=True,
    medianprops=dict(color='black', linewidth=1.5)
)

# Set the tick labels on the axis explicitly
axes[2, 1].set_xticks(range(1, len(salary_by_score) + 1))
axes[2, 1].set_xticklabels(sorted(df['PerformanceScore'].unique()))

# Custom color styling for the Matplotlib boxes
box_colors = ['#d6eaf8', '#aed6f1', '#5adeb2', '#3498db', '#2874a6']
for patch, color in zip(box['boxes'], box_colors):
    patch.set_facecolor(color)

axes[2, 1].set_title('Chart 6: Performance Score vs. Salary', fontsize=12, fontweight='bold')
axes[2, 1].set_xlabel('Performance Score (1 = Low, 5 = High)')
axes[2, 1].set_ylabel('Salary ($)')
axes[2, 1].yaxis.set_major_formatter('${x:,.0f}')
axes[2, 1].grid(axis='y', linestyle='--', alpha=0.5)

# Adjust layout and display
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()