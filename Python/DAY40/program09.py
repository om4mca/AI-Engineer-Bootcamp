import numpy as np

# Parameters: 10 flips per experiment, 50% chance of heads, run 8 experiments
n_trials = 10     # Number of Bernoulli trials per experiment (n)
prob = 0.5        # Success probability per trial (p)
experiments = 8   # Number of experiment iterations

# Run simulation
outcomes = np.random.binomial(n=n_trials, p=prob, size=experiments)

print("--- NUMPY BINOMIAL OUTCOMES ---")
print(f"Successes out of {n_trials} trials across {experiments} runs:")
print(outcomes)