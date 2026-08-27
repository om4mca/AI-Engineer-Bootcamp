import numpy as np
from typing import Dict, List, Tuple, Union

class EigenVerifier:
    """Production verification engine for matrix eigenpairs."""
    
    def __init__(self, rtol: float = 1e-5, atol: float = 1e-8):
        self.rtol = rtol
        self.atol = atol

    def verify_pair(
        self, A: np.ndarray, val: float, vec: np.ndarray
    ) -> Dict[str, Union[bool, float, np.ndarray]]:
        """Verifies a single candidate (λ, v) pair against matrix A."""
        A = np.asarray(A, dtype=np.float64)
        v = np.asarray(vec, dtype=np.float64).flatten()
        
        # 1. Structural Checks
        if A.ndim != 2 or A.shape[0] != A.shape[1]:
            raise ValueError("Matrix A must be square.")
        if A.shape[0] != v.shape[0]:
            raise ValueError(f"Vector dimension ({v.shape[0]}) does not match matrix shape ({A.shape}).")
            
        # 2. Non-zero vector check
        v_norm = np.linalg.norm(v)
        if np.isclose(v_norm, 0.0, atol=self.atol):
            return {
                "valid": False,
                "reason": "Invalid Eigenvector: Vector magnitude is zero.",
                "residual_norm": np.nan
            }

        # 3. Compute Transformations
        left_side = A @ v           # Matrix-vector transformation
        right_side = val * v        # Scalar scaling
        
        # 4. Residual Calculation
        residual = left_side - right_side
        residual_norm = np.linalg.norm(residual)
        
        # 5. Tolerance Validation
        is_valid = np.allclose(left_side, right_side, rtol=self.rtol, atol=self.atol)
        
        return {
            "valid": bool(is_valid),
            "eigenvalue": float(val),
            "eigenvector": v,
            "left_side": left_side,
            "right_side": right_side,
            "residual_norm": float(residual_norm),
            "relative_error": float(residual_norm / (np.linalg.norm(left_side) + 1e-15))
        }

    def verify_full_decomposition(
        self, A: np.ndarray
    ) -> Tuple[bool, List[Dict]]:
        """Computes eigen-decomposition via NumPy and verifies every returned pair."""
        eigenvalues, eigenvectors = np.linalg.eig(A)
        results = []
        all_passed = True
        
        for i in range(len(eigenvalues)):
            lam = eigenvalues[i]
            v = eigenvectors[:, i]  # Extract column eigenvector
            res = self.verify_pair(A, lam, v)
            results.append(res)
            if not res["valid"]:
                all_passed = False
                
        return all_passed, results


# --- SYSTEM DEMONSTRATION ---
if __name__ == "__main__":
    verifier = EigenVerifier(rtol=1e-5, atol=1e-8)
    
    # 3x3 Operational Matrix
    Hospital_Matrix = np.array([
        [12.0, 4.0, 6.0],
        [4.0, 10.0, 2.0],
        [6.0, 2.0, 8.0]
    ])
    
    print("=== RUNNING EIGENPAIR VERIFICATION SYSTEM ===")
    passed, report = verifier.verify_full_decomposition(Hospital_Matrix)
    
    for idx, item in enumerate(report, start=1):
        status = "PASSED ✅" if item["valid"] else "FAILED ❌"
        print(f"\nEigenpair #{idx} [{status}]")
        print(f"  λ value       : {item['eigenvalue']:.6f}")
        print(f"  v vector      : {np.round(item['eigenvector'], 4)}")
        print(f"  Residual ||r||: {item['residual_norm']:.2e}")
        print(f"  Rel. Error    : {item['relative_error']:.2e}")
        
    print(f"\nOverall System Status: {'ALL PAIRS VALIDATED ✅' if passed else 'VERIFICATION FAILED ❌'}")