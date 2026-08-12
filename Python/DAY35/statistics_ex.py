import numpy as np

data = [10, 20, 30, 40, 50]

mean = np.mean(data)

print(mean)

data = [10, 20, 30, 40, 50]

median = np.median(data)

print(median)

from collections import Counter

data = [10, 20, 20, 30, 30, 30, 40]

mode = Counter(data).most_common(1)

print(mode)

data = [10, 20, 30, 40, 50]

data_range = max(data) - min(data)

print(data_range)

variance = np.var(data)

print(variance)

std = np.std(data)

print(std)

data = [10, 20, 30, 40, 50]

p50 = np.percentile(data, 50)

print(p50)

q1 = np.percentile(data, 25)
q2 = np.percentile(data, 50)
q3 = np.percentile(data, 75)

print(q3)

iqr = q3 - q1

print(iqr)


ages = [
    20, 22, 25, 27, 28,
    30, 32, 35, 40, 75
]

print("Mean:", np.mean(ages))
print("Median:", np.median(ages))
print("Std:", np.std(ages))
print("Min:", np.min(ages))
print("Max:", np.max(ages))