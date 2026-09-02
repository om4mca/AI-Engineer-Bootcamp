import numpy as np


class NumPyStatisticalAnalyzer:
    """Multi-Dimensional NumPy Array-based Statistical Analysis Engine."""

    def __init__(self, data: np.ndarray):
        """Matrix ensure karta hai baseline analysis ke liye."""
        self.data = np.asarray(data, dtype=float)

    def summary_statistics(self, axis: int = None) -> dict:
        """Computes fundamental parametric metrics, properly ignoring NaNs."""
        return {
            "Count (Non-NaN)": np.count_nonzero(~np.isnan(self.data), axis=axis),
            "Mean": np.nanmean(self.data, axis=axis),
            "Median": np.nanmedian(self.data, axis=axis),
            "Std Dev": np.nanstd(self.data, axis=axis),
            "Variance": np.nanvar(self.data, axis=axis),
            "Min": np.nanmin(self.data, axis=axis),
            "Max": np.nanmax(self.data, axis=axis),
        }

    def compute_percentiles(
        self, percentiles: list = [25, 50, 75], axis: int = None
    ) -> dict:
        """Percentiles and Interquartile Ranges (IQR) across multi-dimensions."""
        results = {}
        for p in percentiles:
            results[f"{p}th Percentile"] = np.nanpercentile(
                self.data, p, axis=axis
            )
        return results

    def weighted_average(self, weights: np.ndarray, axis: int = 0) -> np.ndarray:
        """Calculates weighted arithmetic mean along a specified axis."""
        return np.average(self.data, weights=weights, axis=axis)

    def correlation_and_covariance(self) -> dict:
        """Computes Covariance matrix and Pearson Correlation Coefficients."""
        # Removing rows containing NaN for matrix operations
        clean_data = self.data[~np.isnan(self.data).any(axis=1)]
        return {
            "Covariance Matrix": np.cov(clean_data, rowvar=False),
            "Correlation Matrix": np.corrcoef(clean_data, rowvar=False),
        }


# ==========================================
# Driver Code & Execution
# ==========================================
if __name__ == "__main__":
    print("============================================")
    print("      NUMPY STATISTICAL ANALYZER SYSTEM     ")
    print("============================================\n")

    # 1. Create a 5x3 dataset with NaN values simulating real-world noisy data
    dataset = np.array(
        [
            [10.0, 20.0, 30.0],
            [12.0, np.nan, 35.0],
            [15.0, 25.0, 40.0],
            [18.0, 30.0, np.nan],
            [22.0, 35.0, 50.0],
        ]
    )

    analyzer = NumPyStatisticalAnalyzer(dataset)

    # 2. Overall Summary Statistics (All Elements)
    print("--- [1] Overall Dataset Statistics ---")
    overall_stats = analyzer.summary_statistics()
    for metric, val in overall_stats.items():
        print(f"  {metric:<18}: {val}")

    # 3. Column-wise Statistics (Axis = 0)
    print("\n--- [2] Column-wise Mean & Std Dev (Axis 0, Ignoring NaNs) ---")
    col_stats = analyzer.summary_statistics(axis=0)
    print("  Column Means  :", col_stats["Mean"])
    print("  Column Std Dev:", col_stats["Std Dev"])

    # 4. Percentile Calculations
    print("\n--- [3] Quartiles & Percentiles (Column-wise) ---")
    percentiles = analyzer.compute_percentiles(
        percentiles=[25, 50, 75], axis=0
    )
    for p_name, p_val in percentiles.items():
        print(f"  {p_name:<15}: {p_val}")

    # 5. Weighted Mean Along Columns
    weights = np.array([0.1, 0.2, 0.3, 0.1, 0.3])
    # Impute NaN temporarily for weighted calculation
    clean_imputed = np.nan_to_num(dataset, nan=np.nanmean(dataset))
    imputed_analyzer = NumPyStatisticalAnalyzer(clean_imputed)
    weighted_mean = imputed_analyzer.weighted_average(weights=weights, axis=0)
    print(
        f"\n--- [4] Weighted Column Means ---\n  Result: {weighted_mean}"
    )

    # 6. Correlation & Covariance Matrix
    print("\n--- [5] Covariance & Correlation Matrix ---")
    matrices = imputed_analyzer.correlation_and_covariance()
    print("Correlation Matrix:\n", matrices["Correlation Matrix"])