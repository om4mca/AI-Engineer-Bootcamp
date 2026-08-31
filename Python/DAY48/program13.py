import numpy as np

class EmployeeSalaryAnalyzer:
    def __init__(self):
        self.weights = None
        self.feature_names = []
        
    def fit(self, X_data: np.ndarray, y_data: np.ndarray, feature_names: list):
        """
        Fits the least-squares regression model using np.linalg.lstsq.
        """
        self.feature_names = ["Intercept"] + feature_names
        m = len(y_data)
        
        # 1. Build Design Matrix X (Shape: m x (n + 1))
        bias_column = np.ones((m, 1), dtype=np.float64)
        self.X = np.hstack([bias_column, X_data])
        self.y = y_data.astype(np.float64)
        
        # 2. Solve Least Squares via SVD: w = (X^T X)^(-1) X^T y
        self.weights, self.rss_lstsq, self.rank, self.singular_vals = np.linalg.lstsq(
            self.X, self.y, rcond=None
        )
        
        # 3. Compute Predictions and Residual Analytics
        self.y_hat = self.X @ self.weights
        self.residuals = self.y - self.y_hat
        self.rss = np.sum(self.residuals**2)
        self.mse = np.mean(self.residuals**2)
        self.rmse = np.sqrt(self.mse)
        self.mape = np.mean(np.abs(self.residuals / self.y)) * 100
        
    def summary(self):
        """Displays full analytical breakdown of model performance."""
        print("=" * 65)
        print("         EMPLOYEE SALARY LEAST-SQUARES ANALYZER REPORT         ")
        print("=" * 65)
        
        # Matrix Properties
        print("\n--- MATRIX & MODEL PROPERTIES ---")
        print(f"Design Matrix Shape (X)  : {self.X.shape[0]} samples x {self.X.shape[1]} parameters")
        print(f"Matrix Rank              : {self.rank}")
        print(f"Condition Number         : {np.linalg.cond(self.X):.4f}")
        
        # Learned Parameters
        print("\n--- LEARNED PARAMETERS (WEIGHTS) ---")
        for name, weight in zip(self.feature_names, self.weights):
            print(f"  • {name:<20} : ${weight:,.2f}")
            
        # Sample Predictions & Residual Breakdown
        print("\n--- INDIVIDUAL PREDICTION ANALYSIS ---")
        header = f"{'ID':^5}|{'Actual ($)':^14}|{'Predicted ($)':^14}|{'Residual ($)':^14}|{'Abs Error %':^12}"
        print(header)
        print("-" * len(header))
        for i in range(len(self.y)):
            print(f"{i+1:^5}|${self.y[i]:^13,.2f}|${self.y_hat[i]:^13,.2f}|${self.residuals[i]:^13,.2f}|{np.abs(self.residuals[i]/self.y[i])*100:^11.2f}%")
            
        # Error Metrics
        print("\n--- GLOBAL PERFORMANCE METRICS ---")
        print(f"  • Sum of Residuals (e)  : {np.sum(self.residuals):.4e} (≈ 0)")
        print(f"  • Residual Sum Sq (RSS) : {self.rss:,.2f}")
        print(f"  • Mean Squared Err (MSE): {self.mse:,.2f}")
        print(f"  • Root Mean Sq Err (RMSE): ${self.rmse:,.2f}")
        print(f"  • Mean Abs Pct Err (MAPE): {self.mape:.2f}%")
        print("=" * 65)

    def predict(self, new_features: np.ndarray) -> np.ndarray:
        """Predicts salary for new employee data array."""
        bias = np.ones((len(new_features), 1))
        X_new = np.hstack([bias, new_features])
        return X_new @ self.weights


# =====================================================================
# RUNNING THE SALARY ANALYZER
# =====================================================================

# Features: [Experience (Years), Performance Rating (1-10)]
X_employee_data = np.array([
    [1.5, 6.0],
    [3.0, 7.5],
    [4.5, 7.0],
    [6.0, 8.5],
    [8.0, 9.0],
    [10.0, 9.5]
])

# Actual Salaries ($ in thousands or exact values)
y_salary_data = np.array([52000, 64000, 71000, 88000, 105000, 122000])

# Initialize and Fit Analyzer
analyzer = EmployeeSalaryAnalyzer()
analyzer.fit(X_employee_data, y_salary_data, feature_names=["Experience (Yrs)", "Performance (1-10)"])
analyzer.summary()