import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------------------
# 1. Generate Realistic Age Dataset
# -------------------------------------------------------------
np.random.seed(42)
n_samples = 350

# Simulated workforce ages centered around 36 with standard deviation of 9
ages = np.random.normal(loc=36, scale=9, size=n_samples).astype(int)
ages = np.clip(ages, 18, 65) # Restrict ages between 18 and 65

df = pd.DataFrame({'Age': ages})

# -------------------------------------------------------------
# 2. Descriptive Statistics & Distribution Checks
# -------------------------------------------------------------
mean_age   = df['Age'].mean()
median_age = df['Age'].median()
std_age    = df['Age'].std()
skewness   = df['Age'].skew()
min_age    = df['Age'].min()
max_age    = df['Age'].max()

print("="*45)
print("📊 AGE DISTRIBUTION SUMMARY")
print("="*45)
print(f"Mean Age          : {mean_age:.1f} years")
print(f"Median Age        : {median_age:.1f} years")
print(f"Age Range         : {min_age} to {max_age} years")
print(f"Standard Deviation: {std_age:.2f} years")
print(f"Skewness          : {skewness:.2f}")
print("="*45)

# -------------------------------------------------------------
# 3. Categorical Age Binning (Bracket Analysis)
# -------------------------------------------------------------
bins = [17, 25, 35, 45, 55, 65]
labels = ['18-25 (Entry)', '26-35 (Mid-level)', '36-45 (Senior)', '46-55 (Lead)', '56-65 (Executive)']

df['Age_Group'] = pd.cut(df['Age'], bins=bins, labels=labels)

print("\n--- Age Group Breakdown ---")
age_group_summary = pd.DataFrame({
    'Count': df['Age_Group'].value_counts(sort=False),
    'Share (%)': (df['Age_Group'].value_counts(normalize=True, sort=False) * 100).round(2)
})
print(age_group_summary)

# -------------------------------------------------------------
# 4. Visualizations Dashboard
# -------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1: Histogram with Mean & Median lines
axes[0].hist(df['Age'], bins=12, color='#3498db', edgecolor='black', alpha=0.75)
axes[0].axvline(mean_age, color='#e74c3c', linestyle='--', linewidth=2, label=f'Mean ({mean_age:.1f})')
axes[0].axvline(median_age, color='#2c3e50', linestyle='-', linewidth=2, label=f'Median ({median_age:.1f})')

axes[0].set_title('1. Age Continuous Distribution (Histogram)', fontweight='bold')
axes[0].set_xlabel('Age (Years)')
axes[0].set_ylabel('Frequency')
axes[0].grid(axis='y', linestyle='--', alpha=0.5)
axes[0].legend()

# Plot 2: Categorical Age Brackets Bar Chart
df['Age_Group'].value_counts(sort=False).plot(
    kind='bar', 
    ax=axes[1], 
    color='#2ecc71', 
    edgecolor='black'
)
axes[1].set_title('2. Distribution by Age Brackets (pd.cut)', fontweight='bold')
axes[1].set_xlabel('Age Group')
axes[1].set_ylabel('Count')
axes[1].tick_params(axis='x', rotation=30)
axes[1].grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()