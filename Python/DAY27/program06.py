import pandas as pd

# 1. Default integer index
df1 = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30]})

print("Default Index:")
print(df1.index)


# 2. Custom string index
data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
df2 = pd.DataFrame(data, index=['Emp_1', 'Emp_2'])

print("\nCustom Index:")
print(df2.index)

# 3. Convert index to a Python list
index_list = df2.index.tolist()
print("\nIndex as a Python List:", index_list)