import matplotlib.pyplot as plt

departments = ["IT", "HR", "Finance"]
employees = [25, 15, 20]

plt.bar(
    departments,
    employees
)

plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Employees")

plt.show()

print()
print("*****Horizontal Bar Chart*****")

plt.barh(
    departments,
    employees
)

plt.show()