import numpy as np

n = 10
p = 0.8

results = np.random.binomial(
    n,
    p,
    size=1000
)

print(results)

import matplotlib.pyplot as plt

plt.hist(
    results,
    bins=range(0, n + 2)
)

plt.title("Binomial Distribution")
plt.xlabel("Number of Successes")
plt.ylabel("Frequency")

plt.show()