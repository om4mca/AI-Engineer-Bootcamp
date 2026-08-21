import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Set seed for reproducible synthetic dataset
np.random.seed(42)

# ==========================================
# 1. DATASET CREATION
# ==========================================
n_patients = 200

patient_ids = [f'PAT-{2000 + i}' for i in range(n_patients)]
genders = np.random.choice(['Male', 'Female'], size=n_patients, p=[0.48, 0.52])
departments = np.random.choice(
    ['Cardiology', 'Orthopedics', 'Pediatrics', 'Oncology', 'General Surgery'],
    size=n_patients,
    p=[0.25, 0.20, 0.15, 0.15, 0.25]
)

# Variable 1: Age (skewed toward older adults with pediatric cases)
age = np.random.normal(loc=58, scale=18, size=n_patients)
age = np.clip(age, 1, 92).astype(int)

# Variable 2: StayDays (right-skewed exponential-like distribution)
stay_days = np.random.exponential(scale=5, size=n_patients) + 1
stay_days = np.round(stay_days).astype(int)

# Variable 3: Bill (strongly right-skewed, correlated with StayDays + random variation)
base_cost = stay_days * np.random.uniform(1200, 2500, size=n_patients)
dept_multiplier = {
    'Cardiology': 1.6, 'Orthopedics': 1.4, 'Oncology': 1.8, 
    'General Surgery': 1.2, 'Pediatrics': 0.9
}
mult = np.array([dept_multiplier[d] for d in departments])
bill = (base_cost * mult) + np.random.normal(500, 200, size=n_patients)
bill = np.clip(bill, 500, None).round(2)

# Inject intentional extreme outliers
bill[15] = 125000.00      # Massive billing anomaly
stay_days[42] = 48        # Extended stay anomaly
age[88] = 95              # High age outlier

df = pd.DataFrame({
    'PatientID': patient_ids,
    'Age': age,
    'Gender': genders,
    'Department': departments,
    'Bill': bill,
    'StayDays': stay_days
})

# ==========================================
# 2. STATISTICAL CALCULATIONS
# ==========================================
num_cols = ['Age', 'Bill', 'StayDays']

# Calculate Central Tendency, Spread, & Percentiles
stats_table = pd.DataFrame(index=num_cols)

stats_table['Mean'] = df[num_cols].mean().round(2)
stats_table['Median'] = df[num_cols].median().round(2)
stats_table['Std_Dev'] = df[num_cols].std(ddof=1).round(2)
stats_table['25th_Percentile (Q1)'] = df[num_cols].quantile(0.25).round(2)
stats_table['75th_Percentile (Q3)'] = df[num_cols].quantile(0.75).round(2)

# Interquartile Range (IQR = Q3 - Q1)
stats_table['IQR'] = (stats_table['75th_Percentile (Q1)'] - stats_table['25th_Percentile (Q1)']).round(2)

# Coefficient of Variation (CV = Std_Dev / Mean) to evaluate relative variability
stats_table['Coeff_Var (%)'] = ((stats_table['Std_Dev'] / stats_table['Mean']) * 100).round(2)

print("=== STATISTICAL SUMMARY (CENTRAL TENDENCY, SPREAD, & PERCENTILES) ===")
print(stats_table.to_string())
print("\n" + "="*80 + "\n")

# ==========================================
# 3. Z-SCORE & OUTLIER ANALYSIS
# ==========================================
# Compute Z-Scores using scipy.stats.zscore
for col in num_cols:
    df[f'{col}_ZScore'] = stats.zscore(df[col]).round(2)

# IQR Outliers Detection (Tukey's Fences: < Q1 - 1.5*IQR or > Q3 + 1.5*IQR)
iqr_outliers_dict = {}
for col in num_cols:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outlier_count = df[(df[col] < lower_bound) | (df[col] > upper_bound)].shape[0]
    iqr_outliers_dict[col] = outlier_count

# Identify observations with unusually large absolute Z-scores (|Z| > 3.0)
extreme_z_mask = (df['Age_ZScore'].abs() > 3.0) | (df['Bill_ZScore'].abs() > 3.0) | (df['StayDays_ZScore'].abs() > 3.0)
extreme_observations = df[extreme_z_mask]

print("=== OBSERVATIONS WITH UNUSUALLY LARGE ABSOLUTE Z-SCORES (|Z| > 3.0) ===")
print(extreme_observations[['PatientID', 'Department', 'Age', 'Age_ZScore', 'Bill', 'Bill_ZScore', 'StayDays', 'StayDays_ZScore']].to_string(index=False))
print("\n" + "="*80 + "\n")

# ==========================================
# 4. VISUALIZATION (PURE MATPLOTLIB)
# ==========================================
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
plt.subplots_adjust(hspace=0.35, wspace=0.3)

# Row 1: Histograms / Distributions
# Age Distribution
axes[0, 0].hist(df['Age'], bins=15, color='#2c7bb6', edgecolor='black', alpha=0.8)
axes[0, 0].set_title('Age Distribution', fontsize=12, fontweight='bold')
axes[0, 0].set_xlabel('Age (Years)')
axes[0, 0].set_ylabel('Patient Count')
axes[0, 0].grid(axis='y', linestyle='--', alpha=0.5)

# Bill Distribution
axes[0, 1].hist(df['Bill'], bins=20, color='#d7191c', edgecolor='black', alpha=0.8)
axes[0, 1].set_title('Bill Distribution', fontsize=12, fontweight='bold')
axes[0, 1].set_xlabel('Bill Amount ($)')
axes[0, 1].set_ylabel('Patient Count')
axes[0, 1].grid(axis='y', linestyle='--', alpha=0.5)

# Stay Duration Distribution
axes[0, 2].hist(df['StayDays'], bins=15, color='#fdae61', edgecolor='black', alpha=0.8)
axes[0, 2].set_title('Stay Duration Distribution', fontsize=12, fontweight='bold')
axes[0, 2].set_xlabel('Stay Days')
axes[0, 2].set_ylabel('Patient Count')
axes[0, 2].grid(axis='y', linestyle='--', alpha=0.5)

# Row 2: Boxplots (Outlier Visualizations)
# Age Boxplot
axes[1, 0].boxplot(df['Age'], patch_artist=True, boxprops=dict(facecolor='#2c7bb6', alpha=0.6))
axes[1, 0].set_title('Age Boxplot', fontsize=12, fontweight='bold')
axes[1, 0].set_ylabel('Age (Years)')
axes[1, 0].set_xticklabels(['Patients'])
axes[1, 0].grid(axis='y', linestyle='--', alpha=0.5)

# Bill Boxplot
axes[1, 1].boxplot(df['Bill'], patch_artist=True, boxprops=dict(facecolor='#d7191c', alpha=0.6))
axes[1, 1].set_title('Bill Boxplot', fontsize=12, fontweight='bold')
axes[1, 1].set_ylabel('Bill Amount ($)')
axes[1, 1].set_xticklabels(['Patients'])
axes[1, 1].grid(axis='y', linestyle='--', alpha=0.5)

# StayDays Boxplot
axes[1, 2].boxplot(df['StayDays'], patch_artist=True, boxprops=dict(facecolor='#fdae61', alpha=0.6))
axes[1, 2].set_title('Stay Duration Boxplot', fontsize=12, fontweight='bold')
axes[1, 2].set_ylabel('Stay Days')
axes[1, 2].set_xticklabels(['Patients'])
axes[1, 2].grid(axis='y', linestyle='--', alpha=0.5)

plt.suptitle('Hospital Statistical Intelligence System - Clinical Metrics Analysis', fontsize=16, fontweight='bold')
plt.show()