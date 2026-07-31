import numpy as np

marks = np.array([70, 80, 90, 60, 50])

total = np.sum(marks)

print(total)

average = np.mean(marks)

print(average)

arr = np.array([10, 20, 30, 40, 50])

print(np.median(arr))

arr = np.array([10, 20, 5, 40, 30])

print(np.min(arr))

print(np.max(arr))

arr = np.array([10, 20, 30, 40, 50])

print(np.std(arr))

arr = np.array([10, 20, 30, 40, 50])

print(np.var(arr))

arr = np.array([50, 20, 80, 10, 60])

index = np.argmin(arr)

print(index)

index = np.argmax(arr)

print(index)

arr = np.array([10, 20, 30, 40])

print(np.cumsum(arr))

arr = np.array([2, 3, 4])

print(np.cumprod(arr))

marks = np.array([
    40, 50, 60, 70, 80,
    90, 100
])

print(np.percentile(marks, 50))

print(np.percentile(marks, 25))
print(np.percentile(marks, 75))


arr = np.array([
    10, 20, 20, 30, 30, 30
])

values, counts = np.unique(
    arr,
    return_counts=True
)

print(values)
print(counts)

arr = np.array([50, 20, 40, 10, 30])

sorted_arr = np.sort(arr)

print(sorted_arr)

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(np.sum(data, axis=0))

print(np.sum(data, axis=1))

result = np.mean(data, axis=1)

print(result.shape)

result = np.mean(
    data,
    axis=1,
    keepdims=True
)

print(result.shape)