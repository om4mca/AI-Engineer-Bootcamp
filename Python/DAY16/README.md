# 🚀 AI Engineer Bootcamp - Day 13

## 📅 Date
21-07-2026

## 📚 Topics Covered

## Lambda Functions

## map()

## filter()

## reduce()

## Mini Project

## Bonus Project

## Practice Programs

## Key Learnings

## Interview Questions

## How to Run


## Official Python Documentation

✅ Lambda Expressions
✅ map()
✅ filter()
✅ functools.reduce()

---

## 💻 Programs

- lambda_basics.py
- map_examples.py
- filter_examples.py
- reduce_examples.py
- hospital_data_processing.py
- employee_salary_processing.py

- program01.py
- program02.py
...
- program20.py




---

## 🏥 Mini Project

Hospital Patient Data Processing System


Implement:

✅ Find patients whose age is greater than 40.

✅ Create a list containing only patient names.

✅ Sort patients by bill amount.

✅ Calculate total hospital revenue.



---

## 🎯 Bonus Project

Employee Salary Processing System

Implement:

- Employees with salary > ₹60,000.
- Increase salary by 10%.
- Sort employees by salary.
- Calculate total salary expense.



---

## 20 Practice Programs
- Lambda Square
- Lambda Cube
- Lambda Addition
- Lambda Maximum
- Lambda Even/Odd
- map() Square
- map() Cube
- map() Salary Increase
- filter() Even Numbers
- filter() Odd Numbers
- filter() Age > 18
- filter() Salary > 50000
- reduce() Sum
- reduce() Product
- Sort Numbers
- Sort Names
- Sort Employees by Salary
- Sort Patients by Age
- Calculate Total Hospital Bill
- Combined map() + filter() + reduce()

## 📖 Learning Resources


### Videos

FreeCodeCamp

- (Lambda / Functional Programming Section) ✅


---


## 💡 What I Learned Today

 
- Lambda Functions
- Mini Project : Hospital Patient Data Processing System
- Bonus Project : Employee Salary Processing System


---

## 📂 GitHub

Day16 Completed Successfully ✅

## 🧠 Interview Preparation


### Q1. What is a Lambda Function?

An anonymous (nameless), single-line function designed for short, disposable operations without defining a full def function.

### 2. What is the syntax of Lambda?

Pythonlambda arguments: expression

### 3. Lambda vs. Normal Function?

Feature           Lambda FunctionNormal       Function (def)NameAnonymousExplicitly namedLengthStrictly 1 lineMulti-lineReturnImplicit (automatic)Explicit (return statement)Use CaseQuick inline callbacksComplex, reusable logic


### 4. What is map()?
A higher-order function that applies a given function to every element in an iterable and returns a 1-to-1 transformed iterator.

### 5. What is filter()?
A higher-order function that tests each element in an iterable against a condition, keeping only items where the condition returns True.

### 6. What is reduce()?
A higher-order function that repeatedly applies a function pairwise across elements to condense/fold an entire collection down into a single final value.

### 7. Where does reduce() come from?
It lives in Python's standard functools module:

Python
from functools import reduce

### 8. Can Lambda have multiple arguments?
Yes. Separate them with commas:
### 9. Can Lambda contain multiple statements?No. A lambda can only contain a single expression. Statements like assignments (x = 5), loops (for/while), or multiple code lines are not allowed.

### 10. How do you sort a list using Lambda?
Pass the lambda as the key parameter in sorted() or .sort():

Python
patients = [{"name": "Om", "age": 42}, {"name": "Priya", "age": 28}]

# Sort by age
sorted_patients = sorted(patients, key=lambda p: p["age"])

### 11. How do you filter a list using Lambda?
Pass the lambda condition into filter():

Python
numbers = [10, 25, 5, 40, 15]

# Keep numbers > 15
high_nums = list(filter(lambda x: x > 15, numbers))  # [25, 40]

### 12. Real-world use case of map()
Parsing API data / Data formatting:
Converting a list of string prices received from a web service into floats:

Python
raw_prices = ["$12.50", "$9.99", "$100.00"]
clean_prices = list(map(lambda p: float(p.replace("$", "")), raw_prices))
# Output: [12.5, 9.99, 100.0]

### 13. Real-world use case of filter()
Data cleaning / Removing invalid inputs:
Filtering out missing (None) or inactive user accounts before processing orders:

Python
users = [
    {"username": "alice", "is_active": True},
    {"username": "bob", "is_active": False},
    {"username": "charlie", "is_active": True}
]

active_users = list(filter(lambda u: u["is_active"], users))

### 14. Why should Lambda not be overused?
Hurts Readability: Complex logic packed into one line becomes "write-only" code.

Harder to Debug: Error stack traces only show <lambda> instead of a clear function name.

