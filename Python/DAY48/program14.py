import numpy as np

class HospitalDataAnalyzer:
    def __init__(self):
        self.weights = None
        self.feature_names = []
        
    def fit(self, X_data: np.ndarray, y_data: np.ndarray, feature_names: list, target_name: str = "Stay Length (Days)"):
        """
        Fits the least-squares regression model using np.linalg.lstsq.
        """
        self.target_name = target_name
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
        """Displays complete clinical performance readout."""
        print("=" * 70)
        print("           HOSPITAL DATA LEAST-SQUARES ANALYZER REPORT          ")
        print("=" * 70)
        
        # Matrix Properties
        print("\n--- MATRIX & MODEL PROPERTIES ---")
        print(f"Design Matrix Shape (X)  : {self.X.shape[0]} patients x {self.X.shape[1]} parameters")
        print(f"Matrix Rank              : {self.rank}")
        print(f"Condition Number         : {np.linalg.cond(self.X):.4f}")
        
        # Learned Parameters
        print("\n--- CLINICAL PARAMETER WEIGHTS ---")
        for name, weight in zip(self.feature_names, self.weights):
            print(f"  • {name:<22} : {weight:+.4f}")
            
        # Sample Predictions & Residual Breakdown
        print("\n--- INDIVIDUAL PATIENT PREDICTIONS ---")
        header = f"{'Patient':^9}|{'Actual':^12}|{'Predicted':^12}|{'Residual (e)':^14}|{'Abs Error %':^12}"
        print(header)
        print("-" * len(header))
        for i in range(len(self.y)):
            print(f"{i+1:^9}|{self.y[i]:^12.2f}|{self.y_hat[i]:^12.2f}|{self.residuals[i]:^14.4f}|{np.abs(self.residuals[i]/self.y[i])*100:^11.2f}%")
            
        # Error Metrics
        print("\n--- GLOBAL CLINICAL ERROR METRICS ---")
        print(f"  • Residual Sum (e)      : {np.sum(self.residuals):.4e} (≈ 0)")
        print(f"  • Residual Sum Sq (RSS) : {self.rss:.4f}")
        print(f"  • Mean Squared Err (MSE): {self.mse:.4f}")
        print(f"  • Root Mean Sq Err (RMSE): {self.rmse:.4f} {self.target_name.split()[-1][1:-1]}")
        print(f"  • Mean Abs Pct Err (MAPE): {self.mape:.2f}%")
        print("=" * 70)

    def predict(self, new_patient_data: np.ndarray) -> np.ndarray:
        """Predicts hospital outcomes for new patient records."""
        bias = np.ones((len(new_patient_data), 1))
        X_new = np.hstack([bias, new_patient_data])
        return X_new @ self.weights


# =====================================================================
# RUNNING THE HOSPITAL DATA ANALYZER
# =====================================================================

# Clinical Predictors: [Age (Years), Illness Severity (1-10), Comorbidity Index (0-5)]
X_hospital_data = np.array([
    [45, 3.0, 1.0],
    [52, 5.5, 2.0],
    [61, 7.0, 3.0],
    [38, 2.5, 0.0],
    [74, 8.5, 4.0],
    [68, 6.0, 2.0],
    [55, 4.0, 1.0]
])

# Actual Target: Length of Stay in Days (y)
y_length_of_stay = np.array([3.5, 6.0, 9.5, 2.0, 14.0, 8.5, 5.0])

# Initialize and Fit Analyzer
analyzer = HospitalDataAnalyzer()
analyzer.fit(
    X_hospital_data, 
    y_length_of_stay, 
    feature_names=["Age (Yrs)", "Severity (1-10)", "Comorbidity Index"],
    target_name="Stay Length (Days)"
)
analyzer.summary()