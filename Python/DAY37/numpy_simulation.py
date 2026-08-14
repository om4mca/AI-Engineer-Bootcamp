import numpy as np

np.random.seed(42)

data = np.random.randint(
    0,
    2,
    size=10000
)

print(data.mean())