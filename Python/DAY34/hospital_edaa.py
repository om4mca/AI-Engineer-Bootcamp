import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# -------------------------------------------------------------
# 0. Create Synthetic Dataset
# -------------------------------------------------------------
np.random.seed(42)
n = 300

departments = ['Cardiology', 'Orthopedics', 'Neurology', 'Pediatrics', 'Oncology']

df = pd.DataFrame({
    'PatientID': [f'PAT-{1000 + i}' for i in range(n)],
    'Department': np.random.choice(departments, size=n, p=[0.25, 0.25, 0.20, 0.15, 0.15]),
    'Age': np.random.randint(1, 85, size=n),
    'StayDays': np.random.geometric(p=0.15, size=n).clip(1, 30)
})

# Calculate realistic hospital bills based on StayDays and Department complexity
base_bill = df['StayDays'] * np.random.uniform(2500, 5500, size=n)
dept_multiplier = df['Department'].map({
    'Cardiology': 1.4, 'Oncology': 1.5, 'Neurology': 1.3, 'Orthopedics': 1.1, 'Pediatrics': 0.9
})
df['Bill'] = (base_bill * dept_multiplier + np.random.normal(3000, 1000, size=n)).round(2).clip(min=1200)

# -------------------------------------------------------------
# 1. Summary Metrics & KPI Calculation
# -------------------------------------------------------------
total_patients = df['PatientID'].nunique()
avg_age = df['Age'].mean()
avg_bill = df['Bill'].mean()
max_bill = df['Bill'].max()
min_bill = df['Bill'].min()

print("="*50)
print("🏥 HOSPITAL EDA SUMMARY METRICS")
print("="*50)
print(f"Total Patients       : {total_patients}")
print(f"Average Age          : {avg_age:.1f} years")
print(f"Average Bill         : ${avg_bill:,.2f}")
print(f"Maximum Bill         : ${max_bill:,.2f}")
print(f"Minimum Bill         : ${min_bill:,.2f}")
print("="*50)

print("\n--- Department Distribution ---")
print(df['Department'].value_counts())

# -------------------------------------------------------------
# 2. Exploratory Data Visualizations
# -------------------------------------------------------------
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(14, 15))
fig.suptitle('Hospital Exploratory Data Analysis (EDA) System', fontsize=18, fontweight='bold', y=0.98)

# 1. Department Distribution (Bar Chart)
dept_counts = df['Department'].value_counts()
bars1 = axes[0, 0].bar(dept_counts.index, dept_counts.values, color='#3498db', edgecolor='#1d6fa5', width=0.55)
axes[0, 0].set_title('1. Department Patient Distribution', fontweight='bold')
axes[0, 0].set_ylabel('Number of Patients')
axes[0, 0].grid(axis='y', linestyle='--', alpha=0.5)

for bar in bars1:
    yval = bar.get_height()
    axes[0, 0].text(bar.get_x() + bar.get_width()/2, yval + 1, f'{int(yval)}', ha='center', va='bottom', fontweight='bold')

# 2. Age Distribution (Histogram)
axes[0, 1].hist(df['Age'], bins=12, color='#2ecc71', edgecolor='#1e8449', alpha=0.85)
axes[0, 1].set_title('2. Patient Age Distribution', fontweight='bold')
axes[0, 1].set_xlabel('Age (Years)')
axes[0, 1].set_ylabel('Frequency')
axes[0, 1].grid(axis='y', linestyle='--', alpha=0.5)

# 3. Bill Distribution (Histogram)
axes[1, 0].hist(df['Bill'], bins=15, color='#9b59b6', edgecolor='#4a235a', alpha=0.85)
axes[1, 0].set_title('3. Bill Amount Distribution', fontweight='bold')
axes[1, 0].set_xlabel('Bill ($)')
axes[1, 0].set_ylabel('Frequency')
axes[1, 0].xaxis.set_major_formatter('${x:,.0f}')
axes[1, 0].grid(axis='y', linestyle='--', alpha=0.5)

# 4. Stay Duration Distribution (Histogram)
axes[1, 1].hist(df['StayDays'], bins=10, color='#f1c40f', edgecolor='#b7950b', alpha=0.85)
axes[1, 1].set_title('4. Stay Duration Distribution', fontweight='bold')
axes[1, 1].set_xlabel('Stay Duration (Days)')
axes[1, 1].set_ylabel('Frequency')
axes[1, 1].grid(axis='y', linestyle='--', alpha=0.5)

# 5. Age vs Bill Relationship (Scatter Plot)
axes[2, 0].scatter(df['Age'], df['Bill'], color='#e67e22', edgecolor='#d35400', alpha=0.7, s=50)
axes[2, 0].set_title('5. Relationship: Age vs. Bill', fontweight='bold')
axes[2, 0].set_xlabel('Age (Years)')
axes[2, 0].set_ylabel('Bill ($)')
axes[2, 0].yaxis.set_major_formatter('${x:,.0f}')
axes[2, 0].grid(True, linestyle='--', alpha=0.5)

# 6. StayDays vs Bill Relationship (Scatter Plot with Trendline)
axes[2, 1].scatter(df['StayDays'], df['Bill'], color='#e74c3c', edgecolor='#922b21', alpha=0.7, s=50)
z = np.polyfit(df['StayDays'], df['Bill'], 1)
p = np.poly1d(z)
axes[2, 1].plot(df['StayDays'], p(df['StayDays']), color='#2c3e50', linestyle='--', linewidth=2, label='Trendline')
axes[2, 1].set_title('6. Relationship: Stay Days vs. Bill', fontweight='bold')
axes[2, 1].set_xlabel('Stay Duration (Days)')
axes[2, 1].set_ylabel('Bill ($)')
axes[2, 1].yaxis.set_major_formatter('${x:,.0f}')
axes[2, 1].grid(True, linestyle='--', alpha=0.5)
axes[2, 1].legend()

# Display Visualizations
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()