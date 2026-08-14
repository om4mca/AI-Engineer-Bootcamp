import numpy as np
import pandas as pd

# ------------------------------------------------------------------
# 1. Create Sample Student Dataset
# ------------------------------------------------------------------
np.random.seed(42)
n_students = 500

data = {
    "StudentID": range(1001, 1001 + n_students),
    "Gender": np.random.choice(["Female", "Male"], size=n_students, p=[0.52, 0.48]),
    "Status": np.random.choice(["Pass", "Fail"], size=n_students, p=[0.75, 0.25]),
}

df = pd.DataFrame(data)

# Inject realistic correlation:
# Let's say Female students have an 80% pass rate and Male students have a 70% pass rate
for idx in df.index:
    if df.loc[idx, "Gender"] == "Female":
        df.loc[idx, "Status"] = np.random.choice(["Pass", "Fail"], p=[0.80, 0.20])
    else:
        df.loc[idx, "Status"] = np.random.choice(["Pass", "Fail"], p=[0.70, 0.30])

# ------------------------------------------------------------------
# 2. Probability Function
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

# P(Pass | Female)
p_pass_given_female = prob_conditional(
    df, 
    event_cond=(df["Status"] == "Pass"), 
    given_cond=(df["Gender"] == "Female")
)

# P(Pass | Male)
p_pass_given_male = prob_conditional(
    df, 
    event_cond=(df["Status"] == "Pass"), 
    given_cond=(df["Gender"] == "Male")
)

# Overall Baseline Pass Rate: P(Pass)
p_overall_pass = len(df[df["Status"] == "Pass"]) / len(df)

# ------------------------------------------------------------------
# 4. Results & Contingency Table
# ------------------------------------------------------------------
print("==========================================")
print("     CONTINGENCY TABLE (Counts)")
print("==========================================")
contingency_table = pd.crosstab(df["Gender"], df["Status"], margins=True)
print(contingency_table)
print("==========================================\n")

print("==========================================")
print("     CONDITIONAL PROBABILITY RESULTS")
print("==========================================")
print(f"Overall Pass Rate P(Pass)    : {p_overall_pass:.2%}")
print(f"P(Pass | Female)             : {p_pass_given_female:.2%}")
print(f"P(Pass | Male)               : {p_pass_given_male:.2%}")
print("==========================================")