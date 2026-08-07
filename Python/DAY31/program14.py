import pandas as pd

df = pd.read_excel(
    "E:/OM AI/AI-Engineer-Bootcamp/Python/employees.xlsx"
)

print(df)

print(df.to_excel(
    "employee_report.xlsx",
    index=False
))
