# 🚀 AI Engineer Bootcamp - Day 13

## 📅 Date
20-07-2026

## 📚 Topics Covered

## Professional Python Development
## Official Python Documentation

✅ Modules

   - Revision

 ✅ Packages
    - Revision

✅ Virtual Environments

   Understand:

        - Why virtual environments exist
        - Project isolation
         -Installing packages

---

## 💻 Programs

-pip_examples.py
- Hospital Management System
- Employee Management System




---

## 🏥 Mini Project

Hospital Management System


Features:

✅ OOP

✅ File Handling

✅ Exception Handling

✅ Modules

✅ Packages

Suggested Menu:

1 Register Patient

2 Search Patient

3 Display All Patients

4 Update Patient

5 Exit






---

## 🎯 Bonus Project

Employee Management System

Features:

- Add Employee
- Search Employee
- Update Employee
- Salary Calculation
- File Storage

Use modules and packages.



---

## 20 Practice Programs
- Create venv
- Activate venv
- Install package
- Create requirements.txt
- Import package
- Create module
- Create package
- Use package
- File structure
- Validator
- Patient model
- Employee model
- Billing module
- Search function
- Update function
- Error handling
- README improvements
- requirements.txt generation
- Project cleanup
- Final project run

## 📖 Learning Resources


### Videos

FreeCodeCamp

- (Modules / Packages / Virtual Environment section) ✅

Microsoft Python

- Episode 42 --Lists ✅
- Episode 43 -- Dictionaries ✅
- Episode 44 -- Importing Modules ✅

---


## 💡 What I Learned Today

 
- Learn pip
- Mini Project : Hospital Management System
- Bonus Project : Employee Management System


---

## 📂 GitHub

Day15 Completed Successfully ✅

## 🧠 Interview Preparation


### Q1. What is pip?
pip (Package Installer for Python) is Python’s standard package manager. It allows you to download, install, update, and manage third-party libraries and dependencies from the Python Package Index (PyPI) into your Python environment.

### 2. What is a virtual environment?
A virtual environment is an isolated workspace directory containing its own Python executable and installed packages. It operates independently of the global Python installation and other virtual environments on your computer.

### 3. Why use requirements.txt
requirements.txt is a text file that lists all third-party libraries and their exact versions required by a project. Using it ensures:

Reproducibility: Anyone running your code installs the exact same library versions.

Ease of Setup: New developers or server deployment scripts can install every dependency with a single command (pip install -r requirements.txt).

Clean Codebases: It keeps external package files out of version control (like Git), storing only the text list of references instead.

### 4. Difference between module and package?
Feature	Module	Package
Definition	A single Python file (.py) containing reusable code.	A directory (folder) containing multiple related Python modules.
Structure	File: math_utils.py	Directory: my_package/ containing an __init__.py file.
Import Syntax	import math_utils	from my_package import math_utils
### 5. How do you install a package?
To install a package from PyPI using pip, run the following command in your terminal:

Bash
pip install package_name
(For example: pip install requests or pip install pydantic)

### 6. What is pip freeze?
pip freeze is a terminal command that outputs a formatted list of all installed Python packages and their exact version numbers currently available in your active environment.

It is primarily used to generate the requirements.txt file by redirecting its output:

Bash
pip freeze > requirements.txt
### 7. How do you activate a virtual environment?
First, navigate to your project directory in the terminal, then run the activation script based on your operating system:

Windows (PowerShell):

PowerShell
.\.venv\Scripts\Activate.ps1
macOS / Linux:

Bash
source .venv/bin/activate
### 8. Why isolate project dependencies?
Isolating dependencies using virtual environments prevents version conflicts:

Project A might require Pydantic v1.10, while Project B requires Pydantic v2.6. Installing both globally would break one of the applications.

Isolation prevents accidental system-wide breaks when updating a package for a single project.

### 9. Explain Python project structure.
A standard, professional Python project structure follows a clean layout (often referred to as the src layout):

Plaintext
my_project/
├── .venv/                 # Isolated environment (ignored by Git)
├── .gitignore             # Tells Git what files to ignore (.venv, __pycache__)
├── README.md              # Documentation and setup instructions
├── requirements.txt       # Project dependencies
├── src/                   # Core application source code
│   └── my_app/            # Package directory
│       ├── __init__.py    # Marks directory as a package
│       ├── core.py        # Business logic
│       └── utils.py       # Helper functions
├── tests/                 # Automated unit tests
│   └── test_core.py
└── main.py                # Entry point script
### 10. How do teams share Python projects?
Teams collaborate and share Python projects by following these standard steps:

Version Control (Git & GitHub/GitLab): Push source code files, documentation, and requirements.txt to a shared repository.

Exclude Local Artifacts (.gitignore): Do not upload the .venv/ folder, database files, or __pycache__/ folders.

Environment Replication: Teammates clone the repository, create their own local virtual environment, and install dependencies using:

Bash
pip install -r requirements.txt