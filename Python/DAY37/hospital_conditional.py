import numpy as np
import pandas as pd

# ------------------------------------------------------------------
# 1. Generate Synthetic Hospital Dataset
# ------------------------------------------------------------------
np.random.seed(42)
n_patients = 1000

data = {
    "PatientID": range(1001, 1001 + n_patients),
    "Department": np.random.choice(
        ["Cardiology", "Neurology", "Orthopedics", "General"], size=n_patients
    ),
    "Age": np.random.randint(18, 85, size=n_patients),
    "Gender": np.random.choice(["Male", "Female"], size=n_patients, p=[0.48, 0.52]),
    "Disease": np.random.choice([1, 0], size=n_patients, p=[0.15, 0.85]),  # 1 = Present, 0 = Absent
    "TestResult": np.random.choice(["Positive", "Negative"], size=n_patients, p=[0.20, 0.80]),
    "Hospitalization": np.random.choice([1, 0], size=n_patients, p=[0.30, 0.70]),
    "Bill": np.random.choice(["High", "Medium", "Low"], size=n_patients, p=[0.25, 0.45, 0.30]),
}

df = pd.DataFrame(data)

# Inject realistic correlation for test results (Sensitivity & Specificity)
# If Disease == 1, 85% chance of Positive test (Sensitivity)
# If Disease == 0, 90% chance of Negative test (Specificity -> 10% False Positive)
for idx in df.index:
    if df.loc[idx, "Disease"] == 1:
        df.loc[idx, "TestResult"] = np.random.choice(["Positive", "Negative"], p=[0.85, 0.15])
    else:
        df.loc[idx, "TestResult"] = np.random.choice(["Positive", "Negative"], p=[0.10, 0.90])

# ------------------------------------------------------------------
# 2. Probability Function
# ------------------------------------------------------------------
def prob(dataframe, event_cond, given_cond=None):
    """Calculates P(Event) or P(Event | Given)"""
    if given_cond is None:
        return len(dataframe[event_cond]) / len(dataframe)
    
    given_df = dataframe[given_cond]
    if len(given_df) == 0:
        return 0.0
    return len(dataframe[event_cond & given_cond]) / len(given_df)

# ------------------------------------------------------------------
# 3. Calculate Requested Conditional Probabilities
# ------------------------------------------------------------------

# P(Disease | Positive Test) - Positive Predictive Value (PPV)
p_disease_given_pos = prob(df, df["Disease"] == 1, df["TestResult"] == "Positive")

# P(Positive Test | Disease) - Sensitivity
p_pos_given_disease = prob(df, df["TestResult"] == "Positive", df["Disease"] == 1)

# P(Disease | Age > 60)
p_disease_given_age60 = prob(df, df["Disease"] == 1, df["Age"] > 60)

# P(High Bill | Hospitalization)
p_highbill_given_hosp = prob(df, df["Bill"] == "High", df["Hospitalization"] == 1)

# P(Disease | Male)
p_disease_given_male = prob(df, df["Disease"] == 1, df["Gender"] == "Male")

# Output Conditional Probabilities
print("==================================================")
print("   HOSPITAL CONDITIONAL PROBABILITY RESULTS")
print("==================================================")
print(f"1. P(Disease | Positive Test)      : {p_disease_given_pos:.2%}")
print(f"2. P(Positive Test | Disease)      : {p_pos_given_disease:.2%}")
print(f"3. P(Disease | Age > 60)           : {p_disease_given_age60:.2%}")
print(f"4. P(High Bill | Hospitalization)  : {p_highbill_given_hosp:.2%}")
print(f"5. P(Disease | Male)               : {p_disease_given_male:.2%}")
print("==================================================\n")


# ------------------------------------------------------------------
# 4. Bayes Analysis: Medical Test Breakdown
# ------------------------------------------------------------------
# Components for Bayes' Theorem: P(Disease | Positive) = [P(Positive | Disease) * P(Disease)] / P(Positive)

prior = prob(df, df["Disease"] == 1)                             # P(Disease)
sensitivity = p_pos_given_disease                               # P(Positive | Disease)
false_positive_rate = prob(df, df["TestResult"] == "Positive", df["Disease"] == 0) # P(Positive | No Disease)
p_no_disease = 1 - prior                                        # P(No Disease)

# Evidence: Total P(Positive) = P(Pos|Disease)*P(Disease) + P(Pos|No Disease)*P(No Disease)
evidence = (sensitivity * prior) + (false_positive_rate * p_no_disease)

# Posterior Probability
posterior = (sensitivity * prior) / evidence

print("🔎 BAYES ANALYSIS (Medical Test Example)")
print("--------------------------------------------------")
print(f"• Prior P(Disease)                 : {prior:.2%} (Base rate in population)")
print(f"• Likelihood P(Positive | Disease) : {sensitivity:.2%} (Sensitivity of test)")
print(f"• False Positive Rate              : {false_positive_rate:.2%} P(Positive | No Disease)")
print(f"• Evidence P(Positive Test)        : {evidence:.2%} (Total positive test rate)")
print("--------------------------------------------------")
print(f"• Posterior P(Disease | Positive)  : {posterior:.2%}")
print("==================================================\n")

print("💡 BAYESIAN BREAKDOWN EXPLANATION")
print("""
1. PRIOR  [P(Disease)]:
   This is the initial belief or baseline risk of a patient having the disease 
   BEFORE taking any test, based solely on general population data.

2. EVIDENCE [P(Positive Test)]:
   This is the total probability of getting a positive test result across ALL patients.
   It combines two scenarios:
   - True Positives: Patients WITH disease who test positive.
   - False Positives: Healthy patients WITHOUT disease who wrongly test positive.

3. POSTERIOR [P(Disease | Positive Test)]:
   This is the updated probability that a patient ACTUALLY has the disease AFTER 
   receiving a positive test result.

Key Takeaway: Even with high sensitivity, if the Prior (disease prevalence) is low,
a positive test result may still have a surprisingly low Posterior probability due
to false positives in the general population.
""")