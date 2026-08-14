import numpy as np
import pandas as pd

# ------------------------------------------------------------------
# 1. Create Sample Hospital Dataset
# ------------------------------------------------------------------
np.random.seed(42)
n_patients = 1000

data = {
    "PatientID": range(1001, 1001 + n_patients),
    "Gender": np.random.choice(["Female", "Male"], size=n_patients, p=[0.52, 0.48]),
    # Disease Status: 1 = Has Disease, 0 = Healthy
    "Disease": np.random.choice([1, 0], size=n_patients, p=[0.20, 0.80]),
}

df = pd.DataFrame(data)

# Inject realistic correlation:
# Example: Females have a 15% prevalence rate, Males have a 25% prevalence rate
for idx in df.index:
    if df.loc[idx, "Gender"] == "Female":
        df.loc[idx, "Disease"] = np.random.choice([1, 0], p=[0.15, 0.85])
    else:
        df.loc[idx, "Disease"] = np.random.choice([1, 0], p=[0.25, 0.75])

# Map 1/0 to readable strings
df["DiseaseStatus"] = df["Disease"].map({1: "Disease Present", 0: "Healthy"})

# ------------------------------------------------------------------
# 2. Conditional Probability Function
# ------------------------------------------------------------------
def prob_conditional(dataframe, event_cond, given_cond):
    """
    Calculates P(Event | Given) = Count(Event AND Given) / Count(Given)
    """
    given_df = dataframe[given_cond]
    if len(given_df) == 0:
        return 0.0
    return len(dataframe[event_cond & given_cond]) / len(given_df)

# ------------------------------------------------------------------
# 3. Calculate Conditional Probabilities
# ------------------------------------------------------------------

# P(Disease | Female)
p_disease_given_female = prob_conditional(
    df, 
    event_cond=(df["Disease"] == 1), 
    given_cond=(df["Gender"] == "Female")
)

# P(Disease | Male)
p_disease_given_male = prob_conditional(
    df, 
    event_cond=(df["Disease"] == 1), 
    given_cond=(df["Gender"] == "Male")
)

# Overall Baseline Disease Prevalence: P(Disease)
p_overall_disease = len(df[df["Disease"] == 1]) / len(df)

# ------------------------------------------------------------------
# 4. Print Results & Crosstab Table
# ------------------------------------------------------------------
print("==================================================")
print("     PATIENT CONTINGENCY TABLE (Counts)")
print("==================================================")
crosstab = pd.crosstab(df["Gender"], df["DiseaseStatus"], margins=True)
print(crosstab)
print("==================================================\n")

print("==================================================")
print("     CONDITIONAL PROBABILITY RESULTS")
print("==================================================")
print(f"Overall Disease Prevalence P(Disease) : {p_overall_disease:.2%}")
print(f"P(Disease | Female)                   : {p_disease_given_female:.2%}")
print(f"P(Disease | Male)                     : {p_disease_given_male:.2%}")
print("==================================================")