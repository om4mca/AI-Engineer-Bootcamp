import pandas as pd

data = {
    "Name": ["Amit", "Rahul", "Priya"],
    "Age": [25, 30, 28],
    "Salary": [30000, 40000, 35000]
}

df = pd.DataFrame(data)

print(df)

import pandas as pd

data = {
    "Name": ["Amit", "Rahul", "Priya"],
    "Age": [25, 30, 28],
    "City": ["Delhi", "Mumbai", "Bhubaneswar"]
}

df = pd.DataFrame(data)

print(df)

data = [
    ["Amit", 25, "Delhi"],
    ["Rahul", 30, "Mumbai"],
    ["Priya", 28, "Bhubaneswar"]
]

df = pd.DataFrame(
    data,
    columns=["Name", "Age", "City"]
)

print(df)

data = [
    {
        "Name": "Amit",
        "Age": 25,
        "City": "Delhi"
    },
    {
        "Name": "Rahul",
        "Age": 30,
        "City": "Mumbai"
    },
    {
        "Name": "Priya",
        "Age": 28,
        "City": "Bhubaneswar"
    }
]

df = pd.DataFrame(data)

print(df)

df = pd.DataFrame(
    data,
    index=["EMP001", "EMP002", "EMP003"]
)
print(df.columns)

print(df.columns.tolist())

print(df.shape)
print(df.size)

print(df.dtypes)

df.info()

df.head()
df.head(3)

df.tail()

df.tail(3)

df.describe()

print(df["Name"])
print(df.Name)
df["Name"]

print(
    df[
        ["Name", "Age"]
    ]
)

print(df.iloc[0])
print(df.iloc[0:2])
print(df.loc["EMP001"])
