import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set seed for reproducibility matching same synthetic data
np.random.seed(42)

n_records = 300
patient_ids = [f"P-{1000 + i}" for i in range(n_records)]
departments = ['Cardiology', 'Orthopedics', 'Neurology', 'Pediatrics', 'General Medicine', 'Oncology']
dept_probs = [0.20, 0.22, 0.15, 0.15, 0.18, 0.10]

dept_choice = np.random.choice(departments, size=n_records, p=dept_probs)

ages = []
for d in dept_choice:
    if d == 'Pediatrics':
        ages.append(np.random.randint(1, 18))
    elif d in ['Cardiology', 'Oncology']:
        ages.append(np.random.randint(45, 85))
    elif d == 'Neurology':
        ages.append(np.random.randint(30, 80))
    else:
        ages.append(np.random.randint(18, 75))

stay_days = []
for d in dept_choice:
    if d == 'Oncology':
        stay_days.append(np.random.randint(5, 25))
    elif d in ['Cardiology', 'Neurology']:
        stay_days.append(np.random.randint(3, 15))
    elif d == 'Orthopedics':
        stay_days.append(np.random.randint(2, 10))
    else:
        stay_days.append(np.random.randint(1, 8))

bills = []
for i in range(n_records):
    d = dept_choice[i]
    days = stay_days[i]
    
    base_cost = {'Cardiology': 3000, 'Oncology': 4000, 'Neurology': 2500, 
                 'Orthopedics': 2000, 'General Medicine': 1000, 'Pediatrics': 800}[d]
    
    daily_cost = {'Cardiology': 800, 'Oncology': 1000, 'Neurology': 700, 
                  'Orthopedics': 600, 'General Medicine': 400, 'Pediatrics': 350}[d]
    
    bill = base_cost + days * daily_cost + np.random.normal(0, 500)
    bills.append(round(max(bill, 500), 2))

df = pd.DataFrame({
    'PatientID': patient_ids,
    'Department': dept_choice,
    'Age': ages,
    'Bill': bills,
    'StayDays': stay_days
})

dept_colors = {
    'Cardiology': '#1f77b4',
    'Orthopedics': '#ff7f0e',
    'General Medicine': '#2ca02c',
    'Pediatrics': '#d62728',
    'Neurology': '#9467bd',
    'Oncology': '#8c564b'
}

# Chart 1: Department-wise Patients (Matplotlib only)
fig, ax = plt.subplots(figsize=(8, 4.5))
dept_counts = df['Department'].value_counts()
bars = ax.barh(dept_counts.index[::-1], dept_counts.values[::-1], color='#2b5c8f', edgecolor='black', alpha=0.85)
ax.set_title('Chart 1: Department-wise Patient Count', fontsize=12, fontweight='bold')
ax.set_xlabel('Number of Patients')
ax.set_ylabel('Department')
ax.grid(axis='x', linestyle='--', alpha=0.7)
for bar in bars:
    width = bar.get_width()
    ax.text(width + 1, bar.get_y() + bar.get_height()/2, f'{int(width)}', va='center', fontweight='bold')
plt.tight_layout()
plt.savefig('chart1_mpl.png', dpi=300)
plt.close()

# Chart 2: Department-wise Average Bill (Matplotlib only)
fig, ax = plt.subplots(figsize=(8, 4.5))
dept_avg = df.groupby('Department')['Bill'].mean().sort_values(ascending=True)
bars = ax.barh(dept_avg.index, dept_avg.values, color='#2e7d32', edgecolor='black', alpha=0.85)
ax.set_title('Chart 2: Department-wise Average Bill ($)', fontsize=12, fontweight='bold')
ax.set_xlabel('Average Bill ($)')
ax.set_ylabel('Department')
ax.grid(axis='x', linestyle='--', alpha=0.7)
for bar in bars:
    width = bar.get_width()
    ax.text(width + 200, bar.get_y() + bar.get_height()/2, f'${width:,.2f}', va='center', fontweight='bold')
plt.tight_layout()
plt.savefig('chart2_mpl.png', dpi=300)
plt.close()

# Chart 3: Patient Age Distribution (Matplotlib only)
fig, ax = plt.subplots(figsize=(8, 4.5))
ax.hist(df['Age'], bins=20, color='#4682b4', edgecolor='black', alpha=0.7)
ax.set_title('Chart 3: Patient Age Distribution', fontsize=12, fontweight='bold')
ax.set_xlabel('Age (Years)')
ax.set_ylabel('Patient Count')
ax.grid(linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('chart3_mpl.png', dpi=300)
plt.close()

# Chart 4: Age vs Hospital Bill (Matplotlib only)
fig, ax = plt.subplots(figsize=(8, 4.5))
for dept, group in df.groupby('Department'):
    ax.scatter(group['Age'], group['Bill'], label=dept, color=dept_colors[dept], alpha=0.8, edgecolors='none', s=45)
ax.set_title('Chart 4: Age vs. Hospital Bill', fontsize=12, fontweight='bold')
ax.set_xlabel('Age (Years)')
ax.set_ylabel('Hospital Bill ($)')
ax.grid(linestyle='--', alpha=0.7)
ax.legend(title='Department', bbox_to_anchor=(1.02, 1), loc='upper left')
plt.tight_layout()
plt.savefig('chart4_mpl.png', dpi=300)
plt.close()

# Chart 5: Stay Days vs Bill (Matplotlib only)
fig, ax = plt.subplots(figsize=(8, 4.5))
for dept, group in df.groupby('Department'):
    ax.scatter(group['StayDays'], group['Bill'], label=dept, color=dept_colors[dept], alpha=0.8, edgecolors='none', s=45)

# Calculate linear trendline using numpy polyfit
m, b = np.polyfit(df['StayDays'], df['Bill'], 1)
x_vals = np.array([df['StayDays'].min(), df['StayDays'].max()])
ax.plot(x_vals, m*x_vals + b, color='black', linestyle='--', linewidth=1.5, label='Trendline')

ax.set_title('Chart 5: Stay Days vs. Hospital Bill', fontsize=12, fontweight='bold')
ax.set_xlabel('Length of Stay (Days)')
ax.set_ylabel('Hospital Bill ($)')
ax.grid(linestyle='--', alpha=0.7)
ax.legend(title='Department', bbox_to_anchor=(1.02, 1), loc='upper left')
plt.tight_layout()
plt.savefig('chart5_mpl.png', dpi=300)
plt.close()

print("Charts successfully generated using pure Matplotlib.")