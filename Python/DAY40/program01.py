import numpy as np
import pandas as pd
from scipy import stats

# ==============================================================================
# 1. BASIC COMPUTATION (NUMPY & PANDAS)
# ==============================================================================
data = [12, 15, 18, 14, 16, 15, 100]  # Note: 100 is an outlier

# Pure NumPy
mean_val = np.mean(data)
median_val = np.median(data)

print("--- BASIC CALCULATION ---")
print(f"Dataset: {data}")
print(f"Mean:   {mean_val:.2f}  (Pulled upward by the outlier '100')")
print(f"Median: {median_val:.2f}  (Robust center point)")


# ==============================================================================
# 2. PANDAS DATAFRAME & SKEWNESS ANALYSIS
# ==============================================================================
# Sample dataset with symmetric vs. skewed distributions
df = pd.DataFrame({
    'Symmetric_Scores': [70, 75, 80, 85, 90, 95, 100],        # Mean ≈ Median
    'Right_Skewed_Income': [35000, 40000, 42000, 45000, 50000, 120000, 350000] # Mean > Median
})

# Calculate summary stats
summary = pd.DataFrame({
    'Mean': df.mean(),
    'Median': df.median(),
    'Skewness': df.skew()  # Positive = Right-skewed, Negative = Left-skewed
})

# Determine Distribution Shape
summary['Distribution_Shape'] = summary.apply(
    lambda row: 'Right-Skewed (Mean > Median)' if row['Mean'] > row['Median'] 
    else ('Left-Skewed (Mean < Median)' if row['Mean'] < row['Median'] else 'Symmetric'),
    axis=1
)

print("\n--- DATAFRAME ANALYSIS & SKEWNESS ---")
print(summary.to_string())


# ==============================================================================
# 3. HANDLING MISSING DATA (NaNs)
# ==============================================================================
data_with_nan = [10, 20, np.nan, 30, 40]

# Standard NumPy functions return NaN if missing values exist
# Use nanmean and nanmedian to ignore NaNs automatically:
clean_mean = np.nanmean(data_with_nan)
clean_median = np.nanmedian(data_with_nan)

print("\n--- HANDLING MISSING VALUES ---")
print(f"Dataset with NaNs: {data_with_nan}")
print(f"Ignored-NaN Mean:   {clean_mean:.2f}")
print(f"Ignored-NaN Median: {clean_median:.2f}")


# ==============================================================================
# 4. GROUPED MEAN & MEDIAN ANALYSIS (BY CATEGORY)
# ==============================================================================
employee_df = pd.DataFrame({
    'Department': ['Sales', 'Sales', 'Sales', 'IT', 'IT', 'IT'],
    'Salary': [50000, 52000, 150000, 80000, 85000, 90000]
})

# Groupby calculation
grouped_analysis = employee_df.groupby('Department')['Salary'].agg(
    Mean_Salary='mean',
    Median_Salary='median',
    Difference=lambda x: x.mean() - x.median()
).reset_index()

print("\n--- GROUPED DEPARTMENT ANALYSIS ---")
print(grouped_analysis.to_string(index=False))