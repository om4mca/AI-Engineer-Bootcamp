import numpy as np
import pandas as pd

# ------------------------------------------------------------------
# 1. Create Sample Employee Dataset
# ------------------------------------------------------------------
np.random.seed(42)
n_employees = 200

data = {
    "EmployeeID": range(101, 101 + n_employees),
    "Department": np.random.choice(
        ["IT", "HR", "Sales", "Finance"], size=n_employees, p=[0.35, 0.2, 0.25, 0.2]
    ),
    "Age": np.random.randint(22, 55, size=n_employees),
    "Salary": np.random.choice(["High", "Medium", "Low"], size=n_employees, p=[0.35, 0.4, 0.25]),
    "Experience": np.random.randint(1, 20, size=n_employees),
    "Performance": np.random.choice(["High", "Average", "Low"], size=n_employees, p=[0.4, 0.4, 0.2]),
}

df = pd.DataFrame(data)

# ------------------------------------------------------------------
# 2. Probability Calculation Function
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
# 3. Calculate Conditional Probabilities
# ------------------------------------------------------------------
p_high_sal_given_it = prob(df, df["Salary"] == "High", df["Department"] == "IT")
p_high_perf_given_exp5 = prob(df, df["Performance"] == "High", df["Experience"] > 5)
p_age30_given_it = prob(df, df["Age"] > 30, df["Department"] == "IT")
p_high_sal_given_exp5 = prob(df, df["Salary"] == "High", df["Experience"] > 5)

# Overall baseline probabilities for comparison
p_overall_high_salary = prob(df, df["Salary"] == "High")
p_overall_high_perf = prob(df, df["Performance"] == "High")

# ------------------------------------------------------------------
# 4. Print Calculations & Automated 5 Data Insights
# ------------------------------------------------------------------
print("==========================================")
print("   CONDITIONAL PROBABILITY RESULTS")
print("==========================================")
print(f"1. P(High Salary | IT)                 : {p_high_sal_given_it:.2%}")
print(f"2. P(High Performance | Experience > 5): {p_high_perf_given_exp5:.2%}")
print(f"3. P(Age > 30 | IT)                    : {p_age30_given_it:.2%}")
print(f"4. P(High Salary | High Experience)    : {p_high_sal_given_exp5:.2%}")
print("==========================================\n")

print("💡 5 KEY DATA INSIGHTS")
print("------------------------------------------")

# Insight 1: Experience vs Salary
diff_sal = p_high_sal_given_exp5 - p_overall_high_salary
print(
    f"1. Experience-Driven Compensation:\n"
    f"   Employees with >5 years experience have a {p_high_sal_given_exp5:.1%} chance of "
    f"receiving a High Salary compared to the baseline ({p_overall_high_salary:.1%}). "
    f"This represents a {diff_sal:+.1%} probability shift based on tenure.\n"
)

# Insight 2: Performance Progression
diff_perf = p_high_perf_given_exp5 - p_overall_high_perf
print(
    f"2. High Experience Boosts Performance:\n"
    f"   The probability of High Performance for experienced staff (>5 yrs) is {p_high_perf_given_exp5:.1%}, "
    f"showing a {diff_perf:+.1%} variance from the average employee performance rate ({p_overall_high_perf:.1%}).\n"
)

# Insight 3: IT Department Demographics
young_it_pct = 1 - p_age30_given_it
print(
    f"3. IT Department Demographic Composition:\n"
    f"   {p_age30_given_it:.1%} of IT employees are over 30 years old. Conversely, {young_it_pct:.1%} "
    f"of the IT team consists of younger professionals (≤30 years old).\n"
)

# Insight 4: IT Salary Premium
diff_it_sal = p_high_sal_given_it - p_overall_high_salary
print(
    f"4. Departmental Salary Disparity (IT Sector):\n"
    f"   IT employees have a {p_high_sal_given_it:.1%} chance of earning a High Salary, "
    f"which is {diff_it_sal:+.1%} relative to the company-wide average.\n"
)

# Insight 5: Pay vs Performance Alignment Gap
gap = p_high_sal_given_exp5 - p_high_perf_given_exp5
print(
    f"5. Pay-for-Performance Alignment Gap:\n"
    f"   Among experienced employees (>5 yrs), there is a {abs(gap):.1%} gap between the probability "
    f"of earning a High Salary ({p_high_sal_given_exp5:.1%}) and achieving High Performance ({p_high_perf_given_exp5:.1%}). "
    f"This reveals how strongly compensation aligns with actual output vs tenure."
)