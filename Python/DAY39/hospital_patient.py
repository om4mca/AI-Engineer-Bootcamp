import math
import random

# Set random seed for exact reproducibility
random.seed(42)

# ==============================================================================
# 1. DATASET GENERATION
# ==============================================================================
departments = ["Cardiology", "Orthopedics", "Pediatrics", "Neurology", "General"]
genders = ["Male", "Female"]

N = 200
# Generating synthetic patient ages centered around 52 years with sigma = 18 years
mean_age_target = 52
std_age_target = 18

dataset = []
for p_id in range(5001, 5001 + N):
    # Truncate age between 1 and 95
    age = int(max(1, min(95, random.gauss(mean_age_target, std_age_target))))
    gender = random.choice(genders)
    dept = random.choice(departments)
    stay_days = random.randint(1, 14)
    # Bill correlated with stay days and department complexity
    bill = round(stay_days * random.uniform(800, 1500) + random.uniform(500, 2000), 2)

    dataset.append(
        {
            "PatientID": p_id,
            "Age": age,
            "Gender": gender,
            "Department": dept,
            "Bill": bill,
            "StayDays": stay_days,
        }
    )

ages = [p["Age"] for p in dataset]

# ==============================================================================
# 2. STATISTICAL ANALYSIS
# ==============================================================================
# Mean Age
mean_age = sum(ages) / N

# Median Age
sorted_ages = sorted(ages)
mid = N // 2
if N % 2 == 0:
    median_age = (sorted_ages[mid - 1] + sorted_ages[mid]) / 2.0
else:
    median_age = sorted_ages[mid]

# Standard Deviation
variance = sum((x - mean_age) ** 2 for x in ages) / N
std_dev = math.sqrt(variance)

# Compute Z-Scores and tag patients
for patient in dataset:
    z_score = (patient["Age"] - mean_age) / std_dev
    patient["Z_Score"] = round(z_score, 2)

# Identify Outliers
above_2sig = [p for p in dataset if p["Z_Score"] > 2.0]
below_neg2sig = [p for p in dataset if p["Z_Score"] < -2.0]

# Sorting outliers by absolute Z-score descending
above_2sig = sorted(above_2sig, key=lambda x: x["Z_Score"], reverse=True)
below_neg2sig = sorted(below_neg2sig, key=lambda x: x["Z_Score"])

# ==============================================================================
# 3. OUTPUT RESULTS
# ==============================================================================
print("==================================================================")
print("             HOSPITAL PATIENT AGE DISTRIBUTION ANALYSIS           ")
print("==================================================================")
print(f"Total Sample Size (N)       : {N} Patients")
print(f"Mean Age                    : {mean_age:.2f} years")
print(f"Median Age                  : {median_age:.2f} years")
print(f"Standard Deviation (Sigma)  : {std_dev:.2f} years")
print(
    f"Age Distribution Shape      : Mean ≈ Median (Difference: {abs(mean_age - median_age):.2f}) -> Symmetric / Bell-Shaped\n"
)

print("------------------------------------------------------------------")
print("                     EMPIRICAL RULE & Z-SCORES                    ")
print("------------------------------------------------------------------")
print(f"Upper Threshold (+2σ)       : Age > {mean_age + 2*std_dev:.2f} years")
print(f"Lower Threshold (-2σ)       : Age < {mean_age - 2*std_dev:.2f} years")
print(f"Patients Above +2σ          : {len(above_2sig)} ({len(above_2sig)/N:.1%})")
print(f"Patients Below -2σ          : {len(below_neg2sig)} ({len(below_neg2sig)/N:.1%})\n")

print("==================================================================")
print("           PATIENTS WITH UNUSUALLY HIGH AGES (> +2σ)              ")
print("==================================================================")
print(f"{'PatientID':<10} | {'Age':<5} | {'Gender':<8} | {'Department':<12} | {'Z-Score':<8}")
print("-" * 55)
for p in above_2sig:
    print(f"{p['PatientID']:<10} | {p['Age']:<5} | {p['Gender']:<8} | {p['Department']:<12} | {p['Z_Score']:<+8.2f}")

print("\n==================================================================")
print("           PATIENTS WITH UNUSUALLY LOW AGES (< -2σ)               ")
print("==================================================================")
print(f"{'PatientID':<10} | {'Age':<5} | {'Gender':<8} | {'Department':<12} | {'Z-Score':<8}")
print("-" * 55)
for p in below_neg2sig:
    print(f"{p['PatientID']:<10} | {p['Age']:<5} | {p['Gender']:<8} | {p['Department']:<12} | {p['Z_Score']:<+8.2f}")