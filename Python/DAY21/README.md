# 🚀 AI Engineer Bootcamp - Day 20

## 📅 Date
27-07-2026

## 📚 Topics Covered

## Python Project Architecture

## Separation of Concerns

## Models

## Services

## Utilities

## Managers

## Exception Handling

## Decorators

## Generators

## Context Managers

## File Handling

## Mini Project

## Bonus Project

## Practice Programs

## Key Learnings

## Interview Questions

## How to Run

## Official Python Documentation


- OOP ✅
- Generators ✅
- Decorators ✅
- Exception Handling ✅



---

## 💻 Programs

- models/patient.py
- models/employee.py
- utils/validators.py
- utils/decorators.py
- services/patient_service.py
- managers/file_manager.py
- main.py
- hospital_system
- employee_system

- program01.py
- program02.py
...
- program15.py

- README.md


---

## 🏥 Mini Project

Hospital Patient Management System — Version 2


## 🎯 Bonus Project

Employee Management System — Professional Version



---

## 15 Practice Programs
- 1. Function + List Integration
- 2. Dictionary + Function
- 3. Class + List
- 4. Class + Exception
- 5. Inheritance + Method Overriding
- 6. Module + Function
- 7. Package + Module
- 8. File Handling + Exception
- 9. Generator + List
- 10. Decorator + Function
- 11. Context Manager + File
- 12. OOP + File Handling
- 13. Decorator + Exception Handling
- 14. Generator + File Processing
- 15. Complete Mini Application Integration

## 📖 Learning Resources


### Videos

FreeCodeCamp

- (Functions / OOP / Exception Handling / Generators / Decorators) ✅


---


## 💡 What I Learned Today

✅ Revision Previous Topics
✅ Mini Project
✅ Bonus Project


---

## 📂 GitHub

Day21 Completed Successfully ✅

## 🧠 Interview Preparation




1. What is Separation of Concerns?
Separation of Concerns (SoC) is a core design principle where a program is split into distinct, non-overlapping sections. Each section (or layer) is responsible for a single aspect of the application's functionality. For instance, data storage, user interface, and business rules should each live in separate components.

2. Why should we divide a Python application into modules?
Maintainability: Small, focused files are easier to read, debug, and update.

Reusability: Functions and classes written in one module can be imported across multiple parts of the app without duplicating code.

Collaboration: Multiple developers can work on different modules simultaneously without causing git merge conflicts.

Testing: Smaller components can be unit-tested in isolation.

3. What is the role of a Model?
A Model represents the domain data and schema of an application (e.g., Patient, Employee, Invoice). Its primary roles are:

Defining object attributes and properties.

Enforcing data validation rules (e.g., preventing negative salaries or invalid emails).

Converting objects to and from database formats or raw dictionaries (serialization).

4. What is the role of a Service?
The Service Layer encapsulates the core business logic and workflows of the application. It acts as the coordinator:

It receives requests from the interface (CLI, Web API, UI).

It fetches or creates Models.

It performs calculations, validations, and decisions.

It tells Managers/Persistence layers when to save or update data.

5. What is the purpose of a Utility module?
A Utility module contains generic, reusable helper functions that do not belong to a specific business domain. Examples include string formatters, date/time parsers, encryption functions, or logging setup wrappers.

6. What is a Context Manager?
A Context Manager is a mechanism (accessed using the with statement) that manages setup and cleanup phases around a block of code.

Purpose: Ensures resources like files, database connections, or thread locks are safely opened and guaranteed to close, even if an exception occurs mid-execution.

7. What is a Generator?
A Generator is a special type of iterator created using the yield keyword.

Purpose: Instead of computing an entire dataset and storing it in memory at once (like a list), a generator evaluates data lazily—one item at a time. This keeps RAM usage minimal when processing massive files or streams.

8. What is a Decorator?
A Decorator is a function that wraps another function to modify or extend its behavior without altering its underlying source code.

Purpose: Useful for cross-cutting concerns like measuring function execution time, logging operations, checking authorization, or retrying failed network requests.

9. How can these concepts work together?
They build an end-to-end pipeline where each tool handles a specific layer:

A Decorator logs execution and handles runtime errors.

The Service coordinates the business logic.

It validates input using a Model.

A Generator streams large data files line-by-line.

A Context Manager inside a Manager safely writes the processed results to disk.

10. Why is modular architecture important?
Without a modular architecture, applications degrade into monolithic "spaghetti code"—where UI logic, database queries, and business rules are tangled in a single file. Modular architecture prevents this by ensuring that changes in one part of the system (e.g., swapping a CSV file for a SQL database) do not break unrelated parts (e.g., validation rules or UI screens).

11. What is if __name__ == "__main__"?
This conditional check checks whether a Python script is being executed directly or imported as a module:

If you run python main.py, __name__ is automatically set to "__main__", and the code inside the block executes.

If another file writes import main, __name__ becomes "main", and the block is skipped—preventing scripts from running automatically during imports.

12. What is the difference between a module and a package?
Module: A single Python file (.py) containing code.

Package: A directory containing multiple modules (and an __init__.py file) grouped under a single folder name.

13. How do you handle exceptions in a large application?
Define Custom Exception Hierarchies: Create a base class (e.g., AppError(Exception)) and child classes (e.g., ValidationError, UserNotFoundError).

Catch Specifically: Catch precise exceptions at the lowest necessary layer rather than using bare except:.

Centralize with Decorators or Middleware: Intercept unhandled exceptions at the top layer (CLI or API framework) to log stack traces and return clean, user-friendly messages.

14. Why should business logic be separated from the main program?
The main program (CLI/UI) should only be concerned with getting user input and presenting output.

If business logic is embedded inside main.py:

You cannot easily swap the interface (e.g., migrating a CLI app to a FastAPI web backend) without rewriting all your business rules.

You cannot write automated unit tests for your logic without simulating manual user input.

15. How would you design a Python application for a hospital?
A clean architecture for a Hospital Patient System would look like this:

Plaintext
hospital_system/
│
├── exceptions.py       # Custom errors (PatientNotFoundError, ValidationError)
├── decorators.py       # @log_operation, @require_auth
├── models/
│   └── patient.py      # Patient class schema & field validation rules
├── managers/
│   └── file_manager.py # Safe context manager to save/load JSON or CSV records
├── services/
│   └── patient_service.py # Core business rules (admit, discharge, assign doctor)
└── main.py             # CLI / Web interface and entry point
Flow:

User enters data in main.py.

main.py passes the request to PatientService.

PatientService instantiates a Patient model (which runs validate()).

@log_operation logs the attempt.

FileManager uses a with context manager to safely persist the updated patient record to disk.