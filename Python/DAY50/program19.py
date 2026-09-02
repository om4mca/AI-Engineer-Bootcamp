import numpy as np


class LeastSquaresAnalyzer:
    """Production-Grade Least Squares & Regression Diagnostics Engine using Linear Algebra."""

    def __init__(self, A, b):
        self.A = np.asarray(A, dtype=float)
        self.b = np.asarray(b, dtype=float)

        if self.A.ndim != 2:
            raise ValueError("Design matrix A must be 2-dimensional.")
        if self.b.ndim == 1:
            self.b = self.b.reshape(-1, 1)

        self.rows, self.cols = self.A.shape
        if self.b.shape[0] != self.rows:
            raise ValueError("Row count of A must match length of target vector b.")

    def solve_normal_equations(self) -> np.ndarray:
        """Solves x using Normal Equations: (A^T * A) * x = A^T * b."""
        AtA = self.A.T @ self.A
        Atb = self.A.T @ self.b

        if abs(np.linalg.det(AtA)) < 1e-10:
            # Fallback to Pseudo-Inverse if AtA is singular/collinear
            return np.linalg.pinv(self.A) @ self.b

        x_sol = np.linalg.inv(AtA) @ Atb
        return x_sol.flatten()

    def solve_qr_decomposition(self) -> np.ndarray:
        """Solves x using QR Decomposition (A = Q*R -> R*x = Q^T*b). Numerically more stable."""
        Q, R = np.linalg.qr(self.A)
        Qb = Q.T @ self.b
        x_sol = np.linalg.solve(R, Qb)
        return x_sol.flatten()

    def compute_fit_metrics(self, x_solution: np.ndarray) -> dict:
        """Calculates Residuals, Residual Sum of Squares (RSS), Total Sum of Squares (TSS), and R^2."""
        x_vec = np.asarray(x_solution, dtype=float).reshape(-1, 1)
        b_pred = self.A @ x_vec
        residuals = self.b - b_pred

        rss = float(np.sum(residuals**2))  # Residual Sum of Squares
        tss = float(np.sum((self.b - np.mean(self.b)) ** 2))  # Total Sum of Squares
        r_squared = 1.0 - (rss / tss) if tss > 0 else 1.0
        rmse = float(np.sqrt(rss / self.rows))

        return {
            "Residual Sum of Squares (RSS)": round(rss, 4),
            "Total Sum of Squares (TSS)": round(tss, 4),
            "R-squared (R^2 Score)": round(r_squared, 4),
            "Root Mean Squared Error (RMSE)": round(rmse, 4),
        }

    @staticmethod
    def fit_polynomial(x: np.ndarray, y: np.ndarray, degree: int = 1):
        """Builds a polynomial Vandermonde Matrix and fits Least Squares."""
        x_flat = np.asarray(x, dtype=float).flatten()
        y_flat = np.asarray(y, dtype=float).flatten()

        # Build Vandermonde Matrix: [1, x, x^2, ..., x^degree]
        A_poly = np.column_stack([x_flat**i for i in range(degree + 1)])

        analyzer = LeastSquaresAnalyzer(A_poly, y_flat)
        weights = analyzer.solve_qr_decomposition()
        metrics = analyzer.compute_fit_metrics(weights)

        return weights, metrics


# ==========================================
# Driver Code & Verification
# ==========================================
if __name__ == "__main__":
    print("============================================")
    print("      LEAST SQUARES ANALYZER SYSTEM         ")
    print("============================================\n")

    # 1. Synthetic Data: Y = 2.5*X + 4.0 + Noise
    np.random.seed(42)
    X_raw = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=float)
    Y_raw = 2.5 * X_raw + 4.0 + np.random.normal(0, 1.2, size=len(X_raw))

    # 2. Linear Model Fit (Polynomial Degree 1)
    weights, metrics = LeastSquaresAnalyzer.fit_polynomial(
        X_raw, Y_raw, degree=1
    )

    print("--- [1] Least Squares Line Coefficients ---")
    print(f"  Intercept (w0) : {weights[0]:.4f}")
    print(f"  Slope (w1)     : {weights[1]:.4f}")
    print(f"  Fitted Line    : y = {weights[1]:.4f}*x + {weights[0]:.4f}")

    print("\n--- [2] Goodness-of-Fit Metrics ---")
    for metric_name, val in metrics.items():
        print(f"  {metric_name:<32}: {val}")

    # 3. Method Comparison: Normal Equations vs QR
    A_design = np.column_stack([np.ones_like(X_raw), X_raw])
    solver = LeastSquaresAnalyzer(A_design, Y_raw)

    sol_normal = solver.solve_normal_equations()
    sol_qr = solver.solve_qr_decomposition()

    print("\n--- [3] Algorithm Stability Check ---")
    print(f"  Normal Equations Solution : {np.round(sol_normal, 4)}")
    print(f"  QR Decomposition Solution : {np.round(sol_qr, 4)}")
    print(
        f"  Solutions Match?          : {np.allclose(sol_normal, sol_qr)}"
    )