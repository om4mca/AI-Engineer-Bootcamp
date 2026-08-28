import numpy as np
import pandas as pd

class LinearIndependenceAnalyzer:
    """
    Complete Linear Independence Analysis Engine built on Pure NumPy.
    Analyzes Vector Spaces, Matrix Rank, VIF, and performs Automatic Pruning.
    """
    def __init__(self, vif_threshold: float = 10.0):
        self.vif_threshold = vif_threshold

    @staticmethod
    def _compute_vif_numpy(X_mat: np.ndarray) -> np.ndarray:
        """Calculates VIF for each column using OLS Regression in Pure NumPy."""
        n_features = X_mat.shape[1]
        vif_list = []
        
        for i in range(n_features):
            y = X_mat[:, i]
            X = np.delete(X_mat, i, axis=1)
            # Add bias/intercept column
            X = np.hstack([np.ones((X.shape[0], 1)), X])
            
            try:
                # Solve OLS: beta = (X^T X)^(-1) X^T y
                beta = np.linalg.lstsq(X, y, rcond=None)[0]
                y_pred = X @ beta
                
                ss_tot = np.sum((y - np.mean(y)) ** 2)
                ss_res = np.sum((y - y_pred) ** 2)
                
                if ss_tot == 0 or ss_res < 1e-10:
                    vif = np.inf
                else:
                    r_sq = 1.0 - (ss_res / ss_tot)
                    vif = 1.0 / (1.0 - r_sq) if r_sq < 1.0 else np.inf
            except np.linalg.LinAlgError:
                vif = np.inf
                
            vif_list.append(vif)
        return np.array(vif_list)

    def analyze(self, df: pd.DataFrame) -> dict:
        """Runs complete linear independence diagnostic on a DataFrame."""
        X = df.values.astype(np.float64)
        m_rows, n_cols = X.shape
        rank = np.linalg.matrix_rank(X)
        cond_num = np.linalg.cond(X)
        vifs = self._compute_vif_numpy(X)
        
        report_df = pd.DataFrame({
            "Feature": df.columns,
            "VIF": vifs,
            "Status": ["REDUNDANT ❌" if v > self.vif_threshold else "INDEPENDENT ✅" for v in vifs]
        })
        
        return {
            "matrix_shape": (m_rows, n_cols),
            "rank": rank,
            "full_rank": rank == n_cols,
            "condition_number": cond_num,
            "vif_report": report_df
        }

    def prune_redundant_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """Iteratively removes features with highest VIF until full independence is achieved."""
        current_df = df.copy()
        
        while True:
            X = current_df.values.astype(np.float64)
            if X.shape[1] <= 1:
                break
                
            vifs = self._compute_vif_numpy(X)
            max_vif_idx = np.argmax(vifs)
            max_vif = vifs[max_vif_idx]
            
            if max_vif > self.vif_threshold or np.isinf(max_vif):
                dropped_col = current_df.columns[max_vif_idx]
                print(f"Pruning Redundant Feature: {dropped_col} (VIF: {max_vif:.2f})")
                current_df = current_df.drop(columns=[dropped_col])
            else:
                break
                
        return current_df


# --- SYSTEM EXECUTION DEMONSTRATION ---
if __name__ == "__main__":
    # Create dataset with both unique and linearly dependent features
    raw_data = pd.DataFrame({
        "Age":         [25, 30, 45, 50, 60],
        "Salary":      [50, 65, 90, 110, 140],
        "Experience":  [2,  5,  12, 15, 22],
        "Proj_Count":  [3,  6,  8,  11, 14],
        "Exact_Dup":   [4,  10, 24, 30, 44]  # Exact: 2 * Experience
    })

    system = LinearIndependenceAnalyzer(vif_threshold=10.0)
    
    print("=== INITIAL LINEAR INDEPENDENCE DIAGNOSTIC ===")
    diag = system.analyze(raw_data)
    print(f"Matrix Shape     : {diag['matrix_shape']}")
    print(f"Matrix Rank      : {diag['rank']} / {diag['matrix_shape'][1]}")
    print(f"Full Rank Status : {'FULL RANK ✅' if diag['full_rank'] else 'RANK DEFICIENT ❌'}")
    print(f"Condition Number : {diag['condition_number']:.2f}\n")
    print("VIF Diagnostic Report:\n", diag["vif_report"])
    
    print("\n=== AUTOMATED PRUNING PROCESS ===")
    pruned_df = system.prune_redundant_features(raw_data)
    
    print("\n=== POST-PRUNING DIAGNOSTIC ===")
    post_diag = system.analyze(pruned_df)
    print(f"Pruned Features  : {list(pruned_df.columns)}")
    print(f"Pruned Rank      : {post_diag['rank']} / {post_diag['matrix_shape'][1]}")
    print(f"Full Rank Status : {'FULL RANK ✅' if post_diag['full_rank'] else 'RANK DEFICIENT ❌'}")