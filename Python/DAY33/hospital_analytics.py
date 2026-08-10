import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set seed for reproducible synthetic dataset
np.random.seed(42)

# 1. Generate Synthetic Dataset
n_patients = 150
departments = ['Cardiology', 'Orthopedics', 'General', 'Pediatrics', 'Neurology', 'Oncology']

df = pd.DataFrame({
    'PatientID': [f'PAT{1000 + i}' for i in range(n_patients)],
    'Department': np.random.choice(departments, size=n_patients, p=[0.25, 0.2, 0.25, 0.1, 0.1, 0.1]),
    'Age': np.random.randint(1, 85, size=n_patients),
    'StayDays': np.random.geometric(p=0.15, size=n_patients) # Right-skewed stay length
})

# Bill estimation base (Stay duration + Dept multiplier + noise)
dept_bill_base = {
    'Cardiology': 8500, 'Orthopedics': 6500, 'General': 3000, 
    'Pediatrics': 2500, 'Neurology': 9000, 'Oncology': 11000
}

df['Bill'] = df.apply(
    lambda row: dept_bill_base[row['Department']] + (row['StayDays'] * 1200) + np.random.normal(0, 1500), 
    axis=1
).clip(lower=1000).round(-1)

# 2. Setup Figure Layout Grid (4 rows x 2 columns - 7 plots total)
fig = plt.figure(figsize=(15, 20))
fig.suptitle('Hospital Analytics & Operational Dashboard', fontsize=18, fontweight='bold', y=0.98)


# -------------------------------------------------------------
# Chart 1: Department-wise Patients
# -------------------------------------------------------------
ax1 = plt.subplot(4, 2, 1)
dept_counts = df['Department'].value_counts()
bars1 = ax1.bar(dept_counts.index, dept_counts.values, color='#008080', edgecolor='#004d4d', width=0.55)
ax1.set_title('1. Department-wise Patient Count', fontsize=12, fontweight='bold')
ax1.set_ylabel('Number of Patients')
ax1.tick_params(axis='x', rotation=15)
ax1.grid(axis='y', linestyle='--', alpha=0.5)

for bar in bars1:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 0.5, f'{int(yval)}', ha='center', va='bottom', fontweight='bold')


# -------------------------------------------------------------
# Chart 2: Department-wise Average Bill
# -------------------------------------------------------------
ax2 = plt.subplot(4, 2, 2)
avg_bill = df.groupby('Department')['Bill'].mean().sort_values(ascending=False)
bars2 = ax2.bar(avg_bill.index, avg_bill.values, color='#27ae60', edgecolor='#1e8449', width=0.55)
ax2.set_title('2. Department-wise Average Bill', fontsize=12, fontweight='bold')
ax2.set_ylabel('Average Bill ($)')
ax2.yaxis.set_major_formatter('${x:,.0f}')
ax2.tick_params(axis='x', rotation=15)
ax2.grid(axis='y', linestyle='--', alpha=0.5)

for bar in bars2:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval + 300, f'${yval:,.0f}', ha='center', va='bottom', fontweight='bold', fontsize=9)


# -------------------------------------------------------------
# Chart 3: Age Distribution
# -------------------------------------------------------------
ax3 = plt.subplot(4, 2, 3)
counts, bins, _ = ax3.hist(df['Age'], bins=8, color='#8e44ad', edgecolor='#4a235a', alpha=0.85)
ax3.set_title('3. Age Distribution', fontsize=12, fontweight='bold')
ax3.set_xlabel('Age (Years)')
ax3.set_ylabel('Patient Count')
ax3.grid(axis='y', linestyle='--', alpha=0.5)

for count, bin_left, bin_right in zip(counts, bins[:-1], bins[1:]):
    if count > 0:
        ax3.text((bin_left + bin_right)/2, count + 0.3, f'{int(count)}', ha='center', va='bottom', fontweight='bold')


# -------------------------------------------------------------
# Chart 4: Bill Distribution
# -------------------------------------------------------------
ax4 = plt.subplot(4, 2, 4)
counts, bins, _ = ax4.hist(df['Bill'], bins=10, color='#2980b9', edgecolor='#1b4f72', alpha=0.85)
ax4.set_title('4. Total Bill Distribution', fontsize=12, fontweight='bold')
ax4.set_xlabel('Bill Amount ($)')
ax4.set_ylabel('Patient Count')
ax4.xaxis.set_major_formatter('${x:,.0f}')
ax4.grid(axis='y', linestyle='--', alpha=0.5)

for count, bin_left, bin_right in zip(counts, bins[:-1], bins[1:]):
    if count > 0:
        ax4.text((bin_left + bin_right)/2, count + 0.3, f'{int(count)}', ha='center', va='bottom', fontweight='bold')


# -------------------------------------------------------------
# Chart 5: Stay Days Distribution
# -------------------------------------------------------------
ax5 = plt.subplot(4, 2, 5)
counts, bins, _ = ax5.hist(df['StayDays'], bins=10, color='#e67e22', edgecolor='#a04000', alpha=0.85)
ax5.set_title('5. Stay Days Distribution', fontsize=12, fontweight='bold')
ax5.set_xlabel('Length of Stay (Days)')
ax5.set_ylabel('Patient Count')
ax5.grid(axis='y', linestyle='--', alpha=0.5)

for count, bin_left, bin_right in zip(counts, bins[:-1], bins[1:]):
    if count > 0:
        ax5.text((bin_left + bin_right)/2, count + 0.3, f'{int(count)}', ha='center', va='bottom', fontweight='bold')


# -------------------------------------------------------------
# Chart 6: Age vs Bill
# -------------------------------------------------------------
ax6 = plt.subplot(4, 2, 6)
ax6.scatter(df['Age'], df['Bill'], color='#c0392b', edgecolor='#7b241c', alpha=0.7, s=45)
z6 = np.polyfit(df['Age'], df['Bill'], 1)
p6 = np.poly1d(z6)
ax6.plot(df['Age'], p6(df['Age']), color='#2c3e50', linestyle='--', linewidth=2, label='Trendline')
ax6.set_title('6. Age vs. Bill Amount', fontsize=12, fontweight='bold')
ax6.set_xlabel('Age (Years)')
ax6.set_ylabel('Total Bill ($)')
ax6.yaxis.set_major_formatter('${x:,.0f}')
ax6.grid(True, linestyle='--', alpha=0.5)
ax6.legend()


# -------------------------------------------------------------
# Chart 7: Stay Days vs Bill
# -------------------------------------------------------------
ax7 = plt.subplot(4, 2, 7)
ax7.scatter(df['StayDays'], df['Bill'], color='#16a085', edgecolor='#0e6251', alpha=0.75, s=45)
z7 = np.polyfit(df['StayDays'], df['Bill'], 1)
p7 = np.poly1d(z7)
ax7.plot(df['StayDays'], p7(df['StayDays']), color='#d35400', linestyle='--', linewidth=2, label='Trendline')
ax7.set_title('7. Stay Days vs. Bill Amount', fontsize=12, fontweight='bold')
ax7.set_xlabel('Stay Duration (Days)')
ax7.set_ylabel('Total Bill ($)')
ax7.yaxis.set_major_formatter('${x:,.0f}')
ax7.grid(True, linestyle='--', alpha=0.5)
ax7.legend()

# Clean layout and display
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()