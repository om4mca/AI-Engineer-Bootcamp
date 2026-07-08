# ------------------------------------------
# AI Engineer Bootcamp
# Day 6
# Mini Project: Hospital Patient Management System
# Author: Om Roy
# Date: 08-07-2026
#--------------------------------------------


# Initialize an empty list to store patient names
patients = []

print("--- Hospital Patient Management System ---")

while True:
    # Display the menu options
    print("\n1. Add Patient")
    print("2. Display Patients")
    print("3. Search Patient")
    print("4. Remove Patient")
    print("5. Total Patients")
    print("6. Exit")
    
    # Take user input for choice
    choice = input("\nEnter your choice (1-6): ")
    
    # 1. Add Patient
    if choice == '1':
        name = input("Enter patient name to add: ").strip()
        if name:
            patients.append(name)
            print(f"Patient '{name}' added successfully!")
        else:
            print("Patient name cannot be empty.")
            
    # 2. Display Patients
    elif choice == '2':
        if len(patients) == 0:
            print("No patients in the system.")
        else:
            print("\n--- Current Patient List ---")
            # Loop through the list to print names with their index number
            for index, name in enumerate(patients, start=1):
                print(f"{index}. {name}")
                
    # 3. Search Patient
    elif choice == '3':
        search_name = input("Enter patient name to search: ").strip()
        if search_name in patients:
            print(f"Patient '{search_name}' found in the system.")
        else:
            print(f"Patient '{search_name}' not found.")
            
    # 4. Remove Patient
    elif choice == '4':
        remove_name = input("Enter patient name to remove: ").strip()
        if remove_name in patients:
            patients.remove(remove_name)
            print(f"Patient '{remove_name}' removed successfully.")
        else:
            print(f"Patient '{remove_name}' not found in the records.")
            
    # 5. Total Patients
    elif choice == '5':
        total = len(patients)
        print(f"Total number of active patients: {total}")
        
    # 6. Exit
    elif choice == '6':
        print("Exiting system. Goodbye!")
        break
        
    # Handle invalid inputs
    else:
        print("Invalid choice! Please enter a number between 1 and 6.")


        #End of the program