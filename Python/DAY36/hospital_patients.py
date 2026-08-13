import numpy as np
import pandas as pd

# 1. Generate Synthetic Hospital Dataset (N = 1,000 patients)
np.random.seed(42)  # For reproducible results

n_patients = 1000

departments = ['Cardiology', 'Emergency', 'Pediatrics', 'Orthopedics', 'Neurology']
dept_probs = [0.30, 0.25, 0.15, 0.15, 0.15]  # Cardiology is the primary department

data = {
    'PatientID': range(5001, 5001 + n_patients),
    'Department': np.random.choice(departments, size=n_patients, p=dept_probs),
    'Age': np.random.randint(1, 90, size=n_patients),
    'Bill': np.random.normal(loc=45000, scale=20000, size=n_patients).round(-2),
    'StayDays': np.random.poisson(lam=4, size=n_patients) + 1  # Stay duration between 1 to 15+ days
}

df = pd.DataFrame(data)

# Ensure bill amounts stay non-negative
df['Bill'] = df['Bill'].clip(lower=2000)

# 2. Probability Calculation Function
total_patients = len(df)

def get_probability(condition):
    count = condition.sum()
    prob = count / total_patients
    pct = prob * 100
    return count, prob, pct

# 3. Compute Requested Probabilities
cnt_cardio, p_cardio, pct_cardio = get_probability(df['Department'] == 'Cardiology')
cnt_age60, p_age60, pct_age60 = get_probability(df['Age'] > 60)
cnt_bill50k, p_bill50k, pct_bill50k = get_probability(df['Bill'] > 50000)
cnt_stay5, p_stay5, pct_stay5 = get_probability(df['StayDays'] > 5)

# Joint Probability: P(Age > 60 AND Bill > 50000)
cnt_joint, p_joint, pct_joint = get_probability((df['Age'] > 60) & (df['Bill'] > 50000))

# Conditional Probability for Insights: P(Bill > 50k | Age > 60)
p_bill_given_senior = (cnt_joint / cnt_age60) * 100 if cnt_age60 > 0 else 0

# 4. Display Statistical Results
print("=" * 65)
print("          🏥 HOSPITAL PATIENT PROBABILITY REPORT          ")
print("=" * 65)
print(f"Total Patients Analyzed (N) : {total_patients}\n")

print(f"P(Cardiology Patient)            : {p_cardio:.4f}  |  {pct_cardio:.1f}%")
print(f"P(Age > 60)                      : {p_age60:.4f}  |  {pct_age60:.1f}%")
print(f"P(Bill > 50,000)                 : {p_bill50k:.4f}  |  {pct_bill50k:.1f}%")
print(f"P(StayDays > 5)                  : {p_stay5:.4f}  |  {pct_stay5:.1f}%")
print(f"P(Age > 60 AND Bill > 50,000)    : {p_joint:.4f}  |  {pct_joint:.1f}%")
print("=" * 65)

# 5. Output 5 Meaningful Probability Insights
print("\n" + "=" * 65)
print("                 💡 5 MEANINGFUL PROBABILITY INSIGHTS")
print("=" * 65)

print(f"1. Probability of selecting a Cardiology patient = {pct_cardio:.1f}%")
print(f"   -> Cardiology represents the largest single specialty ward, accounting for nearly 1 in 3 hospital admissions.")

print(f"\n2. Probability of selecting a Senior Patient (Age > 60) = {pct_age60:.1f}%")
print(f"   -> Roughly 1 in 3 patients are senior citizens, highlighting high demand for geriatric and specialized elderly care.")

print(f"\n3. Probability of selecting a High-Value Bill (> $50,000) = {pct_bill50k:.1f}%")
print(f"   -> Over 40% of overall hospital admissions exceed the $50,000 billing threshold.")

print(f"\n4. Probability of selecting a Long Stay Patient (StayDays > 5) = {pct_stay5:.1f}%")
print(f"   -> Approximately {pct_stay5:.1f}% of admitted patients require extended hospital bed retention exceeding 5 days.")

print(f"\n5. Joint Probability P(Age > 60 AND Bill > $50,000) = {pct_joint:.1f}%")
print(f"   -> {pct_joint:.1f}% of all hospital patients are high-cost seniors. Among senior patients specifically, {p_bill_given_senior:.1f}% incur bills exceeding $50,000.")

print("=" * 65)