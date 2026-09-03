import pandas as pd
import numpy as np

def detect_data_leakage(df, target_col, train_indices, test_indices, correlation_threshold=0.90):
    """
    Programmatically detects potential data leakage risks in a dataset pipeline.
    """
    features_only = [c for c in df.columns if c != target_col]
    train_df = df.iloc[train_indices]
    test_df = df.iloc[test_indices]
    
    warnings = []
    
    # 1. Detect Direct Feature Leakage (Unusually high correlation with target)
    if pd.api.types.is_numeric_dtype(df[target_col]):
        correlations = df[features_only].apply(
            lambda x: x.corr(df[target_col]) if pd.api.types.is_numeric_dtype(x) else 0
        )
        high_corr = correlations[abs(correlations) >= correlation_threshold]
        for col in high_corr.index:
            warnings.append(
                f"⚠️ FEATURE LEAKAGE: '{col}' has a {correlations[col]:.4f} correlation with target."
            )

    # 2. Detect Train-Test Contamination (Duplicate feature rows across split)
    duplicates = pd.merge(train_df[features_only], test_df[features_only], how='inner').shape[0]
    if duplicates > 0:
        warnings.append(
            f"⚠️ DATA CONTAMINATION: {duplicates} identical feature rows exist in BOTH Train and Test sets."
        )

    # 3. Detect ID / High Cardinality Leakage (Columns with unique values per row)
    for col in features_only:
        if df[col].nunique() == len(df):
            warnings.append(
                f"⚠️ UNIQUE ID LEAKAGE: '{col}' is a unique row identifier that should be dropped."
            )

    # Print Report
    print("--- DATA LEAKAGE ANALYSIS REPORT ---")
    if warnings:
        for w in warnings:
            print(w)
    else:
        print("✅ No immediate data leakage indicators detected.")
    print("-" * 50)


# --- Example Test Setup ---
np.random.seed(42)
n_samples = 100

df = pd.DataFrame({
    'Patient_ID': np.arange(1000, 1000 + n_samples),             # ID column
    'Age': np.random.randint(20, 80, n_samples),                   # Valid feature
    'Readmitted': np.random.choice([0, 1], n_samples),             # Target (y)
})

# Injecting post-outcome feature (Direct Leakage)
df['Discharge_Code'] = df['Readmitted'] * 5.0 + np.random.normal(0, 0.01, n_samples)

# Indices with intentional overlap (Contamination Leakage)
train_idx = list(range(0, 80))
test_idx = list(range(75, 100))  # Indices 75-79 overlap

detect_data_leakage(df, target_col='Readmitted', train_indices=train_idx, test_indices=test_idx)