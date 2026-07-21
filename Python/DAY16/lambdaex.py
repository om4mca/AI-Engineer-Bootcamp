#Normal Function:

def square(x):
    return x * x

#Lambda:

print()
print("*****Lambda Function**********")
square = lambda x: x * x

print(square(5))

# syntax:
#lambda arguments: expression

#Lambda function का purpose है छोटे, simple operations को concise तरीके से लिखना।

#Multiple Arguments

print()
print("********Multiple Arguments*******")
add = lambda a, b: a + b

print(add(10, 20))

#Lambda with Condition
print()
print("*****Lambda with Condition******")
check_even = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check_even(10))

#map()
# map() का use collection के हर item पर operation apply करने के लिए किया जाता है।
print()
print("********map() Function***********")
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))

print(squares)

# filter()
# filter() का use condition के आधार पर data filter करने के लिए किया जाता है।
print()
print("*****filter()*****")
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(
    filter(lambda x: x % 2 == 0, numbers)
)

print(even_numbers)

#  reduce()
# reduce() functools module से आता है।

print()
print("***** reduce() ***** ")
from functools import reduce

numbers = [1, 2, 3, 4, 5]

total = reduce(
    lambda x, y: x + y,
    numbers
)

print(total)


# Lambda with sort()
print()
print("****** Lambda with sort()********")
employees = [
    {"name": "Om", "salary": 50000},
    {"name": "Rahul", "salary": 70000},
    {"name": "Priya", "salary": 60000}
]

employees.sort(
    key=lambda employee: employee["salary"]
)

print(employees)