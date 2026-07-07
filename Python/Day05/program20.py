# ------------------------------------------
# AI Engineer Bootcamp
# Day 5
# Program: Employee ID Generator (Loop Version)
# Author: Om Roy
# Date: 07-07-2026
#--------------------------------------------

# Start our ID counter at 1
id_counter = 1

print("=== Corporate Employee ID Generator ===")
print("Type 'exit' as the employee name when you are finished.\n")

while True:
    name = input("Enter Employee Full Name: ")
    
    # Check if the user wants to stop the generator
    if name.lower() == 'exit':
        print("\nClosing ID Generator. Goodbye!")
        break
        
    # Check if the input is empty or just spaces
    if name.strip() == "":
        print("❌ Name cannot be empty. Please try again.\n")
        continue

    # Clean up the name casing (e.g., "jane doe" -> "Jane Doe")
    formatted_name = name.title()

    # Generate the ID string padded with zeros up to 3 digits (e.g., '001')
    id_number_string = str(id_counter).zfill(3)
    employee_id = f"EMP-{id_number_string}"

    # Print the generated ID card details
    print("-----------------------------------")
    print(f"ID Created Successfully!")
    print(f"👤 Name: {formatted_name}")
    print(f"🆔 ID:   {employee_id}")
    print("-----------------------------------")

    # Increment the counter so the next employee gets the next number
    id_counter += 1


#End of the program