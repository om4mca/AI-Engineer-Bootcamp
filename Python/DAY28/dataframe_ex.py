import pandas as pd

data = {
    "EmployeeID": ["E001", "E002", "E003", "E004", "E005", "E006"],
    "Name": ["Amit", "Rahul", "Priya", "Neha", "Rohan", "Pooja"],
    "Department": [
        "IT",
        "HR",
        "IT",
        "Finance",
        "HR",
        "IT"
    ],
    "Age": [25, 30, 28, 35, 32, 26],
    "Salary": [35000, 45000, 50000, 60000, 40000, 55000]
}

df = pd.DataFrame(data)

print(df)

print(df["Name"])

print(df["Salary"])

df[
    ["Name", "Department", "Salary"]
]

print(df.iloc[0])
print(df.iloc[0:3])

print(df.iloc[[0, 2, 4]])



print(df.iloc[0:3, 1:4])

print(df.loc[0:2, ["Name", "Age"]])

print(df[df["Salary"] > 50000])

print(df[df["Age"] > 30])
print(df[df["Age"] < 30])
print(df[df["Age"] == 30])

print(df[
    df["Department"] == "IT"
])

print(df[
    df["Department"] == "HR"
])

print(df[
    (df["Department"] == "IT") &
    (df["Salary"] > 50000)
])

print(df[
    (df["Department"] == "IT") |
    (df["Department"] == "HR")
])

print(df[
    ~(df["Department"] == "IT")
])

print(df[
    (df["Age"] >= 25) &
    (df["Age"] <= 30)
])

print(df[
    (df["Salary"] >= 40000) &
    (df["Salary"] <= 60000)
])

print(df[
    df["Department"].isin(
        ["IT", "HR"]
    )
])

print(df[
    df["Name"].str.contains(
        "a",
        case=False
    )
])

print(df[
    df["Department"].str.startswith("I")
])

print(df[
    df["Department"].str.endswith("R")
])


print(df.sort_values(
    by="Salary"
))

print(df.sort_values(
    by="Salary",
    ascending=False
))

print(df.sort_values(
    by=["Department", "Salary"]
))

print(df.sort_values(
    by=["Department", "Salary"],
    ascending=[True, False]
))

print(df.sort_index())

print(df.sort_index(
    ascending=False
))

filtered_df = df[
    df["Salary"] > 40000
]

filtered_df = filtered_df.reset_index(
    drop=True
)

print(filtered_df)

print(df.query(
    "Salary > 50000"
))

print(df.query(
    "Age > 25 and Salary > 40000"
))

print(df.query(
    "Department == 'IT'"
))