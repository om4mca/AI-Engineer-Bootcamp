# 🚀 AI Engineer Bootcamp - Day 10

## 📅 Date
13-07-2026

## 📚 Topics Covered

## Exception Handling


✅ try
✅ except
✅ else
✅ finally
✅ Multiple Exceptions
✅ Raising Exceptions (raise)
✅ Custom Exceptions (Introduction)
✅ Mini Project
✅ 20 Practice Programs
---

## 💻 Programs

- try_except.py
- hospital_registration.py
- bank_account.py



---

## 🏥 Mini Project

Hospital Registration System


Features:

- Enter Patient Name
- Enter Age
- Enter Mobile Number
- Enter Consultation Fee

Validation:

- Age must be positive
- Mobile must contain 10 digits
- Fee cannot be negative



---

## 🎯 Bonus Project

Bank Account Simulator

Features

- Deposit
- Withdraw
- Balance Check

Handle:

- Invalid Amount
- Negative Deposit
- Insufficient Balance

---

## 20 Practice Programs
- Handle ValueError
- Handle ZeroDivisionError
- Handle FileNotFoundError
- Multiple Exceptions
- try-else
- try-finally
- raise ValueError
- Custom Exception
- Safe Division
- Safe Input
- ATM PIN Validation
- Employee Salary Validation
- Student Marks Validation
- Hospital Fee Validation
- Login Retry
- Age Verification
- Bank Withdrawal
- Calculator with Exception Handling
- File Reader
- Patient Registration

## 📖 Learning Resources

### Official Python Documentation

- Errors and Exceptions ✅
- Raising Exceptions ✅
- User-defined Exceptions ✅

---

### Videos

FreeCodeCamp

- (Exception Handling Section) ✅

Microsoft Python

- Episode 27 -- Loops ✅
- Episode 28 -- Demo: Loops ✅
- Episode 29 -- Introducing Functions ✅

---

## 💡 What I Learned Today

 
- Exception Handling (try, except, else, finally, Multiple Exceptions)
- Mini Project :- Hospital Registration System
- Bonus Project :- Bank Account Simulator

---

## 📂 GitHub

Day10 Completed Successfully ✅

## 🧠 Interview Preparation


### Q1.What is an exception?
An exception is an error that occurs during the execution (runtime) of a program. Even if the code is written with perfect syntax, Python can encounter an unexpected condition it cannot handle by itself—such as trying to open a missing file, or dividing a number by zero. When this happens, Python creates an "Exception Object" and halts the program unless it is handled.

### 2. Why do we use try-except?
We use try-except blocks for graceful error handling and crash prevention. Without them, any minor runtime error will instantly crash the application, losing all unsaved data in memory. By implementing try-except, you can catch the error, inform the user with a friendly notification, log the issue for developers, and keep the application running.

### 3. Difference between a syntax error and an exception?
Syntax Error: Occurs before the code runs (during parsing). It means you broke the grammatical rules of the programming language (e.g., forgetting a colon :, typos in keywords like whlie, or mismatched parentheses). The program will refuse to start.

Exception: Occurs while the code is running (at runtime). The code has flawless grammar and syntax, but a specific line encounters an impossible operation during execution (e.g., trying to add a string to an integer).

### 4. What is ValueError?
A ValueError is a built-in Python exception raised when a function receives an argument of the correct data type, but an inappropriate value.

Example: If you pass a string to the int() function, the data type (string) is acceptable because int() accepts strings, but the value "apple" cannot be mathematically converted into a number.

Python
age = int("apple")  # Raises ValueError
### 5. What is ZeroDivisionError?
A ZeroDivisionError is a specific built-in mathematical exception raised when the denominator in a division or modulo operation evaluates to exactly zero. Because division by zero is mathematically undefined, Python halts the calculation.

Python
result = 50 / 0  # Raises ZeroDivisionError
### 6. What is finally?
finally is a structural block placed at the end of a try-except architecture. It is guaranteed to run, no matter what happens. Whether the try block succeeds perfectly, or an except block catches an error, or even if the script encounters an unhandled crash—the code inside finally executes. It is primarily used for critical system cleanup tasks, like closing database connections or freeing file handles.

### 7. What is raise?
The raise keyword is used to manually trigger/emit an exception. You use it when a user input or state passes language validations but violates your specific business rules.

Python
if user_age < 0:
    raise ValueError("Age cannot be negative!") # Forces the program to go to an except block
### 8. What is a custom exception?
A custom exception is a user-defined error class that inherits from Python's built-in Exception class. It is used when Python's default exceptions (like ValueError) are too generic to describe a specific business logic failure. Custom exceptions make code self-documenting and easier to debug.

Python
class InsufficientFundsError(Exception): 
    pass  # Custom error specific to a banking application
### 9. Can we have multiple except blocks?
Yes. You can chain multiple except blocks together following a single try statement, just like an if-elif-else ladder. This allows you to handle different types of failures uniquely. Python will check them in order from top to bottom and execute the first matching exception block.

Python
try:
    # Code that could fail in multiple ways
except ValueError:
    # Handles bad inputs
except ZeroDivisionError:
    # Handles division issues
### 10. Where is exception handling used in real software?
In production systems, exception handling is used everywhere to build resilient, fault-tolerant software:

**Web Applications & APIs:** If a database query fails or a network timeout happens, a try-except block prevents the entire website from going down, showing the user a clean 500 Internal Server Error page instead of raw code.

**Authentication Systems**: To lock an account temporarily after too many failed password attempts without crashing the underlying app.

**File Upload & Systems Processing**: To catch issues like a user uploading a corrupted file, running out of disk space, or a network disconnection mid-transfer.

**Payment Gateways**: To safely catch credit card declines, bank timeouts, or network loss midway through charging a customer, ensuring money isn't lost or double-charged.