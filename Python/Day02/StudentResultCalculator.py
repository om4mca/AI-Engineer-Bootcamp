# ------------------------------------------
# AI Engineer Bootcamp
# Day 2
# Program: Student Result Calculator
# Author: Om Roy
# Date: 03-07-2026
# ------------------------------------------

#Highest Marks Subject
#Lowest Marks Subject
#Distinction (Percentage ≥ 75)
#Fail agar kisi bhi subject me marks < 33

name=input("Enter Student Name : ")
physics=int(input("Enter Physics Marks : "))
chemistry=int(input("Enter Chemistry Marks : "))
maths=int(input("Enter Maths Marks : "))
total=physics+chemistry+maths
percentage=(total/300)*100

highest_marks=max(physics, chemistry, maths)

if highest_marks==physics:
    highest_subject="Physics"   
elif highest_marks==chemistry:
    highest_subject="Chemistry"
else:
    highest_subject="Maths"

lowest_marks=min(physics, chemistry, maths)

if lowest_marks==physics:
    lowest_subject="Physics"
elif lowest_marks==chemistry:
    lowest_subject="Chemistry"
else:
    lowest_subject="Maths"




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
print("Highest Marks Subject : ", highest_subject)
print("Lowest Marks Subject : ", lowest_subject)

distinction="Yes" if percentage>=75 else "No"
print("Distinction : ", distinction)

fail="Yes" if physics<33 or chemistry<33 or maths<33 else "No"
print("Fail in any subject : ", fail)   






#End of the program