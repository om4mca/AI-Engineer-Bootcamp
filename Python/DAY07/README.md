# 🚀 AI Engineer Bootcamp - Day 07

## 📅 Date
09-07-2026

## 📚 Topics Covered

## Tuples

   - Immutable Data
   - Tuple Methods
   - Packing & Unpacking
## Sets 
 - Unique Values
 - Union
 - Intersection
 - Difference

 ## Dictionaries
 - Key-Value Pairs
 - Access Values
 - Update Data
 - Loop Through Dictionary
---

## 💻 Programs

- Create tuple_basics.py


---

## 🏥 Mini Project

Hospital Doctor Directory

Features

- Add Doctor
- Display Doctors
- Search by ID
- Update Department
- Remove Doctor
- Total Doctors

---

## 🎯 Bonus Project

Employee Attendance System

Features

- Add Employee
- Mark Present
- Mark Absent
- Display Attendance
- Count Present Employees

---

## 20 Practice Programs
- Create Tuple
- Access Tuple Elements
- Tuple Unpacking
- Create Set
- Remove Duplicates
- Set Union
- Set Intersection
- Set Difference
- Create Dictionary
- Access Dictionary Value
- Add Dictionary Item
- Update Dictionary Item
- Remove Dictionary Item
- Loop Through Dictionary
- Count Dictionary Items
- Student Dictionary
- Hospital Doctor Dictionary
- Employee Salary Dictionary
- Phone Book
- Inventory Dictionary


## 📖 Learning Resources

### Official Documentation

- Tuples ✅
- Sets ✅
- Dictionaries ✅
- Dictionary Methods ✅

---

### Videos

FreeCodeCamp

- (Tuples, Sets, Dictionaries) ✅

Microsoft Python

- Episode 18 -- Demo: Error Handling ✅
- Episode 19 -- Conditional Logic ✅
- Episode 20 -- Demo: Conditional Logic ✅

---

## 💡 What I Learned Today

 
- Tuples
- Sets
- Dictionaries

---

## 📂 GitHub

Day07 Completed Successfully ✅

## 🧠 Interview Preparation


### Q1. What is a Tuple?
A tuple is an ordered, unchangeable (immutable) collection of items in Python. Once you create a tuple, you cannot add new elements, modify existing ones, or remove them. It is defined using parentheses ().

Python
dimensions = (1920, 1080)  # A static screen resolution
### 2. Difference between List and Tuple?
The core difference is mutability (the ability to change):

Lists [ ] are mutable: You can freely add, remove, or edit items. They are slightly slower and use more memory.

Tuples ( ) are immutable: They are locked. Because they are static, Python processes them faster, and they use less memory.

### 3. What is a Set?
A set is an unordered collection of unique items defined by curly braces {}. Sets do not allow duplicate values. Because they are unordered, items do not have an index (you cannot look up my_set[0]).

Python
categories = {"Admin", "Manager", "Guest"}
### 4. How are duplicates removed?
The easiest way to remove duplicates from a list is to convert it into a set using set(), then turn it back into a list. Because sets cannot hold duplicates, Python instantly discards any repeating items.

Python
raw_list = [1, 2, 2, 3, 3, 3]
clean_list = list(set(raw_list))  # Result: [1, 2, 3]
### 5. Difference between add() and append()?
append() is a List method. It places an item at the very end of an ordered list and allows duplicates.

add() is a Set method. It inserts an item into a set. If that item is already present in the set, add() does nothing.

### 6. What is a Dictionary?
A dictionary is an ordered (as of Python 3.7+) collection of key-value pairs defined by curly braces {} with colons separating pairs. It works exactly like a real-world phonebook or database table, allowing you to instantly look up a specific item.

### 7. What are keys and values?
Keys: The unique identifiers you use to look things up (like a Roll Number, Username, or SKU code). Keys must be unique and unchangeable data types (strings, numbers, tuples).

Values: The actual data associated with that key (like a student's name, age, or list of grades). Values can be anything and can duplicate freely.

Python
#  Key      : Value
{"EMP001"   : "Alice Vance"}
### 8. How do you update a dictionary?
You can update a dictionary by using square brackets [] to target a specific key, or by using the .update() method to modify multiple entries at once. If the key doesn't exist yet, Python will create it.

Python
user = {"name": "Bob", "role": "User"}

# Method A: Direct assignment
user["role"] = "Admin"

# Method B: Using .update()
user.update({"status": "Active", "login_attempts": 0})
### 9. How do you loop through a dictionary?
You can use a for loop combined with the .items() method to pull out both the keys and values simultaneously:

Python
inventory = {"Apples": 50, "Bananas": 30}

for item, quantity in inventory.items():
    print(f"Stock: {item} -> {quantity}")
(You can also use .keys() to loop through just the keys, or .values() to loop through just the values).

### 10. Where are dictionaries used in real software?
Dictionaries are everywhere in professional software because they match the way data moves across the internet. Real-world use cases include:

User Session Management: Tracking logged-in users at runtime (e.g., {"user_id_123": {"token": "xyz", "ip": "1.1.1.1"}}).

API Data (JSON): Web services send data back and forth in JSON format, which maps perfectly to a Python dictionary.

Application Settings: Storing configuration profiles (e.g., {"theme": "dark", "notifications": True}).