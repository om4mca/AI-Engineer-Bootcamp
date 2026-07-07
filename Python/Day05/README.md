# 🚀 AI Engineer Bootcamp - Day 05

## 📅 Date
07-07-2026

## 📚 Topics Covered

- for Loop
- while Loop
- range()
- break
- continue
- pass
- Nested Loop

---

## 💻 Programs

- for_loop.py
- while_loop.py
- break_continue.py
- nested_loop.py

---

## 🏥 Mini Project

Hospital Token Generator

Features

- Auto Token Generation
- HOSP001 Format
- Zero Padding
- Dynamic Patient Count

---

## 🎯 Bonus Project

Hospital Appointment Scheduler

Features

- Appointment Generation
- Doctor Break after Every 10 Patients

---

## 📖 Learning Resources

### Official Documentation

- for Statement ✅
- while Statement ✅
- break ✅
- continue ✅
- pass ✅
- range() ✅

---

### Videos

FreeCodeCamp

- Loops Section ✅

Microsoft Python

- Episode 12 ✅
- Episode 13 ✅
- Episode 14 ✅

---

## 💡 What I Learned Today

- Difference between for and while loops.
- How range() works.
- How break and continue affect loop execution.
- How loops are used in real hospital software.

---

## 📂 GitHub

Day05 Completed Successfully ✅

## 🧠 Interview Preparation

### Q1. Difference between for and while?

Answer:•	
**for loop**: Used when you know in advance how many times you want to loop (e.g., printing 10 items, looping through a fixed list of names).
•	**while loop**: Used when you want to loop until a specific condition changes (e.g., repeating a game while the player still has lives left). You don't always know exactly how many loops it will take.


### Q2. What is range()?

Answer: 
**range()** is a built-in Python function that generates a sequence of numbers on the fly. It is most commonly used to control how many times a for loop runs.
•	Example: range(1, 5) generates 1, 2, 3, 4 (it always stops 1 number before the ending value).

### Q3. What does break do?
**break ** is the emergency exit button for loops. The moment Python hits a break statement, it terminates the loop completely and jumps straight to the code below the loop, ignoring any remaining cycles.
...

### 4. Difference between break and continue?
•	break stops the entire loop completely.
•	continue only skips the rest of the current turn, jumping immediately to the top of the loop to start the next cycle.
### 5. What is pass?
pass is a do-nothing placeholder. Python crashes if you leave an if statement or a loop empty. If you are designing code and want to leave a loop empty to write later, you put pass inside it so the code runs without syntax errors.
### 6. When should you use a while loop?
Use a while loop when the number of repetitions depends on user input or external conditions rather than a fixed count. Examples include:
•	Waiting for a user to type "exit".
•	Reading a stream of incoming data from the internet until it stops.
•	Running a game menu loop until the player hits "Quit".
### 7. What is a nested loop?
A nested loop is simply a loop inside another loop. For every single turn of the outer loop, the inner loop runs through its entire cycle from start to finish. They are perfect for working with grids, tables, or coordinates.
### 8. How do you avoid an infinite loop?
An infinite loop happens when a while loop's condition never becomes False. To avoid this, you must ensure that something inside the loop changes the condition variable on every turn.
•	Example: If your condition is while balance > 0:, you must subtract money from balance inside the loop so it eventually hits 0 and stops.
### 9. Write a loop to print even numbers.
Here is a simple for loop using the third parameter (the step) of range() to skip odd numbers:
Python
# Starts at 2, stops before 11, counts up by 2
for num in range(2, 11, 2):
    print(num)

# Output: 2, 4, 6, 8, 10
### 10. Where are loops used in real software?
Loops are the engine behind almost all software functions. Here are a few real-world examples:
•	Social Media: A for loop goes through a database of posts to render them onto your timeline screen.
•	Video Games: A continuous while loop (often called the Game Loop) checks for controller inputs, updates physics, and redraws the graphics on your screen 60+ times every second.
•	Music Apps: A loop steps through your playlist array one song at a time when "Repeat All" is toggled on.
•	Cybersecurity: A program loops through a dictionary list of thousands of common password variations to test a system's vulnerability.
