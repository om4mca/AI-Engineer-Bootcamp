# ------------------------------------------
# AI Engineer Bootcamp
# Day 5
# Program: Hospital Queue
# Author: Om Roy
# Date: 07-07-2026
#--------------------------------------------


# Initialize an empty list to act as our waiting room queue
hospital_queue = []

print("=== Hospital Queue Management System ===")

while True:
    print("\n--- MENU ---")
    print("1. Patient Check-In (Add to Queue)")
    print("2. Treat Next Patient (Remove from Queue)")
    print("3. View Waiting Room")
    print("4. Exit System")
    
    choice = input("Select an option (1-4): ")
    
    if choice == "1":
        # Add a patient to the end of the list
        patient_name = input("Enter patient name: ")
        hospital_queue.append(patient_name)
        print(f" '{patient_name}' added to the queue. Current waiting: {len(hospital_queue)}")
        
    elif choice == "2":
        # Treat the first patient in line
        if len(hospital_queue) > 0:
            # pop(0) removes and returns the item at index 0 (the front of the line)
            treated_patient = hospital_queue.pop(0)
            print(f" Doctor is now treating: '{treated_patient}'")
        else:
            print(" No patients waiting! The clinic is clear.")
            
    elif choice == "3":
        # Display the full queue
        if len(hospital_queue) > 0:
            print(f"\n Current Waiting Room Queue:")
            # Simple loop to show positions
            for index in range(len(hospital_queue)):
                print(f"  {index + 1}. {hospital_queue[index]}")
        else:
            print(" The waiting room is empty.")
            
    elif choice == "4":
        print("Closing the system. Have a good day!")
        break  # Stops the while loop and exits the program
        
    else:
        print(" Invalid choice! Please select an option between 1 and 4.")

#End of the program