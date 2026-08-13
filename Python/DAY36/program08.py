import numpy as np
import pandas as pd

# Set simulation parameters
num_trials = 1_000_000

# Roll two 6-sided dice
die1 = np.random.randint(1, 7, size=num_trials)
die2 = np.random.randint(1, 7, size=num_trials)
sums = die1 + die2

# Calculate frequencies and empirical probabilities
unique_sums, counts = np.unique(sums, return_counts=True)
empirical_probs = counts / num_trials

# Theoretical probabilities mapping
theoretical_counts = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
theoretical_probs = [c / 36 for c in theoretical_counts]

# Display comparative dataframe
df_results = pd.DataFrame({
    'Sum': unique_sums,
    'Favorable Outcomes': theoretical_counts,
    'Theoretical P': [f"{p*100:.2f}%" for p in theoretical_probs],
    'Empirical P (1M Runs)': [f"{p*100:.2f}%" for p in empirical_probs]
})

print(df_results.to_string(index=False))