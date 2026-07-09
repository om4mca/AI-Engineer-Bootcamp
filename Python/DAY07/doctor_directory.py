# ------------------------------------------
# AI Engineer Bootcamp
# Day 7
# Program: Hospital Doctor Directory
# Author: Om Roy
# Date: 09-07-2026
#--------------------------------------------


# Initial sample data
doctors = {
    "CARD101": {"name": "Dr. Sharma", "dept": "Cardiology"},
    "ORTH102": {"name": "Dr. Singh", "dept": "Orthopedics"},
    "NEUR103": {"name": "Dr. Das", "dept": "Neurology"}
}

def add_doctor():
    doc_id = input("Enter Doctor ID (e.g., CARD101): ").strip().upper()
    if doc_id in doctors:
        print("Error: A doctor with this ID already exists.")
        return
    
    name = input("Enter Doctor Name: ").strip()
    dept = input("Enter Department: ").strip()
    
    doctors[doc_id] = {"name": name, "dept": dept}
    print(f"Successfully added {name} to the directory.")

def display_doctors():
    if not doctors:
        print("The directory is currently empty.")
        return
    
    print("\n--- Doctor Directory ---")
    print(f"{'ID':<10} | {'Name':<20} | {'Department':<20}")
    print("-" * 56)
    for doc_id, info in doctors.items():
        print(f"{doc_id:<10} | {info['name']:<20} | {info['dept']:<20}")
    print("-" * 56)

def search_doctor():
    doc_id = input("Enter Doctor ID to search: ").strip().upper()
    if doc_id in doctors:
        info = doctors[doc_id]
        print(f"\nFound Doctor:\nID: {doc_id}\nName: {info['name']}\nDepartment: {info['dept']}")
    else:
        print("Doctor not found.")

def update_department():
    doc_id = input("Enter Doctor ID to update department: ").strip().upper()
    if doc_id in doctors:
        new_dept = input("Enter new department: ").strip()
        doctors[doc_id]['dept'] = new_dept
        print(f"Department updated successfully for {doctors[doc_id]['name']}.")
    else:
        print("Doctor not found.")

def remove_doctor():
    doc_id = input("Enter Doctor ID to remove: ").strip().upper()
    if doc_id in doctors:
        removed_doc = doctors.pop(doc_id)
        print(f"Removed {removed_doc['name']} from the directory.")
    else:
        print("Doctor not found.")

def show_total():
    print(f"\nTotal Doctors in Directory: {len(doctors)}")

def main():
    while True:
        print("\n=== DOCTOR DIRECTORY MENU ===")
        print("1. Add Doctor")
        print("2. Display Doctors")
        print("3. Search by ID")
        print("4. Update Department")
        print("5. Remove Doctor")
        print("6. Total Doctors Count")
        print("7. Exit")
        
        choice = input("Choose an option (1-7): ").strip()
        
        if choice == '1':
            add_doctor()
        elif choice == '2':
            display_doctors()
        elif choice == '3':
            search_doctor()
        elif choice == '4':
            update_department()
        elif choice == '5':
            remove_doctor()
        elif choice == '6':
            show_total()
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()


# end of the program