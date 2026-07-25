# 🚀 AI Engineer Bootcamp - Day 20

## 📅 Date
25-07-2026

## 📚 Topics Covered

## Topics Covered

## Context Managers

## with Statement

## __enter__()

## __exit__()

## Resource Management

## Exception Handling

## Custom Context Managers

## contextlib

## @contextmanager

## ContextDecorator

## Mini Project

## Bonus Project

## Practice Programs

## Key Learnings

## Interview Questions

## How to Run

## Official Python Documentation


- Context Managers ✅
- with Statement ✅
- __enter__() ✅
- __exit__() ✅
- contextlib ✅
- @contextmanager ✅
- ContextDecorator ✅


---

## 💻 Programs

- context_manager_basics.py
- with_statement.py
- enter_exit.py
- custom_context_manager.py
- exception_context_manager.py

- contextlib_example.py
- contextmanager_decorator.py
- timer_context_manager.py

- hospital_context_manager.py
- employee_file_manager.py

- program01.py
- program02.py
...
- program15.py

- README.md


---

## 🏥 Mini Project

Hospital Database Connection Context Manager


## 🎯 Bonus Project

Employee File Manager



---

## 15 Practice Programs
- Basic with Statement
- File Context Manager
- Custom Context Manager
- __enter__()
- __exit__()
- Context Manager with Exception
- Exception Suppression
- contextlib.contextmanager
- yield in Context Manager
- Context Manager with Resource
- Database Connection Simulator
- Hospital Database Context Manager
- Employee File Context Manager
- Logging Context Manager
- Timer Context Manager

## 📖 Learning Resources


### Videos

FreeCodeCamp

- (Context Managers / with Statement / Advanced Python) ✅


---


## 💡 What I Learned Today

✅ Context Manager क्या है?
✅ with Statement
✅ Resource Management
✅ __enter__()
✅ __exit__()
✅ File Handling with with
✅ Exception Handling with Context Managers
✅ Custom Context Manager Class
✅ contextlib
✅ @contextmanager
✅ Custom Context Manager Project
✅ Mini Project
✅ Bonus Project


---

## 📂 GitHub

Day20 Completed Successfully ✅

## 🧠 Interview Preparation


### 1. 1. What is a Context Manager?

A Context Manager is a Python object designed to manage resources by defining exact setup and teardown steps. It sets up temporary conditions (e.g., allocating memory, acquiring a lock, opening a file) before code executes and guarantees those conditions are cleaned up afterward.

### 2. What is the purpose of the with statement?

The with statement is the syntactic wrapper that runs a context manager. It ensures that resource cleanup happens automatically when execution leaves its block—even if the code inside raises an error, hits a return, or encounters break/continue.

### 3. Why should we use Context Managers?

Prevents Resource Leaks: Ensures files, network sockets, database pools, and locks are released immediately when no longer needed.Cleaner Code: Eliminates repetitive try...finally boilerplate.Error Safety: Guarantees that teardown code runs even when unexpected exceptions crash the main block.Encapsulated Logic: Keeps setup and teardown logic isolated inside reusable objects or functions.
### 4. What are __enter__() and __exit__()?

They are the two special dunder methods that form Python’s Context Manager Protocol:__enter__(): Runs before entering the with block. It sets up the resource and optionally returns an object (which gets bound to the variable after as).__exit__(): Runs after leaving the with block. It handles teardown, closes connections, and manages any exceptions that occurred inside the block.

### 5. What parameters does __exit__() receive?

__exit__() receives four arguments: self plus three exception-tracking parameters:Pythondef __exit__(self, exc_type, exc_val, exc_tb):
    ...
exc_type: The exception class (e.g., ValueError). None if no error occurred.exc_val: The actual exception instance/message. None if no error occurred.exc_tb: The traceback object containing call-stack information. None if no error occurred.

### 6. What happens if an exception occurs inside a with block?

Python immediately halts execution inside the with block.It passes the exception's type, value, and traceback into __exit__(exc_type, exc_val, exc_tb).__exit__() performs its cleanup logic.Depending on what __exit__() returns, the exception is either re-raised to crash/be caught outside or suppressed completely.

### 7. What does __exit__() return?

False (or None): Tells Python to re-raise the exception so calling code is aware of the failure (default behavior).True: Tells Python to suppress (swallow) the exception, allowing the script to continue running right after the with block as if no error occurred.

### 8. How can you create a custom Context Manager?

You can create one in two main ways:Way A: Class-Based (Explicit Dunder Methods)Pythonclass SimpleManager:
    def __enter__(self):
        print("Setup")
        return "Resource Handle"
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Cleanup")
        return False
Way B: Generator-Based (@contextmanager)Pythonfrom contextlib import contextmanager

@contextmanager
def simple_manager():
    print("Setup")
    try:
        yield "Resource Handle"
    finally:
        print("Cleanup")

### 9. What is contextlib?

contextlib is a built-in Python module that provides utilities for working with context managers. It includes tools like:@contextmanager: Converts a generator function into a context manager.suppress(): Temporarily ignores specified exceptions.ExitStack: Flexibly handles a dynamic number of context managers at once.ContextDecorator: Lets context managers also act as function decorators.

### 10. What is @contextmanager?

@contextmanager is a decorator from contextlib that lets you define a context manager using a single function containing a yield statement, eliminating the need to write a custom class with __enter__ and __exit__.

### 11. What is the role of yield in @contextmanager?

In a generator decorated with @contextmanager, yield acts as an execution bridge:Code before yield acts as __enter__().The value passed to yield is bound to the target variable after as.yield pauses execution and transfers control to the with block.Once the with block finishes, execution resumes immediately after yield (acting as __exit__()).

### 12. Difference between Context Manager and Decorator?

FeatureContext ManagerDecoratorPrimary ScopeWraps a specific block of code inside a function.Wraps an entire function definition.SyntaxUsed with the with statement.Used with @decorator_name above functions.State SharingEasy to pass variables in/out of the block via as.Applies to every call of the decorated function.Primary GoalManaging fine-grained resource scope/lifespan.Modifying or extending function behavior globally.

### 13. What is ContextDecorator?

ContextDecorator is a base class from contextlib that enables a context manager to be used as both a with statement and a function decorator.Pythonfrom contextlib import ContextDecorator

class TrackTask(ContextDecorator):
    def __enter__(self):
        print("Starting execution...")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Finished execution.")
        return False

# Use as Context Manager
with TrackTask():
    print("Inside block")

# Use as Decorator
@TrackTask()
def my_func():
    print("Inside function")

### 14. Give real-world examples of Context Managers.

Files: open('file.txt', 'r') automatically closes files.Threading/Async: threading.Lock() acquires and releases locks safely to avoid deadlocks.Directory Management: os.chdir() context managers temporarily switch working directories and restore the original path afterwards.Testing: unittest.mock.patch() temporarily mocks functions/objects during test suites.Database Transactions: Committing changes on success or rolling back on error.15. Why are Context Managers useful for database connections?Atomicity (Rollback on Failure): If an error occurs halfway through multi-step SQL queries (e.g., deducting funds from Account A but failing before crediting Account B), __exit__() automatically triggers rollback() to keep data consistent.Auto-Commit on Success: If all statements execute smoothly, __exit__() triggers commit() automatically.Connection Pool Management: Connections drawn from limited pools are guaranteed to be released back to the pool in finally/__exit__(), preventing pool exhaustion errors.