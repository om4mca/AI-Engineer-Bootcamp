import numpy as np

# =====================================================================
# STEP 1: DATA CREATION & PREPARATION
# =====================================================================
def create_dataset(n_samples=100, seed=42):
    """Generates synthetic housing data (Square Feet, Bedrooms) and Price."""
    np.random.seed(seed)
    sqft = np.random.randint(800, 3500, size=(n_samples, 1))
    bedrooms = np.random.randint(1, 6, size=(n_samples, 1))
    
    # Target formula: Price = 150*SqFt + 10000*Bedrooms + Noise
    noise = np.random.normal(0, 10000, size=(n_samples, 1))
    y = (sqft * 150) + (bedrooms * 10000) + noise
    
    # Combine features into X matrix
    X = np.hstack((sqft, bedrooms))
    return X, y.ravel()

# =====================================================================
# STEP 2: FEATURE SCALING (Standardization)
# =====================================================================
def scale_features(X_train, X_test):
    """Scales features to mean=0, std=1 (fitted ONLY on X_train to prevent leakage)."""
    mean = np.mean(X_train, axis=0)
    std = np.std(X_train, axis=0)
    
    X_train_scaled = (X_train - mean) / std
    X_test_scaled = (X_test - mean) / std
    return X_train_scaled, X_test_scaled

# =====================================================================
# STEP 3: TRAIN / TEST SPLIT
# =====================================================================
def train_test_split_manual(X, y, test_ratio=0.2, seed=42):
    """Shuffles and splits feature matrix X and target vector y."""
    np.random.seed(seed)
    n_samples = X.shape[0]
    indices = np.random.permutation(n_samples)
    
    split_idx = int(n_samples * (1 - test_ratio))
    train_idx, test_idx = indices[:split_idx], indices[split_idx:]
    
    return X[train_idx], X[test_idx], y[train_idx], y[test_idx]

# =====================================================================
# STEP 4: MODEL TRAINING (Linear Regression via Normal Equation)
# =====================================================================
def train_linear_regression(X_train, y_train):
    """
    Trains Linear Regression using closed-form analytical solution:
    theta = (X^T * X)^(-1) * X^T * y
    """
    # Add bias column (ones) to X_train
    ones = np.ones((X_train.shape[0], 1))
    X_bias = np.hstack((ones, X_train))
    
    # Closed-form parameters calculation: w = inv(X^T @ X) @ X^T @ y
    weights = np.linalg.inv(X_bias.T @ X_bias) @ X_bias.T @ y_train
    
    bias = weights[0]
    feature_weights = weights[1:]
    return bias, feature_weights

# =====================================================================
# STEP 5: PREDICTION
# =====================================================================
def predict(X, bias, weights):
    """Computes predictions: y_pred = X @ weights + bias"""
    return (X @ weights) + bias

# =====================================================================
# STEP 6: EVALUATION METRICS
# =====================================================================
def evaluate_model(y_true, y_pred):
    """Calculates Mean Absolute Error (MAE) and R² Variance Score."""
    mae = np.mean(np.abs(y_true - y_pred))
    
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    r2 = 1 - (ss_res / ss_tot)
    
    return mae, r2

# =====================================================================
# MAIN PIPELINE EXECUTION
# =====================================================================
def run_ml_pipeline():
    print("--- RUNNING CUSTOM PYTHON ML WORKFLOW PIPELINE ---")
    
    # 1. Generate Data
    X, y = create_dataset(n_samples=200)
    print(f"1. Dataset Prepared    : X shape {X.shape}, y shape {y.shape}")
    
    # 2. Split Dataset
    X_train, X_test, y_train, y_test = train_test_split_manual(X, y, test_ratio=0.2)
    print(f"2. Train/Test Split    : Train ({len(X_train)} samples), Test ({len(X_test)} samples)")
    
    # 3. Scale Features (fit on train, transform both)
    X_train_scaled, X_test_scaled = scale_features(X_train, X_test)
    print("3. Feature Scaling     : Applied Z-score standardization")
    
    # 4. Train Model
    bias, weights = train_linear_regression(X_train_scaled, y_train)
    print(f"4. Model Trained       : Bias = {bias:.2f}, Feature Weights = {np.round(weights, 2)}")
    
    # 5. Predict & Evaluate
    y_pred = predict(X_test_scaled, bias, weights)
    mae, r2 = evaluate_model(y_test, y_pred)
    
    print("\n--- EVALUATION METRICS ---")
    print(f"Mean Absolute Error (MAE) : ${mae:,.2f}")
    print(f"R² Variance Score         : {r2:.4f}")

if __name__ == "__main__":
    run_ml_pipeline()