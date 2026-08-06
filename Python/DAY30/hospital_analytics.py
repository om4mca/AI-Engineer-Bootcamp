import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Parameters
n_patients = 100
departments = ['Cardiology', 'Neurology', 'Orthopedics', 'Pediatrics', 'Oncology', 'Emergency']

# Map departments to typical age ranges, stay days, and bill amounts
dept_profiles = {
    'Cardiology': {'age_range': (45, 85), 'stay_range': (2, 10), 'bill_base': 15000, 'bill_scale': 8000},
    'Neurology': {'age_range': (30, 80), 'stay_range': (3, 14), 'bill_base': 18000, 'bill_scale': 10000},
    'Orthopedics': {'age_range': (20, 75), 'stay_range': (1, 7), 'bill_base': 12000, 'bill_scale': 5000},
    'Pediatrics': {'age_range': (1, 17), 'stay_range': (1, 5), 'bill_base': 4000, 'bill_scale': 2000},
    'Oncology': {'age_range': (35, 80), 'stay_range': (4, 20), 'bill_base': 25000, 'bill_scale': 12000},
    'Emergency': {'age_range': (18, 70), 'stay_range': (1, 3), 'bill_base': 3000, 'bill_scale': 2500}
}

doctors = {
    'Cardiology': ['Dr. Smith', 'Dr. Adams'],
    'Neurology': ['Dr. Chen', 'Dr. Patel'],
    'Orthopedics': ['Dr. Miller', 'Dr. Davis'],
    'Pediatrics': ['Dr. Wilson', 'Dr. Taylor'],
    'Oncology': ['Dr. White', 'Dr. Evans'],
    'Emergency': ['Dr. Brown', 'Dr. Jones']
}

data = []
for i in range(1, n_patients + 1):
    pid = f"PAT{i:04d}"
    dept = np.random.choice(departments, p=[0.2, 0.15, 0.2, 0.15, 0.15, 0.15])
    profile = dept_profiles[dept]
    
    age = int(np.random.randint(profile['age_range'][0], profile['age_range'][1] + 1))
    stay = int(np.random.randint(profile['stay_range'][0], profile['stay_range'][1] + 1))
    bill = round(profile['bill_base'] + (stay * 1200) + np.random.exponential(profile['bill_scale']), 2)
    doc = np.random.choice(doctors[dept])
    
    data.append({
        'PatientID': pid,
        'Department': dept,
        'Doctor': doc,
        'Age': age,
        'Bill': bill,
        'StayDays': stay
    })

df = pd.DataFrame(data)

# Aggregation
dept_summary = df.groupby('Department').agg(
    Patients=('PatientID', 'count'),
    Average_Bill=('Bill', 'mean'),
    Maximum_Bill=('Bill', 'max'),
    Minimum_Bill=('Bill', 'min'),
    Average_Stay=('StayDays', 'mean'),
    Average_Age=('Age', 'mean')
).reset_index()

overall_summary = pd.DataFrame([{
    'Department': 'Overall Total / Avg',
    'Patients': len(df),
    'Average_Bill': df['Bill'].mean(),
    'Maximum_Bill': df['Bill'].max(),
    'Minimum_Bill': df['Bill'].min(),
    'Average_Stay': df['StayDays'].mean(),
    'Average_Age': df['Age'].mean()
}])

print("Department Breakdown:")
print(dept_summary)
print("\n====== HOSPITAL ANALYTICS ======")
print(overall_summary)