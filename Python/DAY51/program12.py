import pandas as pd
import numpy as np

# Sample dataset total counts
total_samples = 1250
train_samples = 1000
test_samples = 250

# -------------------------------------------------------------------
# 1. CALCULATE PROPORTIONS FROM SAMPLE COUNTS
# -------------------------------------------------------------------
train_pct = (train_samples / total_samples) * 100
test_pct = (test_samples / total_samples) * 100

print("--- 1. PROPORTION FROM COUNTS ---")
print(f"Total Samples : {total_samples}")
print(f"Train Ratio   : {train_samples}/{total_samples} -> {train_pct:.2f}%")
print(f"Test Ratio    : {test_samples}/{total_samples}  -> {test_pct:.2f}%")


# -------------------------------------------------------------------
# 2. CALCULATE SAMPLE SIZES FROM A TARGET RATIO (e.g., 80/20)
# -------------------------------------------------------------------
target_test_ratio = 0.20  # 20% test split

calculated_test_size = int(total_samples * target_test_ratio)
calculated_train_size = total_samples - calculated_test_size

print("\n--- 2. SAMPLE SIZES FROM 80/20 SPLIT RATIO ---")
print(f"Calculated Train Count : {calculated_train_size} ({(calculated_train_size/total_samples)*100:.1f}%)")
print(f"Calculated Test Count  : {calculated_test_size} ({(calculated_test_size/total_samples)*100:.1f}%)")


# -------------------------------------------------------------------
# 3. VERIFY SPLIT PROPORTIONS ON REAL ARRAYS / DATAFRAMES
# -------------------------------------------------------------------
# Dummy Feature Matrix X (1000 rows, 4 features)
X = np.zeros((1000, 4))

# Simulating an 80/20 manual split
split_index = int(len(X) * 0.80)
X_train, X_test = X[:split_index], X[split_index:]

total_len = len(X)
train_ratio = len(X_train) / total_len
test_ratio = len(X_test) / total_len

print("\n--- 3. ARRAY SPLIT VERIFICATION ---")
print(f"X_train Proportion : {train_ratio:.4f} ({train_ratio * 100:.1f}%)")
print(f"X_test Proportion  : {test_ratio:.4f} ({test_ratio * 100:.1f}%)")