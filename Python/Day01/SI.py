principal=float(input("Enter the principal amount : "))
rate=float(input("Enter the annual rate of interest (%) : "))
time=float(input("Enter the Time in Years : "))

simpleInterest= (principal * rate * time) / 100
print("\n -------------Calculation Results--------------")
print("Simple Interest : ", simpleInterest)