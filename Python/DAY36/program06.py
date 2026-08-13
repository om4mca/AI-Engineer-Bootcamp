import numpy as np


# Theoretical calculation
def complement_prob(p_event):
    """Returns the probability of the complement event."""
    return 1 - p_event


# Monte Carlo Simulation: "At least one 6 in 4 die rolls"
def simulate_at_least_one_six(num_trials=1_000_000):
    # Roll a die 4 times per trial
    rolls = np.random.randint(1, 7, size=(num_trials, 4))

    # Check if 6 is present in each trial
    has_six = np.any(rolls == 6, axis=1)

    return np.mean(has_six)


# --- Calculations ---
p_single_no_6 = 5 / 6
p_four_no_6 = (5 / 6) ** 4
p_theoretical_at_least_one_6 = 1 - p_four_no_6

p_empirical = simulate_at_least_one_six()

print(f"P(No 6 in 4 rolls)               : {p_four_no_6:.4f}")
print(
    f"Theoretical P(At least one 6)     : {p_theoretical_at_least_one_6:.4f}"
    f" ({p_theoretical_at_least_one_6*100:.2f}%)"
)
print(
    f"Empirical P(1M Simulations)       : {p_empirical:.4f}"
    f" ({p_empirical*100:.2f}%)"
)