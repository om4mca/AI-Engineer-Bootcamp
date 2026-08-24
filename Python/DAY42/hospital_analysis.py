import numpy as np

# Feature Matrix X: [Age, Weight (kg), BloodPressure (mmHg), StayDays, Bill ($)]
X = np.array([
    [45, 70.5, 120, 3, 2500],
    [62, 85.0, 140, 7, 8400],
    [29, 60.2, 115, 2, 1800],
    [54, 92.4, 135, 5, 5100],
    [38, 78.0, 128, 4, 3900]
])

# 1. Shape
print("Shape:", X.shape)

# 2. Indexing (Patient 2's BloodPressure at row 1, col 2)
print("Indexing (Patient 2 BP):", X[1, 2])

# 3. Slicing (First 3 patients, Age and Bill columns)
print("Slicing (First 3 Patients' Age & Bill):\n", X[:3, [0, 4]])

# 4. Addition (Adding a $50 flat administrative surcharge to all elements)
print("Addition (X + 50):\n", X + 50)

# 5. Subtraction (Applying a $200 billing discount column)
discount = np.zeros_like(X)
discount[:, 4] = 200
print("Subtraction (X - Discount):\n", X - discount)

# 6. Scalar Multiplication (Scaling all values by a factor of 1.1)
print("Scalar Multiplication (X * 1.1):\n", X * 1.1)

# 7. Transpose
print("Transpose (X^T):\n", X.T)