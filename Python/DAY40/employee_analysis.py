import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Set seed for reproducibility
np.random.seed(42)

# ==========================================
# 1. DATASET CREATION
# ==========================================
n_employees = 150

departments = np.random.choice(['Engineering', 'Sales', 'HR', 'Marketing'], size=n_employees, p=[0.4, 0.3, 0.15, 0.15])
ages = np.random.randint(22, 61, size=n_employees)

# Experience correlated with age (with noise)
experience = np.clip((ages - 22) // 1.5 + np.random.randint(-2, 3, size=n_employees), 0, 35).astype(int)

# Salary base determined by experience + department factor + intentional outliers
dept_salary_mult = {'Engineering': 1.3, 'Sales': 1.1, 'Marketing': 1.0, 'HR': 0.95}
base_salary = 45000 + (experience * 3200)
dept_mult = np.array([dept_salary_mult[d] for d in departments])
salary = base_salary * dept_mult + np.random.normal(0, 5000, size=n_employees)

# Performance scores (1 to 10 scale)
performance = np.random.normal(6.5, 1.2, size=n_employees)
performance = np.clip(performance, 1.0, 10.0)

# Inject intentional outliers
salary[5] = 260000  # Executive level outlier
salary[12] = 230000 # High outlier
performance[42] = 1.2 # Severe underperformer outlier

df = pd.DataFrame({
    'EmployeeID': [f'EMP-{1000+i}' for i in range(n_employees)],
    'Department': departments,
    'Age': ages,
    'Experience': experience,
    'Salary': salary.round(2),
    'Performance': performance.round(2)
})

# ==========================================
# 2. STATISTICAL CALCULATIONS
# ==========================================
metrics = ['Age', 'Experience', 'Salary', 'Performance']

# Central Tendency & Spread Summary Table
stats_summary = pd.DataFrame(index=metrics)

# Mean
stats_summary['Mean'] = df[metrics].mean().round(2)

# Median
stats_summary['Median'] = df[metrics].median().round(2)

# Mode
stats_summary['Mode'] = df[metrics].apply(lambda x: x.mode()[0]).round(2)

# Variance (Sample, ddof=1)
stats_summary['Variance'] = df[metrics].var(ddof=1).round(2)

# Standard Deviation (Sample, ddof=1)
stats_summary['Std_Dev'] = df[metrics].std(ddof=1).round(2)

# IQR (Q3 - Q1)
q1 = df[metrics].quantile(0.25)
q3 = df[metrics].quantile(0.75)
stats_summary['IQR'] = (q3 - q1).round(2)

print("=== STATISTICAL SUMMARY (CENTRAL TENDENCY & SPREAD) ===")
print(stats_summary.to_string())
print("\n" + "="*60 + "\n")

# ==========================================
# 3. STANDARDIZATION (Z-SCORES)
# ==========================================
df['Salary_Z'] = stats.zscore(df['Salary']).round(3)
df['Performance_Z'] = stats.zscore(df['Performance']).round(3)

# ==========================================
# 4. OUTLIER ANALYSIS (|Z| > 2.0 & |Z| > 3.0)
# ==========================================
salary_outliers_z = df[df['Salary_Z'].abs() > 2.0]
perf_outliers_z = df[df['Performance_Z'].abs() > 2.0]

print("=== SALARY OUTLIERS (|Z| > 2.0) ===")
print(salary_outliers_z[['EmployeeID', 'Department', 'Salary', 'Salary_Z']].to_string(index=False))

print("\n=== PERFORMANCE OUTLIERS (|Z| > 2.0) ===")
print(perf_outliers_z[['EmployeeID', 'Department', 'Performance', 'Performance_Z']].to_string(index=False))
print("\n" + "="*60 + "\n")

# ==========================================
# 5. VISUALIZATIONS (PURE MATPLOTLIB)
# ==========================================
fig = plt.figure(figsize=(16, 12))
plt.subplots_adjust(hspace=0.4, wspace=0.3)

# Plot 1: Histograms (Distributions)
ax1 = plt.subplot(2, 3, 1)
ax1.hist(df['Salary'], bins=15, color='#2b5c8f', edgecolor='black', alpha=0.7)
ax1.set_title('Salary Distribution')
ax1.set_xlabel('Salary ($)')
ax1.set_ylabel('Frequency')
ax1.grid(axis='y', linestyle='--', alpha=0.5)

ax2 = plt.subplot(2, 3, 2)
ax2.hist(df['Age'], bins=12, color='#4682b4', edgecolor='black', alpha=0.7)
ax2.set_title('Age Distribution')
ax2.set_xlabel('Age')
ax2.set_ylabel('Frequency')
ax2.grid(axis='y', linestyle='--', alpha=0.5)

ax3 = plt.subplot(2, 3, 3)
ax3.hist(df['Performance'], bins=10, color='#6baed6', edgecolor='black', alpha=0.7)
ax3.set_title('Performance Score Distribution')
ax3.set_xlabel('Performance Score (1-10)')
ax3.set_ylabel('Frequency')
ax3.grid(axis='y', linestyle='--', alpha=0.5)

# Plot 2: Box Plots (Outlier Identification)
ax4 = plt.subplot(2, 3, 4)
bp1 = ax4.boxplot(df['Salary'], patch_artist=True, boxprops=dict(facecolor='#9ecae1'))
ax4.set_title('Salary Box Plot')
ax4.set_ylabel('Salary ($)')
ax4.set_xticklabels(['All Staff'])
ax4.grid(axis='y', linestyle='--', alpha=0.5)

ax5 = plt.subplot(2, 3, 5)
bp2 = ax5.boxplot(df['Performance'], patch_artist=True, boxprops=dict(facecolor='#c6dbef'))
ax5.set_title('Performance Box Plot')
ax5.set_ylabel('Score (1-10)')
ax5.set_xticklabels(['All Staff'])
ax5.grid(axis='y', linestyle='--', alpha=0.5)

# Plot 3: Scatter Plot (Experience vs. Salary)
ax6 = plt.subplot(2, 3, 6)
scatter = ax6.scatter(df['Experience'], df['Salary'], c=df['Performance'], cmap='viridis', alpha=0.8, edgecolors='k')
ax6.set_title('Experience vs. Salary (Color = Performance)')
ax6.set_xlabel('Experience (Years)')
ax6.set_ylabel('Salary ($)')
cbar = plt.colorbar(scatter, ax=ax6)
cbar.set_label('Performance')
ax6.grid(True, linestyle='--', alpha=0.5)

plt.suptitle('Employee Statistical Intelligence System', fontsize=16, fontweight='bold')
plt.show()