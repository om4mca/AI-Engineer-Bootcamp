import numpy as np

# Experiment: Roll a 6-sided die and track P(Roll = 6)
theoretical_p = 1 / 6

sample_sizes = [10, 100, 10_000, 1_000_000]

print(f"Theoretical Probability P(6) = {theoretical_p:.5f} ({theoretical_p*100:.2f}%)\n")
print(f"{'Sample Size':<15} | {'Experimental P(6)':<20} | {'Absolute Difference':<20}")
print("-" * 60)

for n in sample_sizes:
    rolls = np.random.randint(1, 7, size=n)
    experimental_p = np.sum(rolls == 6) / n
    diff = abs(experimental_p - theoretical_p)
    print(
        f"{n:<15,} | {experimental_p:<20.5f} | {diff:<20.5f}"
    )