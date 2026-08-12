import numpy as np
import pandas as pd

def analyze_employee_salaries(salaries, currency="$"):
    """
    Computes summary statistics and identifies salary outliers without scipy.
    """
    salary_series = pd.Series(salaries, name="Salary")
    n = len(salary_series)
    
    if n == 0:
        print("❌ Dataset is empty.")
        return

    # --- 1. Central Tendency ---
    mean_val = salary_series.mean()
    median_val = salary_series.median()
    
    # Mode calculation via Pandas (handles ties automatically)
    mode_series = salary_series.mode()
    mode_str = ", ".join([f"{currency}{x:,.2f}" for x in mode_series]) if len(mode_series) < n else "No Mode (All unique)"

    # --- 2. Dispersion / Spread ---
    min_val = salary_series.min()
    max_val = salary_series.max()
    salary_range = max_val - min_val
    sample_var = salary_series.var(ddof=1)
    sample_std = salary_series.std(ddof=1)

    # --- 3. Quartiles & Relative Position ---
    q1 = salary_series.quantile(0.25)
    q2 = median_val
    q3 = salary_series.quantile(0.75)
    iqr = q3 - q1

    # --- 4. Outlier Identification (1.5x IQR Rule) ---
    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)
    
    outliers = salary_series[(salary_series < lower_bound) | (salary_series > upper_bound)].tolist()
    clean_salaries = salary_series[(salary_series >= lower_bound) & (salary_series <= upper_bound)]

    # --- Display Summary Report ---
    print("=" * 55)
    print("          📊 EMPLOYEE SALARY STATISTICAL REPORT          ")
    print("=" * 55)
    print(f"Total Employees (n)      : {n}")
    print(f"Minimum Salary           : {currency}{min_val:,.2f}")
    print(f"Maximum Salary           : {currency}{max_val:,.2f}")
    print("-" * 55)
    print(f"Mean Salary (Average)    : {currency}{mean_val:,.2f}")
    print(f"Median Salary (Midpoint) : {currency}{median_val:,.2f}")
    print(f"Mode Salary              : {mode_str}")
    print("-" * 55)
    print(f"Salary Range             : {currency}{salary_range:,.2f}")
    print(f"Sample Variance          : {sample_var:,.2f}")
    print(f"Sample Standard Dev (s)  : {currency}{sample_std:,.2f}")
    print("-" * 55)
    print(f"Q1 (25th Percentile)     : {currency}{q1:,.2f}")
    print(f"Q2 (50th / Median)       : {currency}{q2:,.2f}")
    print(f"Q3 (75th Percentile)     : {currency}{q3:,.2f}")
    print(f"Interquartile Range(IQR) : {currency}{iqr:,.2f}")
    print("-" * 55)
    print(f"Outlier Thresholds       : [{currency}{lower_bound:,.2f}, {currency}{upper_bound:,.2f}]")
    print(f"Outliers Detected        : {[f'{currency}{x:,.2f}' for x in outliers] if outliers else 'None'}")
    print(f"Clean Average (no drop)  : {currency}{clean_salaries.mean():,.2f}")
    print("=" * 55)

# --- Sample Dataset ---
# Includes typical workforce salaries + 1 executive outlier ($1,200,000)
employee_data = [
    48000, 52000, 55000, 55000, 58000, 
    62000, 65000, 70000, 72000, 75000, 
    80000, 85000, 90000, 1200000
]

if __name__ == "__main__":
    analyze_employee_salaries(employee_data)