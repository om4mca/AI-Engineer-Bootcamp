# ------------------------------------------
# AI Engineer Bootcamp
# Day 6
# Bonus Challenge: Employee Management System
# Author: Om Roy
# Date: 08-07-2026
#--------------------------------------------



# Initialize an empty list to store employee names
employees = []

print("--- Employee Management System ---")

while True:
    # Display the menu options
    print("\n1. Add Employee")
    print("2. Search Employee")
    print("3. Remove Employee")
    print("4. Display Employees")
    print("5. Count Employees")
    print("6. Exit")
    
    # Take user input for choice
    choice = input("\nEnter your choice (1-6): ")
    
    # 1. Add Employee
    if choice == '1':
        name = input("Enter employee name to add: ").strip()
        if name:
            employees.append(name)
            print(f"Employee '{name}' added successfully!")
        else:
            print("Employee name cannot be empty.")
            
    # 2. Search Employee
    elif choice == '2':
        search_name = input("Enter employee name to search: ").strip()
        if search_name in employees:
            print(f"Employee '{search_name}' found in the system.")
        else:
            print(f"Employee '{search_name}' not found.")
            
    # 3. Remove Employee
    elif choice == '3':
        remove_name = input("Enter employee name to remove: ").strip()
        if remove_name in employees:
            employees.remove(remove_name)
            print(f"Employee '{remove_name}' removed successfully.")
        else:
            print(f"Employee '{remove_name}' not found in the records.")
            
    # 4. Display Employees
    elif choice == '4':
        if len(employees) == 0:
            print("No employees in the system.")
        else:
            print("\n--- Current Employee List ---")
            # Loop through the list to print names with their index number
            for index, name in enumerate(employees, start=1):
                print(f"{index}. {name}")
                
    # 5. Count Employees
    elif choice == '5':
        total = len(employees)
        print(f"Total number of active employees: {total}")
        
    # 6. Exit
    elif choice == '6':
        print("Exiting system. Goodbye!")
        break
        
    # Handle invalid inputs
    else:
        print("Invalid choice! Please enter a number between 1 and 6.")