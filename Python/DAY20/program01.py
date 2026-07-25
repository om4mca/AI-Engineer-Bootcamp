with open("sample.txt", "w") as file:
    file.write("Hello, World!")

# Check if the file closed automatically
print("Is file closed?", file.closed)  # Returns: True