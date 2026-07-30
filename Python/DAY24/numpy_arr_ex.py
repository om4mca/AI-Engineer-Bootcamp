import numpy as np

arr = np.zeros(5)

print(arr)

arr = np.zeros((2, 3))

print(arr)

arr = np.ones(5)

print(arr)

arr = np.ones((2, 3))

print(arr)

arr = np.full(5, 10)

print(arr)

arr = np.full((2, 3), 7)

print(arr)

arr = np.arange(1, 10)

print(arr)

# np.arange(start, stop, step)
arr = np.arange(0, 20, 5)

print(arr)

# ध्यान दें: stop value include नहीं होती।

arr = np.linspace(0, 10, 5)

print(arr)

arr = np.random.rand(5)

print(arr)

arr = np.random.randint(1, 100, 5)

print(arr)

arr = np.random.randint(1, 100, (3, 4))

print(arr)

print()
print("********Random Seed**********")
np.random.seed(42)

arr = np.random.randint(1, 100, 5)

print(arr)

print()
print("****reshape()*****")
arr = np.arange(1, 13)

print(arr)

new_arr = arr.reshape(3, 4)

print(new_arr)

arr = np.arange(1, 13)

new_arr = arr.reshape(3, -1)

print(new_arr)

new_arr1=arr.reshape(-1, 4)
print(new_arr1)


print()
print("***Convert 2D into 1D******")

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

flat = arr.flatten()

print(flat)

flat = arr.ravel()

print(flat)

print()
print("****** Concatenate********")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.concatenate((a, b))

print(result)

print()
print("****** 2D Concatenate********")
a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])

result = np.concatenate((a, b), axis=0)

print(result)

result = np.concatenate((a, b), axis=1)

print(result)

arr = np.array([1, 2, 3, 4, 5, 6])

parts = np.split(arr, 3)

print(parts)

arr = np.array([10, 20, 30, 40, 50])

result = arr[arr > 25]

print(result)

arr = np.array([10, 20, 30, 40, 50])

result = arr[(arr > 20) & (arr < 50)]

print(result)