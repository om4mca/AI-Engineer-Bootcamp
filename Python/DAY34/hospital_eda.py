import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# -------------------------------------------------------------
# 1. Create Synthetic Hospital Dataset
# -------------------------------------------------------------
np.random.seed(42)
n_patients = 250

departments = ['Cardiology', 'Orthopedics', 'Neurology', 'Pediatrics', 'Oncology']
genders = ['Male', 'Female']

df = pd.DataFrame({
    'PatientID': [f'P-{1000 + i}' for i in range(n_patients)],
    'Department': np.random.choice(departments, size=n_patients, p=[0.25, 0.25, 0.20, 0.15, 0.15]),
    'Age': np.random.randint(1, 85, size=n_patients),
    'Gender': np.random.choice(genders, size=n_patients),
    'StayDays': np.random.geometric(p=0.15, size=n_patients).clip(1, 30),
})

# Bill amount is generally correlated with StayDays and Department
base_cost = df['StayDays'] * np.random.uniform(2000, 5000, size=n_patients)
df['Bill'] = (base_cost + np.random.normal(5000, 2000, size=n_patients)).round(2).clip(min=1000)

# -------------------------------------------------------------
# 2. Data Inspection & Summaries
# -------------------------------------------------------------
print("--- 1. First 5 Rows (head) ---")
print(df.head())

print("\n--- 2. Dataset Shape ---")
print("Shape (Rows, Columns):", df.shape)

print("\n--- 3. Data Info ---")
df.info()

print("\n--- 4. Numerical Summary (describe) ---")
print(df.describe())

# -------------------------------------------------------------
# 3. Data Cleaning Checks
# -------------------------------------------------------------
print("\n--- 5. Missing Values Check ---")
print(df.isnull().sum())

print("\n--- 6. Duplicate Rows Check ---")
print("Duplicate Rows Count:", df.duplicated().sum())

print("\n--- 7. Department Patient Count ---")
print(df["Department"].value_counts())

# -------------------------------------------------------------
# 4. Multi-Plot EDA Visualizations
# -------------------------------------------------------------
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(14, 14))
fig.suptitle('Hospital Exploratory Data Analysis (EDA)', fontsize=18, fontweight='bold', y=0.98)

# --- Plot 1: Department -> Patient Count (Bar Chart) ---
dept_counts = df['Department'].value_counts()
bars1 = axes[0, 0].bar(dept_counts.index, dept_counts.values, color='#3498db', edgecolor='#1d6fa5', width=0.55)
axes[0, 0].set_title('1. Department vs Patient Count', fontweight='bold')
axes[0, 0].set_ylabel('Number of Patients')
axes[0, 0].grid(axis='y', linestyle='--', alpha=0.5)

# Add counts on top of bars
for bar in bars1:
    yval = bar.get_height()
    axes[0, 0].text(bar.get_x() + bar.get_width()/2, yval + 1, f'{int(yval)}', ha='center', va='bottom', fontweight='bold')

# --- Plot 2: Age -> Distribution (Histogram) ---
axes[0, 1].hist(df['Age'], bins=12, color='#2ecc71', edgecolor='#1e8449', alpha=0.85)
axes[0, 1].set_title('2. Age Distribution of Patients', fontweight='bold')
axes[0, 1].set_xlabel('Age (Years)')
axes[0, 1].set_ylabel('Frequency')
axes[0, 1].grid(axis='y', linestyle='--', alpha=0.5)

# --- Plot 3: Bill -> Distribution (Histogram) ---
axes[1, 0].hist(df['Bill'], bins=15, color='#9b59b6', edgecolor='#4a235a', alpha=0.85)
axes[1, 0].set_title('3. Medical Bill Amount Distribution', fontweight='bold')
axes[1, 0].set_xlabel('Bill Amount ($)')
axes[1, 0].set_ylabel('Frequency')
axes[1, 0].xaxis.set_major_formatter('${x:,.0f}')
axes[1, 0].grid(axis='y', linestyle='--', alpha=0.5)

# --- Plot 4: Age vs Bill (Scatter Plot) ---
axes[1, 1].scatter(df['Age'], df['Bill'], color='#e67e22', edgecolor='#d35400', alpha=0.7, s=50)
axes[1, 1].set_title('4. Relationship: Age vs Bill', fontweight='bold')
axes[1, 1].set_xlabel('Age (Years)')
axes[1, 1].set_ylabel('Bill Amount ($)')
axes[1, 1].yaxis.set_major_formatter('${x:,.0f}')
axes[1, 1].grid(True, linestyle='--', alpha=0.5)

# --- Plot 5: StayDays vs Bill (Scatter Plot with Trendline) ---
axes[2, 0].scatter(df['StayDays'], df['Bill'], color='#e74c3c', edgecolor='#922b21', alpha=0.7, s=50)
z = np.polyfit(df['StayDays'], df['Bill'], 1)
p = np.poly1d(z)
axes[2, 0].plot(df['StayDays'], p(df['StayDays']), color='#2c3e50', linestyle='--', linewidth=2, label='Trendline')
axes[2, 0].set_title('5. Relationship: Stay Days vs Bill', fontweight='bold')
axes[2, 0].set_xlabel('Stay Duration (Days)')
axes[2, 0].set_ylabel('Bill Amount ($)')
axes[2, 0].yaxis.set_major_formatter('${x:,.0f}')
axes[2, 0].grid(True, linestyle='--', alpha=0.5)
axes[2, 0].legend()

# --- Plot 6: Average Bill by Department (Additional Insight Box Plot) ---
df.boxplot(column='Bill', by='Department', ax=axes[2, 1], patch_artist=True, grid=False)
axes[2, 1].set_title('6. Bill Distribution Across Departments', fontweight='bold')
axes[2, 1].set_xlabel('Department')
axes[2, 1].set_ylabel('Bill ($)')
axes[2, 1].yaxis.set_major_formatter('${x:,.0f}')
axes[2, 1].tick_params(axis='x', rotation=15)
plt.suptitle('') # Remove pandas auto-generated boxplot title

# -------------------------------------------------------------
# 5. Layout Adjustments & Display
# -------------------------------------------------------------
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()