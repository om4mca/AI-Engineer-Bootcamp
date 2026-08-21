import numpy as np

# Simulation Parameters
p = 0.7        # Probability of success
n_trials = 10  # Number of single Bernoulli trials

# Method A: Using np.random.choice
trials_choice = np.random.choice([1, 0], size=n_trials, p=[p, 1 - p])

# Method B: Using uniform random numbers thresholded at p
trials_threshold = (np.random.uniform(0, 1, size=n_trials) < p).astype(int)

print("--- NUMPY BERNOULLI SIMULATION ---")
print(f"Generated Outcomes (Method A): {trials_choice}")
print(f"Generated Outcomes (Method B): {trials_threshold}")