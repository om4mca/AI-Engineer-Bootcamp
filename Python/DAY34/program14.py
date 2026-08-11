import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------------------
# 1. Generate Synthetic Age vs Salary Dataset
# -------------------------------------------------------------
np.random.seed(42)
n = 300

ages = np.random.randint(22, 65, size=n)
# Base salary increases with age + noise
salaries = 30000 + (ages - 22) * 1800 + np.random.normal(0, 15000, size=n)
salaries = np.clip(salaries, 30000, 250000).round(2)

df = pd.DataFrame({'Age': ages, 'Salary': salaries})

# -------------------------------------------------------------
# 2. Correlation Metrics
# -------------------------------------------------------------
pearson_corr  = df['Age'].corr(df['Salary'], method='pearson')
spearman_corr = df['Age'].corr(df['Salary'], method='spearman')

print("="*45)
print("📊 CORRELATION ANALYSIS")
print("="*45)
print(f"Pearson Correlation (Linear)  : {pearson_corr:.2f}")
print(f"Spearman Correlation (Monotonic): {spearman_corr:.2f}")

# -------------------------------------------------------------
# 3. Aggregation by Age Brackets (pd.cut)
# -------------------------------------------------------------
age_bins = [20, 30, 40, 50, 65]
age_labels = ['21-30', '31-40', '41-50', '51-65']
df['Age_Group'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels)

bracket_summary = df.groupby('Age_Group', observed=False)['Salary'].agg(
    Employee_Count='count',
    Mean_Salary='mean',
    Median_Salary='median',
    Std_Dev='std'
).round(2)


print("💰 SALARY METRICS BY AGE BRACKET")
print("="*55)
print(bracket_summary)

# -------------------------------------------------------------
# 4. Bivariate Visualization Dashboard
# -------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(15, 5))

# Chart 1: Scatter Plot with Trend Line
axes[0].scatter(df['Age'], df['Salary'], alpha=0.6, color='#3498db', edgecolors='k')
# Polynomial/Linear fit trend line
z = np.polyfit(df['Age'], df['Salary'], 1)
p = np.poly1d(z)
axes[0].plot(df['Age'], p(df['Age']), color='#e74c3c', linewidth=2, label=f'Trend Line (r={pearson_corr:.2f})')

axes[0].set_title('1. Scatter Plot: Age vs. Salary', fontweight='bold')
axes[0].set_xlabel('Age (Years)')
axes[0].set_ylabel('Salary ($)')
axes[0].yaxis.set_major_formatter('${x:,.0f}')
axes[0].grid(True, linestyle='--', alpha=0.5)
axes[0].legend()

# Chart 2: Boxplot by Age Group (Spread & Median Trends)
df.boxplot(column='Salary', by='Age_Group', ax=axes[1], patch_artist=True, grid=False)
axes[1].set_title('2. Salary Spread Across Age Brackets', fontweight='bold')
axes[1].set_xlabel('Age Bracket')
axes[1].set_ylabel('Salary ($)')
axes[1].yaxis.set_major_formatter('${x:,.0f}')
plt.suptitle('') # Clear pandas automatic title

plt.tight_layout()
plt.show()