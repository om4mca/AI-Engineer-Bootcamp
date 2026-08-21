import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Set random seed for consistent results
np.random.seed(42)

# ==============================================================================
# SECTION 1: EMPLOYEE DATASET GENERATION & PREPROCESSING
# ==============================================================================
n_emp = 150

emp_ids = [f'EMP-{1000 + i}' for i in range(n_emp)]
emp_depts = np.random.choice(['Engineering', 'Sales', 'Marketing', 'HR'], size=n_emp, p=[0.35, 0.30, 0.20, 0.15])
emp_age = np.random.randint(22, 63, size=n_emp)

# Experience correlated with age
emp_exp = np.clip((emp_age - 22) // 1.4 + np.random.randint(-2, 3, size=n_emp), 0, 38).astype(int)

# Salary with base compensation and department multipliers
dept_mult = {'Engineering': 1.35, 'Sales': 1.15, 'Marketing': 1.0, 'HR': 0.90}
base_sal = 42000 + (emp_exp * 3100)
mult_array = np.array([dept_mult[d] for d in emp_depts])
emp_salary = (base_sal * mult_array) + np.random.normal(0, 4500, size=n_emp)

# Performance scores (1 to 10 scale)
emp_perf = np.clip(np.random.normal(6.8, 1.3, size=n_emp), 1.0, 10.0)

# Inject intentional extreme outliers
emp_salary[8] = 255000.00    # Executive salary outlier
emp_salary[45] = 240000.00   # High compensation outlier
emp_perf[72] = 1.1           # Performance anomaly

df_emp = pd.DataFrame({
    'EmployeeID': emp_ids,
    'Department': emp_depts,
    'Age': emp_age,
    'Experience': emp_exp,
    'Salary': emp_salary.round(2),
    'Performance': emp_perf.round(2)
})

# ==============================================================================
# SECTION 2: HOSPITAL DATASET GENERATION & PREPROCESSING
# ==============================================================================
n_hosp = 200

hosp_ids = [f'PAT-{2000 + i}' for i in range(n_hosp)]
hosp_genders = np.random.choice(['Male', 'Female'], size=n_hosp, p=[0.49, 0.51])
hosp_depts = np.random.choice(
    ['Cardiology', 'Orthopedics', 'Pediatrics', 'Oncology', 'General Surgery'],
    size=n_hosp, p=[0.25, 0.20, 0.15, 0.15, 0.25]
)

# Patient Age
hosp_age = np.clip(np.random.normal(57, 19, size=n_hosp), 1, 94).astype(int)

# Stay Duration (Days) - Exponential right-skewed pattern
hosp_stay = np.round(np.random.exponential(scale=5.2, size=n_hosp) + 1).astype(int)

# Hospital Bill ($) - Correlated with stay duration and department multiplier
hosp_dept_mult = {'Cardiology': 1.65, 'Orthopedics': 1.40, 'Oncology': 1.85, 'General Surgery': 1.25, 'Pediatrics': 0.95}
bill_base = hosp_stay * np.random.uniform(1300, 2600, size=n_hosp)
bill_mult = np.array([hosp_dept_mult[d] for d in hosp_depts])
hosp_bill = np.clip((bill_base * bill_mult) + np.random.normal(400, 150, size=n_hosp), 450, None).round(2)

# Inject intentional extreme outliers
hosp_bill[12] = 138000.00    # Billing outlier
hosp_stay[33] = 46           # Chronic stay duration outlier

df_hosp = pd.DataFrame({
    'PatientID': hosp_ids,
    'Gender': hosp_genders,
    'Department': hosp_depts,
    'Age': hosp_age,
    'StayDays': hosp_stay,
    'Bill': hosp_bill
})

# ==============================================================================
# SECTION 3: STATISTICAL FUNCTIONS & CALCULATIONS
# ==============================================================================
def generate_summary(df, num_cols):
    summary = pd.DataFrame(index=num_cols)
    summary['Mean'] = df[num_cols].mean().round(2)
    summary['Median'] = df[num_cols].median().round(2)
    summary['Std_Dev'] = df[num_cols].std(ddof=1).round(2)
    summary['Variance'] = df[num_cols].var(ddof=1).round(2)
    summary['Q1_25%'] = df[num_cols].quantile(0.25).round(2)
    summary['Q3_75%'] = df[num_cols].quantile(0.75).round(2)
    summary['IQR'] = (summary['Q3_75%'] - summary['Q1_25%']).round(2)
    summary['Coeff_Var (%)'] = ((summary['Std_Dev'] / summary['Mean']) * 100).round(2)
    return summary

emp_num_cols = ['Age', 'Experience', 'Salary', 'Performance']
hosp_num_cols = ['Age', 'StayDays', 'Bill']

emp_stats = generate_summary(df_emp, emp_num_cols)
hosp_stats = generate_summary(df_hosp, hosp_num_cols)

# ==============================================================================
# SECTION 4: STANDARDIZATION & OUTLIER DETECTION
# ==============================================================================
# Compute Z-Scores using Scipy
for col in emp_num_cols:
    df_emp[f'{col}_ZScore'] = stats.zscore(df_emp[col]).round(2)

for col in hosp_num_cols:
    df_hosp[f'{col}_ZScore'] = stats.zscore(df_hosp[col]).round(2)

# Identify extreme anomalies (|Z| > 3.0)
emp_anomalies = df_emp[(df_emp['Salary_ZScore'].abs() > 3.0) | (df_emp['Performance_ZScore'].abs() > 3.0)]
hosp_anomalies = df_hosp[(df_hosp['Bill_ZScore'].abs() > 3.0) | (df_hosp['StayDays_ZScore'].abs() > 3.0)]

# ==============================================================================
# SECTION 5: PROBABILITY & DISTRIBUTION TESTS
# ==============================================================================
# Empirical vs Theoretical probabilities for 1SD, 2SD, 3SD
def verify_empirical_rule(series):
    z = np.abs(stats.zscore(series))
    p1 = (z <= 1.0).mean() * 100
    p2 = (z <= 2.0).mean() * 100
    p3 = (z <= 3.0).mean() * 100
    return round(p1, 2), round(p2, 2), round(p3, 2)

# Shapiro-Wilk Normality Tests
emp_salary_shapiro = stats.shapiro(df_emp['Salary'])
hosp_bill_shapiro = stats.shapiro(df_hosp['Bill'])

# Print Executive Summaries
print("=== EMPLOYEE DATASET STATISTICAL SUMMARY ===")
print(emp_stats.to_string())
print("\n=== HOSPITAL DATASET STATISTICAL SUMMARY ===")
print(hosp_stats.to_string())

# ==============================================================================
# SECTION 6: VISUALIZATIONS
# ==============================================================================
fig, axes = plt.subplots(3, 4, figsize=(18, 12))
plt.subplots_adjust(hspace=0.4, wspace=0.3)

# Employee Plots
axes[0, 0].hist(df_emp['Salary'], bins=15, color='#1f77b4', edgecolor='black', alpha=0.7)
axes[0, 0].set_title('Employee Salary Distribution')
axes[0, 0].set_xlabel('Salary ($)')

axes[0, 1].hist(df_emp['Performance'], bins=12, color='#2ca02c', edgecolor='black', alpha=0.7)
axes[0, 1].set_title('Employee Performance Distribution')
axes[0, 1].set_xlabel('Score (1-10)')

axes[0, 2].boxplot(df_emp['Salary'], patch_artist=True, boxprops=dict(facecolor='#1f77b4', alpha=0.6))
axes[0, 2].set_title('Salary Boxplot')

axes[0, 3].scatter(df_emp['Experience'], df_emp['Salary'], c=df_emp['Performance'], cmap='viridis', alpha=0.8, edgecolors='k')
axes[0, 3].set_title('Experience vs Salary (Color=Perf)')
axes[0, 3].set_xlabel('Experience (Yrs)')

# Hospital Plots
axes[1, 0].hist(df_hosp['Bill'], bins=15, color='#d62728', edgecolor='black', alpha=0.7)
axes[1, 0].set_title('Hospital Bill Distribution')
axes[1, 0].set_xlabel('Bill ($)')

axes[1, 1].hist(df_hosp['StayDays'], bins=15, color='#ff7f0e', edgecolor='black', alpha=0.7)
axes[1, 1].set_title('Stay Duration Distribution')
axes[1, 1].set_xlabel('Days')

axes[1, 2].boxplot(df_hosp['Bill'], patch_artist=True, boxprops=dict(facecolor='#d62728', alpha=0.6))
axes[1, 2].set_title('Bill Boxplot')

axes[1, 3].scatter(df_hosp['StayDays'], df_hosp['Bill'], c=df_hosp['Age'], cmap='plasma', alpha=0.8, edgecolors='k')
axes[1, 3].set_title('Stay Days vs Bill (Color=Age)')
axes[1, 3].set_xlabel('Stay Days')

# Z-Score Standardized Overlay Plots
axes[2, 0].hist(df_emp['Salary_ZScore'], bins=15, color='#17becf', edgecolor='black', alpha=0.7)
axes[2, 0].set_title('Standardized Salary Z-Scores')

axes[2, 1].hist(df_hosp['Bill_ZScore'], bins=15, color='#e377c2', edgecolor='black', alpha=0.7)
axes[2, 1].set_title('Standardized Bill Z-Scores')

# Combined Departmental Averages
emp_dept_means = df_emp.groupby('Department')['Salary'].mean()
axes[2, 2].bar(emp_dept_means.index, emp_dept_means.values, color='#8c564b', edgecolor='black', alpha=0.7)
axes[2, 2].set_title('Mean Salary by Dept')

hosp_dept_means = df_hosp.groupby('Department')['Bill'].mean()
axes[2, 3].bar(hosp_dept_means.index, hosp_dept_means.values, color='#7f7f7f', edgecolor='black', alpha=0.7)
axes[2, 3].set_title('Mean Bill by Dept')
axes[2, 3].tick_params(axis='x', rotation=30)

plt.suptitle('Day 40 Integration Exercise - Statistical Analysis', fontsize=16, fontweight='bold')
plt.show()