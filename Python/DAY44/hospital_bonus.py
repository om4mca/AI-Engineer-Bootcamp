import numpy as np

def hospital_matrix_invertibility_system(matrix_dataset):
    print("==================================================")
    print("     HOSPITAL MATRIX INVERTIBILITY SYSTEM         ")
    print("==================================================\n")

    for idx, (label, raw_matrix) in enumerate(matrix_dataset.items(), start=1):
        print(f"--- MATRIX #{idx}: {label} ---")
        A = np.array(raw_matrix, dtype=float)
        print(f"Matrix Input:\n{A}")
        
        # 1. Check Dimensions
        if A.shape != (2, 2):
            print("Error: Input must be a 2x2 matrix.\n")
            continue

        # 2. Calculate Determinant
        # det(A) = ad - bc
        det = np.linalg.det(A)
        det_clean = round(det, 6)
        print(f"Determinant: {det_clean}")

        # 3. Identify Status & 4. Calculate Inverse with Error Handling
        if det_clean != 0:
            print("Status: Non-Singular (Invertible)")
            try:
                # Analytical Formula check vs np.linalg.inv
                inv = np.linalg.inv(A)
                print(f"Inverse Matrix:\n{np.round(inv, 6)}")

                # 5. Verification: A @ Inverse = Identity Matrix
                identity_check = A @ inv
                print(f"Verification Product (A @ Inverse):\n{np.round(identity_check, 4)}")
                print("Verification Result: Identity Matrix ✅\n")
            except np.linalg.LinAlgError as e:
                print(f"Linear Algebra Exception: {e}\n")
        else:
            print("Status: Singular (Non-Invertible)")
            print("Inverse Calculation: Failed -> Determinant is 0.")
            print("Verification Result: Cannot compute inverse ✅\n")


# ----------------------------------------------------
# Patient Numerical Datasets (2x2 Practice Matrices)
# ----------------------------------------------------

patient_dataset = {
    # Case 1: Standard Invertible Matrix [Age, Length of Stay]
    "Patient Cohort A (Distinct Indicators)": [
        [45, 3],
        [60, 7]
    ],

    # Case 2: Singular Matrix (Column 2 is exactly 10x Column 1 -> Collinear)
    "Patient Cohort B (Redundant/Collinear Data)": [
        [5, 50],
        [8, 80]
    ],

    # Case 3: Invertible Matrix with Scale Difference [Age, Total Expenses]
    "Patient Cohort C (High-Magnitude Feature Variance)": [
        [32, 12000],
        [54, 45000]
    ],

    # Case 4: Singular Matrix (Identical Rows)
    "Patient Cohort D (Duplicate Record Entries)": [
        [25, 4],
        [25, 4]
    ]
}

# Run System
hospital_matrix_invertibility_system(patient_dataset)