import matplotlib.pyplot as plt

departments = [
    "Cardiology",
    "Orthopedic",
    "General",
    "Pediatrics"
]

patients = [
    120,
    95,
    150,
    80
]

plt.bar(
    departments,
    patients
)

plt.title(
    "Department-wise Patients"
)

plt.xlabel("Department")
plt.ylabel("Number of Patients")

plt.show()