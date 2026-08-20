import numpy as np

np.random.seed(42)

data = np.random.normal(
    loc=70,
    scale=10,
    size=10000
)

print(data.mean())
print(data.std())