# ------------------------------------------
# AI Engineer Bootcamp
# Day 5
# Program: while loop Ex
# Author: Om Roy
# Date: 07-07-2026
#--------------------------------------------

count = 1

while count <= 5:
    print(count)
    count += 1

print()
# Break Ex
print("Break Statement")

for i in range(1, 11):

    if i == 6:
        break

    print(i)  
#Continue statement
print()
print("Continue Statement")
for i in range(1, 6):

    if i == 3:
        continue

    print(i)  

#pass statement
print()
print("Pass Statement")
for i in range(5):

    pass

print("Completed")

#Nested Loop
print()
print("nested loop")
for row in range(3):

    for column in range(4):

        print("*", end=" ")

    print()