import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(
    loc=70,
    scale=10,
    size=10000
)
plt.hist(
    data,
    bins=30
)

plt.title("Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.show()


print("***Calculate Z-Scores in Python***")
mean = data.mean()
std = data.std()

z_scores = (data - mean) / std

print(z_scores[:10])

print()
print("******")