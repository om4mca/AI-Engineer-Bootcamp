# 🚀 AI Engineer Bootcamp - Day 06

## 📅 Date
08-07-2026

## 📚 Topics Covered

Python Lists:- 
- Create Lists
- Access Elements
- Modify List
- List Methods
   - append()
   - insert()
   - remove()
   - pop()
   - clear()
   - sort()
   - reverse()
- Loop Through List
   - Search
   - Length

---

## 💻 Programs

- list_basics.py


---

## 🏥 Mini Project

Hospital Patient Management System

Features

- Add Patient
- Display Patients
- Search Patient
- Remove Patient
- Total Patients

---

## 🎯 Bonus Project

Employee Management System

Features

- Add Employee
- Search Employee
- Remove Employee
- Display Employees
- Count Employees

---

## 20 Practice Programs
- Create List
- Print List
- Access First Element
- Access Last Element
- Add Item
- Remove Item
- Sort List
- Reverse List
- Find Maximum
- Find Minimum
- Count Elements
- Sum of Numbers
- Search Item
- Copy List
- Merge Two Lists
- Remove Duplicates
- Even Numbers from List
- Odd Numbers from List
- Student Marks List
- Hospital Patient List





## 📖 Learning Resources

### Official Documentation

- Lists  ✅
- More on Lists ✅
- List Methods ✅

---

### Videos

FreeCodeCamp

- Lists Section ✅

Microsoft Python

- Episode 15 -- Date Data Types ✅
- Episode 16 -- Demo: Dates ✅
- Episode 17 -- Error Handling ✅

---

## 💡 What I Learned Today

 Python Lists
- Create Lists
- Access Elements
- Modify List

---

## 📂 GitHub

Day06 Completed Successfully ✅

## 🧠 Interview Preparation


### Q1. What is a List?

A List in Python is a built-in data structure used to store a collection of items in a single variable. Lists are:
•	Ordered: They maintain the exact sequence in which you add items.
•	Mutable: You can add, change, or delete items after the list is created.
•	Flexible: They can hold any data type (strings, integers, booleans, or even other lists) and allow duplicate values.
•	Syntax: Written with square brackets: my_list = ["apple", 42, True]

### Q2. Difference between List and Tuple?

The core difference comes down to mutability (the ability to change):
Feature	List ([])	Tuple (())
Mutability	Mutable: Can be modified (add, remove, change items).	Immutable: Cannot be modified after creation.
Performance	Slightly slower; requires more memory allocation.	Faster; highly memory-efficient.
Use Case	Best for data that changes dynamically (e.g., shopping carts).	Best for fixed data that shouldn't change (e.g., GPS coordinates).

### Q3. Difference between append() and insert()?

Both add a single item to a list, but they place it differently:
•	append(item): Automatically adds the item to the very end of the list. You only pass it the item.
•	insert(index, item): Places the item at a specific position (index) you choose. It pushes all items after it one spot to the right.

### Q4. Difference between remove() and pop()?

Both delete an item from a list, but they target items differently:
•	remove(value): Deletes an item by its actual value/name. It searches the list and deletes the first matching item it finds.
•	pop(index): Deletes an item by its index position. If you leave the parentheses empty pop(), it automatically removes and returns the last item in the list.

### Q5. How do you sort a list?

You have two primary ways depending on whether you want a permanent or temporary sort:
•	Permanently (.sort()): Reorganizes the original list directly.
Python
nums = [3, 1, 2]
nums.sort()  # nums is now permanently [1, 2, 3]
•	Temporarily (sorted()): Leaves the original list alone and yields a new sorted copy.
Python
nums = [3, 1, 2]
new_nums = sorted(nums)  # new_nums is [1, 2, 3], nums stays [3, 1, 2]

### Q6. How do you reverse a list?

•	Permanently (.reverse()): Flips the current order of the original list in place. It does not sort alphabetically or numerically; it just mirrors the sequence.
Python
items = ["A", "C", "B"]
items.reverse()  # items is now ['B', 'C', 'A']
•	The Slicing Trick ([::-1]): Creates a reversed copy of the list instantly.
Python
reversed_copy = items[::-1]

### Q7. How do you search an item?

•	To check if it exists: Use the in keyword for a quick True/False check.
Python
if "Alice" in employees:
    print("Found!")
•	To find where it is: Use .index(value) to get its numerical position.
Python
position = employees.index("Alice") # Returns the index integer

### Q8. How do you loop through a list?

•	Standard loop (items only): Best when you just need to access the values.
Python
for name in employees:
    print(name)
•	Indexed loop (enumerate): Best when you need both the item and its index position.
Python
for index, name in enumerate(employees, start=1):
    print(f"{index}. {name}")

### Q9. What does len() do?

The len() function stands for length. It counts and returns the total number of elements currently inside your list.
Python
items = ["A", "B", "C"]
print(len(items))  # Output: 3
Note: If a list is empty, len() returns 0.

### Q10. Where are Lists used in real software?

Lists are the backbone of data storage in almost all modern applications:
•	E-Commerce Platforms (e.g., Amazon): Your digital shopping cart is a dynamic list of product items.
•	Social Media Feed (e.g., Instagram, X): The timeline posts you scroll through are delivered to your app as an ordered list of content dictionaries.
•	Streaming Services (e.g., Spotify): Playlists and data queues are structured as lists, allowing features like "play next" (append) or reordering tracks (insert/sort).
•	Gaming: An inventory system tracking the items your character is carrying is kept in an accessible list structure.
