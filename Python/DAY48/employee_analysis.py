import numpy as np

def employee_salary_analyzer(experience_years: list, base_performance: list, salary_actual: list):
    """
    Analyzes employee salary data using Ordinary Least Squares (OLS) regression.
    Pipeline: Input Data -> Feature Matrix -> OLS -> Weights -> Predictions -> Residuals -> Metrics
    """
    # 1. Convert Inputs to NumPy Arrays
    y = np.array(salary_actual, dtype=np.float64)
    
    # 2. Build Feature Matrix X (Bias Column + Features)
    # Includes Intercept (Bias = 1), Experience Years, and Performance Rating
    X = np.column_stack([
        np.ones(len(experience_years)),
        experience_years,
        base_performance
    ])
    
    # 3. Solve Least Squares: np.linalg.lstsq
    # Computes weights w that minimize ||Xw - y||^2
    weights, residuals_lstsq, rank, singular_values = np.linalg.lstsq(X, y, rcond=None)
    
    # 4. Predictions: y_hat = X @ w
    predictions = X @ weights
    
    # 5. Residuals: e = y - y_hat
    residuals = y - predictions
    
    # 6. Metrics: RSS and MSE
    RSS = np.sum(residuals**2)
    MSE = np.mean(residuals**2)
    
    # --- DISPLAY OUTPUTS ---
    print("==================================================")
    print("      EMPLOYEE SALARY LEAST-SQUARES ANALYZER      ")
    print("==================================================")
    
    print("\n1. Feature Matrix (X) [Bias, Experience, Performance]:")
    print(X)
    
    print("\n2. Model Parameters / Weights (w):")
    print(f"  • Bias / Base Salary (w0)    : ${weights[0]:.4f}k")
    print(f"  • Experience Weight (w1)     : ${weights[1]:.4f}k per year")
    print(f"  • Performance Weight (w2)    : ${weights[2]:.4f}k per rating pt")
    
    print("\n3. Target Vector vs. Predictions (y vs. ŷ):")
    for i, (actual, pred) in enumerate(zip(y, predictions)):
        print(f"  • Emp {i+1}: Actual = ${actual:.2f}k | Predicted = ${pred:.2f}k")
        
    print("\n4. Residuals (e = y - ŷ):")
    print(np.round(residuals, 4))
    
    print("\n5. Performance Metrics & Matrix Rank:")
    print(f"  • Matrix Rank (X) : {rank}")
    print(f"  • RSS             : {RSS:.4f}")
    print(f"  • MSE             : {MSE:.4f}")
    
    return {
        "weights": weights,
        "predictions": predictions,
        "residuals": residuals,
        "RSS": RSS,
        "MSE": MSE,
        "rank": rank
    }

# =====================================================================
# DATASET INPUT
# =====================================================================
# Features: Experience (years), Performance Rating (1-5 scale)
exp = [1.5, 3.0, 4.5, 6.0, 8.0]
perf = [3.0, 4.0, 3.5, 5.0, 4.5]
salaries = [45.0, 58.0, 65.0, 88.0, 95.0]  # Actual salaries in $1,000s

employee_salary_analyzer(exp, perf, salaries)