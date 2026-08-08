
import matplotlib.pyplot as plt

age = [22,25,28,30,35,40]
salary = [25000,30000,35000,40000,50000,60000]

plt.scatter(
    age,
    salary
)

plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")

plt.show()

