import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("E:/OM AI/AI-Engineer-Bootcamp/Python/DAY31//employee.csv")

summary = (
    df.groupby("Department")["Salary"]
      .mean()
)

summary.plot(
    kind="bar"
)

plt.title(
    "Average Salary by Department"
)

plt.ylabel("Average Salary")

plt.tight_layout()
plt.show()

