
# ------------------------------------------
# AI Engineer Bootcamp
# Day 4
# Program: Hospital Registration Example
# Input Patient Name  Age  Gender  Department  Consultation Fee  Discount %
#Business Rule : Age<5  50% Discount Age>=60  30% Discount  Others No Discount
#Output : Patient Name  Department  Consultation Fee   Discount  Final Bill
# Author: Om Roy
# Date: 06-07-2026

name=input("Enter Patient Name : ")
age=int(input("Enter Age : "))
gender=input("Enter Gender : ")
department=input("Enter Department : ")
consultation_fee=float(input("Enter Consultation Fee : "))
discount_percent=float(input("Enter Discount % : "))
if age<5:
    discount=consultation_fee*50/100
elif age>=60:
    discount=consultation_fee*30/100
else:
    discount=0

final_bill=consultation_fee-discount

print()
print("--------------Hospital Registration Details--------------")

print("Patient Name:", name)
print("Department:", department)
print("Consultation Fee:", consultation_fee)
print("Discount:", discount)
print("Final Bill:", final_bill)

#End of the program