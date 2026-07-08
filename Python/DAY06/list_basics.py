# ------------------------------------------
# AI Engineer Bootcamp
# Day 6
# Program: List Basics
# Author: Om Roy
# Date: 08-07-2026
#--------------------------------------------

patients = ["Suraj", "Raj", "Om", "Kumar"]

print(patients)

print()
print("-------Create Lists-----------")
numbers = [10, 15, 20, 25, 50, 100]

print(numbers)

fruits = ["Apple", "Mango", "Orange"]

print(fruits)

mixed = [101, "Om", True, 95.5]

print(mixed)

print()
print("-------Access Elements-----------")

patients=["Ramesh","Sanjay","Diwakar","Rana"]
print(patients[0])
print(patients[1])
print(patients[2])
print(patients[3])

print()
print("-------Modify List-----------")

patients=["Ramesh","Sanjay","Diwakar","Rana"]
patients[1]="Sachin"
print(patients)

print()
print("-------List Methods-----------")
patients=[]
patients.append("Virat")
patients.append("Kohli")
print(patients)
patients.insert(1,"Om")
print(patients)
patients.remove("Om")
print(patients)
patients.pop()
print(patients)
patients.clear()
print(patients)

print()
print("---------Loop Through List-------------")
patients=["Ram","Shyam","Om","Diwakar","Sanjay"]
for patient in patients:
    print(patient)

print()
print("--------Search----------")
patients=["Ram","Shyam","Om","Diwakar","Sanjay"]

if "Om" in patients:
    print("Found")
else:
    print("Not Found")

patients=["Ram","Shyam","Om","Diwakar","Sanjay"]
print(len(patients))


#End of the program