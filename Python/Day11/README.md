# 🚀 AI Engineer Bootcamp - Day 11

## 📅 Date
14-07-2026

## 📚 Topics Covered

## File Handling


✅ Create File
✅ Read File
✅ Append Data
✅ Read Line by Line
✅ with open()
✅ File Modes
✅ Bonus Project
✅ Mini Project
✅ 20 Practice Programs
---

## 💻 Programs

- file_write.py
- file_read.py
- hospital_records.py
- employee_database.py



---

## 🏥 Mini Project

Hospital Patient Record System


Features:

- Add Patient
- Save to File
- Read All Patients
- Search Patient
- Count Total Patients





---

## 🎯 Bonus Project

Employee Database

Features

- Add Employee
- Save Employee
- Display Employees
- Search Employee



---

## 20 Practice Programs
- Create File
- Write File
- Read File
- Append File
- Read Line by Line
- Count Lines
- Count Words
- Count Characters
- Copy File
- Rename File (using os)
- Delete File (using os)
- Check File Exists
- Student Record
- Employee Record
- Hospital Record
- Product Record
- Notes App
- Diary App
- Feedback Collector
- Contact Book

## 📖 Learning Resources

### Official Python Documentation

- Reading and Writing Files ✅
- Methods of File Objects ✅


---

### Videos

FreeCodeCamp

- (File Handling Section) ✅

Microsoft Python

- Episode 30 -- Demo: Functions ✅
- Episode 31 -- Parameterized functions ✅
- Episode 32 -- Demo: Parameterized Functions ✅

---

## 💡 What I Learned Today

 
- File Handling (Create File, Read File, Append Data, Read Line by Line, with open())
- Mini Project : Hospital Patient Record System
- Bonus Project : Employee Database

---

## 📂 GitHub

Day11 Completed Successfully ✅

## 🧠 Interview Preparation


### Q1. What is file handling?
File handling refers to the mechanism by which a software application interacts with files stored on a physical storage disk (like an SSD or HDD).When a program runs, its active variables and data live in RAM (Volatile Memory). File handling allows a program to step outside of RAM to create, open, read, modify, write, and close files on the local filesystem.
### 2. Why do we use files?
We use files primarily to solve the limitations of RAM:Data Persistence (Non-volatility): Data stored in a program's variables disappears the millisecond the program exits or the computer loses power. Files allow data to survive shutdowns.Storage Capacity: RAM is expensive and limited (typically 8GB–64GB on modern machines). Hard drives are cheap and massive (1TB–16TB+), making files ideal for storing large datasets, images, videos, and logs.Data Sharing & Portability: Files provide a standardized format (like .txt, .csv, .json) that allows different applications or entirely different computers to read and process the same data.
### 3. Difference between "r" and "w"?
Attribute'r' (Read Mode)'w' (Write Mode)Primary PurposeRetrieving and reading existing data.Writing and saving new data.Destructive?No. Safe to run; does not modify the file.Yes. It instantly truncates (wipes) the entire file to $0$ bytes upon opening.If file doesn't existRaises a FileNotFoundError.Creates a brand-new empty file.File Pointer PositionPlaced at the very beginning of the file.Placed at the very beginning of the file.
### 4. Difference between "w" and "a"?
Attribute'w' (Write Mode)'a' (Append Mode)Primary PurposeOverwriting or creating a file from scratch.Adding data to the end of an existing file.Handling of Old DataErases everything already in the file.Preserves everything; only adds new text to the bottom.File Pointer PositionPlaced at the beginning of the file.Placed at the end of the file.If file doesn't existCreates a brand-new empty file.Creates a brand-new empty file.
### 5. What is with open()?
with open() is Python’s implementation of a Context Manager. It is considered the modern industry standard for handling files.Pythonwith open("data.txt", "w") as file:
    file.write("Hello!")
 The file automatically closes here, even if an error occurred inside the block!
Its primary job is to automatically manage system resources. When the execution block indented under with finishes (or crashes due to an error), Python automatically closes the file behind the scenes, preventing resource leaks.
### 6. Why is close() important?
When you open a file, the operating system locks that file and reserves a "file descriptor" in system memory. If you do not explicitly close the file (either using file.close() or a with block):Resource Leakage: The OS keeps the file locked in RAM. Open enough files without closing them, and your system will run out of file descriptors, causing your application (or operating system) to crash.Data Loss / Buffered Out of Sync: Write operations do not always go directly to the disk instantly; they are buffered in temporary memory first. Calling .close() forces the computer to "flush" that buffer and physically write the data to the hard drive.File Locking: Other programs (like text editors or other backend processes) may be blocked from reading or deleting the file because your script still holds an active lock on it.
### 7. What happens if the file doesn't exist?
The outcome depends entirely on the mode you used to open it:If opened in Read Mode ('r'): The operating system cannot find the target file to extract data from, halting your program and throwing a FileNotFoundError.If opened in Write ('w') or Append ('a') Mode: Python gracefully catches the absence of the file and instructs the operating system to generate a brand-new, empty file with that name on the spot.
### 8. What is FileNotFoundError?
FileNotFoundError is a specific, built-in Python exception (specifically a subclass of OSError). It is raised when an operation attempts to access a file or folder path that does not exist on your computer's storage.To prevent your program from crashing when this happens, developers wrap file-reading operations in a try-except block:Pythontry:
    with open("secrets.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Oops! The file 'secrets.txt' does not exist in this directory.")
### 9. What are file modes?
File modes are setting parameters passed to the open() function that tell the operating system exactly what permissions and behaviors your program requires for that file session.They dictate:Operation Access: Are you reading (r), writing (w), or appending (a)?Data Representation: Are you processing text strings (default text mode, e.g., 'r') or raw bytes (binary mode, e.g., 'rb' or 'wb' for images, audio, and compressed files)?
### 10. Where is file handling used in real software?
File handling is a foundational pillar of software engineering. Real-world applications rely on it for:Application Configuration: Storing user settings, API keys, and theme preferences (typically in .json, .yaml, or .ini files).System Logging: Web servers (like Nginx) and databases append system activities, visitor IP addresses, and runtime errors continuously to log files (e.g., error.log) using append mode ('a').Exporting Reports: Applications (like Shopify or banking portals) generate and write transactions to a .csv or .pdf file for users to download.Game Saves: Video games write your character's level, position, and items to local save files so you can resume your progress later.