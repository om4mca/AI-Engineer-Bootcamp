#--------------------------------------------
# AI Engineer Bootcamp
# Day 21
# Program: OOP + File Handling
# Author: Om Roy
# Date: 27-07-2026
#--------------------------------------------

class TextFileManager:
    def __init__(self, filepath):
        self.filepath = filepath

    def write_content(self, text):
        with open(self.filepath, "w") as file:
            file.write(text)

    def read_content(self):
        try:
            with open(self.filepath, "r") as file:
                return file.read()
        except FileNotFoundError:
            return "File does not exist."

# Usage
manager = TextFileManager("notes.txt")
manager.write_content("Meeting at 3 PM")
print(manager.read_content())  