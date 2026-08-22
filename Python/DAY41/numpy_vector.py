import numpy as np

a = np.array([2, 4, 6])
b = np.array([1, 3, 5])

print(a)
print(b)

result = a + b

print(result)

result = a - b

print(result)

result = 3 * a

print(result)

result = np.dot(a, b)

print(result)

magnitude = np.linalg.norm(a)

print(magnitude)