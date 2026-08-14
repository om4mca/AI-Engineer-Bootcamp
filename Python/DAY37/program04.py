# 1. Raw Dataset represented as a list of dictionaries
dataset = [
    {"Gender": "Female", "Status": "Pass"},
    {"Gender": "Male", "Status": "Fail"},
    {"Gender": "Female", "Status": "Pass"},
    {"Gender": "Male", "Status": "Pass"},
    {"Gender": "Female", "Status": "Fail"},
    {"Gender": "Male", "Status": "Pass"},
    {"Gender": "Female", "Status": "Pass"},
    {"Gender": "Male", "Status": "Fail"},
    {"Gender": "Female", "Status": "Pass"},
    {"Gender": "Male", "Status": "Pass"},
]


# 2. Function to compute P(Event A | Event B) using dictionaries
def calculate_conditional_prob_dict(data, event_key, event_val, given_key, given_val):
    """Calculates P(event_key=event_val | given_key=given_val)"""
    given_count = 0
    intersection_count = 0

    for record in data:
        # Check if the record matches the GIVEN condition (B)
        if record.get(given_key) == given_val:
            given_count += 1
            # Check if the record ALSO matches the EVENT condition (A)
            if record.get(event_key) == event_val:
                intersection_count += 1

    # Avoid division by zero if given condition never occurs
    if given_count == 0:
        return 0.0

    return intersection_count / given_count


# 3. Calculate Conditional Probabilities
p_pass_given_female = calculate_conditional_prob_dict(
    dataset,
    event_key="Status",
    event_val="Pass",
    given_key="Gender",
    given_val="Female",
)

p_pass_given_male = calculate_conditional_prob_dict(
    dataset,
    event_key="Status",
    event_val="Pass",
    given_key="Gender",
    given_val="Male",
)

# 4. Print Results
print("--- CONDITIONAL PROBABILITY (USING DICTIONARIES) ---")
print(f"P(Pass | Female) : {p_pass_given_female:.2%}")
print(f"P(Pass | Male)   : {p_pass_given_male:.2%}")