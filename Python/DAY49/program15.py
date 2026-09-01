import numpy as np


class LinearAlgebraMasterSystem:
    """Unified Linear Algebra System integrating:

    1. Matrix Rank & Vector Independence
    2. Linear System Solvers (LU, QR, SVD)
    3. System & Solution Verification
    4. Least Squares Engine & Error Diagnostics (RSS, MSE, RMSE, R^2)
    """

    def __init__(self, A, b=None, tol=1e-8):
        self.A = np.array(A, dtype=float)
        if self.A.ndim != 2:
            raise ValueError("Matrix A must be 2-dimensional.")
        self.m, self.n = self.A.shape
        self.tol = tol

        if b is not None:
            self.b = np.array(b, dtype=float).flatten()
            if self.b.shape[0] != self.m:
                raise ValueError(
                    f"Dimension mismatch: A is {self.m}x{self.n}, but b has length {self.b.shape[0]}."
                )
        else:
            self.b = None

    # =========================================================================
    # 1. INDEPENDENCE & STRUCTURE ANALYZER
    # =========================================================================
    def analyze_independence(self):
        """Analyzes column vector independence, matrix rank, and determinant properties."""
        rank = np.linalg.matrix_rank(self.A, tol=self.tol)
        is_cols_independent = rank == self.n

        det_val = (
            np.linalg.det(self.A)
            if self.m == self.n
            else "N/A (Non-Square)"
        )
        cond_num = np.linalg.cond(self.A)

        # Gram Matrix G = A^T A
        G = self.A.T @ self.A
        gram_det = np.linalg.det(G)

        return {
            "Shape (m x n)": f"{self.m} x {self.n}",
            "Matrix Rank": f"{rank} / {self.n}",
            "Columns Linearly Independent": is_cols_independent,
            "Determinant det(A)": det_val,
            "Condition Number kappa(A)": cond_num,
            "Gramian Determinant det(A^T A)": gram_det,
        }

    # =========================================================================
    # 2. SOLVER ENGINE (LU, QR, SVD)
    # =========================================================================
    def solve_system(self, preferred_method="auto"):
        """Solves Ax = b using Direct LU, QR Least Squares, or SVD Pseudoinverse."""
        if self.b is None:
            raise ValueError("Target vector b must be provided to solve Ax = b.")

        rank_A = np.linalg.matrix_rank(self.A, tol=self.tol)
        Augmented = np.column_stack([self.A, self.b])
        rank_Aug = np.linalg.matrix_rank(Augmented, tol=self.tol)

        # Classify via Rouché-Capelli Theorem
        if rank_A < rank_Aug:
            classification = "Inconsistent (Overdetermined / No Exact Solution)"
        elif rank_A == rank_Aug == self.n:
            classification = "Consistent & Determined (Unique Solution)"
        else:
            classification = "Consistent & Underdetermined (Infinitely Many)"

        # Method Selection Strategy
        if preferred_method == "auto":
            if self.m == self.n and rank_A == self.n:
                method = "lu"
            elif self.m >= self.n and rank_A == self.n:
                method = "qr"
            else:
                method = "svd"
        else:
            method = preferred_method

        # Execution
        if method == "lu":
            x = np.linalg.solve(self.A, self.b)
            used_method = "Exact LU / Gaussian Elimination"
        elif method == "qr":
            Q, R = np.linalg.qr(self.A, mode="reduced")
            x = np.linalg.solve(R, Q.T @ self.b)
            used_method = "Least Squares via QR Decomposition"
        elif method == "svd":
            x = np.linalg.pinv(self.A, rcond=self.tol) @ self.b
            used_method = "Minimum-Norm Pseudoinverse via SVD"
        else:
            raise ValueError(f"Unknown method '{method}'. Use 'lu', 'qr', 'svd', or 'auto'.")

        return {
            "System Classification": classification,
            "Solver Selected": used_method,
            "Solution Vector x": x,
        }

    # =========================================================================
    # 3. VERIFICATION ENGINE
    # =========================================================================
    def verify_solution(self, x_candidate):
        """Verifies candidate vector x against residual and orthogonality conditions."""
        if self.b is None:
            raise ValueError("Target vector b required for solution verification.")

        x = np.array(x_candidate, dtype=float).flatten()
        residual_vec = self.A @ x - self.b
        res_norm = np.linalg.norm(residual_vec)

        # Normal equation residual check: A^T (Ax - b) = 0
        normal_residual_norm = np.linalg.norm(self.A.T @ residual_vec)

        b_norm = np.linalg.norm(self.b)
        rel_error = res_norm / b_norm if b_norm > self.tol else res_norm

        if res_norm < self.tol:
            status = "Verified Exact Solution"
        elif normal_residual_norm < self.tol:
            status = "Verified Optimal Least-Squares Solution"
        else:
            status = "Invalid Candidate Solution"

        return {
            "Status": status,
            "Residual Norm ||Ax - b||": res_norm,
            "Relative Error ||r||/||b||": rel_error,
            "Normal Residual Norm ||A^T r||": normal_residual_norm,
        }

    # =========================================================================
    # 4. RSS, MSE & LEAST SQUARES ERROR DIAGNOSTICS
    # =========================================================================
    def compute_error_diagnostics(self, x, num_params=None):
        """Computes RSS, MSE, RMSE, R-squared, and residual diagnostics."""
        if self.b is None:
            raise ValueError("Target vector b required for error analysis.")

        p = num_params if num_params is not None else self.n
        y_true = self.b
        y_pred = self.A @ x
        residuals = y_true - y_pred

        n = len(y_true)
        rss = np.sum(residuals ** 2)
        mse = rss / n
        rmse = np.sqrt(mse)
        mae = np.mean(np.abs(residuals))

        # Goodness of fit (R^2)
        y_mean = np.mean(y_true)
        tss = np.sum((y_true - y_mean) ** 2)
        r_squared = 1.0 - (rss / tss) if tss > self.tol else 1.0

        # Unbiased degree-of-freedom corrected metrics
        df = n - p
        unbiased_mse = rss / df if df > 0 else mse
        unbiased_rmse = np.sqrt(unbiased_mse)

        return {
            "Sample Size (n)": n,
            "Degrees of Freedom (n - p)": df,
            "Residual Sum of Squares (RSS)": rss,
            "Mean Squared Error (MSE)": mse,
            "Root Mean Squared Error (RMSE)": rmse,
            "Unbiased RMSE": unbiased_rmse,
            "Mean Absolute Error (MAE)": mae,
            "R-squared (R^2)": r_squared,
        }

    # =========================================================================
    # 5. UNIFIED WORKFLOW PIPELINE
    # =========================================================================
    def execute_full_pipeline(self):
        """Runs full end-to-end analysis across structure, solving, verification, and errors."""
        independence_report = self.analyze_independence()

        if self.b is not None:
            solver_report = self.solve_system(preferred_method="auto")
            x_opt = solver_report["Solution Vector x"]
            verifier_report = self.verify_solution(x_opt)
            error_report = self.compute_error_diagnostics(x_opt)
        else:
            solver_report, verifier_report, error_report = None, None, None

        return {
            "1. Independence & Structure": independence_report,
            "2. Solver Execution": solver_report,
            "3. Solution Verification": verifier_report,
            "4. Error Diagnostics": error_report,
        }


# =============================================================================
# EXECUTION & VERIFICATION DEMONSTRATION
# =============================================================================
if __name__ == "__main__":
    print("=" * 70)
    print("       COMPLETE LINEAR ALGEBRA MASTER SYSTEM DEMONSTRATION")
    print("=" * 70)

    # Overdetermined Linear Regression Dataset: y = 1.5*x0 + 2.0*x1 + noise
    np.random.seed(42)
    X_data = np.array([[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6]])
    y_data = np.array([3.6, 5.4, 7.2, 9.1, 10.9, 12.7])

    master = LinearAlgebraMasterSystem(A=X_data, b=y_data)
    pipeline_results = master.execute_full_pipeline()

    for section, content in pipeline_results.items():
        print(f"\n{"-" * 70}\n {section}\n{"-" * 70}")
        if content is None:
            print("  [No Target Vector b Provided]")
            continue
        for key, val in content.items():
            if isinstance(val, np.ndarray):
                print(f"  {key:<34}: {np.round(val, 4)}")
            elif isinstance(val, float):
                print(f"  {key:<34}: {val:.6f}")
            else:
                print(f"  {key:<34}: {val}")

    print("=" * 70)