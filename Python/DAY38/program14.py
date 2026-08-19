from collections import Counter
import math
import random


class HospitalTestDistribution:

    def __init__(self, processing_times_minutes):
        """Initialize with raw test duration data (in minutes)."""
        self.data = list(processing_times_minutes)
        self.total_tests = len(self.data)

        # 1. Summary Statistics
        self.mean = sum(self.data) / self.total_tests
        self.variance = (
            sum((x - self.mean) ** 2 for x in self.data) / self.total_tests
        )
        self.std_dev = math.sqrt(self.variance)

    def calculate_discrete_pmf_cdf(self, bin_size=15):
        """Bins continuous processing times into discrete time windows (e.g., 15-minute intervals)

        and computes PMF / CDF.
        """
        binned_data = [int(x // bin_size) * bin_size for x in self.data]
        counts = Counter(binned_data)
        unique_bins = sorted(counts.keys())

        pmf = {b: counts[b] / self.total_tests for b in unique_bins}

        cdf = {}
        running_sum = 0.0
        for b in unique_bins:
            running_sum += pmf[b]
            cdf[b] = running_sum

        return pmf, cdf, unique_bins

    def ascii_histogram(self, bin_size=15, max_bar_width=30):
        """Displays an ASCII frequency histogram of hospital test processing times."""
        pmf, cdf, unique_bins = self.calculate_discrete_pmf_cdf(bin_size)
        max_p = max(pmf.values())

        print("==================================================")
        print("    HOSPITAL TEST PROCESSING TIME HISTOGRAM       ")
        print("==================================================")
        print(
            f"{'Interval (min)':<15} | {'PMF P(X=x)':<10} | {'CDF P(X<=x)':<10} | Histogram"
        )
        print("-" * 65)

        for b in unique_bins:
            p = pmf[b]
            c = cdf[b]
            interval_str = f"[{b:3d} - {b+bin_size:3d})"
            bar = "█" * int((p / max_p) * max_bar_width)
            print(f"{interval_str:<15} | {p:<10.2%} | {c:<10.2%} | {bar}")


# ==============================================================================
# Simulation: Blood Test Processing Times across 1,000 Hospital Patients
# Modeling right-skewed service times using Gamma distribution (Shape=3, Scale=10)
# ==============================================================================
random.seed(42)

# Generate 1,000 synthetic lab test durations (Mean ~ 30 minutes)
simulated_test_times = [
    random.gammavariate(alpha=3.0, beta=10.0) for _ in range(1000)
]

# Instantiate Analysis
hospital_dist = HospitalTestDistribution(simulated_test_times)

# 1. Output Summary Metrics
print("==================================================")
print("     HOSPITAL LAB TEST DURATION METRICS          ")
print("==================================================")
print(f"Total Tests Processed : {hospital_dist.total_tests:,}")
print(f"Expected Value E[X]   : {hospital_dist.mean:.2f} minutes")
print(f"Variance Var(X)       : {hospital_dist.variance:.2f}")
print(f"Std Dev (Sigma)       : {hospital_dist.std_dev:.2f} minutes\n")

# 2. Output Histogram & Binned Distribution
hospital_dist.ascii_histogram(bin_size=15)