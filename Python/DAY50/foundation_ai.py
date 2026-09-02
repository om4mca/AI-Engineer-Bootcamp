import warnings
import numpy as np
import pandas as pd
from scipy import stats

warnings.filterwarnings("ignore")


class AIEngineerFoundationAnalyticsSystem:
    """Day 50 Capstone Revision Project.

    Combines Python, Pandas, NumPy, Statistics, Probability, EDA, and Linear
    Algebra into an integrated mathematical & analytical engine.
    """

    def __init__(self, raw_data: pd.DataFrame, target_column: str):
        self.df = raw_data.copy()
        self.target_col = target_column
        self.numeric_cols = self.df.select_dtypes(
            include=[np.number]
        ).columns.tolist()
        self.feature_cols = [
            c for c in self.numeric_cols if c != self.target_col
        ]

    # ==========================================
    # 1. Data Processing & Preprocessing (Pandas/NumPy)
    # ==========================================
    def preprocess_pipeline(self) -> pd.DataFrame:
        """Handles missing values, removes outliers via Z-Score, and normalizes features."""
        # Fill missing values with median
        for col in self.numeric_cols:
            if self.df[col].isnull().sum() > 0:
                self.df[col].fillna(self.df[col].median(), inplace=True)

        # Z-Score Outlier Filtering (|Z| < 3.0)
        z_scores = np.abs(stats.zscore(self.df[self.numeric_cols]))
        filtered_entries = (z_scores < 3.0).all(axis=1)
        self.df = self.df[filtered_entries].reset_index(drop=True)

        return self.df

    # ==========================================
    # 2. Descriptive & Inferential Statistics
    # ==========================================
    def compute_statistical_diagnostics(self) -> pd.DataFrame:
        """Calculates Central Tendency, Dispersion, Skewness, Kurtosis, and IQR."""
        stats_dict = {}
        for col in self.numeric_cols:
            data = self.df[col]
            q25, q75 = np.percentile(data, [25, 75])
            stats_dict[col] = {
                "Mean": np.mean(data),
                "Median": np.median(data),
                "Std Dev": np.std(data, ddof=1),
                "Variance": np.var(data, ddof=1),
                "IQR": q75 - q25,
                "Skewness": stats.skew(data),
                "Kurtosis": stats.kurtosis(data),
            }
        return pd.DataFrame(stats_dict).T

    # ==========================================
    # 3. Probability & Hypothesis Testing Engine
    # ==========================================
    def run_probability_and_hypothesis_tests(self) -> dict:
        """Evaluates Gaussian Normality (Shapiro-Wilk) and Correlation Significance."""
        results = {}

        # 1. Normality Check on Target Variable
        shapiro_stat, shapiro_p = stats.shapiro(self.df[self.target_col])
        results["Target Normality (Shapiro-Wilk)"] = {
            "Statistic": round(shapiro_stat, 4),
            "p-value": round(shapiro_p, 4),
            "Is Normal (alpha=0.05)?": shapiro_p > 0.05,
        }

        # 2. Pearson Correlation & P-value with Target
        correlations = {}
        for col in self.feature_cols:
            r, p_val = stats.pearsonr(self.df[col], self.df[self.target_col])
            correlations[col] = {
                "Pearson r": round(r, 4),
                "p-value": round(p_val, 4),
                "Statistically Significant?": p_val < 0.05,
            }
        results["Feature Correlations with Target"] = correlations
        return results

    # ==========================================
    # 4. Exploratory Data Analysis (EDA Insights)
    # ==========================================
    def generate_eda_summary(self) -> dict:
        """Computes Covariance, Correlation Matrices, and Feature Importance via variance."""
        cov_matrix = self.df[self.numeric_cols].cov()
        corr_matrix = self.df[self.numeric_cols].corr()

        # Variance-based feature ordering
        variances = self.df[self.feature_cols].var().sort_values(ascending=False)

        return {
            "Covariance Matrix": cov_matrix.round(4),
            "Correlation Matrix": corr_matrix.round(4),
            "Feature Variance Ranking": variances.round(4).to_dict(),
        }

    # ==========================================
    # 5. Linear Algebra & Mathematical Analysis
    # ==========================================
    def compute_linear_algebra_foundation(self) -> dict:
        """Calculates Matrix Rank, Condition Number, Eigendecomposition, and OLS Weights."""
        X = self.df[self.feature_cols].values
        # Add intercept column for OLS: [1, X]
        X_design = np.hstack([np.ones((X.shape[0], 1)), X])
        y = self.df[self.target_col].values.reshape(-1, 1)

        # 1. Matrix Condition & Stability
        rank = np.linalg.matrix_rank(X_design)
        cond_num = np.linalg.cond(X_design)

        # 2. Eigen Inspection of Covariance Matrix (X^T * X)
        AtA = X_design.T @ X_design
        eigenvalues, eigenvectors = np.linalg.eig(AtA)

        # 3. Closed-Form Ordinary Least Squares (OLS): beta = (X^T * X)^(-1) * X^T * y
        beta = np.linalg.pinv(AtA) @ X_design.T @ y

        # 4. Residual & Variance Analysis
        y_pred = X_design @ beta
        residuals = y - y_pred
        rss = float(np.sum(residuals**2))
        tss = float(np.sum((y - np.mean(y)) ** 2))
        r2_score = 1.0 - (rss / tss)

        return {
            "Design Matrix Rank": rank,
            "Matrix Condition Number": round(cond_num, 4),
            "Eigenvalues of (X^T * X)": np.round(eigenvalues, 4).tolist(),
            "OLS Weights (Intercept + Features)": np.round(
                beta.flatten(), 4
            ).tolist(),
            "Residual Sum of Squares (RSS)": round(rss, 4),
            "R-squared Score (R^2)": round(r2_score, 4),
        }


# ==========================================
# Driver Code & Verification
# ==========================================
if __name__ == "__main__":
    print("==================================================================")
    print("      AI ENGINEER FOUNDATION ANALYTICS SYSTEM (CAPSTONE DAY 50)   ")
    print("==================================================================\n")

    # Synthetic Dataset Generation (100 Samples x 4 Numeric Features)
    np.random.seed(42)
    n_samples = 100

    f1 = np.random.normal(loc=50, scale=10, size=n_samples)
    f2 = 2.5 * f1 + np.random.normal(loc=0, scale=5, size=n_samples)
    f3 = np.random.uniform(low=1, high=100, size=n_samples)
    target = 1.5 * f1 + 0.8 * f2 - 0.5 * f3 + np.random.normal(0, 3, size=n_samples)

    # Introduce some artificial missing values & anomalies for testing
    f1[5] = np.nan
    f3[12] = np.nan

    raw_df = pd.DataFrame(
        {"Feature_1": f1, "Feature_2": f2, "Feature_3": f3, "Target": target}
    )

    # Initialize Engine
    system = AIEngineerFoundationAnalyticsSystem(
        raw_data=raw_df, target_column="Target"
    )

    # Step 1: Preprocessing
    df_clean = system.preprocess_pipeline()
    print(f"[1] Preprocessing Complete: Cleaned Dataset Shape -> {df_clean.shape}")

    # Step 2: Descriptive Statistics
    print("\n--- [2] Descriptive Statistics & Distribution Diagnostics ---")
    stats_df = system.compute_statistical_diagnostics()
    print(stats_df[["Mean", "Std Dev", "IQR", "Skewness", "Kurtosis"]].round(4))

    # Step 3: Probability & Hypothesis Testing
    print("\n--- [3] Probability & Hypothesis Testing ---")
    prob_results = system.run_probability_and_hypothesis_tests()
    print("Target Normality:", prob_results["Target Normality (Shapiro-Wilk)"])
    print("Correlations with Target:")
    for feat, metrics in prob_results["Feature Correlations with Target"].items():
        print(f"  {feat:<12}: r = {metrics['Pearson r']}, p = {metrics['p-value']}")

    # Step 4: EDA Insights
    print("\n--- [4] Exploratory Data Analysis (EDA Summary) ---")
    eda_summary = system.generate_eda_summary()
    print("Feature Variance Ranking:", eda_summary["Feature Variance Ranking"])

    # Step 5: Linear Algebra & Mathematical Foundation
    print("\n--- [5] Linear Algebra & OLS Mathematical Foundation ---")
    linalg_res = system.compute_linear_algebra_foundation()
    for k, v in linalg_res.items():
        print(f"  {k:<36}: {v}")