import numpy as np
import pandas as pd

# Set seed for reproducibility
np.random.seed(42)
N = 100_000  # 100,000 patients/subjects

# ------------------------------------------------------------------
# Step 1: Simulate Baseline Demographic Variable (Age Group)
# ------------------------------------------------------------------
# 0: Young (<30), 1: Middle-Aged (30-60), 2: Senior (>60)
age_group = np.random.choice([0, 1, 2], size=N, p=[0.30, 0.45, 0.25])

# ------------------------------------------------------------------
# Step 2: Conditional Disease Probability based on Age
# P(Disease | Young) = 2%
# P(Disease | Middle) = 10%
# P(Disease | Senior) = 30%
# ------------------------------------------------------------------
disease_probs = np.select(
    condlist=[age_group == 0, age_group == 1, age_group == 2],
    choicelist=[0.02, 0.10, 0.30]
)

# Draw uniform random numbers [0, 1) and compare against conditional probabilities
has_disease = (np.random.rand(N) < disease_probs).astype(int)

# ------------------------------------------------------------------
# Step 3: Conditional Medical Test Result based on Disease Status
# Sensitivity (P(+ | Disease)): 90%
# Specificity (P(- | No Disease)): 95% -> False Positive Rate = 5%
# ------------------------------------------------------------------
test_probs = np.where(has_disease == 1, 0.90, 0.05)
test_positive = (np.random.rand(N) < test_probs).astype(int)

# ------------------------------------------------------------------
# Step 4: Conditional Hospitalization & Cost Allocation
# High risk/cost conditional on having BOTH Disease AND Positive Test
# ------------------------------------------------------------------
# Log-normal distribution for base hospital bill
base_bill = np.random.lognormal(mean=7.5, sigma=0.5, size=N) 

# Multiplier: 3x bill if severe (Disease + Test Positive), otherwise 1x
bill_multiplier = np.where((has_disease == 1) & (test_positive == 1), 3.0, 1.0)
final_bill = np.round(base_bill * bill_multiplier, 2)

# Build DataFrame for verification
df = pd.DataFrame({
    "AgeGroup": np.vectorize({0: "<30", 1: "30-60", 2: ">60"}.get)(age_group),
    "HasDisease": has_disease,
    "TestPositive": test_positive,
    "HospitalBill": final_bill
})

# Display summary statistics
print("==================================================")
print("       NUMPY CONDITIONAL SIMULATION SUMMARY       ")
print("==================================================")
print(f"Simulated Population Size : {N:,}")
print("\n• Disease Rate by Age Group:")
print(df.groupby("AgeGroup")["HasDisease"].mean().map("{:.2%}".format))

print("\n• Test Positives Breakdown:")
print(f"  - True Positives  : {len(df[(df.HasDisease==1) & (df.TestPositive==1)]):,}")
print(f"  - False Positives : {len(df[(df.HasDisease==0) & (df.TestPositive==1)]):,}")

print("\n• Empirical Posterior P(Disease | Test Positive):")
p_posterior = df[df.TestPositive == 1]["HasDisease"].mean()
print(f"  - Calculated: {p_posterior:.2%}")