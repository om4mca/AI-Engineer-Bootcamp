import numpy as np

# 1. Standard range from 0 up to (but excluding) 10
arr1 = np.arange(10)

# 2. Custom start and stop (5 to 14)
arr2 = np.arange(5, 15)

# 3. With a custom step size (0 to 20, jumping by 2)
arr3 = np.arange(0, 20, 2)

# 4. Using float step sizes (0.0 to 1.0, jumping by 0.2)
arr4 = np.arange(0, 1.0, 0.2)

# 5. Descending / Negative step size
arr5 = np.arange(10, 0, -2)

print("1. Default range (0 to 9) :", arr1)
print("2. Start & Stop (5 to 14)  :", arr2)
print("3. Even step of 2         :", arr3)
print("4. Float step of 0.2      :", arr4)
print("5. Descending step (-2)   :", arr5)