import numpy as np

class LinearRegressionMathSystem:
    """
    A mathematical implementation of Ordinary Least Squares (OLS) Linear Regression
    using fundamental matrix operations and SVD pseudo-inversion.
    """
    def __init__(self):
        self.w = None             # Weight parameters
        self.P = None             # Projection (Hat) Matrix
        self.rank = None          # Rank of Design Matrix
        self.cond_num = None      # Condition Number of X
        
    def fit(self, X_raw: np.ndarray, y: np.ndarray):
        """
        Fits model parameters w using Normal Equations / Moore-Penrose Pseudoinverse.
        """
        m = len(y)
        y = y.reshape(-1, 1).astype(np.float64)
        
        # 1. Construct Design Matrix X (Prepend column of 1s for bias w0)
        bias = np.ones((m, 1), dtype=np.float64)
        X = np.hstack([bias, X_raw.astype(np.float64)])
        
        # 2. Compute Matrix Rank & Condition Number
        self.rank = np.linalg.matrix_rank(X)
        self.cond_num = np.linalg.cond(X)
        
        # 3. Compute Normal Equation components: w = (X^T X)^(-1) X^T y
        # Uses pseudo-inverse for numerical stability against rank deficiency
        XtX = X.T @ X
        XtX_inv = np.linalg.pinv(XtX)
        self.w = XtX_inv @ X.T @ y
        
        # 4. Projection (Hat) Matrix P = X (X^T X)^(-1) X^T
        self.P = X @ XtX_inv @ X.T
        
        # 5. Compute Fitted Values and Metrics
        y_hat = X @ self.w
        e = y - y_hat
        
        rss = np.sum(e**2)
        mse = np.mean(e**2)
        rmse = np.sqrt(mse)
        
        # Orthogonality Check: X^T @ e should equal 0
        ortho_err = np.max(np.abs(X.T @ e))
        
        return {
            "X": X,
            "y": y,
            "y_hat": y_hat,
            "e": e,
            "rss": rss,
            "mse": mse,
            "rmse": rmse,
            "ortho_err": ortho_err
        }

    def predict(self, X_new_raw: np.ndarray) -> np.ndarray:
        """Computes predictions y_hat = X_new @ w."""
        bias = np.ones((len(X_new_raw), 1), dtype=np.float64)
        X_new = np.hstack([bias, X_new_raw.astype(np.float64)])
        return X_new @ self.w


# =====================================================================
# VERIFICATION RUN
# =====================================================================
if __name__ == "__main__":
    # Sample Dataset: 5 observations, 2 features
    X_train = np.array([
        [1.0, 3.0],
        [2.0, 4.0],
        [4.0, 3.5],
        [6.0, 5.0],
        [7.0, 6.5]
    ])
    y_train = np.array([12.0, 15.0, 21.0, 29.0, 34.0])

    # Run Mathematical Engine
    system = LinearRegressionMathSystem()
    results = system.fit(X_train, y_train)

    print("==========================================================")
    print("      LINEAR REGRESSION MATHEMATICAL ENGINE REPORT        ")
    print("==========================================================")
    print(f"Design Matrix Shape (m x n+1) : {results['X'].shape}")
    print(f"Design Matrix Rank            : {system.rank}")
    print(f"Condition Number              : {system.cond_num:.4f}")
    print("----------------------------------------------------------")
    print("Learned Weight Vector w^T     :", system.w.ravel().round(4))
    print("Orthogonality Max |X^T e|     :", f"{results['ortho_err']:.4e} (Exact 0)")
    print("----------------------------------------------------------")
    print(f"Residual Sum of Squares (RSS) : {results['rss']:.4f}")
    print(f"Mean Squared Error (MSE)      : {results['mse']:.4f}")
    print(f"Root Mean Squared Error(RMSE) : {results['rmse']:.4f}")
    print("==========================================================")