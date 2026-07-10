# 🚀 AI Engineer Bootcamp - Day 08

## 📅 Date
10-07-2026

## 📚 Topics Covered

## Functions

   - What is a Function
   - Create Your First Function
   - Function with Parameters
   - Function with Return Value
   - Default Parameters
   - Multiple Return Values
   - Variable Scope
---

## 💻 Programs

- function_basics.py


---

## 🏥 Mini Project

Hospital Billing Calculator


Features:

- calculate_consultation()

- calculate_medicine()

- calculate_total()

- print_bill()



---

## 🎯 Bonus Project

Employee Salary Calculator

Features

- calculate_bonus()

- calculate_tax()

- calculate_net_salary()

---

## 20 Practice Programs
- Programs 1–10
        - Create Function
        - Call Function
        - Function with Parameter
        - Function with Return
        - Function with Default Parameter
        - Function Returning Two Values
        - Function for Area of Circle
        - Function for Square
        - Function for Cube
        - Function for Maximum Number
Programs 11–20
        - Factorial Function
        - Prime Number Function
        - Fibonacci Function
        - Even Number Function
        - Odd Number Function
        - Employee Salary Function
        - Student Result Function
        - Hospital Bill Function
        - Calculator Function
        - Greeting Function

## 📖 Learning Resources

### Official Python Documentation

- Defining Functions ✅
- More on Defining Functions ✅
- Special Parameters (overview only) ✅

---

### Videos

FreeCodeCamp

- (Function Section) ✅

Microsoft Python

- Episode 21 -- Handling Multiple Conditions ✅
- Episode 22 -- Demo: Multiple Conditions ✅
- Episode 23 -- Complex Conditions ✅

---

## 💡 What I Learned Today

 
- Function
- Parameters
- Arguments
- Return
- Default Parameters
- Local Variable
- Global Variable

---

## 📂 GitHub

Day08 Completed Successfully ✅

## 🧠 Interview Preparation


### Q1.What is a function?

A function is a self-contained, reusable block of code designed to perform a specific task. You define it once, give it a name, and then "call" it by name whenever you need to run that code.

### 2.  Why do we use functions?

Reusability: Write code once and reuse it instead of copying and pasting.

Organization: Breaks huge, messy programs into small, manageable parts.

Maintainability: If a piece of logic breaks, you only have to fix it inside the function rather than everywhere it is used.

### 3. Difference between parameter and argument?

Parameter: The placeholder variable listed inside the parentheses when defining a function. 
(e.g., def greet(name): $\rightarrow$ name is the parameter).
Argument: The actual value you pass into the function when you call it. 
 (e.g., greet("Om") $\rightarrow$ "Om" is the argument).

### 4. Difference between print() and return?

print() just displays text on the screen for human eyes. It does not save the value for the program to use later.

return silently handovers a value back to the program. This allows you to store the result in a variable and pass it to another part of your code.

Think of print() as a store receipt (you can see it, but you can't buy something else with it) and return as actual cash handed back to you.

### 5. What is a local variable?

A local variable is a variable declared inside a function. It is temporary, only exists while that function is executing, and cannot be accessed from anywhere outside that function.

### 6. What is a global variable?

A global variable is a variable declared outside of all functions (usually at the top of your script). It can be read and accessed by any function throughout the entire file.

### 7. Can a function return multiple values?

Yes. In Python, you can separate multiple values with commas in your return statement (e.g., return length, width). Python automatically wraps these values into a single item called a tuple, which you can unpack when calling the function:

Python
area, perimeter = calculate_box(5, 10)

Python
#  Key      : Value
{"EMP001"   : "Alice Vance"}

### 8. What are default parameters?

They are fallback values assigned to a parameter in case the user forgets to provide an argument for it during a function call. For example, in def power(base, exponent=2):, if you don't provide an exponent, it defaults to squaring the number.

### 9.What is function scope?

Scope is the architectural rule book that determines where a variable can be seen or used. Function scope means that any variables or logic declared inside a specific function are completely invisible and locked away from the rest of your program.

### 10. Where are functions used in real software?

Functions are the fundamental building blocks of all modern software. Real-world examples include:

Authentication: A login_user(username, password) function that checks credentials.

E-Commerce: A calculate_tax(subtotal, state) function running at every digital checkout.

Social Media: A like_post(user_id, post_id) function that increments a like count in a database when you tap a screen.