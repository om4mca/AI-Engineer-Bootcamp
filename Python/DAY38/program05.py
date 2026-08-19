import math
import numpy as np


class ContinuousDistribution:

    def __init__(self, data):
        self.data = np.array(data)
        self.size = len(self.data)

        # Empirical Parametric Estimation (Assuming Normal/Gaussian behavior)
        self.mean = np.mean(self.data)
        self.variance = np.var(self.data, ddof=0)
        self.std_dev = np.sqrt(self.variance)

    def pdf(self, x):
        """Calculates Probability Density Function f(x) for a Gaussian distribution."""
        exponent = math.exp(-0.5 * ((x - self.mean) / self.std_dev) ** 2)
        return (1.0 / (self.std_dev * math.sqrt(2 * math.pi))) * exponent

    def probability_in_interval(self, a, b, num_steps=1000):
        """Calculates P(a <= X <= b) by numerically integrating the PDF using the Trapezoidal Rule."""
        x_vals = np.linspace(a, b, num_steps)
        y_vals = np.array([self.pdf(x) for x in x_vals])

        # Numerical integration (trapezoidal integration)
        area = np.trapezoid(y_vals, x_vals)
        return area

    def ascii_histogram(self, bins=10, max_width=30):
        """Generates an ASCII frequency distribution for continuous data binned into intervals."""
        print("==================================================")
        print("         CONTINUOUS DATA BINNED HISTOGRAM         ")
        print("==================================================")

        counts, bin_edges = np.histogram(self.data, bins=bins)
        max_count = max(counts)

        for i in range(len(counts)):
            low = bin_edges[i]
            high = bin_edges[i + 1]
            count = counts[i]
            pct = count / self.size
            bar = "█" * int((count / max_count) * max_width)

            print(
                f"[{low:5.2f} - {high:5.2f}] | {bar:<{max_width}} | {count:4d} ({pct:5.2%})"
            )


# ==============================================================================
# Example Usage: Server Response Time (in milliseconds) across 10,000 requests
# ==============================================================================
np.random.seed(42)

# Generate continuous Gaussian data (Mean = 200 ms, Std Dev = 15 ms)
response_times = np.random.normal(loc=200.0, scale=15.0, size=10_000)

# Instantiate distribution
dist = ContinuousDistribution(response_times)

# 1. Summary Statistics
print("==================================================")
print("            CONTINUOUS DATA SUMMARY               ")
print("==================================================")
print(f"Sample Size (N)     : {dist.size:,}")
print(f"Empirical Mean E[X] : {dist.mean:.2f} ms")
print(f"Variance Var(X)     : {dist.variance:.2f}")
print(f"Std Dev (Sigma)     : {dist.std_dev:.2f} ms\n")

# 2. Probability Density vs Point Probability
x_test = 200.0
print("==================================================")
print("        PDF & INTERVAL PROBABILITY DEMO           ")
print("==================================================")
print(
    f"P(X = {x_test:.1f})            : 0.0000 (Point probability is ALWAYS zero)"
)
print(
    f"PDF Height f({x_test:.1f})      : {dist.pdf(x_test):.4f} (Probability Density, NOT Probability)"
)

# 3. Interval Probability P(185 <= X <= 215) -> Within 1 Std Dev
p_interval = dist.probability_in_interval(185.0, 215.0)
print(
    f"P(185 <= X <= 215)      : {p_interval:.4f} ({p_interval:.2%} chance)\n"
)

# 4. Display Binned Distribution
dist.ascii_histogram(bins=10)