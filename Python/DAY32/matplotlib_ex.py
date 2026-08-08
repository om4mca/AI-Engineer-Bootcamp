import matplotlib.pyplot as plt

import matplotlib
print(matplotlib.__version__)

print()
print("******First Line Plot******")


x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

print(plt.plot(x, y))

print(plt.show())

print(plt.title("Sales Trend"))

print(plt.xlabel("Month"))

print(plt.ylabel("Sales"))



plt.plot(x, y)

plt.title("Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

print(plt.show())

print()
print("****Legend****")
plt.plot(
    x,
    y,
    label="Sales"
)

plt.legend()

print(plt.show())

print(plt.grid())

print()
print("****Figure****")

plt.figure(
    figsize=(8,5)
)

plt.plot(x, y)

plt.show()

print("***Save Chart***")
plt.savefig(
    "sales_chart.png"
)

plt.figure(
    figsize=(10,6)
)