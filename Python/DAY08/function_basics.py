# AI Engineer Bootcamp
# Day 8
# Program: Function Basics
# Author: Om Roy
# Date: 10-07-2026
#--------------------------------------------


def greet():
    print("Welcome to AI Engineer Bootcamp")

greet()

# Function with Parameters

def greet(name):
    print("Welcome", name)

greet("Om")

# Function with Return Value

def add(a,b):
    return a+b
result= add(10,40)
print(result)


#Default Parameters
print()
def welcome(name="Guest"):
    print("Hello", name)

welcome()
welcome("Om")

#Multiple Return Values
print()
def employee():
    return "Om", 90000

name, salary = employee()

print(name)
print(salary)

#Variable Scope
print()
company = "OpenAI"

def show():
    employee = "Om"
    print(company)
    print(employee)

show()

# end of the program