import numpy as np
import pandas as pd
import random

# =====================================================================
# 1. PURE PYTHON / DICTIONARIES IMPLEMENTATION
# =====================================================================
def manual_train_test_split_python(data, test_size=0.2, seed=42):
    random.seed(seed)
    shuffled_data = data.copy()
    random.shuffle(shuffled_data)
    
    split_idx = int(len(shuffled_data) * (1 - test_size))
    train_data = shuffled_data[:split_idx]
    test_data = shuffled_data[split_idx:]
    
    return train_data, test_data

# Sample dataset
dataset_list = [
    {"Age": 45, "BP": 120, "Risk": "Low"},
    {"Age": 62, "BP": 140, "Risk": "High"},
    {"Age": 29, "BP": 115, "Risk": "Low"},
    {"Age": 58, "BP": 135, "Risk": "Medium"},
    {"Age": 71, "BP": 150, "Risk": "High"}
]

py_train, py_test = manual_train_test_split_python(dataset_list, test_size=0.2)
print("--- PURE PYTHON SPLIT ---")
print(f"Train Count: {len(py_train)} | Test Count: {len(py_test)}")


# =====================================================================
# 2. NUMPY IMPLEMENTATION (Matrix X and Vector y)
# =====================================================================
def manual_train_test_split_numpy(X, y, test_size=0.2, seed=42):
    np.random.seed(seed)
    n_samples = X.shape[0]
    
    # Generate shuffled indices
    indices = np.random.permutation(n_samples)
    split_idx = int(n_samples * (1 - test_size))
    
    train_indices = indices[:split_idx]
    test_indices = indices[split_idx:]
    
    X_train, X_test = X[train_indices], X[test_indices]
    y_train, y_test = y[train_indices], y[test_indices]
    
    return X_train, X_test, y_train, y_test

# Sample NumPy Features and Target
X_arr = np.array([[45, 120], [62, 140], [29, 115], [58, 135], [71, 150]])
y_arr = np.array([0, 2, 0, 1, 2])  # Encoded Risk

X_tr, X_te, y_tr, y_te = manual_train_test_split_numpy(X_arr, y_arr, test_size=0.2)
print("\n--- NUMPY SPLIT ---")
print(f"X_train Shape: {X_tr.shape} | X_test Shape: {X_te.shape}")
print(f"y_train Shape: {y_tr.shape} | y_test Shape: {y_te.shape}")


# =====================================================================
# 3. PANDAS DATAFRAME IMPLEMENTATION
# =====================================================================
def manual_train_test_split_pandas(df, target_col, test_size=0.2, seed=42):
    # Shuffle DataFrame rows randomly
    df_shuffled = df.sample(frac=1, random_state=seed).reset_index(drop=True)
    
    split_idx = int(len(df_shuffled) * (1 - test_size))
    
    train_df = df_shuffled.iloc[:split_idx]
    test_df = df_shuffled.iloc[split_idx:]
    
    X_train = train_df.drop(columns=[target_col])
    y_train = train_df[target_col]
    
    X_test = test_df.drop(columns=[target_col])
    y_test = test_df[target_col]
    
    return X_train, X_test, y_train, y_test

# Sample Pandas DataFrame
df_sample = pd.DataFrame({
    'Age': [45, 62, 29, 58, 71],
    'BP': [120, 140, 115, 135, 150],
    'Risk': ['Low', 'High', 'Low', 'Medium', 'High']
})

X_tr_pd, X_te_pd, y_tr_pd, y_te_pd = manual_train_test_split_pandas(df_sample, target_col='Risk', test_size=0.2)
print("\n--- PANDAS SPLIT ---")
print(f"X_train Rows: {len(X_tr_pd)} | X_test Rows: {len(X_te_pd)}")