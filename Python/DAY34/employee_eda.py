import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# -------------------------------------------------------------
# 1. Dataset Preparation (Synthetic Employee Data)
# -------------------------------------------------------------
np.random.seed(42)
n_emp = 250

departments = ['IT', 'Sales', 'Engineering', 'HR', 'Marketing']
emp_ids = [f'EMP-{1000 + i}' for i in range(n_emp)]
names = [f'Employee_{i}' for i in range(n_emp)]
dept_choice = np.random.choice(departments, size=n_emp, p=[0.30, 0.25, 0.20, 0.15, 0.10])

# Age between 22 and 60
age = np.random.randint(22, 60, size=n_emp)

# Experience is constrained by Age (Exp <= Age - 21)
max_exp = np.clip(age - 21, 0, 35)
experience = np.array([np.random.randint(0, m + 1) for m in max_exp])

# Salary correlated with Experience and Department
base_salary = 35000 + (experience * 3500)
dept_bonus = np.where(dept_choice == 'IT', 15000, 
             np.where(dept_choice == 'Engineering', 20000, 0))
salary = (base_salary + dept_bonus + np.random.normal(0, 5000, size=n_emp)).round(2).clip(min=30000)

performance = np.random.choice([1, 2, 3, 4, 5], size=n_emp, p=[0.05, 0.15, 0.50, 0.20, 0.10])

df = pd.DataFrame({
    'EmployeeID': emp_ids,
    'Name': names,
    'Department': dept_choice,
    'Age': age,
    'Salary': salary,
    'Experience': experience,
    'PerformanceScore': performance
})

# -------------------------------------------------------------
# Step 1 — Structure
# -------------------------------------------------------------
print("="*50)
print("STEP 1: STRUCTURE")
print("="*50)
print("Shape (Rows, Columns):", df.shape)
print("\nColumns:\n", df.columns.tolist())
print("\nData Types:\n", df.dtypes)
print("\nInfo Summary:")
df.info()

# -------------------------------------------------------------
# Step 2 — Data Quality
# -------------------------------------------------------------
print("\n" + "="*50)
print("STEP 2: DATA QUALITY")
print("="*50)
print("Missing Values per Column:\n", df.isnull().sum())
print("\nDuplicate Rows Count:", df.duplicated().sum())

# -------------------------------------------------------------
# Step 3 — Statistics
# -------------------------------------------------------------
print("\n" + "="*50)
print("STEP 3: STATISTICS")
print("="*50)
print(df.describe().round(2))

# -------------------------------------------------------------
# Step 4 — Categorical Analysis
# -------------------------------------------------------------
print("\n" + "="*50)
print("STEP 4: CATEGORICAL ANALYSIS")
print("="*50)
print("Department Headcount Breakdown:\n", df["Department"].value_counts())

# -------------------------------------------------------------
# Step 5 — Visualizations
# -------------------------------------------------------------
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(14, 15))
fig.suptitle('Employee Analytics & HR Dashboard', fontsize=18, fontweight='bold', y=0.98)

# 1. Department Employee Distribution (Bar Chart)
dept_counts = df['Department'].value_counts()
bars1 = axes[0, 0].bar(dept_counts.index, dept_counts.values, color='#1f77b4', edgecolor='#154360', width=0.55)
axes[0, 0].set_title('1. Employee Distribution by Department', fontweight='bold')
axes[0, 0].set_ylabel('Employee Count')
axes[0, 0].grid(axis='y', linestyle='--', alpha=0.5)

for bar in bars1:
    yval = bar.get_height()
    axes[0, 0].text(bar.get_x() + bar.get_width()/2, yval + 1, f'{int(yval)}', ha='center', va='bottom', fontweight='bold')

# 2. Salary Distribution (Histogram)
axes[0, 1].hist(df['Salary'], bins=12, color='#2ecc71', edgecolor='#1e8449', alpha=0.85)
axes[0, 1].set_title('2. Salary Distribution', fontweight='bold')
axes[0, 1].set_xlabel('Salary ($)')
axes[0, 1].set_ylabel('Frequency')
axes[0, 1].xaxis.set_major_formatter('${x:,.0f}')
axes[0, 1].grid(axis='y', linestyle='--', alpha=0.5)

# 3. Age Distribution (Histogram)
axes[1, 0].hist(df['Age'], bins=10, color='#9b59b6', edgecolor='#4a235a', alpha=0.85)
axes[1, 0].set_title('3. Age Distribution', fontweight='bold')
axes[1, 0].set_xlabel('Age (Years)')
axes[1, 0].set_ylabel('Frequency')
axes[1, 0].grid(axis='y', linestyle='--', alpha=0.5)

# 4. Age vs Salary (Scatter Plot)
axes[1, 1].scatter(df['Age'], df['Salary'], color='#e67e22', edgecolor='#d35400', alpha=0.7, s=50)
axes[1, 1].set_title('4. Age vs. Salary', fontweight='bold')
axes[1, 1].set_xlabel('Age (Years)')
axes[1, 1].set_ylabel('Salary ($)')
axes[1, 1].yaxis.set_major_formatter('${x:,.0f}')
axes[1, 1].grid(True, linestyle='--', alpha=0.5)

# 5. Experience vs Salary (Scatter Plot with Trendline)
axes[2, 0].scatter(df['Experience'], df['Salary'], color='#e74c3c', edgecolor='#922b21', alpha=0.7, s=50)
z = np.polyfit(df['Experience'], df['Salary'], 1)
p = np.poly1d(z)
axes[2, 0].plot(df['Experience'], p(df['Experience']), color='#2c3e50', linestyle='--', linewidth=2, label='Trendline')
axes[2, 0].set_title('5. Experience vs. Salary', fontweight='bold')
axes[2, 0].set_xlabel('Experience (Years)')
axes[2, 0].set_ylabel('Salary ($)')
axes[2, 0].yaxis.set_major_formatter('${x:,.0f}')
axes[2, 0].grid(True, linestyle='--', alpha=0.5)
axes[2, 0].legend()

# 6. Performance Score vs Salary (Bonus Plot)
df.boxplot(column='Salary', by='PerformanceScore', ax=axes[2, 1], patch_artist=True, grid=False)
axes[2, 1].set_title('6. Salary Spread across Performance Scores', fontweight='bold')
axes[2, 1].set_xlabel('Performance Rating (1-5)')
axes[2, 1].set_ylabel('Salary ($)')
axes[2, 1].yaxis.set_major_formatter('${x:,.0f}')
plt.suptitle('') # Clean up pandas boxplot title artifact

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()