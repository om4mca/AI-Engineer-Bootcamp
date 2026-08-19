from collections import Counter
import math
import numpy as np


class DiscreteDistribution:

    def __init__(self, data):
        self.data = list(data)
        self.total_count = len(self.data)

        # Count frequencies
        self.frequencies = Counter(self.data)
        self.unique_values = sorted(self.frequencies.keys())

        # Calculate Probability Mass Function (PMF)
        self.pmf = {
            val: count / self.total_count
            for val, count in self.frequencies.items()
        }

        # Calculate Cumulative Distribution Function (CDF)
        self.cdf = {}
        cumulative = 0.0
        for val in self.unique_values:
            cumulative += self.pmf[val]
            self.cdf[val] = cumulative

    def summary_statistics(self):
        """Calculates Expected Value, Variance, and Standard Deviation."""
        # E[X] = sum(x * P(X=x))
        mean = sum(x * p for x, p in self.pmf.items())

        # Var(X) = sum((x - E[X])^2 * P(X=x))
        variance = sum(((x - mean) ** 2) * p for x, p in self.pmf.items())
        std_dev = math.sqrt(variance)

        return {"Mean E[X]": mean, "Variance": variance, "Std Dev": std_dev}

    def display_distribution_table(self):
        """Prints a styled PMF/CDF distribution table."""
        print("==================================================")
        print("         DISCRETE DATA DISTRIBUTION TABLE         ")
        print("==================================================")
        print(
            f"{'Value (x)':<10} | {'Frequency':<10} | {'PMF P(X=x)':<12} | {'CDF P(X<=x)':<12}"
        )
        print("-" * 52)

        for x in self.unique_values:
            freq = self.frequencies[x]
            p = self.pmf[x]
            c = self.cdf[x]
            print(f"{x:<10} | {freq:<10} | {p:<12.4f} | {c:<12.4f}")

    def ascii_histogram(self, max_width=30):
        """Generates an ASCII bar chart of the discrete PMF."""
        print("\n==================================================")
        print("            PMF DISTRIBUTION HISTOGRAM            ")
        print("==================================================")
        max_p = max(self.pmf.values())

        for x in self.unique_values:
            p = self.pmf[x]
            bar = "█" * int((p / max_p) * max_width)
            print(f"{x:2d} | {bar:<{max_width}} | {p:.2%}")


# ==============================================================================
# Example Usage: Customer support calls per hour across 1,000 hours
# ==============================================================================
np.random.seed(42)
# Simulate Poisson discrete data (average 3 calls per hour)
sample_data = np.random.poisson(lam=3, size=1000)

# Instantiate distribution
dist = DiscreteDistribution(sample_data)

# Output Table & Histogram
dist.display_distribution_table()
dist.ascii_histogram()

# Output Key Metrics
stats = dist.summary_statistics()
print("\n==================================================")
print("               SUMMARY STATISTICS                 ")
print("==================================================")
for metric, val in stats.items():
    print(f"{metric:<15}: {val:.4f}")