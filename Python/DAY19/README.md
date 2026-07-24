# 🚀 AI Engineer Bootcamp - Day 13

## 📅 Date
24-07-2026

## 📚 Topics Covered

## Functions as Objects

## Higher-Order Functions

## Nested Functions

## Closures

## Decorators

## @decorator Syntax

## *args and **kwargs

## functools.wraps

## Multiple Decorators

## Mini Project

## Bonus Project

## Practice Programs

## Key Learnings

## Interview Questions

## How to Run

## Official Python Documentation


- Decorator basics ✅
- Function definitions ✅
- *args ✅
- **kwargs ✅
- functools ✅
- functools.wraps ✅


---

## 💻 Programs

- decorator_basics.py
- function_as_object.py
- higher_order_function.py
- nested_function.py
- closure_example.py
- args_kwargs_decorator.py
- wraps_example.py
- timer_decorator.py
- hospital_access_decorator.py
- employee_salary_audit.py

- program01.py
- program02.py
...
- program15.py

- README.md


---

## 🏥 Mini Project

Hospital Access Logging Decorator


## 🎯 Bonus Project

Employee Salary Audit Decorator



---

## 15 Practice Programs
- Simple Decorator
- Before/After Decorator
- Function Logger
- Execution Timer
- *args Decorator
- **kwargs Decorator
- *args + **kwargs Decorator
- functools.wraps
- Permission Decorator
- Authentication Decorator
- Logging Decorator
- Hospital Access Decorator
- Employee Audit Decorator
- Multiple Decorators
- Timing + Logging Combined Decorator

## 📖 Learning Resources


### Videos

FreeCodeCamp

- (Decorators / Advanced Functions Section) ✅


---


## 💡 What I Learned Today

Functions as Objects
✅ Higher-Order Functions
✅ Nested Functions
✅ Closures
✅ Decorators
✅ @decorator Syntax
✅ *args
✅ **kwargs
✅ Decorators with Arguments
✅ Multiple Decorators
✅ functools.wraps
✅ Practical Projects
✅ Interview Questions


---

## 📂 GitHub

Day19 Completed Successfully ✅

## 🧠 Interview Preparation


### 1. What is a Decorator?
A Decorator is a structural pattern in Python that allows you to wrap another function to extend or modify its behavior without changing the original function's source code.

### 2. Why are Decorators used?
Code Reusability: Apply identical cross-cutting logic (e.g., logging, permissions) across dozens of functions without repeating code (DRY principle).

Separation of Concerns: Keeps your core business logic clean by isolating secondary concerns (like performance tracking or authentication).

Maintainability: Updating a single decorator automatically updates the behavior of all functions using it.

### 3. What is a Higher-Order Function?
A Higher-Order Function is any function that either:

Receives one or more functions as arguments.

Returns a function as its result.

Because Python treats functions as first-class citizens (like strings or integers), decorators are inherently higher-order functions.

### 4. What is a Nested Function?
A Nested Function (or inner function) is a function declared inside the scope of another function. It is only accessible within the enclosing function unless explicitly returned.

### 5. What is a Closure?
A Closure is created when an inner function remembers variables from its outer enclosing function's scope, even after the outer function has completed execution and returned.

Decorators rely entirely on closures to remember which target function (func) they are wrapping.

### 6. What does @decorator mean?
The @decorator syntax placed above a function definition is syntactic sugar (a cleaner syntax shortcut).

Writing:

Python
@my_decorator
def my_function():
    pass
Is exact identical shorthand for:

Python
def my_function():
    pass

my_function = my_decorator(my_function)
### 7. What is a Wrapper Function?
A Wrapper Function is the inner function defined inside a decorator. It "wraps" around the target function—executing code before calling the target function, capturing its return value, running cleanup code after, and returning the result.

### 8. Why use *args in a Decorator?
*args allows the inner wrapper function to accept any number of positional arguments (e.g., func(1, 2, 3)). Without it, the decorator would fail if applied to a function taking positional parameters.

### 9. Why use **kwargs in a Decorator?
**kwargs allows the wrapper to accept any number of keyword arguments (e.g., func(user="admin", status="active")).

Combining *args and **kwargs inside wrapper(*args, **kwargs) makes your decorator universal—capable of wrapping any function regardless of its argument structure.

### 10. What is functools.wraps?
functools.wraps is a helper decorator provided by Python's standard library. It is placed directly above your inner wrapper function inside a custom decorator.

### 11. Why is functools.wraps important?
When you wrap a function, its original identity (name, docstring, annotations) is lost and replaced by the wrapper's details. @wraps(func) copies the original function's metadata back to the wrapper.

Without @wraps: my_function.__name__ outputs 'wrapper'.

With @wraps: my_function.__name__ outputs 'my_function'.

This prevents issues with debugging, automated documentation tools, and unit testing.

### 12. Can a function have multiple decorators?
Yes. You can stack as many decorators as needed above a single function:

Python
@decorator_one
@decorator_two
@decorator_three
def my_function():
    pass
### 13. In what order are multiple decorators applied?
Wrapping Order (Bottom-to-Top): Decorators wrap the function starting from the bottom-most decorator up to the top.

Execution Order (Top-to-Bottom): When called, execution enters the top-most decorator first, moving downward through each wrapper layer before reaching the target function.

Real-World Uses of Decorators
Authentication & Authorization: Restricting route access in web apps based on tokens or user roles.

Logging & Diagnostics: Auditing function calls, input parameters, and exceptions.

Caching / Memoization: Storing expensive calculation results in memory (e.g., @functools.lru_cache).

Rate Limiting: Restricting how frequently an API endpoint or function can be called.

Input Validation: Ensuring input arguments match target schemas or data types before function execution.

Web Development Example (Flask API Authentication)
Here is a practical real-world example using Flask (a Python web framework) where a custom decorator protects an administrative endpoint:

Python
from functools import wraps
from flask import Flask, request, jsonify

app = Flask(__name__)

def require_api_key(func):
    """Decorator to enforce API Key verification on HTTP routes."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        api_key = request.headers.get("X-API-KEY")
        
        # Verify if header exists and matches valid key
        if api_key != "secret-api-token-123":
            return jsonify({
                "error": "Unauthorized", 
                "message": "Invalid or missing X-API-KEY header"
            }), 401
            
        # Authentication successful -> Execute the web route
        return func(*args, **kwargs)
        
    return wrapper


# --- Route Usage ---

@app.route("/api/v1/user-data")
@require_api_key  # Protected route
def get_user_data():
    return jsonify({
        "status": "success",
        "data": ["User_A", "User_B", "User_C"]
    })