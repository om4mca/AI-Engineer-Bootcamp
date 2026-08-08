import matplotlib.pyplot as plt

months = [1,2,3,4,5]
sales = [100,120,150,170,200]
expenses = [80,90,110,130,150]

plt.plot(
    months,
    sales,
    label="Sales"
)

plt.plot(
    months,
    expenses,
    label="Expenses"
)

plt.title("Sales vs Expenses")
plt.xlabel("Month")
plt.ylabel("Amount")

plt.legend()
plt.grid()

plt.show()