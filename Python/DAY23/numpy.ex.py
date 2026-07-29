import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(numbers)


import numpy as np

numbers = np.array([10, 20, 30])

result = numbers * 2

print(result)

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr)

import numpy as np

arr = np.array([10, 20, 30])

print(arr.ndim)

arr = np.array([
    [1, 2],
    [3, 4]
])

print(arr.ndim)

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(arr.shape)

arr = np.array([
    10,
    20,
    30
])

print(arr.dtype)

arr = np.array([10, 20, 30])

print(arr.itemsize)

import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data Type:", arr.dtype)
print("Item Size:", arr.itemsize)


import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[0])
print(arr[2])
print(arr[-1])

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(arr[0, 0])
print(arr[1, 2])

arr = np.array([
    10, 20, 30, 40, 50
])

print(arr[1:4])

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(arr[0:2])


print("******Array Arithmetic***********")
import numpy as np

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print(a + b)
print(a - b)
print(a * b)
print(a / b)

print("******Scalar Operations***********")

arr = np.array([10, 20, 30])

print(arr + 5)
print(arr * 2)

print("******Basic Mathematical Functions***********")
import numpy as np

arr = np.array([
    10, 20, 30, 40, 50
])

print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))