#--------------------------------------------
# AI Engineer Bootcamp
# Day 10
# Program: File Reader
# Author: Om Roy
# Date: 13-07-2026
#--------------------------------------------


import os

def safe_list_file_reader():
    print("=== Buffered List File Reader ===")
    print(f"Current Directory: {os.getcwd()}")
    print("Type 'exit' to close the program.\n")

    while True:
        file_path = input("Enter the filename or path to load: ").strip()
        
        if file_path.lower() == 'exit':
            print("\nClosing application context. Goodbye!")
            break

        try:
            # Open, read into list, and close immediately using context manager
            with open(file_path, 'r', encoding='utf-8') as file:
                # readlines() stores every line as an individual string element in a Python list
                file_lines = file.readlines()
                
        except FileNotFoundError:
            print(f"\n[IO Error]: File '{file_path}' could not be located.\n")
            
        except PermissionError:
            print(f"\n[OS Security Error]: Access denied to read '{file_path}'.\n")
            
        except Exception as e:
            print(f"\n[Runtime Error]: Unable to load file. Details: {e}\n")
            
        else:
            # If the try block passes, the file stream is already closed here!
            # We can now manipulate our isolated list safely in memory.
            total_lines = len(file_lines)
            print(f"\n[Success]: Loaded {total_lines} lines into memory buffer.")
            
            if total_lines == 0:
                print("⚠️ This file is empty.")
            else:
                # Let's inspect a clean summary preview
                print(f"--- Data Summary View [{file_path}] ---")
                print(f"First Line : {file_lines[0].strip()}")
                print(f"Last Line  : {file_lines[-1].strip()}")
                print("-" * 40 + "\n")
                
        finally:
            print("-" * 55)


if __name__ == "__main__":
    safe_list_file_reader()