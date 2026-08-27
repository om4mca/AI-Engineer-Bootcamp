import numpy as np

def hospital_eigen_analysis():
    print("=" * 65)
    print("         HOSPITAL FEATURE EIGEN ANALYSIS SYSTEM")
    print("=" * 65)

    # -------------------------------------------------------------
    # Step 1: Create Square Feature Relation Matrix (3x3)
    # Features: [Bed Occupancy (%), Staffing Ratio, Equipment Readiness (%)]
    # -------------------------------------------------------------
    A = np.array([
        [9.0, 2.0, 4.0],
        [2.0, 6.0, 1.0],
        [4.0, 1.0, 8.0]
    ], dtype=float)

    print("\n[Step 1] Hospital Feature Matrix (A):")
    print("   [Occupancy, Staffing, Equipment]")
    print(A)

    # -------------------------------------------------------------
    # Step 2: Compute Eigenvalues and Eigenvectors
    # -------------------------------------------------------------
    eigenvalues, eigenvectors = np.linalg.eig(A)

    # -------------------------------------------------------------
    # Step 3: Display Results
    # -------------------------------------------------------------
    print("\n[Step 3] Eigen Decomposition Results:")
    print("-" * 45)
    print("Eigenvalues (λ):")
    for i, val in enumerate(eigenvalues, start=1):
        print(f"  λ_{i} = {val:.6f}")

    print("\nEigenvectors (v) [Columns]:")
    print(np.round(eigenvectors, 6))

    # -------------------------------------------------------------
    # Step 4 & 5: Verification (A v ≈ λ v) using np.allclose()
    # -------------------------------------------------------------
    print("\n[Step 4 & 5] Eigenpair Verification (A @ v ≈ λ * v):")
    print("-" * 65)

    all_verified = True

    for i in range(len(eigenvalues)):
        lam = eigenvalues[i]
        v = eigenvectors[:, i]

        left_side = A @ v
        right_side = lam * v

        is_equal = np.allclose(left_side, right_side, atol=1e-8)
        if not is_equal:
            all_verified = False

        print(f"\n--- Eigenpair #{i+1} (λ = {lam:.4f}) ---")
        print(f"  A @ v   : {np.round(left_side, 6)}")
        print(f"  λ * v   : {np.round(right_side, 6)}")
        print(f"  np.allclose Check: {'PASSED ✅' if is_equal else 'FAILED ❌'}")

    # -------------------------------------------------------------
    # Analysis Summary
    # -------------------------------------------------------------
    print("\n" + "=" * 65)
    print("                     ANALYSIS SUMMARY")
    print("=" * 65)
    primary_idx = np.argmax(eigenvalues)
    print(f"• Dominant Eigenvalue (λ_max) : {eigenvalues[primary_idx]:.4f}")
    print(f"• Principal Direction Vector  : {np.round(eigenvectors[:, primary_idx], 4)}")
    print(f"• Overall System Verification : {'ALL PASSED ✅' if all_verified else 'FAILED ❌'}")
    print("• Educational Insight         : Because A is a real symmetric matrix,")
    print("                                its eigenvalues are strictly real and its")
    print("                                eigenvectors are mutually orthogonal.")
    print("=" * 65)

if __name__ == "__main__":
    hospital_eigen_analysis()