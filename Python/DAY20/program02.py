# Automatically opens and closes the file
with open("data.txt", "w") as file:
    file.write("Patient ID: P101\nStatus: Active\n")

# File is guaranteed to be closed here
print("Is file closed?", file.closed)  # Returns: True