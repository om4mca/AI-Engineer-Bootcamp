import numpy as np

def hospital_least_squares_analyzer(stay_days: list, age: list, bills_actual: list):
    """
    Analyzes hospital billing data using Ordinary Least Squares (OLS) regression.
    
    Pipeline:
    Feature Matrix -> np.linalg.lstsq() -> Parameters -> Predictions -> Residuals -> RSS & MSE
    """
    # 1. Target Vector (y)
    y = np.array(bills_actual, dtype=np.float64)
    
    # 2. Build Feature Matrix (X): [Bias (1s), Length of Stay (days), Patient Age (years)]
    X = np.column_stack([
        np.ones(len(stay_days)),
        stay_days,
        age
    ])
    
    # 3. Solve Least Squares: np.linalg.lstsq
    # Computes weights w that minimize ||Xw - y||^2
    weights, _, rank, singular_values = np.linalg.lstsq(X, y, rcond=None)
    
    # 4. Predictions: y_hat = X @ w
    predictions = X @ weights
    
    # 5. Residual Analysis: e = y - y_hat
    residuals = y - predictions
    
    # 6. Metrics: RSS and MSE
    RSS = np.sum(residuals**2)
    MSE = np.mean(residuals**2)
    
    # --- DISPLAY RESULTS ---
    print("==================================================")
    print("       HOSPITAL DATA LEAST-SQUARES ANALYZER       ")
    print("==================================================")
    
    print("\n1. Feature Matrix (X) [Bias, Stay Days, Age]:")
    print(X)
    
    print("\n2. Target Vector (y) [Actual Bills ($)]:")
    print(y)
    
    print("\n3. Calculated Parameters / Weights (w):")
    print(f"  • Base Admission Cost (w0) : ${weights[0]:.2f}")
    print(f"  • Per-Day Rate (w1)         : ${weights[1]:.2f} / day")
    print(f"  • Age Weight (w2)           : ${weights[2]:.2f} / year")
    
    print("\n4. Predictions (ŷ = X @ w):")
    print(np.round(predictions, 2))
    
    print("\n5. Residual Analysis (e = y - ŷ):")
    print(np.round(residuals, 2))
    
    print("\n6. Performance Metrics & Diagnostics:")
    print(f"  • Matrix Rank (X) : {rank}")
    print(f"  • RSS             : {RSS:.2f}")
    print(f"  • MSE             : {MSE:.2f}")

# =====================================================================
# NUMERICAL DATASET
# =====================================================================
# Features: Length of Stay (days), Patient Age (years)
stay = [2, 3, 5, 7, 8]
patient_age = [35, 45, 52, 60, 68]
actual_bills = [4500, 6200, 9800, 13100, 15400]  # Total hospital bill in $

hospital_least_squares_analyzer(stay, patient_age, actual_bills)