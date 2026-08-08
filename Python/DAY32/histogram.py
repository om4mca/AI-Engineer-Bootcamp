import matplotlib.pyplot as plt

ages = [22,25,25,28,30,30,31,35,36,40,42,45]

plt.hist(ages)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.show()