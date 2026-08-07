
import pandas as pd
df = pd.read_csv("E:/OM AI/AI-Engineer-Bootcamp/Python/DAY31/employees.csv")
print(df)
print(df.head())

print(df.head(2))

print(df.tail(1))


print(df.info())

print(df.describe())

print(df.columns)
print(df.index)

print(df.to_csv(
    "clean_employee.csv",
    index=False
))


df = pd.read_excel(
    "E:/OM AI/AI-Engineer-Bootcamp/Python/DAY31/employees.xlsx"
)

print(df)

print(df.to_excel(
    "employee_report.xlsx",
    index=False
))

print(pd.read_csv(
    "E:/OM AI/AI-Engineer-Bootcamp/Python/DAY31/employees.csv",
    sep=";"
))

print(pd.read_csv(
   "E:/OM AI/AI-Engineer-Bootcamp/Python/DAY31/employees.csv",
    encoding="utf-8"
))

print(pd.read_csv(
    "E:/OM AI/AI-Engineer-Bootcamp/Python/DAY31/employees.csv",
    usecols=[
        "Name",
        "Salary"
    ]
))

print(pd.read_csv(
    "E:/OM AI/AI-Engineer-Bootcamp/Python/DAY31/employees.csv",
    skiprows=2
))

print(pd.read_csv(
    "E:/OM AI/AI-Engineer-Bootcamp/Python/DAY31/employees.csv",
    nrows=2
))

import os

print(os.path.exists(
    "E:/OM AI/AI-Engineer-Bootcamp/Python/DAY31/employees.csv",
))