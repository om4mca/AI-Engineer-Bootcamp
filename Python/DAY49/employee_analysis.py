import numpy as np

# Set print precision for clean mathematical output
np.set_printoptions(precision=4, suppress=True)

class EmployeeAlgebraSystem:
    """
    Educational Linear Algebra Analysis Pipeline for Employee Feature Engineering,
    Spectral Decomposition, System Solving, and Least Squares Optimization.
    """
    def __init__(self, raw_data: np.ndarray, salary_data: np.ndarray, feature_names: list):
        self.raw_data = raw_data.astype(np.float64)
        self.y = salary_data.astype(np.float64)
        self.feature_names = feature_names
        
        # Build Design Matrix X (Prepend intercept column of 1s)
        self.m, self.n = raw_data.shape
        self.X = np.hstack([np.ones((self.m, 1)), self.raw_data])
        
    def run_pipeline(self):
        print("=" * 70)
        print("   EDUCATIONAL EMPLOYEE LINEAR ALGEBRA INTELLIGENCE SYSTEM")
        print("=" * 70)
        
        # 1. MATRIX PROPERTIES & SHAPE
        print("\n[1] DESIGN MATRIX PROPERTIES")
        print("-" * 40)
        print(f"Design Matrix (X) Shape : {self.X.shape} ({self.m} samples x {self.n + 1} parameters)")
        print(f"Target Vector (y) Shape : {self.y.shape}")
        
        # 2. MATRIX RANK & Gram Matrix Analysis
        rank = np.linalg.matrix_rank(self.X)
        print(f"Matrix Rank Rank(X)     : {rank}")
        if rank == self.n + 1:
            print("Rank Status             : FULL COLUMN RANK (Columns linearly independent)")
        else:
            print("Rank Status             : RANK DEFICIENT (Multicollinearity present)")
            
        # 3. GRAM MATRIX (X^T X), DETERMINANT, & SPECTRAL DECOMPOSITION
        print("\n[2] GRAM MATRIX (X^T X) & SPECTRAL PROPERTIES")
        print("-" * 40)
        Gram = self.X.T @ self.X
        det_Gram = np.linalg.det(Gram)
        eigenvalues, eigenvectors = np.linalg.eig(Gram)
        
        print(f"Gram Matrix (X^T X) Shape : {Gram.shape}")
        print(f"Determinant det(X^T X)    : {det_Gram:.4e}")
        print(f"Gram Matrix Invertible?  : {'YES' if det_Gram != 0 else 'NO'}")
        print("\nEigenvalues (λ) of (X^T X):")
        for i, val in enumerate(eigenvalues):
            print(f"  λ_{i+1} = {val:12.4f}")
            
        print("\nEigenvectors Matrix (V) of (X^T X):")
        print(eigenvectors)

        # 4. LINEAR SYSTEM SOLVER (Symmetric 2x2 Subsystem for exact solving)
        print("\n[3] EXACT LINEAR SYSTEM SOLVER (Subsystem Ax = b)")
        print("-" * 40)
        # Extract a 2x2 deterministic feature matrix from the first 2 features/rows
        A = Gram[:2, :2]
        b_vec = (self.X.T @ self.y)[:2]
        sol_x = np.linalg.solve(A, b_vec)
        verified = np.allclose(A @ sol_x, b_vec)
        
        print("Subsystem A (2x2 Gram Block):\n", A)
        print("Subsystem Projection Vector b:", b_vec)
        print("Exact Solution x              :", sol_x.round(4))
        print("Verification (A @ x == b)     :", verified)

        # 5. ORDINARY LEAST SQUARES REGRESSION
        print("\n[4] ORDINARY LEAST SQUARES OPTIMIZATION")
        print("-" * 40)
        # Closed-form solution via SVD-backed lstsq
        weights, _, _, _ = np.linalg.lstsq(self.X, self.y, rcond=None)
        
        labels = ["Intercept (w0)"] + self.feature_names
        print("Learned Parameter Weights (w):")
        for label, w in zip(labels, weights):
            print(f"  • {label:<22} : {w:10.4f}")

        # 6. PREDICTIONS & RESIDUAL ANALYSIS
        print("\n[5] PREDICTION & RESIDUAL ANALYSIS")
        print("-" * 40)
        y_hat = self.X @ weights
        residuals = self.y - y_hat
        
        rss = np.sum(residuals**2)
        mse = np.mean(residuals**2)
        
        header = f"{'Sample':^8}|{'Actual (y)':^12}|{'Predicted (ŷ)':^14}|{'Residual (e)':^14}"
        print(header)
        print("-" * len(header))
        for i in range(self.m):
            print(f"{i+1:^8}|{self.y[i]:^12.2f}|{y_hat[i]:^14.2f}|{residuals[i]:^14.4f}")
            
        print("-" * len(header))
        print(f"Sum of Residuals (∑e)   : {np.sum(residuals):.4e} (Orthogonality Proof: X^T e ≈ 0)")
        print(f"Residual Sum Sq (RSS)   : {rss:.4f}")
        print(f"Mean Squared Error (MSE): {mse:.4f}")
        print("=" * 70)

# =====================================================================
# SAMPLE DEMONSTRATION DATASET
# =====================================================================
# Features: [Years Experience, Training Modules Completed, Performance Score (1-10)]
raw_features = np.array([
    [1.5, 4, 6.0],
    [3.0, 6, 7.5],
    [4.5, 5, 7.0],
    [6.0, 8, 8.5],
    [8.0, 9, 9.0],
    [10.0, 10, 9.5]
])

# Actual Salaries (in $1,000s)
salaries = np.array([52.0, 64.0, 71.0, 88.0, 105.0, 122.0])

feature_labels = ["Experience (Yrs)", "Training Modules", "Performance Score"]

# Run the system
system = EmployeeAlgebraSystem(raw_features, salaries, feature_labels)
system.run_pipeline()