# 🚀 AI Engineer Bootcamp - Day 09

## 📅 Date
11-07-2026

## 📚 Topics Covered

## Functions

✅  Python Modules
✅ Creating Your Own Modules
✅ Import Statement
✅ Packages
✅ Built-in Modules
✅ math
✅ random
✅ datetime
✅ Mini Project
✅ 20 Practice Programs
---

## 💻 Programs

- calculator.py
- main.py
- hospital_utils.py
- employee_utils.py


---

## 🏥 Mini Project

Hospital Utility Library


Features:

- generate_patient_id()

- calculate_age()

- calculate_bill()

- current_date()



---

## 🎯 Bonus Project

Employee Utility Library

Features

- calculate_bonus()

- calculate_tax()

- calculate_salary()

- generate_employee_id()

---

## 20 Practice Programs
- Import math
- Square Root
- Factorial
- PI Value
- Random Number
- Current Date
- Current Time
- Create Module
- Import Module
- Import Function
- Alias Module
- Create Package
- Call Package Function
- Employee Module
- Hospital Module
- Calculator Module
- Student Module
- Billing Module
- Random OTP Generator
- Digital Clock

## 📖 Learning Resources

### Official Python Documentation

- Modules ✅
- Packages ✅
- import ✅
- Standard Library (overview) ✅

---

### Videos

FreeCodeCamp

- (Module Section) ✅

Microsoft Python

- Episode 24 -- Demo: Complex Conditions ✅
- Episode 25 -- Collections ✅
- Episode 26 -- Demo: Collections ✅

---

## 💡 What I Learned Today

 
- Create Module
- Import Module
- Alias
- Built-in Modules
- Create Package
- Mini Project :- Hospital Utility Library
- Bonus Project :- Employee Utility Library

---

## 📂 GitHub

Day09 Completed Successfully ✅

## 🧠 Interview Preparation


### Q1.What is a module?
A module is a single Python file (ending in .py) containing executable code, functions, classes, or variables. It acts as a standalone library that allows you to organize related code into one file.

### 2. What is a package?
A package is a collection of multiple Python modules organized inside a directory (folder) structure. Packages allow you to group related modules together under a shared namespace using dot notation (e.g., import package.module).

### 3. Difference between a module and a package?
A module is a single file.

A package is a folder that contains multiple modules (and potentially sub-folders/sub-packages). Think of a module as a tool, and a package as an entire toolbox.

### 4. Why do we use import?
We use import to bring code written in external modules or packages into our current script. This allows us to use functions, classes, and variables from other files without having to rewrite or copy-paste them, saving memory and development time.

### 5. Difference between import and from ... import?
import module loads the entire module. To use its features, you must use dot notation (e.g., math.sqrt(16)). This keeps the code clean and explicit.

from module import function extracts only a specific component from that module directly into your workspace. You call it without a prefix (e.g., sqrt(16)). While convenient, doing this with too many functions can cause naming conflicts if two modules have functions with the exact same name.

### 6. What is aliasing?
Aliasing is the process of renaming a module or function locally at the time of import using the as keyword. It is used to shorten long package names or prevent naming conflicts with variables you’ve already created in your current script.

Python
import datetime as dt  # 'dt' is an alias for datetime
### 7. Name some built-in modules.
Python comes with hundreds of built-in modules ready to use out of the box. Some common ones include:

math (advanced arithmetic)

random (generating pseudo-random choices/numbers)

datetime (date and time tracking)

os (interacting with your operating system and files)

sys (handling system-specific parameters and arguments)

json (parsing text data interchange formats)

### 8. What is the Standard Library?
The Standard Library is the massive collection of built-in modules, packages, and data types that come bundled automatically with every single Python installation. It provides immediate solutions for common programming tasks (like math, networking, file handling, and cryptography) without forcing you to download third-party software.

### 9. Why do we create reusable modules?
Maintainability: If a bug occurs, you only have to fix it once inside the module, and it automatically updates everywhere that module is used.

Readability: It stops files from becoming massive "walls of text," breaking them into clean, logical segments.

Efficiency: Multiple developers can work on different modules simultaneously without stepping on each other's toes.

### 10. Where are modules used in real software?
In real-world commercial software, programs are entirely built out of modules. Examples include:

E-Commerce Apps: An application will separate its logic into a billing_mod.py (payment calculations), a cart_mod.py (handling inventory item selections), and a notify_mod.py (sending receipt emails).

Video Games: Separate modules handle graphics rendering, player physics, and audio controls independently.

Data Science Pipelines: Data operations are typically split into isolated modules for data cleaning, model training, and metric logging.