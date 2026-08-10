import matplotlib.pyplot as plt


print("*******Multiple Plots**********")

months = [1, 2, 3, 4, 5]

sales = [100, 120, 150, 130, 170]
expenses = [80, 90, 110, 100, 120]

plt.subplot(2, 1, 1)

plt.plot(months, sales)
plt.title("Sales")

plt.subplot(2, 1, 2)

plt.plot(months, expenses)
plt.title("Expenses")

plt.tight_layout()
plt.show()

print()
print("***Multiple Charts in One Figure***")
fig, ax = plt.subplots(2, 1)

ax[0].plot(months, sales)
ax[0].set_title("Sales")

ax[1].plot(months, expenses)
ax[1].set_title("Expenses")

plt.tight_layout()
plt.show()

print()
print("*******Bar Chart Customization******")
departments = [
    "IT",
    "HR",
    "Finance",
    "Sales"
]

employees = [
    25,
    15,
    20,
    30
]

plt.bar(
    departments,
    employees
)

plt.title("Department-wise Employees")
plt.xlabel("Department")
plt.ylabel("Employees")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

print("****Horizontal Bar Chart*********")
plt.barh(
    departments,
    employees
)

plt.xlabel("Employees")
plt.ylabel("Department")

plt.title(
    "Employees by Department"
)

plt.show()

print("********Histogram Customization***********")
ages = [
    22, 24, 25, 25, 27,
    28, 30, 31, 32, 35,
    38, 40, 42
]

plt.hist(
    ages,
    bins=5
)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.show()

print("*******Scatter Plot Customization*****")
age = [22, 25, 28, 30, 35, 40]

salary = [
    25000,
    30000,
    35000,
    40000,
    50000,
    60000
]

plt.scatter(
    age,
    salary
)

plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Age vs Salary")

plt.grid()

plt.show()