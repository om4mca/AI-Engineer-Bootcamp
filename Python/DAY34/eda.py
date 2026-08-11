import pandas as pd

df = pd.read_csv("E:/OM AI/AI-Engineer-Bootcamp/Python/DAY31//employee.csv")

print(df)

print(df.head())

print(df.tail())
print(df.shape)

print(df.columns)

print(df.dtypes)

print(df.info())

print(df.describe())

print(df.isnull().sum())

print(df.isna().sum())

print(df.duplicated().sum())
print(df[df.duplicated()])

print(df["Department"].unique())

print(df["Department"].nunique())

print(df["Department"].value_counts())

print(df["Salary"].describe())

import matplotlib.pyplot as plt

plt.hist(df["Salary"])

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")

plt.show()

df["Department"].value_counts().plot(
    kind="bar"
)

plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Employee Count")

plt.show()

plt.scatter(
    df["Age"],
    df["Salary"]
)

plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")

plt.show()
