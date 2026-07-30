import numpy as np

# Dataset: Patient temperatures in °C
temperatures = np.array([
    36.5,
    37.2,
    38.1,
    39.0,
    36.8,
    37.5,
    38.5,
    36.9
])

# 1. Average temperature
avg_temp = np.mean(temperatures)

# 2. Highest temperature
max_temp = np.max(temperatures)

# 3. Lowest temperature
min_temp = np.min(temperatures)

# 4. Patients with temperature > 38°C (Fever / High)
high_temp_patients = temperatures[temperatures > 38.0]

# 5. Patients with temperature < 37°C
low_temp_patients = temperatures[temperatures < 37.0]

# 6. Normal temperature range (37.0°C <= Temp <= 38.0°C)
normal_mask = (temperatures >= 37.0) & (temperatures <= 38.0)
normal_temp_patients = temperatures[normal_mask]

# 7. Count high-temperature patients (> 38°C)
high_temp_mask = temperatures > 38.0
count_high = np.sum(high_temp_mask)

# 8. Count normal-temperature patients (37°C - 38°C)
count_normal = np.sum(normal_mask)

# 9. Generate a Boolean mask (Flagging patients with fever > 38°C)
fever_boolean_mask = temperatures > 38.0

# 10. Generate a summary report
print("====== HOSPITAL VITAL ANALYSIS ======")
print(f"Total Patients             : {len(temperatures)}")
print(f"Average Temperature        : {avg_temp:.2f}°C")
print(f"Highest Temperature        : {max_temp:.1f}°C")
print(f"Lowest Temperature         : {min_temp:.1f}°C")
print("-------------------------------------")
print(f"High Temp Patients (> 38°C) : {high_temp_patients}")
print(f"Low Temp Patients (< 37°C)  : {low_temp_patients}")
print(f"Normal Temp Range (37-38°C) : {normal_temp_patients}")
print("-------------------------------------")
print(f"High Temperature Count     : {count_high}")
print(f"Normal Temperature Count   : {count_normal}")
print("-------------------------------------")
print(f"Fever Boolean Mask (> 38°C): {fever_boolean_mask}")
print("=====================================")