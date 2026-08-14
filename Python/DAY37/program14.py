import random

# Number of experimental trials
num_trials = 100_000

count_B = 0  # Condition B: At least one die is a 4
count_A_and_B = 0  # Condition A & B: Sum is 8 AND at least one die is a 4

random.seed(42)  # For reproducible results

for _ in range(num_trials):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)

    # Check Condition B: At least one die shows 4
    if die1 == 4 or die2 == 4:
        count_B += 1

        # Check Condition A: Total sum is 8
        if die1 + die2 == 8:
            count_A_and_B += 1

# Calculate Experimental Conditional Probability
p_experimental = count_A_and_B / count_B

# Theoretical exact value for comparison:
# Outcomes where at least one die is 4: (4,1),(4,2),(4,3),(4,4),(4,5),(4,6),(1,4),(2,4),(3,4),(5,4),(6,4) -> Total = 11
# Outcomes where sum is 8 AND at least one die is 4: (4,4) -> Total = 1
p_theoretical = 1 / 11

print("=== EXPERIMENTAL VS THEORETICAL CONDITIONAL PROBABILITY ===")
print(f"Total Trials               : {num_trials:,}")
print(f"Total occurrences of B     : {count_B:,}")
print(f"Total occurrences of A & B : {count_A_and_B:,}")
print("-" * 55)
print(f"Experimental P(Sum=8 | Die=4) : {p_experimental:.4f} ({p_experimental:.2%})")
print(f"Theoretical P(Sum=8 | Die=4)  : {p_theoretical:.4f} ({p_theoretical:.2%})")