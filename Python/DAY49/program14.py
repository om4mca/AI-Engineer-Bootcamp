import numpy as np


class ErrorAnalyzer:
    """Computes and analyzes RSS, MSE, RMSE, R-squared, and residual properties."""

    def __init__(self, y_true, y_pred, num_params=0):
        self.y_true = np.array(y_true, dtype=float).flatten()
        self.y_pred = np.array(y_pred, dtype=float).flatten()
        
        if self.y_true.shape != self.y_pred.shape:
            raise ValueError("Dimensions of y_true and y_pred must match.")
            
        self.n = len(self.y_true)
        self.p = num_params  # Number of model parameters (used for adjusted metrics)
        self.residuals = self.y_true - self.y_pred

    # --- 1. Core Error Metrics ---
    def compute_metrics(self):
        """Calculates RSS, MSE, RMSE, MAE, and Standard Error of Estimate."""
        rss = np.sum(self.residuals ** 2)
        mse = rss / self.n
        rmse = np.sqrt(mse)
        mae = np.mean(np.abs(self.residuals))

        # Adjusted MSE taking degrees of freedom (n - p) into account
        df = self.n - self.p
        unbiased_mse = rss / df if df > 0 else mse
        unbiased_rmse = np.sqrt(unbiased_mse)

        return {
            "Sample Size (n)": self.n,
            "Degrees of Freedom": df,
            "Residual Sum of Squares (RSS)": rss,
            "Mean Squared Error (MSE)": mse,
            "Root Mean Squared Error (RMSE)": rmse,
            "Mean Absolute Error (MAE)": mae,
            "Unbiased MSE (Dof Corrected)": unbiased_mse,
            "Unbiased RMSE": unbiased_rmse,
        }

    # --- 2. Variance Decomposition & Goodness-of-Fit ---
    def compute_goodness_of_fit(self):
        """Decomposes Total Sum of Squares (TSS) into ESS + RSS."""
        y_mean = np.mean(self.y_true)
        tss = np.sum((self.y_true - y_mean) ** 2)
        ess = np.sum((self.y_pred - y_mean) ** 2)
        rss = np.sum(self.residuals ** 2)

        r_squared = 1.0 - (rss / tss) if tss > 1e-12 else 1.0
        
        # Adjusted R^2
        if self.n > self.p and self.p > 0:
            adj_r2 = 1.0 - ((1.0 - r_squared) * (self.n - 1) / (self.n - self.p))
        else:
            adj_r2 = r_squared

        return {
            "Total Sum of Squares (TSS)": tss,
            "Explained Sum of Squares (ESS)": ess,
            "R-squared (R^2)": r_squared,
            "Adjusted R-squared": adj_r2,
        }

    # --- 3. Residual Diagnostics & Outlier Detection ---
    def analyze_residuals(self):
        """Analyzes residual distribution (mean, std, skewness) and flags outliers."""
        mean_res = np.mean(self.residuals)
        std_res = np.std(self.residuals, ddof=1)
        
        # Standardized Residuals
        std_residuals = self.residuals / std_res if std_res > 1e-12 else self.residuals
        outliers_idx = np.where(np.abs(std_residuals) > 2.0)[0]

        # Skewness calculation
        skewness = np.mean((self.residuals - mean_res) ** 3) / (std_res ** 3) if std_res > 1e-12 else 0.0

        return {
            "Residual Mean": mean_res,
            "Residual Std Dev": std_res,
            "Residual Skewness": skewness,
            "Outlier Indices (|std_res| > 2)": outliers_idx.tolist(),
            "Outlier Count": len(outliers_idx),
        }

    # --- 4. Unified Full Report ---
    def full_report(self):
        return {
            "Error Metrics": self.compute_metrics(),
            "Goodness of Fit": self.compute_goodness_of_fit(),
            "Residual Diagnostics": self.analyze_residuals(),
        }


# --- Execution Example ---
if __name__ == "__main__":
    print("=" * 65)
    print("                 RSS & MSE ERROR ANALYSIS REPORT")
    print("=" * 65)

    # Simulated targets and model predictions
    np.random.seed(42)
    y_true = np.array([10.5, 14.2, 18.0, 22.1, 26.5, 30.0, 35.2, 40.1, 44.8, 50.0])
    y_pred = y_true + np.random.normal(loc=0.0, scale=1.5, size=len(y_true))
    # Inject an outlier
    y_pred[3] += 5.5

    analyzer = ErrorAnalyzer(y_true, y_pred, num_params=2)
    report = analyzer.full_report()

    for category, metrics in report.items():
        print(f"\n[{category}]")
        for k, v in metrics.items():
            if isinstance(v, float):
                print(f"  {k:<32}: {v:.4f}")
            else:
                print(f"  {k:<32}: {v}")

    print("=" * 65)