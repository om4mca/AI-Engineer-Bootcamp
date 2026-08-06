import pandas as pd

data = {
    "EmployeeID":["E001","E002","E003","E004","E005","E006","E007","E008"],
    "Department":["IT","HR","IT","Finance","HR","IT","Finance","IT"],
    "Age":[25,30,28,35,32,26,40,29],
    "Salary":[35000,45000,50000,60000,40000,55000,70000,48000]
}

df = pd.DataFrame(data)

print(df)

print(df.groupby("Department"))

print(df.groupby("Department").count())

print(df.groupby("Department")["Salary"].sum())

print(df.groupby("Department")["Salary"].mean())

print(df.groupby("Department")["Salary"].max())

print(df.groupby("Department")["Salary"].min())

print(df.groupby("Department")["Salary"].median())

print(df.groupby("Department")["Salary"].agg(
    ["count","sum","mean","min","max","median"]
))

print(df.groupby("Department")[["Salary","Age"]].mean())

print(df.groupby(
    ["Department","Age"]
).count())

print(df.groupby("Department").size())

print(df.groupby(
    "Department",
    as_index=False
).sum())

print(df.groupby(
    "Department",
    sort=False
).sum())

print(df.groupby("Department").agg(

TotalSalary=("Salary","sum"),

AverageSalary=("Salary","mean"),

MaximumSalary=("Salary","max"),

AverageAge=("Age","mean")

))

print(df["Department"].value_counts())