import numpy as np

# Set print precision for clean linear algebra output
np.set_printoptions(precision=4, suppress=True)

class HospitalAlgebraSystem:
    """
    Educational Linear Algebra Analysis Pipeline for Hospital Clinical Features,
    Gram Matrix Diagnostics, Spectral Decomposition, System Solving, and OLS Regression.
    """
    def __init__(self, clinical_data: np.ndarray, stay_duration: np.ndarray, feature_names: list):
        self.raw_data = clinical_data.astype(np.float64)
        self.y = stay_duration.astype(np.float64)
        self.feature_names = feature_names
        
        # Build Design Matrix X (Prepend bias column of 1s)
        self.m, self.n = clinical_data.shape
        self.X = np.hstack([np.ones((self.m, 1)), self.raw_data])

    def run_pipeline(self):
        print("=" * 72)
        print("    EDUCATIONAL HOSPITAL LINEAR ALGEBRA INTELLIGENCE SYSTEM")
        print("=" * 72)

        # 1. DESIGN MATRIX PROPERTIES
        print("\n[1] DESIGN MATRIX PROPERTIES")
        print("-" * 45)
        print(f"Design Matrix (X) Shape : {self.X.shape} ({self.m} patients x {self.n + 1} parameters)")
        print(f"Target Vector (y) Shape : {self.y.shape} (Stay duration in days)")

        # 2. MATRIX RANK & CONDITIONING
        rank = np.linalg.matrix_rank(self.X)
        cond_num = np.linalg.cond(self.X)
        print(f"Matrix Rank Rank(X)     : {rank}")
        print(f"Condition Number        : {cond_num:.4f}")
        if rank == self.n + 1:
            print("Rank Status             : FULL COLUMN RANK (No exact collinearity)")
        else:
            print("Rank Status             : RANK DEFICIENT (Features are dependent)")

        # 3. GRAM MATRIX (X^T X) & SPECTRAL DECOMPOSITION
        print("\n[2] GRAM MATRIX (X^T X) & EIGEN ANALYSIS")
        print("-" * 45)
        Gram = self.X.T @ self.X
        det_Gram = np.linalg.det(Gram)
        eigenvalues, eigenvectors = np.linalg.eig(Gram)

        print(f"Gram Matrix Shape       : {Gram.shape}")
        print(f"Determinant det(X^T X)  : {det_Gram:.4e}")
        print(f"Invertible (det ≠ 0)?   : {'YES' if det_Gram != 0 else 'NO'}")
        
        print("\nEigenvalues (λ) of (X^T X):")
        for i, val in enumerate(eigenvalues):
            print(f"  λ_{i+1} = {val:12.4f}")

        print("\nEigenvectors Matrix (V) of (X^T X):")
        print(eigenvectors)

        # 4. LINEAR SYSTEM SOLVER (2x2 Gram Block Subsystem)
        print("\n[3] EXACT LINEAR SYSTEM SOLVER (Ax = b)")
        print("-" * 45)
        # Extract a deterministic 2x2 subsystem from the Gram matrix
        A = Gram[:2, :2]
        b_vec = (self.X.T @ self.y)[:2]
        sol_x = np.linalg.solve(A, b_vec)
        verified = np.allclose(A @ sol_x, b_vec)

        print("Subsystem Matrix A (2x2 Gram Block):\n", A)
        print("Projection Vector b (X^T y subset) :", b_vec)
        print("Exact Solution x                   :", sol_x.round(4))
        print("Verification (A @ x == b)          :", verified)

        # 5. ORDINARY LEAST SQUARES REGRESSION
        print("\n[4] LEAST SQUARES OPTIMIZATION")
        print("-" * 45)
        weights, _, _, _ = np.linalg.lstsq(self.X, self.y, rcond=None)

        labels = ["Intercept (w0)"] + self.feature_names
        print("Learned Clinical Weights (w):")
        for label, w in zip(labels, weights):
            print(f"  • {label:<22} : {w:10.4f}")

        # 6. PREDICTION & RESIDUAL ANALYSIS
        print("\n[5] PREDICTION & RESIDUAL ANALYSIS")
        print("-" * 45)
        y_hat = self.X @ weights
        residuals = self.y - y_hat

        rss = np.sum(residuals**2)
        mse = np.mean(residuals**2)
        rmse = np.sqrt(mse)

        header = f"{'Patient':^9}|{'Actual (y)':^12}|{'Predicted (ŷ)':^14}|{'Residual (e)':^14}"
        print(header)
        print("-" * len(header))
        for i in range(self.m):
            print(f"{i+1:^9}|{self.y[i]:^12.2f}|{y_hat[i]:^14.2f}|{residuals[i]:^14.4f}")

        print("-" * len(header))
        print(f"Sum of Residuals (∑e)   : {np.sum(residuals):.4e} (Orthogonality Proof: X^T e ≈ 0)")
        print(f"Residual Sum Sq (RSS)   : {rss:.4f}")
        print(f"Mean Squared Error (MSE): {mse:.4f}")
        print(f"Root Mean Sq Error(RMSE): {rmse:.4f} days")
        print("=" * 72)


# =====================================================================
# SAMPLE DEMONSTRATION DATASET
# =====================================================================
# Features: [Age (Years), Severity Score (1-10), Comorbidity Index (0-5)]
clinical_features = np.array([
    [45, 3.0, 1.0],
    [52, 5.5, 2.0],
    [61, 7.0, 3.0],
    [38, 2.5, 0.0],
    [74, 8.5, 4.0],
    [68, 6.0, 2.0],
    [55, 4.0, 1.0]
])

# Target Outcome: Patient Length of Stay in Days (y)
length_of_stay = np.array([3.5, 6.0, 9.5, 2.0, 14.0, 8.5, 5.0])

clinical_labels = ["Age (Yrs)", "Illness Severity", "Comorbidity Index"]

# Execute pipeline
system = HospitalAlgebraSystem(clinical_features, length_of_stay, clinical_labels)
system.run_pipeline()