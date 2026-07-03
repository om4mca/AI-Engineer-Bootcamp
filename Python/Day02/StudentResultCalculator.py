# ------------------------------------------
# AI Engineer Bootcamp
# Day 2
# Program: Student Result Calculator
# Author: Om Roy
# Date: 03-07-2026
# ------------------------------------------

name=input("Enter Student Name : ")
physics=int(input("Enter Physics Marks : "))
chemistry=int(input("Enter Chemistry Marks : "))
maths=int(input("Enter Maths Marks : "))
total=physics+chemistry+maths
percentage=(total/300)*100
grade=""
if percentage>=90:
    grade="A+"
elif percentage>=80:
    grade="A"
elif percentage>=70:
    grade="B"
elif percentage>=60:
    grade="C"
elif percentage>=50:
    grade="D"
else:
    grade="F"

result="Pass" if percentage>=50 else "Fail"

print()
print("*************Student Result*************")
print("----------------------------------------")
print("Student Name : ", name)
print("Total Marks : ", total)
print("Percentage : ", percentage)
print("Grade : ", grade)
print("Result : ", result)


#End of the program