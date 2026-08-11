import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# -------------------------------------------------------------
# 1. Create Realistic Skewed Salary Dataset
# -------------------------------------------------------------
np.random.seed(42)
n_employees = 300

# Generating right-skewed salary data (Lognormal Distribution)
salaries = np.random.lognormal(mean=11.0, sigma=0.45, size=n_employees).round(2)
salaries = np.clip(salaries, 35000, 350000) # Clip bounds

departments = np.random.choice(['Engineering', 'Sales', 'IT', 'HR', 'Marketing'], size=n_employees, p=[0.3, 0.25, 0.20, 0.15, 0.10])

df = pd.DataFrame({'Department': departments, 'Salary': salaries})

# -------------------------------------------------------------
# 2. Compute Summary Statistics
# -------------------------------------------------------------
mean_sal   = df['Salary'].mean()
median_sal = df['Salary'].median()
std_sal    = df['Salary'].std()
skewness   = df['Salary'].skew()

q1 = df['Salary'].quantile(0.25)
q3 = df['Salary'].quantile(0.75)
iqr = q3 - q1

# IQR Outlier Boundaries
upper_bound = q3 + (1.5 * iqr)
outliers = df[df['Salary'] > upper_bound]

print("="*50)
print("📊 SALARY STATISTICAL SUMMARY")
print("="*50)
print(f"Mean Salary       : ${mean_sal:,.2f}")
print(f"Median Salary     : ${median_sal:,.2f}  <-- Prefer this for skewed data")
print(f"Standard Deviation: ${std_sal:,.2f}")
print(f"Skewness Coefficient: {skewness:.2f} (>0 means Right-Skewed)")
print(f"Interquartile Range (IQR): ${iqr:,.2f} (${q1:,.0f} to ${q3:,.0f})")
print(f"High-Earner Outliers Count: {len(outliers)} (Threshold > ${upper_bound:,.2f})")
print("="*50)

# -------------------------------------------------------------
# 3. Visualization Dashboard
# -------------------------------------------------------------
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 5))
fig.suptitle('Salary Distribution Analysis', fontsize=16, fontweight='bold')

# Chart 1: Histogram + Kernel Density Estimate (KDE)
axes[0].hist(df['Salary'], bins=20, color='#2ecc71', edgecolor='#1e8449', alpha=0.75, density=False)
axes[0].axvline(mean_sal, color='#e74c3c', linestyle='--', linewidth=2, label=f'Mean (${mean_sal:,.0f})')
axes[0].axvline(median_sal, color='#2c3e50', linestyle='-', linewidth=2, label=f'Median (${median_sal:,.0f})')

axes[0].set_title('1. Overall Salary Distribution (Histogram)', fontweight='bold')
axes[0].set_xlabel('Salary ($)')
axes[0].set_ylabel('Frequency')
axes[0].xaxis.set_major_formatter('${x:,.0f}')
axes[0].grid(axis='y', linestyle='--', alpha=0.5)
axes[0].legend()

# Chart 2: Boxplot by Department (Spread & Outliers)
df.boxplot(column='Salary', by='Department', ax=axes[1], patch_artist=True, grid=False)
axes[1].set_title('2. Salary Spread & Outliers by Department', fontweight='bold')
axes[1].set_xlabel('Department')
axes[1].set_ylabel('Salary ($)')
axes[1].yaxis.set_major_formatter('${x:,.0f}')
plt.suptitle('') # Clear automatic pandas title artifact

plt.tight_layout()
plt.show()