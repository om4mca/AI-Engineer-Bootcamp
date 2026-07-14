file = open("student.txt", "r")

print(file.read())

file.close()

print()
print("-------append data--------")

file = open("student.txt", "a")

file.write("\nPython File Handling")

file.close()

print()
print("----Read Line by Line--------")
file = open("student.txt")

for line in file:
    print(line.strip())

file.close()



## with open()
print()
print("----with open()---------")
with open("student.txt", "r") as file:
    print(file.read())