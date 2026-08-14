# Define the full sample space (Rolling a standard 6-sided die)
sample_space = {1, 2, 3, 4, 5, 6}

# Define Event A: Rolling an Even Number
event_A = {2, 4, 6}

# Define Event B: Rolling a Number Greater Than 3
event_B = {4, 5, 6}


# ------------------------------------------------------------------
# 1. Approach 1: Using the Classical Formula P(A|B) = P(A ∩ B) / P(B)
# ------------------------------------------------------------------
# Event (A ∩ B): Numbers that are BOTH even AND greater than 3
event_A_intersect_B = event_A.intersection(event_B)

# Calculate probabilities relative to the entire sample space
p_B = len(event_B) / len(sample_space)
p_A_and_B = len(event_A_intersect_B) / len(sample_space)

# Formula: P(A | B) = P(A ∩ B) / P(B)
p_A_given_B_formula = p_A_and_B / p_B


# ------------------------------------------------------------------
# 2. Approach 2: Reduced Sample Space Method
# ------------------------------------------------------------------
# Since Event B has already occurred, Event B becomes the new sample space.
# We count how many outcomes in Event B also belong to Event A.
favorable_outcomes = len(event_A_intersect_B)
total_outcomes_in_B = len(event_B)

p_A_given_B_reduced = favorable_outcomes / total_outcomes_in_B


# ------------------------------------------------------------------
# Output Results
# ------------------------------------------------------------------
print(f"Sample Space             : {sample_space}")
print(f"Event A (Even Numbers)   : {event_A}")
print(f"Event B (Numbers > 3)    : {event_B}")
print(f"Intersection (A ∩ B)     : {event_A_intersect_B}\n")

print(f"P(B)                     : {p_B:.4f}  ({len(event_B)}/6)")
print(f"P(A ∩ B)                 : {p_A_and_B:.4f}  ({len(event_A_intersect_B)}/6)")
print("-" * 45)
print(f"P(A | B) via Formula     : {p_A_given_B_formula:.4f}  (2/3)")
print(f"P(A | B) via Reduced Space: {p_A_given_B_reduced:.4f}  (2/3)")