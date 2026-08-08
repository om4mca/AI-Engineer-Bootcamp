import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "E:/OM AI/AI-Engineer-Bootcamp/Python/DAY31/employees.csv"
)

department_salary = (
    df.groupby("Department")["Salary"]
      .mean()
)

department_salary.plot(
    kind="bar"
)

plt.title(
    "Average Salary by Department"
)

plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.show()