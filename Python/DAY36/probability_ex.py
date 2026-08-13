import random

print("***Probability with Python*******")

result = random.choice(["Heads", "Tails"])

print(result)

import random

print("***Dice Simulation*******")

result = random.randint(1, 6)

print("Dice:", result)

print("***Probability Through Simulation*******")

import random

rolls = []

for i in range(1000):
    rolls.append(random.randint(1, 6))

six_count = rolls.count(6)

probability = six_count / len(rolls)

print(probability)

print("***NumPy Simulation***")

import numpy as np

rolls = np.random.randint(
    1,
    7,
    size=10000
)

six_count = np.sum(rolls == 6)

probability = six_count / len(rolls)

print(probability)

print("***Probability Distribution Visualization***")
import matplotlib.pyplot as plt

plt.hist(
    rolls,
    bins=6
)

plt.title("Dice Roll Distribution")
plt.xlabel("Dice Value")
plt.ylabel("Frequency")

plt.show()