import pandas as pd

marks = pd.Series([80, 75, 92, 88])

print(marks)

marks = pd.Series(
    [80, 75, 92, 88],
    index=["Amit", "Rahul", "Priya", "Neha"]
)

print(marks)

print(marks.iloc[0])

print(marks.loc["Amit"])

print()
print("********Series Slicing*******")

marks = pd.Series(
    [80, 75, 92, 88],
    index=["Amit", "Rahul", "Priya", "Neha"]
)
print(marks.iloc[0:2])

print(marks.loc["Amit":"Priya"])

print()
print("******Series Operations******")  
marks = pd.Series([80, 75, 92, 88])

print(marks + 5)
print(marks * 2)
print(marks > 80)

print()
print("******Series Filtering******")

marks = pd.Series([80, 75, 92, 88])

result = marks[marks > 80]

print(result)

print(marks.mean())

print(marks.sum())
print(marks.mean())
print(marks.median())
print(marks.min())
print(marks.max())
print(marks.std())
print(marks.count())

print(marks.index)
print(marks.values)
print(marks.dtype)
print(marks.shape)
print(marks.size)