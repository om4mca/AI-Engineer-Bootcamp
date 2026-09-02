import numpy as np


class AIEngineerFoundationMasterSystem:
    """Unified Production-Grade Linear Algebra Engine for AI & Machine Learning Workloads."""

    def __init__(self, data: np.ndarray):
        self.X = np.asarray(data, dtype=float)
        if self.X.ndim != 2:
            raise ValueError("Input data must be a 2D Matrix (Samples x Features).")
        self.n_samples, self.n_features = self.X.shape

    # ==========================================
    # 1. Structural & Diagnostic Audit
    # ==========================================
    def AuditMatrixProperties(self) -> dict:
        """Matrix ke rank, determinant, trace aur condition number audit karta hai."""
        is_square = self.n_samples == self.n_features
        rank = np.linalg.matrix_rank(self.X)
        cond_num = np.linalg.cond(self.X)
        det = np.linalg.det(self.X) if is_square else None
        trace = np.trace(self.X) if is_square else None

        return {
            "Shape": (self.n_samples, self.n_features),
            "Matrix Rank": rank,
            "Is Full Rank?": rank == min(self.n_samples, self.n_features),
            "Condition Number": round(cond_num, 4),
            "Determinant": round(det, 4) if det is not None else "N/A (Non-Square)",
            "Trace": round(trace, 4) if trace is not None else "N/A (Non-Square)",
        }

    # ==========================================
    # 2. Linear System Solver (Ax = b)
    # ==========================================
    def SolveLinearSystem(self, target_b: np.ndarray) -> dict:
        """Solves Ax = b using Direct LAPACK or Least-Squares solver."""
        b_vec = np.asarray(target_b, dtype=float).flatten()
        if b_vec.shape[0] != self.n_samples:
            raise ValueError("Dimension mismatch between matrix A and target b.")

        if self.n_samples == self.n_features and np.linalg.matrix_rank(self.X) == self.n_features:
            x_sol = np.linalg.solve(self.X, b_vec)
            method = "Direct LAPACK Solver"
        else:
            x_sol, _, _, _ = np.linalg.lstsq(self.X, b_vec, rcond=None)
            method = "Least-Squares Solver"

        residual = np.linalg.norm(self.X @ x_sol - b_vec)
        return {
            "Method Used": method,
            "Solution Vector (x)": np.round(x_sol, 4),
            "Residual L2 Norm": round(float(residual), 6),
        }

    # ==========================================
    # 3. Spectral Analysis (Eigen Engine)
    # ==========================================
    def AnalyzeSpectrum(self) -> dict:
        """Symmetric Covariance Matrix ($X^T X$) ki Spectral properties calculate karta hai."""
        cov_matrix = np.cov(self.X, rowvar=False) if self.n_features > 1 else np.var(self.X)
        evals, evecs = np.linalg.eigh(cov_matrix)

        # Sort descending
        idx = np.argsort(evals)[::-1]
        evals = evals[idx]
        evecs = evecs[:, idx]

        spectral_radius = float(np.max(np.abs(evals)))
        return {
            "Covariance Matrix": np.round(cov_matrix, 4),
            "Eigenvalues": np.round(evals, 4),
            "Principal Eigenvector": np.round(evecs[:, 0], 4),
            "Spectral Radius": round(spectral_radius, 4),
        }

    # ==========================================
    # 4. Dimensionality Reduction (PCA Engine)
    # ==========================================
    def CompressPCA(self, n_components: int = 2) -> dict:
        """PCA dimensionality reduction using Singular Value Decomposition (SVD)."""
        if n_components > min(self.n_samples, self.n_features):
            raise ValueError("n_components higher than data dimensions.")

        # Center the data
        X_centered = self.X - np.mean(self.X, axis=0)

        # SVD: X_centered = U * S * Vt
        U, S, Vt = np.linalg.svd(X_centered, full_matrices=False)

        # Variance Explained
        explained_variance = (S**2) / (self.n_samples - 1)
        total_variance = np.sum(explained_variance)
        variance_ratio = explained_variance / total_variance

        # Projection onto k principal components
        components = Vt[:n_components]
        X_projected = X_centered @ components.T

        return {
            "Transformed Shape": X_projected.shape,
            "Explained Variance Ratio": np.round(variance_ratio[:n_components], 4),
            "Total Cumulative Variance": round(float(np.sum(variance_ratio[:n_components])), 4),
            "Projected Data (First 3 Rows)": np.round(X_projected[:3], 4),
        }


# ==========================================
# Master Driver Execution & Test Run
# ==========================================
if __name__ == "__main__":
    print("==========================================================")
    print("    AI ENGINEER FOUNDATION MASTER SYSTEM (LINEAR ALGEBRA) ")
    print("==========================================================\n")

    # 1. Synthetic Dataset Generation (10 Samples x 4 Features)
    np.random.seed(42)
    sample_dataset = np.array([
        [2.5, 2.4, 0.5, 1.2],
        [0.5, 0.7, 0.1, 0.3],
        [2.2, 2.9, 0.8, 1.5],
        [1.9, 2.2, 0.4, 1.0],
        [3.1, 3.0, 1.1, 1.8],
        [2.3, 2.7, 0.6, 1.3],
        [2.0, 1.6, 0.3, 0.9],
        [1.0, 1.1, 0.2, 0.5],
        [1.5, 1.6, 0.4, 0.7],
        [1.1, 0.9, 0.2, 0.4],
    ])

    master_system = AIEngineerFoundationMasterSystem(sample_dataset)

    # Execution 1: Matrix Diagnostic Audit
    print("--- [1] Structural Diagnostics Audit ---")
    audit = master_system.AuditMatrixProperties()
    for k, v in audit.items():
        print(f"  {k:<24}: {v}")

    # Execution 2: Linear System Solver (Target b vector of size 10)
    print("\n--- [2] System Solver (Ax = b) ---")
    target_b = np.array([10, 3, 11, 8, 14, 11, 8, 5, 6, 4])
    solver_res = master_system.SolveLinearSystem(target_b)
    for k, v in solver_res.items():
        print(f"  {k:<24}: {v}")

    # Execution 3: Spectral Analysis
    print("\n--- [3] Spectral Analysis (Eigendecomposition) ---")
    spectrum = master_system.AnalyzeSpectrum()
    print("  Eigenvalues             :", spectrum["Eigenvalues"])
    print("  Principal Eigenvector   :", spectrum["Principal Eigenvector"])
    print("  Spectral Radius         :", spectrum["Spectral Radius"])

    # Execution 4: Principal Component Analysis (Compression to 2D)
    print("\n--- [4] Dimensionality Reduction (PCA Engine) ---")
    pca_res = master_system.CompressPCA(n_components=2)
    print("  Transformed Data Shape  :", pca_res["Transformed Shape"])
    print("  Explained Variance      :", pca_res["Explained Variance Ratio"])
    print("  Total Retained Variance :", f"{pca_res['Total Cumulative Variance']*100:.2f}%")
    print("  Projected Data (Top 3)  :\n", pca_res["Projected Data (First 3 Rows)"])