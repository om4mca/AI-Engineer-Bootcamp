import numpy as np
import pandas as pd

def analyze_patient_ages(ages):
    """
    Computes statistical metrics and identifies age outliers for hospital patients.
    """
    age_series = pd.Series(ages, name="Age")
    n = len(age_series)
    
    if n == 0:
        print("❌ Dataset is empty.")
        return

    # --- 1. Central Tendency ---
    mean_val = age_series.mean()
    median_val = age_series.median()
    
    # Mode calculation
    mode_series = age_series.mode()
    mode_str = ", ".join([f"{x} yrs" for x in mode_series]) if len(mode_series) < n else "No Mode"

    # --- 2. Range & Dispersion ---
    min_val = int(age_series.min())
    max_val = int(age_series.max())
    age_range = max_val - min_val
    sample_var = age_series.var(ddof=1)
    sample_std = age_series.std(ddof=1)

    # --- 3. Quartiles & IQR ---
    q1 = age_series.quantile(0.25)
    q2 = median_val
    q3 = age_series.quantile(0.75)
    iqr = q3 - q1

    # --- 4. Outlier Identification (1.5x IQR Rule) ---
    lower_bound = max(0, q1 - (1.5 * iqr))  # Age cannot be negative
    upper_bound = q3 + (1.5 * iqr)
    
    outliers = age_series[(age_series < lower_bound) | (age_series > upper_bound)].tolist()

    # --- 5. Demography / Age Brackets Breakdown ---
    pediatric = (age_series < 18).sum()
    adult = ((age_series >= 18) & (age_series < 65)).sum()
    geriatric = (age_series >= 65).sum()

    # --- Display Summary Report ---
    print("=" * 55)
    print("          🏥 HOSPITAL PATIENT AGE STATISTICAL REPORT          ")
    print("=" * 55)
    print(f"Total Patients (n)       : {n}")
    print(f"Youngest Patient         : {min_val} years old")
    print(f"Oldest Patient           : {max_val} years old")
    print("-" * 55)
    print(f"Mean Age (Average)       : {mean_val:.1f} years")
    print(f"Median Age (Midpoint)    : {median_val:.1f} years")
    print(f"Mode Age                 : {mode_str}")
    print("-" * 55)
    print(f"Age Range                : {age_range} years")
    print(f"Sample Variance          : {sample_var:.2f}")
    print(f"Sample Standard Dev (s)  : {sample_std:.2f} years")
    print("-" * 55)
    print(f"Q1 (25th Percentile)     : {q1:.1f} years")
    print(f"Q2 (50th / Median)       : {q2:.1f} years")
    print(f"Q3 (75th Percentile)     : {q3:.1f} years")
    print(f"Interquartile Range(IQR) : {iqr:.1f} years")
    print("-" * 55)
    print("--- Clinical Age Demographics ---")
    print(f"Pediatric  (<18)         : {pediatric} ({pediatric/n*100:.1f}%)")
    print(f"Adult      (18-64)       : {adult} ({adult/n*100:.1f}%)")
    print(f"Geriatric  (65+)         : {geriatric} ({geriatric/n*100:.1f}%)")
    print("-" * 55)
    print(f"Outlier Thresholds       : [{lower_bound:.1f}, {upper_bound:.1f}] yrs")
    print(f"Age Outliers Detected    : {outliers if outliers else 'None'}")
    print("=" * 55)

# --- Sample Dataset ---
# Sample ages including pediatric cases, adults, elderly, and an outlier (115)
patient_ages = [
    3, 12, 24, 29, 31, 35, 42, 45, 48, 
    52, 56, 61, 67, 72, 78, 81, 115
]

if __name__ == "__main__":
    analyze_patient_ages(patient_ages)