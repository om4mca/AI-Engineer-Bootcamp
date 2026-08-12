import numpy as np
import pandas as pd

def complete_statistical_analysis(df, numeric_cols=None, alpha=0.05):
    """
    Performs a comprehensive univariate and bivariate statistical analysis
    on numerical columns in a Pandas DataFrame without requiring external packages.
    """
    if numeric_cols is None:
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

    if not numeric_cols:
        print("❌ No numeric columns found in the dataset.")
        return

    report = []

    for col in numeric_cols:
        series = df[col].dropna()
        n = len(series)
        
        if n < 2:
            continue

        # --- 1. Central Tendency ---
        mean_val = series.mean()
        median_val = series.median()
        mode_series = series.mode()
        mode_val = mode_series.iloc[0] if len(mode_series) < n else "No Mode"
        
        # 10% Trimmed Mean (removes top/bottom 10% extreme values)
        p10, p90 = series.quantile(0.10), series.quantile(0.90)
        trimmed_mean = series[(series >= p10) & (series <= p90)].mean()

        # --- 2. Dispersion & Spread ---
        min_val = series.min()
        max_val = series.max()
        val_range = max_val - min_val
        sample_var = series.var(ddof=1)
        sample_std = series.std(ddof=1)
        cv = (sample_std / mean_val) * 100 if mean_val != 0 else np.nan  # Coefficient of Variation (%)

        # --- 3. Quartiles & IQR ---
        q1 = series.quantile(0.25)
        q2 = median_val
        q3 = series.quantile(0.75)
        iqr = q3 - q1

        # --- 4. Outliers (1.5x IQR Rule) ---
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        outliers = series[(series < lower_bound) | (series > upper_bound)]
        outlier_count = len(outliers)
        outlier_pct = (outlier_count / n) * 100

        # --- 5. Distribution Shape ---
        skewness = series.skew()
        kurtosis = series.kurtosis()
        
        # Distribution Classification
        if abs(skewness) < 0.5:
            skew_label = "Symmetric"
        elif skewness >= 0.5:
            skew_label = "Right-Skewed (Positive)"
        else:
            skew_label = "Left-Skewed (Negative)"

        report.append({
            'Feature': col,
            'Count (n)': n,
            'Mean': round(mean_val, 2),
            'Trimmed Mean (10%)': round(trimmed_mean, 2),
            'Median (Q2)': round(median_val, 2),
            'Mode': round(mode_val, 2) if isinstance(mode_val, (int, float)) else mode_val,
            'Std Dev (s)': round(sample_std, 2),
            'Variance (s²)': round(sample_var, 2),
            'Coeff of Var (%)': round(cv, 2),
            'Min': round(min_val, 2),
            'Q1 (25%)': round(q1, 2),
            'Q3 (75%)': round(q3, 2),
            'Max': round(max_val, 2),
            'IQR': round(iqr, 2),
            'Outlier Count': outlier_count,
            'Outlier %': f"{outlier_pct:.1f}%",
            'Skewness': round(skewness, 2),
            'Kurtosis': round(kurtosis, 2),
            'Shape': skew_label
        })

    summary_df = pd.DataFrame(report).set_index('Feature')

    # Print Report
    print("=" * 80)
    print("                  📊 COMPLETE STATISTICAL SUMMARY REPORT                  ")
    print("=" * 80)
    print(summary_df.T)  # Transposed for easy vertical scanning
    print("=" * 80)

    # --- 6. Bivariate Analysis: Pearson Correlation Matrix ---
    print("\n--- 🔗 Pearson Correlation Matrix ---")
    corr_matrix = df[numeric_cols].corr(method='pearson')
    print(corr_matrix.round(3))
    
    return summary_df, corr_matrix

# --- Sample Dataset Execution ---
if __name__ == "__main__":
    # Generating synthetic healthcare/employee data
    np.random.seed(42)
    sample_data = pd.DataFrame({
        'Age': np.random.randint(20, 65, size=100),
        'Salary': np.append(np.random.normal(60000, 12000, 95), [250000, 280000, 300000, 15000, 12000]), # Has extreme outliers
        'Experience_Yrs': np.random.uniform(1, 25, size=100),
        'Projects_Completed': np.random.poisson(lam=5, size=100)
    })

    stats_summary, correlation = complete_statistical_analysis(sample_data)