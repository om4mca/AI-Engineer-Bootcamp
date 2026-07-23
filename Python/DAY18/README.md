# 🚀 AI Engineer Bootcamp - Day 13

## 📅 Date
23-07-2026

## 📚 Topics Covered

## Generator Functions

## yield

## return vs yield

## Generator Objects

## Generator Expressions

## Lazy Evaluation

## Memory Efficiency

## Iterator vs Generator

## Mini Project

## Bonus Project

## Practice Programs

## Key Learnings

## Interview Questions

## How to Run


## Official Python Documentation

- Generator Functions yield ✅
- Generator Expressions ✅
- yield Expressions ✅
- Iterator Protocol ✅


---

## 💻 Programs

- generator_basics.py
- generator_expressions.py
- yield_examples.py
- even_generator.py
- square_generator.py
- fibonacci_generator.py
- hospital_patient_generator.py
- employee_generator.py

- program01.py
- program02.py
...
- program15.py




---

## 🏥 Mini Project

Hospital Patient Record Generator


## 🎯 Bonus Project

Employee Data Generator



---

## 15 Practice Programs
- Basic Generator
- Number Generator
- Even Number Generator
- Odd Number Generator
- Square Generator
- Cube Generator
- Multiplication Table Generator
- Fibonacci Generator
- Countdown Generator
- Range Generator
- String Character Generator
- Hospital Patient Generator
- Senior Patient Generator
- Employee Generator
- Employee Salary Generator

## 📖 Learning Resources


### Videos

FreeCodeCamp

- (Generators / Iterators) ✅


---


## 💡 What I Learned Today

 
✅ Generator क्या है?
✅ Generator Function
✅ yield
✅ yield vs return
✅ Generator Object
✅ next() with Generator
✅ Generator और Iterator का relationship
✅ Generator Expression
✅ Memory Efficiency
✅ for loop with Generator
✅ Custom Generators
✅ Practical Mini Project
✅ Bonus Project


---

## 📂 GitHub

Day18 Completed Successfully ✅

## 🧠 Interview Preparation


### 1. What is a Generator?
A Generator is a special type of iterator in Python that produces a stream of values one at a time (on-demand) rather than calculating them all upfront and storing them in memory.

### 2. What is a Generator Function?
A Generator Function is a function defined with the standard def keyword, but it uses yield instead of (or in addition to) return. When called, it returns a generator object without executing its body immediately.

### 3. What is yield?
yield is a keyword used to pause a generator function and return a value to the caller. Unlike return, yield saves the local execution state (variables, code position) so the function can resume right where it left off on the next call.

### 4. Difference between yield and return
Feature	yield	return
State	Pauses execution and retains local variables.	Terminates execution and discards local variables.
Output	Can produce a sequence of multiple values over time.	Returns a single final result.
Resumption	Resumes execution after the paused line on next call.	Calling the function again restarts it from the beginning.
### 5. What is a Generator Object?
A Generator Object is the iterator instance returned when you call a generator function. You retrieve items from it using the next() function or inside a for loop.

### 6. What is a Generator Expression?
A Generator Expression is a compact, single-line way to construct a generator object. It shares syntax with list comprehensions, but uses parentheses () instead of square brackets []:

Python
# List Comprehension (evaluates into memory immediately)
nums_list = [x * 2 for x in range(5)]

# Generator Expression (evaluates lazily)
nums_gen = (x * 2 for x in range(5))
### 7. What is Lazy Evaluation?
Lazy Evaluation means that values are computed on-demand only when explicitly requested (e.g., when next() is called), rather than pre-computing all results upfront.

### 8. Why are Generators memory efficient?
Generators do not store the entire dataset in RAM. Instead, they store only their current execution state and the logic needed to derive the next value, maintaining a constant memory footprint (O(1)) regardless of sequence size.

### 9. Difference between List and Generator
Feature	List	Generator
Memory	Stores all elements in memory simultaneously (O(N)).	Stores only 1 item in memory at a time (O(1)).
Access	Supports indexing and slicing (list[0]).	Sequential access only (no indexing).
Reusability	Can be iterated over multiple times.	Can be consumed only once.
### 10. Difference between Iterator and Generator
Key Rule: Every generator is an iterator, but not every iterator is a generator.

Iterator: Built manually by creating a custom Class containing __iter__() and __next__() methods.

Generator: Built simply by using a function with yield or a () expression without custom class setup.

### 11. Can a Generator be iterated only once?
Yes. Once a generator has yielded all its values, it becomes exhausted. To iterate over the sequence again, you must instantiate a brand-new generator object.

### 12. What happens when a Generator finishes?
When a generator completes execution or encounters a return statement, it stops yielding values and terminates iteration.

### 13. What exception indicates the end of iteration?
The StopIteration exception. Python's for loops automatically catch and handle this exception behind the scenes to end the loop cleanly.

### 14. Give a real-world use case of Generators.
Processing Large Log/CSV Files: Reading a multi-gigabyte log file line-by-line (for line in open("large_file.log"):) uses a generator under the hood. This allows you to inspect huge files without crashing system memory.

### 15. Why are Generators useful for large datasets?
Prevents Memory Overflows: Eliminates MemoryError issues because raw data isn't loaded all at once.

Immediate Processing: You don't have to wait for an entire multi-GB dataset to load into memory before you start processing the first item.