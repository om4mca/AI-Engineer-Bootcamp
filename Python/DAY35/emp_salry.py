import pandas as pd
import numpy as np

# =====================================================================
# STEP 1: REPLACE THIS SAMPLE DATA WITH YOUR ACTUAL DATASET
# =====================================================================
data = {
    'EmployeeID': [101, 102, 103, 104, 105, 106, 107, 108],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Henry'],
    'Department': ['IT', 'HR', 'IT', 'Sales', 'Sales', 'IT', 'HR', 'IT'],
    'Age': [28, 35, 29, 42, 31, 55, 40, 24],
    'Salary': [65000, 50000, 68000, 72000, 71000, 180000, 52000, 62000], # Example values
    'Experience': [3, 8, 4, 15, 6, 25, 12, 1]
}

df = pd.DataFrame(data)

# =====================================================================
# STEP 2: CALCULATE ALL REQUIRED STATISTICAL METRICS
# =====================================================================
mean_sal   = df['Salary'].mean()
median_sal = df['Salary'].median()

# Mode can be multiple values if tied; take the first one or convert to list
mode_series = df['Salary'].mode()
mode_sal   = mode_series.tolist() if len(mode_series) > 1 else mode_series[0]

min_sal    = df['Salary'].min()
max_sal    = df['Salary'].max()
range_sal  = max_sal - min_sal

variance_sal = df['Salary'].var()      # Sample variance
std_sal      = df['Salary'].std()      # Sample standard deviation

q1  = df['Salary'].quantile(0.25)
q2  = df['Salary'].quantile(0.50)      # Same as Median
q3  = df['Salary'].quantile(0.75)
iqr = q3 - q1

# Outlier Detection (1.5 * IQR Rule)
lower_bound = q1 - (1.5 * iqr)
upper_bound = q3 + (1.5 * iqr)
outliers    = df[(df['Salary'] < lower_bound) | (df['Salary'] > upper_bound)]

# Department Aggregations
dept_summary = df.groupby('Department')['Salary'].agg(
    Avg_Salary='mean',
    Std_Dev='std',
    Variance='var',
    Count='count'
)

# =====================================================================
# STEP 3: PRINT CALCULATED STATISTICAL TABLE
# =====================================================================
print("=" * 55)
print("           📊 SALARY STATISTICAL ANALYSIS")
print("=" * 55)
print(f"Mean Salary              : ${mean_sal:,.2f}")
print(f"Median Salary (Q2)       : ${median_sal:,.2f}")
print(f"Mode Salary              : {mode_sal}")
print(f"Minimum Salary           : ${min_sal:,.2f}")
print(f"Maximum Salary           : ${max_sal:,.2f}")
print(f"Range                    : ${range_sal:,.2f}")
print(f"Variance                 : {variance_sal:,.2f}")
print(f"Standard Deviation (Std) : ${std_sal:,.2f}")
print(f"Q1 (25th Percentile)     : ${q1:,.2f}")
print(f"Q2 (50th Percentile)     : ${q2:,.2f}")
print(f"Q3 (75th Percentile)     : ${q3:,.2f}")
print(f"Interquartile Range (IQR): ${iqr:,.2f}")
print("=" * 55)

# =====================================================================
# STEP 4: ANSWER INSIGHT QUESTIONS
# =====================================================================
print("\n💡 INSIGHTS\n")

# 1. Highest Average Salary Department
highest_avg_dept = dept_summary['Avg_Salary'].idxmax()
highest_avg_val  = dept_summary['Avg_Salary'].max()
print(f"1. Highest Average Salary Dept : {highest_avg_dept} (${highest_avg_val:,.2f})")

# 2. Difference Between Mean and Median
mean_median_diff_pct = abs(mean_sal - median_sal) / median_sal * 100
is_significantly_different = "YES" if mean_median_diff_pct > 10 else "NO"
print(f"2. Is Mean significantly different from Median? : {is_significantly_different}")
print(f"   (Difference is ${abs(mean_sal - median_sal):,.2f} or {mean_median_diff_pct:.1f}%)")

# 3. Unusual / Outlier Salaries
if not outliers.empty:
    print(f"3. Unusual Salaries Identified : YES")
    for _, row in outliers.iterrows():
        print(f"   • {row['Name']} ({row['Department']}): ${row['Salary']:,.2f}")
else:
    print("3. Unusual Salaries Identified : NO (All salaries lie within normal IQR bounds)")

# 4. Department with Highest Variation
highest_var_dept = dept_summary['Std_Dev'].idxmax()
highest_var_val  = dept_summary['Std_Dev'].max()
print(f"4. Department with Highest Salary Variation : {highest_var_dept} (Std Dev: ${highest_var_val:,.2f})")

# 5. Distribution Assessment
skewness = df['Salary'].skew()
if skewness > 0.5:
    dist_type = "Right-Skewed (Positively Skewed) — pulled up by high earners"
elif skewness < -0.5:
    dist_type = "Left-Skewed (Negatively Skewed) — pulled down by low earners"
else:
    dist_type = "Approximately Symmetric (Bell-shaped)"

print(f"5. Distribution Type : {dist_type} (Skewness = {skewness:.2f})")