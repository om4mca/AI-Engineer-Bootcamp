import numpy as np

patient_matrix = np.array([
    [5, 25000],
    [3, 18000]
])

# 1. Determinant
det = np.linalg.det(patient_matrix)
print("Determinant:", det)
# Output: Determinant: 15000.000000000005 (due to floating-point precision)

# 2. Invertibility Check & Inverse Computation
if det != 0:
    inverse = np.linalg.inv(patient_matrix)
    print("\nInverse Matrix:\n", inverse)
    # Output:
    # [[ 1.2        -1.66666667]
    #  [-0.0002      0.00033333]]

    # 3. Verification: Matrix @ Inverse
    identity = patient_matrix @ inverse
    print("\nPatient Matrix @ Inverse:\n", identity)
    # Output:
    # [[1. 0.]
    #  [0. 1.]]
else:
    print("Matrix is singular and cannot be inverted.")