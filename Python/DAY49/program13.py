import numpy as np


class LeastSquaresSolver:
    """Computes and evaluates linear least squares solutions (Ax ≈ b) using NumPy."""

    def __init__(self, A, b, tol=1e-8):
        self.A = np.array(A, dtype=float)
        self.b = np.array(b, dtype=float).flatten()
        if self.A.ndim != 2:
            raise ValueError("Matrix A must be 2-dimensional.")
        self.m, self.n = self.A.shape
        if self.b.shape[0] != self.m:
            raise ValueError(f"Dimension mismatch: A has {self.m} rows, b has length {self.b.shape[0]}.")
        self.tol = tol

    # --- 1. Solving Methods ---
    def solve_qr(self):
        """Solves Ax = b via QR Decomposition (A = QR -> R x = Q^T b)."""
        Q, R = np.linalg.qr(self.A, mode="reduced")
        Qty = Q.T @ self.b
        try:
            x = np.linalg.solve(R, Qty)
            return x, "QR Decomposition"
        except np.linalg.LinAlgError:
            # Fallback if R is singular
            return self.solve_svd()[0], "QR Fallback -> SVD"

    def solve_svd(self):
        """Solves Ax = b via SVD Pseudoinverse x = A^+ b (Handles Rank Deficiency)."""
        x = np.linalg.pinv(self.A, rcond=self.tol) @ self.b
        return x, "SVD / Pseudoinverse"

    def solve_normal_equations(self):
        """Solves (A^T A) x = A^T b directly (Fast, but squares condition number)."""
        AtA = self.A.T @ self.A
        Atb = self.A.T @ self.b
        try:
            x = np.linalg.solve(AtA, Atb)
            return x, "Normal Equations"
        except np.linalg.LinAlgError:
            return None, "Normal Equations Failed (A^T A is singular)"

    # --- 2. Geometric & Statistical Diagnostics ---
    def Diagnostics(self, x):
        """Computes projection, residual metrics, and coefficient of determination (R^2)."""
        b_pred = self.A @ x
        residual_vector = b_pred - self.b
        residual_norm = np.linalg.norm(residual_vector)

        # Coefficient of Determination R^2
        ss_tot = np.sum((self.b - np.mean(self.b)) ** 2)
        ss_res = np.sum(residual_vector ** 2)
        r_squared = 1.0 - (ss_res / ss_tot) if ss_tot > self.tol else 1.0

        # Orthogonality Check: A^T * r ≈ 0
        normal_residual_norm = np.linalg.norm(self.A.T @ residual_vector)

        return {
            "Fitted Values Proj_Col(A)(b)": b_pred,
            "Residual Vector r": residual_vector,
            "Residual Sum of Squares (RSS)": ss_res,
            "Residual Norm ||Ax - b||": residual_norm,
            "Orthogonality Norm ||A^T r||": normal_residual_norm,
            "R^2 Score": r_squared,
        }

    # --- 3. Unified Execution ---
    def analyze(self, method="qr"):
        if method == "qr":
            x, method_used = self.solve_qr()
        elif method == "svd":
            x, method_used = self.solve_svd()
        elif method == "normal":
            x, method_used = self.solve_normal_equations()
        else:
            raise ValueError("Method must be 'qr', 'svd', or 'normal'.")

        diagnostics = self.Diagnostics(x)

        return {
            "Matrix Dimensions (m x n)": f"{self.m} x {self.n}",
            "Solver Method": method_used,
            "Optimal Solution x": x,
            "Diagnostics": diagnostics,
        }


# --- Execution Example ---
if __name__ == "__main__":
    print("=" * 65)
    print("                LEAST SQUARES SOLVER REPORT")
    print("=" * 65)

    # Overdetermined System (Linear Regression: y = c0 + c1*x)
    # Points: (0, 1), (1, 2.1), (2, 2.9), (3, 3.8)
    X = np.array([[1, 0], [1, 1], [1, 2], [1, 3]])
    y = np.array([1.0, 2.1, 2.9, 3.8])

    solver = LeastSquaresSolver(X, y)
    results = solver.analyze(method="qr")

    for k, v in results.items():
        print(f"\n[{k}]")
        if isinstance(v, np.ndarray):
            print(f"  {np.round(v, 4)}")
        elif isinstance(v, dict):
            for sub_k, sub_v in v.items():
                if isinstance(sub_v, np.ndarray):
                    print(f"  {sub_k:<30}: {np.round(sub_v, 4)}")
                elif isinstance(sub_v, float):
                    print(f"  {sub_k:<30}: {sub_v:.4f}")
                else:
                    print(f"  {sub_k:<30}: {sub_v}")
        else:
            print(f"  {v}")

    print("=" * 65)