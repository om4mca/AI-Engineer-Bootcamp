# ------------------------------------------
# AI Engineer Bootcamp
# Day 4
# Program: BMI Category
# Author: Om Roy
# Date: 06-07-2026
# ------------------------------------------


weight = float(input("Enter your weight in kilograms (e.g., 70): "))
height = float(input("Enter your height in meters (e.g., 1.75): "))
    
    # 2. Validate input
if weight <= 0 or height <= 0:
        print("❌ Error: Weight and height must be positive numbers.")
else:
        # 3. Calculate BMI
        bmi = weight / (height ** 2)
        
        # 4. Determine the category
if bmi < 18.5:
            category = "Underweight"
elif bmi < 25.0:
            category = "Normal weight"
elif bmi < 30.0:
            category = "Overweight"
else:
            category = "Obese"
            
        # 5. Display results
print("\n--- Results ---")
print(f"Your BMI is: {bmi:.2f}")
print(f"Health Category: {category}")



#End of the program