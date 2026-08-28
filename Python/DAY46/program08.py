import numpy as np

# Generate 3D standard basis vectors using NumPy identity matrix
I3 = np.eye(3)

e1 = I3[:, 0]  # [1. 0. 0.]
e2 = I3[:, 1]  # [0. 1. 0.]
e3 = I3[:, 2]  # [0. 0. 1.]

# Reconstruct an arbitrary vector v = [4, -2, 7]
v_coords = np.array([4, -2, 7])
v_reconstructed = v_coords[0] * e1 + v_coords[1] * e2 + v_coords[2] * e3

print("Standard Basis Vectors in R3:")
print("e1 =", e1)
print("e2 =", e2)
print("e3 =", e3)
print("\nReconstructed Vector:", v_reconstructed)  # [4. -2. 7.]