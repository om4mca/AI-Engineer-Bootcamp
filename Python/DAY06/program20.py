# ------------------------------------------
# AI Engineer Bootcamp
# Day 6
# Program: Hospital Patient List
# Author: Om Roy
# Date: 08-07-2026
#--------------------------------------------


# Initialize an empty list to hold patient records (Dictionaries inside a List)
patient_database = []

print("---------Hospital Patient List ----------------")

while True:
    print("\n1. Admit New Patient")
    print("2. Display Patient Directory")
    print("3. Search Patient by Name")
    print("4. Discharge Patient (Remove)")
    print("5. View Hospital Summary Stats")
    print("6. Exit")
    
    choice = input("\nEnter menu selection (1-6): ").strip()
    
    # 1. Admit New Patient
    if choice == '1':
        name = input("Enter patient name: ").strip().title()
        if not name:
            print("Name cannot be blank.")
            continue
            
        try:
            age = int(input("Enter patient age: "))
            if age < 0 or age > 125:
                print("Please enter a realistic age.")
                continue
        except ValueError:
            print("Age must be a whole number.")
            continue
            
        condition = input("Enter medical condition/reason for visit: ").strip().capitalize()
        
        # Create a dictionary representing the patient and append to our database list
        new_patient = {
            "name": name,
            "age": age,
            "condition": condition
        }
        patient_database.append(new_patient)
        print(f"\n[Success] {name} has been admitted to the directory.")

    # 2. Display Patient Directory
    elif choice == '2':
        if not patient_database:
            print("The hospital currently has no active patients.")
        else:
            print(f"\n{'ID':<5} {'Patient Name':<20} {'Age':<6} {'Condition':<20}")
            print("-" * 55)
            for index, patient in enumerate(patient_database, start=1):
                # Using string formatting formatting to align into beautiful columns
                print(f"{index:<5} {patient['name']:<20} {patient['age']:<6} {patient['condition']:<20}")

    # 3. Search Patient by Name
    elif choice == '3':
        search_query = input("Enter patient name to search: ").strip().title()
        found_patients = []
        
        # Look through our database to see if any dictionary name matches the query
        for patient in patient_database:
            if search_query in patient["name"]:
                found_patients.append(patient)
                
        if found_patients:
            print(f"\nFound {len(found_patients)} match(es):")
            for patient in found_patients:
                print(f"• Name: {patient['name']} | Age: {patient['age']} | Condition: {patient['condition']}")
        else:
            print(f"No records found matching '{search_query}'.")

    # 4. Discharge Patient (Remove)
    elif choice == '4':
        if not patient_database:
            print("No patients available to discharge.")
            continue
            
        remove_name = input("Enter the EXACT name of the patient to discharge: ").strip().title()
        
        patient_to_remove = None
        for patient in patient_database:
            if patient["name"] == remove_name:
                patient_to_remove = patient
                break
                
        if patient_to_remove:
            patient_database.remove(patient_to_remove)
            print(f"\n[Discharged] {remove_name} has been successfully removed from active care.")
        else:
            print(f"Patient '{remove_name}' not found in current records.")

    # 5. View Hospital Summary Stats
    elif choice == '5':
        total_patients = len(patient_database)
        if total_patients == 0:
            print("Hospital is empty. No stats to generate.")
        else:
            # Extract ages into a separate list to perform math operations
            ages = [patient["age"] for patient in patient_database]
            avg_age = sum(ages) / total_patients
            
            print("\n=== Current Hospital Summary ===")
            print(f"Total Active Patients:   {total_patients}")
            print(f"Average Patient Age:     {avg_age:.1f} years old")
            print(f"Youngest Patient Age:    {min(ages)}")
            print(f"Oldest Patient Age:      {max(ages)}")

    # 6. Exit
    elif choice == '6':
        print("Shutting down management portal. System safe.")
        break
        
    else:
        print("Invalid choice! Please input a number from 1 to 6.")



#End of the program