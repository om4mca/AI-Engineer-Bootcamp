# 🚀 AI Engineer Bootcamp - Day 13

## 📅 Date
18-07-2026

## 📚 Topics Covered

## Advanced OOP + Pythonic Programming


✅ Encapsulation (Deep Dive)
✅ Abstraction (Introduction)
✅ Magic (Dunder) Methods
✅ __str__()
✅ __repr__()
✅ Class Methods
✅ Static Methods
✅ Mini Project
✅ Bonus Project
✅ 20 Practice Programs
✅ Documentation
✅ Videos
✅ Notebook
✅ Interview Questions

---

## 💻 Programs

- encapsulation.py
- hospital_billing.py
- employee_payroll.py




---

## 🏥 Mini Project

Hospital Billing System


Features:

- Patient Information
- Consultation Fee
- Lab Fee
- Medicine Fee
- Discount
- GST (18%)
- Final Bill


---

## 🎯 Bonus Project

Employee Payroll System

Features

- Employee Details
- Basic Salary
- HRA
- DA
- Bonus
- Tax
- Net Salary


---

## 20 Practice Programs
- Private Variable
- Getter Method
- Setter Method
- Abstract Class
- Abstract Method
- __str__()
- __repr__()
- Class Method
- Static Method
- Bank Class
- Student Class
- Employee Class
- Patient Class
- Doctor Class
- Calculator Class
- Library Class
- Billing Class
- Payroll Class
- Hospital Class
- OOP Challenge

## 📖 Learning Resources

### Official Python Documentation



- Private Variables ✅
- Class Definitions ✅
- Class Objects ✅
- Class and Static Methods (overview) ✅


---

### Videos

FreeCodeCamp

- (OOP Advanced section) ✅

Microsoft Python

- Episode 39 --Scope ✅
- Episode 40 -- Returning Values ✅
- Episode 41 -- Default Parameters ✅

---


## 💡 What I Learned Today

 
- Encapsulation (Deep Dive) ,  Abstraction (Introduction),  Magic (Dunder) Methods, __str__(), __repr__()
- Class Methods
- Static Methods
- Mini Project : Hospital Billing System
- Bonus Project : Employee Payroll System


---

## 📂 GitHub

Day14 Completed Successfully ✅

## 🧠 Interview Preparation


### Q1.Here are clear, direct, interview-ready answers to your advanced Python OOP questions.

### 1. What is Encapsulation?
Encapsulation is the practice of bundling data (attributes) and the methods that operate on that data inside a single unit (a class), while restricting direct access to the inner workings. In Python, this is achieved by using a double underscore prefix (__variable), which hides the variable using name mangling and forces external code to interact via safe "gatekeeper" methods (getters and setters).

### 2. What is Abstraction?
Abstraction is the process of hiding complex implementation details and exposing only the essential interface to the user. It allows developers to use an object's tools without needing to understand the complex internal logic behind how those tools are constructed.

### 3. Difference between Encapsulation and Abstraction?
Encapsulation is about security and data safety: It wraps data tightly to hide the inner mechanics from accidental or unauthorized tampering ("How do I protect my data?").

Abstraction is about hiding complexity: It hides unnecessary details so the user sees a simple, clear public interface ("How do I make my system easy to use?").

Analogy: Encapsulation is the outer shell of a smartphone hiding the internal electrical circuitry so you can't touch it. Abstraction is the touch screen display that lets you place a call with one tap without knowing how cellular radio signals work.

### 4. What is __str__()?
__str__() is a built-in magic method used to define a user-friendly, highly readable string representation of an object. It is automatically triggered when you run print(object) or cast it using str(object). Its goal is to look clean and neat for an end-user.

### 5. What is __repr__()?
__repr__() (short for representation) is a magic method used to define an unambiguous, technical string representation of an object. It is meant for developers, debugging, and logging. It is triggered when you inspect an object in the terminal or use repr(object). Ideally, its output should look exactly like the Python code used to recreate the object (e.g., Patient(name='John', age=20)).

### 6. Difference between Class Method and Static Method?
Class Method (@classmethod): Bound to the class itself. It receives the class context (cls) as its first parameter, allowing it to modify class state or instantiate fresh objects.

Static Method (@staticmethod): Bound to neither the instance nor the class. It does not receive self or cls. It behaves exactly like an isolated, standard function that happens to live inside the class namespace.

### 7. What is @classmethod?
@classmethod is a built-in decorator applied to a function to turn it into a class method. Its primary real-world use case is acting as an alternative constructor (Factory Pattern). For example, it allows you to pass a raw JSON string or a comma-separated line from a text database, parse it, and return a completely initialized instance of the class.

### 8. What is @staticmethod?
@staticmethod is a built-in decorator applied to a function to mark it as a static method. It is used to group an isolated utility helper function inside a class because it makes logical sense to put it there, even though it doesn't need to read or write any variables within the class.

### 9. What are Dunder Methods?
Dunder methods (short for Double Underscore methods, like __init__, __str__, or __add__) are special, predefined methods in Python that start and end with two underscores. They are also known as Magic Methods. They allow you to plug your custom objects directly into Python’s built-in behaviors (like enabling math operators, loops, or custom printing features).

### 10. Where are these concepts used in real software?
Database Management (Django ORM / SQLAlchemy): @classmethod is heavily used to fetch rows from databases and convert them into Python class objects (e.g., User.objects.get(id=1)).

Web APIs and Data Validation (Pydantic / FastAPI): Encapsulation and setters validate inbound JSON payloads, throwing explicit validation errors instantly if ages are negative or email fields don't contain @ symbols.

Logging Frameworks: Production logging suites call __repr__() automatically when an application crashes, capturing exact variable dumps to diagnostic text documents so developers can pinpoint the failure immediately.