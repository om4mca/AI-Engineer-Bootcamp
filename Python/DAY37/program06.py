# ==============================================================================
# Scenario 1: Sampling Without Replacement (Drawing 2 Aces in a Row)
# ==============================================================================
# Standard deck: 52 cards, 4 Aces

total_cards = 52
total_aces = 4

# Step 1: P(First Card is Ace)
p_first_ace = total_aces / total_cards  # 4/52

# Step 2: After drawing an Ace without replacement:
# Remaining cards = 51, Remaining Aces = 3
p_second_ace_given_first = (total_aces - 1) / (total_cards - 1)  # 3/51

# Step 3: P(Both Cards are Aces) = P(First Ace) * P(Second Ace | First Ace)
p_both_aces = p_first_ace * p_second_ace_given_first

print("=== SCENARIO 1: DRAWING TWO ACES WITHOUT REPLACEMENT ===")
print(f"P(1st Card is Ace)              : {p_first_ace:.4f}  (4/52)")
print(
    f"P(2nd Card is Ace | 1st is Ace) : {p_second_ace_given_first:.4f}  (3/51)"
)
print(f"P(Both Cards are Aces)          : {p_both_aces:.4f}  (12/2652 = 1/221)\n")


# ==============================================================================
# Scenario 2: Dependent Probabilities from Dataset
# ==============================================================================
# Dataset: Experience vs Performance
dataset = [
    {"Experience": ">5yrs", "Performance": "High"},
    {"Experience": "<=5yrs", "Performance": "Low"},
    {"Experience": ">5yrs", "Performance": "High"},
    {"Experience": ">5yrs", "Performance": "Low"},
    {"Experience": "<=5yrs", "Performance": "Low"},
    {"Experience": ">5yrs", "Performance": "High"},
    {"Experience": "<=5yrs", "Performance": "High"},
    {"Experience": "<=5yrs", "Performance": "Low"},
]

total = len(dataset)

# Event A: High Performance
# Event B: Experience > 5yrs
count_A = sum(1 for row in dataset if row["Performance"] == "High")
count_B = sum(1 for row in dataset if row["Experience"] == ">5yrs")
count_A_and_B = sum(
    1
    for row in dataset
    if row["Performance"] == "High" and row["Experience"] == ">5yrs"
)

# Unconditional Probabilities
p_A = count_A / total
p_B = count_B / total

# Dependent Conditional Probability P(A | B) = Count(A and B) / Count(B)
p_A_given_B = count_A_and_B / count_B

# Joint Probability via Multiplication Rule: P(A ∩ B) = P(B) * P(A | B)
p_A_and_B_calculated = p_B * p_A_given_B

print("=== SCENARIO 2: DATASET DEPENDENCE CHECK ===")
print(f"P(Performance = High) [P(A)]                   : {p_A:.4f}")
print(f"P(Experience > 5yrs) [P(B)]                    : {p_B:.4f}")
print(f"P(High Performance | Exp > 5yrs) [P(A | B)]    : {p_A_given_B:.4f}")
print(
    f"Joint P(High Perf AND Exp > 5yrs) [P(A ∩ B)]    : {p_A_and_B_calculated:.4f}"
)

# Dependency Verification
if abs(p_A_given_B - p_A) > 1e-9:
    print(
        f"\nDependency Check: P(A|B) [{p_A_given_B:.2f}] != P(A) [{p_A:.2f}] -> Events are DEPENDENT."
    )