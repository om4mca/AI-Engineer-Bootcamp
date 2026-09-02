import math
import statistics
from typing import Dict, List, Union


class StatisticalSummarySystem:
    """Pure Python Descriptive & Diagnostic Statistical Summary Engine."""

    def __init__(self, data: List[Union[int, float]]):
        if not data or len(data) < 2:
            raise ValueError(
                "Data set must contain at least 2 numerical elements."
            )
        self.data = sorted(data)
        self.n = len(self.data)

    def measure_central_tendency(self) -> Dict[str, float]:
        """Calculates Mean, Median, and Mode metrics."""
        mean_val = statistics.mean(self.data)
        median_val = statistics.median(self.data)

        try:
            mode_val = statistics.mode(self.data)
        except statistics.StatisticsError:
            mode_val = None  # Multiple modes or no distinct mode

        return {
            "Mean": round(mean_val, 4),
            "Median": round(median_val, 4),
            "Mode": mode_val,
        }

    def measure_dispersion(self) -> Dict[str, float]:
        """Calculates Variance, Standard Deviation, Range, and IQR."""
        p_var = statistics.pvariance(self.data)
        s_var = statistics.variance(self.data)
        s_std = statistics.stdev(self.data)

        # Quantiles for Interquartile Range (IQR)
        quantiles = statistics.quantiles(self.data, n=4)
        q1, q2, q3 = quantiles[0], quantiles[1], quantiles[2]
        iqr = q3 - q1

        return {
            "Min": self.data[0],
            "Max": self.data[-1],
            "Range": self.data[-1] - self.data[0],
            "Sample Variance": round(s_var, 4),
            "Sample Std Dev": round(s_std, 4),
            "Q1 (25th Percentile)": round(q1, 4),
            "Q3 (75th Percentile)": round(q3, 4),
            "IQR": round(iqr, 4),
        }

    def measure_shape_and_moments(self) -> Dict[str, float]:
        """Calculates Skewness (Asymmetry) and Kurtosis (Tailedness)."""
        mean_val = statistics.mean(self.data)
        std_val = statistics.stdev(self.data)

        if std_val == 0:
            return {"Skewness": 0.0, "Kurtosis": 0.0}

        # Fisher-Pearson coefficient of Skewness
        skewness = (
            sum((x - mean_val) ** 3 for x in self.data) * self.n
        ) / ((self.n - 1) * (self.n - 2) * (std_val**3))

        # Sample Excess Kurtosis
        m4 = sum((x - mean_val) ** 4 for x in self.data) / self.n
        m2 = sum((x - mean_val) ** 2 for x in self.data) / self.n
        excess_kurtosis = (m4 / (m2**2)) - 3.0

        return {
            "Skewness": round(skewness, 4),
            "Excess Kurtosis": round(excess_kurtosis, 4),
        }

    def detect_outliers_iqr(self) -> Dict[str, Union[float, List]]:
        """Identifies statistical outliers using 1.5 * IQR Rule."""
        quantiles = statistics.quantiles(self.data, n=4)
        q1, q3 = quantiles[0], quantiles[2]
        iqr = q3 - q1

        lower_bound = q1 - (1.5 * iqr)
        upper_bound = q3 + (1.5 * iqr)

        outliers = [x for x in self.data if x < lower_bound or x > upper_bound]

        return {
            "Lower Bound": round(lower_bound, 4),
            "Upper Bound": round(upper_bound, 4),
            "Outliers Count": len(outliers),
            "Outliers Detected": outliers,
        }

    def generate_full_report(self):
        """Prints a comprehensive text-based statistical summary table."""
        print("==================================================")
        print("         STATISTICAL SUMMARY REPORT               ")
        print("==================================================")

        print("\n[1] Central Tendency Metrics:")
        for metric, val in self.measure_central_tendency().items():
            print(f"  {metric:<25}: {val}")

        print("\n[2] Dispersion & Spread Metrics:")
        for metric, val in self.measure_dispersion().items():
            print(f"  {metric:<25}: {val}")

        print("\n[3] Distribution Shape Metrics:")
        for metric, val in self.measure_shape_and_moments().items():
            print(f"  {metric:<25}: {val}")

        print("\n[4] Outlier Audit (IQR Method):")
        for metric, val in self.detect_outliers_iqr().items():
            print(f"  {metric:<25}: {val}")
        print("==================================================\n")


# ==========================================
# Driver Code & Execution
# ==========================================
if __name__ == "__main__":
    # Sample Dataset with intentional skewness and an outlier
    sample_dataset = [
        12, 15, 14, 15, 16, 18, 19, 22, 23, 23,
        25, 28, 30, 31, 32, 35, 38, 42, 45, 115 # 115 is a clear outlier
    ]

    # Engine Initialization
    stats_engine = StatisticalSummarySystem(sample_dataset)
    stats_engine.generate_full_report()