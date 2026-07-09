# ------------------------------------------
# AI Engineer Bootcamp
# Day 7
# Program: Dictionary Example
# Author: Om Roy
# Date: 09-07-2026
#--------------------------------------------

# Dictionary store the key-value pair data

doctor = {
"id": "D1001",
"name": "Dr. Roy",
"department": "Cardiology"
}

print(doctor)

# output :
# {'id': 'D1001', 'name': 'Dr. Roy', 'department': 'Cardiology'}
print()
print("----Access Values----")
print(doctor["name"])
print(doctor["department"])

# output :
# Dr. Roy
#Cardiology

print()
print("-------Update Dictionary----------")
doctor["department"] = "Neurology"
print(doctor)

# output :
# -------Update Dictionary----------
# {'id': 'D1001', 'name': 'Dr. Roy', 'department': 'Neurology'}

print()
print("----------Add New Item--------")
doctor["experience"] = 12
print(doctor)

# output :
# ----------Add New Item--------
# {'id': 'D1001', 'name': 'Dr. Roy', 'department': 'Neurology', 'experience': 12}

print()
print("-----Loop Through Dictionary--------")
for key, value in doctor.items():
    print(key, ":", value)

# output :
# -----Loop Through Dictionary--------
# id : D1001
# name : Dr. Roy
# department : Neurology
# experience : 12    


# end of the program