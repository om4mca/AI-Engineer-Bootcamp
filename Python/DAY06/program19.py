# ------------------------------------------
# AI Engineer Bootcamp
# Day 6
# Program: Student Marks List
# Author: Om Roy
# Date: 08-07-2026
#--------------------------------------------


# Initialize an empty list to hold numerical scores
marks = []

print("--- Student Marks Details ---")

while True:
    # Display the menu options
    print("\n1. Add Mark")
    print("2. Display All Marks")
    print("3. View Statistics (Highest, Lowest, Average)")
    print("4. Clear All Marks")
    print("5. Exit")
    
    choice = input("\nEnter your choice (1-5): ").strip()
    
    # 1. Add Mark
    if choice == '1':
        try:
            score = float(input("Enter student mark (0-100): "))
            # Validate that the mark is within a normal grading range
            if 0 <= score <= 100:
                marks.append(score)
                print(f"Mark {score} added successfully!")
            else:
                print("Invalid input! Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid numerical value.")
            
    # 2. Display All Marks
    elif choice == '2':
        if not marks:
            print("The marks list is currently empty.")
        else:
            print("\n--- Recorded Marks ---")
            for index, score in enumerate(marks, start=1):
                print(f"Student #{index}: {score}")
                
    # 3. View Statistics
    elif choice == '3':
        if not marks:
            print("No marks available to calculate statistics.")
        else:
            total_students = len(marks)
            highest = max(marks)
            lowest = min(marks)
            average = sum(marks) / total_students
            
            print("\n--- Grade Statistics ---")
            print(f"Total Papers Graded: {total_students}")
            print(f"Highest Mark:        {highest}")
            print(f"Lowest Mark:         {lowest}")
            print(f"Class Average:       {average:.2f}")
            
    # 4. Clear All Marks
    elif choice == '4':
        confirm = input("Are you sure you want to clear all data? (yes/no): ").lower().strip()
        if confirm == 'yes':
            marks.clear()
            print("All records cleared successfully.")
        else:
            print("Action cancelled.")
            
    # 5. Exit
    elif choice == '5':
        print("Exiting application. Have a great day!")
        break
        
    else:
        print("Invalid choice! Please select an option from 1 to 5.")


#End of the program