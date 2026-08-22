import numpy as np

u = np.array([2, 4, 5])
v = np.array([3, -1, 2])

# Dot product calculation
dot_prod_1 = np.dot(u, v)   # Output: (2*3) + (4*-1) + (5*2) = 6 - 4 + 10 = 12
dot_prod_2 = u @ v          # Modern @ operator syntax

print("Dot Product (np.dot):", dot_prod_1)
print("Dot Product (u @ v):  ", dot_prod_2)