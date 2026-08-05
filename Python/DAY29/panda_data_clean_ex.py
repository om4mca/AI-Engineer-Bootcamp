import pandas as pd
import numpy as np

data = {
    "EmployeeID": ["E001","E002","E003","E004","E005","E005"],
    "Name": ["Amit","Rahul",None,"Neha","Pooja","Pooja"],
    "Department": ["IT","HR","IT",None,"Finance","Finance"],
    "Age": [25,np.nan,28,35,30,30],
    "Salary": [35000,45000,None,60000,50000,50000]
}

df=pd.DataFrame(data)

print(df)

print()
print("***Detect Missing Values***")

print(df.isnull())

#print(df.isna())

print()
print("*****Detect Missing Values******")
print(df.isnull().sum())

print()
print("*****Check if Data Has Missing Values*****")
print(df.isnull().values.any())

print()
print("******Remove Missing Rows*****")
clean_df=df.dropna()
print(clean_df)

print()
print("******Remove Missing Columns*****")
clean_df=df.dropna(axis=1)
print(clean_df)

print()
print("******Fill Missing Values*****")
print(df.fillna(0))
print(df.fillna("Unknown"))

print()
print("******Fill Numeric Missing Values*****")
print(df["Age"].fillna(df["Age"].mean()))
print(df["Salary"].fillna(df["Salary"].mean()))

print()
print("******Fill Text Values*****")
print(df["Department"].fillna("Unknown"))

print()
print("******Forward Fill*****")
print(df.ffill())

print()
print("******Backward Fill*****")
print(df.bfill())

print()
print("******Duplicate Data*****")
print(df.duplicated())
print(df.duplicated().sum())

print()
print("******Remove Duplicate Data*****")
print(df.drop_duplicates())

print(df.drop_duplicates(subset="EmployeeID"))

print()
print("******Rename Columns*****")
print(df.rename(columns={
    "Name":"Employee_Name",
    "Salary":"Monthly_Salary"
}))

print()
print("******Change Data Type*****")
df["Age"] = df["Age"].astype("float")
print(df["Age"])

# df["Salary"] = df["Salary"].astype("int64")
# print(df["Salary"])


print()
print("******Unique Values*****")
print(df["Department"].unique())
print(df["Department"].nunique())

print()
print("******Value Counts*****")
print(df["Department"].value_counts())
