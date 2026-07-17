# 🚀 AI Engineer Bootcamp - Day 13

## 📅 Date
17-07-2026

## 📚 Topics Covered

## File Handling


✅ Inheritance
✅ Types of Inheritance
✅ Method Overriding
✅ super() / isinstance()
✅ Hospital Management System
✅ Banking System
✅ 20 Practice Programs
✅ Documentation
✅ Videos
✅ Notebook
✅ Interview Questions

---

## 💻 Programs

- inheritance.py
- hospital_management.py
- banking_system.py




---

## 🏥 Mini Project

Hospital Management System (Inheritance)


Features:

- display_details()
- update_details()


---

## 🎯 Bonus Project

Banking System (OOP)

Features

- Deposit
- Withdraw
- Check Balance



---

## 20 Practice Programs
- Simple Inheritance
- Multiple Child Classes
- super()
- Method Overriding
- Person → Student
- Person → Employee
- Animal → Dog
- Animal → Cat
- Vehicle → Car
- Vehicle → Bike
- Bank → Savings
- Bank → Current
- Hospital → Patient
- Hospital → Doctor
- Product → Mobile
- Product → Laptop
- Polymorphism Demo
- Encapsulation Demo
- isinstance()
- Mini OOP Challenge

## 📖 Learning Resources

### Official Python Documentation



- Inheritance ✅
- Multiple Inheritance (Overview) ✅
- Private Variables ✅


---

### Videos

FreeCodeCamp

- (Inheritance/Advanced OOP) ✅

Microsoft Python

- Episode 36 --Introduction to Classes ✅
- Episode 37 -- Objects and Methods ✅
- Episode 38 -- Demo: Classes and Objects ✅

---


## 💡 What I Learned Today

 
- Inheritance,  Types of Inheritance,  Method Overriding,  super() / isinstance()
- Mini Project : Hospital Management System (Inheritance)
- Bonus Project : Banking System (OOP)


---

## 📂 GitHub

Day13 Completed Successfully ✅

## 🧠 Interview Preparation


### Q1. What is Inheritance?
Inheritance is an OOP mechanism where a new class (Child Class) automatically acquires the attributes and methods of an existing class (Parent Class). It establishes an "is-a" relationship (e.g., a SavingsAccount is an Account).

### 2. Why do we use Inheritance?
Code Reusability: You write and debug common logic once in the parent class, and all child classes instantly reuse it.

Maintainability: If a core feature needs to change, you update it in one central parent location instead of editing dozens of separate files.

Extensibility: You can easily add new variations of a class without modifying or risking bugs in your existing, working code.

### 3. What is Method Overriding?
Method Overriding occurs when a child class provides a specific, custom implementation for a method that is already defined in its parent class. The child's version replaces or enhances the parent's version when called by a child object.

Example: A parent Account class has a standard withdraw() method, but CurrentAccount overrides it to allow for an overdraft feature.

### 4. What is super()?
super() is a built-in Python function used to access and call methods from a parent class inside a child class.

It is most commonly used inside the child's __init__ constructor to pass shared arguments (like name, age) up to the parent's constructor so you don't have to initialize them manually again.

### 5. What is Encapsulation?
Encapsulation is the practice of bundling data (attributes) and methods into a single unit (a class) while hiding the internal mechanics and restricting direct access from the outside.

It protects an object's internal state from accidental or invalid changes by forcing external code to use "safety gate" methods (getters/setters) to interact with the data.

### 6. What is Polymorphism?
Polymorphism (meaning "many forms") is the ability of different objects to respond to the exact same method call in their own distinct ways.

If you have a list containing a Mobile object and a Laptop object, you can run a loop and call .display_details() on both. You do not need to know which is which; each object automatically executes its own custom version of the method.

### 7. Difference between Overloading and Overriding?
Method Overriding (Runtime Polymorphism): A child class replaces a method inherited from a parent class. The method names and parameters are identical, but the execution logic changes.

Method Overloading (Compile-time Polymorphism): Multiple methods in the same class share the same name but have a different number or type of parameters. (Note: Python does not natively support traditional method overloading by default like Java or C++; instead, Python achieves this behavior using default arguments like arg=None).

### 8. What is isinstance()?
isinstance(object, class) is a built-in Python function used to check if an object belongs to a specific class, or to any class derived from it (subclasses). It returns True or False.

Example: isinstance(my_laptop, Product) returns True if my_laptop is an instance of the Laptop class, which inherits from Product.

### 9. Public vs Private variables?
Public Variables: Accessible from anywhere inside or outside the class. In Python, variables are public by default (e.g., self.name = "Alice").

Private Variables: Accessible only within the class they are defined. In Python, you declare a private variable by prefixing it with double underscores (e.g., self.__balance = 500). Python restricts direct outside access to this variable using a mechanism called name mangling.

### 10. Where is Inheritance used in real software?
Web Frameworks (like Django or Flask): When creating database models or web views, you inherit from the framework's core classes (e.g., class User(models.Model)), instantly gaining access to database saving and querying capabilities.

GUI / Game Engines: A UI button or an enemy monster inherits from a base Widget or Entity class to inherit spatial coordinates, rendering hooks, and click/collision detection properties.

Automated Testing (Unittest): When writing unit tests in Python, your test classes inherit from unittest.TestCase to automatically gain testing tools like assertEqual().