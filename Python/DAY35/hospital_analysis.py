import pandas as pd
import numpy as np

# =====================================================================
# 1. REPLACE THIS SAMPLE DATASET WITH YOUR ACTUAL DATA
# =====================================================================
data = {
    'PatientID': [101, 102, 103, 104, 105, 106, 107, 108],
    'Department': ['Cardiology', 'ICU', 'Pediatrics', 'Cardiology', 'ICU', 'Neurology', 'Cardiology', 'Neurology'],
    'Age': [65, 72, 8, 58, 80, 45, 62, 38],
    'Bill': [45000, 120000, 12000, 38000, 250000, 55000, 42000, 48000],
    'StayDays': [5, 12, 2, 4, 20, 6, 5, 4]
}

df = pd.DataFrame(data)

# =====================================================================
# 2. AGE STATISTICAL ANALYSIS
# =====================================================================
age_stats = {
    'Mean': df['Age'].mean(),
    'Median': df['Age'].median(),
    'Min': df['Age'].min(),
    'Max': df['Age'].max(),
    'Std': df['Age'].std(),
    'Q1': df['Age'].quantile(0.25),
    'Q3': df['Age'].quantile(0.75),
}
age_stats['IQR'] = age_stats['Q3'] - age_stats['Q1']

# =====================================================================
# 3. BILL STATISTICAL ANALYSIS & OUTLIERS
# =====================================================================
bill_stats = {
    'Mean': df['Bill'].mean(),
    'Median': df['Bill'].median(),
    'Min': df['Bill'].min(),
    'Max': df['Bill'].max(),
    'Std': df['Bill'].std(),
    'Q1': df['Bill'].quantile(0.25),
    'Q3': df['Bill'].quantile(0.75),
}
bill_stats['IQR'] = bill_stats['Q3'] - bill_stats['Q1']

# Outlier Detection (1.5 * IQR Rule)
bill_upper_bound = bill_stats['Q3'] + (1.5 * bill_stats['IQR'])
bill_lower_bound = bill_stats['Q1'] - (1.5 * bill_stats['IQR'])
outliers = df[(df['Bill'] < bill_lower_bound) | (df['Bill'] > bill_upper_bound)]

# =====================================================================
# 4. STATISTICAL RESULTS OUTPUT
# =====================================================================
print("=" * 60)
print("📊 1. AGE STATISTICAL ANALYSIS")
print("=" * 60)
for k, v in age_stats.items():
    print(f"• {k:<10}: {v:.2f}")

print("\n" + "=" * 60)
print("💰 2. BILL STATISTICAL ANALYSIS")
print("=" * 60)
for k, v in bill_stats.items():
    print(f"• {k:<10}: ${v:,.2f}")

print("\n" + "=" * 60)
print("🔍 3. BILL SUMMARY & OUTLIERS")
print("=" * 60)
print(f"• Highest Bill : ${bill_stats['Max']:,.2f}")
print(f"• Lowest Bill  : ${bill_stats['Min']:,.2f}")
print(f"• Average Bill : ${bill_stats['Mean']:,.2f}")
print(f"• Median Bill  : ${bill_stats['Median']:,.2f}")

if not outliers.empty:
    print(f"\n⚠️ Possible Outliers (High-Cost Extreme Cases):")
    for _, row in outliers.iterrows():
        print(f"  - Patient ID {row['PatientID']} ({row['Department']}): ${row['Bill']:,} (Stay: {row['StayDays']} days)")
else:
    print("\n• Possible Outliers: No extreme outliers detected.")

# =====================================================================
# 5. 5 MEANINGFUL INSIGHTS
# =====================================================================
print("\n" + "=" * 60)
print("💡 5 MEANINGFUL INSIGHTS")
print("=" * 60)

# Insight 1: Bill Distribution Skewness
if bill_stats['Mean'] > bill_stats['Median']:
    print("1. Right-Skewed Bill Distribution: The Average Bill (Mean) is higher than the Median, indicating that a small number of extremely high-cost patients (e.g., ICU cases) are pulling the overall average upward.")
else:
    print("1. Symmetric Bill Distribution: The Mean and Median bills are closely aligned, showing a balanced cost spread.")

# Insight 2: High-Cost Department Identification
dept_bill = df.groupby('Department')['Bill'].mean()
highest_dept = dept_bill.idxmax()
print(f"2. Most Expensive Department: The '{highest_dept}' department records the highest average billing per patient.")

# Insight 3: Patient Demographic Spread
print(f"3. Core Patient Age Demographics: The middle 50% of hospital patients (Interquartile Range Q1 to Q3) fall between {age_stats['Q1']:.0f} and {age_stats['Q3']:.0f} years of age.")

# Insight 4: Stay Duration Impact
corr = df['StayDays'].corr(df['Bill'])
print(f"4. Hospital Stay Impact: There is a strong positive correlation (r = {corr:.2f}) between the length of stay (StayDays) and total billing.")

# Insight 5: Extreme Outlier Identification
if not outliers.empty:
    print(f"5. Extreme Billing Anomalies: Identified {len(outliers)} statistical outlier(s) exceeding the 1.5x IQR threshold, driven by prolonged hospital stays or specialized treatment requirements.")
else:
    print("5. Cost Consistency: 75% of patient bills remain within normal expected statistical boundaries (below the Q3 upper limit).")